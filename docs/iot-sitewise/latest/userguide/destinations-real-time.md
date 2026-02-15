# Add an AWS IoT SiteWise Edge real-time destination

The real-time destination type enables you to stream IoT data directly from your devices
and gateways into AWS IoT SiteWise storage in real-time. This option is ideal for use cases that require
immediate ingestion and processing of data as it is generated, without the need for batching
or buffering. You can only have one real-time destination configured in each gateway, as it
streams data continuously to AWS IoT SiteWise.

###### Note

Duplicate TQVs may result in double charging.

**To add a real-time destination**

Use the AWS IoT SiteWise console or AWS CLI to add a real-time destination to your SiteWise Edge MQTT-enabled
gateway.

Console

1.  Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2.  In the navigation pane, choose **Edge gateways**.
3.  Select the gateway to which you want to add a
    destination.
4.  In the **Destinations** section, choose **Add
    destination**.
5.  On the **Add destination** page, enter **Destination
    details**:
    1. A name for your destination in the **Destination name**
       field.
    2. Select the **AWS IoT SiteWise real-time** for the
       **Destination type**.

6.  Configure the gateway publishing order by setting the **Publishing
    order** to either **Publish older data first** or
    **Publish newest data first**. By default, the gateway
    publishes the oldest data first.
7.  Use **Maximum batch wait time** to set a maximum time for the
    publisher to wait before sending a batch of data to AWS IoT SiteWise. This setting applies for
    each alias. The data is stored locally until either:

        * The set time has elapsed, or
        * 10 time-quality-value (TQV) entries are received for the alias

    Whichever condition is met first triggers the batch to be sent to the
    cloud.

8.  To compress uploaded data, select the **Activate compression when
    uploading data** check box. Letting the gateway compress your data prior
    to uploading it to the cloud reduces bandwidth usage.
9.  To filter out expired publisher data, select the **Exclude expired
    data** check box. This selection only sends active and current data to
    AWS IoT SiteWise.
10. In the **Cutoff period** field, enter the frequency at which
    data should be considered expired within your dataset. You can determine if the data
    is counted in terms of minutes or days. The minimum cutoff period is five minutes.
    The maximum cutoff period is seven days.
11. Optionally configure the **Local storage settings**:
    1. Set the **Retention period** frequency – The amount
       of time the gateway locally stores data that is older than the cutoff period.
       The minimum retention period is one minute.

    The maximum retention period is 30 days and greater than or equal to the
    rotation period. 2. Set the **Rotation period** – The time interval to
    specify when saving data that is older than the cutoff period for a single file.
    The gateway transfers one batch of data to the following local directory at the
    end of each rotation period:
    `/greengrass/v2/work/aws.iot.SiteWiseEdgePublisher/exports`.

    The retention must be greater than one minute and equal to the retention
    period. 3. Provide the **Storage capacity (GB)** value to set the
    maximum size of data stored locally in GB. If the data exceeds the determined
    maximum local storage size, the gateway starts deleting the oldest data first.
    The gateway continues to delete until the size of data stored locally is equal
    to or less than the quota.

    The storage capacity must be greater than or equal to one GB.

12. Add path filters to your destination. For more information see, [Add path filters to AWS IoT SiteWise Edge
    destinations](destinations-add-path-filters.md "destinations-add-path-filters.md").

For more information, see [Destination types](gw-destinations.md#destination-types "gw-destinations.md#destination-types").

AWS CLI

###### Example: Create a new AWS IoT SiteWise real-time destination

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
            "type": "SITEWISE_REALTIME",
            "name": "`your-destination-name`",
            "config": {
                "publishingOrder": "TIME_ORDER",
                "enableCompression": true,
                "maxBatchWaitTime": "10s"
            },
            "filters": [
                {
                    "type": "PATH",
                    "config": {
                        "paths": [
                            "`#`"
                        ]
                    }
                }
            ]
        }
    ]
}

```

To update an existing AWS IoT SiteWise real-time destination, first use the
`DescribeGatewayCapabilityConfiguration` API to find the
`destinationId`.

###### Example: Update an AWS IoT SiteWise real-time destination

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
            "id": "`your-existing-destination-id`",
            "type": "SITEWISE_REALTIME",
            "name": "`your-destination-name`",
            "config": {
                "publishingOrder": "TIME_ORDER",
                "enableCompression": true,
                "dropPolicy": {
                    "cutoffAge": "7d",
                    "exportPolicy": {
                        "retentionPeriod": "7d",
                        "rotationPeriod": "6h",
                        "exportSizeLimitGB": 10
                    }
                },
                "maxBatchWaitTime": "10s"
            },
            "filters": [
                {
                    "type": "PATH",
                    "config": {
                        "paths": [
                            "`#`"
                        ]
                    }
                }
            ]
        }
    ]
}
```

The following configuration options are specific to gateways using the
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
existing destination ID or leave it blank. If you do not specify an ID then
a UUID is generated by default.

Type: String

Required: No

`type`

Type of destination. Options include: `SITEWISE_REALTIME` and
`SITEWISE_BUFFERED`.

- `SITEWISE_REALTIME` – Send data directly to AWS IoT SiteWise
  storage in real-time.
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

publishingOrder

Determines the order in which data is published. Data publishes
based on its timestamp. Options include `TIME_ORDER` and
`RECENT_DATA`.

- `TIME_ORDER` (default) – Publishes older
  data first.
- `RECENT_DATA` – Publishes newest data
  first.

Type: String

Required: No

enableCompression

When set to `true`, enables data compression before
sending to AWS IoT SiteWise. Letting the gateway compress your data prior to
uploading it to the cloud reduces bandwidth usage. The default value
is `true`.

Type: Boolean

Required: No

dropPolicy

Defines how to handle older data.

Type: object

Required: No

- `cutoffAge`

The maximum age of data to be published specified in days, hours, and minutes. For example, `7d` or `1d7h16m`. Data
older than what you specify is not sent to AWS IoT SiteWise.

Data that is earlier than the cutoff period is not published to the cloud. The cutoff age must be between five minutes and seven days.

You can use `m`, `h`, and `d` when you specify a cutoff age. Note that `m` represents minutes,
`h` represents hours, and `d` represents days.

Type: String

Required: Yes

- `exportPolicy`

Defines how to handle data that exceeds the cutoff age.

Type: Object

Required: No

    + `retentionPeriod`


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


    Type: String


    Required: No
    + `rotationPeriod`


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


    Type: String


    Required: No
    + `exportSizeLimitGB`


    The maximum allowed size of data stored
     locally, in GB. If this quota is breached, the
     SiteWise Edge gateway starts deleting the earliest data
     until the size of data stored locally is equal to
     or less than the quota. The value of this
     parameter must be greater than or equal to
     1.


    Type: Integer


    Required: No

`maxBatchWaitTime`

Sets a maximum time for the publisher to wait before sending a
batch of data to AWS IoT SiteWise. This setting applies for each alias. The data
is stored locally until either:

- The set time has elapsed, or
- 10 time-quality-value (TQV) entries are received for the
  alias

Use `m`, `h`, and `d` to specify
a cutoff time. Note that `m` represents minutes,
`h` represents hours, and `d` represents
days.

Type: String

Required: No

`filters`

Filters to apply to the data. At least one filter is required.

Type: String

Required: Yes

`type`

Type of filter. Use `PATH`.

Type: String

Required: Yes

`config`

Configuration specific to the filter type in JSON format. At least one
object is required, but the array can be empty.

Type: Object

Required: Yes

- `paths`

An array of path filters. For more information, see [Understand path filters for AWS IoT SiteWise Edge
destinations](gw-destinations.md#destinations-path-filters "gw-destinations.md#destinations-path-filters"). The default path is
`#`.

Type: Array of strings

Required: Yes
