

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Terminating a query for a cluster
<a name="ending-cluster-multi-az"></a>

The procedure is applicable to both Multi-AZ and Single-AZ clusters.

**To terminate a query**

You can also use the **Queries** page to end a query that is currently in progress.

Your database user must have the sys:operator role and permissions to end a running query. For information about system roles, see [Amazon Redshift system-defined roles](https://docs.aws.amazon.com/redshift/latest/dg/r_roles-default.html) in the *Amazon Redshift Database Developer Guide*.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Queries and loads** to display the list of queries for your account. 

1. Choose the running query that you want to end in the list, and then choose **Terminate query**. 