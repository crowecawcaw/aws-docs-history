

# View the state of a Capacity Reservation
<a name="capacity-reservations-view"></a>

Amazon EC2 constantly monitors the state of your Capacity Reservations.

Due to the [eventual consistency](https://docs.aws.amazon.com/ec2/latest/devguide/eventual-consistency.html) model followed by the Amazon EC2 API, after you create a Capacity Reservation, it can take up to 5 minutes for the state of the Capacity Reservation to reflect that it is `active`. During this time, the Capacity Reservation might remain in the `pending` state. However, it might already be available for use, in which case attempts to launch instances into the Capacity Reservation would succeed.

------
#### [ Console ]

**To view your Capacity Reservations**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Reservations**.

1. Select the Capacity Reservation.

------
#### [ AWS CLI ]

**To describe your Capacity Reservations**  
Use the [describe-capacity-reservations](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-capacity-reservations.html) command.

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

------
#### [ PowerShell ]

**To describe a Capacity Reservation**  
Use the [Get-EC2CapacityReservation](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2CapacityReservation.html) cmdlet.

```
Get-EC2CapacityReservation `
    -CapacityReservationId {{cr-1234abcd56EXAMPLE}}
```

------

## Capacity Reservation states
<a name="capacity-reseration-states"></a>

Capacity Reservations have the following possible states.


| State | Description | 
| --- | --- | 
| active | The capacity is available for use. | 
| expired | The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use. | 
| cancelled | The Capacity Reservation was canceled. The reserved capacity is no longer available for your use. | 
| pending | The Capacity Reservation request was successful but the capacity provisioning is still pending. | 
| failed | The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes. | 
| scheduled | (Future-dated Capacity Reservations only) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date. | 
| assessing | (Future-dated Capacity Reservations only) Amazon EC2 is assessing your request for a future-dated Capacity Reservation. For more information, see [Future-dated Capacity Reservation assessment](cr-concepts.md#cr-future-dated-assessment). | 
| delayed | (Future-dated Capacity Reservations only) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time. | 
| unsupported | (Future-dated Capacity Reservations only) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered. | 
| cancelling | (Future-dated Capacity Reservations only) The Capacity Reservation is being canceled. Capacity has been released but charges continue through the end of the reduced commitment period. The Capacity Reservation transitions to cancelled when the commitment ends. For more information, see [Cancellation charges](capacity-reservations-release.md#cr-cancellation-charges). | 