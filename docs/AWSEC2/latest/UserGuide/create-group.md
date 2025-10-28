# Create a Capacity Reservation group

You can use the following examples to create a resource group for Capacity Reservations with the following
request parameters.

- `AWS::EC2::CapacityReservationPool` – Ensures that the resource
  group can be targeted for instance launches.
- `AWS::ResourceGroups::Generic` with `allowed-resource-types`
  set to `AWS::EC2::CapacityReservation` – Ensures that the resource
  group accepts Capacity Reservations only.
  After you create a group, you can [add Capacity Reservations](add-to-group.md "add-to-group.md")
  to the group.

AWS CLI

###### To create a group for Capacity Reservations

Use the [create-group](../../../cli/latest/reference/resource-groups/create-group.md "../../../cli/latest/reference/resource-groups/create-group.md") AWS CLI command.

```
aws resource-groups create-group \
    --name `MyCRGroup` \
    --configuration \
        '{"Type": "AWS::EC2::CapacityReservationPool"}' \
        '{"Type": "AWS::ResourceGroups::Generic", "Parameters": [{"Name": "allowed-resource-types", "Values": ["AWS::EC2::CapacityReservation"]}]}'
```

PowerShell

###### To create a group for Capacity Reservations

Use the [New-RGGroup](../../../powershell/latest/reference/items/New-RGGroup.md "../../../powershell/latest/reference/items/New-RGGroup.md")
cmdlet.

```
New-RGGroup `
    -Name `MyCRGroup` `
    -Configuration `
        @{"Type"="AWS::EC2::CapacityReserationPool"} `
        @{"Type"="AWS::ResourceGroups::Generic"; "Parameters"=@{"allowed-resource-types"=@{"Values"="AWS::EC2::CapacityReservations"}}}
```
