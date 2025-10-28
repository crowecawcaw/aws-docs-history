# Create data partitions

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

A data partition in a campaign temporarily stores signal data. You configure when
and how to forward the data to the cloud.

A data partition works by first designating a particular set of data using the
`dataPartitionId` for a campaign. Then, you can further define
partition storage options such as maximum size, minimum time to keep the data
partition live (on disk), and where to store the data on the Edge. You can determine
the storage location on the vehicle using `storageLocation`. The storage location determines the folder name for the data partition under the campaign storage folder. The campaign storage folder is under a folder named after the vehicle name under a persistency path defined in the Edge config file. This is the absolute path of the storage location: `{persistency_path} / {vehicle_name} / {campaign_name} / {storage_location}`.

The spooling mode set to `TO_DISK` specifies that the partitioned
data should be saved to a disk on the vehicle. Data storage for data partitions
operates on a FIFO (first in, first out) basis. If you delete a campaign, you also delete the
data in the associated data partition. If you don't specify a data partition for
connectivity on/off use cases, AWS IoT FleetWise still stores data in a ring buffer on the
vehicle when there is no connectivity. When connectivity resumes, AWS IoT FleetWise uploads the
data to the cloud. This behavior is configurable in the Edge Agent for AWS IoT FleetWise software.

###### Important

If your data partition exceeds your set maximum storage limit, newer data overwrites
older data when the partition reaches the maximum size. Lost data on the Edge isn't
recoverable. Storage size is determined by your Edge storage limit.

When data is uploaded to the cloud, it can be removed after the minimum time to live passes. Set the minimum time to live appropriately to avoid unintended deletion.

Upload options determine variable expressions and condition language. If upload
options are specified, you must also specify storage options. You can also request
that signals in data partitions are uploaded into the cloud. For more information, see
[Upload campaign data](update-campaign-cli-data-partitions.md "update-campaign-cli-data-partitions.md").

After data partition conditions are defined, `signalsToCollect` helps
specify which signals to account for in the data partition. You can either specify
IDs for data partitions, or set the `dataPartitionId` to
`default` to use an established default data partition. A signal
without a specified `dataPartitionId` will be associated with the default
`dataPartition`.

###### To create a data partition

Using the following example, create a campaign with a data partition storage condition. This example campaign is configured to store vehicle data in Amazon Timestream.

1. Replace `campaign-name` with the name of the campaign that you're creating.
2. (Optional) Provide a description.
3. Replace `role-arn` with the Amazon Resource Name (ARN) of the task
   execution role that grants AWS IoT FleetWise permission to deliver data to the Timestream
   table.
4. Replace `table-arn` with the ARN of the Timestream
   table.
5. Replace `signal-catalog-arn` with the ARN of the signal catalog.
6. Replace `data-partition-id` both for the
   `dataPartitions` ID and as the ID to associate with
   `signalsToCollect`. First, replace the ID of the data
   partition to use in the signal. For `signalsToCollect`, the ID
   must match one of the IDs provided in
   `dataPartitions`.

###### Note

Establish a default data partition for a campaign by using
`default` as the ID. 7. Replace `target-arn` with the ARN of a fleet or
vehicle that you created.

```
{
    "name": "`campaign-name`",
    "description": "Measurement of SOC, SOH, thermal, and power optimization for Fleet 2704",
    "targetArn": "`target-arn`",
    "collectionScheme": {
        "conditionBasedCollectionScheme": {
            "conditionLanguageVersion": 1,
            "expression": "$variable.`Vehicle.BMS` > 50",
            "minimumTriggerIntervalMs": 1000,
            "triggerMode": "ALWAYS"
        }
    },
    "compression": "SNAPPY",
    "dataDestinationConfigs": [{
        "timestreamConfig": {
            "executionRoleArn": "`role-arn`",
            "timestreamTableArn": "`table-arn`"
        }
    }],
    "dataPartitions": [{
        "id": "`data-partition-id`",
        "storageOptions": {
            "maximumSize": {
                "unit": "GB",
                "value": 1024
            },
            "minimumTimeToLive": {
                "unit": "WEEKS",
                "value": 6
            },
            "storageLocation": "string"
        },
        "uploadOptions": {
            "conditionLanguageVersion": 1,
            "expression": "$variable.`Vehicle.BMS.PowerOptimization` > 90"
        }
    }],
    "signalCatalogArn": "`signal-catalog-arn`",
    "signalsToCollect": [{
        "dataPartitionId": "`data-partition-id`",
        "maxSampleCount": 50000,
        "minimumSamplingIntervalMs": 100,
        "name": "Below-90-percent"
    }],
    "spoolingMode": "TO_DISK",
    "tags": [{
        "Key": "BMS",
        "Value": "Under-90"
    }]
}

```

After meeting all specified conditions, the partitioned data forwards to the
cloud, enabling the collection and storage of new partitioned signals.

Next, you'll call the `UpdateCampaign` API to deploy it to the
Edge Agent for AWS IoT FleetWise software. For more information, see [Upload campaign data](update-campaign-cli-data-partitions.md "update-campaign-cli-data-partitions.md").
