

# Accepting or declining account invitations with AWS Organizations
<a name="orgs_manage_accounts_accept-decline-invite"></a>

If you receive an invitation to join an organization, you can accept or decline the invitation.

## Considerations
<a name="orgs_manage_accounts_accept-decline-invite-considerations"></a>

**An account’s status with an organization affects what cost and usage data is visible**

If a member account leaves an organization and becomes a standalone account, the account no longer has access to cost and usage data from the time range when the account was a member of the organization. The account has access only to the data that is generated as a standalone account.

If a member account leaves organization A to join organization B, the account no longer has access to cost and usage data from the time range when the account was a member of organization A. The account has access only to the data that is generated as a member of organization B.

If an account rejoins an organization that it previously belonged to, the account regains access to its historical cost and usage data.

**Only member accounts and standalone accounts can accept or decline an invitation**

Only member accounts and standalone accounts can accept or decline an invitation to join an organization. If an invitation is sent to a management account that is already part of an organization, that account won't be able to view the invitation until they [remove all member accounts from their organization](orgs_manage_accounts_remove.md) and [delete the organization](orgs_manage_org_delete.md).

**CloudTrail logging takes place in the account taking the action **

If a member account or standalone account accepts or declines an account invitation, that action will be logged in the CloudTrail log of the acting account. If the acting account is a member account, that action will not be logged in the management account's CloudTrail logs. This is consistent with CloudTrail logging in related scenarios (ex. Member account leaving organization will be logged in member account trail, management account removing member account will be logged in management account trail). 

## Accept or decline to an account invitation
<a name="orgs_manage_accounts_accept-decline-invite-steps"></a>

To accept or decline the invitation, complete the following steps.

**Minimum permissions**  
To accept or decline an invitation to join an organization, you must have the following permissions:  
`organizations:ListHandshakesForAccount` – Required to see the list of invitations in the AWS Organizations console.
`organizations:AcceptHandshake`.
`organizations:DeclineHandshake`.
`organizations:LeaveOrganization` – Required only when accepting an invitation when your account is already a member of an organization.
`iam:CreateServiceLinkedRole` – Required only when accepting the invitation requires the creation of a service-linked role in the member account to support integration with other AWS services. For more information, see [AWS Organizations and service-linked roles](orgs_integrate_services.md#orgs_integrate_services-using_slrs).

------
#### [ AWS Management Console ]

**To accept or decline an invitation**

1. An invitation to join an organization is sent to the email address of the account owner. If you are an account owner and you receive an invitation email message, follow the instructions in the email invitation or go to [AWS Organizations console](https://console.aws.amazon.com/organizations/v2) in your browser, and then choose **Invitations**, or go straight to the **[member account's Invitation](https://console.aws.amazon.com/organizations/v2/home/invitations)** page.

1. If prompted, sign in to the invited account as an IAM user, assume an IAM role, or sign in as the account's root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)).

1. The **[member account's Invitation](https://console.aws.amazon.com/organizations/v2/home/invitations)** page displays your account's open invitations to join organizations.

   Choose **Accept invitation** or **Decline invitation** as appropriate.
   + If you choose **Accept invitation** in the preceding step, the console redirects you to the [Organization overview](https://console.aws.amazon.com/organizations/v2/home/dashboard) page with details about the organization that your account is now a member of. You can view the organization's ID and the owner's email address.
**Note**  
Accepted invitations continue to appear in the list for 30 days. After that, they are deleted and no longer appear in the list.

     AWS Organizations automatically creates a service-linked role in the new member account to support integration between AWS Organizations and other AWS services. For more information, see [AWS Organizations and service-linked roles](orgs_integrate_services.md#orgs_integrate_services-using_slrs).

     AWS sends an email message to the owner of the organization's management account stating that you accepted the invitation. It also sends an email message to the member account owner stating that the account is now a member of the organization.
   + If you choose **Decline** in the preceding step, your account remains on the **[member account's Invitation](https://console.aws.amazon.com/organizations/v2/home/invitations)** page that lists any other pending invitations.

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
                          "Value": "bill@amazon.com"
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