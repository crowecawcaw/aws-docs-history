

# Reserve compute capacity with EC2 On-Demand Capacity Reservations
<a name="ec2-capacity-reservations"></a>

Amazon EC2 Capacity Reservations allow you to reserve compute capacity for your Amazon EC2 instances in a specific Availability Zone for any duration. If you have strict capacity requirements for current or future business-critical workloads that require a certain level of long or short-term capacity assurance, we recommend that you create a Capacity Reservation to help ensure that you always have access to Amazon EC2 capacity when you need it, for as long as you need it.

You can create a Capacity Reservation at any time, and you can choose when it starts. You can request a Capacity Reservation for immediate use or you can request a Capacity Reservation for a future date.
+ If you request a **Capacity Reservation for immediate use**, the Capacity Reservation becomes available for use immediately and there is no term commitment. You can modify the Capacity Reservation at any time, and you can cancel it at any time to release the reserved capacity and to stop incurring charges.
+ If you request a **future-dated Capacity Reservation**, you specify when you need the capacity and how long you commit to keeping it. At the specified future date, the Capacity Reservation becomes available for use and billing starts. During the commitment duration, you can't decrease the instance count or commitment duration below your initial commitment. You can cancel the Capacity Reservation, but a cancellation charge might apply depending on when you cancel. After the commitment duration elapses, you can modify the Capacity Reservation in any way or cancel it without charge.

Capacity Reservations can only be used by instances that match their attributes. By default, Capacity Reservations automatically match new instances and running instances that have matching attributes (instance type, platform, Availability Zone, and tenancy). This means that any instance with matching attributes automatically runs in the Capacity Reservation. However, you can also target a Capacity Reservation for specific workloads. This allows you to explicitly control which instances are allowed to run in that reserved capacity. You can also specify that instances will only run in a Capacity Reservation or Capacity Reservation Resource Group.

**Important**  
Future-dated Capacity Reservations are for helping you launch and cover incremental instances, and not to cover existing running instances. If you need to cover existing running instances, use Capacity Reservations that start immediately instead.

All supported Amazon EC2 instances with matching attributes, that is instance type, platform, Availability Zone, and tenancy, are eligible to run in a Capacity Reservation. The Amazon EC2 instance can be launched by you (*non-managed instances*) or on your behalf by an AWS service (*managed instances*). This is particularly true for *open* Capacity Reservations, which automatically match with any running instances that have matching attributes. For example, managed instances launched on your behalf by the following services are eligible to run in Capacity Reservations that you create and manage.
+ Amazon EC2 Auto Scaling
+ Amazon ECS
+ Amazon EKS
+ Amazon EMR
+ AWS Batch
+ AWS Elastic Beanstalk
+ AWS ParallelCluster
+ AWS Parallel Computing Service (AWS PCS)

**Topics**
+ [Concepts for Amazon EC2 Capacity Reservations](cr-concepts.md)
+ [Differences between Capacity Reservations, Reserved Instances, and Savings Plans](#capacity-reservations-differences)
+ [Supported platforms](#capacity-reservations-platforms)
+ [Quotas](#capacity-reservations-limits)
+ [Limitations](#capacity-reservations-limitations)
+ [Capacity Reservation pricing and billing](capacity-reservations-pricing-billing.md)
+ [Create a Capacity Reservation](capacity-reservations-create.md)
+ [View the state of a Capacity Reservation](capacity-reservations-view.md)
+ [Launch instances into an existing Capacity Reservation](capacity-reservations-launch.md)
+ [Modify an active Capacity Reservation](capacity-reservations-modify.md)
+ [Modify the Capacity Reservation settings of your instance](capacity-reservations-modify-instance.md)
+ [Move capacity between Capacity Reservations](capacity-reservations-move.md)
+ [Split off capacity from an existing Capacity Reservation](capacity-reservations-split.md)
+ [Cancel a Capacity Reservation](capacity-reservations-release.md)
+ [Use Capacity Reservations with placement groups](cr-cpg.md)
+ [Capacity Reservations in Local Zones](capacity-reservations-localzones.md)
+ [Capacity Reservations in Wavelength Zones](capacity-reservations-wavelengthzones.md)
+ [Capacity Reservations on AWS Outposts](capacity-reservations-outposts.md)
+ [Shared Capacity Reservations](capacity-reservation-sharing.md)
+ [Capacity Reservation Fleets](cr-fleets.md)
+ [Monitor Capacity Reservations usage with CloudWatch metrics](capacity-reservation-cw-metrics.md)
+ [Monitor Capacity Reservation underutilization](cr-eventbridge.md)
+ [Monitor state changes for future-dated Capacity Reservations](monitor-fcr-state.md)
+ [Interruptible Capacity Reservations](interruptible-capacity-reservations.md)

## Differences between Capacity Reservations, Reserved Instances, and Savings Plans
<a name="capacity-reservations-differences"></a>

The following table highlights key differences between Capacity Reservations, Reserved Instances, and Savings Plans:


<table>
<thead>
  <tr><th></th><th>Capacity Reservations</th><th>Zonal Reserved Instances</th><th>Regional Reserved Instances</th><th>Savings Plans</th></tr>
</thead>
<tbody>
  <tr><td><b>Term</b></td><td>No commitment required for immediate-use Capacity Reservations. They can be created, modified, and canceled as needed.<br />With future-dated Capacity Reservations, you specify a commitment duration for which you commit to keeping the capacity in your account. You can cancel at any time; a cancellation charge might apply during the commitment duration.</td><td colspan="3">Requires a fixed one-year or three-year commitment</td></tr>
  <tr><td><b>Capacity benefit</b></td><td colspan="2">Capacity reserved in a specific Availability Zone.</td><td colspan="2">No capacity reserved.</td></tr>
  <tr><td><b>Billing discount</b></td><td>No billing discount. †</td><td colspan="3">Provides a billing discount.</td></tr>
  <tr><td><b>Instance Limits</b></td><td>Your On-Demand Instance limits per Region apply.</td><td>Default is 20 per Availability Zone. You can request a limit increase.</td><td>Default is 20 per Region. You can request a limit increase.</td><td>No limit.</td></tr>
</tbody>
</table>


† You can combine Capacity Reservations with Savings Plans or Regional Reserved Instances to receive a discount.

For more information, see the following:
+ [Reserved Instances for Amazon EC2 overview](ec2-reserved-instances.md)
+ [Savings Plans User Guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/)

## Supported platforms
<a name="capacity-reservations-platforms"></a>

You must create the Capacity Reservation with the correct platform to ensure that it properly matches with your instances. Capacity Reservations support the following values for `platform`:
+ Linux/UNIX
+ Linux with SQL Server Standard
+ Linux with SQL Server Web
+ Linux with SQL Server Enterprise
+ SUSE Linux
+ Red Hat Enterprise Linux
+ RHEL with SQL Server Standard
+ RHEL with SQL Server Enterprise
+ RHEL with SQL Server Web
+ RHEL with HA
+ RHEL with HA and SQL Server Standard
+ RHEL with HA and SQL Server Enterprise
+ Ubuntu Pro
+ Windows
+ Windows with SQL Server
+ Windows with SQL Server Web
+ Windows with SQL Server Standard
+ Windows with SQL Server Enterprise

To ensure that an instance runs in a specific Capacity Reservation, the platform of the Capacity Reservation must match the platform of the AMI used to launch the instance. For Linux AMIs, it is important to check whether the AMI platform uses the general value **Linux/UNIX** or a more specific value like **SUSE Linux**.

------
#### [ Console ]

**To check the AMI platform**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **AMIs**.

1. Select the AMI.

1. On the **Details** tab, note the value of **Platform details**.

------
#### [ AWS CLI ]

**To check the AMI platform**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command and check the value of `PlatformDetails`.

```
aws ec2 describe-images \
    --image-ids {{ami-0abcdef1234567890}} \
    --query Images[*].PlatformDetails
```

The following is example output.

```
[
    "Linux/UNIX"
]
```

------
#### [ PowerShell ]

**To check the AMI platform**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet and check the value of `PlatformDetails`.

```
(Get-EC2Image -ImageId {{ami-0abcdef1234567890}}).PlatformDetails
```

The following is example output.

```
Linux/UNIX
```

------

## Quotas
<a name="capacity-reservations-limits"></a>

The number of instances for which you are allowed to reserve capacity is based on your account's On-Demand Instance quota. You can reserve capacity for as many instances as that quota allows, minus the number of instances that are already running.

Capacity Reservations in the `assessing`, `scheduled`, `pending` , `active`, and `delayed` state count towards your On-Demand Instance quota.

## Limitations
<a name="capacity-reservations-limitations"></a>

Before you create Capacity Reservations, take note of the following limitations and restrictions.
+ Active and unused Capacity Reservations count toward your On-Demand Instance limits.
+ Capacity Reservations are not transferable from one AWS account to another. However, you can share Capacity Reservations with other AWS accounts. For more information, see [Shared Capacity Reservations](capacity-reservation-sharing.md).
+ Zonal Reserved Instance billing discounts do not apply to Capacity Reservations.
+ Capacity Reservations can be created in cluster placement groups. Spread and partition placement groups are not supported.
+ Capacity Reservations can't be used with Dedicated Hosts. Capacity Reservations can be used with Dedicated Instances.
+ [Windows instances] Capacity Reservations can't be used with Bring Your Own License (BYOL).
+ [Red Hat instances] Capacity Reservations can be used with Bring Your Own License (BYOL).
+ Capacity Reservations do not ensure that a hibernated instance can resume after you try to start it.
+ You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for `m5.xlarge` instances, you must request at least 8 instances (*8 \* m5.xlarge = 32 vCPUs*).
+ You can request future-dated Capacity Reservations for instance types in the following families: C, G, I, M, R, T, U, and X.