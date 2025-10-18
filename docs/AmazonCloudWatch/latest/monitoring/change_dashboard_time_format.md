# Changing the time range or time zone format of a CloudWatch
 dashboard

You can
 change the time range to display dashboard data over minutes, hours, days, or weeks. You
 also can change the time zone format to display dashboard data in
 UTC
 or local time. Local time is the time zone that's specified in your computer's operating
 system. 

###### Note

If
 you create a dashboard with graphs that contain 100 or more high-resolution metrics,
 we recommend that you don't set the time range to longer than 1 hour. For more
 information,
 see [High-resolution metrics](publishingMetrics.md#high-resolution-metrics "publishingMetrics.md#high-resolution-metrics"). 

###### Note

If the time range of a dashboard is shorter than the period used for a widget on the dashboard, the following happens:


* The widget is modified to display the amount of data corresponding one complete period for 
 that widget, even though this is longer than the dashboard time range. This ensures that there is at 
 least one data point on the graph.
* The start time of the period for this data point is adjusted backwards to ensure that at 
 least one data point can be displayed.

New console
###### To change the dashboard time range

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**,
 and then
 choose
 a dashboard.
3. From the dashboard screen, 
 do one 
 of the following:
 


	* In the
	 upper area of the dashboard, select one of the predefined time ranges. These span
	 from 1 hour to 1 week (**1h**,
	 **3h**, **12h**,
	 **1d**, or
	 **1w**).
	* Alternatively, you can choose one of the following custom time range options:
	
	
	
	
		+ Choose
		 **Custom**, and then choose the
		 **Relative** tab.
		 Choose
		 a time range from 1 minute to 15
		 months.
		+ Choose
		 **Custom**, and then choose the
		 **Absolute** tab. Use the
		 calendar or text
		 fields
		 to specify your time range.

###### Tip

If
 the
 aggregation period is set to **Auto** when
 you change the time range of a
 graph,
 CloudWatch might change the period. To set the period manually, choose the
 **Actions** dropdown, and then choose
 **Period override**. 


###### To change the dashboard time zone format

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**,
 and then
 choose
 a dashboard.
3. In the
 upper area of the dashboard, choose
 **Custom**.
4. In the
 upper-right
 corner of the box that appears, select **UTC** or
 **Local time** from the dropdown.
5. Choose
 **Apply**.


Old console
###### To change the dashboard time range

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**,
 and then
 choose
 a dashboard.
3. From the dashboard screen, 
 do one 
 of the following:
 


	* In the
	 upper area of the dashboard, select one of the predefined time ranges. These span
	 from 1 hour to 1 week (**1h**,
	 **3h**, **12h**,
	 **1d**, **3d**, or
	 **1w**).
	* Alternatively, you can
	 choose one of the following custom time range
	 options:
	
	
	
	
		+ Choose the
		 **custom**
		 dropdown, and then choose the
		 **Relative** tab. Select one of
		 the predefined ranges, which span from 1 minute to
		 15 months.
		+ Choose the
		 **custom**
		 dropdown, and then choose the
		 **Absolute** tab. Use the
		 calendar or text
		 fields
		 to specify your time range.

###### Tip

If
 the aggregation period is set to **Auto**
 when
 you change the time range of a
 graph,
 CloudWatch might change the period. To set the period manually, choose the
 **Actions** dropdown, and then choose
 **Period override**. 


###### To change the dashboard time zone format

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**,
 and then
 choose
 a dashboard.
3. In the
 upper-right
 corner of the dashboard screen, choose the
 **Custom** dropdown.
4. In the
 upper-right
 corner of the box that appears, select **UTC** or
 **Local timezone** from the dropdown.
