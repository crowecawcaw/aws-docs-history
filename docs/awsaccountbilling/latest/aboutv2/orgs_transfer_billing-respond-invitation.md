# Responding to

invitations

When you sign in to your organization's management account, you can respond to invitations
you have received.

## Considerations

**Transfers are inherited**

If you are the _bill-transfer account_ for another organization,
and you accept a _billing transfer invitation_ from a different
account, that account becomes your _bill-transfer account_ and will
manage and pay for any consolidated bills that you manage and pay for.

**Transfers start at the beginning of month**

If an invitation is accepted, the start date is 00:00:00 UTC on the first day of the month specified in the invitation (for Eastern Standard Time this is 7:00 PM on the evening before the first day of the month).

**Invitations must be accepted before the start
date**

Invites must be accepted 24 hours before the billing transfer start date. For example, an invitation with a start date of May 1st, needs to be accepted by April 29th 6:59:59PM Eastern Standard Time (11:59:59 PM UTC), which is two days before the start date.

## Respond to an

invitation

###### Terms and concepts

The following are terms and concepts used in the AWS Billing and Cost Management console:

- **Inbound billing**: Billing transfers that allow you to
  manage and pay for another organization’s consolidated bill.
- **Outbound billing**: Billing transfers that allow an
  account outside your organization to manage and pay your consolidated
  bill.

###### Minimum permissions

To respond to an invitation, you must have the following permissions
actions:

- `organizations:ListHandshakesAccount`
- `organizations:AcceptHandshake`
- `organizations:DeclineHandshake`

To respond to an invitation, complete the following steps.

###### To respond to an invitation

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the left navigation in **Preferences and
   Settings**, choose **Billing
   transfers**.
3. On the **Billing transfers** page, select the
   **Outbound billing** tab.
4. On the **Outbound billing** tab, chose
   **View details** in the alert box.
5. On the details page for the invitation, choose
   **Decline** or
   **Accept**.

###### To respond to an invitation

You can use one of the following operations:

- AWS CLI: [list-handshakes-for-account](../../../cli/latest/reference/organizations/list-handshakes-for-account.md "../../../cli/latest/reference/organizations/list-handshakes-for-account.md"), [accept-handshake](../../../cli/latest/reference/organizations/accept-handshake.md "../../../cli/latest/reference/organizations/accept-handshake.md"), and [decline-handshake](../../../cli/latest/reference/organizations/accept-decline.md "../../../cli/latest/reference/organizations/accept-decline.md")
  1.  Run the following command to find the [handshake](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#invitations-handshakes "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#invitations-handshakes") ID:

  ```
  `$` `C:\>` **aws organizations list-handshakes-for-account \
   --filter HandshakeType=TRANSFER\_RESPONSIBILITY**
  ```

  2.  From the response, note the handshake ID for the
      invitation you want to respond to.
  3.  **To accept the
      request:**

  Run the following command to accept the invitation:

  ```
  `$` `C:\>` **aws organizations accept-handshake \
   --handshake-id `examplehandshakeid`**
  ```

  **To decline the
  request:**

  Run the following command to decline the
  invitation:

  ```
  `$` `C:\>` **aws organizations decline-handshake \
   --handshake-id `examplehandshakeid`**
  ```

- AWS SDKs: [ListHandshakesForAccount](../../../cli/latest/reference/organizations/ListHandshakesForAccount.md "../../../cli/latest/reference/organizations/ListHandshakesForAccount.md"), [AcceptHandshake](../../../organizations/latest/APIReference/API_AcceptHandshake.md "../../../organizations/latest/APIReference/API_AcceptHandshake.md"), and [DeclineHandshake](../../../organizations/latest/APIReference/API_DeclineHandshake.md "../../../organizations/latest/APIReference/API_DeclineHandshake.md")

###### What to do next

After you accepting an invitation, you can monitor the status in the AWS Billing and Cost Management
console or using the . For more information, see [View transfers](orgs_transfer_billing-view-transfer.md "orgs_transfer_billing-view-transfer.md"). If you
decline an invitation or the invitation expires, the account that sent the
invitation must send another one if you want to begin a transfer.
