# Change the instance type for your Amazon EC2 instance

Use the following instructions to change the instance type of an Amazon EBS-backed instance if
the instance type that you need is compatible with the current configuration of your instance.
For more information, see [Compatibility for changing the instance type](resize-limitations.md "resize-limitations.md").

###### Considerations

- You must stop your instance before you can change its instance type.
  Ensure that you plan for downtime while your instance is stopped. Stopping the
  instance and changing its instance type might take a few minutes, and restarting
  your instance might take a variable amount of time depending on your application's
  startup scripts. For more information, see [Stop and start Amazon EC2 instances](Stop_Start.md "Stop_Start.md").
- When you stop and start an instance, we move the instance to new hardware.
  If your instance has a public IPv4 address, that is not an Elastic IP, we release the address and give your instance a new public IPv4 address. For more information on IP address behavior throughout the lifecycle of an instance, see [Differences between instance states](ec2-instance-lifecycle.md#lifecycle-differences "ec2-instance-lifecycle.md#lifecycle-differences").
- You can't change the instance type of a [Spot Instance](using-spot-instances-request.md#stopping-a-spot-instance "using-spot-instances-request.md#stopping-a-spot-instance").
- [Windows instances] We recommend that you update the AWS PV driver package before
  changing the instance type. For more information, see [Upgrade PV drivers on EC2 Windows
  instances](Upgrading_PV_drivers.md "Upgrading_PV_drivers.md").
- If your instance is in an Amazon EC2 Auto Scaling group, the Amazon EC2 Auto Scaling service marks the stopped
  instance as unhealthy, and might terminate it and launch a replacement instance. To
  prevent this, you can suspend the scaling processes for the group while you're changing
  the instance type. For more information, see [Suspending and resuming a process
  for an Amazon EC2 Auto Scaling group](../../../autoscaling/ec2/userguide/as-suspend-resume-processes.md "../../../autoscaling/ec2/userguide/as-suspend-resume-processes.md") in the _Amazon EC2 Auto Scaling User Guide_.
- When you change the instance type of an instance with NVMe instance store volumes, the
  updated instance might have additional instance store volumes, because all NVMe instance
  store volumes are available even if they are not specified in the AMI or instance block
  device mapping. Otherwise, the updated instance has the same number of instance store
  volumes that you specified when you launched the original instance.
- The maximum number of Amazon EBS volumes that you can attach to an instance depends on the
  instance type and instance size. You can't change to an instance type or instance size that
  does not support the number of volumes that are already attached to your instance. For more
  information, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md "volume_limits.md").
- [Linux instances] You can use the `AWSSupport-MigrateXenToNitroLinux` runbook
  to migrate compatible Linux instances from a Xen instance type to a Nitro instance type. For
  more information, see [AWSSupport-MigrateXenToNitroLinux runbook](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-migrate-xen-to-nitro.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-migrate-xen-to-nitro.md") in the _AWS Systems Manager
  Automation runbook reference_.
- [Windows instances] For additional guidance on migrating compatible Windows instances
  from a Xen instance type to a Nitro instance type, see [Migrate to latest generation instance
  types](migrating-latest-types.md "migrating-latest-types.md").

###### To change the instance type of an Amazon EBS-backed instance

1. (Optional) If the new instance type requires drivers that are not installed on the existing
   instance, you must connect to your instance and install the drivers first. For more information,
   see [Compatibility for changing the instance type](resize-limitations.md "resize-limitations.md").
2. [Windows instances] If you configured your Windows instance to use [static IP addressing](config-windows-multiple-ip.md#step1 "config-windows-multiple-ip.md#step1") and you change from an instance type that doesn't
   support enhanced networking to an instance type that does support enhanced
   networking, you might get a warning about a potential IP address conflict when you
   reconfigure static IP addressing. To prevent this, enable DHCP on the network
   interface for your instance before you change the instance type. From your instance,
   open the **Network and Sharing Center**, open **Internet
   Protocol Version 4 (TCP/IPv4) Properties** for the network interface, and
   choose **Obtain an IP address automatically**. Change the instance
   type and reconfigure static IP addressing on the network interface.
3. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
4. In the navigation pane, choose **Instances**.
5. Select the instance and choose **Instance
   state**, **Stop instance**. When prompted for
   confirmation, choose **Stop**. It can take a few minutes for the
   instance to stop.
6. With the instance still selected, choose **Actions**,
   **Instance settings**, **Change instance
   type**. This option is grayed out if the instance state is not
   `stopped`.
7. On the **Change instance type** page, do the following:
   1. For **Instance type**, select the instance type that you
      want.

   If the instance type is not in the list, then it's not compatible with the
   configuration of your instance. Instead, use the following instructions: [Migrate to a new instance type by launching a new EC2 instance](migrate-instance-configuration.md "migrate-instance-configuration.md"). 2. (Optional) If the instance type that you selected supports EBS optimization,
   select **EBS-optimized** to enable EBS optimization, or
   deselect **EBS-optimized** to disable EBS optimization.

   If the instance type that you selected is EBS optimized by default,
   **EBS-optimized** is selected and you can't deselect
   it. 3. (Optional) Configure vCPU options on the new instance type.

   When you change the instance type of an existing instance, Amazon EC2 applies the
   CPU option settings from the existing instance to the new instance, if possible.
   If the new instance type doesn't support those settings, the CPU options are reset
   to **None**. This option uses the default number of vCPUs for the
   new instance type.

   If the instance type that you selected supports vCPU configuration,
   select **Specify CPU options** in the **Advanced
   details** panel to configure vCPUs for your new instance type. 4. Choose **Change** to accept the new settings.

8. To start the instance, select the instance and choose **Instance
   state**, **Start instance**. It can take a few minutes
   for the instance to enter the `running` state. If your instance won't
   start, see [Troubleshoot changing the instance type](troubleshoot-change-instance-type.md "troubleshoot-change-instance-type.md").
9. [Windows instances] If your instance runs Windows Server 2016 or Windows Server
   2019 with EC2Launch v1, connect to your Windows instance and run the following EC2Launch
   PowerShell script to configure the instance after the instance type is changed.

###### Important

The administrator password will reset when you enable the initialize
instance EC2 Launch script. You can modify the configuration file to
disable the administrator password reset by specifying it in the
settings for the initialization tasks. For steps on how to disable
password reset, see [Configure initialization tasks](ec2launch-config.md#ec2launch-inittasks "ec2launch-config.md#ec2launch-inittasks")
(EC2Launch) or [Change settings](ec2launch-v2-settings.md#ec2launch-v2-ui "ec2launch-v2-settings.md#ec2launch-v2-ui") (EC2Launch v2).

```
`PS C:\>` C:\ProgramData\Amazon\EC2-Windows\Launch\Scripts\InitializeInstance.ps1 -Schedule
```
