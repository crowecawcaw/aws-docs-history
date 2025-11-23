# Add a delegated administrator

for IAM Access Analyzer

If you're configuring AWS Identity and Access Management Access Analyzer in your AWS Organizations management account, you can add a
member account in the organization as the delegated administrator to manage IAM Access Analyzer
for your organization. The delegated administrator has permissions to create and manage
analyzers within the organization. Only the management account can add a delegated
administrator.

###### To add a delegated administrator using the console

1. Log in to the AWS console using the management account for your
   organization.
2. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
3. Under **Access Analyzer**, choose **Analyzer
   settings**.
4. Choose **Add delegated administrator**.
5. In the **Delegated administrator** field, enter the AWS account
   number of an organization member account to make the delegated administrator.

The account must be a member of your organization. 6. Choose **Save changes**.

###### To add a delegated administrator using the AWS CLI or the AWS SDKs

When you create an analyzer to analyzer access across the organization in a delegated
administrator account using the AWS CLI, AWS API (using the AWS SDKs) or CloudFormation,
you must use AWS Organizations APIs to enable service access for IAM Access Analyzer and register the
member account as a delegated administrator.

1. Enable trusted service access for IAM Access Analyzer in AWS Organizations. See [How to Enable
   or Disable Trusted Access](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the AWS Organizations User Guide.
2. Register a valid member account of your AWS organization as a delegated
   administrator using the AWS Organizations [`RegisterDelegatedAdministrator`](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md") API operation or the
   `register-delegated-administrator` AWS CLI command.
