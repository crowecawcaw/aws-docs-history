Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Finding your cluster connection

string

To connect to your cluster with your SQL client tool, you must have the
cluster connection string. You can find the cluster connection string in the
Amazon Redshift console, on a cluster's details page.

###### To find the connection string for a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then
   choose the cluster name from the list to open its details.
3. The **JDBC URL** and **ODBC URL**
   connection strings are available, along with additional details, in the
   **General information** section. Each string is
   based on the AWS Region where the cluster runs. Click the icon next to
   the appropriate connection string to copy it.
   To connect to a cluster endpoint, you can use the cluster endpoint URL from a
   [DescribeClusters API request](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md"). The following is an example of a
   cluster endpoint URL.

```
mycluster.cmeaswqeuae.us-east-2.redshift.amazonaws.com
```

If you have set up a custom domain name for your cluster, you can also use
that to connect to your cluster. For more information about creating a custom
domain name, see [Setting
up a custom domain name](connecting-connection-CNAME-connect.md "connecting-connection-CNAME-connect.md").

###### Note

When you connect, don't use the IP address of a cluster node or the IP
address of the VPC endpoint. Always use the Redshift endpoint to avoid an
unnecessary outage. The only exception to using the endpoint URL is when you
use a custom domain name. For more information, see [Using a custom
domain name for client connections](connecting-connection-CNAME.md "connecting-connection-CNAME.md").
