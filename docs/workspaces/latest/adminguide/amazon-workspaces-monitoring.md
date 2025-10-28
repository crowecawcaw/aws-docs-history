# Monitor WorkSpaces Personal

You can use the following features to monitor your WorkSpaces.

**CloudWatch metrics**

Amazon WorkSpaces publishes data points to Amazon CloudWatch about your WorkSpaces. CloudWatch
enables you to retrieve statistics about those data points as an ordered set of
time-series data, known as _metrics_. You can use these
metrics to verify that your WorkSpaces are performing as expected. For more
information, see [Monitor your WorkSpaces using CloudWatch metrics](cloudwatch-metrics.md "cloudwatch-metrics.md").

**CloudWatch Events**

Amazon WorkSpaces can submit events to Amazon CloudWatch Events when users log in to your WorkSpace.
This enables you to respond when the event occurs. For more information, see
[Monitor your WorkSpaces using Amazon EventBridge](cloudwatch-events.md "cloudwatch-events.md").

**CloudTrail logs**

AWS CloudTrail provides a record of actions taken by a user, role, or an AWS
service in WorkSpaces. Using the information collected by CloudTrail, you can determine the
request that was made to WorkSpaces, the IP address from which the request was made,
who made the request, when it was made, and additional details. For more
information, see [Logging WorkSpaces
API Calls by Using CloudTrail](../api/cloudtrail_logging.md "../api/cloudtrail_logging.md"). AWS CloudTrail logs successful and unsuccessful
sign-in events for smart card users. For more information, see [Understanding AWS sign-in events for smart card
users](signin-events.md "signin-events.md").

**CloudWatch Internet Monitor**

Amazon CloudWatch Internet Monitor provides visibility into how internet issues impact
the performance and availability between your applications hosted on AWS and
your end users. You can also use CloudWatch Internet Monitor to:

- Create monitors for one or more WorkSpace directories.
- Monitor internet performance.
- Get alarms for issues between your end users’ city-network, including
  its location and ASN, which is typically the Internet Service Provider
  (ISP), and their WorkSpace Regions.

Internet Monitor uses the connectivity data that AWS captures from its
global networking footprint to calculate a baseline of performance and
availability for internet-facing traffic. Internet Monitor currently can't
provide internet performance for individual end user but it can at city and ISP
level.

**Amazon S3 Access Logs**

If your users have application settings data or home folders data stored in
Amazon S3 buckets, consider viewing Amazon S3 server access logs to monitor access. These
logs provide detailed records about requests that are made to a bucket. Server
access logs are useful for many applications. For example, access log
information can be useful in security and access audits. For more information,
see [Amazon S3 Server
Access Logging](../../../AmazonS3/latest/dev/ServerLogs.md "../../../AmazonS3/latest/dev/ServerLogs.md") in the _Amazon Simple Storage Service User Guide_.
