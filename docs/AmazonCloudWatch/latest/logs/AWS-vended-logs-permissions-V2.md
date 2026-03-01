# Logging that requires additional permissions [V2]

Some AWS services use a new method to send their logs. This is a flexible method
that enables you to set up log delivery from these services to one or more of the
following destinations: CloudWatch Logs, Amazon S3, or Firehose and X-Ray for trace delivery.

A working log delivery consists of three elements:

- A `DeliverySource`, which is a logical object that represents the
  resource(s) that actually send the logs.
- A `DeliveryDestination`, which is a logical object that represents
  the actual delivery destination.
- A `Delivery`, which connects a delivery source to delivery
  destination
  To configure logs delivery between a supported AWS service and a
  destination, you must do the following:

- Create a delivery source with [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md").
- Create a delivery destination with [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md").
- If you are delivering logs cross-account, you must use [PutDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md") in the destination account to assign
  an IAM policy to the destination. This policy authorizes creating
  a delivery from the delivery source in account A to the delivery destination in
  account B. For cross-account delivery, you must manually create the permission
  policies yourself.
- Create a delivery by pairing exactly one delivery source and one delivery
  destination, by using [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md").
  The following sections provide the details of the permissions you need to have when
  you are signed in to set up log delivery to each type of destination, using the V2
  process. These permissions can be granted to an IAM role that you are signed in
  with.

###### Important

It is your responsibility to remove log delivery resources after deleting the
log-generating resource. To do so, follow these steps.

1. Delete the `Delivery` by using the [DeleteDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md") operation.
2. Delete the `DeliverySource` by using the [DeleteDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md") operation.
3. If the `DeliveryDestination` associated with the
   `DeliverySource` that you just deleted is used only for this
   specific `DeliverySource`, then you can remove it by using the
   [DeleteDeliveryDestinations](../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.md") operation.

###### Contents

- [Logs sent to CloudWatch Logs](AWS-logs-infrastructure-V2-CloudWatchLogs.md "AWS-logs-infrastructure-V2-CloudWatchLogs.md")
- [Logs sent to Amazon S3](AWS-logs-infrastructure-V2-S3.md "AWS-logs-infrastructure-V2-S3.md")
  - [Amazon S3 bucket server-side encryption](AWS-logs-infrastructure-V2-S3.md#AWS-logs-SSE-KMS-S3-V2 "AWS-logs-infrastructure-V2-S3.md#AWS-logs-SSE-KMS-S3-V2")

- [Logs sent to Firehose](AWS-logs-infrastructure-V2-Firehose.md "AWS-logs-infrastructure-V2-Firehose.md")
- [Traces sent to X-Ray](AWS-logs-infrastructure-V2-XRayTraces.md "AWS-logs-infrastructure-V2-XRayTraces.md")
