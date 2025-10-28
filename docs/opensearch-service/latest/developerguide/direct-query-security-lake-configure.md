# Configuring and querying a

Security Lake data source in OpenSearch Dashboards

Now that you've created your data source, you can set it up in OpenSearch Dashboards.

This section walks you through various use cases with your data source in
OpenSearch Dashboards before you query your data. To get started, you need to
navigate to your data source in OpenSearch Dashboards. In the left-hand menu, under
**Management**, choose **Data sources**. Then,
select the name of the data source that you created earlier in the OpenSearch Service
console.

## Query Security Lake

tables from Discover

If you have created tables based on your Security Lake logs, you can now query those
tables directly from OpenSearch Discover. This enables you to seamlessly access
and analyze data stored in Security Lake, directly from the familiar Discover interface.
By querying Security Lake directly from Discover, you can avoid the need to manually
extract, transform, and load the data into a separate search index. To quickly
get started analyzing your logs, Discover includes a set of PPL and SQL saved
queries.

Start by selecting the data source that you configured. Select the associated
database and table you want to query, then use the search bar to write queries
against your tables. To understand what statements, commands, and limitations
are supported for the Security Lake integration, see [Supported SQL and PPL commands](direct-query-supported-commands.md "direct-query-supported-commands.md").

To take advantage of the pre-built queries that are available for Security Lake, go to
**...** on the top right hand side of Discover, choose
**Open Query** and then choose
**Templates**. There are many pre-built queries available
for log sources supported in Security Lake. Search for the templates that match your use
case, copy the query to use in the search bar, and replace templated fields
(such as Region and action) with your own information.

## Accelerate data

from Discover

To enhance performance and enable faster subsequent queries and analysis in
OpenSearch, you can ingest the results of your query from Discover into an
OpenSearch indexed view.

###### To create an indexed view

1. From Discover, choose **Create Indexed View**.
2. In the query editor, enter your desired query. You can create a new
   query here or use an existing one from your previous searches.
3. Specify a name for your new indexed view. Choose a descriptive name
   that will help you identify the view later.
4. Configure the data retention settings for your indexed view. You can
   specify how long the data should be kept in the index, allowing you to
   balance performance with storage costs.
5. Create the indexed view. After it's created, your indexed view will be
   available for faster querying and analysis.

If you've previously created indexed views, you can access them from
Discover.

###### To use an existing index view

1. From Discover, choose **Select Indexed View** to see
   a list of your existing indexed views for Security Lake.
2. Choose the indexed view you want to use. This will apply the view to
   your current query, potentially significantly speeding up your data
   retrieval and analysis.

## Create a dashboard

view for your data source

When you use OpenSearch Service, you can analyze popular AWS log types using pre-built
dashboard templates. For Security Lake there are templates for VPC, CloudTrail, and WAF
logs. These templates allow you to create a dashboard tailored to your specific
data. They include pre-built queries and dashboards tailored for that specific
log type. This enables you to quickly get up and running with analyzing these
popular AWS log sources, without having to build everything from
scratch.

###### Note

Dashboards use indexed views, which ingest data from Security Lake and contribute
to direct query and collection compute.

Follow these steps to create a dashboard using one of these pre-built
templates, so you can start exploring and analyzing your data right away.

###### To create a dashboard view

1. Navigate to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. From the left navigation pane, choose **Central
   management**, then **Connected data
   sources**.
3. Select the data source to open the details page.
4. Choose **Create dashboard**.
5. Choose which type of dashboard you want to create.
6. Enter a name for your dashboard.
7. Enter an optional description for your dashboard.
8. Select one or more AWS Glue tables to view on your dashboard.
9. Choose how often you want to refresh the data in your
   dashboard.
10. Choose which OpenSearch workspace you want to use.
    1. To create a new workspace, select **Create new
       workspace**.
    2. To use an existing workspace, select **Select existing
       workspace**.

11. Enter a name for your workspace.
12. Choose **Create dashboard**.

## Troubleshooting

There might be instances when results don’t return as expected. If you
experience any issues, make sure that you're following the [Recommendations for using direct queries
in Amazon OpenSearch Service](direct-query-recommendations.md "direct-query-recommendations.md").
