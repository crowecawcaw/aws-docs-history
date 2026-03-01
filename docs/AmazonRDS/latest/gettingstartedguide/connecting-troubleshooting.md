# Troubleshooting connection issues to your Amazon RDS DB instance

When you attempt to connect to an Amazon RDS DB instance, you might encounter common
issues that prevent successful connections. This topic addresses several frequent connection
problems, along with steps to identify and resolve them.

###### Topics

- [Incorrect security group configuration](#connecting-troubleshooting-sg "#connecting-troubleshooting-sg")
- [Incorrect database endpoint and port](#connecting-troubleshooting-endpoint-port "#connecting-troubleshooting-endpoint-port")
- [Network ACLs blocking traffic](#connecting-troubleshooting-acls "#connecting-troubleshooting-acls")
- [Authentication errors](#connecting-troubleshooting-auth "#connecting-troubleshooting-auth")
- [VPC peering or network misconfigurations](#connecting-troubleshooting-network "#connecting-troubleshooting-network")
- [Next steps](#connecting-troubleshooting-next-steps "#connecting-troubleshooting-next-steps")

## Incorrect security group configuration

If the security group associated with your DB instance doesn't allow traffic from your
client, connections will fail.

**Solution**:

- Verify the security group rules in the Amazon EC2 console.
- Ensure inbound rules allow traffic on the database port (3306 for MySQL, 5432 for
  PostgreSQL, and so on).
- Add your client IP address or a CIDR block to the inbound rules.

For more information, see [Controlling access
with security groups](../UserGuide/Overview.md "../UserGuide/Overview.md").

## Incorrect database endpoint and port

Using the wrong endpoint or port results in failed connection attempts.

**Solution**:

- Retrieve the correct endpoint from the RDS console.
- Make sure you're using the database's assigned port.
- Check for typos in the connection string.

For more information, see [Finding the connection
information for an RDS for MySQL DB instance](../UserGuide/USER_ConnectToInstance.md "../UserGuide/USER_ConnectToInstance.md").

## Network ACLs blocking traffic

If Network Access Control Lists (NACLs) block traffic to or from the subnet, connection
attempts fail.

**Solution**:

- Check the NACLs associated with your subnet in the Amazon VPC console.
- Make sure that inbound and outbound rules allow traffic on your database
  port.

For more information, see [Control subnet traffic with network
access control lists](../UserGuide/vpc-network-acls.md "../UserGuide/vpc-network-acls.md").

## Authentication errors

Using incorrect credentials or configuration errors in database authentication can
result in failed logins.

**Solution**:

- Confirm the username and password in your connection string.
- Check IAM policies if you're using IAM authentication.

For more information, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL](../../../vpc/latest/userguide/UsingWithRDS.md "../../../vpc/latest/userguide/UsingWithRDS.md") .

## VPC peering or network misconfigurations

Misconfigured peering connections or route tables might block communication between the
client and the database.

**Solution**:

- Verify that the VPC peering connection is active.
- Check route tables to ensure traffic can flow between VPCs.
- Make sure there are no overlapping IP ranges between VPCs.

For more information, see [Connect VPCs using VPC
peering](../../../vpc/latest/userguide/vpc-peering.md "../../../vpc/latest/userguide/vpc-peering.md").

## Next steps

If these steps don’t resolve your connection issues, consider enabling enhanced logging
or contacting Support for further assistance. Additionally, explore the troubleshooting guides
specific to your database engine:

- [Troubleshooting connections to your MySQL DB instance](../UserGuide/USER_ConnectToInstance.md "../UserGuide/USER_ConnectToInstance.md")
- [Troubleshooting connections to your PostgreSQL DB instance](../UserGuide/USER_ConnectToPostgreSQLInstance.md "../UserGuide/USER_ConnectToPostgreSQLInstance.md")
