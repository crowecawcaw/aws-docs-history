# View your aggregate margins with margin

summary

## Viewing your billing group margins summary

###### To view your billing group margins summary

1. Open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, under **Analytics**, choose **Margin
   summary**.
3. For **Report type**, choose **All billing groups** or
   **Select billing group**.
4. If you chose **Select billing groups**, choose a **Billing
   period** and one or more billing groups.
5. In the **Month-to-date overview** section, you can view your
   **Charged amount**, **AWS costs**, and
   **Margin**.
6. You can view your margin analysis in two ways:
   - As a bar chart in the **Performance (up to last 13 months)**
     section.
   - As a table in the **Margin analysis** table.Negative margins are shown in red in the graph, with a negative dollar amount and negative
     percentage.

## Understanding your margin analysis

table

The billing group margin analysis table is sorted in reverse chronological order by
default. You can sort the table by all of the columns, which include the following:

- Month
- Charged amount
- AWS costs
- Margin amount
- Margin percentage

The graph and table returns values for the last 13 months of the billing groups selected.
If the billing groups were created at different times, we assume the time range of the oldest
selected billing group.

You can export your margin analysis table to a downloadable CSV file. Next to your margin
analysis table, choose **Download CSV**. Your download will start
automatically.

###### Note

To download a CSV file with your billing group margin analysis, you must have the
`billingconductor:ListBillingGroupCostReport` permission added to your IAM
policy.
