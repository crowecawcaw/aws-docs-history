# Viewing a Cost Explorer report using billing views

Cost Explorer provides two types of default reports: cost and usage reports and Reserved
Instance reports. Only Cost Explorer reports of type “cost and usage reports” are supported
by custom and AWS managed billing views; “Reserved Instance reports” can’t be used with a custom and AWS managed billing views.
Cost Explorer also enables you to create your own reports by saving the results of a
Cost Explorer query as a report. Cost Explorer reports can be used alongside custom billing
views to access the cost management data contained in a custom billing view with the query
saved as a Cost Explorer report.

When creating a new Cost Explorer report, only the Cost Explorer query is saved as part
of the report definition. The currently selected custom and AWS managed billing view is not saved as part of
the report. To learn more about Cost Explorer reports, see [Understanding
your costs using Cost Explorer reports](ce-reports.md "ce-reports.md").

###### To view a saved Cost Explorer report

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, enable **billing view** mode. The
   default selection is the **Primary view**, which represents cost
   management data for the account you're currently logged in to.
3. From the dropdown list, choose either **Custom** or **AWS managed views** (`billing group` or `billing transfer` views). Choose the
   custom billing view you want to use for accessing cost management data.
4. In the navigation pane, choose **Cost Explorer Saved
   Reports**.
5. Select the report you want to access.

###### Note

You can save your Cost Explorer configuration and billing view selection as a
favorite or bookmark in your browser. When you return to this saved link, Cost Explorer
refreshes the page to display the cost management data from the billing view along
with the saved configuration. This feature allows you to quickly access frequently used
combinations of configurations and billings views, saving you time and effort.
