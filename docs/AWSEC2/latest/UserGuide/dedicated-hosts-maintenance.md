# Host maintenance for Amazon EC2 Dedicated Host

With host maintenance, in the rare event that a Dedicated Host becomes degraded, we automatically
migrate instances running on it onto a healthy replacement Dedicated Host. This helps to minimize
the downtime for your workload, and simplify the management of your Dedicated Hosts. Host maintenance
is also performed for planned and routine Amazon EC2 maintenance.

Amazon EC2 supports two types of host maintenance:

- **Live migration host maintenance** — Instances
  are automatically migrated to the replacement host within 24 hours, without stopping
  and restarting them.
- **Reboot-based host maintenance** — Instances
  are scheduled for _instance reboot_ scheduled events, during which
  they are automatically stopped and restarted on the replacement host.

###### Contents

- [Host maintenance versus host recovery](#dedicated-hosts-maintenance-differences "#dedicated-hosts-maintenance-differences")
- [Considerations](#dedicated-hosts-maintenance-basics-limitations "#dedicated-hosts-maintenance-basics-limitations")
- [Related services](#dedicated-hosts-maintenance-related "#dedicated-hosts-maintenance-related")
- [Pricing](#dedicated-hosts-maintenance-pricing "#dedicated-hosts-maintenance-pricing")
- [How host maintenance works for Amazon EC2 Dedicated Hosts](dedicated-hosts-maintenance-basics.md "dedicated-hosts-maintenance-basics.md")
- [Configure the host maintenance setting for an Amazon EC2 Dedicated Host](dedicated-hosts-maintenance-configuring.md "dedicated-hosts-maintenance-configuring.md")

## Host maintenance versus host recovery

The following table shows the main differences between host recovery and host maintenance.

|                       | Host recovery      | Host maintenance    |
| --------------------- | ------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Instance reachability | Unreachable        | Reachable           |
| Dedicated Host state  | `under-assessment` | `permanent-failure` |
| Host resource group   | Supported          | Not supported       | For more information about host recovery, see [Host recovery](dedicated-hosts-recovery.md "dedicated-hosts-recovery.md"). ## Considerations <br>• Host maintenance is available in all AWS Regions, except the China Regions and AWS GovCloud (US) Regions. <br>• Host maintenance is not supported in AWS Outposts, AWS Local Zones, and AWS Wavelength Zones. <br>• Host maintenance can't be turned on or off for hosts already within a host resource group. Hosts added to a host resource group retain their host maintenance setting. For more information, see [Host resource groups](../../../license-manager/latest/userguide/host-resource-groups.md "../../../license-manager/latest/userguide/host-resource-groups.md"). <br>• Host maintenance is not supported with the following instance types, because they have instance store root volumes: C1, C3, D2, I2, M1, M2, M3, R3, and X1. ## Related services Dedicated Host integrates with **AWS License Manager**—Tracks licenses across your Amazon EC2 Dedicated Hosts (supported only in Regions in which AWS License Manager is available). For more information, see the [AWS License Manager User Guide](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md"). You must have sufficient licenses in your AWS account for your new Dedicated Host. The licenses associated with your degraded host are released when the host is released after the completion of the scheduled event. ## Pricing There are no additional charges for using host maintenance, but the usual Dedicated Host charges apply. For more information, see [Amazon EC2 Dedicated Hosts Pricing](https://aws.amazon.com/ec2/dedicated-hosts/pricing/ "https://aws.amazon.com/ec2/dedicated-hosts/pricing/"). As soon as host maintenance is initiated, you are no longer billed for the degraded Dedicated Host. Billing for the replacement Dedicated Host begins only after it enters the `available` state. If the degraded Dedicated Host was billed using the On-Demand rate, the replacement Dedicated Host is also billed using the On-Demand rate. If the degraded Dedicated Host had an active Dedicated Host Reservation, it is transferred to the new Dedicated Host. |
