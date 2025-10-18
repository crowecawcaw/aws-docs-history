# Viewing the CloudWatch RUM dashboard

CloudWatch RUM helps you collect data from user sessions about your application's performance,
 including page load times, Apdex score, browsers and devices used, geolocation of user
 sessions, and sessions with errors. All of this information is displayed in a
 dashboard.

###### To view the RUM dashboard

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Application Signals**,
 **RUM**.


The **Overview** tab displays information collected by one of
 the app monitors that you have created. 


The top row of panes displays the following information for this app monitor: 




	* Number of page loads
	* Average page load speed
	* Apdex score
	* Status of any alarms associated with the app monitor
The application performance index (Apdex) score indicates end users' level of
 satisfaction. Scores range from 0 (least satisfied) to 1 (most satisfied). The
 scores are based on application performance only. Users are not asked to rate
 the application. For more information about Apdex scores, see [How CloudWatch RUM sets Apdex scores](CloudWatch-RUM-apdex.md "CloudWatch-RUM-apdex.md").


Several of these panes include links that you can use to further examine the
 data. Choosing any of these links displays a detailed view with
 **Performance**, **Errors**, **HTTP requests**,
 **Sessions**, **Events Browsers & Devices**, and
 **User Journey** tabs at the top of the display.
3. To focus further, choose the **List view** tab and then
 choose the name of the app monitor that you want to focus on. This displays the 
 following tabs for the chosen app monitor.




	* The **Performance** tab displays page performance
	 information including load times, request information, web vitals, and page loads over time. This view features 
	 interactive web vitals graphs where you can see the different percentile values of core web vitals for your pages and 
	 choose datapoints on the graph to view associated events captured by CloudWatch RUM. From there, you can either explore more 
	 events related to the metric spike or view page details for a selected event to identify specific conditions causing performance issues.
	
	
	On this tab you can also toggle the view between **Page loads**,
	 **Requests**, and
	 **Location** to see more details about page performance.
	* The **Errors** tab displays Javascript error
	 information including the error message most frequently seen by users 
	 and the
	 devices and browsers with the most errors. This view includes a histogram of 
	 the errors and a list view of errors. You can filter the list of errors by user
	 and event details. Choose an error message to see more details.
	* The **HTTP requests** tab displays HTTP request
	 information including the request URL with most errors and the devices and browsers with the most errors. 
	 This tab includes a histogram of the requests, a list view of requests, and a list view of network errors. 
	 You can filter the lists by user and event details. Choose a response code or an error message to s
	 ee more details about the request or network error, respectively.
	* The **Sessions** tab displays session metrics. This tab includes a 
	 histogram of session start events and a list view of sessions. You can filter the list 
	 of sessions by event type, user details, and event details. Choose a **sessionId** to 
	 see more details about a session.
	* The **Events** tab displays a histogram of RUM events and a list 
	 view of the events. You can filter the list of events by event type, user details, and event details. 
	 Choose a RUM event to see the raw event.
	* The **Browsers & Devices** tab displays
	 information such as the performance and usage of different browsers and
	 devices to access your application. This view includes controls to
	 toggle the view between focusing on **Browsers** and
	 **Devices**.
	
	
	If you narrow the scope to a single browser, you see the data broken
	 down by browser version.
	* The **User Journey** tab displays the paths that your
	 customers use to navigate your application. You can see where your
	 customers enter your application and what page they exit your
	 application from. You can also see the paths that they take and the
	 percentage of customers that follow those paths. You can pause on a node
	 to get more details about that page. You can choose a single path to
	 highlight the connections for easier viewing.
4. (Optional) On any of the first six tabs, you can choose the **Pages** button and
 select a page or page group from the list. This narrows down the displayed data to a single
 page or group of pages of your application. You can also mark pages and page groups in the list as
 favorites.
