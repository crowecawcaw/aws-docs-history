# EUCSEC10-BP02 Restrict access to open ports on instances to reduce risks

Restrict use of network ports on end user systems to reduce the
potential exposure surface of these systems. Block network ports
that aren't required for the operation and support of end user
systems using host-based or network firewalls.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Implement networking security controls on Amazon EUC
instances. AWS provides several services and capabilities that
can help you secure AWS EUC instances for Amazon WorkSpaces
and AppStream 2.0. In addition to these services, consider OS
capabilities and additional software to provide the required
level of security.

For AWS networking, the following services and features should
be evaluated: 

- Network ACLs
- Security groups
- AWS Network Firewall
- NAT Gateway

Consider these services to create a baseline of network
security. Additionally, review and explore
[best
practices for VPC and networking in WorkSpaces](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf "https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf"), as well
as
[best practices for deploying AppStream 2.0](../../../whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-deploying-amazon-appstream-2.md "../../../whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-deploying-amazon-appstream-2.md"), as you evaluate
your network security.

In addition to AWS security capabilities and services, when
users require access to the Internet from browsers installed
in Amazon WorkSpaces or AppStream 2.0 instances, consider
using a web proxy to log web site access and implement
restrictions on where users can browse.

In Amazon WorkSpaces and AppStream 2.0 instances, consider
existing OS software to harden the instances. For example, you
can use host-based firewalls available within the operating
system to restrict accessible ports in your instances. In
addition, consider endpoint protection software to identify
and mitigate security risks that may be introduced into the
environment using software local to the instances. For detail
on the ports required by Amazon WorkSpaces and AppStream 2.0,
see the following:

- [List of ports required by Amazon AppStream 2.0](../../../appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.md "../../../appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.md")
- [List
  of ports required for Amazon WorkSpaces](../../../workspaces/latest/adminguide/workspaces-port-requirements.md "../../../workspaces/latest/adminguide/workspaces-port-requirements.md")
