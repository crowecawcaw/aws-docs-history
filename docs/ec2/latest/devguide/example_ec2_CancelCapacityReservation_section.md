# Use `CancelCapacityReservation` with a CLI

The following code examples show how to use `CancelCapacityReservation`.

CLI

**AWS CLI**

**To cancel a capacity reservation**

The following `cancel-capacity-reservation` example cancels the specified capacity reservation.

```
`aws ec2 cancel-capacity-reservation \
 --capacity-reservation-id `cr-1234abcd56EXAMPLE``

```

Output:

```
{
    "Return": true
}
```

For more information, see [Cancel a Capacity Reservation](../../../AWSEC2/latest/UserGuide/capacity-reservations-release.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-release.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [CancelCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example cancels the capacity reservation cr-0c1f2345db6f7cdba**

```
Remove-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2CapacityReservation (CancelCapacityReservation)" on target "cr-0c1f2345db6f7cdba".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
True
```

- For API details, see
  [CancelCapacityReservation](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example cancels the capacity reservation cr-0c1f2345db6f7cdba**

```
Remove-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-EC2CapacityReservation (CancelCapacityReservation)" on target "cr-0c1f2345db6f7cdba".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): y
True
```

- For API details, see
  [CancelCapacityReservation](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
