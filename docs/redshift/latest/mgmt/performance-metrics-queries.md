Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing queries and loads

The Amazon Redshift console provides information about queries and loads that run in the
database. You can use this information to identify and troubleshoot queries that
take a long time to process and that create bottlenecks preventing other queries
from processing efficiently. You can use the queries information in the Amazon Redshift
console to monitor query processing.

###### To display query performance data

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Queries and loads** to
   display the list of queries for your account.

By default, the list displays queries for all your clusters over the past
24 hours. You can change the scope of the displayed date in the console.

###### Important

The **Queries and loads** list displays the longest
running queries in the system, up to 100 queries.
