

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Analyzing query execution
<a name="analyzing-query-execution"></a>

You can analyze the execution details of a query to understand how it performed and identify potential areas for optimization. Analyzing a query provides insights into the query plan, including the steps involved, the time taken by each step, and the amount of data processed. Common use cases include troubleshooting slow-running queries, optimizing data distribution strategies, and identifying opportunities for query rewriting or indexing. 

**To analyze a query**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Queries and loads** to display the list of queries for your account. You might need to change settings on this page to find your query. 

1. Choose the **Query** identifier in the list to display **Query details**. 

   The **Query details** page includes **Query details** and **Query plan** tabs with metrics about the query. 
**Note**  
You can also navigate to the **Query details** page from a **Cluster details** page, **Query history** tab when you drill down into a query in a **Query runtime** graph. 

The **Query details** page contains the following sections:
+ A list of **Rewritten queries**, as shown in the following screenshot.  
![Table showing a list of rewritten queries, with attributes such as start time, duration, status, and query ID as the column names.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/query-details-rewritten-queries.png)
+ A **Query details** section, as shown in the following screenshot.  
![The query details section in the console showing attributes for a specific query.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/query-details-query.png)
+ A **Query details** tab that contains the **SQL** that was run and **Execution details** about the run. 
+ A **Query plan** tab that contains the **Query plan** steps and other information about the query plan. This table also contains graphs about the cluster when the query ran. 
  + **Cluster health status**   
![The cluster health status section of the console showing the cluster health during the workload.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/query-details-cluster-health-status.png)
  + **CPU utilization**   
![The CPU utilization section in the console showing a line graph of CPU utilization of the cluster in increments of minutes.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/query-details-cpu-utilization.png)
  + **Storage capacity used**   
![The storage capacity used section in the console showing a line graph of the percent of stoage capacity used in increments of minutes.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/query-details-storage-capacity-used.png)
  + **Active database connections**   
![The active database connections section in the console showing a line graph of the number of active database connections to the cluster over time.](http://docs.aws.amazon.com/redshift/latest/mgmt/images/query-details-active-database-connections.png)