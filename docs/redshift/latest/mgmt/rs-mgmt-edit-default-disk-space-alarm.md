Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a disk space

alarm

You can monitor disk space usage and set alarms to be notified when disk space exceeds
a specified threshold for a cluster. Creating a disk space usage alarm allows you to
proactively manage storage capacity and prevent issues caused by insufficient disk
space, such as query failures or data ingestion errors. The following procedure guides
you through the process of creating a disk space usage alarm.

###### To create a disk space usage alarm for a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Alarms**.
3. For **Actions**, choose **Create alarm**.
   The **Create alarm** page appears.
4. Follow the instructions on the page.
5. Choose **Create alarm**.
