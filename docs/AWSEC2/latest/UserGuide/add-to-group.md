# Add a Capacity Reservation to a group

If you add a Capacity Reservation that is shared with you to a group, and that Capacity Reservation is unshared,
it is automatically removed from the group.

AWS CLI

###### To add a Capacity Reservation to a group

Use the [group-resources](../../../cli/latest/reference/resource-groups/group-resources.md "../../../cli/latest/reference/resource-groups/group-resources.md") command.

The following example adds two Capacity Reservations to the specified group.

```
aws resource-groups group-resources \
    --group `MyCRGroup` \
    --resource-arns \
        arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-1234567890abcdef1` \
        arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-54321abcdef567890`
```

PowerShell

###### To add a Capacity Reservation to a group

Use the [Add-RGResource](../../../powershell/latest/reference/items/Add-RGResource.md "../../../powershell/latest/reference/items/Add-RGResource.md")
cmdlet.

The following example adds two Capacity Reservations to the specified group.

```
Add-RGResource `
    -Group `MyCRGroup` `
    -ResourceArn `
        "arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-1234567890abcdef1`", `
        "arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-54321abcdef567890`"
```
