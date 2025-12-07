# Using Redis OSS as a target for

AWS Database Migration Service

Redis OSS is an open-source in-memory data structure store used as a database, cache, and
message broker. Managing data in-memory can result in read or write operations taking
less than a millisecond, and hundreds of millions of operations performed each second. As an
in-memory data store, Redis OSS powers the most demanding applications requiring
sub-millisecond response times.

Using AWS DMS, you can migrate data from any supported source
database to a target Redis OSS data store with minimal downtime. For additional information about Redis OSS see, [Redis OSS Documentation](https://redis.io/documentation "https://redis.io/documentation").

In addition to on-premises Redis OSS, AWS Database Migration Service supports the following:

- [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/ "https://aws.amazon.com/elasticache/redis/")
  as a target data store. ElastiCache (Redis OSS) works with your Redis OSS clients and uses the open Redis OSS data
  format to store your data.
- [Amazon MemoryDB](https://aws.amazon.com/memorydb/ "https://aws.amazon.com/memorydb/")
  as a target data store. MemoryDB is compatible with Redis OSS and enables you to build
  applications using all the Redis OSS data structures, APIs, and commands in use today.
  For additional information about working with Redis OSS as a target for AWS DMS, see the following sections:

###### Topics

- [Prerequisites for using a Redis OSS
  cluster as a target for AWS DMS](#CHAP_Target.Redis.Prerequisites "#CHAP_Target.Redis.Prerequisites")
- [Limitations when using Redis
  as a target for AWS Database Migration Service](#CHAP_Target.Redis.Limitations "#CHAP_Target.Redis.Limitations")
- [Migrating data from a
  relational or non-relational database to a Redis OSS target](#CHAP_Target.Redis.Migrating "#CHAP_Target.Redis.Migrating")
- [Specifying endpoint settings
  for Redis OSS as a target](#CHAP_Target.Redis.EndpointSettings "#CHAP_Target.Redis.EndpointSettings")

## Prerequisites for using a Redis OSS

cluster as a target for AWS DMS

DMS supports an on-premises Redis OSS target in a standalone configuration, or as a
Redis OSS cluster where data is automatically _sharded_
across multiple nodes. Sharding is the process of separating data into smaller
chunks called shards that are spread across multiple servers or nodes. In effect, a
shard is a data partition that contains a subset of the total data set, and serves a
slice of the overall workload.

Since Redis OSS is a key-value NoSQL data store, the Redis OSS key naming convention
to use when your source is a relational database, is **schema-name.table-name.primary-key**. In Redis OSS, the key and value must
not contain the special character %. Otherwise, DMS skips the record.

###### Note

If you are using ElastiCache (Redis OSS) as a target, DMS supports _cluster mode
enabled_ configurations only. For more information about using
ElastiCache (Redis OSS) version 6.x or higher to create a cluster mode enabled target data store,
see [Getting
started](../../../AmazonElastiCache/latest/red-ug/GettingStarted.md "../../../AmazonElastiCache/latest/red-ug/GettingStarted.md") in the _Amazon ElastiCache (Redis OSS) User Guide_.

Before you begin a database migration, launch your Redis OSS cluster with the following criteria.

- Your cluster has one or more shards.
- If you're using an ElastiCache (Redis OSS) target, ensure that your cluster doesn't use
  IAM role-based access control. Instead, use Redis OSS Auth to authenticate users.
- Enable Multi-AZ (Availability Zones).
- Ensure the cluster has sufficient memory available to fit the data to be
  migrated from your database.
- Make sure that your target Redis OSS cluster is clear of all data before
  starting the initial migration task.

You should determine your security requirements for the data migration prior to
creating your cluster configuration. DMS supports migration to target replication
groups regardless of their encryption configuration. But you can enable or disable
encryption only when you create your cluster configuration.

## Limitations when using Redis

as a target for AWS Database Migration Service

The following limitations apply when using Redis OSS as a target:

- Since Redis OSS is a key-value no-sql data store, the Redis OSS key naming convention to use
  when your source is a relational database, is `schema-name.table-name.primary-key`.
- In Redis OSS, the key-value can't contain the special character `%`.
  Otherwise, DMS skips the record.
- DMS won't migrate rows that contain the `%` character.
- DMS won't migrate fields that contain the `%` character in the field name.
- Full LOB mode is not supported.
- A private Certificate Authority (CA) isn’t supported when using ElastiCache (Redis OSS) as a target.

## Migrating data from a

relational or non-relational database to a Redis OSS target

You can migrate data from any source SQL or NoSQL data store directly to a Redis OSS
target. Setting up and starting a migration to a Redis OSS target is similar to any full
load and change data capture migration using the DMS console or API. To perform a
database migration to a Redis OSS target, you do the following.

- Create a replication instance to perform all the processes for the
  migration. For more information, see [Creating a replication instance](CHAP_ReplicationInstance.md "CHAP_ReplicationInstance.md").
- Specify a source endpoint. For more information, see [Creating source and target endpoints](CHAP_Endpoints.md "CHAP_Endpoints.md").
- Locate the DNS name and port number of your cluster.
- Download a certificate bundle that you can use to verify SSL
  connections.
- Specify a target endpoint, as described below.
- Create a task or set of tasks to define what tables and replication processes you
  want to use. For more information, see [Creating a task](CHAP_Tasks.md "CHAP_Tasks.md").
- Migrate data from your source database to your target cluster.

You begin a database migration in one of two ways:

1. You can choose the AWS DMS console and perform each step there.
2. You can use the AWS Command Line Interface (AWS CLI). For more information about
   using the CLI with AWS DMS, see [AWS CLI for
   AWS DMS](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md").

###### To locate the DNS name and port number of your cluster

- Use the following AWS CLI command to provide the
  `replication-group-id` with the name of your
  replication group.

```

aws elasticache describe-replication-groups --replication-group-id *myreplgroup*

```

Here, the output shows the DNS name in the `Address` attribute and the port number in the
`Port` attribute of the primary node in the cluster.

```
 ...
"ReadEndpoint": {
"Port": 6379,
"Address": "myreplgroup-
111.1abc1d.1111.uuu1.cache.example.com"
}
...

```

If you are using MemoryDB as your target, use the following
AWS CLI command to provide an endpoint address to your Redis OSS cluster.

```

aws memorydb describe-clusters --clusterid `clusterid`

```

###### Download a certificate bundle for use to verify SSL connections

- Enter the following `wget` command at the command line. Wget is a free
  GNU command-line utility tool used to download files from the internet.

```

wget https://s3.aws-api-domain/rds-downloads/rds-combined-ca-bundle.pem

```

Here, `*aws-api-domain*` completes the Amazon S3
domain in your AWS Region required to access the speciﬁed S3 bucket and the
rds-combined-ca-bundle.pem ﬁle that it provides.

###### To create a target endpoint using the AWS DMS console

This endpoint is for your Redis OSS target that is already running.

- On the console, choose **Endpoints** from the navigation
  pane and then choose **Create Endpoint**. The following
  table describes the settings.

| For this option           | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Endpoint type**         | Choose the \*_Target_<br>• endpoint type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Endpoint identifier**   | Enter the name of your endpoint. For example, include the<br>type of endpoint in the name, such as<br>`my-redis-target`.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Target engine**         | Choose \*_Redis OSS_<br>• as the type of<br>database engine that you want this endpoint to<br>connect.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Cluster name**          | Enter the DNS name of your Redis OSS cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Port**                  | Enter the port number of your Redis OSS cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **SSL security protocol** | Choose either **Plain text\*<br>• or<br>**SSL encryption**.<br>**Plain text**—This option doesn't provide<br>Transport Layer Security (TLS) encryption for traffic between endpoint and database.<br>**SSL encryption\*\*—If you choose<br>this option, enter an SSL Certificate Authority (CA)<br>certificate ARN to verify the server’s certificate and<br>make an encrypted connection.<br>For on-premises Redis OSS, DMS supports both public and<br>private Certificate Authority (CA). For ElastiCache (Redis OSS), DMS<br>supports only a public CA. |
| **Authentication type**   | Choose the type of authentication to perform while connecting to Redis OSS. Options include,<br>**None**, **Authentication role**, and<br>**Authentication token**.<br>If you choose Authentication role, provide an **Authentication username\*<br>• and an<br>**Authentication password**.<br>If you choose Authentication token, provide an<br>**Authentication password\*<br>• only.                                                                                                                                                                    |
| **Replication instance**  | **[Optional]\*<br>• Only if you<br>intend to test your connection, choose the name of the<br>replication instance you previously entered on the<br>**Create replication instance\*\*<br>page.                                                                                                                                                                                                                                                                                                                                                               |

When you're finished providing all information for your endpoint, AWS DMS
creates your Redis OSS target endpoint for use during database migration.

For information about creating a migration task and starting your database
migration, see [Creating a task](CHAP_Tasks.md "CHAP_Tasks.md").

## Specifying endpoint settings

for Redis OSS as a target

To create or modify a target endpoint, you can use the console or the
`CreateEndpoint` or `ModifyEndpoint` API operations.

For a Redis OSS target in the AWS DMS console, specify **Endpoint-specific
settings** on the **Create endpoint** or
**Modify endpoint** console page.

When using `CreateEndpoint` and `ModifyEndpoint` API
operations, specify request parameters for the `RedisSettings` option.
The example following shows how to do this using the AWS CLI.

```
aws dms create-endpoint --endpoint-identifier `my-redis-target`
--endpoint-type target --engine-name redis --redis-settings
'{"ServerName":"`sample-test-sample.zz012zz.cluster.eee1.cache.bbbxxx.com`","Port":6379,"AuthType":"auth-token",
 "SslSecurityProtocol":"ssl-encryption", "AuthPassword":"`notanactualpassword`"}'

{
    "Endpoint": {
        "EndpointIdentifier": "my-redis-target",
        "EndpointType": "TARGET",
        "EngineName": "redis",
        "EngineDisplayName": "Redis",
        "TransferFiles": false,
        "ReceiveTransferredFiles": false,
        "Status": "active",
        "KmsKeyId": "arn:aws:kms:us-east-1:999999999999:key/x-b188188x",
        "EndpointArn": "arn:aws:dms:us-east-1:555555555555:endpoint:ABCDEFGHIJKLMONOPQRSTUVWXYZ",
        "SslMode": "none",
        "RedisSettings": {
            "ServerName": "sample-test-sample.zz012zz.cluster.eee1.cache.bbbxxx.com",
            "Port": 6379,
            "SslSecurityProtocol": "ssl-encryption",
            "AuthType": "auth-token"
        }
    }
}

```

The `--redis-settings` parameters follow:

- `ServerName`–(Required) Of type `string`,
  specifies the Redis OSS cluster that data will be migrated to, and is in your
  same VPC.
- `Port`–(Required) Of type `number`, the port
  value used to access the endpoint.
- `SslSecurityProtocol`–(Optional) Valid values include `plaintext`
  and `ssl-encryption`. The default is `ssl-encryption`.

The `plaintext` option doesn't provide Transport Layer Security (TLS)
encryption for traffic between endpoint and database.

Use `ssl-encryption` to make an encrypted connection. `ssl-encryption`
doesn’t require an SSL Certificate Authority (CA) ARN to verify a server’s certificate, but one can be
identified optionally using the `SslCaCertificateArn` setting. If a certificate authority ARN
isn't given, DMS uses the Amazon root CA.

When using an on-premises Redis OSS target, you can use
`SslCaCertificateArn` to import public or private Certificate
Authority (CA) into DMS, and provide that ARN for server authentication. A
private CA isn’t supported when using ElastiCache (Redis OSS) as a target.

- `AuthType`–(Required) Indicates the type of
  authentication to perform when connecting to Redis OSS. Valid values include
  `none`, `auth-token`, and
  `auth-role`.

The `auth-token` option requires an
"`AuthPassword`" be provided, while the
`auth-role` option requires
"`AuthUserName`" and
"`AuthPassword`" be provided.
