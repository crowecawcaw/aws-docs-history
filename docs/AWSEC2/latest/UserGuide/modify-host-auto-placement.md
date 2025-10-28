# Modify the auto-placement setting for an existing Amazon EC2 Dedicated Host

You can modify the auto-placement settings of a Dedicated Host after you have allocated it
to your AWS account.

Console

###### To modify the auto-placement of a Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Dedicated Hosts**.
3. Select a host and choose **Actions**,
   **Modify host**.
4. For **Instance auto-placement**, choose
   **Enable** to enable auto-placement, or
   clear **Enable** to disable auto-placement. For
   more information, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").
5. Choose **Save**.

AWS CLI

###### To modify the auto-placement of a Dedicated Host

Use the [modify-hosts](../../../cli/latest/reference/ec2/modify-hosts.md "../../../cli/latest/reference/ec2/modify-hosts.md") command.

```
aws ec2 modify-hosts \
    --auto-placement `on` \
    --host-ids `h-012a3456b7890cdef`
```

PowerShell

###### To modify the auto-placement of a Dedicated Host

Use the [Edit-EC2Host](../../../powershell/latest/reference/items/Edit-EC2Host.md "../../../powershell/latest/reference/items/Edit-EC2Host.md") cmdlet.

```
Edit-EC2Host `
    -AutoPlacement `1` `
    -HostId `h-012a3456b7890cdef`
```
