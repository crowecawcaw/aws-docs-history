# Monitor interruptible Capacity Reservations with EventBridge and CloudTrail

Interruptible Capacity Reservations send EventBridge notifications and CloudTrail events to help you monitor and respond to capacity changes.

###### Topics

- [EventBridge notifications](#eventbridge-notifications "#eventbridge-notifications")
- [CloudTrail events](#cloudtrail-events "#cloudtrail-events")

## EventBridge notifications

You receive two types of EventBridge notifications. For information about how to set up EventBridge notifications, see [Creating Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

### Instance interruption warning

If you're running instances in an interruptible reservation, you receive this notification 2 minutes before your instances are terminated:

```
{
    "version": "0",
    "id": "`12345678-1234-1234-1234-123456789012`",
    "detail-type": "EC2 Interruptible Capacity Reservation Instance Interruption Warning",
    "source": "aws.ec2",
    "account": "[`instance owner Account ID`]",
    "time": "[`Current time in yyyy-mm-ddThh:mm:ssZ`]",
    "resources": "[`instance arn`]",
    "region": "[`region`]",
    "detail": {
        "instance-id": "[`instance-id`]",
        "instance-action": "`terminate`",
        "instance-termination-time": "`yyyy-mm-ddThh:mm:ssZ`",
        "azId": "[`availability-zone-id`]"
    }
}
```

### Reclamation completion

If you own the source reservation, you receive this notification when capacity reclamation finishes:

```
{
    "version": "0",
    "id": "`12345678-1234-1234-1234-123456789012`",
    "detail-type": "EC2 Capacity Reservation Interruptible Reclamation Complete",
    "source": "aws.ec2",
    "account": "[`source Capacity Reservation Owner Account ID`]",
    "time": "[`Current time in yyyy-mm-ddThh:mm:ssZ`]",
    "region": "`us-east-1`",
    "resources": ["`source_cr_arn`"],
    "detail": {
        "sourceCapacityReservationId": "string",
        "instanceType": "string",
        "availabilityZoneId": "string",
        "TotalInstanceCount": "`current total count in the source`",
        "ReclaimedInstanceCount": "`count of instances added to the source`",
        "targetInstanceCount": "`number`"
    }
}
```

## CloudTrail events

CloudTrail logs these events for interruptible Capacity Reservations:

- `InterruptibleCapacityReservationCreated` — When you create an interruptible allocation
- `InterruptibleCapacityReservationAllocationUpdated` — When you modify the allocation
- `InterruptibleCapacityReservationCancelled` — When you cancel the allocation
- `CapacityReservationModified` — When we modify the source reservation for allocation
- `InterruptibleCapacityReservationInstancesTerminated` — When we terminate instances during reclamation
