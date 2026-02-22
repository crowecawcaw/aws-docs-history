# Using service control policies to restrict

Amazon Quick sign-up options

If you're an administrator in AWS Organizations, you can use service control policies (SCPs) to
restrict how individuals in your organization can sign up for Amazon Quick. You can restrict
the edition of Quick they can sign up for, and also the type of user that they
can sign up for.

AWS Organizations is a user account management service that you can use to consolidate multiple
AWS accounts into an organization that you create and centrally manage. You can use SCPs
in AWS Organizations to manage the permissions in your organization. For more information, see [What
is AWS Organizations?](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") and [Service control
policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.

In the following topic, you can learn about two ways to restrict Quick sign-up
options using SCPs in AWS Organizations. The topic includes an example SCP. To learn more about
creating SCPs, see the following topics in the _AWS Organizations User Guide_:

- [Creating, updating, and deleting service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md")
- [SCP
  syntax](../../../organizations/latest/userguide/orgs_manage_policies_scps_syntax.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_syntax.md")
- [Strategies for using SCPs](../../../organizations/latest/userguide/orgs_manage_policies_scps_strategies.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_strategies.md")

###### Topics

- [Restricting the Quick edition](#security-scp-edition "#security-scp-edition")
- [Restricting user management options](#security-scp-user "#security-scp-user")
- [Example SCP](#security-scp-example "#security-scp-example")

## Restricting the Quick edition

To restrict the edition of Quick that your managed accounts can sign up
for, use the `quicksight:Edition` condition key in your SCP. The values for
this key are listed and described in the following table.

| Key Name             | Key Value    | Description                     |
| -------------------- | ------------ | ------------------------------- |
| `quicksight:Edition` | `standard`   | Amazon Quick Standard Edition   |
|                      | `enterprise` | Amazon Quick Enterprise Edition |

## Restricting user management options

To restrict the user management options that individuals in your organization can use
to sign up for Quick, use the `quicksight:DirectoryType`
condition key in your SCP. The values for this key are listed and described in the
following table.

| Key Name                   | Key Value             | Description                                                                                                                                 |
| -------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `quicksight:DirectoryType` | `quicksight`          | IAM federated identities and Amazon Quick-managed users                                                                                     |
|                            | `iam`                 | Only IAM federated identities                                                                                                               |
|                            | `microsoft_ad`        | Users managed in Microsoft Active Directory on AWS Directory Service for Microsoft Active Directory                                         |
|                            | `ad_connector`        | Users managed in on-premises Active Directory and connected<br>through AD_Connector to AWS Directory Service for Microsoft Active Directory |
|                            | `iam_identity_center` | Users managed in a Amazon Quick account that is integrated with<br>IAM Identity Center.                                                     |

## Example SCP

The following example for Quick shows a service control policy that denies
signing up for a Amazon Quick Standard Edition and prevents the ability to sign up
using IAM Identity Center authentication. This policy uses the
`quicksight:Subscribe` action, in addition to the condition keys
previously described. For a list of Amazon Quick-specific keys for use in IAM
permission policies, see [Actions,
resources, and condition keys for Quick](../../../service-authorization/latest/reference/list_amazonquicksight.md "../../../service-authorization/latest/reference/list_amazonquicksight.md") in the
_Service Authorization Reference_.

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Deny",
            "Action": [
                "quicksight:Subscribe"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "quicksight:DirectoryType": [
                        "iam_identity_center"
                    ]
                }
            }
        },
        {
            "Sid": "Statement2",
            "Effect": "Deny",
            "Action": [
                "quicksight:Subscribe"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringEquals": {
                    "quicksight:Edition": "standard"
                }
            }
        }
    ]
}
```

With this policy in effect, individuals in an organization can sign up only for
Amazon Quick Enterprise Edition, and they must use authentication methods other than
IAM Identity Center. If they try to sign up for Amazon Quick Standard Edition or attempt
to use IAM Identity Center authentication, they will be restricted from signing up and
receive a message explaining that they don't have the right permissions.
