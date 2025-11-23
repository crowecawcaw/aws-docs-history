# Withdrawing

transfers

When you sign in to your organization's management account, you can withdraw a transfer at
any time. The transfer continues until the end date.

Consolidated bills for charges accrued before the end date are managed and paid for by the
_bill-transfer account_. After the transfer ends, all consolidated
bills for charges accrued thereafter are managed and paid for by the organization's own
management account _(bill-source account)_.

## Considerations

**Withdrawal can be done by either account in a
transfer**

Either account involved in a transfer can withdraw the transfer at any time.

**Withdrawal cannot be undone**

If a transfer is withdrawn, the account that was managing and paying for another
organization's consolidated bill must send a new invitation to that organization to
start again.

**Transfers end at the end of the month**

If a transfer is withdrawn, the end date is 23:59:59 UTC on the last day of the month specified in the withdrawal. Note, this is 6:59 PM Eastern Standard Time on the evening before the last day of the month.

## Withdraw a transfer

###### Terms and concepts

The following are terms and concepts used in the AWS Billing and Cost Management console:

- **Inbound billing**: Billing transfers that allow you to
  manage and pay for another organization’s consolidated bill.
- **Outbound billing**: Billing transfers that allow an
  account outside your organization to manage and pay your consolidated
  bill.

###### Minimum permissions

To withdraw a transfer, you must have the following permissions:

- `organizations:ListInboundResponsibilityTransfers`
- `organizations:ListOutboundResponsibilityTransfers`
- `organizations:TerminateResponsibilityTransfer`

To withdraw a transfer, complete the following steps.

###### To withdraw a transfer

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the left navigation in **Preferences and
   Settings**, choose **Billing
   transfers**.
3. ###### For inbound billings:
   1. On the **Billing transfers** page, select
      the **Inbound billing** tab.
   2. On the **Inbound billing** tab, select
      the transfer you want to withdraw from.
   3. Choose the **Actions** dropdown menu, and
      then chose **Withdraw transfer**.
   4. On the confirmation dialogue box, select the month you
      want to end the transfer and choose **Withdraw
      transfer**.

4. ###### For outbound billings:
   1. On the **Billing transfers** page, select
      the **Outbound billing** tab.
   2. On the **Outbound billing** tab, choose
      **Withdraw transfer**.
   3. On the confirmation dialogue box, select the month you
      want to end the transfer and choose **Withdraw
      transfer**.

###### To withdraw a transfer

You can use one of the following operations:

- AWS CLI: [list-inbound-responsibility-transfers](../../../cli/latest/reference/organizations/list-inbound-responsibility-transfers.md "../../../cli/latest/reference/organizations/list-inbound-responsibility-transfers.md"), [list-outbound-responsibility-transfers](../../../cli/latest/reference/organizations/list-outbound-responsibility-transfers.md "../../../cli/latest/reference/organizations/list-outbound-responsibility-transfers.md"), and [terminate-responsibility-transfer](../../../cli/latest/reference/organizations/terminate-responsibility-transfer.md "../../../cli/latest/reference/organizations/terminate-responsibility-transfer.md")
  1.  **For inbound
      billing:**

  Run the following command to find the billing transfer ID
  for inbound billings:

  ```
  `$` `C:\>` **aws organizations list-inbound-responsibility-transfers \
   --type BILLING**
  ```

  **For outbound
  billing:**

  Run the following command to find the billing transfer ID
  for outbound billings:

  ```
  `$` `C:\>` **aws organizations list-outbound-responsibility-transfers \
   --type BILLING**
  ```

  2.  From the response, note the billing transfer ID for the
      transfer you want to withdraw.
  3.  Run the following command to withdraw the transfer:

  ```
  `$` `C:\>` **aws organizations terminate-responsibility-transfer \
   --responsibility-id `exampleid` \
  --end-timestamp `exampletimestamp`**
  ```

- AWS SDKs: [list-inbound-responsibility-transfers](../../../cli/latest/reference/organizations/API_ListInboundResponsibilityTransfers.md "../../../cli/latest/reference/organizations/API_ListInboundResponsibilityTransfers.md"), [list-outbound-responsibility-transfers](../../../organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.md "../../../organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.md"), and [terminate-responsibility-transfer](../../../organizations/latest/APIReference/API_TerminateResponsibilityTransfer.md "../../../organizations/latest/APIReference/API_TerminateResponsibilityTransfer.md")

###### Note

When a transfer is withdrawn, the bill transfer account continues to access
billing transfer views associated with the withdrawn transfers. This allows auditing
of historical cost and usage data.

When you withdraw from billing transfer as a bill source account, you receive
AWS invoices for charges that occur after the withdrawal. You view cost and usage
data as computed by AWS from the standard billable domain instead of rates set by
the bill transfer account. During this transition, you lose access to historical
data in Cost Explorer (data remains but becomes inaccessible). The transition also
marks your AWS Cost and Usage Report preferences as `unhealthy`. You must reconfigure
your AWS Cost and Usage Report preferences for your files to correctly show your billable cost and
usage data. For more information, see [Controlling cost
management data access with Billing View](../../../cost-management/latest/userguide/billing-view.md "../../../cost-management/latest/userguide/billing-view.md") and [AWS Cost and Usage Report](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md").
