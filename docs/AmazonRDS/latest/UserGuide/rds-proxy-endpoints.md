# Working with Amazon RDS Proxy endpoints

RDS Proxy endpoints provide flexible and efficient ways to manage database connections, which
improves scalability, availability, and security. With proxy endpoints, you can:

- **Simplify monitoring and troubleshooting** – Use multiple
  endpoints to track and manage connections from different applications independently.

###### Topics

- [Overview of proxy endpoints](#rds-proxy-endpoints-overview "#rds-proxy-endpoints-overview")
- [Limitations for proxy endpoints](#rds-proxy-endpoints-limits "#rds-proxy-endpoints-limits")
- [Proxy endpoints for Multi-AZ DB clusters](#rds-proxy-endpoints-overview-maz "#rds-proxy-endpoints-overview-maz")
- [Accessing RDS databases across VPCs](#rds-proxy-cross-vpc "#rds-proxy-cross-vpc")
- [Creating a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md")
- [Viewing proxy endpoints](rds-proxy-endpoints.md "rds-proxy-endpoints.md")
- [Modifying a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md")
- [Deleting a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md")

## Overview of proxy endpoints

Working with RDS Proxy endpoints involves the same kinds of procedures as with RDS instance endpoints.

If you aren't familiar with RDS endpoints, find more information in
[Connecting to a DB
instance running the MySQL database engine](USER_ConnectToInstance.md "USER_ConnectToInstance.md") and
[Connecting
to a DB instance running the PostgreSQL database engine](USER_ConnectToPostgreSQLInstance.md "USER_ConnectToPostgreSQLInstance.md").

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

## Limitations for proxy endpoints

RDS Proxy endpoints have the following limitations:

- The RDS proxy default endpoint cannot be modified.
- The maximum number of user-defined endpoints for a proxy is 20. Thus, a proxy can have up to 21 endpoints: the
  default endpoint, plus 20 that you create.
- When you associate additional endpoints with a proxy, RDS Proxy automatically determines which DB instances in
  your cluster to use for each endpoint.
- For IPv6 or dual-stack endpoint network types, your VPC and subnets must be configured to support the selected network type.

When you create a proxy, RDS automatically creates a VPC endpoint for secure communication between applications and the database.
The VPC endpoint is visible and can be accessed from the Amazon VPC Console.

Adding a new proxy endpoint provisions an AWS PrivateLink interface endpoint. If you add one or more endpoints to your proxy, you incure additional charges.
For more information, see [RDS Proxy Pricing](https://aws.amazon.com/rds/proxy/pricing/ "https://aws.amazon.com/rds/proxy/pricing/").

## Proxy endpoints for Multi-AZ DB clusters

By default, the endpoint that you connect to when you use RDS Proxy with a Multi-AZ DB cluster has read/write capability. As a
result, this endpoint sends all requests to the writer instance of the cluster. All of those connections count
against the `max_connections` value for the writer instance. If your proxy is associated with a Multi-AZ DB cluster,
then you can create additional read/write or read-only endpoints for that proxy.

You can use a read-only endpoint with your proxy for read-only queries. You do this the
same way that you use the reader endpoint for a Multi-AZ DB cluster. Doing so helps you
to take advantage of the read scalability of a Multi-AZ DB cluster with one or more reader DB
instances. You can run more simultaneous queries and make more simultaneous connections by
using a read-only endpoint and adding more reader DB instances to your Multi-AZ DB cluster as
needed. These reader endpoints help to improve the read scalability of your query-intensive applications. Reader
endpoints also help to improve the availability of your connections if a reader DB instance in your cluster
becomes unavailable.

### Reader endpoints for

Multi-AZ DB clusters

With RDS Proxy, you can create and use reader endpoints. However, these endpoints only work for proxies
associated with
Multi-AZ DB clusters. If you use the RDS CLI or API, you might see the
`TargetRole` attribute with a value of `READ_ONLY`.
You can take advantage of such proxies by changing the target of a proxy from an RDS DB instance to a Multi-AZ DB cluster.

You can create and connect to read-only endpoints called _reader endpoints_ when you use
RDS Proxy with Multi-AZ DB clusters.

#### How reader endpoints help application availability

In some cases, a reader instance in your cluster might become unavailable. If that
occurs, connections that use a reader endpoint of a DB proxy can recover more quickly than
ones that use the Multi-AZ DB cluster reader endpoint. RDS Proxy routes connections to only the available
reader instance in the cluster. There isn't a delay due to DNS caching when an
instance becomes unavailable.

If the connection is multiplexed, RDS Proxy directs subsequent queries to a different reader instance
without any interruption to your application. If a reader instance is in an unavailable state, all client
connections to that instance endpoint are closed.

If the connection is pinned, the next query on the connection returns an error. However, your application
can immediately reconnect to the same proxy endpoint. RDS Proxy routes the connection to a different reader DB
instance that's in `available` state. When you manually reconnect, RDS Proxy doesn't
check the replication lag between the old and new reader instance.

If your Multi-AZ DB cluster doesn't have any available reader instances, RDS Proxy attempts to connect
to a reader endpoint when it becomes available. If no reader instance becomes available within the
connection borrow timeout period, the connection attempt fails. If a reader instance does become available,
the connection attempt succeeds.

#### How reader endpoints help query scalability

Reader endpoints for a proxy help with Multi-AZ DB cluster query scalability in the following ways:

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

## Accessing RDS databases across VPCs

By default, the components of your RDS
technology stack are all in the same Amazon VPC. For example,
suppose that an application running on an Amazon EC2 instance connects to an Amazon RDS DB instance.
In this case, the application server and database must both be within the same VPC.

With RDS Proxy, you can set up access to an Amazon RDS DB instance in one VPC from
resources in another VPC, such as EC2 instances. For example, your organization might have
multiple applications that access the same database resources. Each application might be in its
own VPC.

To enable cross-VPC access, you create a new endpoint for the proxy. The
proxy itself resides in the same VPC as the Amazon RDS DB instance. However, the cross-VPC endpoint
resides in the other VPC, along with the other resources such as the EC2 instances. The cross-VPC endpoint is
associated with subnets and security groups from the same VPC as the EC2 and other resources. These associations
let you connect to the endpoint from the applications that otherwise can't access the database due to the
VPC restrictions.

The following steps explain how to create and access a cross-VPC endpoint through RDS Proxy:

1. Create two VPCs, or choose two VPCs that you already use for
   RDS work. Each VPC should have its
   own associated network resources such as an internet gateway, route tables, subnets, and security groups.
   If you only have one
   VPC, you can consult [Getting started with Amazon RDS](CHAP_GettingStarted.md "CHAP_GettingStarted.md") for the
   steps to set up another VPC to use RDS successfully. You can also examine your existing VPC in the
   Amazon EC2 console to see the kinds of resources to connect together.
2. Create a DB proxy associated with the Amazon RDS DB instance that you want to connect to. Follow
   the procedure in [Creating a proxy for Amazon RDS](rds-proxy-creating.md "rds-proxy-creating.md").
3. On the **Details** page for your proxy in the RDS console, under the **Proxy
   endpoints** section, choose **Create endpoint**. Follow the procedure in
   [Creating a proxy endpoint](rds-proxy-endpoints.md "rds-proxy-endpoints.md").
4. Choose whether to make the cross-VPC endpoint read/write or read-only.
5. Instead of accepting the default of the same VPC as the Amazon RDS DB instance, choose a different
   VPC. This VPC must be in the same AWS Region as the VPC where the proxy resides.
6. Now instead of accepting the defaults for subnets and security groups from the same VPC as the Amazon RDS DB instance, make new selections.
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
