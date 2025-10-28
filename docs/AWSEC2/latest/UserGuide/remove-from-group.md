# Remove a Capacity Reservation from a group

You can use the following examples to remove a Capacity Reservation from a group.

AWS CLI

###### To remove a Capacity Reservation from a group

Use the [ungroup-resources](../../../cli/latest/reference/resource-groups/ungroup-resources.md "../../../cli/latest/reference/resource-groups/ungroup-resources.md") command.

The following example removes two Capacity Reservations from the specified group.

```
aws resource-groups ungroup-resources \
    --group `MyCRGroup` \
    --resource-arns \
        arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-0e154d26a16094dd` \
        arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-54321abcdef567890`
```

PowerShell

###### To remove a Capacity Reservation from a group

Use the [Remove-RGResource](../../../powershell/latest/reference/items/Remove-RGResource.md "../../../powershell/latest/reference/items/Remove-RGResource.md") cmdlet.

The following example removes two Capacity Reservations from the specified group.

```
Remove-RGResource `
    -Group `MyCRGroup` `
    -ResourceArn `
        "arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-0e154d26a16094dd`", `
        "arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-54321abcdef567890`"
```
