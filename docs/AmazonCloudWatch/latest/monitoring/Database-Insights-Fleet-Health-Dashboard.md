# Viewing the Fleet Health Dashboard for CloudWatch Database Insights

You can use the Fleet Health Dashboard to view a snapshot of the health of your database fleet.


![Fleet Health Dashboard](images/dbi_fhd.png)

## Fleet health views


A *database fleet* in Database Insights is a group of databases that you want to monitor. 
 You can create a monitoring view for a database fleet by choosing filters in the **Filters** component. 
 This component allows you to apply filters on properties, such as cluster or instance names and tags. 
 In the Fleet Health Dashboard, CloudWatch shows databases that match at least one of the filter conditions for the fleet health view.



![Filter by properties and tags](images/dbi_filter.png)

To create, modify, or delete views for database fleets, use the procedures in the following topics.



* [Create a fleet health view for CloudWatch Database Insights](Database-Insights-fleet-views-create.md "Database-Insights-fleet-views-create.md")
* [Edit a fleet health view for CloudWatch Database Insights](Database-Insights-fleet-views-edit.md "Database-Insights-fleet-views-edit.md")
* [Delete a fleet health view for CloudWatch Database Insights](Database-Insights-fleet-views-delete.md "Database-Insights-fleet-views-delete.md")

## RDS instances overview table


Use the **RDS instances overview** table to view the alarm state, max DB Load percentage, and the time of the last state update for each instance in your fleet.



![Amazon RDS resources table](images/dbi_fhd-resources.png)

## Instances state summary


Use the **Instances state summary** to view the health of all instances in your fleet. The Instances state summary provides two views based on **Alarms** and the DB Load metric. By default, CloudWatch displays the **Alarms** view.



![Instances state summary](images/dbi_iss.png)

Each node in the honeycomb represents an instance. For more information about an instance, you can choose the corresponding node and choose **Filter view by this instance**. 



![Instances state summary selected](images/dbi_iss-selected.png)

The honeycomb component summarizes the alarm state for instances in your fleet with the number of nodes in each state at the top of the honeycomb. CloudWatch displays the time of the last refresh of the data shown in the honeycomb.


When you switch to the **DB Load** view, you can see the overall health of the fleet from the point of view of the DB Load metric. Database load (DB Load) measures the number of active sessions in your database. DB Load is the key metric in Database Insights and is collected every second. CloudWatch categorizes DB instances into the following states based on thresholds for DB Load. 



* High
* Warning
* Ok
* Idle

You can see the thresholds for DB Load by choosing the corresponding state icons.


For information about DB Load for Amazon RDS, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.Overview.ActiveSessions.html") in the *Amazon RDS User Guide*. For information about DB Load for Amazon Aurora, see [Database load](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.Overview.ActiveSessions.html") in the *Amazon Aurora User Guide*.


By default, CloudWatch displays the average DB Load. Choose **Max** to monitor the maximum DB Load for each instance.


Choose a node from the Instances state summary to display alarms and DB Load for the instance.


## Top 10 charts


Use the **Top 10 instances per relative DB Load** chart to view the DB Load trend over time for the 10 instances with the highest DB Load. The chart also provides the top queries and top wait events for the instance with the highest DB Load.



![Top 10 instances by DB Load chart](images/dbi_top10.png)

Use the **Top 10 instances per metric** charts to compare two key metrics for the top 10 instances in your fleet. You can select the following metrics.



* CPU Utilization (%)
* Freeable Memory (%)
* DB Connections (%)
* Network throughput
* Read IOPS
* Write IOPS
* Read Latency
* Write Latency


![Top 10 instances per metrics charts](images/dbi_fhd-top10per.png)

## Amazon RDS events


Use the **Events** summary and table to view RDS events for instances in your fleet.



![Events summary](images/dbi_events.png)

To view the **Events** table, choose **Details**.



![Events details](images/dbi_events-details.png)

For a list of events for Amazon RDS and Amazon Aurora, see the following topics.



* [Amazon RDS event categories and event messages for Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Events.Messages.html") in the *Amazon Aurora User Guide*
* [Amazon RDS event categories and event messages](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.Messages.html") in the *Amazon RDS User Guide*

## Calling services table


Use the **Calling services** table to view CloudWatch Application Signals services that are calling your database endpoints and related application-level metrics such as latency or errors.



![Calling services table](images/dbi_fhd-calling.png)

Database Insights shows the services that are calling your top 10 instances by DB Load. To view calling services for another instance, choose the instance in the database instance dashboard.


When the endpoint called by the application is an Aurora cluster, Database Insights will display either the writer or the reader endpoint for the Aurora cluster in the **Calling services** table, not the individual 
 database instance. However, when the endpoint called by the application is an Amazon RDS cluster, Database Insights shows the specific database instance the application is calling within the Amazon RDS cluster.


For more information about CloudWatch Application Signals, see [Application Signals](CloudWatch-Application-Monitoring-Sections.md "CloudWatch-Application-Monitoring-Sections.md").
