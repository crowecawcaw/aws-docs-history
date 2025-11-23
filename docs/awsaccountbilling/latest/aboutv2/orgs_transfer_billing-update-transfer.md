# Updating transfers

When you sign in to your organization's management account, you can update the name assigned to transfers that allow you to manage and pay for another organization’s consolidated bill.
This can help you identify and organize your transfers.

The name is only visible to you and any account that inherits the transfer.

## Update a transfer

###### Terms and concepts

The following are terms and concepts used in the AWS Billing and Cost Management console:

- **Inbound billing**: Billing transfers that allow you to manage and pay for another organization’s consolidated bill.
- **Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.

###### Minimum permissions

To update a transfer, your must have the following permissions:

- `organizations:ListInboundResponsibilityTransfers`
- `organizations:ListOutboundResponsibilityTransfers`
- `organizations:UpdateResponsibilityTransfer`

To update a transfer, complete the following steps.

###### To update a transfer

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. On the left navigation in **Preferences and Settings**, choose **Billing transfers**.
3. On the **Inbound billing** tab, select the transfer you want to update.
4. Choose the **Actions** dropdown menu, and then chose **Edit name**.
5. On the **Edit the transfer name** dialogue box, enter a new name and choose **Update name**.

###### To update a transfer

You can use one of the following operations:

- AWS CLI: [list-inbound-responsibility-transfers](../../../cli/latest/reference/organizations/list-inbound-responsibility-transfers.md "../../../cli/latest/reference/organizations/list-inbound-responsibility-transfers.md"), [list-outbound-responsibility-transfers](../../../cli/latest/reference/organizations/list-outbound-responsibility-transfers.md "../../../cli/latest/reference/organizations/list-outbound-responsibility-transfers.md"), and [update-responsibility-transfer](../../../cli/latest/reference/organizations/describe-responsibility-transfer.md "../../../cli/latest/reference/organizations/describe-responsibility-transfer.md")
  1.  Run the following command to find the billing transfer ID for inbound billings:

  ```
  `$` `C:\>` **aws organizations list-inbound-responsibility-transfers \
   --type BILLING**
  ```

  2.  From the response, note the billing transfer ID for the transfer you want to update.
  3.  Run the following command to update the transfer:

  ```
  `$` `C:\>` **aws organizations update-responsibility-transfer \
   --id `exampleid`
   --name `"Updated name for billing transfer"`**
  ```

- AWS SDKs: [list-inbound-responsibility-transfers](../../../cli/latest/reference/organizations/API_ListInboundResponsibilityTransfers.md "../../../cli/latest/reference/organizations/API_ListInboundResponsibilityTransfers.md"), [list-outbound-responsibility-transfers](../../../organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.md "../../../organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.md"), and [update-responsibility-transfer](../../../organizations/latest/APIReference/API_DescribeResponsibilityTransfer.md "../../../organizations/latest/APIReference/API_DescribeResponsibilityTransfer.md")
