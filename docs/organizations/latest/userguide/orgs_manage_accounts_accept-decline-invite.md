

# Accepting or declining account invitations with AWS Organizations
<a name="orgs_manage_accounts_accept-decline-invite"></a>

If you receive an invitation to join an organization, you can accept or decline the invitation.

## Considerations
<a name="orgs_manage_accounts_accept-decline-invite-considerations"></a>

**An account's status with an organization affects what cost and usage data is visible**

A member account can leave an organization and become a standalone account. It then loses access to cost and usage data from its time in the organization. It can see only the data that it creates as a standalone account.

A member account can leave organization A to join organization B. It then loses access to cost and usage data from its time in organization A. It can see only the data that it creates as a member of organization B.

If an account rejoins an organization that it was in before, it gets back access to its past cost and usage data.

**Only member accounts and standalone accounts can accept or decline an invitation**

Only member accounts and standalone accounts can accept or decline an invitation to join an organization. A management account that is already part of an organization can't see an invitation. To see it, that account must first [remove all member accounts from its organization](orgs_manage_accounts_remove.md). Then it must [delete the organization](orgs_manage_org_delete.md).

**CloudTrail logging takes place in the account taking the action **

When a member account or standalone account accepts or declines an invitation, CloudTrail logs the action in that account. If that account is a member account, the management account's CloudTrail logs don't show the action. Other CloudTrail actions work the same way. For example, CloudTrail logs a member account leaving an organization in that account's trail, and logs the management account removing a member account in the management account's trail.

## Accept or decline to an account invitation
<a name="orgs_manage_accounts_accept-decline-invite-steps"></a>

To accept or decline the invitation, complete the following steps.

**Minimum permissions**  
To accept or decline an invitation to join an organization, you must have the following permissions:  
`organizations:ListHandshakesForAccount` – Required to see the list of invitations in the AWS Organizations console.
`organizations:AcceptHandshake`.
`organizations:DeclineHandshake`.
`organizations:LeaveOrganization` – Required only when your account is already a member of an organization. If a [service control policy (SCP)](orgs_manage_policies_scps.md) in your current organization denies this action, you can't accept the invitation.
`iam:CreateServiceLinkedRole` – Required only when accepting the invitation creates a service-linked role in the member account. This role supports integration with other AWS services. For more information, see [AWS Organizations and service-linked roles](orgs_integrate_services.md#orgs_integrate_services-using_slrs).

------
#### [ AWS Management Console ]

**To accept or decline an invitation**

1. AWS sends the invitation to the email address of the account owner. If you get an invitation email, follow the instructions in the email. You can also open the **[member account's Invitation](https://console.aws.amazon.com/organizations/v2/home/invitations)** page directly in your browser.

1. If prompted, sign in to the invited account as an IAM user, assume an IAM role, or sign in as the account's root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)).

1. The **[member account's Invitation](https://console.aws.amazon.com/organizations/v2/home/invitations)** page displays your account's open invitations to join organizations.

   Choose **Accept invitation** or **Decline invitation** as appropriate.
   + If you chose **Accept invitation**, you go to the [Organization overview](https://console.aws.amazon.com/organizations/v2/home/dashboard) page with details about the organization that your account is now a member of. You can view the organization's ID and the owner's email address.
**Note**  
Accepted invitations continue to appear in the list for 30 days. After that, they are deleted and no longer appear in the list.

     AWS Organizations automatically creates a service-linked role in the new member account to support integration between AWS Organizations and other AWS services. For more information, see [AWS Organizations and service-linked roles](orgs_integrate_services.md#orgs_integrate_services-using_slrs).

     AWS sends an email message to the owner of the organization's management account stating that you accepted the invitation. It also sends an email message to the member account owner stating that the account is now a member of the organization.
   + If you chose **Decline**, your account remains on the **[member account's Invitation](https://console.aws.amazon.com/organizations/v2/home/invitations)** page that lists any other pending invitations.

     AWS sends an email message to the organization's management account owner stating that you declined the invitation.
**Note**  
Declined invitations continue to appear in the list for 30 days. After that, they are deleted and no longer appear in the list.

------
#### [ AWS CLI & AWS SDKs ]

**To accept or decline an invitation**  
You can use the following commands to accept or decline an invitation:
+ AWS CLI: [accept-handshake](https://docs.aws.amazon.com/cli/latest/reference/organizations/accept-handshake.html), [decline-handshake](https://docs.aws.amazon.com/cli/latest/reference/organizations/decline-handshake.html) 

  The following example shows how to accept an invitation to join an organization.

  ```
  $ aws organizations accept-handshake --handshake-id h-examplehandshakeid111
  {
      "Handshake": {
          "Action": "INVITE",
          "Arn": "arn:aws:organizations::111111111111:handshake/o-exampleorgid/invite/h-examplehandshakeid111",
          "RequestedTimestamp": 1481656459.257,
          "ExpirationTimestamp": 1482952459.257,
          "Id": "h-examplehandshakeid111",
          "Parties": [
              {
                  "Id": "o-exampleorgid",
                  "Type": "ORGANIZATION"
              },
              {
                  "Id": "juan@example.com",
                  "Type": "EMAIL"
              }
          ],
          "Resources": [
              {
                  "Resources": [
                      {
                          "Type": "MASTER_EMAIL",
                          "Value": "bill@example.com"
                      },
                      {
                          "Type": "MASTER_NAME",
                          "Value": "Management Account"
                      },
                      {
                          "Type": "ORGANIZATION_FEATURE_SET",
                           "Value": "ALL"
                      }
                  ],
                  "Type": "ORGANIZATION",
                  "Value": "o-exampleorgid"
              },
              {
                  "Type": "EMAIL",
                  "Value": "juan@example.com"
              }
          ],
          "State": "ACCEPTED"
      }
  }
  ```

  The following example shows how to decline an invitation to join an organization.
+ AWS SDKs: [AcceptHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AcceptHandshake.html), [DeclineHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeclineHandshake.html)

------