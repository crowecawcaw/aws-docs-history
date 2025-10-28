# Tutorial: Creating

a dashboard that uses a regular expression pattern to switch between AWS Regions

The steps in this procedure illustrate how to create a flexible dashboard that can
switch between Regions. This tutorial uses a regular expression _pattern
variable_ instead of a property variable. For a tutorial that
uses a property variable, see
[Tutorial: Creating
a CloudWatch Lambda dashboard with function name as the variable](cloudwatch_dashboard_variables_property.md "cloudwatch_dashboard_variables_property.md").

For many use cases, you can create a dashboard that switches between Regions by
using a property variable. But if the widgets rely on Amazon Resource Names (ARNs)
that include Region names, you must use a pattern variable to change the Region
names within the ARNs.

######

To use a dashboard pattern variable to create a flexible multi-Region dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane,
   choose **Dashboards**,
   **Create dashboard**.
3. Enter a name for the dashboard, and choose **Create dashboard**.
4. Add widgets to the dashboard. When you add the widgets that you want to
   display Region-specific data, avoid specifying any dimensions with values
   that appear in only one Region. For example, for Amazon EC2 metrics, specify
   metrics that are aggregated instead of metrics that use
   **InstanceID** as a dimension.

For more information about adding widgets to a dashboard,
see [Using widgets
on CloudWatch dashboards](create-and-work-with-widgets.md "create-and-work-with-widgets.md"). 5. After you add the widgets, as you are viewing the dashboard, choose
**Actions**, **Variables**,
**Create a variable**. 6. Choose **Pattern variable**. 7. For **Property that the variable changes**, enter the
name of the current dashboard Region, such as `us-east-2`.

You have the correct Region entered if the label below that box displays the
widgets that will be impacted by the variable. 8. For **Input type**, for this use case, select
**Radio button**. 9. For **Define how inputs are populated**,
choose **Create a list of custom values**. 10. For **Create your custom values**, enter the Regions that you want to switch
between, with one Region on each line. After each Region, enter a comma and
then the label to display for that radio button. For example:

`us-east-1, N. Virginia`

`us-east-2, Ohio`

`eu-west-3, Paris`

As you fill in the custom values, the **Preview** pane updates to display
what the radio buttons will look like. 11. (Optional) For more settings, choose **Secondary settings** and do one or
more of the following:

    * To customize the name of your variable, enter the name in
     **Custom variable name**.
    * To customize the label for the variable input field, enter the label in **Input
     label**. For this tutorial, enter
     `Region:`.


    If you enter a value here, the **Preview** pane updates to display
     what the radio buttons will look like.
    * To set the default value for this variable when the dashboard
     is first opened, enter the default in
     **Default value**.

12. Choose
    **Add variable**.

The dashboard appears, with a **Region:** label next to
the radio buttons for the Regions near the top. When you switch between
Regions, all the widgets that use the variable will display information
about the selected Region.
