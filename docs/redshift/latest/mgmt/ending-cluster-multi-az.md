Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Terminating a query for a cluster

The procedure is applicable to both Multi-AZ and Single-AZ clusters.

###### To terminate a query

You can also use the **Queries** page to end a query that is
currently in progress.

Your database user must have the sys:operator role and permissions to end a
running query. For information about system roles, see [Amazon Redshift system-defined roles](../dg/r_roles-default.md "../dg/r_roles-default.md") in
the _Amazon Redshift Database Developer Guide_.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Queries and loads** to
   display the list of queries for your account.
3. Choose the running query that you want to end in the list, and then choose
   **Terminate query**.
