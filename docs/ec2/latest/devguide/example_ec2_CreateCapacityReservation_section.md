# Use `CreateCapacityReservation` with a CLI

The following code examples show how to use `CreateCapacityReservation`.

CLI

**AWS CLI**

**Example 1: To create a Capacity Reservation**

The following `create-capacity-reservation` example creates a capacity reservation in the `eu-west-1a` Availability Zone, into which you can launch three `t2.medium` instances running a Linux/Unix operating system. By default, the capacity reservation is created with open instance matching criteria and no support for ephemeral storage, and it remains active until you manually cancel it.

```
`aws ec2 create-capacity-reservation \
 --availability-zone `eu-west-1a` \
 --instance-type `t2.medium` \
 --instance-platform `Linux/UNIX` \
 --instance-count `3``

```

Output:

```
{
    "CapacityReservation": {
        "CapacityReservationId": "cr-1234abcd56EXAMPLE ",
        "EndDateType": "unlimited",
        "AvailabilityZone": "eu-west-1a",
        "InstanceMatchCriteria": "open",
        "EphemeralStorage": false,
        "CreateDate": "2019-08-16T09:27:35.000Z",
        "AvailableInstanceCount": 3,
        "InstancePlatform": "Linux/UNIX",
        "TotalInstanceCount": 3,
        "State": "active",
        "Tenancy": "default",
        "EbsOptimized": false,
        "InstanceType": "t2.medium"
    }
}
```

**Example 2: To create a Capacity Reservation that automatically ends at a specified date/time**

The following `create-capacity-reservation` example creates a capacity reservation in the `eu-west-1a` Availability Zone, into which you can launch three `m5.large` instances running a Linux/Unix operating system. This capacity reservation automatically ends on 08/31/2019 at 23:59:59.

```
`aws ec2 create-capacity-reservation \
 --availability-zone `eu-west-1a` \
 --instance-type `m5.large` \
 --instance-platform `Linux/UNIX` \
 --instance-count `3` \
 --end-date-type `limited` \
 --end-date `2019-08-31T23:59:59Z``

```

Output:

```
{
    "CapacityReservation": {
        "CapacityReservationId": "cr-1234abcd56EXAMPLE ",
        "EndDateType": "limited",
        "AvailabilityZone": "eu-west-1a",
        "EndDate": "2019-08-31T23:59:59.000Z",
        "InstanceMatchCriteria": "open",
        "EphemeralStorage": false,
        "CreateDate": "2019-08-16T10:15:53.000Z",
        "AvailableInstanceCount": 3,
        "InstancePlatform": "Linux/UNIX",
        "TotalInstanceCount": 3,
        "State": "active",
        "Tenancy": "default",
        "EbsOptimized": false,
        "InstanceType": "m5.large"
    }
}
```

**Example 3: To create a Capacity Reservation that accepts only targeted instance launches**

The following `create-capacity-reservation` example creates a capacity reservation that accepts only targeted instance launches.

```
`aws ec2 create-capacity-reservation \
 --availability-zone `eu-west-1a` \
 --instance-type `m5.large` \
 --instance-platform `Linux/UNIX` \
 --instance-count `3` \
 --instance-match-criteria `targeted``

```

Output:

```
{
    "CapacityReservation": {
        "CapacityReservationId": "cr-1234abcd56EXAMPLE ",
        "EndDateType": "unlimited",
        "AvailabilityZone": "eu-west-1a",
        "InstanceMatchCriteria": "targeted",
        "EphemeralStorage": false,
        "CreateDate": "2019-08-16T10:21:57.000Z",
        "AvailableInstanceCount": 3,
        "InstancePlatform": "Linux/UNIX",
        "TotalInstanceCount": 3,
        "State": "active",
        "Tenancy": "default",
        "EbsOptimized": false,
        "InstanceType": "m5.large"
    }
}
```

For more information, see [Create a Capacity Reservation](../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [CreateCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example creates a new Capacity Reservation with the specified attributes**

```
Add-EC2CapacityReservation -InstanceType m4.xlarge -InstanceCount 2 -AvailabilityZone eu-west-1b -EbsOptimized True -InstancePlatform Windows

```

**Output:**

```
AvailabilityZone       : eu-west-1b
AvailableInstanceCount : 2
CapacityReservationId  : cr-0c1f2345db6f7cdba
CreateDate             : 3/28/2019 9:29:41 AM
EbsOptimized           : True
EndDate                : 1/1/0001 12:00:00 AM
EndDateType            : unlimited
EphemeralStorage       : False
InstanceMatchCriteria  : open
InstancePlatform       : Windows
InstanceType           : m4.xlarge
State                  : active
Tags                   : {}
Tenancy                : default
TotalInstanceCount     : 2
```

- For API details, see
  [CreateCapacityReservation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example creates a new Capacity Reservation with the specified attributes**

```
Add-EC2CapacityReservation -InstanceType m4.xlarge -InstanceCount 2 -AvailabilityZone eu-west-1b -EbsOptimized True -InstancePlatform Windows

```

**Output:**

```
AvailabilityZone       : eu-west-1b
AvailableInstanceCount : 2
CapacityReservationId  : cr-0c1f2345db6f7cdba
CreateDate             : 3/28/2019 9:29:41 AM
EbsOptimized           : True
EndDate                : 1/1/0001 12:00:00 AM
EndDateType            : unlimited
EphemeralStorage       : False
InstanceMatchCriteria  : open
InstancePlatform       : Windows
InstanceType           : m4.xlarge
State                  : active
Tags                   : {}
Tenancy                : default
TotalInstanceCount     : 2
```

- For API details, see
  [CreateCapacityReservation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
