# Working with Amazon RDS Proxy endpoints

RDS Proxy endpoints provide flexible and efficient ways to manage database connections, which
improves scalability, availability, and security. With proxy endpoints, you can:

- **Simplify monitoring and troubleshooting** – Use multiple
  endpoints to track and manage connections from different applications independently.
- **Enhance read scalability** – Leverage reader
  endpoints with Aurora DB clusters to distribute read traffic efficiently, which optimizes
  performance for query-heavy workloads.
- **Enable cross-VPC access** – Connect databases
  across VPCs using cross-VPC endpoints, which allows resources like Amazon EC2 instances in one
  VPC to access databases in another.

###### Topics

- [Overview of proxy endpoints](#rds-proxy-endpoints-overview "#rds-proxy-endpoints-overview")
- [Limitations for proxy endpoints](#rds-proxy-endpoints-limits "#rds-proxy-endpoints-limits")
- [Using reader endpoints with Aurora clusters](#rds-proxy-endpoints-reader "#rds-proxy-endpoints-reader")
- [Accessing Aurora databases across VPCs](#rds-proxy-cross-vpc "#rds-proxy-cross-vpc")
- [Creating a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md")
- [Viewing proxy endpoints](rds-proxy-endpoints.md "rds-proxy-endpoints.md")
- [Modifying a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md")
- [Deleting a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md")

## Overview of proxy endpoints

Working with RDS Proxy endpoints involves the same kinds of procedures as with Aurora DB cluster and reader
endpoints.
If you aren't familiar with Aurora endpoints, find more information in
[Amazon Aurora endpoint connections](Aurora.Overview.md "Aurora.Overview.md").

When you use RDS Proxy with an Aurora cluster, the default endpoint
supports both read and write operations. This means it routes all requests to the cluster’s
writer instance, contributing to its `max_connections` limit. To better distribute
traffic, you can create additional read/write or read-only endpoints for your proxy, which
allows more efficient workload management and improved scalability.

Use a read-only endpoint with your proxy to handle read queries, just
as you would with a reader endpoint for an Aurora provisioned cluster. This approach maximizes
Aurora's read scalability by distributing queries across one or more reader DB instances. By
using a read-only endpoint and adding more reader instances as needed, you can increase the
number of simultaneous queries and connections that your cluster can handle.

###### Tip

When you create a proxy for an Aurora cluster using the AWS Management Console, you can have RDS Proxy
automatically create a reader endpoint. For information about the benefits of a reader
endpoint, see [Using reader endpoints with Aurora clusters](#rds-proxy-endpoints-reader "#rds-proxy-endpoints-reader").

When you create a proxy endpoint, you can associate it with a different virtual private
cloud (VPC) than the proxy’s VPC. This allows you to connect to the proxy from another VPC,
such as one used by a different application within your organization.

For information about limits associated with proxy endpoints, see
[Limitations for proxy endpoints](#rds-proxy-endpoints-limits "#rds-proxy-endpoints-limits").

RDS Proxy logs prefix each entry with the name of the associated proxy endpoint. This can be
either the name that you specified for a user-defined endpoint, or the special name
`default` for the proxy’s default read/write endpoint.

Each proxy endpoint has its own set of CloudWatch metrics. Monitor metrics for all proxy
endpoints, a specific endpoint, or all read/write or read-only endpoints of a proxy. For more
information, see [Monitoring RDS Proxy metrics with Amazon CloudWatch](rds-proxy.md "rds-proxy.md").

A proxy endpoint uses the same authentication mechanism as its associated proxy. RDS Proxy automatically sets up
permissions and authorizations for the user-defined endpoint, consistent with the properties of the associated
proxy.

To learn how proxy endpoints work for DB clusters in an Aurora global database,
see [How RDS Proxy endpoints work with global databases](rds-proxy-gdb.md#rds-proxy-gdb.endpoints "rds-proxy-gdb.md#rds-proxy-gdb.endpoints").

## Limitations for proxy endpoints

RDS Proxy endpoints have the following limitations:

- The RDS proxy default endpoint cannot be modified.
- The maximum number of user-defined endpoints for a proxy is 20. Thus, a proxy can have up to 21 endpoints: the
  default endpoint, plus 20 that you create.
- When you associate additional endpoints with a proxy, RDS Proxy automatically determines which DB instances in
  your cluster to use for each endpoint. You can't choose specific instances the way that you can with
  Aurora custom endpoints.
- For IPv6 or dual-stack endpoint network types, your VPC and subnets must be configured to support the selected network type.

When you create a proxy, RDS automatically creates a VPC endpoint for secure communication between applications and the database.
The VPC endpoint is visible and can be accessed from the Amazon VPC Console.

Adding a new proxy endpoint provisions an AWS PrivateLink interface endpoint. If you add one or more endpoints to your proxy, you incure additional charges.
For more information, see [RDS Proxy Pricing](https://aws.amazon.com/rds/proxy/pricing/ "https://aws.amazon.com/rds/proxy/pricing/").

## Using reader endpoints with Aurora clusters

You can create and connect to read-only endpoints called _reader endpoints_ when you use
RDS Proxy with Aurora clusters. These reader endpoints help to improve the read scalability of your
query-intensive applications. Reader endpoints also help to improve the availability of your connections if a
reader DB instance in your cluster becomes unavailable.

###### Note

When you specify that a new endpoint is read-only, RDS Proxy requires that the Aurora
cluster has one or more reader DB instances. In some cases, you might change the target of
the proxy to an Aurora cluster containing only a single writer.
If you do, any requests to the reader endpoint fail with an error. Requests also
fail if the target of the proxy is an RDS instance instead of an Aurora cluster.

If an Aurora cluster has reader instances but those instances aren't available, RDS Proxy waits to send
the request instead of returning an error immediately. If no reader instance becomes available within the
connection borrow timeout period, the request fails with an error.

### How reader endpoints help application availability

In some cases, one or more reader instances in your cluster might become unavailable. If so, connections
that use a reader endpoint of a DB proxy can recover more quickly than ones that use the Aurora reader
endpoint. RDS Proxy routes connections to only the available reader instances in the cluster. There isn't
a delay due to DNS caching when an instance becomes unavailable.

If the connection is multiplexed, RDS Proxy directs subsequent queries to a different reader DB instance
without any interruption to your application. During the automatic switchover to a new reader instance,
RDS Proxy checks the replication lag of the old and new reader instances. RDS Proxy makes sure that the new
reader instance is up to date with the same changes as the previous reader instance. That way, your
application never sees stale data when RDS Proxy switches from one reader DB instance to another.

If the connection is pinned, the next query on the connection returns an error. However, your application
can immediately reconnect to the same endpoint. RDS Proxy routes the connection to a different reader DB
instance that's in `available` state. When you manually reconnect, RDS Proxy doesn't
check the replication lag between the old and new reader instances.

If your Aurora cluster doesn't have any available reader instances, RDS Proxy checks whether this
condition is temporary or permanent. The behavior in each case is as follows:

- Suppose that your cluster has one or more reader DB instances, but none of them are in the
  `Available` state. For example, all reader instances might be rebooting or encountering
  problems. In that case, attempts to connect to a reader endpoint wait for a reader instance to become
  available. If no reader instance becomes available within the connection borrow timeout period, the
  connection attempt fails. If a reader instance does become available, the connection attempt succeeds.
- Suppose that your cluster has no reader DB instances. In that case, RDS Proxy returns an error immediately
  if you try to connect to a reader endpoint. To resolve this problem, add one or more reader instances to
  your cluster before you connect to the reader endpoint.

### How reader endpoints help query scalability

Reader endpoints for a proxy help with Aurora query scalability in the following ways:

- As you add reader instances to your Aurora cluster, RDS Proxy can route new connections to any reader
  endpoints to the different reader instances. That way, queries performed using one reader endpoint
  connection don't slow down queries performed using another reader endpoint connection. The queries
  run on separate DB instances. Each DB instance has its own compute resources, buffer cache, and so on.
- Where practical, RDS Proxy uses the same reader DB instance for all the queries issue using a particular
  reader endpoint connection. That way, a set of related queries on the same tables can take advantage of
  caching, plan optimization, and so on, on a particular DB instance.
- If a reader DB instance becomes unavailable, the effect on your application depends on whether the
  session is multiplexed or pinned. If the session is multiplexed, RDS Proxy routes any subsequent queries
  to a different reader DB instance without any action on your part. If the session is pinned, your
  application gets an error and must reconnect. You can reconnect to the reader endpoint immediately and
  RDS Proxy routes the connection to an available reader DB instance. For more information about
  multiplexing and pinning for proxy sessions, see
  [Overview of RDS Proxy concepts](rds-proxy.md#rds-proxy-overview "rds-proxy.md#rds-proxy-overview").
- The more reader DB instances that you have in the cluster, the more simultaneous connections you
  can make using reader endpoints. For example, suppose that your cluster has four reader
  DB instances, each configured to support 200 simultaneous connections. Suppose also
  that your proxy is configured to use 50% of the maximum connections.
  Here, the maximum number of connections that you can make through the reader endpoints
  in the proxy is 100 (50% of 200) for reader 1. It's also 100 for reader 2, and so
  on, for a total of 400. If you double the number of cluster reader DB instances to
  eight, then the maximum number of connections through the reader endpoints also
  doubles, to 800.

### Examples of using reader endpoints

The following Linux example shows how you can confirm that you're connected to an Aurora MySQL cluster
through a reader endpoint. The `innodb_read_only` configuration setting is enabled. Attempts to
perform write operations such as `CREATE DATABASE` statements fail with an error. And you can
confirm that you're connected to a reader DB instance by checking the DB instance name using the
`aurora_server_id` variable.

###### Tip

Don't rely only on checking the DB instance name to determine whether the connection is read/write or
read-only. Remember that DB instances in an Aurora cluster can change roles between writer and reader when
failovers happen.

```
`$` mysql -h endpoint-demo-reader.endpoint.proxy-demo.us-east-1.rds.amazonaws.com -u admin -p
`...`
`mysql>` select @@innodb_read_only;
`+--------------------+
| @@innodb_read_only |
+--------------------+
| 1 |
+--------------------+`
`mysql>` create database shouldnt_work;
`ERROR 1290 (HY000): The MySQL server is running with the --read-only option so it cannot execute this statement`

`mysql>` select @@aurora_server_id;
`+---------------------------------------+
| @@aurora_server_id |
+---------------------------------------+
| proxy-reader-endpoint-demo-instance-3 |
+---------------------------------------+`

```

The following example shows how your connection to a proxy reader endpoint can keep working even when the
reader DB instance is deleted. In this example, the Aurora cluster has two reader instances,
`instance-5507` and `instance-7448`. The connection to the reader endpoint begins
using one of the reader instances. During the example, this reader instance is deleted by a
`delete-db-instance` command. RDS Proxy switches to a different reader instance for subsequent
queries.

```
`$` mysql -h reader-demo.endpoint.proxy-demo.us-east-1.rds.amazonaws.com
  -u `my_user` -p
`...`
`mysql>` select @@aurora_server_id;
`+--------------------+
| @@aurora_server_id |
+--------------------+
| instance-5507 |
+--------------------+`

`mysql>` select @@innodb_read_only;
`+--------------------+
| @@innodb_read_only |
+--------------------+
| 1 |
+--------------------+`

`mysql>` select count(*) from information_schema.tables;
`+----------+
| count(*) |
+----------+
| 328 |
+----------+`

```

While the `mysql` session is still running, the following command deletes the reader instance
that the reader endpoint is connected to.

```
aws rds delete-db-instance --db-instance-identifier instance-5507 --skip-final-snapshot
```

Queries in the `mysql` session continue working without the need to reconnect. RDS Proxy
automatically switches to a different reader DB instance.

```
`mysql>` select @@aurora_server_id;
`+--------------------+
| @@aurora_server_id |
+--------------------+
| instance-7448 |
+--------------------+`

`mysql>` select count(*) from information_schema.TABLES;
`+----------+
| count(*) |
+----------+
| 328 |
+----------+`

```

## Accessing Aurora databases across VPCs

By default, the components of your Aurora
technology stack are all in the same Amazon VPC. For example,
suppose that an application running on an Amazon EC2 instance connects to an Aurora DB
cluster.
In this case, the application server and database must both be within the same VPC.

With RDS Proxy, you can set up access to an Aurora DB
cluster in one VPC from
resources in another VPC, such as EC2 instances. For example, your organization might have
multiple applications that access the same database resources. Each application might be in its
own VPC.

To enable cross-VPC access, you create a new endpoint for the proxy. The
proxy itself resides in the same VPC as the Aurora DB
cluster. However, the cross-VPC endpoint
resides in the other VPC, along with the other resources such as the EC2 instances. The cross-VPC endpoint is
associated with subnets and security groups from the same VPC as the EC2 and other resources. These associations
let you connect to the endpoint from the applications that otherwise can't access the database due to the
VPC restrictions.

The following steps explain how to create and access a cross-VPC endpoint through RDS Proxy:

1. Create two VPCs, or choose two VPCs that you already use for Aurora
   work. Each VPC should have its
   own associated network resources such as an internet gateway, route tables, subnets, and security groups.
   If you only have one VPC, you can consult
   [Getting started with Amazon Aurora](CHAP_GettingStartedAurora.md "CHAP_GettingStartedAurora.md") for the steps to
   set up another VPC to use Aurora successfully. You can also examine your existing VPC in the
   Amazon EC2 console to see the kinds of resources to connect together.
2. Create a DB proxy associated with the Aurora DB
   cluster that you want to connect to. Follow
   the procedure in [Creating a proxy for Amazon Aurora](rds-proxy-creating.md "rds-proxy-creating.md").
3. On the **Details** page for your proxy in the RDS console, under the **Proxy
   endpoints** section, choose **Create endpoint**. Follow the procedure in
   [Creating a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md").
4. Choose whether to make the cross-VPC endpoint read/write or read-only.
5. Instead of accepting the default of the same VPC as the Aurora DB
   cluster, choose a different
   VPC. This VPC must be in the same AWS Region as the VPC where the proxy resides.
6. Now instead of accepting the defaults for subnets and security groups from the same VPC as the Aurora DB
   cluster, make new selections.
   Make these based on the subnets and security groups from the
   VPC that you chose.
7. You don't need to change any of the settings for the Secrets Manager secrets. The same credentials work for all endpoints for your proxy,
   regardless of which VPC each endpoint is in. Similarly, when using IAM authentication, your IAM configuration and permissions
   work consistently across all proxy endpoints, even when endpoints are in different VPCs. No additional IAM configuration is required per endpoint.
8. Wait for the new endpoint to reach the **Available** state.
9. Make a note of the full endpoint name. This is the value ending in
   ``Region_name`.rds.amazonaws.com` that you supply as part of the
   connection string for your database application.
10. Access the new endpoint from a resource in the same VPC as the endpoint. A simple way to test this process
    is to create a new EC2 instance in this VPC. Then, log into the EC2 instance and run the
    `mysql` or `psql` commands to connect by using the endpoint value in your connection
    string.
