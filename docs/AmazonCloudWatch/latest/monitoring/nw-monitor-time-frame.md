# Specify metrics time frame

Metrics and events on the dashboards in Network Synthetic Monitor use a default time of two hours, calculated from the
 current time, but you can set a custom metrics default time frame to use. You can change the default to one 
 of the following presets for the metrics time frame:


* **1h** — one hour
* **2h** — two hours
* **1d** — one day
* **1w** — one week
You can also set a custom time frame. Choose **Custom**,
 choose an **Absolute** or **Relative**
 time, and then set the time frame to a time of your own choosing. Relative time supports only 15
 days back from today's date, following CloudWatch guidelines.

Additionally, you can choose the time displayed in the charts to be based on either the UTC
 time zone or a local time zone. 

For more information, see [Changing the time range or time zone format of a CloudWatch
 dashboard](change_dashboard_time_format.md "change_dashboard_time_format.md").
