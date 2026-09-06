

# Logging RTB Fabric link activity using vended logs
<a name="monitoring-cloudwatch-logs"></a>

AWS RTB Fabric publishes application logs as vended logs, an AWS-managed log-delivery pipeline. You can route the logs to:
+ *Amazon S3*, for high-volume log retention and downstream analytics.
+ *Amazon CloudWatch Logs*, for live querying with CloudWatch Logs Insights and CloudWatch alarms.
+ *Amazon Data Firehose*, for streaming logs to downstream systems.

Choose the destination that fits your workload's retention, query, and cost requirements.

For more information about vended logs, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*. For pricing, see the *Vended Logs* section on the [CloudWatch pricing page](https://aws.amazon.com/cloudwatch/pricing/).

**Prerequisites**  
Vended-log records appear only when an active link is processing traffic. Before configuring delivery, set up a link and verify that requests reach it. For instructions, see [Testing and using links](testing-and-using-links.md).

The following topics describe how to set up vended-log delivery, grant the required permissions, and control log volume with sampling.

**Topics**
+ [Configure log delivery for RTB Fabric](#monitoring-logs-delivery-setup)
+ [Required permissions for log delivery](#monitoring-logs-permissions)
+ [Configure log sampling rates](#monitoring-logs-sampling)

## Configure log delivery for RTB Fabric
<a name="monitoring-logs-delivery-setup"></a>

To enable logging for RTB Fabric, you need to create a log delivery source, destination, and delivery configuration. Only links can be registered as log sources, and only APPLICATION\_LOGS log type is supported.

**To set up log delivery for RTB Fabric**

1. Register the link as a delivery source. The resource ARN must specify a link within a gateway.

   ```
   $ aws logs put-delivery-source \
     --name rtbfabric-delivery-source \
     --resource-arn arn:aws:rtbfabric:us-east-1:{{111122223333}}:gateway/{{rtb-gw-EXAMPLE1}}/link/{{link-EXAMPLE1}} \
     --log-type APPLICATION_LOGS
   ```

1. Create a delivery destination. The example below uses a CloudWatch Logs log group; you can also use an Amazon S3 bucket or an Amazon Data Firehose stream.

   ```
   $ aws logs put-delivery-destination \
     --name rtbfabric-delivery-destination \
     --delivery-destination-configuration "destinationResourceArn=arn:aws:logs:us-east-1:{{111122223333}}:log-group:{{/aws/vendedlogs/rtbfabric}}"
   ```

1. Create the delivery that ties the source to the destination.

   ```
   $ aws logs create-delivery \
     --delivery-source-name rtbfabric-delivery-source \
     --delivery-destination-arn arn:aws:logs:us-east-1:{{111122223333}}:delivery-destination:rtbfabric-delivery-destination
   ```

For destination-specific setup, including Amazon S3 and Amazon Data Firehose targets, and for the underlying log-delivery model, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

After the delivery is created, CloudWatch Logs writes a single record to a stream named `log_stream_created_by_aws_to_validate_log_delivery_subscriptions` on the destination log group. This stream confirms that the delivery wiring, IAM permissions, and resource policy are valid. It does not confirm that RTB Fabric is emitting application records; for that, send traffic to the link and watch for additional streams to appear.

## Required permissions for log delivery
<a name="monitoring-logs-permissions"></a>

To set up log delivery for RTB Fabric, you need the following IAM permissions:

```
{
   "Sid": "AllowLogDeliveryCreation",
   "Effect": "Allow",
   "Action": [
       "logs:PutDeliverySource",
       "logs:PutDeliveryDestination",
       "logs:CreateDelivery"
   ],
   "Resource": "*"
}
```

Additionally, you need service-level permissions for the specific link resource:

```
{
   "Sid": "ServiceLevelAccessForLogDelivery",
   "Effect": "Allow",
   "Action": [
       "rtbfabric:AllowVendedLogDeliveryForResource"
   ],
   "Resource": "arn:aws:rtbfabric:us-east-1:{{111122223333}}:gateway/{{rtb-gw-EXAMPLE1}}/link/{{link-EXAMPLE1}}"
}
```

You can harden the resource permissions by specifying exact ARNs instead of using wildcards, and add additional actions like delete operations as needed.

When you call `create-delivery` against a CloudWatch Logs log group, CloudWatch Logs attaches a resource policy to that log group automatically. The policy grants `delivery.logs.amazonaws.com` permission to write log events, scoped by a `SourceArn` condition that lists the link ARN. You do not need to author this policy. If you create a resource policy with the same name on the destination log group beforehand, the auto-managed policy can fail to attach. Let the service manage it.

## Configure log sampling rates
<a name="monitoring-logs-sampling"></a>

You can configure log sampling rates when creating or accepting links to control the volume of logs generated. This helps manage costs and focus on the most relevant log data.

Example of setting log sampling rates when accepting a link:

```
$ aws rtbfabric accept-link \
  --link-id {{link-EXAMPLE1}} \
  --gateway-id {{rtb-gw-EXAMPLE1}} \
  --log-settings '{
      "applicationLogs": {
          "sampling": {
              "errorLog": 100.0,
              "filterLog": 100.0
          }
      }
  }'
```

The sampling rates are specified as percentages (0.0 to 100.0) where:
+ `errorLog` – Percentage of error logs to capture
+ `filterLog` – Percentage of filter logs to capture

You can also configure sampling rates when creating links using the `CreateLink` operation with similar log-settings parameters.