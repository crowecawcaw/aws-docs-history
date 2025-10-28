# Diagnostic trouble code use cases

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The following use cases assume the `DTC_QUERY` function was defined in the [demo script](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/edge-agent-uds-dtc-dev-guide.md").

## Periodic fetch

Fetch a DTC collection at configured intervals.

The following example is a campaign with periodic signal fetching of `Vehicle.DTC_INFO` for all DTCs with a status mask for all ECUs. There is a condition for data collected for `Vehicle.DTC_INFO`.

```
{
  "compression": "SNAPPY",
  "spoolingMode": "TO_DISK",
  "signalsToFetch": [
    {
      "fullyQualifiedName": "Vehicle.ECU1.DTC_INFO",
      "signalFetchConfig": {
        "timeBased": {
        // The FleetWise Edge Agent will query the UDS module for all DTCs every five seconds.
          "executionFrequencyMs": 5000
        }
      },
      "actions": [
      // Every five seconds, this action is called and its output is stored in the
      // signal history buffer of Vehicle.DTC_INFO
        "custom_function(\"DTC_QUERY\", -1, 2, -1)"
      ]
    }
  ],
  "signalsToCollect": [
    {
      "name": "Vehicle.ECU1.DTC_INFO"
    }
  ],
  "collectionScheme": {
    "conditionBasedCollectionScheme": {
      "conditionLanguageVersion": 1,
      // Whenever a new DTC is filled into the signal, the data is ingested.
      "expression": "!isNull($variable.`Vehicle.ECU1.DTC_INFO`)",
      "minimumTriggerIntervalMs": 1000,
      // Make sure that data is ingested only when there are new DTCs.
      "triggerMode": "RISING_EDGE"
    }
  },
  "dataDestinationConfigs": [
    {
      "s3Config":
        {
          "bucketArn": "bucket-arn",
          "dataFormat": "PARQUET",
          "prefix": "campaign-name",
          "storageCompressionFormat": "GZIP"
        }
    }
  ]
}
```

## Condition-driven fetch

Fetch a DTC collection when a condition is met. For example, when the CAN signal is `Vehicle.Ignition == 1`, fetch and upload the DTC data.

The following example campaign has condition-driven signal fetching of `Vehicle.ECU1.DTC_INFO` to check whether the DTC ("AAA123") is pending with recordNumber 1 for ECU-1. This campaign has time-based data collection and upload.

```
{
  "compression": "SNAPPY",
  "spoolingMode": "TO_DISK",
  "signalsToFetch": [
    {
      "fullyQualifiedName": "Vehicle.ECU1.DTC_INFO",
      "signalFetchConfig": {
        "conditionBased": {
        // The action will only run when the ignition is on.
          "conditionExpression": "$variable.`Vehicle.Ignition` == 1",
          "triggerMode": "ALWAYS"
        }
      },
      // The UDS module is only requested for the specific ECU address and the specific DTC Number/Status.
      "actions": ["custom_function(\"DTC_QUERY\", 1, 2, 8, \"0xAAA123\")"]
    }
  ],
  "signalsToCollect": [
    {
      "name": "Vehicle.ECU1.DTC_INFO"
    },
    {
      "name": "Vehicle.Ignition"
    }
  ],
  "collectionScheme": {
    "timeBasedCollectionScheme": {
      "periodMs": 10000
    }
  },
  "dataDestinationConfigs": [
    {
      "s3Config":
        {
          "bucketArn": "bucket-arn",
          "dataFormat": "PARQUET",
          "prefix": "campaign-name",
          "storageCompressionFormat": "GZIP"
        }
    }
  ]
}
```

## On-demand fetch

Fetch a specific DTC for a fleet.

For an on-demand use case, you can use the same campaign as defined in the periodic fetch. The on-demand effect is achieved by suspending the campaign shortly after the campaign is deployed using the AWS IoT FleetWise console or by running the following CLI command.

- Replace `command-name` with the command name.

```
aws iotfleetwise update-campaign \
    --name `campaign-name` \
    --action APPROVE
```

Then, suspend the campaign after the DTC data arrives.

```
aws iotfleetwise update-campaign \
    --name `campaign-name` \
    --action SUSPEND
```

You can resume the campaign again for DTC data fetching.

```
aws iotfleetwise update-campaign \
    --name `campaign-name` \
    --action RESUME
```
