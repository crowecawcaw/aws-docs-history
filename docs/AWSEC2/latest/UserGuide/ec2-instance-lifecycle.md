

# Amazon EC2 instance state changes
<a name="ec2-instance-lifecycle"></a>

An Amazon EC2 instance transitions through different states from the moment you launch it through to its termination.

The following illustration represents the transitions between instance states.

![The instance lifecycle.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/instance_lifecycle.png)


You can receive notifications when your instances change states. For more information, see [State change events for Amazon EC2 instances](monitoring-instance-state-changes.md).

## Billing by instance state
<a name="instance-billing-by-state"></a>

The following table provides a brief description of each instance state and indicates whether instance usage is billed. Some AWS resources, such as Amazon EBS volumes and Elastic IP addresses, incur charges regardless of the instance's state. For more information, see [Avoiding Unexpected Charges](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/checklistforunwantedcharges.html) in the *AWS Billing User Guide*.


| Instance state | Description | Instance usage billing | 
| --- | --- | --- | 
| `pending` | The instance is preparing to enter the `running` state. An instance enters the `pending` state when it is launched or when it is started after being in the `stopped` state. | Not billed | 
| `running` | The instance is running and ready for use. | Billed | 
| `stopping` | The instance is preparing to be stopped. | Not billed If you hibernate an instance, you're billed while the instance is in the `stopping` state.  | 
| `stopped` | The instance is shut down and cannot be used. The instance can be started at any time. | Not billed | 
| `shutting-down` | The instance is preparing to be terminated. | Not billed | 
| `terminated` | The instance has been permanently deleted and cannot be started. | Not billed Reserved Instances that applied to terminated instances are billed until the end of their term according to their payment option. For more information, see [Reserved Instances for Amazon EC2 overview](ec2-reserved-instances.md)  | 

## Pending instances
<a name="instance-launch"></a>

When you launch an instance, it enters the `pending` state. The instance type that you specified at launch determines the hardware of the host computer for your instance. The Amazon Machine Image (AMI) you specified at launch is used to boot the instance. After the instance is ready for you, it enters the `running` state. You can connect to your running instance and use it the way that you'd use a computer sitting in front of you.

As soon as your instance transitions to the `running` state, you're billed for each second, with a one-minute minimum, that you keep the instance running, even if the instance remains idle and you don't connect to it.

## Stopped instances
<a name="instance-stop-start"></a>

If your instance fails a status check or is not running your applications as expected, and if the root volume of your instance is an Amazon EBS volume, you can stop and start your instance to try to fix the problem.

When you stop your instance, it enters the `stopping` state, and then the `stopped` state. You are not charged for usage or data transfer fees for your instance when it is `stopped`. Charges are incurred for the storage of any Amazon EBS volumes. While your instance is in the `stopped` state, you can modify certain attributes of the instance, including the instance type.

When you start your instance, it enters the `pending` state, and the instance is moved to a new host computer (though in some cases, it remains on the current host). When you stop and start your instance, you lose any data on the instance store volumes attached to the previous host computer.

Your instance retains its private IPv4 address, which means that an Elastic IP address associated with the private IPv4 address or network interface remains associated with your instance. If your instance has an IPv6 address, it retains the IPv6 address.

Each time you transition an instance from `stopped` to `running`, you are charged per second when the instance is running, with a minimum of one minute per instance start.

For more details about stopping and starting an instance, see [Stop and start Amazon EC2 instances](Stop_Start.md).

## Hibernated instances
<a name="instance-hibernate"></a>

When you hibernate an instance, the operating system is signaled to perform hibernation (suspend-to-disk), which saves the contents from the instance memory (RAM) to your Amazon EBS root volume. The instance's Amazon EBS root volume and any attached Amazon EBS data volumes are persisted. When you start your instance, the Amazon EBS root volume is restored to its previous state and the RAM contents are reloaded. Previously attached data volumes are reattached and the instance retains its instance ID.

When you hibernate your instance, it enters the `stopping` state, and then the `stopped` state. You are not charged for usage for a hibernated instance when it is in the `stopped` state, but you are charged while it is in the `stopping` state, unlike when you [stop an instance](#instance-stop-start) without hibernating it. You are not charged for data transfer fees, but you are charged for the storage for any Amazon EBS volumes, including storage for the RAM data.

When you start your hibernated instance, it enters the `pending` state, and the instance is moved to a new host computer (though in some cases, it remains on the current host).

Your instance retains its private IPv4 address, which means that an Elastic IP address associated with the private IPv4 address or network interface is still associated with your instance. If your instance has an IPv6 address, it retains its IPv6 address.

For more information, see [Hibernate your Amazon EC2 instance](Hibernate.md).

## Rebooting instances
<a name="instance-reboot"></a>

You can reboot your instance using the Amazon EC2 console, a command line tool, and the Amazon EC2 API. We recommend that you use Amazon EC2 to reboot your instance instead of running the operating system reboot command from your instance.

Rebooting an instance is equivalent to rebooting an operating system. The instance remains on the same host computer and maintains its public DNS name, private IP address, and any data on its instance store volumes. It typically takes a few minutes for the reboot to complete, but the time it takes to reboot depends on the instance configuration.

Rebooting an instance doesn't start a new instance billing period; per second billing continues without a further one-minute minimum charge.

For more information, see [Reboot your Amazon EC2 instance](ec2-instance-reboot.md).

## Terminated instances
<a name="instance-termination"></a>

When you've decided that you no longer need an instance, you can terminate it. As soon as the status of an instance changes to `shutting-down` or `terminated`, you stop incurring charges for that instance.

If you enable termination protection, you can't terminate the instance using the console, CLI, or API.

After you terminate an instance, it remains visible in the console for a short while, and then the entry is automatically deleted. You can also describe a terminated instance using the CLI and API. Resources (such as tags) are gradually disassociated from the terminated instance, therefore may no longer be visible on the terminated instance after a short while. You can't connect to or recover a terminated instance. 

Each Amazon EBS-backed instance supports the `InstanceInitiatedShutdownBehavior` attribute, which controls whether the instance stops or terminates when you initiate shutdown from within the instance itself (for example, by using the **shutdown** command on Linux). The default behavior is to stop the instance. You can modify the setting of this attribute while the instance is running or stopped.

Each Amazon EBS volume supports the `DeleteOnTermination` attribute, which controls whether the volume is deleted or preserved when you terminate the instance it is attached to. The default is to delete the root volume and preserve any other EBS volumes.

For more information, see [Terminate Amazon EC2 instances](terminating-instances.md).

## Differences between instance states
<a name="lifecycle-differences"></a>

The following table summarizes the key differences between rebooting, stopping, hibernating, and terminating your instance.


| Characteristic | Reboot | Stop/start (Amazon EBS-backed instances only) | Hibernate (Amazon EBS-backed instances only) | Terminate | 
| --- | --- | --- | --- | --- | 
| Host computer | The instance stays on the same host computer. | The instance is moved to a new host computer (though in some cases, it remains on the current host). | The instance is moved to a new host computer (though in some cases, it remains on the current host). | None | 
| Private IPv4 address | The instance keeps its private IPv4 address. | The instance keeps its private IPv4 address. | The instance keeps its private IPv4 address. | None | 
| Public IPv4 address | The instance keeps its public IPv4 address. | The instance gets a new public IPv4 address, unless it has a secondary network interface or a secondary private IPv4 address that is associated with an Elastic IP address. | The instance gets a new public IPv4 address, unless it has a secondary network interface or a secondary private IPv4 address that is associated with an Elastic IP address. | None | 
| Elastic IP address (IPv4) | The Elastic IP address remains associated with the instance | The Elastic IP address remains associated with the instance | The Elastic IP address remains associated with the instance | The Elastic IP address is disassociated from the instance | 
| IPv6 address | The instance keeps its IPv6 address | The instance keeps its IPv6 address | The instance keeps its IPv6 address | None | 
| Instance store volumes | The data is preserved | The data is erased | The data is erased | The data is erased | 
| Root volume | The volume is preserved | The volume is preserved | The volume is preserved | The volume is deleted by default | 
| RAM (contents of memory) | The RAM is erased | The RAM is erased | The RAM is saved to a file on the root volume | The RAM is erased | 
| Billing | The instance billing hour doesn't change | You stop incurring charges for an instance as soon as its state changes to `stopping`. Each time an instance transitions from `stopped` to `running`, we start a new instance billing period, billing a minimum of one minute every time you start your instance. | You incur charges while the instance is in the `stopping` state, but stop incurring charges when the instance is in the `stopped` state. Each time an instance transitions from `stopped` to `running`, we start a new instance billing period, billing a minimum of one minute every time you start your instance. | You stop incurring charges for an instance as soon as its state changes to `shutting-down` | 

Operating system shutdown commands always terminate an instance with an instance store root volume. You can control whether operating system shutdown commands stop or terminate an instance with an EBS root volume. For more information, see [Change instance initiated shutdown behavior](Using_ChangingInstanceInitiatedShutdownBehavior.md).