# Adding a number widget to a CloudWatch dashboard

###### Note

Only the new interface supports the sparkline feature. When you create a
number widget, the sparkline feature
is
automatically
included.

######

To add a number widget
to a dashboard

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**, and
   then
   choose a dashboard.
3. Choose the **+** symbol,
   and select **Number**.
4. In the **Browse** tab,
   search or browse for the metric
   that you want to display.
5. (Optional) To change the color
   of the sparkline feature,
   choose **Graphed metrics**,
   and select the color box
   next
   to the metric label.
   A menu appears
   where you can choose a different color
   or enter a six-digit hex color code
   to specify a color.
6. (Optional) To
   turn
   off the sparkline feature, choose
   **Options**. Under
   **_Sparkline_**,

the
check
box. 7. (Optional) To change your number widget's time range, select one of the predefined
time ranges in the upper area of the widget. The time ranges span
from 1 hour to 1 week (**_1h_**,
**_3h_**,
**_12h_**,
**_1d_**,
**_3d_**, or
**_1w_**).

To set your own time range,
choose **Custom**.

    1. (Optional) To have this widget keep using this time range that you select, even
     if the time range for the rest of the dashboard is later changed, choose **Persist time range**.

8. (Optional) To have the number widget display an aggregate (**_1h_**,
   **_3h_**,
   **_12h_**,
   **_1d_**,
   **_3d_**, or
   **_1w_**).

To set your own time range,
choose **Custom**.

    1. (Optional) To have this widget display an average of the metric value over the entire time range, instead of the
     most recent value, choose
     **Options**, **Time range value shows the value from the entire time range**.

9. Choose **Create widget**,
   and choose **Save dashboard**.

###### Tip

You can turn off the sparkline feature
from the number widget
on the dashboard screen.
In the upper-right corner
of the number widget
that you want
to modify,
choose **Widget actions**.
Select **Sparkline**,
and then choose **Hide sparkline**.
