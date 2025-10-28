For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Configuring a DB instance

This section shows how to set up your Amazon Timestream for InfluxDB DB instance. Before creating a DB instance,
decide on the DB instance class that will run the DB instance. Also, decide where the DB instance will run by choosing an AWS Region.
Next, create the DB instance.

You can configure a DB instance with a DB parameter group.A DB parameter group acts as a container for engine configuration values that are applied to one or more DB instances.

The parameters that are available depend on the DB engine and DB engine version. You can specify a DB parameter group when you create a DB instance. You can also modify a DB instance to specify them.

###### Important

At this time, you can't modify compute (Instance types) and Storage (Storage Types) configuration of existing instances.

## Creating a DB instance

###### Using the console

1. Sign in to the AWS Management Console and open [Amazon Timestream for InfluxDB](https://console.aws.amazon.com/timestream/ "https://console.aws.amazon.com/timestream/").
2. In the upper-right corner of the Amazon Timestream for InfluxDB console, choose the AWS Region in which you want
   to create the DB instance.
3. In the navigation pane, choose **InfluxDB Databases**.
4. Choose **Create Influx database**.
5. For **DB Instance Identifier**. enter a name that will identify your instance.
6. Provide the InfluxDB basic configuration parameters **User Name, Organization, Bucket Name and Password**.

###### Important

Your user name, organization, bucket name and password will be stored as a secret in AWS Secrets Manager
that will be created for your account.

If you need to change the user password after the DB instance is available, you can modify using the
[Influx CLI](https://docs.influxdata.com/influxdb/v2/admin/users/change-password/ "https://docs.influxdata.com/influxdb/v2/admin/users/change-password/"). 7. 8. For **DB Instance Class**,
select an instance size that better fit your workload needs. 9. For **DB Storage Class**,
select a storage class that fits your need. In all cases, you will only need to configure the allocated storage. 10. In the **Connectivity configuration** section,
make sure your InfluxDB instance is in the same subnet as your new the clients that require connectivity to your Timestream for InfluxDB DB instance. You could also chose to make your DB instance publicly available. 11. Choose **Create Influx database**. 12. In the **Databases** list, choose the name
of your new InfluxDB instance to show its details.
The DB Instance has a status of **Creating** until is ready to use. 13. When the status changes to **Available**, you can connect to
the DB instance. Depending on the DB instance class and the amount of storage,
it can take up to 20 minutes before the new instance is available.

**Using the CLI**

To create a DB instance by using the AWS Command Line Interface, call the `create-db-instance` command with the following parameters:

```
--name
--vpc-subnet-ids
--vpc-security-group-ids
--db-instance-type
--db-storage-type
--username
--organization
--password
--allocated-storage

```

For information about each setting, see [Settings for DB instances](#timestream-for-influx-configuring-create-db-settings "#timestream-for-influx-configuring-create-db-settings").

###### Example: Using default engine configs

For Linux, macOS, or Unix:

```
aws timestream-influxdb create-db-instance \
    --name myinfluxDbinstance \
    --allocated-storage 400 \
    --db-instance-type db.influx.4xlarge \
    --vpc-subnet-ids subnetid1 subnetid2
    --vpc-security-group-ids mysecuritygroup \
    --username masterawsuser \
    --password \
    --db-storage-type InfluxIOIncludedT2
```

For Windows:

```
aws timestream-influxdb create-db-instance \
    --name myinfluxDbinstance \
    --allocated-storage 400 \
    --db-instance-type db.influx.4xlarge \
    --vpc-subnet-ids subnetid1 subnetid2
    --vpc-security-group-ids mysecuritygroup \
    --username masterawsuser \
    --password \
    --db-storage-type InfluxIOIncludedT2
```

**Using the API**

To create a DB instance by using the AWS Command Line Interface, call the `CreateDBInstance` command with the following parameters:

For information about each setting, see [Settings for DB instances](#timestream-for-influx-configuring-create-db-settings "#timestream-for-influx-configuring-create-db-settings").

###### Important

Part of the DBInstance response object you receive an influxAuthParametersSecretArn.
This will hold an ARN to a SecretsManager secret in your account.
It will only be populated after your InfluxDB DB instances is available.
The secret contains influx authentication parameters provided during the `CreateDbInstance` process.
This is a READONLY copy as any updates/modifications/deletions to this secret doesn't impact the created
DB instance. If you delete this secret, our API response will still refer to the deleted secret ARN.

Once you have finished creating your Timestream for InfluxDB DB instance, we recommend you download, install and configure the Influx CLI.

The influx CLI provides a simple way to interact with InfluxDB from a command line. For detailed installation and setup instructions, see [Use the Influx CLI](https://docs.influxdata.com/influxdb/v2/tools/influx-cli/ "https://docs.influxdata.com/influxdb/v2/tools/influx-cli/").

## Settings for DB instances

You can create a DB instance using the console, the `create-db-instance` CLI command, or the `CreateDBInstance` Timestream for InfluxDB API operation.

The following table provides details about settings that you choose when you create a DB instance.

| Console Setting               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | CLI option and Timestream API parameter                           |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Allocated storage             | The amount of storage to allocate for your DB instance (in gibibytes). In some cases, allocating a higher amount of storage for your DB instance than the size of your database can improve I/O performance. For more information, see [InfluxDB instance storage](timestream-for-influxdb.md#timestream-for-influx-dbi-storage "timestream-for-influxdb.md#timestream-for-influx-dbi-storage").                                                                                                                                                                                                                                                                                                                                                                                                               | CLI: `allocated-storage` API: `allocatedstorage`                  |
| Bucket Name                   | A name for the bucket to initialize the InfluxDb instance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | CLI: `bucket` API: `bucket`                                       |
| DB instance type              | The configuration for your DB instance. For example, a db.influx.large DB instance class has 16 GiB memory, 2 vCPUs, memory optimized. If possible, choose a DB instance type large enough that a typical query working set can be held in memory. When working sets are held in memory, the system can avoid writing to disk, which improves performance. For more information, see [DB instance class types](timestream-for-influxdb.md#timestream-for-influx-dbi-classtypes "timestream-for-influxdb.md#timestream-for-influx-dbi-classtypes").                                                                                                                                                                                                                                                             | CLI: `db-instance-type` API: `Dbinstancetype`                     |
| DB instance identifier        | The name for your DB instance. Name your DB instances in the same way that you name your on-premises servers. Your DB instance identifier can contain up to 63 alphanumeric characters, and must be unique for your account in the AWS Region you chose.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | CLI: `db-instance-identifier` API: `Dbinstanceidentifier`         |
| DB parameter group            | A parameter group for your DB instance. You can choose the default parameter group, or you can create a custom parameter group. For more information, see [Working with DB parameter groups](timestream-for-influx-db-connecting.md#timestream-for-influx-working-with-parameter-groups "timestream-for-influx-db-connecting.md#timestream-for-influx-working-with-parameter-groups")..                                                                                                                                                                                                                                                                                                                                                                                                                        | CLI: `db-parameter-group-name` API: `DBParameterGroupName`        |
| Log Delivery Setting          | The name of the S3 bucket were the InfluxDB logs will be stored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | CLI: `LogDeliveryConfiguration` API: `log-delivery-configuration` |
| Multi-AZ deployment           | Create a standby instance to create a passive secondary replica of your DB instance in another Availability Zone for failover support. We recommend Multi-AZ for production workloads to maintain high availability. For development and testing, you can choose Do not create a standby instance. For more information, see [Configuring and managing a multi-AZ deployment](timestream-for-influx-managing-multi-az.md "timestream-for-influx-managing-multi-az.md").                                                                                                                                                                                                                                                                                                                                        | CLI: `MultiAz` API: `multi-az`                                    |
| Network Type                  | The IP addressing protocols supported by the DB instance. IPv4 (the default) to specify that resources can communicate with the DB instance only over the Internet Protocol version 4 (IPv4) addressing protocol. Dual-stack mode to specify that resources can communicate with the DB instance over IPv4, Internet Protocol version 6 (IPv6), or both. Use dual-stack mode if you have any resources that must communicate with your DB instance over the IPv6 addressing protocol. Also, make sure that you associate an IPv6 CIDR block with all subnets in the DB subnet group that you specify. While IPv6 is public by default, we do support private IPv6 endpoints, keep in mind that this is a one way door since we do not support changing the _Publicly Accessible_ flag after instance creation. | CLI: `network-type` API: `NetworkType`                            |
| Password                      | This will be your master use password use to Initialize your InfluxDB Db instance. You will use this password to log in into the InfluxUI to obtain your operator token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | CLI: `password` API: `password`                                   |
| Public Access                 | Yes to give the DB instance a public IP address, meaning that it's accessible outside the VPC. To be publicly accessible, the DB instance also has to be in a public subnet in the VPC. No to make the DB instance accessible only from inside the VPC. To connect to a DB instance from outside of its VPC, the DB instance must be publicly accessible. Also, access must be granted using the inbound rules of the DB instance's security group. In addition, other requirements must be met.                                                                                                                                                                                                                                                                                                               | CLI: `publicly-accessible` API: `PubliclyAccessible`              |
| Storage Type                  | The storage type for your DB instance You can choose between 3 different types Provisioned influx IOPS Included storage according to your workloads requirements: \* Influx IOPS Included 3000 IOPS \* Influx IOPS Included 12000 IOPS \* INflux IOPS Included 16000 IOPS For more information, see [InfluxDB instance storage](timestream-for-influxdb.md#timestream-for-influx-dbi-storage "timestream-for-influxdb.md#timestream-for-influx-dbi-storage").                                                                                                                                                                                                                                                                                                                                                  | CLI: `db-storage-type` API: `DbStorageType`                       |
| Initial username              | This will be the master user to initialize your InfluxDB DB instance with. You will use this username to log in into the InfluxUI to obtain your operator token.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | CLI: `username` API: `Username`                                   |
| Subnets                       | A vpc subnet to associate with this DB instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | CLI: `vpc-subnet-ids` API: `VPCSubnetIds`                         |
| VPC Security Group (firewall) | The security group to associate with the DB instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | CLI: `vpc-security-group-ids` API: `VPCSecurityGroupIds`          |
