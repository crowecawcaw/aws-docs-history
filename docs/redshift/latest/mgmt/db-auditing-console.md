Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Enabling audit logging

Configure Amazon Redshift to export audit log data. Logs can be exported to CloudWatch, or as files
to Amazon S3 buckets.

## Enabling audit logging using the

console

###### To enable audit logging for a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then
   choose the cluster that you want to update.
3. Choose the **Properties** tab. On the
   **Database configurations** panel, choose
   **Edit**, then **Edit audit
   logging**.
4. On the **Edit audit logging** page, choose
   **Turn on** and select **S3
   bucket** or **CloudWatch**. We recommend
   using CloudWatch because administration is easy and it has helpful
   features for data visualization.
5. Choose which logs to export.
6. To save your choices, choose **Save
   changes**.
