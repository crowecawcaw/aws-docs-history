# Using service control policies to restrict Amazon Quick sign-up options

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
- [Restricting which accounts can create Quick subscriptions](#security-scp-centralize "#security-scp-centralize")

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

| Key Name                   | Key Value             | Description                                                                                                                                  |
| -------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `quicksight:DirectoryType` | `quicksight`          | IAM federated identities and Amazon Quick-managed users                                                                                      |
|                            | `iam`                 | Only IAM federated identities                                                                                                                |
|                            | `microsoft_ad`        | Users managed in Microsoft Active Directory on AWS Directory Service for Microsoft Active Directory                                          |
|                            | `ad_connector`        | Users managed in on-premises Active Directory and connected<br>through AD\_Connector to AWS Directory Service for Microsoft Active Directory |
|                            | `iam_identity_center` | Users managed in a Amazon Quick account that is integrated with<br>IAM Identity Center.                                                      |

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
    "Version": "2012-10-17",
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

## Restricting which accounts can create Quick subscriptions

In addition to restricting the edition and the user management options that
individuals can sign up for, you can use an SCP to control _which_
AWS accounts in your organization are allowed to create a Amazon Quick subscription.
This helps you centralize Quick on a set of approved accounts and prevent
individuals from starting new subscriptions in other accounts.

Two actions can create a Amazon Quick subscription:
`quicksight:Subscribe` and `quicksight:CreateAccountSubscription`.
If a policy denies either action, the deny takes effect and the attempt to create a
subscription fails. To restrict subscription creation, include both actions in your
`Deny` statement.

The following example SCP denies both actions in every account except the approved
accounts that you list. The policy uses the `aws:PrincipalAccount` global
condition key to compare the account of the principal making the request against your
approved accounts. Replace the example account IDs with the IDs of the accounts where
you allow Quick subscriptions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Deny",
            "Action": [
                "quicksight:Subscribe",
                "quicksight:CreateAccountSubscription"
            ],
            "Resource": [
                "*"
            ],
            "Condition": {
                "StringNotEquals": {
                    "aws:PrincipalAccount": [
                        "111111111111",
                        "222222222222"
                    ]
                }
            }
        }
    ]
}
```

With this policy in effect, only principals in the listed accounts can create a
Amazon Quick subscription. Principals in any other account in your organization are
prevented from signing up, and they receive a message explaining that they don't have
the right permissions.

As an alternative to using the condition key, you can attach a `Deny`
statement for the same two actions (without the `aws:PrincipalAccount`
condition) to every organizational unit (OU) except the OU that contains your approved
accounts. For more information about where to attach policies, see [Strategies for using SCPs](../../../organizations/latest/userguide/orgs_manage_policies_scps_strategies.md "../../../organizations/latest/userguide/orgs_manage_policies_scps_strategies.md") in the _AWS Organizations User Guide_.
