# Application migration from Neo4j to Neptune

After you have migrated your data from Neo4j to Neptune, the next step is to
migrate the application itself. As with data, there are multiple approaches to
migrating your application based on the tools your use, requirements, architectural
differences, and so on. Things that you usually need to consider in this process are
outlined below.

## Migrating connections when moving from Neo4j to Neptune

If you don't currently use the Bolt drivers, or would like to use an alternative,
you can connect to the [HTTPS endpoint](access-graph-opencypher-queries.md "access-graph-opencypher-queries.md")
which provides full access to the data returned.

If you do have an application that uses the [Bolt
protocol](access-graph-opencypher-bolt.md "access-graph-opencypher-bolt.md"), you can migrate these connections to Neptune and let your applications
connect using the same drivers as you did in Neo4j. To connect to Neptune, you may need
to make one or more of the following changes to your application:

- The URL and port will need to be updated to use the cluster endpoints and
  cluster port (the default is 8182).
- Neptune requires all connections to use SSL, so you need to specify for
  each connection that it is encrypted.
- Neptune manages authentication through the assignment of [IAM policies and roles](iam-auth.md "iam-auth.md"). IAM policies and roles provide
  an extremely flexible level of user management within the application, so it is
  important to read and understand the information in the [IAM
  overview](iam-auth.md "iam-auth.md") before configuring your cluster.
- Bolt connections behave differently in Neptune than in Neo4j in
  several ways, as explained in [Bolt connection behavior in Neptune](access-graph-opencypher-bolt.md#access-graph-opencypher-bolt-connections "access-graph-opencypher-bolt.md#access-graph-opencypher-bolt-connections").
- You can find more information and suggestions in [Neptune Best Practices Using openCypher and Bolt](best-practices-opencypher.md "best-practices-opencypher.md").

There are code samples for commonly used language such as Java, Python, .NET, and NodeJS,
and for connection scenarios such as using IAM authentication, in [Using the Bolt protocol to make openCypher queries to Neptune](access-graph-opencypher-bolt.md "access-graph-opencypher-bolt.md").

## Routing queries to cluster instances when moving from Neo4j to Neptune

Neo4j client applications use a [routing
driver](https://neo4j.com/docs/driver-manual/1.7/client-applications/#routing_drivers_bolt_routing "https://neo4j.com/docs/driver-manual/1.7/client-applications/#routing_drivers_bolt_routing") and specify an [access
mode](https://neo4j.com/docs/driver-manual/1.7/sessions-transactions/#driver-transactions-access-mode "https://neo4j.com/docs/driver-manual/1.7/sessions-transactions/#driver-transactions-access-mode") to route read and write requests to an appropriate server in a causal cluster.

When migrating a client application to Neptune, use [Neptune
endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") to route queries efficiently to an appropriate instance in your cluster:

- All connections to Neptune should use `bolt://` rather
  than `bolt+routing://` or `neo4j://` in the URL.
- The cluster endpoint connects to the current primary instance in your
  cluster. Use the cluster endpoint to route write requests to the primary.
- The reader endpoint [distributes
  connections](best-practices-general-basic.md#best-practices-general-loadbalance "best-practices-general-basic.md#best-practices-general-loadbalance") across read-replica instances in your cluster. If you have a single-instance
  cluster with no read-replica instances, the reader endpoint connects to the primary instance,
  which supports write operations. If the cluster does contain one or more read-replica
  instances, sending a write request to the reader endpoint generates an exception.
- Each instance in your cluster can also have its own instance endpoint. Use an instance
  endpoint if your client application needs to send a request to a specific instance in the cluster.

For more information, see [Neptune endpoint considerations](feature-overview-endpoints.md#feature-overview-endpoint-considerations "feature-overview-endpoints.md#feature-overview-endpoint-considerations").

## Data consistency in Neptune

When using Neo4j causal clusters, read replicas are eventually consistent with
core servers, but client applications can ensure causal consistency by using [causal
chaining](https://neo4j.com/docs/driver-manual/1.7/sessions-transactions/#driver-transactions-causal-chaining "https://neo4j.com/docs/driver-manual/1.7/sessions-transactions/#driver-transactions-causal-chaining"). Causal chaining entails passing bookmarks between transactions, which
allows a client application to write to a core server and then read its own write from
a read-replica.

In Neptune, read-replica instances are eventually consistent with the writer,
with replica lag that is usually less than 100 milliseconds. However, until a change
has been replicated, updates to existing edges and vertices and additions of new edges
and vertices are not visible on a replica instance. Therefore, if your application
needs immediate consistency on Neptune by reading each write, use the cluster endpoint
for the read-after-write operation. This is the only time to use the cluster endpoint
for read operations. In all other circumstances, use the reader endpoint for reads.

## Migrating queries from Neo4j to Neptune

Although Neptune's [support
for openCypher](https://aws.amazon.com/blogs/database/announcing-the-general-availability-of-opencypher-support-for-amazon-neptune/ "https://aws.amazon.com/blogs/database/announcing-the-general-availability-of-opencypher-support-for-amazon-neptune/") dramatically reduces the amount of work required to migrate queries
from Neo4j, there are still some differences to assess when migrating:

- As discussed in [Data-model optimizations](migration-data-migration.md#migration-data-model-optimization "migration-data-migration.md#migration-data-model-optimization") above, there may be
  modifications to your data model that you need to make so as to create an
  optimized graph data model for Neptune, which in turn will require changes
  to your queries and testing.
- Neo4j offers a variety of Cypher-specific language extensions that
  are not included in the openCypher specification implemented by Neptune.
  Depending on the use case and feature used, there may be workarounds within
  the openCypher language, or using the Gremlin language, or through other mechanisms
  as described in [Rewriting Cypher queries to run in openCypher on Neptune](migration-opencypher-rewrites.md "migration-opencypher-rewrites.md").
- Applications often use other middleware components to interact
  with the database instead of the Bolt drivers themselves. Please check [Neptune compatibility with Neo4j](migration-compatibility.md "migration-compatibility.md")
  to see if tools or middleware that you're using are supported.
- In the case of a failover, the Bolt driver might continue to
  connect to the previous writer or reader instance because the cluster endpoint
  provided to the connection has resolved to an IP address. Proper error handling
  in your application should handle this, as described in [Create a new connection after failover](best-practices-opencypher.md#best-practices-opencypher-renew-connection "best-practices-opencypher.md#best-practices-opencypher-renew-connection").
- When transactions are canceled because of unresolvable conflicts or
  lock-wait timeouts, Neptune responds with a `ConcurrentModificationException`.
  For more information, see [Engine Error Codes](errors-engine-codes.md "errors-engine-codes.md"). As a best practice, clients should
  always catch and handle these exceptions.

A `ConcurrentModificationException` occurs occasionally when
multiple threads or multiple applications are writing to the system simultaneously.
Because of [transaction isolation
levels](transactions-neptune.md#transactions-neptune-mutation "transactions-neptune.md#transactions-neptune-mutation"), these conflicts may sometimes be unavoidable.

- Neptune supports running both Gremlin and openCypher queries
  on the same data. This means that in some scenarios you may need to consider
  using Gremlin, with its more powerful querying capabilities, to perform some
  of the functionality of your queries.

As discussed in [Provisioning infrastructure](migration-provisioning-infrastructure.md "migration-provisioning-infrastructure.md") above, each
application should go through a right-sizing exercise to ensure that the number
of instances, the instance sizes, and the cluster topology are all optimized
for the specific workload of the application.

The considerations discussed here for migrating your application are the
most common ones, but this is not an exhaustive list. Each application is unique.
Please reach out to AWS support or engage your account team if you have further
questions.

## Migrating features and tools that are specific to Neo4j

Neo4j has a variety of custom features and add-ons with funtionality that your
application may rely on. When evaluating the need to migrate this functionality,
it often helps to investigate whether there is a better approach within AWS to
achieve the same goal. Considering the [architectural
differences between Neo4j and Neptune](migration-architectural-differences.md "migration-architectural-differences.md"), you can often find effective
alternatives that take advantage of other AWS services or [integrations](integrations.md "integrations.md").

See [Neptune compatibility with Neo4j](migration-compatibility.md "migration-compatibility.md")
for a list of Neo4j-specific features and suggested workarounds.
