

# Host maintenance for Amazon EC2 Dedicated Host
<a name="dedicated-hosts-maintenance"></a>

With host maintenance, in the rare event that a Dedicated Host becomes degraded, Amazon EC2 automatically migrates instances running on it onto a healthy replacement Dedicated Host. This helps to minimize the downtime for your workload, and simplify the management of your Dedicated Hosts. Host maintenance is also performed for planned and routine Amazon EC2 maintenance.

Amazon EC2 supports two types of host maintenance:
+ **Live migration host maintenance** — Instances are automatically migrated to the replacement host within 24 hours, without stopping and restarting them.
+ **Reboot-based host maintenance** — Instances are scheduled for *instance reboot* scheduled events, during which they are automatically stopped and restarted on the replacement host.

**Topics**
+ [Host maintenance versus host recovery](#dedicated-hosts-maintenance-differences)
+ [Considerations](#dedicated-hosts-maintenance-basics-limitations)
+ [Related services](#dedicated-hosts-maintenance-related)
+ [Pricing](#dedicated-hosts-maintenance-pricing)
+ [How host maintenance works for Amazon EC2 Dedicated Hosts](dedicated-hosts-maintenance-basics.md)
+ [Configure the host maintenance setting for an Amazon EC2 Dedicated Host](dedicated-hosts-maintenance-configuring.md)

## Host maintenance versus host recovery
<a name="dedicated-hosts-maintenance-differences"></a>

The following table shows the main differences between host recovery and host maintenance.



|  | Host recovery | Host maintenance | 
| --- | --- | --- | 
| Instance reachability | Unreachable | Reachable | 
| Dedicated Host state | under-assessment | permanent-failure | 
| Host resource group | Supported | Not supported | 

For more information about host recovery, see [Host recovery](dedicated-hosts-recovery.md).

## Considerations
<a name="dedicated-hosts-maintenance-basics-limitations"></a>
+ Host maintenance is available in all AWS Regions, except the China Regions and AWS GovCloud (US) Regions.
+ Host maintenance is not supported in AWS Outposts, AWS Local Zones, and AWS Wavelength Zones.
+ Host maintenance can't be turned on or off for hosts already within a host resource group. Hosts added to a host resource group retain their host maintenance setting. For more information, see [Host resource groups](https://docs.aws.amazon.com/license-manager/latest/userguide/host-resource-groups.html).
+ Host maintenance is not supported with the following instance types, because they have instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1.

## Related services
<a name="dedicated-hosts-maintenance-related"></a>

Dedicated Host integrates with **AWS License Manager**—Tracks licenses across your Amazon EC2 Dedicated Hosts (supported only in Regions in which AWS License Manager is available). For more information, see the [AWS License Manager User Guide](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html).

You must have sufficient licenses in your AWS account for your new Dedicated Host. The licenses associated with your degraded host are released when the host is released after the completion of the scheduled event.

## Pricing
<a name="dedicated-hosts-maintenance-pricing"></a>

There are no additional charges for using host maintenance, but the usual Dedicated Host charges apply. For more information, see [ Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/).

As soon as host maintenance is initiated, you are no longer billed for the degraded Dedicated Host. Billing for the replacement Dedicated Host begins only after it enters the `available` state.

If the degraded Dedicated Host was billed using the On-Demand rate, the replacement Dedicated Host is also billed using the On-Demand rate. If the degraded Dedicated Host had an active Dedicated Host Reservation, it is transferred to the new Dedicated Host.