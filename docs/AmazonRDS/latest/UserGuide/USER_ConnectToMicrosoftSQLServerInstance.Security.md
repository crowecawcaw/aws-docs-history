

# Security group considerations
<a name="USER_ConnectToMicrosoftSQLServerInstance.Security"></a>

To connect to your DB instance, your DB instance must be associated with a security group. This security group contains the IP addresses and network configuration that you use to access the DB instance. You might have associated your DB instance with an appropriate security group when you created your DB instance. If you assigned a default, no-configured security group when you created your DB instance, your DB instance firewall prevents connections.

In some cases, you might need to create a new security group to make access possible. For instructions on creating a new security group, see [Controlling access with security groups](Overview.RDSSecurityGroups.md). For a topic that walks you through the process of setting up rules for your VPC security group, see [Tutorial: Create a VPC for use with a DB instance (IPv4 only)](CHAP_Tutorials.WebServerDB.CreateVPC.md).

After you have created the new security group, modify your DB instance to associate it with the security group. For more information, see [Modifying an Amazon RDS DB instance](Overview.DBInstance.Modifying.md). 

You can enhance security by using SSL to encrypt connections to your DB instance. For more information, see [Using SSL with a Microsoft SQL Server DB instance](SQLServer.Concepts.General.SSL.Using.md). 