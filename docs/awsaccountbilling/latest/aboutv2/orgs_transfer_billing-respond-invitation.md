

# Responding to invitations
<a name="orgs_transfer_billing-respond-invitation"></a>

When you sign in to your organization's management account, you can respond to invitations you have received.

## Considerations
<a name="orgs_transfer_billing-respond-invitation-considerations"></a>

**Transfers are inherited**

If you are the *bill-transfer account* for another organization, and you accept a *billing transfer invitation* from a different account, that account becomes your *bill-transfer account* and will manage and pay for any consolidated bills that you manage and pay for.

**Transfers start at the beginning of month**

If an invitation is accepted, the start date is 00:00:00 UTC on the first day of the month specified in the invitation (for Eastern Standard Time this is 7:00 PM on the evening before the first day of the month).

**Invitations must be accepted before the start date**

Invites must be accepted 24 hours before the billing transfer start date. For example, an invitation with a start date of May 1st, needs to be accepted by April 29th 6:59:59PM Eastern Standard Time (11:59:59 PM UTC), which is two days before the start date.

## Respond to an invitation
<a name="orgs_transfer_billing-respond-invitation-steps"></a>

**Terms and concepts**  
The following are terms and concepts used in the AWS Billing and Cost Management console:  
**Inbound billing**: Billing transfers that allow you to manage and pay for another organization’s consolidated bill.
**Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.

**Minimum permissions**  
To respond to an invitation, you must have the following permissions actions:  
`organizations:ListHandshakesAccount`
`organizations:AcceptHandshake`
`organizations:DeclineHandshake`

To respond to an invitation, complete the following steps.

------
#### [  ]

**To respond to an invitation**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. On the left navigation in **Preferences and Settings**, choose **Billing transfers**.

1. On the **Billing transfers** page, select the **Outbound billing** tab.

1. On the **Outbound billing** tab, chose **View details** in the alert box.

1. On the details page for the invitation, choose **Decline** or **Accept**.

------
#### [  ]

**To respond to an invitation**  
You can use one of the following operations:
+ AWS CLI: [list-handshakes-for-account](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-handshakes-for-account.html), [accept-handshake](https://docs.aws.amazon.com/cli/latest/reference/organizations/accept-handshake.html), and [decline-handshake](https://docs.aws.amazon.com/cli/latest/reference/organizations/accept-decline.html)

  1. Run the following command to find the [handshake](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#invitations-handshakes) ID:

     ```
     $ C:\> aws organizations list-handshakes-for-account \
         --filter HandshakeType=TRANSFER_RESPONSIBILITY
     ```

  1. From the response, note the handshake ID for the invitation you want to respond to.

  1. **To accept the request:**

     Run the following command to accept the invitation:

     ```
     $ C:\> aws organizations accept-handshake \
         --handshake-id {{examplehandshakeid}}
     ```

     **To decline the request:**

     Run the following command to decline the invitation:

     ```
     $ C:\> aws organizations decline-handshake \
         --handshake-id {{examplehandshakeid}}
     ```
+ AWS SDKs: [ListHandshakesForAccount](https://docs.aws.amazon.com/cli/latest/reference/organizations/ListHandshakesForAccount.html), [AcceptHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_AcceptHandshake.html), and [DeclineHandshake](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DeclineHandshake.html)

------

**What to do next**  
After you accepting an invitation, you can monitor the status in the AWS Billing and Cost Management console or using the . For more information, see [View transfers](orgs_transfer_billing-view-transfer.md). If you decline an invitation or the invitation expires, the account that sent the invitation must send another one if you want to begin a transfer.