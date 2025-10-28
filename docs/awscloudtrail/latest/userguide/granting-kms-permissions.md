# Granting permissions to create a KMS key

You can grant users permission to create an AWS KMS key with the
[`AWSKeyManagementServicePowerUser`](../../../aws-managed-policy/latest/reference/AWSKeyManagementServicePowerUser.md "../../../aws-managed-policy/latest/reference/AWSKeyManagementServicePowerUser.md") policy.

###### To grant permission to create a KMS key

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose the group or user that you want to give permission.
3. Choose the **Permissions** tab.
4. From the **Add permissions** list, choose **Attach policies**.
5. Search for **AWSKeyManagementServicePowerUser**, choose the
   policy, and then choose **Attach policies**.

The user now has permission to create a KMS key. For more information about
creating policies, see [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.
