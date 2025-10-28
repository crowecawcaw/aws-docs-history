Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Logging Amazon Monitron actions with

AWS CloudTrail

Amazon Monitron is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Monitron. CloudTrail captures API calls for
Amazon Monitron as events. CloudTrail captures calls from both the Amazon Monitron console and the
Amazon Monitron mobile app. If you create a trail, you can enable continuous delivery of CloudTrail
events to an Amazon Simple Storage Service (Amazon S3) bucket, including events for Amazon Monitron. If you don't
configure a trail, you can still view the most recent events in the CloudTrail console in
**Event history**. Using the information collected by CloudTrail, you can
determine the console or mobile app request that was made to Amazon Monitron, the IP address
from which the request was made, who made the request, when it was made, and additional
details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Amazon Monitron information in
  CloudTrail](service-name-info-in-cloudtrail.md "service-name-info-in-cloudtrail.md")
- [Example: Amazon Monitron log file
  entries](understanding-service-name-entries.md "understanding-service-name-entries.md")
