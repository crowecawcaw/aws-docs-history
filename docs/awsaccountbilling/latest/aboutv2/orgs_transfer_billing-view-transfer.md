

# Viewing transfers
<a name="orgs_transfer_billing-view-transfer"></a>

When you sign in to your organization's management account, you can view your transfers.

## Status
<a name="orgs_transfer_billing-view-transfer-status"></a>

The following are the statuses for transfers:
+ **Transfer accepted** (`ACCEPTED`): Invitation was accepted by the recipient. The transfer begins on the start date.
+ **Transfer withdrawn** (`WITHDRAWN`): Transfer has been withdrawn. The transfer ends on the end date.

![Status panel showing Transfer accepted in green and Transfer withdrawn in gray.](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/images/transfer-billing-relationship-statuses.png)


*Figure 1: Transfer statuses as displayed in the AWS Billing and Cost Management console.*

## View a transfer
<a name="orgs_transfer_billing-view-transfers-steps"></a>

**Terms and concepts**  
The following are terms and concepts used in the AWS Billing and Cost Management console:  
**Inbound billing**: Billing transfers that allow you to manage and pay for another organization's consolidated bill.
**Outbound billing**: Billing transfers that allow an account outside your organization to manage and pay your consolidated bill.

**Minimum permissions**  
To view a transfer, you must have the following permissions  
`organizations:ListInboundResponsibilityTransfers`
`organizations:ListOutboundResponsibilityTransfers`
`organizations:DescribeResponsibilityTransfer`

To view a transfer, complete the following steps.

------
#### [  ]

**To view a transfer**

1. Sign in to the AWS Management Console and open the AWS Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. On the left navigation in **Preferences and Settings**, choose **Billing transfers**.

1. 

**For inbound billings:**

   1. On the **Billing transfers** page, select the **Inbound billing** tab.

   1. On the **Inbound billing** tab, select the transfer you want to view details for.

   1. Choose the **Actions** dropdown menu, and then chose **View details**.

1. 

**For outbound billings:**

   1. On the **Billing transfers** page, select the **Outbound billing** tab.

   1. On the **Outbound billing** tab, you can view details for the transfer.

------
#### [  ]

**To view a transfer**  
You can use one of the following operations:
+ AWS CLI: [list-inbound-responsibility-transfers](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-inbound-responsibility-transfers.html), [list-outbound-responsibility-transfers](https://docs.aws.amazon.com/cli/latest/reference/organizations/list-outbound-responsibility-transfers.html), and [describe-responsibility-transfer](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-responsibility-transfer.html)

  1. **For inbound billing:**

     Run the following command to find the billing transfer ID for inbound billings:

     ```
     $ C:\> aws organizations list-inbound-responsibility-transfers \
         --type BILLING
     ```

     **For outbound billing:**

     Run the following command to find the billing transfer ID for outbound billings:

     ```
     $ C:\> aws organizations list-outbound-responsibility-transfers \
         --type BILLING
     ```

  1. From the response, note the billing transfer ID for the transfer you want to view details for.

  1. Run the following command to view details for the transfer:

     ```
     $ C:\> aws organizations describe-responsibility-transfer \
         --id {{exampleid}}
     ```
+ AWS SDKs: [list-inbound-responsibility-transfers](https://docs.aws.amazon.com/cli/latest/reference/organizations/API_ListInboundResponsibilityTransfers.html), [list-outbound-responsibility-transfers](https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOutboundResponsibilityTransfers.html), and [describe-responsibility-transfer](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeResponsibilityTransfer.html)

------