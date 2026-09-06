

# Add a delegated administrator for IAM Access Analyzer
<a name="access-analyzer-delegated-administrator-add"></a>

If you're configuring AWS Identity and Access Management Access Analyzer in your AWS Organizations management account, you can add a member account in the organization as the delegated administrator to manage IAM Access Analyzer for your organization. The delegated administrator has permissions to create and manage analyzers within the organization. Only the management account can add a delegated administrator.

**To add a delegated administrator using the console**

1. Log in to the AWS console using the management account for your organization.

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Under **Access Analyzer**, choose **Analyzer settings**.

1. Choose **Add delegated administrator**.

1. In the **Delegated administrator** field, enter the AWS account number of an organization member account to make the delegated administrator.

   The account must be a member of your organization.

1. Choose **Save changes**.

**To add a delegated administrator using the AWS CLI or the AWS SDKs**

When you create an analyzer to analyze access across the organization in a delegated administrator account using the AWS CLI, AWS API (using the AWS SDKs) or CloudFormation, you must use AWS Organizations APIs to enable service access for IAM Access Analyzer and register the member account as a delegated administrator.

1. Enable trusted service access for IAM Access Analyzer in AWS Organizations. See [How to Enable or Disable Trusted Access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) in the AWS Organizations User Guide.

1. Register a valid member account of your AWS organization as a delegated administrator using the AWS Organizations [`RegisterDelegatedAdministrator`](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RegisterDelegatedAdministrator.html) API operation or the `register-delegated-administrator` AWS CLI command.