# View sample queries with the CloudTrail console

The CloudTrail console provides a number of sample queries that can help you get started writing your 
 own queries.

CloudTrail queries incur charges based upon the amount of data scanned. To help control costs, 
 we recommend that you constrain queries by adding starting and ending `eventTime` time stamps to queries. 
 For more information about CloudTrail pricing, see [AWS CloudTrail
 Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

###### Note

You can also view queries created by the GitHub community. For more
 information, see [CloudTrail
 Lake sample queries](https://github.com/aws-samples/cloud-trail-lake-query-samples "https://github.com/aws-samples/cloud-trail-lake-query-samples") on the GitHub website. AWS CloudTrail has not evaluated the queries in GitHub. 

###### To view and run a sample query

1. Sign in to the AWS Management Console and open the CloudTrail console at
 [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. From the navigation pane, under **Lake**, choose **Query**.
3. On the **Query** page, choose the **Sample
 queries** tab.
4. Choose a sample query from the list or enter a phrase to search by. In this example, we'll open the query **Investigate who made console changes** by choosing the **Query
 name**. This opens the query in the **Editor** tab.


###### Note

By default, this page uses basic search functionality. You can improve the search functionality 
 by adding permissions for the `cloudtrail:SearchSampleQueries` action, if it is not 
 already provided by your permissions policy. The [`AWSCloudTrail_FullAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSCloudTrail_FullAccess.html") 
 managed policy provides permissions to perform the `cloudtrail:SearchSampleQueries` action.



![Sample queries tab](images/query-sample-console.png)
5. On the **Editor** tab, choose the event data store for which you want to run the query. When you choose the event data store from the list, 
 CloudTrail automatically populates the event data store ID in the `FROM` line of the query editor.



![Choose event data store for query](images/query-editor-console.png)
6. Choose **Run** to run the query.


The **Command output** tab shows you metadata about your query, such as whether the query was successful, the number of records matched, and the run time of the query.



![View query status](images/query-console-status.png)

The **Query results** tab shows you the event data in the selected event data store that matched your query.



![View query results](images/query-console-results.png)
For more information about editing a query, see [Create or edit a query with the CloudTrail console](query-create-edit-query.md "query-create-edit-query.md"). 
 For more information about running a query and saving query results, see [Run a query and save query results with the console](query-run-query.md "query-run-query.md").
