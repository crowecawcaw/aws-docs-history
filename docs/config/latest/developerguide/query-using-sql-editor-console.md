# Query Using the SQL Query Editor for

AWS Config (Console)

|                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Introducing a preview feature for advanced queries that allows you to<br>use generative artificial intelligence (generative AI) capabilities to<br>enter prompts in plain English and convert them into a ready-to-use<br>query format. For more information, see [Natural language query<br>processor for advanced queries](query-assistant.md "query-assistant.md"). |

You can either use AWS sample queries or you can create your own query called as
custom queries.

## Considerations

**Prerequisites**

If you are using the one of the following AWS managed policies, you will have
the necessary permissions to run and save a query: [AWSServiceRoleForConfig](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForConfig "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSServiceRoleForConfig") (service-linked role) or [AWS_ConfigRole](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS_ConfigRole "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS_ConfigRole").

Otherwise, you must have the permissions included in the [AWSConfigUserAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSConfigUserAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSConfigUserAccess") AWS managed policy.

**List of properties that you can query**

An updated list of properties and their data types is available in [GitHub](https://github.com/awslabs/aws-config-resource-schema "https://github.com/awslabs/aws-config-resource-schema").

**Advanced queries and aggregators**

To run a query on an aggregator, create an aggregator. For more information, see
[Creating Aggregators for AWS Config](aggregated-create.md "aggregated-create.md").

If you already have an aggregator set up, in the query scope, choose the
aggregator to run an advanced query on that aggregator. When you select an
aggregator, consider adding the AWS account ID and AWS Region in the query
statement to view that information in the results.

## Use an AWS Sample Query

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Advanced queries** from the left navigation to
   query your resource configurations for a single account and Region or for
   multiple accounts and Regions.
3. On the **Advanced queries** page, choose an appropriate
   query from the list of queries. You can filter through the list of queries
   either by the name, description, creator, or tags. To filter for AWS
   queries, choose
   **Creator**,
   and enter **AWS**. The query that you select is displayed
   in the SQL query editor. You can edit the selected query
   to
   fit your needs.
4. To save this query to a new query, choose **Save
   As**.
   - In the **Query Name** field, update the name of
     the query.
   - In the **Description** field, update the
     description of the query.
   - Enter up to 50 unique tags for this query.
   - Choose **Save**.

5. Choose **Run**. The query results are displayed in the
   table below the query editor.
6. Choose **Export as** to export the query results in CSV
   or JSON format.

## Create your custom query

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Choose **Advanced queries** from the left navigation to
   query your resource configurations for a single account and Region or for
   multiple accounts and Regions.
3. To create your custom query, choose **New query**.

To view or edit a custom query, filter a query either by the name,
description, creator or tags. To filter custom queries, choose
**Creater** and enter
**Custom**. 4. On the **Query editor** page, create your own query for
this account and Region. You can also select an appropriate aggregator to
create a query for multiple accounts and Regions. 5. Edit if you wish you make changes to this query. Choose **Save
Query** to save this query.

    * In the **Query Name** field, update the name of
     the query.
    * In the **Description** field, update the
     description of the query.
    * Enter up to 50 unique tags for this query.
    * Choose **Save**.

6. Choose **Run**. The query results are displayed in the
   table below the query editor.
7. Choose **Export as** to export the query results in CSV
   or JSON format.
