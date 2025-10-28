# Unshare a Dedicated Host that is shared with other AWS accounts

The Dedicated Host owner can unshare a shared Dedicated Host at any time. When you unshare a shared
Dedicated Host, the following rules apply:

- Consumers with whom the Dedicated Host was shared can no longer launch new instances
  onto it.
- Instances owned by consumers that were running on the Dedicated Host at the time of
  unsharing continue to run but are scheduled for [retirement](schedevents_actions_retire.md "schedevents_actions_retire.md").
  Consumers receive retirement notifications for the
  instances and they have two weeks to take action on the notifications.
  However, if the Dedicated Host is reshared with the consumer within the retirement
  notice period, the instance retirements are cancelled.
  To unshare a shared Dedicated Host that you own, you must remove it from the resource share.

Console

###### To unshare a shared Dedicated Host that you own

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Dedicated Hosts**.
3. Choose the Dedicated Host to unshare and choose the
   **Sharing** tab.
4. The **Sharing** tab lists the resource shares
   to which the Dedicated Host has been added. Select the resource share from
   which to remove the Dedicated Host and choose **Remove host from
   resource share**.

###### To unshare a shared Dedicated Host that you own using the AWS RAM console

See [Update a resource share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS RAM User Guide_.

AWS CLI

###### To unshare a shared Dedicated Host that you own

Use the [disassociate-resource-share](../../../cli/latest/reference/ram/disassociate-resource-share.md "../../../cli/latest/reference/ram/disassociate-resource-share.md") command.

```
aws ram disassociate-resource-share \
    --resource-share-arn arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE` \
	--resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:dedicated-host/`h-07879acf49EXAMPLE`
```

PowerShell

###### To unshare a shared Dedicated Host that you own

Use the [Disconnect-RAMResourceShare](../../../powershell/latest/reference/items/Disconnect-RAMResourceShare.md "../../../powershell/latest/reference/items/Disconnect-RAMResourceShare.md") cmdlet.

```
Disconnect-RAMResourceShare `
    -ResourceShareArn "arn:aws:ram:`us-east-2`:`123456789012`:resource-share/`7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`" `
    -ResourceArn "arn:aws:ec2:`us-east-2`:`123456789012`:dedicated-host/`h-07879acf49EXAMPLE`"
```
