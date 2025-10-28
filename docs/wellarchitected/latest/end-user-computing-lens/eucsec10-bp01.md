# EUCSEC10-BP01 Implement network separation for AWS EUC instances

Separating end user systems from infrastructure, application
servers, and data at the network level verifies that you can
enforce minimal access between systems to help prevent
unauthorized access to data and applications.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Enforce network separation between user instances and other
services. EUC instances provided by Amazon WorkSpaces or
AppStream 2.0 usually have network connectivity to other
workloads in the same network subnet. The use of security
groups within VPCs can restrict lateral movement and are
recommended for implementation. For defense-in-depth, non-end
user instances such as application servers, authentication
providers, and other infrastructure services should reside on
subnets different to those where user instances reside.

You can apply security controls to the non-end user instances
at various points using AWS capabilities, such as separate AWS accounts and VPCs, VPC endpoints, proxy servers, and network
firewalls. Review network security best practices for
[WorkSpaces](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf "https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf")
and

[AppStream
2.0](../../../appstream2/latest/developerguide/what-is-appstream.md "../../../appstream2/latest/developerguide/what-is-appstream.md") to improve security posture in your EUC
environment.
