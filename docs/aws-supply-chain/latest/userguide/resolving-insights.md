# Resolving an inventory risk insight

Insights recommends one or more ways to resolve an inventory risk depending on the distance, time horizon, available transportation modes in the ingested data (transportation_lane.trans_mode), shipping
costs (transportation_lane.unit_costs), and emissions that you've configured under Insights settings. The recommendation might include an inventory transfer from other locations within a certain distance and this
would resolve an inventory risk in the location under review.

Under **Settings** > **Insights**, **Rebalancing Recommendations Score Weights**, you can adjust the core weight values
to determine how ranking is calculated for rebalance recommendations. You can setup the radius surrounding the stocked out site to search for available stock for rebalance. You can set the distance in miles and kilometers. You can configure the rebalance model to
optimize inventory levels for both supplying and receiving sites. Insights supports up to a maximum of six weeks beyond the current date, and you can customize the time horizon by
factoring your lead times to see the impact of the rebalance before and after transfers.

Inventory risk recommendations are helpful for immediately resolving stockout issues rather than overstocks. You may see rebalancing recommendations linked with overstock or excess stock issues but those will have a stockout risk at the receiving site.

1. In the left navigation pane on the AWS Supply Chain dashboard, choose
   **Insights**.

The **Insights** page appears. 2. Under **New Insights**, select an insight to resolve the inventory
risk. 3. Choose **View details**.

An overview of the inventory risk with the current and projected inventory, and the
rebalance options are displayed. 4. Under the details page, you can view the following:

    * *Identified* – Displays the date on when the inventory risk was identified.
    * *Product* – Displays the product in the inventory that is at risk.
    * *Destination* – Displays the destination where the product should be shipped.
    * *Risk Timeframe* – Displays the upcoming risk in days with the current inventory.
    * *Summary* – Displays the details of the risk in detail.
    * *Current inventory* – Displays the inventory that is currently on hand, the safety stock limit, and the allocated amount of inventory against the current orders.
    * *Projected Inventory* – Displays how your current inventory is projected starting daily to upto six weeks. Choose the **graph** icon to view the inventory in a graph.

5. Under **Rebalance Options**, review the rebalance options and choose **Select** against
   the rebalance option recommended by Insights.

Once you select the rebalance option, you can view the current and projected inventories
before and after the rebalance. 6. On the **Confirm Resolution** page, the rebalance option that you chose
is shown under **Resolution Option**. 7. Under **Message the team**, select the **After
clicking...** check box to notify the team on the selected rebalance option. 8. Choose **Confirm**. 9. Choose **Send to Amazon S3** to export the resolution recommendation to your Amazon S3 bucket.

###### Note

Insights only recommends options to rebalance inventory. You must use your own planning system to update the inventory transfers or orders. 10. Choose the chat icon to collaborate with other users or add users as watchers to the current insight.
