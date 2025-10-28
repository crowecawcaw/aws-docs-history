# Configuring RTB Fabric logs with Amazon CloudWatch Logs

You can configure RTB Fabric to send application logs to Amazon CloudWatch Logs using log delivery. Logging is not enabled by default and requires setup.

###### Topics

- [Setting up log delivery for RTB Fabric](#monitoring-logs-delivery-setup "#monitoring-logs-delivery-setup")
- [Required permissions for log delivery](#monitoring-logs-permissions "#monitoring-logs-permissions")
- [Configuring log sampling rates](#monitoring-logs-sampling "#monitoring-logs-sampling")

## Setting up log delivery for RTB Fabric

To enable logging for RTB Fabric, you need to create a log delivery source, destination, and delivery configuration. Only links can be registered as log sources, and only APPLICATION_LOGS log type is supported.

###### To set up log delivery for RTB Fabric

1. Create a log delivery source for your link. The resource ARN must specify a link within a gateway:

```
aws logs put-delivery-source \
  --name rtbfabric-delivery \
  --resource-arn arn:aws:rtbfabric:us-east-1:545746263314:gateway/rtb-gw-m8x4n2p9q7r5s1t6u3v8w0y2z/link/link-a9b7c5d3e1f4g8h2i6j0k4l7m \
  --log-type APPLICATION_LOGS
```

2. Create a log delivery destination (such as an Amazon S3 bucket or CloudWatch log group).
3. Create the delivery configuration to connect the source and destination.

For detailed information about log delivery setup, see [Configure standard logging](../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging.md "../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging.md") in the _Amazon CloudFront Developer Guide_ for a similar implementation pattern.

## Required permissions for log delivery

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
    "Resource": "arn:aws:rtbfabric:us-east-1:545746263314:gateway/rtb-gw-m8x4n2p9q7r5s1t6u3v8w0y2z/link/link-a9b7c5d3e1f4g8h2i6j0k4l7m"
}
```

You can harden the resource permissions by specifying exact ARNs instead of using wildcards, and add additional actions like delete operations as needed.

## Configuring log sampling rates

You can configure log sampling rates when creating or accepting links to control the volume of logs generated. This helps manage costs and focus on the most relevant log data.

Example of setting log sampling rates when accepting a link:

```
aws rtbfabric accept-link \
    --link-id link-brhta7fllwkwlb3l7gbpofkn \
    --gateway-id rtb-gw-d43re9jdjmkw2r08e6psphe37 \
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

- `errorLog` – Percentage of error logs to capture
- `filterLog` – Percentage of filter logs to capture

You can also configure sampling rates when creating links using the `CreateLink` operation with similar log-settings parameters.
