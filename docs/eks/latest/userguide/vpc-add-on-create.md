**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Create the Amazon VPC CNI (Amazon EKS add-on)

Use the following steps to create the Amazon VPC CNI plugin for Kubernetes Amazon EKS add-on.

Before you begin, review the considerations. For more information, see [Considerations](managing-vpc-cni.md#manage-vpc-cni-add-on-on-considerations "managing-vpc-cni.md#manage-vpc-cni-add-on-on-considerations").

## Prerequisites

The following are prerequisites for the Amazon VPC CNI plugin for Kubernetes Amazon EKS add-on.

- An existing Amazon EKS cluster. To deploy one, see [Get started with Amazon EKS](getting-started.md "getting-started.md").
- An existing AWS Identity and Access Management (IAM) OpenID Connect (OIDC) provider for your cluster. To determine whether you already have one, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").
- An IAM role with the [AmazonEKS_CNI_Policy](../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md "../../../aws-managed-policy/latest/reference/AmazonEKS_CNI_Policy.md") IAM policy (if your cluster uses the `IPv4` family) or an IPv6 policy (if your cluster uses the `IPv6` family) attached to it. For more information about the VPC CNI role, see [Configure Amazon VPC CNI plugin to use IRSA](cni-iam-role.md "cni-iam-role.md"). For information about the IPv6 policy, see [Create IAM policy for clusters that use the IPv6 family](cni-iam-role.md#cni-iam-role-create-ipv6-policy "cni-iam-role.md#cni-iam-role-create-ipv6-policy").

###### Important

Amazon VPC CNI plugin for Kubernetes versions `v1.16.0` to `v1.16.1` implement CNI specification version `v1.0.0`. For more information about `v1.0.0` of the CNI spec, see [Container Network Interface (CNI) Specification](https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md "https://github.com/containernetworking/cni/blob/spec-v1.0.0/SPEC.md") on GitHub.

## Procedure

After you complete the prerequisites, use the following steps to create the add-on.

1. See which version of the add-on is installed on your cluster.

```
kubectl describe daemonset aws-node --namespace kube-system | grep amazon-k8s-cni: | cut -d : -f 3
```

An example output is as follows.

```
v1.16.4-eksbuild.2
```

2. See which type of the add-on is installed on your cluster. Depending on the tool that you created your cluster with, you might not currently have the Amazon EKS add-on type installed on your cluster. Replace `my-cluster` with the name of your cluster.

```
aws eks describe-addon --cluster-name my-cluster --addon-name vpc-cni --query addon.addonVersion --output text
```

If a version number is returned, you have the Amazon EKS type of the add-on installed on your cluster and don’t need to complete the remaining steps in this procedure. If an error is returned, you don’t have the Amazon EKS type of the add-on installed on your cluster. Complete the remaining steps of this procedure to install it. 3. Save the configuration of your currently installed add-on.

```
kubectl get daemonset aws-node -n kube-system -o yaml > aws-k8s-cni-old.yaml
```

4. Create the add-on using the AWS CLI. If you want to use the AWS Management Console or `eksctl` to create the add-on, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md") and specify `vpc-cni` for the add-on name. Copy the command that follows to your device. Make the following modifications to the command, as needed, and then run the modified command.
   - Replace `my-cluster` with the name of your cluster.
   - Replace `v1.20.3-eksbuild.1` with the latest version listed in the latest version table for your cluster version. For the latest version table, see [Amazon VPC CNI versions](managing-vpc-cni.md#vpc-cni-latest-available-version "managing-vpc-cni.md#vpc-cni-latest-available-version").
   - Replace `111122223333` with your account ID and `AmazonEKSVPCCNIRole` with the name of an [existing IAM role](cni-iam-role.md#cni-iam-role-create-role "cni-iam-role.md#cni-iam-role-create-role") that you’ve created. Specifying a role requires that you have an IAM OpenID Connect (OIDC) provider for your cluster. To determine whether you have one for your cluster, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").

   ```
   aws eks create-addon --cluster-name my-cluster --addon-name vpc-cni --addon-version v1.20.3-eksbuild.1 \
       --service-account-role-arn arn:aws:iam::111122223333:role/AmazonEKSVPCCNIRole
   ```

   If you’ve applied custom settings to your current add-on that conflict with the default settings of the Amazon EKS add-on, creation might fail. If creation fails, you receive an error that can help you resolve the issue. Alternatively, you can add `--resolve-conflicts OVERWRITE` to the previous command. This allows the add-on to overwrite any existing custom settings. Once you’ve created the add-on, you can update it with your custom settings.

5. Confirm that the latest version of the add-on for your cluster’s Kubernetes version was added to your cluster. Replace `my-cluster` with the name of your cluster.

```
aws eks describe-addon --cluster-name my-cluster --addon-name vpc-cni --query addon.addonVersion --output text
```

It might take several seconds for add-on creation to complete.

An example output is as follows.

```
v1.20.3-eksbuild.1
```

6. If you made custom settings to your original add-on, before you created the Amazon EKS add-on, use the configuration that you saved in a previous step to update the EKS add-on with your custom settings. Follow the steps in [Update the Amazon VPC CNI (Amazon EKS add-on)](vpc-add-on-update.md "vpc-add-on-update.md").
7. (Optional) Install the `cni-metrics-helper` to your cluster. It scrapes elastic network interface and IP address information, aggregates it at a cluster level, and publishes the metrics to Amazon CloudWatch. For more information, see [cni-metrics-helper](https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md "https://github.com/aws/amazon-vpc-cni-k8s/blob/master/cmd/cni-metrics-helper/README.md") on GitHub.
