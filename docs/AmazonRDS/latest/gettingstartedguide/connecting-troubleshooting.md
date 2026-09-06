

# Troubleshooting connection issues to your Amazon RDS DB instance
<a name="connecting-troubleshooting"></a>

When you attempt to connect to an Amazon RDS DB instance, you might encounter common issues that prevent successful connections. This topic addresses several frequent connection problems, along with steps to identify and resolve them.

**Topics**
+ [Incorrect security group configuration](#connecting-troubleshooting-sg)
+ [Incorrect database endpoint and port](#connecting-troubleshooting-endpoint-port)
+ [Network ACLs blocking traffic](#connecting-troubleshooting-acls)
+ [Authentication errors](#connecting-troubleshooting-auth)
+ [VPC peering or network misconfigurations](#connecting-troubleshooting-network)
+ [Next steps](#connecting-troubleshooting-next-steps)

## Incorrect security group configuration
<a name="connecting-troubleshooting-sg"></a>

If the security group associated with your DB instance doesn't allow traffic from your client, connections will fail.

**Solution**:
+ Verify the security group rules in the Amazon EC2 console.
+ Ensure inbound rules allow traffic on the database port (3306 for MySQL, 5432 for PostgreSQL, and so on).
+ Add your client IP address or a CIDR block to the inbound rules.

For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html).

## Incorrect database endpoint and port
<a name="connecting-troubleshooting-endpoint-port"></a>

Using the wrong endpoint or port results in failed connection attempts.

**Solution**:
+ Retrieve the correct endpoint from the RDS console.
+ Make sure you're using the database's assigned port.
+ Check for typos in the connection string.

For more information, see [Finding the connection information for an RDS for MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.EndpointAndPort.html).

## Network ACLs blocking traffic
<a name="connecting-troubleshooting-acls"></a>

If Network Access Control Lists (NACLs) block traffic to or from the subnet, connection attempts fail.

**Solution**:
+ Check the NACLs associated with your subnet in the Amazon VPC console.
+ Make sure that inbound and outbound rules allow traffic on your database port.

For more information, see [Control subnet traffic with network access control lists](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/vpc-network-acls.html).

## Authentication errors
<a name="connecting-troubleshooting-auth"></a>

Using incorrect credentials or configuration errors in database authentication can result in failed logins.

**Solution**:
+ Confirm the username and password in your connection string.
+ Check IAM policies if you're using IAM authentication.

For more information, see [IAM database authentication for MariaDB, MySQL, and PostgreSQL ](https://docs.aws.amazon.com/vpc/latest/userguide/UsingWithRDS.IAMDBAuth.html).

## VPC peering or network misconfigurations
<a name="connecting-troubleshooting-network"></a>

Misconfigured peering connections or route tables might block communication between the client and the database.

**Solution**:
+ Verify that the VPC peering connection is active.
+ Check route tables to ensure traffic can flow between VPCs.
+ Make sure there are no overlapping IP ranges between VPCs.

For more information, see [Connect VPCs using VPC peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html).

## Next steps
<a name="connecting-troubleshooting-next-steps"></a>

If these steps don’t resolve your connection issues, consider enabling enhanced logging or contacting Support for further assistance. Additionally, explore the troubleshooting guides specific to your database engine:
+ [Troubleshooting connections to your MySQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.Troubleshooting.html)
+ [Troubleshooting connections to your PostgreSQL DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.Troubleshooting.html)