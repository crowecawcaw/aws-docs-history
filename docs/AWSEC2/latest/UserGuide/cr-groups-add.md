

# Add Capacity Reservations to a group
<a name="cr-groups-add"></a>

You can add Capacity Reservations that you own in your account, or Capacity Reservations that are shared with you by other AWS accounts to a group.

**Considerations**  

+ You can add only Capacity Reservations in the `active` state to a group.
+ If a shared Capacity Reservation is later unshared by its owner, Amazon EC2 automatically removes it from your group.

------
#### [ Console ]

You can add Capacity Reservations to a group from the Capacity Reservation Resource Group details page, or from the Capacity Reservation console.

**To add Capacity Reservations from the Capacity Reservation Resource Group page**  


1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Reservations**.

1. Choose **Capacity Reservation Resource Group**.

1. Select the group name to open its details page.

1. In the **Capacity Reservations** section, choose **Add**.

1. Select the Capacity Reservations you want to add, then choose **Add**.

**To add Capacity Reservations from the Capacity Reservation console**  


1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Reservations**.

1. Select the Capacity Reservation you want to add to a group.

1. Choose **Action**, then choose **Add to group**.

1. Select the group, then choose **Add**.

------
#### [ AWS CLI ]

**To add Capacity Reservations to a group**  
Use the [group-resources](https://docs.aws.amazon.com/cli/latest/reference/resource-groups/group-resources.html) command. Provide the ARN of each Capacity Reservation you want to add.

The following example adds two Capacity Reservations to the specified group.

```
aws resource-groups group-resources \
    --group {{MyCRGroup}} \
    --resource-arns \
        arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-1234567890abcdef1}} \
        arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-54321abcdef567890}}
```

------
#### [ PowerShell ]

**To add Capacity Reservations to a group**  
Use the [Add-RGResource](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-RGResource.html) cmdlet.

The following example adds two Capacity Reservations to the specified group.

```
Add-RGResource `
    -Group {{MyCRGroup}} `
    -ResourceArn `
        "arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-1234567890abcdef1}}", `
        "arn:aws:ec2:{{sa-east-1}}:{{123456789012}}:capacity-reservation/{{cr-54321abcdef567890}}"
```

------