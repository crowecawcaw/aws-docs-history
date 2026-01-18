**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Install AWS Load Balancer Controller with Helm

###### Tip

With Amazon EKS Auto Mode, you don’t need to install or upgrade networking add-ons. Auto Mode includes pod networking and load balancing capabilities.

For more information, see [Automate cluster infrastructure with EKS Auto Mode](automode.md "automode.md").

This topic describes how to install the AWS Load Balancer Controller using Helm, a package manager for Kubernetes, and `eksctl`. The controller is installed with default options. For more information about the controller, including details on configuring it with annotations, see the [AWS Load Balancer Controller Documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/ "https://kubernetes-sigs.github.io/aws-load-balancer-controller/") on GitHub.

In the following steps, replace the example values with your own values.

## Prerequisites

Before starting this tutorial, you must complete the following steps:

- Create an Amazon EKS cluster. To create one, see [Get started with Amazon EKS](getting-started.md "getting-started.md").
- Install [Helm](https://helm.sh/docs/helm/helm_install/ "https://helm.sh/docs/helm/helm_install/") on your local machine.
- Make sure that your Amazon VPC CNI plugin for Kubernetes, `kube-proxy`, and CoreDNS add-ons are at the minimum versions listed in [Service account tokens](service-accounts.md#boundserviceaccounttoken-validated-add-on-versions "service-accounts.md#boundserviceaccounttoken-validated-add-on-versions").
- Learn about AWS Elastic Load Balancing concepts. For more information, see the [Elastic Load Balancing User Guide](../../../elasticloadbalancing/latest/userguide.md "../../../elasticloadbalancing/latest/userguide.md").
- Learn about Kubernetes [service](https://kubernetes.io/docs/concepts/services-networking/service/ "https://kubernetes.io/docs/concepts/services-networking/service/") and [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/ "https://kubernetes.io/docs/concepts/services-networking/ingress/") resources.

### Considerations

Before proceeding with the configuration steps on this page, consider the following:

- The IAM policy and role (`AmazonEKSLoadBalancerControllerRole`) can be reused across multiple EKS clusters in the same AWS account.
- If you’re installing the controller on the same cluster where the role (`AmazonEKSLoadBalancerControllerRole`) was originally created, go to [Step 2: Install Load Balancer Controller](#lbc-helm-install "#lbc-helm-install") after verifying the role exists.
- If you’re using IAM Roles for Service Accounts (IRSA), IRSA must be set up for each cluster, and the OpenID Connect (OIDC) provider ARN in the role’s trust policy is specific to each EKS cluster. Additionally, if you’re installing the controller on a new cluster with an existing `AmazonEKSLoadBalancerControllerRole`, update the role’s trust policy to include the new cluster’s OIDC provider and create a new service account with the appropriate role annotation. To determine whether you already have an OIDC provider, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").

## Step 1: Create IAM Role using `eksctl`

The following steps refer to the AWS Load Balancer Controller **v2.14.1** release version. For more information about all releases, see the [AWS Load Balancer Controller Release Page](https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/ "https://github.com/kubernetes-sigs/aws-load-balancer-controller/releases/") on GitHub.

1. Download an IAM policy for the AWS Load Balancer Controller that allows it to make calls to AWS APIs on your behalf.

```
 curl -O https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.14.1/docs/install/iam_policy.json
```

    * If you are a non-standard AWS partition, such as a Government or China region, [review the policies on GitHub](https://github.com/kubernetes-sigs/aws-load-balancer-controller/tree/main/docs/install "https://github.com/kubernetes-sigs/aws-load-balancer-controller/tree/main/docs/install") and download the appropriate policy for your region.

2. Create an IAM policy using the policy downloaded in the previous step.

```
 aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam_policy.json
```

###### Note

If you view the policy in the AWS Management Console, the console shows warnings for the **ELB** service, but not for the **ELB v2** service. This happens because some of the actions in the policy exist for **ELB v2**, but not for **ELB**. You can ignore the warnings for **ELB**. 3. Replace the values for cluster name, region code, and account ID.

```
 eksctl create iamserviceaccount \
    --cluster=<cluster-name> \
    --namespace=kube-system \
    --name=aws-load-balancer-controller \
    --attach-policy-arn=<shared id="region.arn"/>iam::<AWS_ACCOUNT_ID>:policy/AWSLoadBalancerControllerIAMPolicy \
    --override-existing-serviceaccounts \
    --region <aws-region-code> \
    --approve
```

## Step 2: Install AWS Load Balancer Controller

1. Add the `eks-charts` Helm chart repository. AWS maintains [this repository](https://github.com/aws/eks-charts "https://github.com/aws/eks-charts") on GitHub.

```
 helm repo add eks https://aws.github.io/eks-charts
```

2. Update your local repo to make sure that you have the most recent charts.

```
 helm repo update eks
```

3. Install the AWS Load Balancer Controller.

If you’re deploying the controller to Amazon EC2 nodes that have [restricted access to the Amazon EC2 instance metadata service (IMDS)](https://aws.github.io/aws-eks-best-practices/security/docs/iam/#restrict-access-to-the-instance-profile-assigned-to-the-worker-node "https://aws.github.io/aws-eks-best-practices/security/docs/iam/#restrict-access-to-the-instance-profile-assigned-to-the-worker-node"), or if you’re deploying to Fargate or Amazon EKS Hybrid Nodes, then add the following flags to the `helm` command that follows:

    * `--set region=`region-code``
    * `--set vpcId=`vpc-xxxxxxxx``



    Replace `my-cluster` with the name of your cluster. In the following command, `aws-load-balancer-controller` is the Kubernetes service account that you created in a previous step.


    For more information about configuring the helm chart, see [values.yaml](https://github.com/aws/eks-charts/blob/master/stable/aws-load-balancer-controller/values.yaml "https://github.com/aws/eks-charts/blob/master/stable/aws-load-balancer-controller/values.yaml") on GitHub.



    ```
     helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
      -n kube-system \
      --set clusterName=my-cluster \
      --set serviceAccount.create=false \
      --set serviceAccount.name=aws-load-balancer-controller \
      --version 1.14.0
    ```

###### Important

The deployed chart doesn’t receive security updates automatically. You need to manually upgrade to a newer chart when it becomes available. When upgrading, change `install` to `upgrade` in the previous command.

The `helm install` command automatically installs the custom resource definitions (CRDs) for the controller. The `helm upgrade` command does not. If you use `helm upgrade,` you must manually install the CRDs. Run the following command to install the CRDs:

```
 wget https://raw.githubusercontent.com/aws/eks-charts/master/stable/aws-load-balancer-controller/crds/crds.yaml
kubectl apply -f crds.yaml
```

## Step 3: Verify that the controller is installed

1. Verify that the controller is installed.

```
 kubectl get deployment -n kube-system aws-load-balancer-controller
```

An example output is as follows.

```
 NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
aws-load-balancer-controller   2/2     2            2           84s
```

You receive the previous output if you deployed using Helm. If you deployed using the Kubernetes manifest, you only have one replica. 2. Before using the controller to provision AWS resources, your cluster must meet specific requirements. For more information, see [Route application and HTTP traffic with Application Load Balancers](alb-ingress.md "alb-ingress.md") and [Route TCP and UDP traffic with Network Load Balancers](network-load-balancing.md "network-load-balancing.md").
