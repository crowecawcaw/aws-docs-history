# Modify the time range or time zone format for a
 graph

 This section describes how you can modify the date, time, and time zone format on a
 CloudWatch metrics graph. It also describes how you can zoom in on a graph to apply a specific
 time range. For information about creating a graph, see [Graph a metric](graph_a_metric.md "graph_a_metric.md"). 

###### Note

If the time range of a dashboard is shorter than the period used for a graph on the
 dashboard, the following happens:


* The graph is modified to display the amount of data corresponding one complete
 period for that widget, even though this is longer than the dashboard time range. This
 ensures that there is at least one data point on the graph.
* The start time of the period for this data point is adjusted backwards to ensure
 that at least one data point can be displayed.

## Set a relative time range



 New interface 
######  To specify a relative time range for a graph

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
 choose **All metrics**. In the upper right corner of the
 screen, you can select one of the predefined time ranges, which span from 1 hour
 to 1 week (**1h**, **3h**,
 **12h**, **1d**, **3d**, or
 **1w**). Alternatively, you can choose
 **Custom** to set your own time range.
3. Choose **Custom**, and then select the
 **Relative** tab in the upper left corner of the box. You can
 specify a time range in **Minutes**,
 **Hours**, **Days**,
 **Weeks**, **Months**.
4. After you specify a time range, choose **Apply**.


 Original interface 
######  To specify a relative time range for a graph

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
 choose **All metrics**. In the upper right corner of the
 screen, you can select one of the predefined time ranges, which span from 1 hour
 to 1 week (**1h**, **3h**,
 **12h**, **1d**, **3d**, or
 **1w**). Alternatively, you can choose
 **custom** to set your own time range.
3. Choose **custom**, and then choose
 **Relative** in the upper left corner of the box. You can
 specify a time range in **Minutes**,
 **Hours**, **Days**,
 **Weeks**, or **Months**.



## Set an absolute time range



 New interface 
###### To specify an absolute time range for a graph

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
 choose **All metrics**. In the upper right corner of the
 screen, you can select one of the predefined time ranges, which span from 1 hour
 to 1 week (**1h**, **3h**,
 **12h**, **1d**, **3d**, or
 **1w**). Alternatively, you can choose
 **Custom** to set your own time range.
3. Choose **Custom**, and then select the
 **Absolute** tab in the upper left corner of the box. Use the
 calendar picker or text field boxes to specify a time range.
4. After you specify a time range, choose **Apply**.


 Original interface 
###### To specify an absolute time range for a graph

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
 choose **All metrics**. In the upper right corner of the
 screen, you can select one of the predefined time ranges, which span from 1 hour
 to 1 week (**1h**, **3h**,
 **12h**, **1d**, **3d**, or
 **1w**). Alternatively, you can choose
 **custom** to set your own time range.
3. Choose **custom**, and then choose
 **Absolute** in the upper left corner of the box. Use the
 calendar picker or text field boxes to specify a time range.
4. After you specify a time range, choose **Apply**.



## Set the time zone format



 New interface 
###### To specify the time zone for a graph

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
 choose **All metrics**. In the upper right corner of the
 screen, you can select one of the predefined time ranges, which span from 1 hour
 to 1 week (**1h**, **3h**,
 **12h**, **1d**, **3d**, or
 **1w**). Alternatively, you can choose
 **Custom** to set your own time range.
3. Choose **Custom**, and then choose the dropdown in the
 upper right corner of the box. You can change the time zone to
 **UTC** or **Local time zone**.
4. After you make your changes, choose **Apply**.


 Original interface 
###### To specify the time zone for a graph

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then
 choose **All metrics**. In the upper right corner of the
 screen, you can select one of the predefined time ranges, which span from 1 hour
 to 1 week (**1h**, **3h**,
 **12h**, **1d**, **3d**, or
 **1w**). Alternatively, you can choose
 **custom** to set your own time range.
3. Choose **custom**, and then choose the dropdown in the
 upper right corner of the box. You can change the time zone to
 **UTC** or **Local timezone**.
