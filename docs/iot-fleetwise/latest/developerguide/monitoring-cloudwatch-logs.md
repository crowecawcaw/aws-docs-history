# Monitor AWS IoT FleetWise with Amazon CloudWatch Logs

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

Amazon CloudWatch Logs monitors the events that occur in your resources and alerts you if there are any issues. If you receive an alert, you can access the log files to get information about the specific event. For more information, see the [Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs.md "../../../AmazonCloudWatch/latest/logs.md").

## View AWS IoT FleetWise logs in the CloudWatch console

###### Important

Before you can see the AWS IoT FleetWise log group in the CloudWatch console, make sure that the
following is true:

- You've enabled logging in AWS IoT FleetWise. For more information about logging, see [Configure AWS IoT FleetWise logging](logging-cw.md "logging-cw.md").
- There are already log entries written by AWS IoT operations.

###### To view your AWS IoT FleetWise logs in the CloudWatch console

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch").
2. On the navigation pane, choose **Logs**, **Log groups**.
3. Choose the log group.
4. Choose **Search log group**. You'll see a complete list of the log events generated for your account.
5. Choose the expand icon to look at an individual stream and find all logs that have a
   log level of `ERROR`.

You can also enter a query in the **Filter events** search box. For
example, you can try the following query:

`{ $.logLevel = "ERROR" }`

For more information about creating filter expressions, see [Filter and pattern syntax](../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md "../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md") in the
_Amazon CloudWatch Logs User Guide_.

###### Example log entry

```
{
  "accountId": "123456789012",
  "vehicleName": "test-vehicle",
  "message": "Unrecognized signal ID",
  "eventType": "MODELING_ERROR",
  "logLevel": "ERROR",
  "timestamp": 1685743214239,
  "campaignName": "test-campaign",
  "signalCatalogName": "test-catalog",
  "signalId": 10242
}
```

| Signal event types          | Event type                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| MODELING_ERROR              | A message sent from the vehicle and received by AWS IoT FleetWise contains signals that fail to<br>validate against the vehicle model.<br>Attributes: vehicleName, campaignName (optional), signalCatalogName, signalId (optional),<br>signalValue (optional), signalValueRangeMin (optional), signalValueRangeMax (optional),<br>modelManifestName (optional), signalIds, stateTemplateName |
| ILLEGAL_MESSAGE_FROM_EDGE   | A message sent from the vehicle and received by AWS IoT FleetWise didn't match the required format.<br>Attributes: vehicleName, campaignName, signalCatalogName                                                                                                                                                                                                                              |
| DECODING_ERROR              | A message sent from the vehicle and received by AWS IoT FleetWise contains signals that fail to decoder against the vehicle's decoder manifest.<br>Attributes: campaignName, signalCatalogName, decoderManifestName, (optional) signalName, (optional) s3URI                                                                                                                                 |
| MESSAGE_THROTTLED           | A message sent from the vehicle to AWS IoT FleetWise was throttled. This is because you exceeded the service limits for this account in the current Region.<br>Attributes: accountId, vehicleName, message, eventType, logLevel, timestamp                                                                                                                                                   |
| MESSAGE_SIZE_LIMIT_EXCEEDED | A message sent from the vehicle and received by AWS IoT FleetWise exceeds the maximum size of a message [service limit](../../../general/latest/gr/iotfleetwise.md "../../../general/latest/gr/iotfleetwise.md").<br>Attributes: accountId, vehicleName                                                                                                                                      |
| CHECKIN_THROTTLED           | A check-in sent from the vehicle to AWS IoT FleetWise was throttled. This is because you exceeded the [service limit](../../../general/latest/gr/iotfleetwise.md "../../../general/latest/gr/iotfleetwise.md") for this account in the current Region.<br>Attributes: vehicleName                                                                                                            |

| Vehicle event types | Event type                                                                                                                                                | Description |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| VEHICLE_NOT_FOUND   | A message received by AWS IoT FleetWise, where the vehicle was unknown.<br>Attributes: vehicleName, campaignName (optional), stateTemplateName (optional) |

| Deployment event types      | Event type                                                                                                                                                                         | Description |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| PAYLOAD_SIZE_LIMIT_EXCEEDED | A message sent from AWS IoT FleetWise to the vehicle exceeded the maximum size service<br>limit.<br>Attributes: vehicleName, campaignName (optional), stateTemplateName (optional) |

| Campaign event types | Event type                                                                                                                                               | Description |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| CAMPAIGN_NOT_FOUND   | A message sent from the vehicle and received by AWS IoT FleetWise, where the campaign was unknown.<br>Attributes: vehicleName (optional), campaignName   |
| CAMPAIGN_INVALID     | A message sent from the vehicle and received by AWS IoT FleetWise, where the campaign was not valid.<br>Attributes: vehicleName (optional), campaignName |

| Campaign data destination event types | Event type                                                                                                                                                                        | Description |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| TIMESTREAM_WRITE_ERROR                | AWS IoT FleetWise couldn't write a message from the vehicle to the Amazon Timestream table.<br>Attributes: vehicleName, campaignName, timestreamDatabaseName, timestreamTableName |
| S3_WRITE_ERROR                        | AWS IoT FleetWise couldn't write a message from the vehicle to the Amazon Simple Storage Service (Amazon S3) bucket.<br>Attributes: campaignName, destinationName                 |
| S3_READ_ERROR                         | AWS IoT FleetWise couldn't read an object key from the vehicle in the Amazon Simple Storage Service (Amazon S3) bucket.<br>Attributes: campaignName, destinationName              |

| State template event types | Event type                                                                                                                                                        | Description |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| STATE_TEMPLATE_NOT_FOUND   | A message sent from the vehicle and received by AWS IoT FleetWise, where the state template was unknown.<br>Attributes: vehicleName (optional), stateTemplateName |

| Customer managed AWS KMS key event types | Event type                                                                                                                                                                                                            | Description |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| KMS_KEY_ACCESS_DENIED                    | AWS IoT FleetWise couldn't write a message from the vehicle to the Timestream table or the Amazon S3 bucket because of an AWS KMS key access denied error.<br>Attributes: kmsKeyId (optional), resourceArn (optional) |

### Attributes

All CloudWatch Logs entries include these attributes:

**accountId**

Your AWS account ID.

**eventType**

The event type for which the log was generated. The value of the event type depends
on the event that generated the log entry. Each log entry description includes the
value of `eventType` for that log entry.

**logLevel**

The log level that is being used. For more information, see [Log levels](../../../iot/latest/developerguide/configure-logging.md#log-level "../../../iot/latest/developerguide/configure-logging.md#log-level")
in the _AWS IoT Core Developer Guide_.

**message**

Contains specific details about the log.

**timestamp**

The epoch millisecond timestamp of when AWS IoT FleetWise processed the log.

### Optional attributes

CloudWatch Logs entries optionally include these attributes, depending on the
`eventType`:

**decoderManifestName**

The name of the decoder manifest that contains the signal.

**destinationName**

The name of the destination for vehicle data. For example, the Amazon S3 bucket name.

**campaignName**

The name of the campaign.

**signalCatalogName**

The name of the signal catalog that contains the signal.

**signalId**

The ID of the error signal.

**signalIds**

A list of error signal IDs.

**signalName**

The name of the signal.

**signalTimestampEpochMs**

The timestamp of the error signal.

**signalValue**

The value of the error signal.

**signalValueRangeMax**

The maximum range of the error signal.

**signalValueRangeMin**

The minimum range of the error signal.

**s3URI**

The Amazon S3 unique identifier of an Amazon Ion file from a vehicle message.

**timestreamDatabaseName**

The name of the Timestream database.

**timestreamTableName**

The name of the Timestream table.

**vehicleName**

The name of the vehicle.
