# Custom endpoints for Amazon Aurora

A _custom endpoint_ for an Aurora cluster represents a set of DB
instances that you choose. When you connect to the endpoint, Aurora performs connection
balancing and chooses one of the instances in the group to handle the connection. You define
which instances this endpoint refers to, and you decide what purpose the endpoint
serves.

An Aurora DB cluster has no custom endpoints until you create one. You can create up to
five custom endpoints for each provisioned Aurora cluster or Aurora Serverless v2 cluster. You
can't use custom endpoints for Aurora Serverless v1 clusters.

The custom endpoint provides balanced database connections based on criteria other than
the read-only or read/write capability of the DB instances. For example, you might define a
custom endpoint to connect to instances that use a particular AWS instance class or a
particular DB parameter group. Then you might tell particular groups of users about this
custom endpoint. For example, you might direct internal users to low-capacity instances for
report generation or ad hoc (one-time) querying, and direct production traffic to
high-capacity instances.

Because the connection can go to any DB instance that is associated with the custom
endpoint, we recommend that you make sure that all the DB instances within that group share
some similar characteristic. Doing so ensures that the performance, memory capacity, and so
on, are consistent for everyone who connects to that endpoint.

This feature is intended for advanced users with specialized kinds of workloads where it
isn't practical to keep all the Aurora Replicas in the cluster identical. With custom
endpoints, you can predict the capacity of the DB instance used for each connection. When
you use custom endpoints, you typically don't use the reader endpoint for that
cluster.

The following example illustrates a custom endpoint for a DB instance in an Aurora MySQL
DB cluster.

```
myendpoint.cluster-custom-c7tj4example.us-east-1.rds.amazonaws.com:3306
```

You use custom endpoints to simplify connection management when your cluster contains DB
instances with different capacities and configuration settings.

Previously, you might have used the CNAMES mechanism to set up Domain Name Service (DNS)
aliases from your own domain to achieve similar results. By using custom endpoints, you can
avoid updating CNAME records when your cluster grows or shrinks. Custom endpoints also mean
that you can use encrypted Transport Layer Security/Secure Sockets Layer (TLS/SSL)
connections.

Instead of using one DB instance for each specialized purpose and connecting to its
instance endpoint, you can have multiple groups of specialized DB instances. In this case,
each group has its own custom endpoint. This way, Aurora can perform connection balancing
among all the instances dedicated to tasks such as reporting or handling production or
internal queries. The custom endpoints distribute connections across instances passively,
using DNS to return the IP address of one of the instances randomly. If one of the DB
instances within a group becomes unavailable, Aurora directs subsequent custom endpoint
connections to one of the other DB instances associated with the same endpoint.

###### Topics

- [Considerations for custom endpoints
  in Amazon Aurora](Aurora.Endpoints.Custom.md "Aurora.Endpoints.Custom.md")
- [Creating a custom endpoint](aurora-custom-endpoint-creating.md "aurora-custom-endpoint-creating.md")
- [Viewing custom endpoints](aurora-endpoint-viewing.md "aurora-endpoint-viewing.md")
- [Editing a custom endpoint](aurora-endpoint-editing.md "aurora-endpoint-editing.md")
- [Deleting a custom endpoint](aurora-endpoints-custom-deleting.md "aurora-endpoints-custom-deleting.md")
- [AWS CLI examples for custom endpoints for
  Amazon Aurora](Aurora.Endpoint.md "Aurora.Endpoint.md")
