

# Reserve capacity for hosts

Amazon Elastic VMware Service launches Amazon Elastic Compute Cloud (Amazon EC2) bare metal instances as the ESX hosts of your environment. To make sure that capacity is available when you add hosts, we recommend that you request an Amazon EC2 Capacity Reservation before you deploy.

## How Capacity Reservations work
<a name="plan-capacity-reservations"></a>

A Capacity Reservation reserves EC2 capacity for an instance type in one Availability Zone, for any duration. Create the reservation for the instance type of your hosts, in the Availability Zone of your Amazon EVS environment. An Amazon EVS environment runs in one Availability Zone. For more information, see [VPC and subnets](plan-network-supported.md#plan-network-supported-vpc).

You can create a Capacity Reservation at any time, and you can choose when it starts.

 **For immediate use**   
The reservation starts when you create it.

 **For a future date**   
You can request the reservation 5 to 120 days ahead. We recommend that you request it at least 8 weeks ahead. The minimum commitment is 14 days for most instance types.

**Important**  
Billing for a Capacity Reservation starts when the reservation becomes active, whether or not instances use it.

Each Capacity Reservation has instance matching criteria.

 **Open**   
An Open reservation is used automatically by any instance with matching attributes. Any matching instance in your account can use it, not only your Amazon EVS hosts.

 **Targeted**   
A Targeted reservation is used only by instances that explicitly target it.

You can create a future-dated reservation only as Targeted. After it becomes active, you can change it to Open.

For more information, see [Reserve compute capacity with EC2 On-Demand Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*. For the steps, see [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) in the *Amazon EC2 User Guide*.

## Capacity and quotas
<a name="plan-capacity-quotas"></a>

A Capacity Reservation reserves EC2 capacity. Your account also needs Amazon EVS and Amazon EC2 quotas that cover every host. For the quotas to check, see [Quotas to raise before you start](plan-sizing.md#plan-sizing-quotas).

## Keep a spare host
<a name="plan-capacity-spare-host"></a>

You’re responsible for monitoring host health and replacing failed hosts. When you replace a host, you add the new host before you remove the old one, so your environment needs capacity for one more host during the replacement.

If you use Capacity Reservations or EC2 Dedicated Hosts, we recommend that you keep a spare host for mission-critical workloads.
+ A Capacity Reservation gives you access to EC2 capacity in an Availability Zone. A spare host adds redundancy on top of that capacity.
+ With Dedicated Hosts, a spare host keeps your environment running for mission-critical workloads if a primary host needs maintenance or has an issue.

Include the spare host and any temporary host in the **Host count per EVS environment** quota and in your Capacity Reservation. For the quota, see [Service quotas for Amazon EVS](service-quotas-evs.md). For the replacement steps, see [Replace a failed host (Self-deployed)](host-replace.md).

## Release capacity that you no longer need
<a name="plan-capacity-release"></a>

When you delete hosts or an environment, cancel the Capacity Reservations that you no longer need, because they’re billed until you cancel them. For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

Next, choose your storage. See [Choose storage](plan-storage.md).