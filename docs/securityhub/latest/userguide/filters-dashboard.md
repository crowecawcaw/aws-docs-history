# Filtering the Summary dashboard in Security Hub CSPM

You can curate the **Summary** dashboard on the Security Hub CSPM console so that
it includes only the security data that's most relevant to you. For example, if you're a
member of an application team, you might create a dedicated view for a critical
application in your production environment. If you're a member of a security team, you
might create a dedicated view that helps you focus on high-severity findings.

To create these curated views, enter filter criteria in the filter box above the
dashboard. If you apply filter criteria, the criteria apply to all the data and widgets
on the dashboard, except the data in the **Insights** and
**Security standards** widgets. For a list of available widgets on
the dashboard, see [Available widgets for the Summary dashboard](dashboard.md#available-widgets "dashboard.md#available-widgets").

You can filter the data by using the following fields:

- Account name
- Account ID
- Application ARN
- Application name
- Product name (for an AWS service or third-party product that sends findings to Security Hub CSPM)
- Record state
- Region
- Resource tag
- Severity
- Workflow status
  By default, dashboard data is filtered using the following criteria: `Workflow.Status` is `NOTIFIED` or `NEW`, and
  `RecordState` is `ACTIVE`. These criteria appear above the dashboard, below the filter box. To remove
  these criteria, choose **X** in the filter token for the criteria that you want to remove.

If you apply filter criteria that you want to use again, you can save it as a
_filter set_. A filter set is a set of filter criteria that you
create and save to reapply when you review data on the **Summary**
dashboard. You can create and save a filter set that uses any of the available fields
except the following fields: Application ARN, application name, and resource tag.

## Creating and saving filter sets

Follow these steps to create and save a filter set.

###### To create and save a filter set

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Summary**.
3. In the filter box above the **Summary** dashboard, enter the filter criteria for the filter set.
4. On the **Clear filters** menu, choose
   **Save new filter set**.
5. In the **Save filter set** dialog box, enter a name for the
   filter set.
6. (Optional) To use the filter set by default each time you open
   the **Summary** page, select the option to set it as the default view.
7. Choose **Save**.

To switch between filter sets that you’ve created and saved, use the **Choose a filter set**
menu above the **Summary** dashboard. When you select a filter set, Security Hub CSPM applies the criteria of
the filter set to the data on the dashboard.

## Updating or deleting filter sets

Follow these steps to update or delete an existing filter set. If you delete a filter set that is currently set
as your default view of the **Summary** dashboard, your default view is reset to the default Security Hub CSPM view.

###### To update or delete a filter set

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Summary**.
3. In the **Choose a filter set** menu above the **Summary** page, choose the filter set.
4. On the **Clear filters** menu, do one of the following:
   - To update the filter set, choose **Update current filter set**. Then, enter your changes in the dialog box that appears.
   - To delete the filter set choose **Delete current filter set**. Then, choose **Delete** in the dialog box that appears.
