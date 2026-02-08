# Share Capacity Blocks

Capacity Block sharing enables Capacity Block owners to share Amazon EC2 Capacity Blocks with other AWS accounts within an AWS Organization.
This allows you to maximize utilization of reserved GPU capacity across different teams and projects to efficiently use the Capacity Blocks.

The AWS account that owns the Capacity Block (owner) can share it with other AWS accounts (consumers).
An owner can share a Capacity Block with specific AWS accounts inside their AWS Organization, an organizational unit inside their AWS Organization, or the entire AWS Organization.
Consumers can launch instances into Capacity Blocks that are shared with them in the same way that they launch instances into Capacity Blocks they own.

## Prerequisites for sharing Capacity Blocks

Before you can share a Capacity Block, the following conditions must be met:

- **You must own the Capacity Block** - You cannot share a Capacity Block that has been shared with you.
- **The Capacity Block state must be active or scheduled** - Capacity Blocks that are in other
  [states](../../../cli/latest/reference/ec2/purchase-capacity-block.md "../../../cli/latest/reference/ec2/purchase-capacity-block.md"), such as
  `expired` or `payment-pending` cannot be shared.
- **Sharing within your AWS Organization only** - An owner can share a Capacity Block with specific AWS accounts inside their AWS Organization, an organizational unit inside their AWS Organization, or the entire AWS Organization.
- **UltraServer Capacity Blocks not supported** - You cannot share Capacity Blocks for Amazon EC2 UltraServers.
- **Account eligibility** - Capacity Block sharing is not available to new AWS accounts or AWS accounts that have a limited billing history.

## Related services

Capacity Block sharing integrates with AWS Resource Access Manager (AWS RAM). AWS RAM is a service that enables
you to share your AWS resources with any AWS account or through AWS Organizations. With
AWS RAM, you share resources that you own by creating a _resource share_.
A resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can be individual AWS accounts, or organizational units or an entire organization from AWS Organizations.

For more information about AWS RAM, see the _[AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md")_.

## Shared Capacity Block permissions

### Permissions for owners

The Capacity Block owner remains responsible for managing the Capacity Block (e.g. extending, sharing), and the instances they launch into it.
Owners cannot modify instances that consumers launch into Capacity Blocks they have shared.

### Permissions for consumers

Consumers can launch instances into the shared capacity and are responsible for managing those instances.
Consumers cannot view or modify instances owned by other consumers or by the Capacity Block owner.
Consumers can also only view the total capacity and available capacity in the shared Capacity Block.

## Share a Capacity Block

To share a Capacity Block, you must add it to a resource share. A resource share is an AWS RAM resource that lets you share your resources across AWS accounts.

If you added your Capacity Block to a resource share that is shared with the entire AWS Organization, consumers in your organization are granted access to the shared Capacity Block.

Console

###### To share a Capacity Block that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Reservations**.
3. Select the Capacity Block to share and choose **Actions, Share reservation**.
4. Select the resource share to which to add the Capacity Block and choose **Share Capacity Reservation**.

It could take a few minutes for consumers to get access to the shared Capacity Block.

###### To add a Capacity Block to a new resource share

You must first create the resource share using the AWS RAM console.
For more information, see
[Creating a resource share](../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create "../../../ram/latest/userguide/working-with-sharing.md#working-with-sharing-create")
in the _AWS RAM User Guide_.

AWS CLI

###### To share a Capacity Block that you own

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") and
[associate-resource-share](../../../cli/latest/reference/ram/associate-resource-share.md "../../../cli/latest/reference/ram/associate-resource-share.md") commands.

```
aws ram create-resource-share \
    --name `my-resource-share` \
    --resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`
```

```
aws ram associate-resource-share \
    --resource-share-arn arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE` \
    --resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`
```

PowerShell

###### To share a Capacity Block that you own

Use the [New-RAMResourceShare](../../../powershell/latest/reference/items/New-RAMResourceShare.md "../../../powershell/latest/reference/items/New-RAMResourceShare.md") and
[Connect-RAMResourceShare](../../../powershell/latest/reference/items/Connect-RAMResourceShare.md "../../../powershell/latest/reference/items/Connect-RAMResourceShare.md") cmdlets.

```
New-RAMResourceShare `
    -Name `my-resource-share` `
    -ResourceArn "arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`"
```

```
Connect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`" `
    -ResourceArn "arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`"
```

Capacity Blocks operate on a **first-come, first-served basis** for all accounts, regardless of ownership status.
When you share a Capacity Block, if a consumer launches instances before the owner, those instances occupy the capacity
until the consumer terminates the instances or until 30 minutes before the Capacity Block expires.

## Stop sharing a Capacity Block

You can stop sharing a Capacity Block at any time until 30 minutes before the block expiry date.

###### What happens when you stop sharing:

- Consumers can no longer launch new instances into the Capacity Block that was unshared.
- Any running instances continue running until 30 minutes before the Capacity Block expiry date, unless terminated by the consumer.

Console

###### To stop sharing a Capacity Block that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Capacity Reservations**.
3. Select the Capacity Block and choose the **Sharing** tab.
4. The **Sharing** tab lists the resource shares to which the Capacity Block has been added.
   Select the resource share from which to remove the Capacity Block.
5. Choose **Remove from resource share**.

AWS CLI

###### To stop sharing a Capacity Block that you own

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

```
aws ram disassociate-resource-share \
    --resource-share-arn arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE` \
    --resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`
```

PowerShell

###### To stop sharing a Capacity Block that you own

Use the [Disconnect-RAMResourceShare](../../../powershell/latest/reference/items/Disconnect-RAMResourceShare.md "../../../powershell/latest/reference/items/Disconnect-RAMResourceShare.md") cmdlet.

```
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`" `
    -ResourceArn "arn:aws:ec2:`us-east-2`:`123456789012`:capacity-reservation/`cr-1234abcd56EXAMPLE`"
```

## Monitor shared Capacity Block usage

Capacity Block owners can monitor which accounts are using their shared Capacity Blocks and track instance usage per account.

AWS CLI

###### To monitor usage of a Capacity Block

Use the [get-capacity-reservation-usage](../../../cli/latest/reference/ec2/get-capacity-reservation-usage.md "../../../cli/latest/reference/ec2/get-capacity-reservation-usage.md") command.

```
aws ec2 get-capacity-reservation-usage \
    --capacity-reservation-id `cr-1234abcd56EXAMPLE`
```

###### This API enables owners to:

- View which accounts are currently using the Capacity Block.
- See the number of instances each account is running.

## Instance termination notices

Owner and consumer accounts that have instances running in the Capacity Block will receive an EventBridge event
40 minutes before the Capacity Block reservation ends, indicating that any instances running in the
reservation will begin to terminate in 10 minutes. For more information, see
[Monitor Capacity Blocks using EventBridge](capacity-blocks-monitor.md "capacity-blocks-monitor.md").

## Capacity Block extensions

Capacity Blocks can be extended while they are shared. Only the owner account can extend a shared Capacity Block.

When a Capacity Block is extended, running instances launched by the owner or consumers automatically inherit the new expiry date,
and consumers can continue using the shared capacity until the new expiry date without any instance interruption.

## Pricing and billing

Owners are billed for the Capacity Blocks they share and pay upfront for the Capacity Block when they purchase it.
Owners also pay for operating system charges for instances they run on the Capacity Block.

Consumers are billed only for the operating system charges for instances they run in the shared Capacity Block.
Consumers are not charged for the Capacity Block reservation itself.
