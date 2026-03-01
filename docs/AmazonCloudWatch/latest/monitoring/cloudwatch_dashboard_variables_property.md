# Tutorial: Creating a CloudWatch Lambda dashboard with function name as the variable

The steps in this procedure illustrate how to create a flexible dashboard that
shows a variety of metric graphs, using a property variable. This includes a
dropdown selection box on the dashboard that you can use to switch the metrics in
all the graphs between different Lambda functions.

Other use case examples for this type of dashboard include using
`InstanceId` as the variable to create a dashboard of metrics with a
dropdown for instance IDs. Alternatively, you could create a dashboard that uses
`region` as the variable to display the same set of metrics from
different Regions.

###### To use a dashboard property variable to create a flexible Lambda dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane,
   choose **Dashboards**,
   **Create dashboard**.
3. Enter a name for the dashboard, and choose **Create dashboard**.
4. Add widgets to the dashboard that display metrics for a Lambda function.
   When you create these widgets, specify **Lambda**,
   **By Function Name** for the widget metrics. For the
   function, specify one of the Lambda functions that you want to include in
   this dashboard.

For more information about adding widgets to a dashboard,
see [Using widgets on CloudWatch dashboards](create-and-work-with-widgets.md "create-and-work-with-widgets.md"). 5. After you add the widgets, as you are viewing the dashboard, choose
**Actions**, **Variables**,
**Create a variable**. 6. Choose **Property variable**. 7. For **Property that the variable changes**, choose
**FunctionName**. 8. For **Input type**, for this use case, we recommend
choosing **Select menu (dropdown)**. This creates a
dropdown menu in the dashboard where you can select the Lambda function name
to display metrics for.

If this was for a dashboard that toggled between only two or three
different values for a variable, then **Radio button**
would be a good choice.

If you prefer to enter or paste in values for the variable, you would
choose **Text input**. This option doesn't include a
dropdown list or radio buttons. 9. When you choose **Select menu (dropdown)**, you must then choose whether to
populate the menu by entering values, or using a metric search. For this use
case, let's assume that you have a large number of Lambda functions and you
don't want to enter all of them manually. Choose **Use the results
of a metric search** and then do the following:

    1. Choose **Pre-built queries**, **Lambda**,
     **Errors**.


    (Choosing **Errors** does not add the
     **Errors** metric to the dashboard. However, it
     quickly populates the **FunctionName** variable
     selection box.)
    2. Choose **By Function Name** and then choose **Search**.


    Under the **Search** button, you will then see
     **FunctionName** selected. You also see a
     message about how many **FunctionName** dimension
     values were found to populate the input box.

10. (Optional) For more settings, choose **Secondary settings** and do one or
    more of the following:
    - To customize the name of your variable, enter the name in
      **Custom variable name**.
    - To customize the label for the variable input field, enter the label in **Input
      label**.
    - To set the default value for this variable when the dashboard
      is first opened, enter the default in
      **Default value**.

11. Choose
    **Add variable**.

A **FunctionName** dropdown selection box appears near the
top of the dashboard. You can select a Lambda function in this box and all
the widgets that use the variable will display information about the
selected function.

Later, if you add more widgets to the dashboard that watch Lambda metrics with
the **FunctionName** dimension, they will automatically use
the variable.
