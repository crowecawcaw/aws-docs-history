# Sending

invitations

When you sign in to your organization's management account, you can invite the management
account of another organization to designate your account to manage and pay their
consolidated bill.

## Considerations

**Only management accounts can send invitations**

Invitations can only be sent between management accounts.

**Invitations are unidirectional**

Only the account that will manage and pay for the consolidated bill (bill-transfer
account) can send invitations. Bill-source accounts cannot send invitations asking other
accounts to manage and pay for their consolidated bill.

**Invitations must be accepted before the start
date**

Invites must be accepted 24 hours before the billing transfer start date. For example,
an invitation with a start date of May 1st, needs to be accepted by April 29th 6:59:59PM
Eastern Standard Time (11:59:59 PM UTC), which is two days before the start date.

**Transfers start at the beginning of month**

If an invitation is accepted, the start date is 00:00:00 UTC on the first day of the month specified in the invitation (for Eastern Standard Time this is 7:00 PM on the evening before the first day of the month).

## Send an invitation

To send a billing transfer invitation, complete the following steps.

###### Terms and concepts

The following are terms and concepts used in the AWS Billing and Cost Management console:

- **Inbound billing**: Billing transfers that allow you to
  manage and pay for another organization’s consolidated bill.
- **Outbound billing**: Billing transfers that allow an
  account outside your organization to manage and pay your consolidated
  bill.

###### Minimum permissions

To send an invitation, you must have the following permissions:

- `organizations:InviteOrganizationToTransferResponsibility`
- `billingconductor:CreateBillingGroup`
- `billingconductor:ListPricingPlans`

###### To send an invitation

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the left navigation in **Preferences and
   Settings**, choose **Billing
   transfers**.
3. On the **Billing transfers** page, select the
   **Inbound billing** tab.
4. On the **Inbound billing** page, choose
   **Send invitation**.
5. On the **Send a billing transfer invitation**
   page, enter the following information:
   - **Name:** Name you want to
     assign to the transfer.

   ###### Note

   When you use two-level billing transfer as a bill
   receiver account, you can control the names only for
   your direct transfers. The bill transfer accounts
   control transfer names for their bill source accounts.
   For distribution partners, we recommend using your
   downstream sellers' names consistently for each billing
   transfer. This helps you search for all billing
   transfers associated with a specific downstream
   seller.
   - **Email address or account ID of the
     AWS management account:** Account you want to
     invite. This must be the management account of an
     organization.
   - **Monthly billing period
     start:** Start date when your account will
     begin managing and paying for their consolidated bills. It
     can be either the first day of the next month or two months
     in the future.

   ###### Note

   The start date is the first day of the month you
   select. Transfers begin on the start date regardless of
   the date the invitation is accepted. Invitations expire
   at 8 PM Eastern Standard Time two days before the start
   date.
   - **Pricing configuration:**
     Pricing seen by the _bill-source account_
     once the transfer begins.
   - **(Optional) Message to include in the
     request**: Text included in the email sent to
     the management account. For example, "Hello account owner,
     I'd like to pay your organization's consolidated
     bill."
   - **(Optional) Add new tags**:
     Specify one or more tags that are automatically applied to
     the inbound transfer. To do this, choose **Add
     tag** and then enter a key and an optional
     value. Leaving the value blank sets it to an empty string;
     it isn't `null`. You can attach up to 50 tags to
     an inbound transfer.

6. On the **Send a billing transfer invitation**
   page, choose **Send invitation**.

###### To send an invitation

You can use one of the following operations:

- AWS CLI: [invite-organization-to-transfer-responsibility](../../../cli/latest/reference/organizations/invite-organization-to-transfer-responsibility.md "../../../cli/latest/reference/organizations/invite-organization-to-transfer-responsibility.md")

```
`$` `C:\>`  **organizations invite-organization-to-transfer-responsibility \
 --type BILLING \
 --target '[{"Id":"`123456789012`","Type":"`ACCOUNT`"}]' \
 --start-timestamp `yyyy‑MM‑dd HH:mm:ss.SSS` \
 --sourceName `"My billing transfer"` \
 --notes `"Optional notes for the invitation"`
 --tags '[{"Key":"`exampleKey`","`Value`":"`exampleValue`"}]'**
```

- **`type` (Required)**:
  `BILLING`.
- **`target` (Required)**: A
  `HandshakeParty` object. Contains details for the
  account you want to invite.

* `Id`: Email address or account ID of the account you
  want to invite. For example,
  `{"Id":"alejandro_rosalez@example.com","Type":"EMAIL"}`

* `Type`: The type of ID for the participant:
  `ACCOUNT` or `EMAIL`.

- **`start-timestamp`
  (Required)**: Start date when your account will begin
  managing and paying for their consolidated bill. It can be either
  the first day of the next month or two months in the future. It must
  be the beginning of the day (00:00:00.000).

###### Note

The start date is the first day of the month you select.
Transfers begin on the start date regardless of the date the
invitation is accepted. Invitations expire at 8 PM Eastern
Standard Time two days before the start date.

- **`sourceName`
  (Optional)**: Name you want to assign to the
  transfer.
- **`notes` (Optional)**:
  Text included in the email sent to the management account. For
  example, "Hello account owner, I'd like to pay your organization's
  consolidated bill."
- **`tags (Optional)`**:
  Specify one or more tags that are automatically applied to the
  inbound transfer. You can attach up to 50 tags to an inbound
  transfer.
- AWS SDKs: [InviteOrganizationToTransferResponsibility](../../../organizations/latest/APIReference/API_InviteOrganizationToTransferResponsibility.md "../../../organizations/latest/APIReference/API_InviteOrganizationToTransferResponsibility.md")

###### What to do next

You will receive an email notification if you get a response to your invitation.
After you send an invitation you can monitor the status in the AWS Billing and Cost Management console or
using the . For more information, see [View invitation](orgs_transfer_billing-view-invitation.md "orgs_transfer_billing-view-invitation.md").
