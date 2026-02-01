Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing queries and loads for Multi-AZ

data warehouses

You can view information on queries that ran in the past 7 days irrespective of the
type, size, and status (pause or resume) of your cluster.

The information shown on the queries and loads page is populated with information from
Amazon Redshift system tables (SYS\_\* views). This information lets you display additional
information about your queries and offers rolling 7 days of retention. Query diagnostics
become faster, letting you filter data by database, username, or SQL statement type. To
see these additional filters and information on all queries that ran, note the following
prerequisites:

- You must connect to a database by choosing **Connect to
  database**.
- Your database user must have the sys:operator or sys:monitor roles and
  permissions to perform query monitoring. For information about system roles, see
  [Amazon Redshift system-defined
  roles](../dg/r_roles-default.md "../dg/r_roles-default.md") in the _Amazon Redshift Database Developer Guide_.
  You will see these additional filters and query information once you connect to a
  database.

###### To display query performance data from Queries and loads

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Queries and loads** to
   display the list of queries for your account.
3. You might have to connect to a database to see additional filter. If required,
   click **Connect to database** and follow the prompts to connect
   to a database.

By default, the list displays queries for all your clusters over the past 24
hours. You can change the scope of the displayed date in the console.

###### To display query performance data from Query monitoring

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**. Under
   **Clusters**, select a cluster.
3. Choose **Query monitoring**.
4. Depending on the configuration or version of your cluster, you might have to
   connect to a database to see additional filters. If required, click
   **Connect to database** and follow the prompts to connect
   to a database.
