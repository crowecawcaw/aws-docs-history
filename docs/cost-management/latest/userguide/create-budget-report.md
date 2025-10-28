# Creating an AWS Budgets report

Use the following procedure to create an AWS Budgets report.

###### To create an AWS Budgets report

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Budgets Reports**.
3. On the top right of the page, choose **Create budget report**.
4. Select the budgets that you want to include in your report. You can select up to 50 budgets.

###### Note

If you select more, you can't proceed to the next step until you change your selection to 50 or fewer budgets. 5. For **Report frequency**, choose **Daily**, **Weekly**, or **Monthly**.

    * If you choose a **Weekly** report: For **Day of week**, choose the day of the week that you want the report delivered.
    * If you choose a **Monthly** report: For **Day of month**, choose the calendar day of the month that you want the report delivered. If you choose any day after the 28th day, and the next month doesn't have that calendar day, then your report is delivered on the last day of that month.

Reports are delivered at approximately 0:00 UTC+0 on the speciﬁed day. 6. For **Email recipients**, enter the email addresses to deliver the report to. Separate multiple email addresses with commas. You can include up to 50 email recipients for each budget report. 7. For **Budget report name**, enter the name of your budget report. This name appears on the subject line of the budget report email. You can change the report name at any time. 8. Choose **Create budget report**.
Your report appears on the AWS Budgets Reports dashboard. On the dashboard, you can filter your reports by **Report name**. For each report, the dashboard also shows **Frequency**, **Budgets included**, and **Recipient(s)**.
