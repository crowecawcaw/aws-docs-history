# Stop sharing a Capacity Reservation

The Capacity Reservation owner can stop sharing a Capacity Reservation at any time. The following rules
apply:

- Instances owned by consumers that were running in the shared capacity at
  the time sharing stops continue to run normally outside of the reserved
  capacity, and the capacity is restored to the Capacity Reservation subject to Amazon EC2 capacity
  availability.
- Consumers with whom the Capacity Reservation was shared can no longer launch new instances
  into the reserved capacity.
  To stop sharing a Capacity Reservation that you own, you must remove it from the resource share.

Console

###### To stop sharing a Capacity Reservation that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Capacity Reservations**.
3. Select the Capacity Reservation and choose the **Sharing**
   tab.
4. The **Sharing** tab lists the resource shares
   to which the Capacity Reservation has been added. Select the resource share from
   which to remove the Capacity Reservation and choose **Remove from
   resource share**.

###### To stop sharing a Capacity Reservation that you own using the AWS RAM console

See [Updating a Resource Share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-update") in the _AWS RAM User Guide_.

AWS CLI

###### To stop sharing a Capacity Reservation that you own

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

```
aws ram disassociate-resource-share \
    --resource-share-arn arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE` \
	--resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`
```

PowerShell

###### To stop sharing a Capacity Reservation that you own

Use the [Disconnect-RAMResourceShare](../../../powershell/latest/reference/items/Disconnect-RAMResourceShare.md "../../../powershell/latest/reference/items/Disconnect-RAMResourceShare.md") cmdlet.

```
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`" `
    -ResourceArn "arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`"
```
