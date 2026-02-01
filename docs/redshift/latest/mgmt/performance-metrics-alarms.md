Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating an alarm

Alarms you create in the Amazon Redshift console are CloudWatch alarms. They are useful because
they help you make proactive decisions about your cluster or serverless instance. You
can set one or more alarms on any of the metrics listed in [Performance data in Amazon Redshift](metrics-listing.md "metrics-listing.md"). For example, setting an
alarm for high `CPUUtilization` on a cluster node helps indicate when the
node is overutilized. An alarm for high `DataStorage` would keep track of the
storage space that your serverless namespace is using for your data.

From **Actions**, you can modify or delete alarms. You can also
create a chime or slack alert to send an alert from CloudWatch to Slack or Amazon Chime by
specifying a Slack or Amazon Chime webhook URL.

In this section, you can find how to create an alarm using the Amazon Redshift console. You
can create an alarm using the CloudWatch console or any other way you work with metrics, such
as with the AWS CLI or an AWS SDK.

###### To create a CloudWatch alarm with the Amazon Redshift console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").

If you're using Amazon Redshift Serverless, Choose **Go to Serverless** on the upper right of the dashboard. 2. On the navigation menu, choose **Alarms**, then choose
**Create alarm**. 3. On the **Create alarm** page, enter the properties to create
a CloudWatch alarm. 4. Choose **Create alarm**.
