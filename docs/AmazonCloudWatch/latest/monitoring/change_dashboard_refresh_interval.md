# Changing the period override setting or refresh

interval for the CloudWatch dashboard

You can specify how the period setting of graphs added to this dashboard are retained or
modified.

When an auto period or persisted time range is applied to a widget, the overall time range of
the graph can affect the periods that you have set.

- If the time range is one day or less, period settings are not changed.
- If the time range is between one day and three days, periods set to below
  five minutes are changed to 5 minutes.
- If the time range is more than three days, periods set to below one hour
  are changed to one hour.
  The following steps explain how to use the console to change the period override options. You can
  also change them by using the `periodOverride` field in the JSON structure of the dashboard.
  For more information, see
  [Dashboard Body Overall Structure](../APIReference/CloudWatch-Dashboard-Body-Structure.md#Dashboard-Body-Overall-Structure "../APIReference/CloudWatch-Dashboard-Body-Structure.md#Dashboard-Body-Overall-Structure").

###### To change the period override options

1.  Open the CloudWatch console at
    [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2.  Choose **Actions**.
3.  Under **Period override**, choose one of the following:

        * Choose **Auto** to have the period of the metrics on each
         graph automatically adapt to the dashboard's time range.
        * Choose **Do not override** to ensure that the period setting of each
         graph is always obeyed.
        * Choose one of the other options to cause graphs added
         to the dashboard to always adapt that chosen time as their period setting.

    The **Period override** always reverts to
    **Auto** when the dashboard is closed or the browser is
    refreshed. Different settings for **Period override** can't be
    saved.
    You can change how often the data on your CloudWatch dashboard is refreshed.

###### To change the dashboard refresh interval

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose
   **Dashboards**,
   and
   then
   choose a dashboard.
3. On the **Refresh options** menu (upper-right corner), choose
   **10 Seconds**, **1 Minute**, **2
   Minutes**, **5 Minutes**, or **15
   Minutes**.
