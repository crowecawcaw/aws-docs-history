

# Specify a query result location
<a name="query-results-specify-location"></a>

The query result location that Athena uses is determined by a combination of workgroup settings and *client-side settings*. Client-side settings are based on how you run the query. 
+  If you run the query using the Athena console, the **Query result location** entered under **Settings** in the navigation bar determines the client-side setting. 
+ If you run the query using the Athena API, the `OutputLocation` parameter of the [StartQueryExecution](https://docs.aws.amazon.com/athena/latest/APIReference/API_StartQueryExecution.html) action determines the client-side setting. 
+ If you use the ODBC or JDBC drivers to run queries, the `S3OutputLocation` property specified in the connection URL determines the client-side setting. 

**Important**  
When you run a query using the API or using the ODBC or JDBC driver, the console setting does not apply. 

Each workgroup configuration has an [Override client-side settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) option that can be enabled. When this option is enabled, the workgroup settings take precedence over the applicable client-side settings when an IAM principal associated with that workgroup runs the query.

## About previously created default locations
<a name="query-results-specify-location-previous-defaults"></a>

Previously in Athena, if you ran a query without specifying a value for **Query result location**, and the query result location setting was not overridden by a workgroup, Athena created a default location for you. The default location was `aws-athena-query-results-{{MyAcctID}}-{{MyRegion}}`, where {{MyAcctID}} was the Amazon Web Services account ID of the IAM principal that ran the query, and {{MyRegion}} was the region where the query ran (for example, `us-west-1`.)

Now, before you can run an Athena query in a region in which your account hasn't used Athena previously, you must specify a query result location, or use a workgroup that overrides the query result location setting. While Athena no longer creates a default query results location for you, previously created default `aws-athena-query-results-{{MyAcctID}}-{{MyRegion}}` locations remain valid and you can continue to use them.

**Topics**
+ [About previously created default locations](#query-results-specify-location-previous-defaults)
+ [Specify a query result location using the Athena console](query-results-specify-location-console.md)
+ [Specify a query result location using a workgroup](query-results-specify-location-workgroup.md)