

# Stop sharing a Capacity Reservation
<a name="unsharing-cr"></a>

The Capacity Reservation owner can stop sharing a Capacity Reservation at any time. The following rules apply:
+ Instances owned by consumers that were running in the shared capacity at the time sharing stops continue to run in the reserved capacity. The capacity is restored to the Capacity Reservation when consumers terminate the instances.
+ Consumers with whom the Capacity Reservation was shared can no longer launch new instances into the reserved capacity.

To stop sharing a Capacity Reservation that you own, you must remove it from the resource share.

------
#### [ Console ]

**To stop sharing a Capacity Reservation that you own using the Amazon EC2 console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Capacity Reservations**.

1. Select the Capacity Reservation and choose the **Sharing** tab.

1. The **Sharing** tab lists the resource shares to which the Capacity Reservation has been added. Select the resource share from which to remove the Capacity Reservation and choose **Remove from resource share**.

**To stop sharing a Capacity Reservation that you own using the AWS RAM console**  
See [Updating a Resource Share](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing.html#working-with-sharing-update) in the *AWS RAM User Guide*.

------
#### [ AWS CLI ]

**To stop sharing a Capacity Reservation that you own**  
Use the [disassociate-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/disassociate-resource-share.html) command.

```
aws ram disassociate-resource-share \
    --resource-share-arn arn:aws:ram:{{us-east-2}}:{{123456789012}}:resource-share/{{7ab63972-b505-7e2a-420d-6f5d3EXAMPLE}} \
	--resource-arns arn:aws:ec2:{{us-east-2}}:{{123456789012}}:capacity-reservation/{{cr-1234abcd56EXAMPLE}}
```

------
#### [ PowerShell ]

**To stop sharing a Capacity Reservation that you own**  
Use the [Disconnect-RAMResourceShare](https://docs.aws.amazon.com/powershell/latest/reference/items/Disconnect-RAMResourceShare.html) cmdlet.

```
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:{{us-east-2}}:{{123456789012}}:resource-share/{{7ab63972-b505-7e2a-420d-6f5d3EXAMPLE}}" `
    -ResourceArn "arn:aws:ec2:{{us-east-2}}:{{123456789012}}:capacity-reservation/{{cr-1234abcd56EXAMPLE}}"
```

------