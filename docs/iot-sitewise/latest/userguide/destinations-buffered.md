# Add an AWS IoT SiteWise buffered destination using Amazon S3

The buffered destination type allows you to save on ingestion costs into AWS IoT SiteWise if you
don't need the data in real-time. It enables you to temporarily store your IoT data in an Amazon S3
bucket before importing it into AWS IoT SiteWise. Or, you can simply upload your data to S3 for storage,
regardless of whether you plan to import it to AWS IoT SiteWise. This is useful for batching and
buffering data from your devices and gateways before ingesting it into AWS IoT SiteWise. With this
option, data is uploaded to the specified S3 bucket in Parquet format at a configured
frequency. You can then import this data into AWS IoT SiteWise storage for further analysis and
processing.

**To add a destination buffered using Amazon S3**

Use the AWS IoT SiteWise console or AWS CLI to add a destination that buffers data using Amazon S3 to your
SiteWise Edge gateway.

Console
Use the AWS Management Console to add an AWS IoT SiteWise destination buffered using Amazon S3.

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the navigation pane, choose **Edge gateways**.
3. Select the gateway to which you want to add a
   destination.
4. In the **Destinations** section, choose **Add
   destination**.
5. On the **Add destination** page, enter **Destination
   details**:
   1. A name for your destination in the **Destination name**
      field.
   2. Select **AWS IoT SiteWise buffered using Amazon S3** for
      **Destination type**. AWS IoT SiteWise buffered using Amazon S3 sends data
      to Amazon Simple Storage Service in batches, in Parquet format, and then imports the data into AWS IoT SiteWise
      storage.

6. Enter the Amazon S3 URL for the location where you want to store your gateway data.
   You can browse for the path by choosing **Browse S3**. Once a
   bucket is added, you can also view the bucket by choosing
   **View**.
7. Specify how often your gateway should upload data to Amazon S3 by entering a time
   frame and selecting a time increment for **Data upload frequency**.
   The frequency value should be greater than 0 and less than or equal to 30
   days.
8. In **Data storage settings**, determine what to do with your
   gateway data after importing it to AWS IoT SiteWise. There are two decisions to make regarding
   data storage:
   - If you want to copy imported data into AWS IoT SiteWise storage, select the **Copy data to storage** check box. This option duplicates
     the imported data from your configured Amazon S3 bucket into AWS IoT SiteWise storage.
   - If you choose to import your data from your Amazon S3 bucket into AWS IoT SiteWise storage,
     you can also specify whether the imported data should be deleted after the
     import is complete. Select the **Delete data from
     Amazon S3** check box to delete the imported date from the configured Amazon S3
     bucket after importing it to AWS IoT SiteWise storage.

9. Add path filters to your destination. For more information see, [Add path filters to AWS IoT SiteWise Edge
   destinations](destinations-add-path-filters.md "destinations-add-path-filters.md").

AWS CLI

###### Example: Create a new AWS IoT SiteWise destination buffered using Amazon S3

Use the [UpdateGatewayCapabilityConfiguration](../APIReference/API_UpdateGatewayCapabilityConfiguration.md "../APIReference/API_UpdateGatewayCapabilityConfiguration.md") API to configure the publisher.

Set the `capabilityNamespace` parameter to
`iotsitewise:publisher:3`.

```
{
    "sources": [
      {
        "type": "MQTT"
      }
    ],
    "destinations": [
      {
        "type": "SITEWISE_BUFFERED",
        "name": "`your-s3-destination-name`",
        "config": {
          "targetBucketArn": "arn:aws:s3:::amzn-s3-demo-bucket/`Optional`/`SomeFolder`",
          "publishPolicy": {
            "publishFrequency": "15m",
            "localSizeLimitGB": 10
          },
          "siteWiseImportPolicy": {
            "enableSiteWiseStorageImport": true,
            "enableDeleteAfterImport": true,
            "bulkImportJobRoleArn": "arn:aws:iam::`123456789012`:role/`your-role-name`"
          }
        },
        "filters": [
          {
            "type": "PATH",
            "config": {
              "paths": [
                "#"
              ]
            }
          }
        ]
      }
    ]
  }

```

###### Example: Update an AWS IoT SiteWise destination buffered using Amazon S3

To update an existing AWS IoT SiteWise real-time destination, first use the
`DescribeGatewayCapabilityConfiguration` API to find the
`destinationId`.

The publisher namespace: `iotsitewise:publisher:3`

```
{
    "sources": [
      {
        "type": "MQTT"
      }
    ],
    "destinations": [
      {
        "id": "`your-existing-destination-id`",
        "type": "SITEWISE_BUFFERED",
        "name": "`your-s3-destination-name`",
        "config": {
          "targetBucketArn": "arn:aws:s3:::amzn-s3-demo-bucket/`Optional`/`SomeFolder`",
          "publishPolicy": {
            "publishFrequency": "15m",
            "localSizeLimitGB": 10
          },
          "siteWiseImportPolicy": {
            "enableSiteWiseStorageImport": true,
            "enableDeleteAfterImport": true,
            "bulkImportJobRoleArn": "arn:aws:iam::`123456789012`:role/`your-role-name`"
          }
        },
        "filters": [
          {
            "type": "PATH",
            "config": {
              "paths": [
                "#"
              ]
            }
          }
        ]
      }
    ]
  }

```

The following configuration options are specific to MQTT-enabled gateways using the
`iotsitewise:publisher:3` namespace.

`sources`

Defines data sources to transfer of data from your industrial equipment to
AWS IoT SiteWise. For MQTT-enabled gateways, use `MQTT`.

Type: Array of objects

Required: Yes

`destinations`

Defines where to send data. Destinations are either real-time or buffered
using Amazon S3. At least one destination object is required, but you can add an empty
array. You can have one real-time destination for each gateway. For more
information, see [Understand AWS IoT SiteWise Edge destinations](gw-destinations.md#source-destination "gw-destinations.md#source-destination").

Type: Array of objects

Required: Yes

`id`

The unique identifier for the destination. You can either provide an
existing destination ID or leave it blank to have a new ID automatically
generated for the destination.

Type: String

Required: No

`type`

Type of destination. Options include: `SITEWISE_REALTIME` and
`SITEWISE_BUFFERED`. Choose
`SITEWISE_BUFFERED`.

- `SITEWISE_REALTIME` (default) – Send data directly
  to AWS IoT SiteWise storage in real-time. For more information, see [Add an AWS IoT SiteWise Edge real-time destination](destinations-real-time.md "destinations-real-time.md").
- `SITEWISE_BUFFERED` – Send data to Amazon S3 in batches
  in Parquet format, and then import into AWS IoT SiteWise storage.

Type: String

Required: Yes

`name`

A unique name for the destination.

Type: String

Required: Yes

`config`

Configuration specific to the destination type in JSON format. The
configuration varies between real-time and buffered destinations.

Type: Object

Required: Yes

`targetBucketArn`

The bucket ARN to publish to. Choose the same
AWS Region for both AWS IoT SiteWise and Amazon S3. If a prefix is chosen, it must
have between 1-255 characters.

###### Note

AWS IoT SiteWise, including the gateway, will have access to the entire
specified S3 bucket. We recommend using a dedicated bucket for
buffered data ingestion.

Type: String

Required: Yes

`publishPolicy`

Details of the publishing policy.

Type: Object

Required: Yes

`publishFrequency`

The frequency with which the SiteWise Edge gateway publishes to
the Amazon S3 bucket. Data upload frequency to Amazon S3 must be greater
than 0 minutes and less than or equal to 30 days. You can use
`m`, `h`, and `d` when you
specify a publishing frequency age. Note that `m`
represents minutes, `h` represents hours, and
`d` represents days. The default value is 15
minutes.

Type: String

Required: Yes

`localSizeLimitGB`

The maximum size of the files written to local disk in GB.
If this threshold is breached, the publisher publishes all
buffered data to its destination.

Type: Integer

Required: Yes

`siteWiseImportPolicy`

Details of the import policy for importing data to AWS IoT SiteWise.

Type: Object

Required: Yes

`enableSiteWiseStorageImport`

Set this to `true` to import data from an Amazon S3
bucket to AWS IoT SiteWise storage. It initially makes a copy of the data
in AWS IoT SiteWise. Then, if you set `enableDeleteAfterImport`
to true, the data in S3 deletes after copying to AWS IoT SiteWise. Pricing
implications apply. The default value is
`true`.

Type: Boolean

Required: Yes

`enableDeleteAfterImport`

Set this to `true` to delete the file in the Amazon S3
bucket after ingestion into the AWS IoT SiteWise storage. The default
value is `true`.

Type: Boolean

Required: Yes

`bulkImportJobRoleArn`

The ARN of the IAM role that AWS IoT SiteWise assumes to read buffered
data from Amazon S3 during data ingestion. This role is used when an
edge device calls on AWS IoT SiteWise APIs to initiate the bulk import
process.

###### Note

If `enableSiteWiseStorageImport` is set to
`true`, this parameter is required.

Type: String

Required: No

Add path filters for your destination. For more information, see [Add path filters to AWS IoT SiteWise Edge
destinations](destinations-add-path-filters.md "destinations-add-path-filters.md").
