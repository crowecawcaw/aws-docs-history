# Select a membership account

A membership account is the AWS account used to configure account details, add and remove
details for your incident response team, and where all active and historical security events
can be created and managed. It's recommended that you align your AWS Security Incident Response membership account
to the same account that you have enabled for services such as Amazon GuardDuty and AWS Security Hub CSPM.

You have two options for selecting your AWS Security Incident Response membership account using AWS Organizations. You can either create a
membership in the Organizations management account or in an Organizations delegated administrator account.

**Use the delegated administrator
account:** AWS Security Incident Response administrative
tasks and case management are located in the delegated
administrator account. We recommend using the same delegated
administrator that you set for other AWS security and compliance
services. Provide the 12-digit delegated administrator account ID
and then log in to that account to proceed.

AWS Security Incident Response automatically creates the `AWSServiceRoleForSecurityIncidentResponse_Triage` service-linked role in your AWS Organizations management account and in all accounts that are in scope when onboarding through the AWS Security Incident Response console. For instructions on enabling AWS Security Incident Response and designating a delegated administrator account using the API/CLI, see [Enable Security Incident Response and configure your incident response team using the API/CLI](enable-sir-using-cli.md "enable-sir-using-cli.md").

**Use the currently logged in
account**: Selecting this account means the current account will be designated as the
central membership account for your AWS Security Incident Response membership. Individuals within your organization will need to
access the service through this account to create, access, and manage active and resolved cases.

Ensure you have sufficient permissions to administer AWS Security Incident Response.

Refer to [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") for specific steps to add permissions.

Refer to [AWS Security Incident Response
managed policies.](aws-managed-policies.md "aws-managed-policies.md")

To verify IAM permissions, you can follow these steps:

- _Check the IAM Policy:_ Review the IAM policy attached to your user, group, or
  role to ensure it grants the necessary permissions. You can do this by navigating
  to the [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), select the `Users` option, choose the specific user,
  and then on their summary page, go to the `Permissions` tab where
  you can see a list of all attached policies; you can expand each policy row to view its details.
- _Test the Permissions:_ Try to perform the action you need to verify the permissions.
  For example, if you need to access a case, try to `ListCases`. If you don't have the necessary
  permissions, you'll receive an error message.
- _Use the AWS CLI or SDK:_ You can use the AWS Command Line Interface or an
  AWS SDK in your preferred programming language to test the permissions. For example, with the AWS Command Line Interface,
  you can run the `aws sts get-caller-identity` command to verify your current user permissions.
- _Check the AWS CloudTrail logs:_ [Review the CloudTrail logs](../../../awscloudtrail/latest/userguide/view-cloudtrail-events-console.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events-console.md")
  to see if the actions you're trying to perform are being logged. This can help you identify any permission issues.
- _Use the IAM policy simulator:_ [The IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md")
  is a tool that allows you to test IAM policies and see the effect they have on your permissions.

###### Note

The specific steps might vary depending on the AWS service and the actions you're trying to perform.
