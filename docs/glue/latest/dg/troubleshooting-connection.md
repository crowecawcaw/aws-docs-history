# Troubleshooting connection issues in

AWS Glue

When an AWS Glue crawler or a job uses connection properties to access a data store, you
might encounter errors when you try to connect.
AWS Glue uses private IP addresses in the subnet when it creates elastic network
interfaces in your specified virtual private cloud (VPC) and subnet. Security groups specified
in the connection are applied on each of the elastic network interfaces. Check to see whether
security groups allow outbound access and if they allow connectivity to the database cluster.

In addition, Apache Spark requires bidirectional connectivity among driver and executor
nodes. One of the security groups needs to allow ingress rules on all TCP ports. You can prevent
it from being open to the world by restricting the source of the security group to itself with a
self-referencing security group.

Here are some typical actions you can take to troubleshoot connection problems:

- Check the port address of your connection.
- Check the user name and password string in your connection or secret.
- For a JDBC data store, verify that it allows incoming connections.
- Verify that your data store can be accessed within your VPC.
- If you store your connection credentials using AWS Secrets Manager, make sure that your IAM role
  for AWS Glue has permission to access your secret. For more information, see [Example: Permission to retrieve secret values](../../../secretsmanager/latest/userguide/auth-and-access_examples.md#auth-and-access_examples_read "../../../secretsmanager/latest/userguide/auth-and-access_examples.md#auth-and-access_examples_read") in the _AWS Secrets Manager User Guide_. Depending on your network setup, you might also need to
  create a VPC endpoint to establish a private connection between your VPC and Secrets Manager. For more
  information, see [Using an AWS Secrets Manager VPC
  endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md").
