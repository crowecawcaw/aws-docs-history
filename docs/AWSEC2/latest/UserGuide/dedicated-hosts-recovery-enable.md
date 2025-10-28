# Manage Amazon EC2 Dedicated Host recovery

Dedicated Host auto recovery restarts your instances on to a new replacement host when certain
problematic conditions are detected on your Dedicated Host. You can enable host recovery when you
allocate the Dedicated Host or after allocation.

Use the following procedures to enable host recovery when allocating the host.

Console

###### To enable host recovery at allocation

When allocating a Dedicated Host using the Amazon EC2 console, for **Host recovery**,
choose **Enable**. For more information, see [Allocate an Amazon EC2 Dedicated Host for use in
your account](dedicated-hosts-allocating.md "dedicated-hosts-allocating.md").

AWS CLI

###### To enable host recovery at allocation

Use the [allocate-hosts](../../../cli/latest/reference/ec2/allocate-hosts.md "../../../cli/latest/reference/ec2/allocate-hosts.md") command.

```
aws ec2 allocate-hosts \
    --instance-type `m5.large` \
    --availability-zone `eu-west-1a` \
    --auto-placement on \
    --host-recovery on \
    --quantity 1
```

PowerShell

###### To enable host recovery at allocation

Use the [New-EC2Host](../../../powershell/latest/reference/items/New-EC2Host.md "../../../powershell/latest/reference/items/New-EC2Host.md") cmdlet.

```
New-EC2Host `
    -InstanceType `m5.large` `
    -AvailabilityZone `eu-west-1a` `
    -AutoPlacement on `
    -HostRecovery on `
    -Quantity 1
```

Use the following procedures to manage host recovery for a Dedicated Host.

Console

###### To manage host recovery after allocation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Dedicated Hosts**.
3. Select the Dedicated Host.
4. Choose **Actions**, **Modify host**.
5. For **Host recovery**, select or clear
   **Enable**.
6. Choose **Save**.

AWS CLI

###### To enable host recovery after allocation

Use the [modify-hosts](../../../cli/latest/reference/ec2/modify-hosts.md "../../../cli/latest/reference/ec2/modify-hosts.md") command.

```
aws ec2 modify-hosts \
    --host-recovery on \
    --host-ids `h-012a3456b7890cdef`
```

###### To disable host recovery after allocation

Use the [modify-hosts](../../../cli/latest/reference/ec2/modify-hosts.md "../../../cli/latest/reference/ec2/modify-hosts.md") command and specify the `host-recovery`
parameter with a value of `off`.

```
aws ec2 modify-hosts \
    --host-recovery off \
    --host-ids `h-012a3456b7890cdef`
```

PowerShell

###### To enable host recovery after allocation

Use the [Edit-host](../../../powershell/latest/reference/items/Edit-EC2Host.md "../../../powershell/latest/reference/items/Edit-EC2Host.md") cmdlet.

```
Edit-EC2Host `
    -HostRecovery on `
    -HostId `h-012a3456b7890cdef`
```

###### To disable host recovery after allocation

Use the [Edit-EC2Host](../../../powershell/latest/reference/items/Edit-EC2Host.md "../../../powershell/latest/reference/items/Edit-EC2Host.md") cmdlet.

```
Edit-EC2Host `
    -HostRecovery off `
    -HostId `h-012a3456b7890cdef`
```
