

# Getting started with Amazon AppFlow
<a name="getting-started"></a>

This section provides an introduction to Amazon AppFlow with prerequisites for getting started. The following diagram illustrates how you can use Amazon AppFlow to transfer and enrich data from a data source to a data destination in your flow:

![Amazon AppFlow overview page.](http://docs.aws.amazon.com/appflow/latest/userguide/images/appflow-ov.png)


**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Prerequisites](#prerequisites)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Prerequisites
<a name="prerequisites"></a>

Complete the following prerequisites before getting started with Amazon AppFlow.
+ **SaaS application setup** — You must verify that you have the required information about the source and destination applications, and that they meet the relevant configuration requirements. For application-specific requirements and setup instructions, see [Supported source and destination applications](app-specific.md).
+ **Identity and access management** — Your administrator must grant you the permissions required to create and run flows. For more information, see [Identity and access management for Amazon AppFlow](security-iam.md).
+ **CloudFormation OAuth (Optional)** — If you want to use CloudFormation to create a connector profile for connectors that implement OAuth (such as Salesforce, Slack, Zendesk, and Google Analytics), you must fetch the access and refresh tokens. You can do this by implementing your own UI for OAuth, or by retrieving them from elsewhere. Alternatively, you can use the Amazon AppFlow console to create the connector profile, and then use that connector profile in the flow creation CloudFormation template.
+ **Data encryption (Optional)** — Amazon AppFlow encrypts your data and connection details during transit and at rest. For more information, see [Data protection in Amazon AppFlow](data-protection.md). When you configure a flow, you specify an AWS Key Management Service CMK to use for encryption. You can choose the AWS managed customer master key (CMK) that Amazon AppFlow creates by default, named **AWSDefaultEncryptionKey**, or you can choose a customer managed CMK that you create. To create a CMK, see [Creating symmetric CMKs](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *AWS Key Management Service Developer Guide*. For examples of how to set IAM permissions for KMS access, see [Identity-based policy examples for Amazon AppFlow](security_iam_id-based-policy-examples.md).