# Permissions required to designate a

delegated Security Incident Response administrator account

You can chose to set up your AWS Security Incident Response membership using delegated administrator for AWS Organizations.
For information about how these permissions are granted, see [Using AWS Organizations
with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md").

###### Note

AWS Security Incident Response automatically enables the AWS Organizations trusted relationship when using the console for setup and management.
If you use the CLI/SDK then you have to manually enable this by using the [EnableAWSServiceAccess API](../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md "../../../organizations/latest/APIReference/API_EnableAWSServiceAccess.md")
to trust `security-ir.amazonaws.com`.

As the AWS Organizations manager, before you designate the delegated Security Incident Response administrator account for your
organization, verify that you can perform the following AWS Security Incident Response actions:
`security-ir:CreateMembership` and `security-ir:UpdateMembership`. These actions allow you to
designate the delegated Security Incident Response administrator account for your organization by using AWS Security Incident Response. You must also ensure that
you are allowed to perform the AWS Organizations actions that help you retrieve information about
your organization.

To grant these permissions, include the following statement in an AWS Identity and Access Management (IAM)
policy for your account:

```

        {
            "Sid": "PermissionsForSIRAdmin",
            "Effect": "Allow",
            "Action": [
                "security-ir:CreateMembership",
                "security-ir:UpdateMembership",
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

If you want to designate your AWS Organizations management account as the delegated Security Incident Response administrator account, your account
will also need the IAM action: `CreateServiceLinkedRole`. Review [Considerations and recommendations for using
AWS Security Incident Response with AWS Organizations](considerations_important.md "considerations_important.md")
before you proceed to add the permissions.

To continue with designating your AWS Organizations management account as the delegated Security Incident Response administrator account,
add the following statement to the IAM policy and replace
`111122223333` with the AWS account ID of your
AWS Organizations management account:

```

        {
        	"Sid": "PermissionsToEnableSecurityIncidentResponse"
        	"Effect": "Allow",
        	"Action": [
        		"iam:CreateServiceLinkedRole"
        	],
        	"Resource": "arn:aws:iam::`111122223333`:role/aws-service-role/security-ir.amazonaws.com/AWSServiceRoleForSecurityIncidentResponse",
        	"Condition": {
        		"StringLike": {
        			"iam:AWSServiceName": "security-ir.amazonaws.com"
        		}
        	}
        }

```
