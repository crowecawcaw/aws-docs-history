# Set up an AWS DMS replication instance

To provision an AWS DMS replication instance, download the [DMS_CF.yaml template](https://aws-database-blog.s3.amazonaws.com/artifacts/mariadb-to-aurora-mysql-migration/DMS_CF.yaml "https://aws-database-blog.s3.amazonaws.com/artifacts/mariadb-to-aurora-mysql-migration/DMS_CF.yaml").

1. On the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/"), under **Services**, choose **CloudFormation**.
2. Choose **Create stack**.
3. For **Specify template**, choose **Upload a template file**.
4. Select **Choose File**.
5. Choose the `DMS_CF.yaml` file.
6. Choose **Next**.
7. On the **Specify Stack Details** page, edit the predefined values as needed, and then choose **Next**:
   - **Stack name** — Enter a name for the stack.
   - **AllocatedStorageSize** — Enter the storage size in GB. The default is 200 GB.
   - **DMSReplicationSubnetGroup** — Enter the subnet group for DMS replication.
   - **DMSSecurityGroup** — Enter the security group for DMS replication.
   - **InstanceType** — Enter the instance type.
   - **SourceDBPort** — Enter the source database port.
   - **SourceDatabaseName** — Enter the source database name.
   - **SourceServerName** — Enter the IP address of the source database server.
   - **SourceUsername** — Enter the source database user name.
   - **SourcePassword** — Enter the source database password.
   - **TargetDBPort** — Enter the target database port.
   - **TargetDatabaseName** — Enter the target database name.
   - **TargetServerName** — Enter the IP address of the target database server.
   - **TargetUsername** — Enter the target database user name.
   - **TargetPassword** — Enter the target database password.

8. On the **Configure stack options** page, for **Tags**, specify any optional tags, and then choose **Next**.
9. On the **Review** page, choose **I acknowledge that AWS CloudFormation might create IAM resources**.
10. Choose **Create Stack**.
    This AWS CloudFormation template creates a replication instance named `mariadb-mysql`. This replication instance has a source endpoint named `maria-on-prem` and a target endpoint named `mysqltrg-rds`. This target endpoint has extra connection attributes to disable foreign key constraint checks during the AWS DMS replication, as shown following.

```
ExtraConnectionAttributes : "initstmt=SET FOREIGN_KEY_CHECKS=0;parallelLoadThreads=1"
```
