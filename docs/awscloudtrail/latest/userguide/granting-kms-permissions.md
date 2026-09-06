

# Granting permissions to create a KMS key
<a name="granting-kms-permissions"></a>

You can grant users permission to create an AWS KMS key with the [`AWSKeyManagementServicePowerUser`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSKeyManagementServicePowerUser.html) policy.

**To grant permission to create a KMS key**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose the group or user that you want to give permission.

1. Choose the **Permissions** tab.

1.  From the **Add permissions** list, choose **Attach policies**. 

1. Search for **AWSKeyManagementServicePowerUser**, choose the policy, and then choose **Attach policies**. 

   The user now has permission to create a KMS key. For more information about creating policies, see [Creating IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.