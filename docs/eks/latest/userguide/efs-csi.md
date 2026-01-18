**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use elastic file system storage with Amazon EFS

[Amazon Elastic File System](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") (Amazon EFS) provides serverless, fully elastic file storage so that you can share file data without provisioning or managing storage capacity and performance. The [Amazon EFS Container Storage Interface (CSI) driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver "https://github.com/kubernetes-sigs/aws-efs-csi-driver") provides a CSI interface that allows Kubernetes clusters running on AWS to manage the lifecycle of Amazon EFS file systems. This topic shows you how to deploy the Amazon EFS CSI driver to your Amazon EKS cluster.

## Considerations

- The Amazon EFS CSI driver isn’t compatible with Windows-based container images.
- You can’t use [dynamic provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/dynamic_provisioning/README.md "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/dynamic_provisioning/README.md") for persistent volumes with Fargate nodes, but you can use [static provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/static_provisioning/README.md "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/static_provisioning/README.md").
- [Dynamic provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/dynamic_provisioning/README.md "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/dynamic_provisioning/README.md") requires [1.2](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-1.x.md#v12 "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-1.x.md#v12") or later of the driver. You can use [static provisioning](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/static_provisioning/README.md "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/static_provisioning/README.md") for persistent volumes using version `1.1` of the driver on any supported Amazon EKS cluster version (see [Amazon EKS supported versions](kubernetes-versions.md "kubernetes-versions.md")).
- Version [1.3.2](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-1.x.md#v132 "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-1.x.md#v132") or later of this driver supports the Arm64 architecture, including Amazon EC2 Graviton-based instances.
- Version [1.4.2](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-1.x.md#v142 "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-1.x.md#v142") or later of this driver supports using FIPS for mounting file systems.
- Take note of the resource quotas for Amazon EFS. For example, there’s a quota of 1000 access points that can be created for each Amazon EFS file system. For more information, see [Amazon EFS resource quotas that you cannot change](../../../efs/latest/ug/limits.md#limits-efs-resources-per-account-per-region "../../../efs/latest/ug/limits.md#limits-efs-resources-per-account-per-region").
- Starting in version [2.0.0](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-2.x.md#v200 "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-2.x.md#v200"), this driver switched from using `stunnel` to `efs-proxy` for TLS connections. When `efs-proxy` is used, it will open a number of threads equal to one plus the number of cores for the node it’s running on.
- The Amazon EFS CSI driver isn’t compatible with Amazon EKS Hybrid Nodes.

## Prerequisites

- The Amazon EFS CSI driver needs AWS Identity and Access Management (IAM) permissions.
  - AWS suggests using EKS Pod Identities. For more information, see [Overview of setting up EKS Pod Identities](pod-identities.md#pod-id-setup-overview "pod-identities.md#pod-id-setup-overview").
  - For information about IAM roles for service accounts and setting up an IAM OpenID Connect (OIDC) provider for your cluster, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").

- Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quick configuration with aws configure](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") in the _AWS Command Line Interface User Guide_. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software "../../../cloudshell/latest/userguide/vm-specs.md#install-cli-software") in the _AWS CloudShell User Guide_.
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").

###### Note

A Pod running on Fargate automatically mounts an Amazon EFS file system, without needing manual driver installation steps.

## Step 1: Create an IAM role

The Amazon EFS CSI driver requires IAM permissions to interact with your file system. Create an IAM role and attach the required AWS managed policy to it. To implement this procedure, you can use one of these tools:

- [eksctl](#eksctl_efs_store_app_data "#eksctl_efs_store_app_data")
- [AWS Management Console](#console_efs_store_app_data "#console_efs_store_app_data")
- [AWS CLI](#awscli_efs_store_app_data "#awscli_efs_store_app_data")

###### Note

The specific steps in this procedure are written for using the driver as an Amazon EKS add-on. For details on self-managed installations, see [Set up driver permission](https://github.com/kubernetes-sigs/aws-efs-csi-driver#set-up-driver-permission "https://github.com/kubernetes-sigs/aws-efs-csi-driver#set-up-driver-permission") on GitHub.

### `eksctl`

#### If using Pod Identities

Run the following commands to create an IAM role and Pod Identity association with `eksctl`. Replace `my-cluster` with your cluster name. You can also replace `AmazonEKS_EFS_CSI_DriverRole` with a different name.

```
 export cluster_name=my-cluster
export role_name=AmazonEKS_EFS_CSI_DriverRole
eksctl create podidentityassociation \
    --service-account-name efs-csi-controller-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name $role_name \
    --permission-policy-arns <shared id="region.arn"/>iam::aws:policy/service-role/AmazonEFSCSIDriverPolicy
```

#### If using IAM roles for service accounts

Run the following commands to create an IAM role with `eksctl`. Replace `my-cluster` with your cluster name. You can also replace `AmazonEKS_EFS_CSI_DriverRole` with a different name.

```
 export cluster_name=my-cluster
export role_name=AmazonEKS_EFS_CSI_DriverRole
eksctl create iamserviceaccount \
    --name efs-csi-controller-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name $role_name \
    --role-only \
    --attach-policy-arn <shared id="region.arn"/>iam::aws:policy/service-role/AmazonEFSCSIDriverPolicy \
    --approve
TRUST_POLICY=$(aws iam get-role --output json --role-name $role_name --query 'Role.AssumeRolePolicyDocument' | \
    sed -e 's/efs-csi-controller-sa/efs-csi-*/' -e 's/StringEquals/StringLike/')
aws iam update-assume-role-policy --role-name $role_name --policy-document "$TRUST_POLICY"
```

### AWS Management Console

Run the following to create an IAM role with AWS Management Console.

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. On the **Roles** page, choose **Create role**.
4. On the **Select trusted entity** page, do the following:
   1. If using EKS Pod Identities:
      1. In the **Trusted entity type** section, choose **AWS service**.
      2. In the **Service or use case** drop down, choose **EKS**.
      3. In the **Use case** section, choose **EKS - Pod Identity**.
      4. Choose **Next**.

   2. If using IAM roles for service accounts:
      1. In the **Trusted entity type** section, choose **Web identity**.
      2. For **Identity provider**, choose the **OpenID Connect provider URL** for your cluster (as shown under **Overview** in Amazon EKS).
      3. For **Audience**, choose `sts.amazonaws.com`.
      4. Choose **Next**.

5. On the **Add permissions** page, do the following:
   1. In the **Filter policies** box, enter `AmazonEFSCSIDriverPolicy`.
   2. Select the check box to the left of the `AmazonEFSCSIDriverPolicy` returned in the search.
   3. Choose **Next**.

6. On the **Name, review, and create** page, do the following:
   1. For **Role name**, enter a unique name for your role, such as `AmazonEKS_EFS_CSI_DriverRole`.
   2. Under **Add tags (Optional)**, add metadata to the role by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
   3. Choose **Create role**.

7. After the role is created:
   1. If using EKS Pod Identities:
      1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
      2. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to configure the EKS Pod Identity association for.
      3. Choose the **Access** tab.
      4. In **Pod Identity associations**, choose **Create**.
      5. Choose the **IAM role** dropdown and select your newly created role.
      6. Choose the **Kubernetes namespace** field and input `kube-system`.
      7. Choose the **Kubernetes service account** field and input `efs-csi-controller-sa`.
      8. Choose **Create**.
      9. For more information on creating Pod Identity associations, see [Create a Pod Identity association (AWS Console)](pod-id-association.md#pod-id-association-create "pod-id-association.md#pod-id-association-create").

   2. If using IAM roles for service accounts:
      1. Choose the role to open it for editing.
      2. Choose the **Trust relationships** tab, and then choose **Edit trust policy**.
      3. Find the line that looks similar to the following line:

      ```
       "oidc.eks.region-code.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:aud": "sts.amazonaws.com"
      ```

      Add the following line above the previous line. Replace `<region-code>` with the AWS Region that your cluster is in. Replace `<EXAMPLED539D4633E53DE1B71EXAMPLE>` with your cluster’s OIDC provider ID.

      ```
       "oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:sub": "system:serviceaccount:kube-system:efs-csi-*",
      ```

      4. Modify the `Condition` operator from `"StringEquals"` to `"StringLike"`.
      5. Choose **Update policy** to finish.

### AWS CLI

Run the following commands to create an IAM role with AWS CLI.

#### If using Pod Identities

1. Create the IAM role that grants the `AssumeRole` and `TagSession` actions to the `pods.eks.amazonaws.com` service.
   1. Copy the following contents to a file named `aws-efs-csi-driver-trust-policy-pod-identity.json`.

   ```
    {
       "Version":"2012-10-17",
       "Statement": [
           {
               "Sid": "AllowEksAuthToAssumeRoleForPodIdentity",
               "Effect": "Allow",
               "Principal": {
                   "Service": "pods.eks.amazonaws.com"
               },
               "Action": [
                   "sts:AssumeRole",
                   "sts:TagSession"
               ]
           }
       ]
   }
   ```

   2. Create the role. Replace `my-cluster` with your cluster name. You can also replace `AmazonEKS_EFS_CSI_DriverRole` with a different name.

   ```
    export cluster_name=my-cluster
   export role_name=AmazonEKS_EFS_CSI_DriverRole
   aws iam create-role \
     --role-name $role_name \
     --assume-role-policy-document file://"aws-efs-csi-driver-trust-policy-pod-identity.json"
   ```

2. Attach the required AWS managed policy to the role with the following command.

```
 aws iam attach-role-policy \
  --policy-arn <shared id="region.arn"/>iam::aws:policy/service-role/AmazonEFSCSIDriverPolicy \
  --role-name $role_name
```

3. Run the following command to create the Pod Identity association. Replace `arn:aws:iam::<111122223333>:role/my-role` with the role created in previous steps.

```
aws eks create-pod-identity-association --cluster-name $cluster_name --role-arn {arn-aws}iam::<111122223333>:role/my-role --namespace kube-system --service-account efs-csi-controller-sa
```

4. For more information on creating Pod Identity associations, see [Create a Pod Identity association (AWS Console)](pod-id-association.md#pod-id-association-create "pod-id-association.md#pod-id-association-create").

#### If using IAM roles for service accounts

1. View your cluster’s OIDC provider URL. Replace `my-cluster` with your cluster name. You can also replace `AmazonEKS_EFS_CSI_DriverRole` with a different name.

```
 export cluster_name=my-cluster
export role_name=AmazonEKS_EFS_CSI_DriverRole
aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text
```

An example output is as follows.

```
 https://oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>
```

If the output from the command is `None`, review the **Prerequisites**. 2. Create the IAM role that grants the `AssumeRoleWithWebIdentity` action.

    1. Copy the following contents to a file named `aws-efs-csi-driver-trust-policy.json`. Replace `<111122223333>` with your account ID. Replace `<EXAMPLED539D4633E53DE1B71EXAMPLE>` and `<region-code>` with the values returned in the previous step.



    ```
     {
      "Version":"2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::123456789012:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringLike": {
              "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:kube-system:efs-csi-*",
              "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
            }
          }
        }
      ]
    }
    ```
    2. Create the role.



    ```
     aws iam create-role \
      --role-name $role_name \
      --assume-role-policy-document file://"aws-efs-csi-driver-trust-policy.json"
    ```

3. Attach the required AWS managed policy to the role with the following command.

```
 aws iam attach-role-policy \
  --policy-arn <shared id="region.arn"/>iam::aws:policy/service-role/AmazonEFSCSIDriverPolicy \
  --role-name $role_name
```

## Step 2: Get the Amazon EFS CSI driver

We recommend that you install the Amazon EFS CSI driver through the Amazon EKS add-on. To add an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md"). If you’re unable to use the Amazon EKS add-on, we encourage you to submit an issue about why you can’t to the [Containers roadmap GitHub repository](https://github.com/aws/containers-roadmap/issues "https://github.com/aws/containers-roadmap/issues").

###### Important

Before adding the Amazon EFS driver as an Amazon EKS add-on, confirm that you don’t have a self-managed version of the driver installed on your cluster. If so, see [Uninstalling the Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#uninstalling-the-amazon-efs-csi-driver "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#uninstalling-the-amazon-efs-csi-driver") on GitHub.

Alternatively, if you want a self-managed installation of the Amazon EFS CSI driver, see [Installation](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#installation "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#installation") on GitHub.

## Step 3: Create an Amazon EFS file system

To create an Amazon EFS file system, see [Create an Amazon EFS file system for Amazon EKS](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/efs-create-filesystem.md "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/efs-create-filesystem.md") on GitHub.

## Step 4: Deploy a sample application

You can deploy a variety of sample apps and modify them as needed. For more information, see [Examples](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#examples "https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/README.md#examples") on GitHub.
