

# Performing common system tasks for Oracle DB instances
<a name="Appendix.Oracle.CommonDBATasks.System"></a>

Following, you can find how to perform certain common DBA tasks related to the system on your Amazon RDS DB instances running Oracle. To deliver a managed service experience, Amazon RDS doesn't provide shell access to DB instances, and restricts access to certain system procedures and tables that require advanced privileges. 

**Topics**
+ [Disconnecting a session](Appendix.Oracle.CommonDBATasks.DisconnectingSession.md)
+ [Terminating a session](Appendix.Oracle.CommonDBATasks.KillingSession.md)
+ [Canceling a SQL statement in a session](Appendix.Oracle.CommonDBATasks.CancellingSQL.md)
+ [Enabling and disabling restricted sessions](Appendix.Oracle.CommonDBATasks.RestrictedSession.md)
+ [Flushing the shared pool](Appendix.Oracle.CommonDBATasks.FlushingSharedPool.md)
+ [Granting SELECT or EXECUTE privileges to SYS objects](Appendix.Oracle.CommonDBATasks.TransferPrivileges.md)
+ [Revoking SELECT or EXECUTE privileges on SYS objects](Appendix.Oracle.CommonDBATasks.RevokePrivileges.md)
+ [Managing RDS\_X$ views for Oracle DB instances](Appendix.Oracle.CommonDBATasks.X-dollar.md)
+ [Granting privileges to non-master users](Appendix.Oracle.CommonDBATasks.PermissionsNonMasters.md)
+ [Creating custom functions to verify passwords](Appendix.Oracle.CommonDBATasks.CustomPassword.md)
+ [Setting up a custom DNS server](#Appendix.Oracle.CommonDBATasks.CustomDNS)
+ [Setting and unsetting system diagnostic events](Appendix.Oracle.CommonDBATasks.SystemEvents.md)

## Setting up a custom DNS server
<a name="Appendix.Oracle.CommonDBATasks.CustomDNS"></a>

Amazon RDS supports outbound network access on your DB instances running Oracle. For more information about outbound network access, including prerequisites, see [Configuring UTL\_HTTP access using certificates and an Oracle wallet](Oracle.Concepts.ONA.md). 

Amazon RDS Oracle allows Domain Name Service (DNS) resolution from a custom DNS server owned by the customer. You can resolve only fully qualified domain names from your Amazon RDS DB instance through your custom DNS server. 

After you set up your custom DNS name server, it takes up to 30 minutes to propagate the changes to your DB instance. After the changes are propagated to your DB instance, all outbound network traffic requiring a DNS lookup queries your DNS server over port 53. 

To set up a custom DNS server for your Amazon RDS for Oracle DB instance, do the following: 
+ From the DHCP options set attached to your virtual private cloud (VPC), set the `domain-name-servers` option to the IP address of your DNS name server. For more information, see [DHCP options sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html). 
**Note**  
The `domain-name-servers` option accepts up to four values, but your Amazon RDS DB instance uses only the first value. 
+ Ensure that your DNS server can resolve all lookup queries, including public DNS names, Amazon EC2 private DNS names, and customer-specific DNS names. If the outbound network traffic contains any DNS lookups that your DNS server can't handle, your DNS server must have appropriate upstream DNS providers configured. 
+ Configure your DNS server to produce User Datagram Protocol (UDP) responses of 512 bytes or less. 
+ Configure your DNS server to produce Transmission Control Protocol (TCP) responses of 1024 bytes or less. 
+ Configure your DNS server to allow inbound traffic from your Amazon RDS DB instances over port 53. If your DNS server is in an Amazon VPC, the VPC must have a security group that contains inbound rules that permit UDP and TCP traffic on port 53. If your DNS server is not in an Amazon VPC, it must have appropriate firewall allow-listing to permit UDP and TCP inbound traffic on port 53.

  For more information, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) and [Adding and removing rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#AddRemoveRules). 
+ Configure the VPC of your Amazon RDS DB instance to allow outbound traffic over port 53. Your VPC must have a security group that contains outbound rules that allow UDP and TCP traffic on port 53. 

  For more information, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) and [Adding and removing rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#AddRemoveRules). 
+ The routing path between the Amazon RDS DB instance and the DNS server has to be configured correctly to allow DNS traffic. 
  + If the Amazon RDS DB instance and the DNS server are not in the same VPC, a peering connection has to be set up between them. For more information, see [What is VPC peering?](https://docs.aws.amazon.com/vpc/latest/peering/Welcome.html) 