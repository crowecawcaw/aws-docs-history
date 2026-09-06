

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Viewing automatic optimization data
<a name="performance-metrics-autonomics"></a>

The Amazon Redshift console provides information about automatic optimizations, or autonomics, run using extra compute resources. You can use this information to track usage and monitor whether usage limits have been reached. Though Amazon Redshift doesn't bill you for autonomics run on the provisioned cluster itself, it does bill you for autonomics run using extra compute resources. For more information, see [ Allocating extra compute resources for automatic database optimizations](https://docs.aws.amazon.com/redshift/latest/dg/t_extra-compute-autonomics.html) in the *Amazon Redshift Database Developer Guide*.

**To view extra compute autonomics data**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, then choose the name of a cluster from the list to open its details.

1. From the cluster's details page, select **Manage usage limit** from the **Actions** drop-down menu. You can also select the **Maintenance** tab for a cluster, then scroll down and select **Create usage limits**.

1. The graph showing extra compute autonomics data appears under the section titled **Usage limit for extra compute for automatic optimization**. The graph displays the amount of time that Amazon Redshift runs autonomics using extra compute resources in a given time period.