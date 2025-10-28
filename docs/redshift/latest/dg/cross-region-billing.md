Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing cost control for cross-Region data

sharing

With Amazon Redshift, you can manage cost control for cross-Region data sharing by
configuring data sharing to limit the amount of data that is transferred between
AWS Regions. Managing cost control for cross-Region data sharing allows you to
set data transfer limits, monitor data transfer usage, and receive notifications
when approaching or exceeding those limits.

When consuming data from a different Region, the consumer pays the Cross-Region
data transfer fee from the producer Region to the consumer Region. The price of
data transfer is different for different Regions. The charge is based on the bytes
of data scanned for every successful query run. For more information about
Amazon Redshift pricing, see [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

You are charged for the number of bytes, rounded up to the next megabyte, with
a 10MB minimum per query. You can set cost controls on your query usage and view
the amount of data being transferred per query on your cluster.

To monitor and control your usage and associated cost of using cross-Region
data sharing, you can create daily, weekly, monthly usage limits, and define
actions that Amazon Redshift automatically takes if those limits are reached to help
maintain your budget with predictability.

Depending on the usage limits you set, actions that Amazon Redshift takes can be to
log an event to a system table, send a CloudWatch alarm and notify an administrator with
an Amazon SNS, or to turn off cross-Region data sharing for further usage.

To create usage limits in the Amazon Redshift console, choose **Configure
usage limit** under **Actions** for your cluster. You
can monitor your usage trends and get alerts on usage exceeding your defined
limits with automatically generated CloudWatch metrics from the **Cluster
performance** or **Monitoring** tabs. You can also
create, modify, and delete usage limits programmatically by using the AWS CLI or
Amazon Redshift API operations.
