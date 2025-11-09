Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Billing

for Support for Amazon CodeCatalyst

When
you create a space in CodeCatalyst, users in the space can create and manage support
cases from Support for Amazon CodeCatalyst. You can create two types of customer
cases:

- **Account and billing**
  support
  cases are available to all CodeCatalyst users in the space.
  You can get help with billing and account questions based on your permissions in
  CodeCatalyst.
- **Technical**
  support cases connect you to a technical support engineer for
  help with service-related technical issues and extensions to third-party
  applications. If you have Basic Support, you can't create a technical support
  case.

The AWS account designated as the billing account for the space must
have a Business Support or Enterprise Support plan for the space to use
Support for CodeCatalyst for technical cases.

###### Note

If your space uses Support for Amazon CodeCatalyst from an account that doesn't have a
Business Support or Enterprise Support plan, you can still use
Support for Amazon CodeCatalyst for account and billing cases.
For technical support, you must open all cases through the CodeCatalyst console. You cannot
create technical support cases for CodeCatalyst from [Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")
in the AWS Management Console.

###### Note

**Service limit increase** requests are not available from
Support for Amazon CodeCatalyst. These requests can only be submitted by the root user for the
space billing account in the AWS Support Center Console.

Support for Amazon CodeCatalyst has the same support agreements as Support, with the following
considerations:

- Severity lists, response times, and SLAs in Support apply for support cases in
  Support for CodeCatalyst, as detailed in [Choosing a severity](../../../awssupport/latest/user/case-management.md#choosing-severity "../../../awssupport/latest/user/case-management.md#choosing-severity").
- Space administrators and space members cannot use the Support APIs or AWS SDK
  or Support app in Slack to create cases for CodeCatalyst. CodeCatalyst support cases can only
  be submitted from CodeCatalyst.

###### Note

CodeCatalyst is not fully integrated with AWS Trusted Advisor or AWS Incident Detection and
Response.
Validate
how CodeCatalyst is integrated to ensure your business practices are aligned with the
current integration.

You must be a user in the space where you want to request support.

###### Note

If you have more than one builder in your space, we recommend that you
purchase a Business Support or Enterprise Support plan.
These
plans provide technical support for the space for up to 5,000
builders.

The AWS account designated as the billing account for the space uses the
`AWSRoleForCodeCatalystSupport` role and [AmazonCodeCatalystSupportAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess") managed policy. This allows CodeCatalyst users in
a space to access the Support for Amazon CodeCatalyst page. For more information about this role and
policy, see [AmazonCodeCatalystSupportAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeCatalystSupportAccess"). For other considerations about billing, see [Managing billing](../adminguide/managing-billing.md "../adminguide/managing-billing.md") in the Amazon CodeCatalyst Administrator Guide.

Here is a possible flow for a builder creating a support case in CodeCatalyst:

Mateo Jackson is a developer on a project in CodeCatalyst. After signing up the
AWS account that manages billing with Support for Amazon CodeCatalyst and upgrading to a Business
Support plan, all builders in the space can create technical support cases. Mateo
submits a technical support case for a failed workflow in their project. Mateo uses the
Support for Amazon CodeCatalyst page to fill out the form and create a case, providing the workflow ID
and other details in the request. The case is created with a case ID and includes the
account ID of the AWS account designated as the billing account and associated with
support plan for the space.

While all builders can create support cases in Support for CodeCatalyst, you are not charged
for each case created. You can open virtually
unlimited
cases and contacts based on the Support Premium plan you purchase on
your space billing account.

###### Note

The space billing account is the AWS account that you are charged for
CodeCatalyst users and resources. If you have deployed to additional AWS accounts,
contact Support through the AWS Management Console for assistance with resources deployed to other
services.

You can identify the AWS account you deployed to from the workflow.
