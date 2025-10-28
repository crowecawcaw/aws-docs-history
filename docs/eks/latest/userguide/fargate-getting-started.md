**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Get started with AWS Fargate for your cluster

This topic describes how to get started running Pods on AWS Fargate with your Amazon EKS cluster.

If you restrict access to the public endpoint of your cluster using CIDR blocks, we recommend that you also enable private endpoint access. This way, Fargate Pods can communicate with the cluster. Without the private endpoint enabled, the CIDR blocks that you specify for public access must include the outbound sources from your VPC. For more information, see [Cluster API server endpoint](cluster-endpoint.md "cluster-endpoint.md").

###### Prerequisite

An existing cluster. If you don’t already have an Amazon EKS cluster, see [Get started with Amazon EKS](getting-started.md "getting-started.md").

## Step 1: Ensure that existing nodes can communicate with Fargate Pods

If you’re working with a new cluster with no nodes, or a cluster with only managed node groups (see [Simplify node lifecycle with managed node groups](managed-node-groups.md "managed-node-groups.md")), you can skip to [Step 2: Create a Fargate Pod execution role](#fargate-sg-pod-execution-role "#fargate-sg-pod-execution-role").

Assume that you’re working with an existing cluster that already has nodes that are associated with it. Make sure that Pods on these nodes can communicate freely with the Pods that are running on Fargate. Pods that are running on Fargate are automatically configured to use the cluster security group for the cluster that they’re associated with. Ensure that any existing nodes in your cluster can send and receive traffic to and from the cluster security group. Managed node groups are automatically configured to use the cluster security group as well, so you don’t need to modify or check them for this compatibility (see [Simplify node lifecycle with managed node groups](managed-node-groups.md "managed-node-groups.md")).

For existing node groups that were created with `eksctl` or the Amazon EKS managed AWS CloudFormation templates, you can add the cluster security group to the nodes manually. Or, alternatively, you can modify the Auto Scaling group launch template for the node group to attach the cluster security group to the instances. For more information, see [Changing an instance’s security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SG_Changing_Group_Membership "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SG_Changing_Group_Membership") in the _Amazon VPC User Guide_.

You can check for a security group for your cluster in the AWS Management Console under the **Networking** section for the cluster. Or, you can do this using the following AWS CLI command. When using this command, replace `<my-cluster>` with the name of your cluster.

```
aws eks describe-cluster --name <my-cluster> --query cluster.resourcesVpcConfig.clusterSecurityGroupId
```

## Step 2: Create a Fargate Pod execution role

When your cluster creates Pods on AWS Fargate, the components that run on the Fargate infrastructure must make calls to AWS APIs on your behalf. The Amazon EKS Pod execution role provides the IAM permissions to do this. To create an AWS Fargate Pod execution role, see [Amazon EKS Pod execution IAM role](pod-execution-role.md "pod-execution-role.md").

###### Note

If you created your cluster with `eksctl` using the `--fargate` option, your cluster already has a Pod execution role that you can find in the IAM console with the pattern `eksctl-my-cluster-FargatePodExecutionRole-ABCDEFGHIJKL`. Similarly, if you use `eksctl` to create your Fargate profiles, `eksctl` creates your Pod execution role if one isn’t already created.

## Step 3: Create a Fargate profile for your cluster

Before you can schedule Pods that are running on Fargate in your cluster, you must define a Fargate profile that specifies which Pods use Fargate when they’re launched. For more information, see [Define which Pods use AWS Fargate when launched](fargate-profile.md "fargate-profile.md").

###### Note

If you created your cluster with `eksctl` using the `--fargate` option, then a Fargate profile is already created for your cluster with selectors for all Pods in the `kube-system` and `default` namespaces. Use the following procedure to create Fargate profiles for any other namespaces you would like to use with Fargate.

You can create a Fargate profile using either of these tools:

- [eksctl](#eksctl_fargate_profile_create "#eksctl_fargate_profile_create")
- [AWS Management Console](#console_fargate_profile_create "#console_fargate_profile_create")

### `eksctl`

This procedure requires `eksctl` version `0.215.0` or later. You can check your version with the following command:

```
eksctl version
```

For instructions on how to install or upgrade `eksctl`, see [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation.

**To create a Fargate profile with `eksctl`**

Create your Fargate profile with the following `eksctl` command, replacing every `<example value>` with your own values. You’re required to specify a namespace. However, the `--labels` option isn’t required.

```
eksctl create fargateprofile \
    --cluster <my-cluster> \
    --name <my-fargate-profile> \
    --namespace <my-kubernetes-namespace> \
    --labels <key=value>
```

You can use certain wildcards for `<my-kubernetes-namespace>` and `<key=value>` labels. For more information, see [Fargate profile wildcards](fargate-profile.md#fargate-profile-wildcards "fargate-profile.md#fargate-profile-wildcards").

### AWS Management Console

**To create a Fargate profile with AWS Management Console**

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. Choose the cluster to create a Fargate profile for.
3. Choose the **Compute** tab.
4. Under **Fargate profiles**, choose **Add Fargate profile**.
5. On the **Configure Fargate profile** page, do the following:
   1. For **Name**, enter a name for your Fargate profile. The name must be unique.
   2. For **Pod execution role**, choose the Pod execution role to use with your Fargate profile. Only the IAM roles with the `eks-fargate-pods.amazonaws.com` service principal are shown. If you don’t see any roles listed, you must create one. For more information, see [Amazon EKS Pod execution IAM role](pod-execution-role.md "pod-execution-role.md").
   3. Modify the selected **Subnets** as needed.

   ###### Note

   Only private subnets are supported for Pods that are running on Fargate. 4. For **Tags**, you can optionally tag your Fargate profile. These tags don’t propagate to other resources that are associated with the profile such as Pods. 5. Choose **Next**.

6. On the **Configure Pod selection** page, do the following:
   1. For **Namespace**, enter a namespace to match for Pods.
      - You can use specific namespaces to match, such as `kube-system` or `default`.
      - You can use certain wildcards (for example, `prod-*`) to match multiple namespaces (for example, `prod-deployment` and `prod-test`). For more information, see [Fargate profile wildcards](fargate-profile.md#fargate-profile-wildcards "fargate-profile.md#fargate-profile-wildcards").

   2. (Optional) Add Kubernetes labels to the selector. Specifically add them to the one that the Pods in the specified namespace need to match.
      - You can add the label `infrastructure: fargate` to the selector so that only Pods in the specified namespace that also have the `infrastructure: fargate` Kubernetes label match the selector.
      - You can use certain wildcards (for example, `key?: value?`) to match multiple namespaces (for example, `keya: valuea` and `keyb: valueb`). For more information, see [Fargate profile wildcards](fargate-profile.md#fargate-profile-wildcards "fargate-profile.md#fargate-profile-wildcards").

   3. Choose **Next**.

7. On the **Review and create** page, review the information for your Fargate profile and choose **Create**.

## Step 4: Update CoreDNS

By default, CoreDNS is configured to run on Amazon EC2 infrastructure on Amazon EKS clusters. If you want to _only_ run your Pods on Fargate in your cluster, complete the following steps.

###### Note

If you created your cluster with `eksctl` using the `--fargate` option, then you can skip to [Next steps](#fargate-gs-next-steps "#fargate-gs-next-steps").

1. Create a Fargate profile for CoreDNS with the following command. Replace `<my-cluster>` with your cluster name, `<111122223333>` with your account ID, `<AmazonEKSFargatePodExecutionRole>` with the name of your Pod execution role, and `<000000000000000a>`, `<000000000000000b>`, and `<000000000000000c>` with the IDs of your private subnets. If you don’t have a Pod execution role, you must create one first (see [Step 2: Create a Fargate Pod execution role](#fargate-sg-pod-execution-role "#fargate-sg-pod-execution-role")).

###### Important

The role ARN can’t include a [path](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-friendly-names "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-friendly-names") other than `/`. For example, if the name of your role is `development/apps/AmazonEKSFargatePodExecutionRole`, you need to change it to `AmazonEKSFargatePodExecutionRole` when specifying the ARN for the role. The format of the role ARN must be `arn:aws:iam::<111122223333>:role/<AmazonEKSFargatePodExecutionRole>`.

```
aws eks create-fargate-profile \
    --fargate-profile-name coredns \
    --cluster-name <my-cluster> \
    --pod-execution-role-arn arn:aws:iam::<111122223333>:role/<AmazonEKSFargatePodExecutionRole> \
    --selectors namespace=kube-system,labels={k8s-app=kube-dns} \
    --subnets subnet-<000000000000000a> subnet-<000000000000000b> subnet-<000000000000000c>
```

2. Trigger a rollout of the `coredns` deployment.

```
kubectl rollout restart -n kube-system deployment coredns
```

## Next steps

- You can start migrating your existing applications to run on Fargate with the following workflow.
  1.  [Create a Fargate profile](fargate-profile.md#create-fargate-profile "fargate-profile.md#create-fargate-profile") that matches your application’s Kubernetes namespace and Kubernetes labels.
  2.  Delete and re-create any existing Pods so that they’re scheduled on Fargate. Modify the `<namespace>` and `<deployment-type>` to update your specific Pods.

  ```
  kubectl rollout restart -n <namespace> deployment <deployment-type>
  ```

- Deploy the [Route application and HTTP traffic with Application Load Balancers](alb-ingress.md "alb-ingress.md") to allow Ingress objects for your Pods running on Fargate.
- You can use the [Adjust pod resources with Vertical Pod Autoscaler](vertical-pod-autoscaler.md "vertical-pod-autoscaler.md") to set the initial correct size of CPU and memory for your Fargate Pods, and then use the [Scale pod deployments with Horizontal Pod Autoscaler](horizontal-pod-autoscaler.md "horizontal-pod-autoscaler.md") to scale those Pods. If you want the Vertical Pod Autoscaler to automatically re-deploy Pods to Fargate with higher CPU and memory combinations, set the Vertical Pod Autoscaler’s mode to either `Auto` or `Recreate`. This is to ensure correct functionality. For more information, see the [Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler#quick-start "https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler#quick-start") documentation on GitHub.
- You can set up the [AWS Distro for OpenTelemetry](https://aws.amazon.com/otel "https://aws.amazon.com/otel") (ADOT) collector for application monitoring by following [these instructions](../../../AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-otel.md "../../../AmazonCloudWatch/latest/monitoring/Container-Insights-EKS-otel.md").
