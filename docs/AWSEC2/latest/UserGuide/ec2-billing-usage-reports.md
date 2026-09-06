

# Understand codes for Amazon EC2 in billing and usage reports
<a name="ec2-billing-usage-reports"></a>

When you use Amazon EC2, we include related codes in your AWS billing and usage reports. Reviewing these codes helps you understand your costs and usage patterns for Amazon EC2. Tracking and managing your expenses is essential for optimizing your costs.

The following tables describe the codes for Amazon EC2 that appear in your billing and usage reports. For a list of the Region codes used in the billing and usage reports, see [AWS Region billing codes](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-region-billing-codes.html).

**Topics**
+ [Instances](#instances-billing-usage-reports)
+ [Bare metal instances](#bare-metal-instances-billing-usage-reports)
+ [Dedicated Hosts](#dedicated-hosts-billing-usage-reports)
+ [Dedicated Instances](#dedicated-instances-billing-usage-reports)
+ [EBS optimization](#ebs-billing-usage-reports)
+ [Capacity Reservations](#capacity-reservation-billing-usage-reports)

**Related resources**
+ [Amazon EC2 billing and purchasing options](instance-purchasing-options.md)
+ [Understand AMI billing information](ami-billing-info.md)
+ [Amazon EC2 pricing](https://aws.amazon.com/ec2/pricing/)

## Instances
<a name="instances-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-BoxUsage:{{instance-type}} | The running time for On-Demand Instances. | Hours | 
| {{region}}-HostBoxUsage:{{instance-type}} | The running time for instances on Dedicated Hosts. | Hours | 
| {{region}}-SpotUsage:{{instance-type}} | The running time for Spot Instances. | Hours | 



## Bare metal instances
<a name="bare-metal-instances-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-BoxUsage:{{instance-family}}.metal | The running time for bare metal On-Demand Instances. | Hours | 
| {{region}}-HostBoxUsage:{{instance-family}}.metal | The running time for bare metal instances on Dedicated Hosts. | Hours | 
| {{region}}-SpotUsage:{{instance-family}}.metal | The running time for bare metal Spot Instances. | Hours | 



## Dedicated Hosts
<a name="dedicated-hosts-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-HostUsage:{{host-type}} | The time that Dedicated Hosts are provisioned. | Hours | 
| {{region}}-ReservedHostUsage:{{host-type}} | The time that Dedicated Host Reservations are applied. | Hours | 



## Dedicated Instances
<a name="dedicated-instances-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-DedicatedUsage:{{instance-type}} | The running time for Dedicated Instances. | Hours \+ per-Region fee | 



## EBS optimization
<a name="ebs-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-EBSOptimized:{{instance-type}} | The time that EBS optimization is enabled. | Hours | 



## Capacity Reservations
<a name="capacity-reservation-billing-usage-reports"></a>


| Code | Description | Units | 
| --- | --- | --- | 
| {{region}}-Reservation:{{instance-type}} | The reserved instance time for Capacity Reservations. | Hours | 
| {{region}}-UnusedBox:{{instance-type}} | The unused reserved instance time for Capacity Reservations. | Hours | 
| {{region}}-DedicatedRes:{{instance-type}} | The reserved instance time for Dedicated Capacity Reservations. | Hours | 
| {{region}}-UnusedDed:{{instance-type}} | The unused reserved instance time for Dedicated Capacity Reservations. | Hours | 

