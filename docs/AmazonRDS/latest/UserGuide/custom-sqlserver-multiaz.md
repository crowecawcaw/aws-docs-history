# Prerequisites for a Multi-AZ deployment with RDS Custom for SQL Server

If you have an existing RDS Custom for SQL Server Single-AZ deployment, the following additional
prerequisites are required before modifying it to a Multi-AZ deployment. You can choose to complete
the prerequisites manually or with the provided CloudFormation template. The latest CloudFormation
template contains the prerequisites for both Single-AZ and Multi-AZ deployments.

###### Important

To simplify setup, we recommend that you use the latest CloudFormation template file provided
in the network setup instructions to create the prerequisites. For more information, see
[Configuring with CloudFormation](custom-setup-sqlserver.md#custom-setup-sqlserver.cf "custom-setup-sqlserver.md#custom-setup-sqlserver.cf").

###### Note

When you modify an existing RDS Custom for SQL Server Single-AZ deployment to a Multi-AZ deployment, you must
complete these prerequisites. If you don't complete the prerequisites, the Multi-AZ setup will fail. To complete
the prerequisites, follow the steps in [Modifying an RDS Custom for SQL Server Single-AZ deployment to a Multi-AZ deployment](custom-sqlserver-multiaz.md "custom-sqlserver-multiaz.md").

- Update the RDS security group inbound and outbound rules to allow port 1120.
- Add a rule in your private network Access Control List (ACL) that allows TCP ports `0-65535` for the DB instance VPC.
- Create new Amazon SQS VPC endpoints that allow the RDS Custom for SQL Server DB instance to communicate with SQS.
- Update the SQS permissions in the instance profile role.
