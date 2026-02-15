# Configure the AWS IoT SiteWise publisher

component

After you create an AWS IoT SiteWise Edge gateway and install the software, you can set up
the publisher component so your SiteWise Edge gateway can export data to the AWS Cloud.
Use the publisher component to enable additional features or configure default
settings. For more information, see [AWS IoT SiteWise publisher](../../../greengrass/v2/developerguide/iotsitewise-publisher-component.md "../../../greengrass/v2/developerguide/iotsitewise-publisher-component.md")
in the _AWS IoT Greengrass Version 2 Developer Guide_.

###### Note

The publisher configuration differs based on the type of gateway you're using.
For Classic stream, V2 gateways, use the `iotsitewise:publisher:2`
namespace. For MQTT-enabled, V3 gateways, use the `iotsitewise:publisher:3`
namespace.

Console

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge
   gateways**.
3. Select the SiteWise Edge gateway for which you want to configure the
   publisher.
4. In the **Publisher configuration** section,
   choose **Edit**
5. For **Publishing order**, choose one of the
   following:
   - **Publish oldest data first**
     – The SiteWise Edge gateway publishes the oldest data
     to the cloud first by default.
   - **Publish newest data first**
     – The SiteWise Edge gateway publishes the newest data
     to the cloud first.

6. (Optional) If you don't want the SiteWise Edge gateway to compress
   your data, unselect **Activate compression when
   uploading data**.
7. (Optional) If you don't want to publish old data, choose
   **Exclude expired data** and do the
   following:
   1. For **Cutoff period**, enter a value
      and choose a unit. The cutoff period must be between
      five minutes and seven days. For example, if the cutoff
      period is three days, data that's older than three days
      isn't published to the cloud.

8. (Optional) To set custom settings about how data is handled on
   your local device, choose **Local storage
   settings** and do the following:
   1. For **Retention period**, enter a
      number and choose a unit. The retention period must be
      between one minute and 30 days, and greater than or
      equal to the rotation period. For example, if the
      retention period is 14 days, the SiteWise Edge gateway deletes
      any data at the edge that's older than the specified
      cutoff period after it's stored for 14 days.
   2. For **Rotation period**, enter a
      number and choose a unit. The rotation period must be
      greater than one minute, and equal to, or less than, the
      retention period. For example, say the rotation period
      is two days, the SiteWise Edge gateway batches up and saves
      data that is older than the cutoff period to a single
      file. For self-hosted gateways through AWS IoT Greengrass V2, the
      SiteWise Edge gateway transfers a batch of data to the
      following local directory once every two days:
      `/greengrass/v2/work/aws.iot.SiteWiseEdgePublisher/exports`.
   3. For **Storage capacity**, enter a
      value that is greater than or equal to 1. If the storage
      capacity is 2 GB, the SiteWise Edge gateway starts deleting
      data when more than 2 GB of data is stored locally.

9. Choose **Save**.

AWS CLI
Use the [UpdateGatewayCapabilityConfiguration](../APIReference/API_UpdateGatewayCapabilityConfiguration.md "../APIReference/API_UpdateGatewayCapabilityConfiguration.md") API to configure the
publisher.

Set the `capabilityNamespace` parameter to
`iotsitewise:publisher:2`.

###### Example: Publisher configuration for Classic Stream, V2 gateways

The publisher namespace:
`iotsitewise:publisher:2`

```
{
    "SiteWisePublisherConfiguration": {
        "publishingOrder": "TIME_ORDER",
        "enableCompression": true,
        "dropPolicy": {
            "cutoffAge": "7d",
            "exportPolicy": {
                "retentionPeriod": "7d",
                "rotationPeriod": "6h",
                "exportSizeLimitGB": 10
            }
        }
    },
    "SiteWiseS3PublisherConfiguration": {
        "accessRoleArn": "arn:aws:iam:123456789012:role/roleName",
        "streamToS3ConfigMapping": [
            {
                "streamName": "S3_OPC-UA_Data_Collector",
                "targetBucketArn": "arn:aws:s3:::amzn-s3-demo-bucket/dataCollector",
                "publishPolicy": {
                    "publishFrequency": "10m",
                    "localSizeLimitGB": 10
                },
                "siteWiseImportPolicy": {
                    "enableSiteWiseStorageImport": true,
                    "enableDeleteAfterImport": true
                }
            }
        ]
    }
}
```

The publisher provides the following configuration parameters that you
can customize:

`SiteWisePublisherConfiguration`

`publishingOrder`

The order in which data is published to the
cloud. The value of this parameter can be one of
the following:

- `TIME_ORDER` (**Publish
  oldest data first**) – The
  earliest data is published to the cloud first, by
  default.
- `RECENT_DATA` (**Publish
  newest data first**) – The newest
  data is published to the cloud first.

`enableCompression`

Set this to `true` to compress data
before publishing. Data compression can reduce
bandwidth usage.

`dropPolicy`

(Optional) A policy that controls what data is
published to the cloud.

`cutoffAge`
The maximum age of data to be published specified in days, hours, and minutes. For example, `7d` or `1d7h16m`. Data
older than what you specify is not sent to AWS IoT SiteWise.

Data that is earlier than the cutoff period is not published to the cloud. The cutoff age must be between five minutes and seven days.

You can use `m`, `h`, and `d` when you specify a cutoff age. Note that `m` represents minutes,
`h` represents hours, and `d` represents days.

`exportPolicy`

(Optional) A policy that manages data
storage at the edge. This policy applies to data
that is earlier than the cutoff age.

`retentionPeriod`
Your SiteWise Edge gateway deletes any data at the
edge that is earlier than the cutoff period from
the local storage after it is stored for the
specified retention period. The retention period
must be between one minute and 30 days, and
greater than or equal to the rotation
period.

You can use `m`, `h`,
and `d` when you specify a retention
period. Note that `m` represents
minutes, `h` represents hours, and
`d` represents days.

`rotationPeriod`
The time interval over which to batch up and
save data that is earlier than the cutoff period
to a single file. The SiteWise Edge gateway transfers
one batch of data to the following local directory
at the end of each rotation period:
`/greengrass/v2/work/aws.iot.SiteWiseEdgePublisher/exports`.
The rotation period must be greater than one
minute, and equal to or less than the retention
period.

You can use `m`, `h`,
and `d` when you specify a rotation
period. Note that `m` represents
minutes, `h` represents hours, and
`d` represents days.

`exportSizeLimitGB`
The maximum allowed size of data stored
locally, in GB. If this quota is breached, the
SiteWise Edge gateway starts deleting the earliest data
until the size of data stored locally is equal to
or less than the quota. The value of this
parameter must be greater than or equal to

1.

`SiteWiseS3PublisherConfiguration`

`accessRoleArn`

The access role that gives AWS IoT SiteWise permission
to manage the Amazon S3 bucket that you are publishing
to.

`streamToS3ConfigMapping`

An array of configurations that maps a stream
to an Amazon S3 configuration.

`streamName`

The stream to read from and publish to the
Amazon S3 configuration.

`targetBucketArn`

The bucket ARN to publish
to.

`publishPolicy`

`publishFrequency`

The frequency with which the SiteWise Edge gateway
publishes to the Amazon S3 bucket.

`localSizeLimitGB`

The maximum size of the files written to
local disk. If this threshold is breached, the
publisher publishes all buffered data to its
destination.

`siteWiseImportPolicy`

`enableSiteWiseStorageImport`

Set this to `true` to import data
from an Amazon S3 bucket to AWS IoT SiteWise storage.

`enableDeleteAfterImport`

Set this to `true` to delete the
file in the Amazon S3 bucket after ingestion into the
AWS IoT SiteWise storage.
