End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Logging AWS Elemental MediaStore API calls with

AWS CloudTrail

AWS Elemental MediaStore is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in MediaStore. CloudTrail captures a
subset of API calls for MediaStore as events, including calls from the MediaStore
console and from code calls to the MediaStore API. If you create a trail, you can
enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for
MediaStore. If you don't configure a trail, you can still view the most recent events
in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to MediaStore, the IP
address from which the request was made, who made the request, when it was made, and
more.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [AWS Elemental MediaStore
  information in CloudTrail](monitoring-service-info-in-cloudtrail.md "monitoring-service-info-in-cloudtrail.md")
- [Example: AWS Elemental MediaStore log
  file entries](monitoring-example-log-file-entries.md "monitoring-example-log-file-entries.md")
