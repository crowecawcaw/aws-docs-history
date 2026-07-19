# Prerequisites to use Amazon Connect Decisions

Before you create an Amazon Connect Decisions instance, make sure that you
complete the following steps:

- You have an AWS account. To create an AWS account, see
  [Setting up an AWS account](setting-up-an-aws-account.md "setting-up-an-aws-account.md").
- Make sure IAM Identity Center is enabled. To enable IAM Identity Center, see
  [Enabling IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md").
- An IAM Identity Center instance must be activated in the same region where
  you want to create your Amazon Connect Decisions instance. Amazon Connect Decisions
  is only supported in US East (N. Virginia) and Europe (Ireland) Region.
- If the Amazon Connect Decisions instance is not in the same region as
  your existing IAM Identity Center region,
  [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/")
  for further assistance.
- You must have at least one user in the IAM Identity Center instance to
  assign as the Amazon Connect Decisions administrator. You can connect your
  active directory to IAM Identity Center. For more information, see
  [Connect to a Microsoft AD directory](../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md "../../../singlesignon/latest/userguide/manage-your-identity-source-ad.md").
- Add any additional users who need access to Amazon Connect Decisions to
  IAM Identity Center.
- You need AWS Key Management Service (AWS KMS) to create an instance.
  Amazon Connect Decisions uses this AWS KMS key to encrypt all the data that
  comes into Amazon Connect Decisions. For information about AWS KMS Keys, see
  [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
- If you intend to enable the actions feature, you will need to configure a
  connection to the system you use to maintain the relevant data, and provide
  credentials for Amazon Connect Decisions to use. Please
  [contact us](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/")
  for further assistance.
