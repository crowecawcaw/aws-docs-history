# Adjusting database links

for use with DB instances in a VPC

To use Oracle database links with Amazon RDS DB instances inside the same virtual
private cloud (VPC) or peered VPCs, the two DB instances should have a valid route
between them. Verify the valid route between the DB instances by using your VPC
routing tables and network access control list (ACL).

The security group of each DB instance must allow ingress to and egress from the
other DB instance. The inbound and outbound rules can refer to security groups from
the same VPC or a peered VPC. For more information, see [Updating your security groups to reference peered VPC security groups](../../../vpc/latest/peering/working-with-vpc-peering.md#vpc-peering-security-groups "../../../vpc/latest/peering/working-with-vpc-peering.md#vpc-peering-security-groups").

If you have configured a custom DNS server using the DHCP Option Sets in your VPC,
your custom DNS server must be able to resolve the name of the database link target.
For more information, see [Setting up a custom DNS
server](Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.CustomDNS "Appendix.Oracle.CommonDBATasks.md#Appendix.Oracle.CommonDBATasks.CustomDNS").

For more information about using database links with Oracle Data Pump, see [Importing using Oracle Data Pump](Oracle.Procedural.Importing.md "Oracle.Procedural.Importing.md").
