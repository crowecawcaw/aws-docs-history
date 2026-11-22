

# Host maintenance and retirement events

Amazon Elastic VMware Service hosts run on EC2 bare metal instances, and AWS performs scheduled maintenance on these instances. You’re responsible for the VMware Cloud Foundation (VCF) software on the host, for monitoring host health, and for replacing a host before a scheduled event or after a host failure. What a scheduled event does to your data depends on whether the host has local storage or is diskless.

For more information about managing ESX hosts in VCF, see the [Broadcom documentation for VCF 9.x](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html), or [Host Management](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin.html) in the Broadcom documentation for VCF 5.2.x.

## Checking health of the underlying EC2 instance
<a name="evs-host-ec2-instance-health"></a>

Amazon EC2 runs automated status checks on every running instance, and you can create a CloudWatch alarm that warns you when a check fails. For the steps, see [Monitor hosts and VCF](monitor-observability.md).

## About AWS scheduled maintenance for EC2 instances
<a name="evs-host-maintenance-about"></a>

 AWS performs scheduled maintenance on the underlying EC2 instances for reliability, availability, and performance. EC2 bare metal instances are subject to the same types of scheduled events as other EC2 instances. AWS can schedule events to reboot, stop, and retire your instances because of underlying hardware issues or scheduled maintenance. These events don’t occur often. For more information, see [Types of scheduled events](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html#types-of-scheduled-events) in the *Amazon EC2 User Guide*.

If a scheduled event affects one of your instances, AWS notifies you in advance. AWS sends an email to the address that’s associated with your AWS account, and sends an AWS Health event. To route these events to your team with Amazon EventBridge, see [Get notified about host events](monitor-notifications.md). For more information about the events, see [Scheduled events for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html) in the *Amazon EC2 User Guide*.

You can reschedule an event so that it occurs at a date and time that suits you, up to the event deadline. For more information, see [Reschedule a scheduled event for an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reschedule-event.html) in the *Amazon EC2 User Guide*.

**Important**  
Before a scheduled reboot event, place the host in maintenance mode in the vSphere Client.

## Preparing for AWS scheduled `system-maintenance` and `instance-retirement` events
<a name="evs-host-preparing-aws-scheduled-maintenance"></a>

 AWS schedules two types of `system-maintenance` events, network maintenance and power maintenance.
+ During network maintenance, the scheduled instances lose network connectivity for a brief period. Normal network connectivity is restored after maintenance is complete.
+ During power maintenance, the scheduled instances are taken offline for a brief period, and then rebooted. When EC2 reboots a bare metal instance that has instance store volumes, the instance store data is not preserved.

 AWS schedules EC2 `instance-retirement` events when it detects degradation of the underlying hardware that hosts your instances.

The following table shows how to respond by host storage type.


| Host storage | VCF version | What to do | 
| --- | --- | --- | 
| Local storage (vSAN on instance store volumes) | VCF 5.2.x and VCF 9.x | Replace the host with a new host before the event occurs. If you wait for the event and EC2 must reboot the instance, you lose the vSAN data that’s stored on the instance store volumes. | 
| Diskless hosts | VCF 9.x | Diskless hosts have no instance store volumes, and your data stays on your external storage. | 

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

### Replace an Amazon EVS host
<a name="evs-replace-host"></a>

The replacement procedure depends on the deployment mode.
+ For Self-deployed environments that run VCF 9.x, see [Replace a failed host (Self-deployed)](host-replace.md).
+ For EVS-deployed environments (VCF 5.2.x), see [Replace a host (EVS-deployed)](host-replace-evs-deployed.md).

## Why EC2 automatic recovery doesn’t apply
<a name="evs-host-auto-recovery"></a>

Amazon EC2 offers two kinds of instance recovery.
+ Simplified automatic recovery doesn’t support metal instance sizes, and doesn’t support instances that attach instance store volumes at launch.
+ CloudWatch action-based recovery supports metal instances, but instance store data isn’t preserved. On hosts with local storage, vSAN keeps its data on the instance store volumes.

For more information, see [Automatic instance recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) in the *Amazon EC2 User Guide*. Don’t configure a recover action for an Amazon EVS host. Replace a failed or retiring host instead.

## Using EC2 On-Demand Capacity Reservations
<a name="evs-host-maintenance-odcr"></a>

You can use EC2 On-Demand Capacity Reservations to make sure that your cluster has enough capacity during maintenance periods. You can reserve capacity in a specific Availability Zone for any duration. For the reservation settings that Amazon EVS hosts use, see [Reserve capacity for hosts](plan-capacity.md). For more information, see [Reserve compute capacity with EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) and [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) in the *Amazon EC2 User Guide*.

A Capacity Reservation gives you access to EC2 capacity in an Availability Zone, and a spare host adds a layer of redundancy. With Dedicated Hosts, a spare host keeps your mission-critical workloads running if a host needs maintenance or has an issue.

**Note**  
If you use EC2 On-Demand Capacity Reservations or EC2 Dedicated Hosts, we recommend that you keep a spare host for mission-critical workloads.

## Troubleshooting
<a name="evs-maintenance-troubleshooting"></a>

For host problems, such as cluster image remediation failures and commissioning validation failures, see [Troubleshoot hosts](troubleshoot-hosts.md). For who to contact, AWS Support or Broadcom, see [Get help from AWS Support and Broadcom](get-help.md).