# Using a custom DNS server for outbound network access

RDS for PostgreSQL supports outbound network access on your DB instances and allows Domain
Name Service (DNS) resolution from a custom DNS server owned by the customer. You can
resolve only fully qualified domain names from your RDS for PostgreSQL DB instance through
your custom DNS server.

###### Topics

- [Turning on custom DNS resolution](#Appendix.PostgreSQL.CommonDBATasks.CustomDNS.Enable "#Appendix.PostgreSQL.CommonDBATasks.CustomDNS.Enable")
- [Turning off custom DNS resolution](#Appendix.PostgreSQL.CommonDBATasks.CustomDNS.Disable "#Appendix.PostgreSQL.CommonDBATasks.CustomDNS.Disable")
- [Setting up a custom DNS server](#Appendix.Oracle.CommonDBATasks.CustomDNS.Setup "#Appendix.Oracle.CommonDBATasks.CustomDNS.Setup")

## Turning on custom DNS resolution

To turn on DNS resolution in your customer VPC, first associate a custom DB
parameter group to your RDS for PostgreSQL instance. Then turn on the `rds.custom_dns_resolution` parameter by setting it to 1, and then restart
the DB instance for the changes to take place.

## Turning off custom DNS resolution

To turn off DNS resolution in your customer VPC, first turn off the `rds.custom_dns_resolution` parameter of your custom DB
parameter group by setting it to 0. Then restart the DB instance for the changes to
take place.

## Setting up a custom DNS server

After you set up your custom DNS name server, it takes up to 30 minutes to
propagate the changes to your DB instance. After the changes are propagated to your
DB instance, all outbound network traffic requiring a DNS lookup queries your DNS
server over port 53.

###### Note

If you don't set up a custom DNS server and `rds.custom_dns_resolution` is set to 1, hosts are resolved using an
Amazon Route 53 private zone. For more information, see [Working with
private hosted zones](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md").

###### To set up a custom DNS server for your RDS for PostgreSQL DB instance

1. From the Dynamic Host Configuration Protocol (DHCP) options set attached
   to your VPC, set the `domain-name-servers` option to the IP
   address of your DNS name server. For more information, see [DHCP options sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md").

###### Note

The `domain-name-servers` option accepts up to four values,
but your Amazon RDS DB instance uses only the first value. 2. Ensure that your DNS server can resolve all lookup queries, including
public DNS names, Amazon EC2 private DNS names, and customer-specific DNS names.
If the outbound network traffic contains any DNS lookups that your DNS
server can't handle, your DNS server must have appropriate upstream DNS
providers configured. 3. Configure your DNS server to produce User Datagram Protocol (UDP)
responses of 512 bytes or less. 4. Configure your DNS server to produce Transmission Control Protocol (TCP)
responses of 1,024 bytes or less. 5. Configure your DNS server to allow inbound traffic from your Amazon RDS DB
instances over port 53. If your DNS server is in an Amazon VPC, the VPC must have
a security group that contains inbound rules that allow UDP and TCP traffic
on port 53. If your DNS server is not in an Amazon VPC, it must have appropriate
firewall settings to allow UDP and TCP inbound traffic on port 53.

For more information, see [Security groups for your
VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") and [Adding and
removing rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#AddRemoveRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#AddRemoveRules"). 6. Configure the VPC of your Amazon RDS DB instance to allow outbound traffic over
port 53. Your VPC must have a security group that contains outbound rules
that allow UDP and TCP traffic on port 53.

For more information, see [Security groups for your
VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") and [Adding and
removing rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#AddRemoveRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#AddRemoveRules") in the _Amazon VPC User Guide_. 7. Make sure that the routing path between the Amazon RDS DB instance and the DNS
server is configured correctly to allow DNS traffic.

Also, if the Amazon RDS DB instance and the DNS server are not in the same VPC,
make sure that a peering connection is set up between them. For more
information, see [What is VPC
peering?](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md") in _Amazon VPC Peering Guide_.
