# Getting started with Amazon AppFlow

This section provides an introduction to Amazon AppFlow with prerequisites for getting started.
The following diagram illustrates how you can use Amazon AppFlow to transfer and enrich data from a data source to a data destination in your flow:

![Amazon AppFlow overview page.](images/appflow-ov.png)

###### Tasks

- [Prerequisites](#prerequisites "#prerequisites")

## Prerequisites

Complete the following prerequisites before getting started with Amazon AppFlow.

- AWS account setup — If you don't have
  an AWS account, you must create one. For more information, see [How to
  create and activate a new AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/ "https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/").
- SaaS application setup — You must verify
  that you have the required information about the source and destination
  applications, and that they meet the relevant configuration requirements. For
  application-specific requirements and setup instructions, see [Supported source and destination applications](app-specific.md "app-specific.md").
- Identity and access management — Your
  administrator must grant you the permissions required to create and run flows. For more
  information, see [Identity and access management for Amazon AppFlow](security-iam.md "security-iam.md") .
- CloudFormation OAuth (Optional) — If you want to use CloudFormation
  to create a connector profile for connectors that implement OAuth (such as Salesforce,
  Slack, Zendesk, and Google Analytics), you must fetch the access and refresh tokens. You
  can do this by implementing your own UI for OAuth, or by retrieving them from elsewhere.
  Alternatively, you can use the Amazon AppFlow console to create the connector profile, and
  then use that connector profile in the flow creation CloudFormation template.
- Data encryption (Optional) — Amazon AppFlow encrypts
  your data and connection details during transit and at rest. For more information, see
  [Data protection in Amazon AppFlow](data-protection.md "data-protection.md"). When you configure a
  flow, you specify an AWS Key Management Service CMK to use for encryption. You can choose the AWS managed
  customer master key (CMK) that Amazon AppFlow creates by default, named
  **AWSDefaultEncryptionKey**, or you can choose a customer managed CMK
  that you create. To create a CMK, see [Creating symmetric CMKs](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk")
  in the _AWS Key Management Service Developer Guide_. For examples of how to set IAM permissions
  for KMS access, see [Identity-based policy examples
  for Amazon AppFlow](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
