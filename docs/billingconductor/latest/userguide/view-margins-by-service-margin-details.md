# View your margins by AWS service using margin details

## Viewing your billing group margins by service

###### To view your billing group margins by service

1. Open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, , under **Analytics**, choose **Margin
   details**.
3. Under **Report parameters**, choose a **Billing period**
   and a **Billing group**.
4. You can view your margin analysis in two ways:
   - As a line chart in the **Margin trend by top 5 services**
     section.
   - As a table in the **Margin analysis** table.

## Understanding your margin trend chart

Your margin details will display a line chart that displays the top five services by margin
for the chosen billing period. The line chart will display the margins for each service over the
last three months for comparison.

The chart will also include a table that displays the margins for each service for the
chosen billing period. The table displays the average margin calculated over the last three
months, which includes the following columns:

- Service name
- Average
- Margin

If the billing group wasn't active for the entirety of the last three months, then the
chart will only display the cost report data that is available.

## Understanding your margin analysis

table

The billing group margin analysis table includes the following columns:

- Service name
- Charged amount
- AWS costs
- Margin amount
- Margin percentage

You can export your margin analysis table to a downloadable CSV file. Next to your margin
analysis table, choose **Download CSV**. Your download will start
automatically.

###### Note

To download a CSV file with your billing group margin analysis, you must have the
`billingconductor:GetBillingGroupCostReport` permission added to your IAM
policy.
