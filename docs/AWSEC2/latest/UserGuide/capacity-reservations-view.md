# View the state of a Capacity Reservation

Amazon EC2 constantly monitors the state of your Capacity Reservations.

Due to the [eventual consistency](../../../ec2/latest/devguide/eventual-consistency.md "../../../ec2/latest/devguide/eventual-consistency.md") model followed by the Amazon EC2 API, after you create a Capacity Reservation,
it can take up to 5 minutes for the state of the Capacity Reservation to reflect that it is `active`.
During this time, the Capacity Reservation might remain in the `pending` state. However, it
might already be available for use, in which case attempts to launch instances into the Capacity Reservation
would succeed.

Console

###### To view your Capacity Reservations

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Reservations**.
3. Select the Capacity Reservation.

AWS CLI

###### To describe your Capacity Reservations

Use the [describe-capacity-reservations](../../../cli/latest/reference/ec2/describe-capacity-reservations.md "../../../cli/latest/reference/ec2/describe-capacity-reservations.md") command.

For example, the following command describes all Capacity Reservations.

```
aws ec2 describe-capacity-reservations
```

The following is example output.

```
{
    "CapacityReservations": [
        {
            "CapacityReservationId": "cr-1234abcd56EXAMPLE",
            "EndDateType": "unlimited",
            "AvailabilityZone": "eu-west-1a",
            "InstanceMatchCriteria": "open",
            "Tags": [],
            "EphemeralStorage": false,
            "CreateDate": "2019-08-16T09:03:18.000Z",
            "AvailableInstanceCount": 1,
            "InstancePlatform": "Linux/UNIX",
            "TotalInstanceCount": 1,
            "State": "active",
            "Tenancy": "default",
            "EbsOptimized": true,
            "InstanceType": "a1.medium",
            "PlacementGroupArn": "arn:aws:ec2:us-east-1:123456789012:placement-group/MyPG"
        },
        {
            "CapacityReservationId": "cr-abcdEXAMPLE9876ef",
            "EndDateType": "unlimited",
            "AvailabilityZone": "eu-west-1a",
            "InstanceMatchCriteria": "open",
            "Tags": [],
            "EphemeralStorage": false,
            "CreateDate": "2019-08-07T11:34:19.000Z",
            "AvailableInstanceCount": 3,
            "InstancePlatform": "Linux/UNIX",
            "TotalInstanceCount": 3,
            "State": "cancelled",
            "Tenancy": "default",
            "EbsOptimized": true,
            "InstanceType": "m5.large"
        }
    ]
}
```

PowerShell

###### To describe a Capacity Reservation

Use the [Get-EC2CapacityReservation](../../../powershell/latest/reference/items/Get-EC2CapacityReservation.md "../../../powershell/latest/reference/items/Get-EC2CapacityReservation.md")
cmdlet.

```
Get-EC2CapacityReservation `
    -CapacityReservationId `cr-1234abcd56EXAMPLE`
```

## Capacity Reservation states

Capacity Reservations have the following possible states.

| State         | Description                                                                                                                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `active`      | The capacity is available for use.                                                                                                                                                                                                                                                            |
| `expired`     | The Capacity Reservation expired automatically at the date and time specified in your<br>reservation request. The reserved capacity is no longer available for<br>your use.                                                                                                                   |
| `cancelled`   | The Capacity Reservation was canceled. The reserved capacity is no longer available<br>for your use.                                                                                                                                                                                          |
| `pending`     | The Capacity Reservation request was successful but the capacity provisioning is<br>still pending.                                                                                                                                                                                            |
| `failed`      | The Capacity Reservation request has failed. A request can fail due to request<br>parameters that are not valid, capacity constraints, or instance limit<br>constraints. You can view a failed request for 60 minutes.                                                                        |
| `scheduled`   | (_Future-dated Capacity Reservations only_) The future-dated Capacity Reservation<br>request was approved and the Capacity Reservation is scheduled for delivery on the<br>requested start date.                                                                                              |
| `assessing`   | (_Future-dated Capacity Reservations only_) Amazon EC2 is assessing<br>your request for a future-dated Capacity Reservation. For more information, see [Future-dated Capacity Reservation assessment](cr-concepts.md#cr-future-dated-assessment "cr-concepts.md#cr-future-dated-assessment"). |
| `delayed`     | (_Future-dated Capacity Reservations only_) Amazon EC2 encountered a<br>delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable<br>to deliver the requested capacity by the requested start date and<br>time.                                             |
| `unsupported` | (_Future-dated Capacity Reservations only_) Amazon EC2 can't support<br>the future-dated Capacity Reservation request due to capacity constraints. You can view<br>unsupported requests for 30 days. The Capacity Reservation will not be<br>delivered.                                       |
