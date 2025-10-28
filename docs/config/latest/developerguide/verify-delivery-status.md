# Verifying Delivery Status

Enter the [`describe-delivery-channel-status`](../../../cli/latest/reference/configservice/describe-delivery-channel-status.md "../../../cli/latest/reference/configservice/describe-delivery-channel-status.md") command to verify that
the AWS Config has started delivering the configurations to the specified delivery
channel:

```
**aws configservice describe-delivery-channel-status**
```

The response lists the status of all the three delivery formats that AWS Config uses to
deliver configurations to your bucket and topic.

```
{
    "DeliveryChannelsStatus": [
        {
            "configStreamDeliveryInfo": {
                "lastStatusChangeTime": 1415138614.125,
                "lastStatus": "SUCCESS"
            },
            "configHistoryDeliveryInfo": {
                "lastSuccessfulTime": 1415148744.267,
                "lastStatus": "SUCCESS",
                "lastAttemptTime": 1415148744.267
            },
            "configSnapshotDeliveryInfo": {
                "lastSuccessfulTime": 1415333113.4159999,
                "lastStatus": "SUCCESS",
                "lastAttemptTime": 1415333113.4159999
            },
            "name": "default"
        }
    ]
}
```

View the `lastSuccessfulTime` field in
`configSnapshotDeliveryInfo`. The time should match the time you last
requested the delivery of the configuration snapshot.

###### Note

AWS Config uses the UTC format (Coordinated Universal Time) to record the time.
