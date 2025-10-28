# Allocate an Amazon EC2 Dedicated Host for use in

your account

To begin using a Dedicated Host, you must first allocate it in your account. After you
allocate the Dedicated Host, the Dedicated Host capacity is made available in your account immediately
and you can start launching instances onto the Dedicated Host.

When you allocate a Dedicated Host in your account, you can choose a configuration
that supports either a **single instance type**,
or **multiple instance types** within the same
instance family. The number of instances that you can run on the host depends
on the configuration you choose. For more information see
[Amazon EC2 Dedicated Host instance capacity configurations](dedicated-hosts-limits.md "dedicated-hosts-limits.md").

Console

###### To allocate a Dedicated Host

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Dedicated Hosts** and
   then choose **Allocate Dedicated Host**.
3. For **Instance family**, choose the instance
   family for the Dedicated Host.
4. Specify whether the Dedicated Host supports multiple instance sizes
   within the selected instance family, or a specific instance type
   only. Do one of the following.
   - To configure the Dedicated Host to support multiple instance
     types in the selected instance family, for
     **Support multiple instance
     types**, choose **Enable**.
     Enabling this allows you to launch different instance
     sizes from the same instance family onto the Dedicated Host. For
     example, if you choose the `m5` instance
     family and choose this option, you can launch
     `m5.xlarge` and `m5.4xlarge`
     instances onto the Dedicated Host.
   - To configure the Dedicated Host to support a single instance
     type within the selected instance family, clear
     **Support multiple instance
     types**, and then for **Instance
     type**, choose the instance type to
     support. This allows you to launch a single instance
     type on the Dedicated Host. For example, if you choose this option
     and specify `m5.4xlarge` as the supported
     instance type, you can launch only
     `m5.4xlarge` instances onto the
     Dedicated Host.

5. For **Availability Zone**, choose the
   Availability Zone in which to allocate the Dedicated Host.
6. To allow the Dedicated Host to accept untargeted instance launches that
   match its instance type, for **Instance
   auto-placement**, choose
   **Enable**. For more information about
   auto-placement, see [Amazon EC2 Dedicated Host auto-placement and host affinity](dedicated-hosts-understanding.md "dedicated-hosts-understanding.md").
7. To enable host recovery for the Dedicated Host, for **Host
   recovery**, choose **Enable**. For
   more information, see [Amazon EC2 Dedicated Host recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md").
8. For **Quantity**, enter the number of Dedicated Hosts
   to allocate.
9. (Optional) Choose **Add new tag** and enter a
   tag key and a tag value.
10. Choose **Allocate**.

AWS CLI

###### To allocate a Dedicated Host

Use the [allocate-hosts](../../../cli/latest/reference/ec2/allocate-hosts.md "../../../cli/latest/reference/ec2/allocate-hosts.md") command. The following example
allocates a Dedicated Host that supports multiple instance types from the
`m5` instance family in the `us-east-1a`
Availability Zone. It also enables host recovery and disables
auto-placement.

```
aws ec2 allocate-hosts \
    --instance-family "`m5`" \
    --availability-zone "`us-east-1a`" \
    --auto-placement "`off`" \
    --host-recovery "`on`" \
    --quantity 1
```

The following example allocates a Dedicated Host that supports
_untargeted_ instance launches in the specified
Availability Zone, enables host recovery, and enables auto-placement.

```
aws ec2 allocate-hosts \
    --instance-type `"m5.large"` \
    --availability-zone `"eu-west-1a"` \
    --auto-placement `"on"` \
    --host-recovery `"on"` \
    --quantity 1
```

PowerShell

###### To allocate a Dedicated Host

Use the [New-EC2Host](../../../powershell/latest/reference/items/New-EC2Host.md "../../../powershell/latest/reference/items/New-EC2Host.md") cmdlet. The following example
allocates a Dedicated Host that supports multiple instance types from the
`m5` instance family in the `us-east-1a`
Availability Zone. The host also has host recovery enabled and
auto-placement disabled.

```
New-EC2Host `
    -InstanceFamily `m5` `
    -AvailabilityZone `us-east-1a` `
    -AutoPlacement `Off` `
    -HostRecovery `On` `
    -Quantity 1
```

The following example allocates a Dedicated Host that supports
_untargeted_ instance launches in the specified
Availability Zone and enables host recovery.

```
New-EC2Host `
    -InstanceType `m5.large` `
    -AvailabilityZone `eu-west-1a` `
    -AutoPlacement `On` `
    -HostRecovery `On` `
    -Quantity 1
```
