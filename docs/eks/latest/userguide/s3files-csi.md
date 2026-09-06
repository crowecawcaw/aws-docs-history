

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use Amazon S3 file system storage with the Amazon EFS CSI driver
<a name="s3files-csi"></a>

S3 Files is a shared file system that connects any AWS compute directly with your data in Amazon S3. It provides fast, direct access to all of your S3 data as files with full file system semantics and low-latency performance, without your data ever leaving S3. That means file-based applications, agents, and teams can access and work with S3 data as a file system using the tools they already depend on. The [Amazon EFS Container Storage Interface (CSI) driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver) allows Kubernetes clusters running on AWS to mount Amazon S3 file systems as persistent volumes starting from version [3.0.0](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-3.x.md#v300). This topic shows you how to use the Amazon EFS CSI driver to manage Amazon S3 file systems on your Amazon EKS cluster.

## Considerations
<a name="s3files-csi-considerations"></a>
+ The Amazon EFS CSI driver isn’t compatible with Windows-based container images.
+ EKS Fargate doesn’t support S3 Files.
+ The Amazon EFS CSI driver isn’t compatible with Amazon EKS Hybrid Nodes.
+ Amazon S3 Files support in Amazon EFS CSI driver starts from version [3.0.0](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/CHANGELOG-3.x.md#v300).

## Prerequisites
<a name="s3files-csi-prereqs"></a>
+ The Amazon EFS CSI driver needs AWS Identity and Access Management (IAM) permissions.
  +  AWS suggests using EKS Pod Identities. For more information, see [Overview of setting up EKS Pod Identities](pod-identities.md#pod-id-setup-overview).
  + For information about IAM roles for service accounts and setting up an IAM OpenID Connect (OIDC) provider for your cluster, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md).
+ Version `2.12.3` or later or version `1.27.160` or later of the AWS Command Line Interface (AWS CLI) installed and configured on your device or AWS CloudShell. To check your current version, use `aws --version | cut -d / -f2 | cut -d ' ' -f1`. Package managers such as `yum`, `apt-get`, or Homebrew for macOS are often several versions behind the latest version of the AWS CLI. To install the latest version, see [Installing](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) and [Quick configuration with aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config) in the * AWS Command Line Interface User Guide*. The AWS CLI version that is installed in AWS CloudShell might also be several versions behind the latest version. To update it, see [Installing AWS CLI to your home directory](https://docs.aws.amazon.com/cloudshell/latest/userguide/vm-specs.html#install-cli-software) in the * AWS CloudShell User Guide*.
+ The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up `kubectl` and `eksctl`](install-kubectl.md).

## Step 1: Create IAM roles
<a name="s3files-create-iam-resources"></a>

The Amazon EFS CSI driver requires IAM permissions to interact with your file system. The EFS CSI driver uses two service accounts with separate IAM roles:
+  `efs-csi-controller-sa` — used by the controller, requires `AmazonS3FilesCSIDriverPolicy` and `AmazonS3FilesClientFullAccess`.
+  `efs-csi-node-sa` — used by the node daemonset, requires:
  +  `AmazonS3FilesClientFullAccess` — grants permissions to mount and write to S3 file systems (`s3files:ClientMount`, `s3files:ClientWrite`, `s3files:ClientRootAccess`).
  +  `AmazonS3ReadOnlyAccess` — enables streaming reads directly from your S3 bucket for higher throughput.
  +  `AmazonElasticFileSystemsUtils` — enables publishing efs-utils logs to Amazon CloudWatch for visibility into mount operations and easier troubleshooting.

**Note**  
If you want to use both Amazon S3 file system and Amazon EFS storage, you must attach both the `AmazonS3FilesCSIDriverPolicy` and the `AmazonEFSCSIDriverPolicy` managed policies to the controller role. For more information about Amazon EFS storage, see [Use elastic file system storage with Amazon EFS](efs-csi.md).

To implement this procedure, you can use one of these tools:
+  [`eksctl`](#eksctl_s3files_store_app_data) 
+  [AWS Management Console](#console_s3files_store_app_data) 
+  [AWS CLI](#awscli_s3files_store_app_data) 

**Note**  
The specific steps in this procedure are written for using the driver as an Amazon EKS add-on. For details on self-managed installations, see [Set up driver permission](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/install.md#set-up-driver-permission) on GitHub.

### `eksctl`
<a name="eksctl_s3files_store_app_data"></a>

#### If using Pod Identities
<a name="s3files-eksctl-pod-identities"></a>

Run the following commands to create IAM roles and Pod Identity associations with `eksctl`. Replace {{my-cluster}} with your value.

```
export cluster_name=my-cluster

# Create the controller role
eksctl create podidentityassociation \
    --service-account-name efs-csi-controller-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name AmazonEKS_EFS_CSI_ControllerRole \
    --permission-policy-arns arn:aws:iam::aws:policy/service-role/AmazonS3FilesCSIDriverPolicy,arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess

# Create the node role
eksctl create podidentityassociation \
    --service-account-name efs-csi-node-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name AmazonEKS_EFS_CSI_NodeRole \
    --permission-policy-arns arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess,arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess,arn:aws:iam::aws:policy/AmazonElasticFileSystemsUtils
```

#### If using IAM roles for service accounts
<a name="s3files-eksctl-irsa"></a>

Run the following commands to create IAM roles with `eksctl`. Replace {{my-cluster}} with your cluster name and {{region-code}} with your AWS Region code.

```
export cluster_name=my-cluster
export region_code=region-code

# Create the controller role
export controller_role_name=AmazonEKS_EFS_CSI_ControllerRole
eksctl create iamserviceaccount \
    --name efs-csi-controller-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name $controller_role_name \
    --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonS3FilesCSIDriverPolicy \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess \
    --approve \
    --region $region_code

# Create the node role
export node_role_name=AmazonEKS_EFS_CSI_NodeRole
eksctl create iamserviceaccount \
    --name efs-csi-node-sa \
    --namespace kube-system \
    --cluster $cluster_name \
    --role-name $node_role_name \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
    --attach-policy-arn arn:aws:iam::aws:policy/AmazonElasticFileSystemsUtils \
    --approve \
    --region $region_code
```

### AWS Management Console
<a name="console_s3files_store_app_data"></a>

Run the following to create an IAM role with AWS Management Console.

1. Open the IAM console at https://console.aws.amazon.com/iam/.

1. In the left navigation pane, choose **Roles**.

1. On the **Roles** page, choose **Create role**.

1. On the **Select trusted entity** page, do the following:

   1. If using EKS Pod Identities:

      1. In the **Trusted entity type** section, choose ** AWS service**.

      1. In the **Service or use case** drop down, choose **EKS**.

      1. In the **Use case** section, choose **EKS - Pod Identity**.

      1. Choose **Next**.

   1. If using IAM roles for service accounts:

      1. In the **Trusted entity type** section, choose **Web identity**.

      1. For **Identity provider**, choose the **OpenID Connect provider URL** for your cluster (as shown under **Overview** in Amazon EKS).

      1. For **Audience**, choose `sts.amazonaws.com`.

      1. Choose **Next**.

1. On the **Add permissions** page, do the following:

   1. In the **Filter policies** box, enter `AmazonS3FilesCSIDriverPolicy`. Select the check box to the left of the policy returned in the search. Then search for and select `AmazonS3FilesClientFullAccess`.

   1. Choose **Next**.

1. On the **Name, review, and create** page, do the following:

   1. For **Role name**, enter a unique name for your role, such as `AmazonEKS_EFS_CSI_ControllerRole`.

   1. Under **Add tags (Optional)**, add metadata to the role by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html) in the *IAM User Guide*.

   1. Choose **Create role**.

1. After the role is created:

   1. If using EKS Pod Identities:

      1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters).

      1. In the left navigation pane, select **Clusters**, and then select the name of the cluster that you want to configure the EKS Pod Identity association for.

      1. Choose the **Access** tab.

      1. In **Pod Identity associations**, choose **Create**.

      1. Choose the **IAM role** dropdown and select your newly created role.

      1. Choose the **Kubernetes namespace** field and input `kube-system`.

      1. Choose the **Kubernetes service account** field and input `efs-csi-controller-sa`.

      1. Choose **Create**.

      1. For more information on creating Pod Identity associations, see [Create a Pod Identity association (AWS Console)](pod-id-association.md#pod-id-association-create).

      1. Repeat the above steps to create a second role for the node service account. On the **Add permissions** page, attach `AmazonS3FilesClientFullAccess`, `AmazonS3ReadOnlyAccess` and `AmazonElasticFileSystemsUtils` instead. Then create a Pod Identity association with `efs-csi-node-sa` for the **Kubernetes service account** field.

   1. If using IAM roles for service accounts:

      1. Choose the role to open it for editing.

      1. Choose the **Trust relationships** tab, and then choose **Edit trust policy**.

      1. Find the line that looks similar to the following line:

         ```
         "oidc.eks.region-code.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:aud": "sts.amazonaws.com"
         ```

         Add the following line above the previous line. Replace `<region-code>` with the AWS Region that your cluster is in. Replace `<EXAMPLED539D4633E53DE1B71EXAMPLE>` with your cluster’s OIDC provider ID.

         ```
         "oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:sub": "system:serviceaccount:kube-system:efs-csi-controller-sa",
         ```

      1. Choose **Update policy** to finish.

      1. Repeat the above steps to create a second role for the node service account. On the **Add permissions** page, attach `AmazonS3FilesClientFullAccess`, `AmazonS3ReadOnlyAccess` and `AmazonElasticFileSystemsUtils` instead. In the trust policy, use `efs-csi-node-sa` for the `:sub` condition value.

### AWS CLI
<a name="awscli_s3files_store_app_data"></a>

Run the following commands to create IAM roles with AWS CLI.

#### If using Pod Identities
<a name="s3files-cli-pod-identities"></a>

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

   1. Create the role. Replace {{my-cluster}} with your cluster name.

      ```
      export cluster_name=my-cluster
      export controller_role_name=AmazonEKS_EFS_CSI_ControllerRole
      aws iam create-role \
        --role-name $controller_role_name \
        --assume-role-policy-document file://"aws-efs-csi-driver-trust-policy-pod-identity.json"
      ```

1. Attach the required AWS managed policies to the controller role.

   ```
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/service-role/AmazonS3FilesCSIDriverPolicy \
     --role-name $controller_role_name
   
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess \
     --role-name $controller_role_name
   ```

1. Create the node IAM role using the same trust policy.

   ```
   export node_role_name=AmazonEKS_EFS_CSI_NodeRole
   aws iam create-role \
     --role-name $node_role_name \
     --assume-role-policy-document file://"aws-efs-csi-driver-trust-policy-pod-identity.json"
   ```

1. Attach the required AWS managed policies to the node role.

   ```
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess \
     --role-name $node_role_name
   
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
     --role-name $node_role_name
   
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonElasticFileSystemsUtils \
     --role-name $node_role_name
   ```

1. Run the following commands to create the Pod Identity associations. Replace `<111122223333>` with your account ID.

   ```
   aws eks create-pod-identity-association --cluster-name $cluster_name --role-arn {arn-aws}iam::<111122223333>:role/$controller_role_name --namespace kube-system --service-account efs-csi-controller-sa
   aws eks create-pod-identity-association --cluster-name $cluster_name --role-arn {arn-aws}iam::<111122223333>:role/$node_role_name --namespace kube-system --service-account efs-csi-node-sa
   ```

1. For more information on creating Pod Identity associations, see [Create a Pod Identity association (AWS Console)](pod-id-association.md#pod-id-association-create).

#### If using IAM roles for service accounts
<a name="s3files-cli-irsa"></a>

1. View your cluster’s OIDC provider URL. Replace {{my-cluster}} with your cluster name.

   ```
   export cluster_name=my-cluster
   aws eks describe-cluster --name $cluster_name --query "cluster.identity.oidc.issuer" --output text
   ```

   An example output is as follows.

   ```
   https://oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>
   ```

   If the output from the command is `None`, review the **Prerequisites**.

1. Create the IAM role for the controller service account.

   1. Copy the following contents to a file named `controller-trust-policy.json`. Replace `<111122223333>` with your account ID. Replace `<EXAMPLED539D4633E53DE1B71EXAMPLE>` and `<region-code>` with the values returned in the previous step.

      ```
      {
          "Version": "2012-10-17", 		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Federated": "arn:aws:iam::<111122223333>:oidc-provider/oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>"
                  },
                  "Action": "sts:AssumeRoleWithWebIdentity",
                  "Condition": {
                      "StringEquals": {
                          "oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:aud": "sts.amazonaws.com",
                          "oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:sub": "system:serviceaccount:kube-system:efs-csi-controller-sa"
                      }
                  }
              }
          ]
      }
      ```

   1. Create the role.

      ```
      export controller_role_name=AmazonEKS_EFS_CSI_ControllerRole
      aws iam create-role \
        --role-name $controller_role_name \
        --assume-role-policy-document file://"controller-trust-policy.json"
      ```

1. Attach the required AWS managed policies to the controller role.

   ```
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/service-role/AmazonS3FilesCSIDriverPolicy \
     --role-name $controller_role_name
   
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess \
     --role-name $controller_role_name
   ```

1. Create the IAM role for the node service account.

   1. Copy the following contents to a file named `node-trust-policy.json`. Replace `<111122223333>` with your account ID. Replace `<EXAMPLED539D4633E53DE1B71EXAMPLE>` and `<region-code>` with the values returned in step 1.

      ```
      {
          "Version": "2012-10-17", 		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "Federated": "arn:aws:iam::<111122223333>:oidc-provider/oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>"
                  },
                  "Action": "sts:AssumeRoleWithWebIdentity",
                  "Condition": {
                      "StringEquals": {
                          "oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:sub": "system:serviceaccount:kube-system:efs-csi-node-sa",
                          "oidc.eks.<region-code>.amazonaws.com/id/<EXAMPLED539D4633E53DE1B71EXAMPLE>:aud": "sts.amazonaws.com"
                      }
                  }
              }
          ]
      }
      ```

   1. Create the role.

      ```
      export node_role_name=AmazonEKS_EFS_CSI_NodeRole
      aws iam create-role \
        --role-name $node_role_name \
        --assume-role-policy-document file://"node-trust-policy.json"
      ```

1. Attach the required AWS managed policies to the node role.

   ```
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3FilesClientFullAccess \
     --role-name $node_role_name
   
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess \
     --role-name $node_role_name
   
   aws iam attach-role-policy \
     --policy-arn arn:aws:iam::aws:policy/AmazonElasticFileSystemsUtils \
     --role-name $node_role_name
   ```

**Note**  
The `AmazonS3ReadOnlyAccess` policy grants read access to all S3 buckets. To constrain access to specific buckets, you can detach it and replace it with a tag-based inline policy. See [Amazon EFS CSI driver IAM policy documentation](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/iam-policy-create.md) on GitHub for details.

## Step 2: Get the Amazon EFS CSI driver
<a name="s3files-install-driver"></a>

We recommend that you install the Amazon EFS CSI driver through the Amazon EKS add-on. To add an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md). For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md). If you’re unable to use the Amazon EKS add-on, we encourage you to submit an issue about why you can’t to the [Containers roadmap GitHub repository](https://github.com/aws/containers-roadmap/issues).

**Important**  
Before adding the Amazon EFS driver as an Amazon EKS add-on, confirm that you don’t have a self-managed version of the driver installed on your cluster. If so, see [Uninstalling the Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/install.md#uninstalling-the-amazon-efs-csi-driver) on GitHub.

Alternatively, if you want a self-managed installation of the Amazon EFS CSI driver, see [Installation](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/install.md) on GitHub.

## Step 3: Create an Amazon S3 file system
<a name="s3files-create-filesystem"></a>

To create an Amazon S3 file system, see [Create an Amazon S3 file system for Amazon EKS](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/s3files-create-filesystem.md) on GitHub.

## Step 4: Deploy a sample application
<a name="s3files-sample-app"></a>

You can deploy a variety of sample apps and modify them as needed. For more information, see [Examples](https://github.com/kubernetes-sigs/aws-efs-csi-driver/tree/master/examples/kubernetes) on GitHub.