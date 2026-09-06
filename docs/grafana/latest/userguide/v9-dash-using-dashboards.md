

# Using dashboards
<a name="v9-dash-using-dashboards"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

This topic provides an overview of dashboard features and shortcuts, and describes how to use dashboard search.

## Features
<a name="v9-dash-features"></a>

You can use dashboards to customize the presentation of your data in the following ways.


|  Feature  |  Description  | 
| --- | --- | 
| **1. Home** | Click the Grafana home icon to be redirected to the home page configured in the Grafana instance. | 
| **2. Title** | When you click the dashboard title, you can search for dashboard contained in the current folder. | 
| **3. Sharing a dashboard** | Use this option to share the current dashboard by link or snapshot. You can also export the dashboard definition from the share modal. | 
| **4. Adding a new panel** | Use this option to add a panel, dashboard row, or library panel to the current dashboard. | 
| **5. Dashboard settings** | Use this option to change dashboard name, folder, and tags and manage variables and annotation queries. For more information about dashboard settings, see [Modifying dashboard settings](v9-dash-modify-settings.md). | 
| **6. Time picker dropdown** | Click to select relative time range options and set custom absolute time ranges.+  You can change the **Timezone** and **fiscal year** settings from the time range controls by clicking the **Change time settings** button. <br />+  Time settings are saved on a per-dashboard basis.  | 
| **7. Zooming out time range** | Click to zoom out the time range. For more information about how to use time range controls, see [Setting dashboard time range](#v9-dash-setting-dashboard-time-range). | 
| **8. Refreshing dashboard** | Click to immediately trigger queries and refresh dashboard data. | 
| **9. Refreshing dashboard time interval** | Click to select a dashboard auto refresh time interval. | 
| **10. View mode** | Click to display the dashboard on a large screen such as a TV or a kiosk. View mode hides irrelevant information such as navigation menus. | 
| **11. Dashboard panel** | The primary building block of a dashboard is the panel. To add a new panel, dashboard row, or library panel, click **Add panel**.+  Library panels can be shared among many dashboards. <br />+  To move a panel, drag the panel header to another location. <br />+  To resize a panel, click and drag the lower right corner of the panel.  | 
| **12. Graph legend** | Change series colors, y-axis, and series visibility directly from the legend. | 
| **13. Dashboard search** | Click **Search** to search for dashboards by name or panel title. | 
| **14. Dashboard row** | A dashboard row is a logical divider within a dashboard that groups panels together.+  Rows can be collapsed or expanded allowing you to hide parts of the dashboard. <br />+  Panels inside a collapsed row do not issue queries.  <br />+  Use repeating rows to create rows dynamically based on a template variable.  | 

## Keyboard shortcuts
<a name="v9-dash-keyboard-shortcuts"></a>

Grafana has a number of keyboard shortcuts available. To display all keyboard shortcuts available to you, press **?** or **h** on your keyboard.
+ `Ctrl+S` saves the current dashboard. 
+ `f` opens the dashboard finder/search. 
+  `d+k` toggles kiosk mode (hides the menu). 
+ `d+e` expands all rows. 
+ `d+s` opens dashboard settings. 
+ `Ctrl+K` opens the command palette.
+ `Esc` exits panel when in fullscreen view or edit mode. Also returns you to the dashboard from the dashboard settings.

**Focused panel**

To use shortcuts targeting a specific panel, hover over a panel with your pointer.
+ `e` toggles panel edit view 
+ `v` toggles panel fullscreen view 
+ `ps` opens panel share feature 
+ `pd` duplicates panel 
+ `pr` removes panel 
+ `pl` toggles panel legend 

## Setting dashboard time range
<a name="v9-dash-setting-dashboard-time-range"></a>

Grafana provides several ways to manage the time ranges of the data being visualized, for dashboard, panels and also for alerting.

This section describes supported time units and relative ranges, the common time controls, dashboard-wide time settings, and panel-specific time settings.

**Time units and relative ranges**

Grafana supports the following time units: `s (seconds)`, `m (minutes)`, `h (hours)`, `d (days)`, `w (weeks)`, `M (months)`, `Q (quarters)`, and `y (years)`. 

The minus operator enables you to step back in time, relative to now. If you want to display the full period of the unit (day, week, or month), append `/<time unit>` to the end. To view fiscal periods, use `fQ (fiscal quarter)` and `fy (fiscal year)` time units.

The plus operator enables you to step forward in time, relative to now. For example, you can use this feature to look at predicted data in the future.

The following table provides example relative ranges.


| Example relative range | From | To | 
| --- | --- | --- | 
| Last 5 minutes |  `now-5m`  |  `now`  | 
| The day so far |  `now/d`  |  `now`  | 
| This week |  `now/w`  |  `now/w`  | 
| This week so far |  `now/w`  |  `now`  | 
| This month |  `now/M`  |  `now/M`  | 
| This month so far |  `now/M`  |  `now`  | 
| Previous Month |  `now-1M/M`  |  `now-1M/M`  | 
| This year so far |  `now/Y`  |  `now`  | 
| This Year |  `now/Y`  |  `now/Y`  | 
| Previous fiscal year |  `now-1y/fy`  |  `now-1y/fy`  | 

**Note**  
 Grafana Alerting does not support `now+n` for future timestamps and `now-1n/n` for *start of n until end of n* timestamps. 

**Common time range controls**

The dashboard and panel time controls have a common user interface. The following describes common time range controls.
+ Current time range, also called the *time picker*, shows the time range currently displayed in the dashboard or panel you are viewing. Hover your cursor over the field to see the exact time stamps in the range and their source (such as the local browser). Click the *current time range* to change it. You can change the current time using a *relative time range*, such as the last 15 minutes, or an absolute time range, such as `2020-05-14 00:00:00` to `2020-05-15 23:59:59`.
+ The **relative time range** can be selected from the **Relative time ranges** list. You can filter the list using the input field at the top. Some examples of time ranges include *Last 30 minutes*, *Last 12 hours*, *Last 7 days*, *Last 2 years*, *Yesterday*, *Day before yesterday*, *This day last week*, *Today so far*, *This week so far*, and *This month so far*.
+ **Absolute time range** can be set in two ways: Typing exact time values or relative time values into the **From** and **To** fields and clicking **Apply time range**, or clicking a date or date range from the calendar displayed when you click the **From** or **To** field. To apply your selections, click **Apply time range**.

*Other time range features*

1. To zoom out, click **Cmd\+Z** or **Ctrl\+Z**. Click the icon to view a larger time range in the dashboard or panel visualization.

1. To use the zoom in feature, click and drag to select the time range in the visualization that you want to view.

**Note**  
Zooming in is only applicable to graph visualizations. 

*Refresh dashboards*

Click the **Refresh dashboard** icon to immediately run every query on the dashboard and refresh the visualizations. Grafana cancels any pending requests when you trigger a refresh.

By default, Grafana does not automatically refresh the dashboard. Queries run on their own schedule according to the panel settings. However, if you want to regularly refresh the dashboard, then click the down arrow next to the **Refresh dashboard** icon and then select a refresh interval.

**Control the time range using a URL**

You can control the time range of a dashboard by providing the following query parameters in the dashboard URL.
+ `from` defines the lower limit of the time range, specified in ms epoch, or [relative time](#v9-dash-setting-dashboard-time-range).
+ `to` defines the upper limit of the time range, specified in ms epoch, or relative time.
+ `time` and `time.window` defines a time range from `time-time.window/2` to `time+time.window/2`. Both parameters should be specified in ms. For example `?time=1500000000000&time.window=10000` results in 10s time range from 1499999995000 to 1500000005000.