# Manage AWS IoT SiteWise Edge destinations

After adding destinations, you can perform various operations to manage them, such as
editing destination configurations, deleting destinations, and managing path filters.

## Edit a destination

Select the radio button next to the destination in the table and choose the
**Edit** button to edit a destination.

Console

###### To edit a destination using the AWS IoT SiteWise console

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Select the appropriate gateway.
4. In the **Destinations** section, choose destination you want
   to edit and then choose **Edit**.
5. Modify the destination and then choose **Save**.

AWS CLI

###### To edit a destination using AWS CLI

- You can edit a destination by modifying the JSON capability configuration
  information.

```
aws iotsitewise update-gateway-capability-configuration \
--gateway-id `your-gateway-id` \
--capability-namespace "iotsitewise:publisher:3" \
--capability-configuration '{
    "sources": [
        {
            "type": "MQTT"
        }
    ],
    "destinations": [
        {
            "id": "your-existing-destination-id",
            "type": "SITEWISE_REALTIME",
            "name": "`your-updated-destination-name`",
            "config": {
                "publishingOrder": "`TIME_ORDER`",
                "enableCompression": `true`,
                "dropPolicy": {
                    "cutoffAge": "`10d`",
                    "exportPolicy": {
                        "retentionPeriod": "`10d`",
                        "rotationPeriod": "`6h`",
                        "exportSizeLimitGB": `10`
                    }
                },
                "maxBatchWaitTime": "`15s`"
            },
            "filters": [
                {
                  ...
                }
            ]
        }
    ]
}'
```

###### Note

You can't update the destination `type` or
`capability-namespace`. For example, you can't switch from a type of
`SITEWISE_REALTIME` to `SITEWISE_BUFFERED`. You can have one
real-time destination for each MQTT-enabled gateway.

## Delete a destination

If you no longer need a destination, you can delete it from your SiteWise Edge gateway.

Console

###### To delete a destination using the AWS IoT SiteWise console

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Select the appropriate gateway.
4. In the **Destinations** section, choose destination you want
   to delete and then choose **Delete**. A confirmation screen
   appears.
5. To confirm your choice to delete the destination, type "delete" in the
   confirmation box.

AWS CLI

###### To delete a destination using AWS CLI

- Delete the gateway capability configuration by specifying the gateway ID and modifying the capability configuration to remove the destination you want to delete.

```
aws iotsitewise update-gateway-capability-configuration \
  --gateway-id `your-gateway-id` \
  --capability-namespace "iotsitewise:publisher:3" \
  --capability-configuration '{
    "sources": [
        {
            "type": "MQTT"
        }
    ],
    "destinations": []
}'
```

###### Note

The destinations array can be empty (`[]`), but the destinations object itself must be included in the capability configuration.

## Download all path filters in a

destination (console)

Download a CSV file containing all of your path filters in the AWS IoT SiteWise console. You can use
a downloaded list of path filters to easily share path filter lists between gateway
destinations.

###### To download a CSV file of all path filters using the AWS IoT SiteWise console

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Select the gateway containing your path filters.
4. Choose either **Add destination** or **Edit
   destination**.
5. Navigate to the **Path filters** section and choose
   **Download CSV**.

###### Note

The CSV file includes all path filters in a particular destination, regardless
of which ones you selected from the list of path filters.

## Edit a path filter

You can edit individual path filters to refine which data your destination
receives.

Console
Using the AWS IoT SiteWise console, you can edit each individual path filter within each
respective text box.

###### To edit a path filter using the AWS IoT SiteWise console

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Select the gateway containing your path filters.
4. Select the appropriate destination.
5. Choose **Edit**.
6. Choose the text box for the row containing the path filter that you want to
   edit.
7. Update the path filter's text, ensuring that the edited path filter's checkbox
   is selected.
8. Choose **Save**.

AWS CLI
To edit path filters for a destination using the AWS CLI, first retrieve the current
configuration, modify it, and then update it using the
`update-gateway-capability-configuration` command.

###### To edit a path filter using AWS CLI

1. Retrieve the current capability configuration:

```
aws iotsitewise describe-gateway-capability-configuration \
  --gateway-id `your-gateway-id` \
  --capability-namespace "iotsitewise:publisher:3" \
  --query "capabilityConfiguration"
```

2. Edit the JSON to modify the path filters as needed.
3. Update the capability configuration with the modified path filters:

```
aws iotsitewise update-gateway-capability-configuration \
  --gateway-id `your-gateway-id` \
  --capability-namespace "iotsitewise:publisher:3" \
  --capability-configuration `json-containing-your-updated-path-filters`
```

## Delete a path filter

You can delete path filters for a destination to control the data it receives from MQTT
sources and data processing pipelines.

Console

###### To delete a path filter using the AWS IoT SiteWise console

1. Open the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/ "https://console.aws.amazon.com/iotsitewise/").
2. In the left navigation, choose **Edge gateways** in the **Edge** section.
3. Select the gateway containing your path filters.
4. Select the appropriate destination.
5. Choose **Edit**.
6. On the **Edit destination** screen, in the **Path
   filters** section, select one or more the path filters to
   delete.
7. Choose **Delete**. A deletion confirmation message appears.
   If want to proceed with deleting the path filters, choose
   **Delete** on the confirmation screen.

AWS CLI

###### To delete a destination using AWS CLI

- Delete a path filter by removing it from the capability configuration.

```
aws iotsitewise update-gateway-capability-configuration \
  --gateway-id `your-gateway-id` \
  --capability-namespace "iotsitewise:publisher:3" \
  --capability-configuration '{
    "sources": [
        {
            "type": "MQTT"
        }
    ],
    "destinations": [
        {
            "id": "your-destination-id",
            "type": "SITEWISE_REALTIME",
            "name": "your-destination-name",
            "config": {
                ...
            },
            "filters": [
                {
                    "type": "PATH",
                    "config": {
                        "paths": [
                            "/path1",
                            "/path2",
                            "/`delete-a-path-to-remove-it`"
                        ]
                    }
                }
            ]
        }
    ]
}
```

###### Note

The filters array can be empty (`[]`), but the filters object itself must be included in the capability configuration.
