# Invite team members to collaborate in AWS Settings

###### Warning

We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

You can give team members access to your projects. When you share a project with a team
member, you cannot control which AWS services they have access to. Both you and the team
member have admin access to the project. This means, the team member has permissions to access
all AWS services available for your project. This includes creating access controls for
services and applications. However, they don't have permissions to perform
administrative or financial actions, such as deleting your project or modifying a spend
limit. To view which team member has modified an AWS service,
see [Monitor your project](monitor-your-project.md "monitor-your-project.md").

In AWS Settings, you and your team members have different levels of access. To view the
AWS managed policy that is applied to a team member, see [AWSManagedSettingsReadOnlyAccess](../../../aws-managed-policy/latest/reference/AWSManagedSettingsReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AWSManagedSettingsReadOnlyAccess.md"). To view the AWS managed policy that is applied
to a project owner, see [AWSManagedSettingsAdminAccess](../../../aws-managed-policy/latest/reference/AWSManagedSettingsAdminAccess.md "../../../aws-managed-policy/latest/reference/AWSManagedSettingsAdminAccess.md").

Consider the following when adding a team member to your project.

## Considerations for team members

A team member can do the following actions:

- View, create, edit, delete, and modify AWS resources in a project.
- Access AWS Settings.
- View spend limits.
- Request a quota increase for an AWS service.

A team member can't do the following actions:

- Leave a project.
- Take any root actions. For more information, see [AWS actions for project owners](aws-actions-project-owners.md "aws-actions-project-owners.md").
- Invite team members to projects.
- Manage any team member's permissions.
- Remove any team member from a project.
- Change the name of a project.
- Set up or update payment methods.
- View or update billing details, including address or phone number.
- View or update tax information.
- Upgrade from Free Tier to Paid Plan.
- Set or modify spend limits per projects.
- View cost trends for each project.
- View total AWS spending across all projects.
- View and redeem non-Free Tier promotional credits.
- View remaining credits and expiration dates for all credit types.
- View full credit history including earned, applied, and expired credits.
- View how credits apply across projects.
- View outstanding balance.
- Execute payments to AWS.
- Download invoices or view past transactions.
- Validate that AWS charges are correct, including credits applied.
- Receive management account-level billing communications.
- Get help with billing issues at the organization level.
- Request a quota increase for account and billing quotas.

## How team members access your AWS resources

Our new AWS experience creates a service-linked role for the organization that contains
all your projects that you cannot modify. This role periodically verifies that the internal
records of your team members stay in sync with your actual team members.

The **AWSServiceRoleForAccountAccessManager** service-linked role trusts the
following services to assume the role:

- `account-access.amazonaws.com`

The role permissions policy named `AccountAccessManagerServiceRolePolicy`
allows account access manager to complete the following actions on the specified
resources:

- Action: `organizations:ListAccounts`,
  `organizations:ListAWSServiceAccessForOrganization`,
  `organizations:DescribeAccount` on `"arn:aws:organizations::*:account/o-*/*"`

For more information, see [AWS Account Access Manager](../../../IAM/latest/UserGuide/account-access-manager.md "../../../IAM/latest/UserGuide/account-access-manager.md").

## Invite team members to collaborate in AWS Settings

To invite team members, you send them an invitation from the Team page in the
AWS Settings. Team members have 14 days to accept their invitation. Team members must
create a AWS Builder ID to access your project. They can do this using Sign up for AWS (new).

###### Invite team members to collaborate in AWS Settings

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com "https://settings.aws.com").
2. In the main navigation pane, choose **Team**.
3. Choose **Invite new team member**.
4. For **Email**, enter an email address or a list of email addresses.
   Separate the email addresses with commas (,) or semicolons (;).
5. Choose one or more projects to share with your new team members.
6. Choose **Send invitation**.

If your team members don't get the invitation, ask them to check their spam and trash
folders.
