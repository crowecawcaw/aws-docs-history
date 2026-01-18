Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Viewing automatic optimization data

The Amazon Redshift console provides information about automatic optimizations, or autonomics,
run using extra compute resources. You can use this information to track usage
and monitor whether usage limits have been reached.
Though Amazon Redshift doesn't bill you for autonomics run on the provisioned cluster itself,
it does bill you for autonomics run using extra compute resources. For more information,
see [Allocating extra compute resources for automatic database optimizations](../dg/t_extra-compute-autonomics.md "../dg/t_extra-compute-autonomics.md")
in the _Amazon Redshift Database Developer Guide_.

###### To view extra compute autonomics data

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose
   the name of a cluster from the list to open its details.
3. From the cluster's details page, select **Manage usage limit**
   from the **Actions** drop-down menu. You can also select the
   **Maintenance** tab for a cluster, then scroll down and select
   **Create usage limits**.
4. The graph showing extra compute autonomics data appears under the section titled
   **Usage limit for extra compute for automatic optimization**.
   The graph displays the amount of time that Amazon Redshift runs autonomics using extra
   compute resources in a given time period.
