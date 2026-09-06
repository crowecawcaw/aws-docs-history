

# Filtering your Amazon Inspector findings
<a name="findings-managing-filtering"></a>

 You can filter your Amazon Inspector findings using filter criteria. If a finding doesn't match your filter criteria, Amazon Inspector excludes the finding from view. This section describes how to filter your Amazon Inspector findings using filter criteria. 

## Creating filters in the Amazon Inspector console
<a name="findings-managing-filters-proc"></a>

In each findings view, you can use the filter functionality to locate findings with specific characteristics. Filters are removed when you move to a different tabbed view.

A filter is made up of a filter criteria, which consists of a filter attribute paired with a filter value. Findings that do not match your filter criteria are excluded from the findings list. For example, to see all findings that are associated with your administrator account, you can choose the AWS account ID attribute and pair it with the value of your twelve digit AWS account ID.

Some filter criteria apply to all findings, while others are available for specific resource types or finding types only.

**To apply a filter to the findings view**

1.  Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home). 

1. In the navigation pane, choose **Findings**. The default view displays all findings with an **Active** status.

1. To filter findings by criteria, select the *Add filter* bar to see a list of all applicable filter criteria for that view. Different filter criteria are available in different views.

1. Choose a criterion that you want to filter by from the list. 

1. From the criterion input pane enter the desired filter values to define that criterion. 

1. Choose **Apply** to apply that filter criterion to your current results. You can continue to add other filter criterion by selecting the filter input bar again.

1. (Optional) To view your suppressed or closed findings, choose **Active** in the filter bar, and then choose **Suppressed** or **Closed**. Choose **Show all** to see active, suppressed, and closed findings in the same view.