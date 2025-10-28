# Share an Amazon EC2 Dedicated Host across AWS accounts

When an owner shares a Dedicated Host, it enables consumers to launch instances on the host.
Consumers can launch as many instances onto the shared host as its available
capacity allows.

###### Important

Note that you are responsible for ensuring that you have appropriate license
rights to share any BYOL licenses on your Dedicated Hosts.

If you share a Dedicated Host with auto-placement enabled, keep the following in mind as it
could lead to unintended Dedicated Host usage:

- If consumers launch instances with Dedicated Host tenancy and they do not have
  capacity on a Dedicated Host that they own in their account, the instance is
  automatically launched onto the shared Dedicated Host.
  To share a Dedicated Host, you must add it to a resource share. A resource share is an AWS RAM
  resource that lets you share your resources across AWS accounts. A resource share
  specifies the resources to share, and the consumers with whom they are shared. You
  can add the Dedicated Host to an existing resource, or you can add it to a new resource
  share.

If you are part of an organization in AWS Organizations and sharing within your
organization is enabled, consumers in your organization are automatically granted
access to the shared Dedicated Host. Otherwise, consumers receive an invitation to join the
resource share and are granted access to the shared Dedicated Host after accepting the
invitation.

###### Note

After you share a Dedicated Host, it could take a few minutes for consumers to have
access to it.

Console

###### To share a Dedicated Host that you own using the Amazon EC2 console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Dedicated Hosts**.
3. Choose the Dedicated Host to share and choose
   **Actions**, **Share
   host**.
4. Select the resource share to which to add the Dedicated Host and choose
   **Share host**.

It could take a few minutes for consumers to get access to the
shared host.

###### To share a Dedicated Host that you own using the AWS RAM console

See [Create a resource share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS RAM User Guide_.

AWS CLI

###### To share a Dedicated Host that you own

Use the [create-resource-share](../../../cli/latest/reference/ram/create-resource-share.md "../../../cli/latest/reference/ram/create-resource-share.md") command.

```
aws ram create-resource-share \
    --name `my-resource-share` \
    --resource-arns arn:aws:ec2:`us-east-2`:`123456789012`:dedicated-host/`h-07879acf49EXAMPLE`
```

PowerShell

###### To share a Dedicated Host that you own

Use the [New-RAMResourceShare](../../../powershell/latest/reference/items/New-RAMResourceShare.md "../../../powershell/latest/reference/items/New-RAMResourceShare.md") cmdlet.

```
New-RAMResourceShare `
    -Name `my-resource-share` `
    -ResourceArn arn:aws:ec2:`us-east-2`:`123456789012`:dedicated-host/`h-07879acf49EXAMPLE`
```
