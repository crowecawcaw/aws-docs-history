# Prerequisites to use AWS Supply Chain

Before you create an AWS Supply Chain instance, make sure that you complete the
following steps:

- You have an AWS account. To create an AWS account, see [Setting up an AWS account](setting-up.md "setting-up.md").
- Make sure IAM Identity Center is enabled. To enable IAM Identity Center, see [Enabling IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md").
- You have the necessary administrative permissions. For more information regarding permissions, see Advanced configuration.
- An IAM Identity Center instance must be activated in the same region where you want to create your AWS Supply Chain instance. AWS Supply Chain is only supported in
  US East (N. Virginia), US West (Oregon), Europe (Frankfurt), Asia Pacific (Sydney),
  and Europe (Ireland) Region.

If the AWS Supply Chain instance is not in the same region as the IAM Identity Center region, [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") for further assistance.

- You must have at least have one user in the IAM Identity Center instance to assign as the AWS Supply Chain administrator. You can connect your active directory to IAM Identity Center. For more information, see [Connect to a Microsoft AD directory](../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md "../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md").
- Add any additional users who need access to AWS Supply Chain to IAM Identity Center.
- You need AWS Key Management Service (AWS KMS) to create an instance. AWS Supply Chain uses this
  AWS KMS key to encrypt all the data that comes into AWS Supply Chain. For information about AWS KMS Keys, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
