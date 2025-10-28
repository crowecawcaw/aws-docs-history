# Adding a gauge widget to a CloudWatch dashboard

###### Note

Only the new interface in the CloudWatch console supports creation
of the gauge widget.
You must set a gauge range
when you create this widget.

######

To add a gauge widget to a dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**, and
   then
   choose
   a dashboard.
3. From the dashboard screen, choose the **+** symbol, and
   then
   select **Gauge**.
4. Choose **Browse**, and
   then
   select the metric that you want to graph.
5. Choose **Options**.
   Under **_Gauge range_**,
   set values
   for **Min** and **Max**.
   For percentages,
   such as CPU utilization,
   we recommend that you set the values
   for `Min`
   to `0`
   and `Max`
   to `100`.
6. (Optional) To change the color of the gauge widget, choose
   **Graphed
   metrics**
   and select the color box next to the metric label. A menu appears where you
   can choose a different color or enter a six-digit hex color code to specify
   a color.
7. Choose **Create widget**,
   and choose **Save dashboard**.
