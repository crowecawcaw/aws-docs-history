# EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service

management connections

AppStream 2.0 instances use a dedicated management network interface (eth0) for
streaming and service management connections.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Do not configure applications or the operating system to interfere with the
connections listed in [Amazon AppStream 2.0 Connections to Your VPC](../../../appstream2/latest/developerguide/appstream2-port-requirements-appstream2.md#management_ports "../../../appstream2/latest/developerguide/appstream2-port-requirements-appstream2.md#management_ports"). If private network connectivity
from AppStream 2.0 instances to resources outside your VPC is required, use a VPC-level
solution such as AWS Site-to-Site VPN or AWS Transit Gateway. Do not use a client VPN on the AppStream 2.0
instance, as this is complex and error-prone to configure properly.

WorkSpaces instances use a dedicated management network interface (eth0) for streaming and
service management connections.
