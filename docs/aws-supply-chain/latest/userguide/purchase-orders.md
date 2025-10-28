# Purchase Orders

You can view the list of purchase order data requests that are published to your
partners. Purchase orders collaboration can only be enabled through Work Orders. For
more information, see [Order Planning and Tracking](work-order.md "work-order.md").

1. In the left navigation pane on the AWS Supply Chain dashboard, choose
   **N-Tier Visibility**.

The **N-Tier Visibility** page appears. 2. Choose the **Purchase Orders** tab. 3. Under **Purchase Orders**, you can view the details of all the purchase order
data requests that are published to your partners from the generated order
insight.

You can select any purchase order to review the purchase order details. 4. Select the **Status** dropdown to filter purchase orders based on
collaboration status. 5. Choose **Review** for purchase orders with a _For review_
collaboration status. These purchase orders require your review if the partner's
response on date or quantity deviate from configured acceptance threshold.

The **Purchase Order** details page appears. 6. Under **Review the Purchase Order Update**, review the purchase order
quantity and delivery date submitted by the partner, and then you can accept or
reject the response.

You can read the reason for the update under **Update details from the partner**. 7. To accept the purchase order update, choose **Accept response**.

The **Accept update** window appears. Choose **Accept update**. 8. To reject the purchase order update, choose **Reject and send**.

The **Reject PO update and send feedback** window appears.
Enter the rejection details and choose **Reject and send**. The
purchase orders will be sent back to your partner and provided an updated
response.

## Viewing purchase orders in EDI format

###### Note

You will only see this configuration if you selected _Yes_ to use **EDI Connection Settings** when setting up N-Tier Visibility.

You can view the Purchase Orders data received through EDI.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose
   **N-Tier Visibility**.

The **N-Tier Visibility** page appears. 2. Choose the **Purchase Orders** tab.

The **Confirm or Update Pending Purchase Orders** page appears. 3. From the **Actions** drop-down, choose **Export EDI data**.

The .json file with the purchase orders information is downloaded to your local computer and also downloaded to the Amazon S3 folder created as part of the outbound connection setup for Supply Planning.
