

# Logging that requires additional permissions [V2]
<a name="AWS-vended-logs-permissions-V2"></a>

Some AWS services use a new method to send their logs. This is a flexible method that enables you to set up log delivery from these services to one or more of the following destinations: CloudWatch Logs, Amazon S3, or Firehose and X-Ray for trace delivery.

A working log delivery consists of three elements:
+ A `DeliverySource`, which is a logical object that represents the resource(s) that actually send the logs.
+ A `DeliveryDestination`, which is a logical object that represents the actual delivery destination.
+ A `Delivery`, which connects a delivery source to delivery destination

To configure logs delivery between a supported AWS service and a destination, you must do the following:
+ Create a delivery source with [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html).
+ Create a delivery destination with [PutDeliveryDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html).
+ If you are delivering logs cross-account, you can use only Amazon S3 and Firehose destinations. You must use [ PutDeliveryDestinationPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html) in the destination account to assign an IAM policy to the destination. This policy authorizes creating a delivery from the delivery source in account A to the delivery destination in account B. For cross-account delivery, you must manually create the permission policies yourself. For setup examples, see [Cross-account delivery example](vended-logs-crossaccount-example.md).
+ Create a delivery by pairing exactly one delivery source and one delivery destination, by using [ CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html).

## Log delivery setup examples
<a name="vended-logs-same-account-examples"></a>

The following examples create the delivery source and delivery destination in the same AWS account. Replace the source resource ARN and log type with values supported by the service that generates the logs. These examples don't require a delivery destination policy.

### Create a delivery source
<a name="vended-logs-same-account-example-source"></a>

Create the delivery source, and then use one of the destination examples that follow.

```
aws logs put-delivery-source \
    --name my-delivery-source \
    --resource-arn {{source-resource-arn}} \
    --log-type {{log-type}}
```

### Create a delivery to CloudWatch Logs
<a name="vended-logs-same-account-example-cwl"></a>

Create a delivery destination for an existing log group.

```
aws logs put-delivery-destination \
    --name my-cwl-delivery-destination \
    --delivery-destination-configuration \
    "destinationResourceArn=arn:aws:logs:{{region}}:{{account-id}}:log-group:{{log-group-name}}"
```

Create the delivery.

```
aws logs create-delivery \
    --delivery-source-name my-delivery-source \
    --delivery-destination-arn arn:aws:logs:{{region}}:{{account-id}}:delivery-destination:my-cwl-delivery-destination
```

### Create a delivery to Amazon S3
<a name="vended-logs-same-account-example-s3"></a>

Create a delivery destination for an existing bucket.

```
aws logs put-delivery-destination \
    --name my-s3-delivery-destination \
    --delivery-destination-configuration \
    "destinationResourceArn=arn:aws:s3:::{{bucket-name}}"
```

Create the delivery.

```
aws logs create-delivery \
    --delivery-source-name my-delivery-source \
    --delivery-destination-arn arn:aws:logs:{{region}}:{{account-id}}:delivery-destination:my-s3-delivery-destination
```

To configure a destination prefix, suffix path, or Hive-compatible path, see [Amazon S3 object key format](AWS-logs-infrastructure-V2-S3.md#AWS-logs-infrastructure-V2-S3-object-key).

### Create a delivery to Firehose
<a name="vended-logs-same-account-example-firehose"></a>

Create a delivery destination for an existing DirectPut delivery stream.

```
aws logs put-delivery-destination \
    --name my-firehose-delivery-destination \
    --delivery-destination-configuration \
    "destinationResourceArn=arn:aws:firehose:{{region}}:{{account-id}}:deliverystream/{{delivery-stream-name}}"
```

Create the delivery.

```
aws logs create-delivery \
    --delivery-source-name my-delivery-source \
    --delivery-destination-arn arn:aws:logs:{{region}}:{{account-id}}:delivery-destination:my-firehose-delivery-destination
```

### Create a delivery to X-Ray
<a name="vended-logs-same-account-example-xray"></a>

For trace delivery, use a source service and log type that supports delivery to X-Ray. Create the logical X-Ray delivery destination.

```
aws logs put-delivery-destination \
    --name my-xray-delivery-destination \
    --delivery-destination-type XRAY
```

Create the delivery.

```
aws logs create-delivery \
    --delivery-source-name my-delivery-source \
    --delivery-destination-arn arn:aws:logs:{{region}}:{{account-id}}:delivery-destination:my-xray-delivery-destination
```

To verify the delivery, use the following command.

```
aws logs describe-deliveries \
    --delivery-source-name-prefix my-delivery-source
```

The following sections provide the details of the permissions you need to have when you are signed in to set up log delivery to each type of destination, using the V2 process. These permissions can be granted to an IAM role that you are signed in with.

**Important**  
It is your responsibility to remove log delivery resources after deleting the log-generating resource. To do so, follow these steps.  
Delete the `Delivery` by using the [DeleteDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.html) operation.
Delete the `DeliverySource` by using the [DeleteDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.html) operation.
If the `DeliveryDestination` associated with the `DeliverySource` that you just deleted is used only for this specific `DeliverySource`, then you can remove it by using the [DeleteDeliveryDestinations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.html) operation.

**Contents**
+ [Log delivery setup examples](#vended-logs-same-account-examples)
  + [Create a delivery source](#vended-logs-same-account-example-source)
  + [Create a delivery to CloudWatch Logs](#vended-logs-same-account-example-cwl)
  + [Create a delivery to Amazon S3](#vended-logs-same-account-example-s3)
  + [Create a delivery to Firehose](#vended-logs-same-account-example-firehose)
  + [Create a delivery to X-Ray](#vended-logs-same-account-example-xray)
+ [Logs sent to CloudWatch Logs](AWS-logs-infrastructure-V2-CloudWatchLogs.md)
  + [User permissions](AWS-logs-infrastructure-V2-CloudWatchLogs.md#AWS-logs-infrastructure-V2-CloudWatchLogs-user-permissions)
  + [Log group resource policy](AWS-logs-infrastructure-V2-CloudWatchLogs.md#AWS-logs-infrastructure-V2-CloudWatchLogs-log-group-resource-policy)
+ [Logs sent to Amazon S3](AWS-logs-infrastructure-V2-S3.md)
  + [User permissions](AWS-logs-infrastructure-V2-S3.md#AWS-logs-infrastructure-V2-S3-user-permissions)
  + [Amazon S3 bucket resource policy](AWS-logs-infrastructure-V2-S3.md#AWS-logs-infrastructure-V2-S3-bucket-resource-policy)
  + [Amazon S3](AWS-logs-infrastructure-V2-S3.md#AWS-logs-SSE-KMS-S3-V2)
  + [Amazon S3 object key format](AWS-logs-infrastructure-V2-S3.md#AWS-logs-infrastructure-V2-S3-object-key)
+ [Logs sent to Firehose](AWS-logs-infrastructure-V2-Firehose.md)
  + [User permissions](AWS-logs-infrastructure-V2-Firehose.md#AWS-logs-infrastructure-V2-Firehose-user-permissions)
  + [IAM roles used for resource permissions](AWS-logs-infrastructure-V2-Firehose.md#AWS-logs-infrastructure-V2-Firehose-resource-permissions)
+ [Traces sent to X-Ray](AWS-logs-infrastructure-V2-XRayTraces.md)
  + [User permissions](AWS-logs-infrastructure-V2-XRayTraces.md#AWS-logs-infrastructure-V2-XRayTraces-user-permissions)
  + [X-Ray resource policy](AWS-logs-infrastructure-V2-XRayTraces.md#AWS-logs-infrastructure-V2-XRayTraces-resource-policy)
  + [Enable transaction search](AWS-logs-infrastructure-V2-XRayTraces.md#AWS-logs-infrastructure-V2-XRayTraces-transaction-search)