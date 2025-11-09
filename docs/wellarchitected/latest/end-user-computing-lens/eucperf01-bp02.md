# EUCPERF01-BP02 Consider the requirements of your Availability Zones when architecting

your AWS EUC services

Within each Region, only select Availability Zones support each AWS EUC service. This
is important if you are architecting solutions with extreme performance or security
requirements that demand that applications and desktops reside on the same subnet as the
user data they need to access.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

For the WorkSpaces service line, explore the Availability Zone information.

- [Amazon WorkSpaces Availability Zone Support](../../../workspaces/latest/adminguide/azs-workspaces.md "../../../workspaces/latest/adminguide/azs-workspaces.md")
- [Amazon WorkSpaces Secure Browser](../../../workspaces-web/latest/adminguide/availability-zones.md "../../../workspaces-web/latest/adminguide/availability-zones.md")

For WorkSpaces Applications, selecting a subnet when creating a new fleet automatically checks
if the associated Availability Zone can support the requested requirements, which are
based on several criteria such as instance type and availability.
