# Logging and monitoring

To detect incidents, receive alerts when incidents occur, and respond to them, use these options with Amazon EMR on EKS:

- Monitor Amazon EMR on EKS with AWS CloudTrail ‐ [AWS CloudTrail](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md") provides a record of actions
  taken by a user, role, or an AWS service in Amazon EMR on EKS. It captures calls from the
  Amazon EMR
  console and code calls to the Amazon EMR on EKS API operations as events. This
  allows you to determine the request that was made to Amazon EMR on EKS, the IP address from which
  the request was made, who made the request, when it was made, and additional details. For
  more information, see [Logging Amazon EMR on EKS API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- Use CloudWatch Events with Amazon EMR on EKS ‐ CloudWatch Events delivers a near real-time stream
  of system events that describe changes in AWS resources. CloudWatch Events becomes aware of
  operational changes as they occur, responds to them, and takes corrective action as
  necessary, by sending messages to respond to the environment, activating functions, making
  changes, and capturing state information. To use CloudWatch Events with Amazon EMR on EKS, create a
  rule that triggers on an Amazon EMR on EKS API call via CloudTrail. For more information, see [Monitor jobs with Amazon CloudWatch Events](monitoring.md#monitoring-cloudwatch-events "monitoring.md#monitoring-cloudwatch-events").
