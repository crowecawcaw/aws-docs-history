

# Create a group
<a name="cr-groups-create"></a>

You can create a group to organize your Capacity Reservations. After you create a group, you can [add Capacity Reservations to the group](cr-groups-add.md).

------
#### [ Console ]

**To create a group**  


1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Reservations**.

1. Choose **Capacity Reservation Resource Group**.

1. Choose **Create Group**.

1. Enter a group name, and optionally add a description, Capacity Reservations, and tags.

1. Choose **Create**.

------
#### [ AWS CLI ]

**To create a group for Capacity Reservations**  
Use the [create-group](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/create-group.html) AWS CLI command with the following request parameters.
+ `AWS::EC2::CapacityReservationPool` – Ensures that the Capacity Reservation Resource Group can be targeted for instance launches.
+ `AWS::ResourceGroups::Generic` with `allowed-resource-types` set to `AWS::EC2::CapacityReservation` – Ensures that the Capacity Reservation Resource Group accepts Capacity Reservations only.

```
aws resource-groups create-group \
    --name {{MyCRGroup}} \
    --configuration \
        '{"Type": "AWS::EC2::CapacityReservationPool"}' \
        '{"Type": "AWS::ResourceGroups::Generic", "Parameters": [{"Name": "allowed-resource-types", "Values": ["AWS::EC2::CapacityReservation"]}]}'
```

------
#### [ PowerShell ]

**To create a group for Capacity Reservations**  
Use the [New-RGGroup](https://docs.aws.amazon.com/powershell/latest/reference/items/New-RGGroup.html) cmdlet.

```
New-RGGroup `
    -Name {{MyCRGroup}} `
    -Configuration `
        @{"Type"="AWS::EC2::CapacityReservationPool"} `
        @{"Type"="AWS::ResourceGroups::Generic"; "Parameters"=@{"allowed-resource-types"=@{"Values"="AWS::EC2::CapacityReservation"}}}
```

------

To create a group that accepts only UltraServer Capacity Blocks of a specific instance type, see [Create a Capacity Reservation Resource Group for UltraServer Capacity Blocks](cb-group.md).