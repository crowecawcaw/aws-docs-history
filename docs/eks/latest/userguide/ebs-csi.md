**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use Kubernetes volume storage with Amazon EBS

###### Note

**New:** Amazon EKS Auto Mode automates routine tasks for block storage. Learn how to [Deploy a sample stateful workload to EKS Auto Mode](sample-storage-workload.md "sample-storage-workload.md").

The [Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/ "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/") manages the lifecycle of Amazon EBS volumes as storage for the Kubernetes Volumes that you create. The Amazon EBS CSI driver makes Amazon EBS volumes for these types of Kubernetes volumes: generic [ephemeral volumes](https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/ "https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/") and [persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/ "https://kubernetes.io/docs/concepts/storage/persistent-volumes/").

## Considerations

- You do not need to install the Amazon EBS CSI controller on EKS Auto Mode clusters.
- You can’t mount Amazon EBS volumes to Fargate Pods.
- You can run the Amazon EBS CSI controller on Fargate nodes, but the Amazon EBS CSI node `DaemonSet` can only run on Amazon EC2 instances.
- Amazon EBS volumes and the Amazon EBS CSI driver are not compatible with Amazon EKS Hybrid Nodes.
- Support will be provided for the latest add-on version and one prior version. Bugs or vulnerabilities found in the latest version will be backported to the previous release in a new minor version.
- EKS Auto Mode requires storage classes to use `ebs.csi.eks.amazonaws.com` as the provisioner. The standard Amazon EBS CSI Driver (`ebs.csi.aws.com`) manages its own volumes separately. To use existing volumes with EKS Auto Mode, migrate them using volume snapshots to a storage class that uses the Auto Mode provisioner.

###### Important

To use the snapshot functionality of the Amazon EBS CSI driver, you must first install the CSI snapshot controller. For more information, see [Enable snapshot functionality for CSI volumes](csi-snapshot-controller.md "csi-snapshot-controller.md").

## Prerequisites

- An existing cluster. To see the required platform version, run the following command.

```
aws eks describe-addon-versions --addon-name aws-ebs-csi-driver
```

- The EBS CSI driver needs AWS IAM Permissions.
  - AWS suggests using EKS Pod Identities. For more information, see [Overview of setting up EKS Pod Identities](pod-identities.md#pod-id-setup-overview "pod-identities.md#pod-id-setup-overview").
  - For information about IAM Roles for Service Accounts, see [Create an IAM OIDC provider for your cluster](enable-iam-roles-for-service-accounts.md "enable-iam-roles-for-service-accounts.md").

## Step 1: Create an IAM role

The Amazon EBS CSI plugin requires IAM permissions to make calls to AWS APIs on your behalf. If you don’t do these steps, attempting to install the add-on and running `kubectl describe pvc` will show `failed to provision volume with StorageClass` along with a `could not create volume in EC2: UnauthorizedOperation` error. For more information, see [Set up driver permission](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#set-up-driver-permissions "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#set-up-driver-permissions") on GitHub.

###### Note

Pods will have access to the permissions that are assigned to the IAM role unless you block access to IMDS. For more information, see [Secure Amazon EKS clusters with best practices](security-best-practices.md "security-best-practices.md").

The following procedure shows you how to create an IAM role and attach the AWS managed policy to it. To implement this procedure, you can use one of these tools:

- [eksctl](#eksctl_store_app_data "#eksctl_store_app_data")
- [AWS Management Console](#console_store_app_data "#console_store_app_data")
- [AWS CLI](#awscli_store_app_data "#awscli_store_app_data")

###### Note

You can create a self-managed policy with scoped-down permissions. Review [`AmazonEBSCSIDriverPolicy`](../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md "../../../aws-managed-policy/latest/reference/AmazonEBSCSIDriverPolicy.md") and create a custom IAM Policy with reduced permissions.

###### Note

The specific steps in this procedure are written for using the driver as an Amazon EKS add-on. Different steps are needed to use the driver as a self-managed add-on. For more information, see [Set up driver permissions](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#set-up-driver-permissions "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#set-up-driver-permissions") on GitHub.

### `eksctl`

1. Create an IAM role and attach a policy. AWS maintains an AWS managed policy or you can create your own custom policy. You can create an IAM role and attach the AWS managed policy with the following command. Replace `my-cluster` with the name of your cluster. The command deploys an AWS CloudFormation stack that creates an IAM role and attaches the IAM policy to it.

```
eksctl create iamserviceaccount \
        --name ebs-csi-controller-sa \
        --namespace kube-system \
        --cluster my-cluster \
        --role-name AmazonEKS_EBS_CSI_DriverRole \
        --role-only \
        --attach-policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
        --approve
```

2. You can skip this step if you do not use a custom [KMS key](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). If you use one for encryption on your Amazon EBS volumes, customize the IAM role as needed. For example, do the following:
   1. Copy and paste the following code into a new `kms-key-for-encryption-on-ebs.json` file. Replace `custom-key-arn` with the custom [KMS key ARN](../../../service-authorization/latest/reference/list_awskeymanagementservice.md#awskeymanagementservice-key "../../../service-authorization/latest/reference/list_awskeymanagementservice.md#awskeymanagementservice-key").

   ```
   {
         "Version":"2012-10-17",
         "Statement": [
           {
             "Effect": "Allow",
             "Action": [
               "kms:CreateGrant",
               "kms:ListGrants",
               "kms:RevokeGrant"
             ],
             "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"],
             "Condition": {
               "Bool": {
                 "kms:GrantIsForAWSResource": "true"
               }
             }
           },
           {
             "Effect": "Allow",
             "Action": [
               "kms:Encrypt",
               "kms:Decrypt",
               "kms:ReEncrypt*",
               "kms:GenerateDataKey*",
               "kms:DescribeKey"
             ],
             "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"]
           }
         ]
       }
   ```

   2. Create the policy. You can change `KMS_Key_For_Encryption_On_EBS_Policy` to a different name. However, if you do, make sure to change it in later steps, too.

   ```
   aws iam create-policy \
         --policy-name KMS_Key_For_Encryption_On_EBS_Policy \
         --policy-document file://kms-key-for-encryption-on-ebs.json
   ```

   3. Attach the IAM policy to the role with the following command. Replace `111122223333` with your account ID.

   ```
   aws iam attach-role-policy \
         --policy-arn arn:aws:iam::111122223333:policy/KMS_Key_For_Encryption_On_EBS_Policy \
         --role-name AmazonEKS_EBS_CSI_DriverRole
   ```

### AWS Management Console

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**.
3. On the **Roles** page, choose **Create role**.
4. On the **Select trusted entity** page, do the following:
   1. In the **Trusted entity type** section, choose **Web identity**.
   2. For **Identity provider**, choose the **OpenID Connect provider URL** for your cluster (as shown under **Overview** in Amazon EKS).
   3. For **Audience**, choose `sts.amazonaws.com`.
   4. Choose **Next**.

5. On the **Add permissions** page, do the following:
   1. In the **Filter policies** box, enter `AmazonEBSCSIDriverPolicy`.
   2. Select the check box to the left of the `AmazonEBSCSIDriverPolicy` returned in the search.
   3. Choose **Next**.

6. On the **Name, review, and create** page, do the following:
   1. For **Role name**, enter a unique name for your role, such as `AmazonEKS_EBS_CSI_DriverRole`.
   2. Under **Add tags (Optional)**, add metadata to the role by attaching tags as key-value pairs. For more information about using tags in IAM, see [Tagging IAM resources](../../../IAM/latest/UserGuide/id_tags.md "../../../IAM/latest/UserGuide/id_tags.md") in the _IAM User Guide_.
   3. Choose **Create role**.

7. After the role is created, choose the role in the console to open it for editing.
8. Choose the **Trust relationships** tab, and then choose **Edit trust policy**.
9. Find the line that looks similar to the following line:

```
"oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com"
```

Add a comma to the end of the previous line, and then add the following line after the previous line. Replace `region-code` with the AWS Region that your cluster is in. Replace `EXAMPLED539D4633E53DE1B71EXAMPLE` with your cluster’s OIDC provider ID.

```
"oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:kube-system:ebs-csi-controller-sa"
```

10. Choose **Update policy** to finish.
11. If you use a custom [KMS key](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") for encryption on your Amazon EBS volumes, customize the IAM role as needed. For example, do the following:
    1.  In the left navigation pane, choose **Policies**.
    2.  On the **Policies** page, choose **Create Policy**.
    3.  On the **Create policy** page, choose the **JSON** tab.
    4.  Copy and paste the following code into the editor, replacing `custom-key-arn` with the custom [KMS key ARN](../../../service-authorization/latest/reference/list_awskeymanagementservice.md#awskeymanagementservice-key "../../../service-authorization/latest/reference/list_awskeymanagementservice.md#awskeymanagementservice-key").

    ```
    {
          "Version":"2012-10-17",
          "Statement": [
            {
              "Effect": "Allow",
              "Action": [
                "kms:CreateGrant",
                "kms:ListGrants",
                "kms:RevokeGrant"
              ],
              "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"],
              "Condition": {
                "Bool": {
                  "kms:GrantIsForAWSResource": "true"
                }
              }
            },
            {
              "Effect": "Allow",
              "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:ReEncrypt*",
                "kms:GenerateDataKey*",
                "kms:DescribeKey"
              ],
              "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"]
            }
          ]
        }
    ```

    5.  Choose **Next: Tags**.
    6.  On the **Add tags (Optional)** page, choose **Next: Review**.
    7.  For **Name**, enter a unique name for your policy (for example, `KMS_Key_For_Encryption_On_EBS_Policy`).
    8.  Choose **Create policy**.
    9.  In the left navigation pane, choose **Roles**.
    10. Choose the **`AmazonEKS_EBS_CSI_DriverRole`** in the console to open it for editing.
    11. From the **Add permissions** dropdown list, choose **Attach policies**.
    12. In the **Filter policies** box, enter `KMS_Key_For_Encryption_On_EBS_Policy`.
    13. Select the check box to the left of the `KMS_Key_For_Encryption_On_EBS_Policy` that was returned in the search.
    14. Choose **Attach policies**.

### AWS CLI

1. View your cluster’s OIDC provider URL. Replace `my-cluster` with your cluster name. If the output from the command is `None`, review the **Prerequisites**.

```
aws eks describe-cluster --name my-cluster --query "cluster.identity.oidc.issuer" --output text
```

An example output is as follows.

```
https://oidc.eks.region-code.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE
```

2. Create the IAM role, granting the `AssumeRoleWithWebIdentity` action.
   1. Copy the following contents to a file that’s named `aws-ebs-csi-driver-trust-policy.json`. Replace `111122223333` with your account ID. Replace `EXAMPLED539D4633E53DE1B71EXAMPLE` and `region-code` with the values returned in the previous step.

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
                 "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:aud": "sts.amazonaws.com",
                 "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLED539D4633E53DE1B71EXAMPLE:sub": "system:serviceaccount:kube-system:ebs-csi-controller-sa"
               }
             }
           }
         ]
       }
   ```

   2. Create the role. You can change `AmazonEKS_EBS_CSI_DriverRole` to a different name. If you change it, make sure to change it in later steps.

   ```
   aws iam create-role \
         --role-name AmazonEKS_EBS_CSI_DriverRole \
         --assume-role-policy-document file://"aws-ebs-csi-driver-trust-policy.json"
   ```

3. Attach a policy. AWS maintains an AWS managed policy or you can create your own custom policy. Attach the AWS managed policy to the role with the following command.

```
aws iam attach-role-policy \
      --policy-arn arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy \
      --role-name AmazonEKS_EBS_CSI_DriverRole
```

4. If you use a custom [KMS key](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") for encryption on your Amazon EBS volumes, customize the IAM role as needed. For example, do the following:
   1. Copy and paste the following code into a new `kms-key-for-encryption-on-ebs.json` file. Replace `custom-key-arn` with the custom [KMS key ARN](../../../service-authorization/latest/reference/list_awskeymanagementservice.md#awskeymanagementservice-key "../../../service-authorization/latest/reference/list_awskeymanagementservice.md#awskeymanagementservice-key").

   ```
   {
         "Version":"2012-10-17",
         "Statement": [
           {
             "Effect": "Allow",
             "Action": [
               "kms:CreateGrant",
               "kms:ListGrants",
               "kms:RevokeGrant"
             ],
             "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"],
             "Condition": {
               "Bool": {
                 "kms:GrantIsForAWSResource": "true"
               }
             }
           },
           {
             "Effect": "Allow",
             "Action": [
               "kms:Encrypt",
               "kms:Decrypt",
               "kms:ReEncrypt*",
               "kms:GenerateDataKey*",
               "kms:DescribeKey"
             ],
             "Resource": ["arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"]
           }
         ]
       }
   ```

   2. Create the policy. You can change `KMS_Key_For_Encryption_On_EBS_Policy` to a different name. However, if you do, make sure to change it in later steps, too.

   ```
   aws iam create-policy \
         --policy-name KMS_Key_For_Encryption_On_EBS_Policy \
         --policy-document file://kms-key-for-encryption-on-ebs.json
   ```

   3. Attach the IAM policy to the role with the following command. Replace `111122223333` with your account ID.

   ```
   aws iam attach-role-policy \
         --policy-arn arn:aws:iam::111122223333:policy/KMS_Key_For_Encryption_On_EBS_Policy \
         --role-name AmazonEKS_EBS_CSI_DriverRole
   ```

Now that you have created the Amazon EBS CSI driver IAM role, you can continue to the next section. When you deploy the add-on with this IAM role, it creates and is configured to use a service account that’s named `ebs-csi-controller-sa`. The service account is bound to a Kubernetes `clusterrole` that’s assigned the required Kubernetes permissions.

## Step 2: Get the Amazon EBS CSI driver

We recommend that you install the Amazon EBS CSI driver through the Amazon EKS add-on to improve security and reduce the amount of work. To add an Amazon EKS add-on to your cluster, see [Create an Amazon EKS add-on](creating-an-add-on.md "creating-an-add-on.md"). For more information about add-ons, see [Amazon EKS add-ons](eks-add-ons.md "eks-add-ons.md").

###### Important

Before adding the Amazon EBS driver as an Amazon EKS add-on, confirm that you don’t have a self-managed version of the driver installed on your cluster. If so, see [Uninstalling a self-managed Amazon EBS CSI driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#uninstalling-the-ebs-csi-driver "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md#uninstalling-the-ebs-csi-driver") on GitHub.

###### Note

By default, the RBAC role used by the EBS CSI has permissions to mutate nodes to support its taint removal feature. Due to limitations of Kubernetes RBAC, this also allows it to mutate any other Node in the cluster.
The Helm chart has a parameter (`node.serviceAccount.disableMutation`) that disables mutating Node RBAC permissions for the ebs-csi-node service account. When enabled, driver features such as taint removal will not function.

Alternatively, if you want a self-managed installation of the Amazon EBS CSI driver, see [Installation](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/blob/master/docs/install.md") on GitHub.

## Step 3: Deploy a sample application

You can deploy a variety of sample apps and modify them as needed. For more information, see [Kubernetes Examples](https://github.com/kubernetes-sigs/aws-ebs-csi-driver/tree/master/examples/kubernetes "https://github.com/kubernetes-sigs/aws-ebs-csi-driver/tree/master/examples/kubernetes") on GitHub.
