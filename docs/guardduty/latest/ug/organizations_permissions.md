# Permissions required to designate a

delegated GuardDuty administrator account

To start using Amazon GuardDuty with AWS Organizations, the AWS Organizations management account for the
organization designates an account as the delegated GuardDuty administrator account. This enables GuardDuty as a trusted
service in AWS Organizations. It also enables GuardDuty for the delegated GuardDuty administrator account and also allows the delegated
administrator account to enable and manage GuardDuty for other accounts in the organization in the current
Region. For information about how these permissions are granted, see [Using AWS Organizations
with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md").

As the AWS Organizations management account, before you designate the delegated GuardDuty administrator account for your
organization, verify that you can perform the following GuardDuty action:
`guardduty:EnableOrganizationAdminAccount`. This action allows you to
designate the delegated GuardDuty administrator account for your organization by using GuardDuty. You must also ensure that
you are allowed to perform the AWS Organizations actions that help you retrieve information about
your organization.

To grant these permissions, include the following statement in an AWS Identity and Access Management (IAM)
policy for your account:

```
{
    "Sid": "PermissionsForGuardDutyAdmin",
    "Effect": "Allow",
    "Action": [
        "guardduty:EnableOrganizationAdminAccount",
        "organizations:EnableAWSServiceAccess",
        "organizations:RegisterDelegatedAdministrator",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:DescribeOrganizationalUnit",
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization",
        "organizations:ListAccounts"
    ],
    "Resource": "*"
}
```

If you want to designate your AWS Organizations management account as the delegated GuardDuty administrator account, your account
will also need the IAM action: `CreateServiceLinkedRole`. This action
allows you to initialize GuardDuty for the management account. However, review [Considerations and recommendations for using
GuardDuty with AWS Organizations](guardduty_organizations.md#delegated_admin_important "guardduty_organizations.md#delegated_admin_important")
before you proceed to add the permissions.

To continue with designating the management account as the delegated GuardDuty administrator account, add the following
statement to the IAM policy and replace
`111122223333` with the AWS account ID of your
organization's management account:

```
{
	"Sid": "PermissionsToEnableGuardDuty"
	"Effect": "Allow",
	"Action": [
		"iam:CreateServiceLinkedRole"
	],
	"Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty",
	"Condition": {
		"StringLike": {
			"iam:AWSServiceName": "guardduty.amazonaws.com"
		}
	}
}
```
