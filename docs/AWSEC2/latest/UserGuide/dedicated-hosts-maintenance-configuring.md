# Configure the host maintenance setting for an Amazon EC2 Dedicated Host

Enable host maintenance to ensure that your instances running on a Dedicated Host are
automatically recovered onto a new Dedicated Host during a scheduled maintenance event.

If you disable host maintenance, you receive an email notification to evict
the degraded host and manually migrate your instances to another host within 28
days. A replacement host is allocated if you have Dedicated Host reservation. After 28
days, the instances running on the degraded host are terminated, and the host is
released automatically.

Console

###### To enable host maintenance for your Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Dedicated Hosts**.
3. Select the Dedicated Host > **Actions** >
   **Modify host**.
4. Select _on_ in the **Host
   maintenance** field.

###### To disable host maintenance for your Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Dedicated Hosts**.
3. Select the Dedicated Host > **Actions** >
   **Modify host**.
4. Select _off_ in the **Host
   maintenance** field.

AWS CLI

###### To enable host maintenance for your Dedicated Host

Use the [modify-hosts](../../../cli/latest/reference/ec2/modify-hosts.md "../../../cli/latest/reference/ec2/modify-hosts.md") command.

```
aws ec2 modify-hosts \
    --host-maintenance on \
    --host-ids `h-0d123456bbf78910d`
```

###### To disable host maintenance for your Dedicated Host

Use the [modify-hosts](../../../cli/latest/reference/ec2/modify-hosts.md "../../../cli/latest/reference/ec2/modify-hosts.md") command.

```
aws ec2 modify-hosts \
    --host-maintenance off \
    --host-ids `h-0d123456bbf78910d`
```

PowerShell

###### To enable host maintenance for your Dedicated Host

Use the [Edit-EC2Host](../../../powershell/latest/reference/items/Edit-EC2Host.md "../../../powershell/latest/reference/items/Edit-EC2Host.md") cmdlet.

```
Edit-EC2Host `
    -HostMaintenance on `
    -HostId `h-0d123456bbf78910d`
```

###### To disable host maintenance for your Dedicated Host

Use the [Edit-EC2Host](../../../powershell/latest/reference/items/Edit-EC2Host.md "../../../powershell/latest/reference/items/Edit-EC2Host.md") cmdlet.

```
Edit-EC2Host `
    -HostMaintenance off `
    -HostId `h-0d123456bbf78910d`
```
