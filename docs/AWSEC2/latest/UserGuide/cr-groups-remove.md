# Remove Capacity Reservations from a group

You can remove a Capacity Reservation from a group at any time. Instances that target the
group continue running in their current Capacity Reservation and are not affected by the
removal. The Capacity Reservation restores the capacity only when you terminate the
instances.

###### Note

If a Capacity Reservation that is shared with you is later unshared, Amazon EC2 automatically
removes it from the group.

Console

###### To remove Capacity Reservations from a group

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity
   Reservations**.
3. Choose **Capacity Reservation
   Resource Group**.
4. Select the group name to open its details page.
5. In the **Capacity Reservations** section,
   select the Capacity Reservations to remove, then choose
   **Remove**.

AWS CLI

###### To remove Capacity Reservations from a group

Use the [ungroup-resources](../../../cli/latest/reference/resource-groups/ungroup-resources.md "../../../cli/latest/reference/resource-groups/ungroup-resources.md") command.

The following example removes two Capacity Reservations from the specified
group.

```
aws resource-groups ungroup-resources \
    --group `MyCRGroup` \
    --resource-arns \
        arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-0e154d26a16094dd` \
        arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-54321abcdef567890`
```

PowerShell

###### To remove Capacity Reservations from a group

Use the [Remove-RGResource](../../../powershell/latest/reference/items/Remove-RGResource.md "../../../powershell/latest/reference/items/Remove-RGResource.md") cmdlet.

The following example removes two Capacity Reservations from the specified
group.

```
Remove-RGResource `
    -Group `MyCRGroup` `
    -ResourceArn `
        "arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-0e154d26a16094dd`", `
        "arn:aws:ec2:`sa-east-1`:`123456789012`:capacity-reservation/`cr-54321abcdef567890`"
```
