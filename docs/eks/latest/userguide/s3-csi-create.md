**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Deploy the Mountpoint for Amazon S3 driver

With the [Mountpoint for Amazon S3 Container Storage Interface (CSI) driver](https://github.com/awslabs/mountpoint-s3-csi-driver "https://github.com/awslabs/mountpoint-s3-csi-driver"), your Kubernetes applications can access Amazon S3 objects through a file system interface, achieving high aggregate throughput without changing any application code.

This procedure will show you how to deploy the [Mountpoint for Amazon S3 CSI Amazon EKS driver](s3-csi.md "s3-csi.md"). Before proceeding, please review the [Considerations](s3-csi.md#s3-csi-considerations "s3-csi.md#s3-csi-considerations").

## Prerequisites

- An existing AWS Identity and Access Management (IAM) OpenID Connect (OIDC) provider for your cluster. To determine whether you already have one, or to create one, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").
- Version 2.12.3 or later of the AWS CLI installed and configured on your device or AWS CloudShell.
- The `kubectl` command line tool is installed on your device or AWS CloudShell. The version can be the same as or up to one minor version earlier or later than the Kubernetes version of your cluster. For example, if your cluster version is `1.29`, you can use `kubectl` version `1.28`, `1.29`, or `1.30` with it. To install or upgrade `kubectl`, see [Set up kubectl and eksctl](install-kubectl.md "install-kubectl.md").

## Step 1: Create an IAM policy

The Mountpoint for Amazon S3 CSI driver requires Amazon S3 permissions to interact with your file system. This section shows how to create an IAM policy that grants the necessary permissions.

The following example policy follows the IAM permission recommendations for Mountpoint. Alternatively, you can use the AWS managed policy [AmazonS3FullAccess](https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess$jsonEditor "https://console.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/AmazonS3FullAccess$jsonEditor"), but this managed policy grants more permissions than are needed for Mountpoint.

For more information about the recommended permissions for Mountpoint, see [Mountpoint IAM permissions](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#iam-permissions "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md#iam-permissions") on GitHub.

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Policies**.
3. On the **Policies** page, choose **Create policy**.
4. For **Policy editor**, choose **JSON**.
5. Under **Policy editor**, copy and paste the following:

###### Important

Replace `amzn-s3-demo-bucket1` with your own Amazon S3 bucket name.

```
 {
   "Version":"2012-10-17",
   "Statement": [
        {
            "Sid": "MountpointFullBucketAccess",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket1"
            ]
        },
        {
            "Sid": "MountpointFullObjectAccess",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:DeleteObject"
            ],
            "Resource": [
                "arn:aws:s3:::amzn-s3-demo-bucket1/*"
            ]
        }
   ]
}
```

Directory buckets, introduced with the Amazon S3 Express One Zone storage class, use a different authentication mechanism from general purpose buckets. Instead of using `s3:*` actions, you should use the `s3express:CreateSession` action. For information about directory buckets, see [Directory buckets](../../../AmazonS3/latest/userguide/directory-buckets-overview.md "../../../AmazonS3/latest/userguide/directory-buckets-overview.md") in the _Amazon S3 User Guide_.

Below is an example of least-privilege policy that you would use for a directory bucket.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3express:CreateSession",
            "Resource": "arn:aws:s3express:us-west-2:111122223333:bucket/amzn-s3-demo-bucket1--usw2-az1--x-s3"
        }
    ]
}
```

6. Choose **Next**.
7. On the **Review and create** page, name your policy. This example walkthrough uses the name `AmazonS3CSIDriverPolicy`.
8. Choose **Create policy**.

## Step 2: Create an IAM role

The Mountpoint for Amazon S3 CSI driver requires Amazon S3 permissions to interact with your file system. This section shows how to create an IAM role to delegate these permissions. To create this role, you can use one of these tools:

- [eksctl](#eksctl_s3_store_app_data "#eksctl_s3_store_app_data")
- [AWS Management Console](#console_s3_store_app_data "#console_s3_store_app_data")
- [AWS CLI](#awscli_s3_store_app_data "#awscli_s3_store_app_data")

###### Note

The IAM policy `AmazonS3CSIDriverPolicy` was created in the previous section.

### eksctl

**To create your Mountpoint for Amazon S3 CSI driver IAM role with `eksctl`**

To create the IAM role and the Kubernetes service account, run the following commands. These commands also attach the `AmazonS3CSIDriverPolicy` IAM policy to the role, annotate the Kubernetes service account (`s3-csi-controller-sa`) with the IAM role’s Amazon Resource Name (ARN), and add the Kubernetes service account name to the trust policy for the IAM role.

```
 CLUSTER_NAME=my-cluster
REGION=region-code
ROLE_NAME=AmazonEKS_S3_CSI_DriverRole
POLICY_ARN=AmazonEKS_S3_CSI_DriverRole_ARN
eksctl create iamserviceaccount \
    --name s3-csi-driver-sa \
    --namespace kube-system \
    --cluster $CLUSTER_NAME \
    --attach-policy-arn $POLICY_ARN \
    --approve \
    --role-name $ROLE_NAME \
    --region $REGION \
    --role-only
```

### AWS Management Console

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the left navigation pane, choose **Roles**.
3. On the **Roles** page, choose **Create role**.
4. On the **Select trusted entity** page, do the following:
   1. In the **Trusted entity type** section, choose **Web identity**.
   2. For **Identity provider**, choose the **OpenID Connect provider URL** for your cluster (as shown under **Overview** in Amazon EKS).

   If no URLs are shown, review the [Prerequisites](#s3-csi-prereqs "#s3-csi-prereqs"). 3. For **Audience**, choose `sts.amazonaws.com`. 4. Choose **Next**.

5. On the **Add permissions** page, do the following:
   1. In the **Filter policies** box, enter AmazonS3CSIDriverPolicy.

   ###### Note

   This policy was created in the previous section. 2. Select the check box to the left of the `AmazonS3CSIDriverPolicy` result that was returned in the search. 3. Choose **Next**.

6. On the **Name, review, and create** page, do the following:
   1. For **Role name**, enter a unique name for your role, such as AmazonEKS_S3_CSI_DriverRole.
   2. Under **Add tags (Optional)**, add metadata to the role by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
   3. Choose **Create role**.

7. After the role is created, choose the role in the console to open it for editing.
8. Choose the **Trust relationships** tab, and then choose **Edit trust policy**.
9. Find the line that looks similar to the following:

```
 "oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
```

Add a comma to the end of the previous line, and then add the following line after it. Replace `region-code` with the AWS Region that your cluster is in. Replace `EXAMPLED539D4633E53DE1B71EXAMPLE` with your cluster’s OIDC provider ID.

```
 "oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:kube-system:s3-csi-driver-sa"
```

10. Ensure that the `Condition` operator is set to `"StringEquals"`.
11. Choose **Update policy** to finish.

### AWS CLI

1. View the OIDC provider URL for your cluster. Replace `my-cluster` with the name of your cluster. If the output from the command is `None`, review the [Prerequisites](#s3-csi-prereqs "#s3-csi-prereqs").

```
 aws eks describe-cluster --name my-cluster --query "cluster.identity.oidc.issuer" --output text
```

An example output is as follows.

```
 https://oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE
```

2. Create the IAM role, granting the Kubernetes service account the `AssumeRoleWithWebIdentity` action.
   1. Copy the following contents to a file named `aws-s3-csi-driver-trust-policy.json`. Replace `111122223333` with your account ID. Replace `EXAMPLED539D4633E53DE1B71EXAMPLE` and `region-code` with the values returned in the previous step.

   ```
    {
     "Version":"2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Federated": "arn:aws:iam::111122223333:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE"
         },
         "Action": "sts:AssumeRoleWithWebIdentity",
         "Condition": {
           "StringEquals": {
             "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:kube-system:s3-csi-driver-sa",
             "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
           }
         }
       }
     ]
   }
   ```

   2. Create the role. You can change `AmazonEKS_S3_CSI_DriverRole` to a different name, but if you do, make sure to change it in later steps too.

   ```
    aws iam create-role \
     --role-name AmazonEKS_S3_CSI_DriverRole \
     --assume-role-policy-document file://"aws-s3-csi-driver-trust-policy.json"
   ```

3. Attach the previously created IAM policy to the role with the following command.

```
 aws iam attach-role-policy \
  --policy-arn <shared id="region.arn"/>iam::aws:policy/AmazonS3CSIDriverPolicy \
  --role-name AmazonEKS_S3_CSI_DriverRole
```

###### Note

The IAM policy `AmazonS3CSIDriverPolicy` was created in the previous section. 4. Skip this step if you’re installing the driver as an Amazon EKS add-on. For self-managed installations of the driver, create Kubernetes service accounts that are annotated with the ARN of the IAM role that you created.

    1. Save the following contents to a file named `mountpoint-s3-service-account.yaml`. Replace `111122223333` with your account ID.



    ```
     ---
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      labels:
        app.kubernetes.io/name: aws-mountpoint-s3-csi-driver
      name: mountpoint-s3-csi-controller-sa
      namespace: kube-system
      annotations:
        eks.amazonaws.com/role-arn: <shared id="region.arn"/>iam::111122223333:role/AmazonEKS_S3_CSI_DriverRole
    ```
    2. Create the Kubernetes service account on your cluster. The Kubernetes service account (`mountpoint-s3-csi-controller-sa`) is annotated with the IAM role that you created named `AmazonEKS_S3_CSI_DriverRole`.



    ```
     kubectl apply -f mountpoint-s3-service-account.yaml
    ```

    ###### Note

    When you deploy the plugin in this procedure, it creates and is configured to use a service account named `s3-csi-driver-sa`.

## Step 3: Install the Mountpoint for Amazon S3 CSI driver

You may install the Mountpoint for Amazon S3 CSI driver through the Amazon EKS add-on. You can use the following tools to add the add-on to your cluster:

- [eksctl](#eksctl_s3_add_store_app_data "#eksctl_s3_add_store_app_data")
- [AWS Management Console](#console_s3_add_store_app_data "#console_s3_add_store_app_data")
- [AWS CLI](#awscli_s3_add_store_app_data "#awscli_s3_add_store_app_data")

Alternatively, you may install Mountpoint for Amazon S3 CSI driver as a self-managed installation. For instructions on doing a self-managed installation, see [Installation](https://github.com/awslabs/mountpoint-s3-csi-driver/blob/main/docs/install.md#deploy-driver "https://github.com/awslabs/mountpoint-s3-csi-driver/blob/main/docs/install.md#deploy-driver") on GitHub.

Starting from `v1.8.0`, you can configure taints to tolerate for the CSI driver’s Pods. To do this, either specify a custom set of taints to tolerate with `node.tolerations` or tolorate all taints with `node.tolerateAllTaints`. For more information, see [Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/ "https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/") in the Kubernetes documentation.

### eksctl

**To add the Amazon S3 CSI add-on using `eksctl`**

Run the following command. Replace `my-cluster` with the name of your cluster, `111122223333` with your account ID, and `AmazonEKS_S3_CSI_DriverRole` with the name of the [IAM role created earlier](#s3-create-iam-role "#s3-create-iam-role").

```
 eksctl create addon --name aws-mountpoint-s3-csi-driver --cluster my-cluster \
  --service-account-role-arn <shared id="region.arn"/>iam::111122223333:role/AmazonEKS_S3_CSI_DriverRole --force
```

If you remove the `--force` option and any of the Amazon EKS add-on settings conflict with your existing settings, then updating the Amazon EKS add-on fails, and you receive an error message to help you resolve the conflict. Before specifying this option, make sure that the Amazon EKS add-on doesn’t manage settings that you need to manage, because those settings are overwritten with this option. For more information about other options for this setting, see [Addons](https://eksctl.io/usage/addons/ "https://eksctl.io/usage/addons/") in the `eksctl` documentation. For more information about Amazon EKS Kubernetes field management, see [Determine fields you can customize for Amazon EKS add-ons](kubernetes-field-management.md "kubernetes-field-management.md").

You can customize `eksctl` through configuration files. For more information, see [Working with configuration values](https://eksctl.io/usage/addons/#working-with-configuration-values "https://eksctl.io/usage/addons/#working-with-configuration-values") in the `eksctl` documentation. The following example shows how to tolerate all taints.

```
 # config.yaml
...

addons:
- name: aws-mountpoint-s3-csi-driver
  serviceAccountRoleARN: <shared id="region.arn"/>iam::111122223333:role/AmazonEKS_S3_CSI_DriverRole
  configurationValues: |-
    node:
      tolerateAllTaints: true
```

### AWS Management Console

1. Open the [Amazon EKS console](https://console.aws.amazon.com/eks/home#/clusters "https://console.aws.amazon.com/eks/home#/clusters").
2. In the left navigation pane, choose **Clusters**.
3. Choose the name of the cluster that you want to configure the Mountpoint for Amazon S3 CSI add-on for.
4. Choose the **Add-ons** tab.
5. Choose **Get more add-ons**.
6. On the **Select add-ons** page, do the following:
   1. In the **Amazon EKS-addons** section, select the **Mountpoint for Amazon S3 CSI Driver** check box.
   2. Choose **Next**.

7. On the **Configure selected add-ons settings** page, do the following:
   1. Select the **Version** you’d like to use.
   2. For **Select IAM role**, select the name of an IAM role that you attached the Mountpoint for Amazon S3 CSI driver IAM policy to.
   3. (Optional) Update the **Conflict resolution method** after expanding the **Optional configuration settings**. If you select **Override**, one or more of the settings for the existing add-on can be overwritten with the Amazon EKS add-on settings. If you don’t enable this option and there’s a conflict with your existing settings, the operation fails. You can use the resulting error message to troubleshoot the conflict. Before selecting this option, make sure that the Amazon EKS add-on doesn’t manage settings that you need to self-manage.
   4. (Optional) Configure tolerations in the **Configuration values** field after expanding the **Optional configuration settings**.
   5. Choose **Next**.

8. On the **Review and add** page, choose **Create**. After the add-on installation is complete, you see your installed add-on.

### AWS CLI

**To add the Mountpoint for Amazon S3 CSI add-on using the AWS CLI**

Run the following command. Replace `my-cluster` with the name of your cluster, `111122223333` with your account ID, and `AmazonEKS_S3_CSI_DriverRole` with the name of the role that was created earlier.

```
 aws eks create-addon --cluster-name my-cluster --addon-name aws-mountpoint-s3-csi-driver \
  --service-account-role-arn <shared id="region.arn"/>iam::111122223333:role/AmazonEKS_S3_CSI_DriverRole
```

You can customize the command with the `--configuration-values` flag. The following alternative example shows how to tolerate all taints.

```
 aws eks create-addon --cluster-name my-cluster --addon-name aws-mountpoint-s3-csi-driver \
  --service-account-role-arn <shared id="region.arn"/>iam::111122223333:role/AmazonEKS_S3_CSI_DriverRole \
  --configuration-values '{"node":{"tolerateAllTaints":true}}'
```

## Step 4: Configure Mountpoint for Amazon S3

In most cases, you can configure Mountpoint for Amazon S3 with only a bucket name. For instructions on configuring Mountpoint for Amazon S3, see [Configuring Mountpoint for Amazon S3](https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/CONFIGURATION.md") on GitHub.

## Step 5: Deploy a sample application

You can deploy static provisioning to the driver on an existing Amazon S3 bucket. For more information, see [Static provisioning](https://github.com/awslabs/mountpoint-s3-csi-driver/blob/main/examples/kubernetes/static_provisioning/README.md "https://github.com/awslabs/mountpoint-s3-csi-driver/blob/main/examples/kubernetes/static_provisioning/README.md") on GitHub.
