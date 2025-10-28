# Neptune Best Practices Using openCypher and Bolt

Follow these best practices when using the openCypher query language and Bolt protocol
with Neptune. For information about using openCypher in Neptune, see [Accessing the Neptune Graph with openCypher](access-graph-opencypher.md "access-graph-opencypher.md").

###### Topics

- [Create a new connection after failover](#best-practices-opencypher-renew-connection "#best-practices-opencypher-renew-connection")
- [Connection handling for
  long-lived applications](#best-practices-opencypher-long-connections "#best-practices-opencypher-long-connections")
- [Connection handling for AWS Lambda](#best-practices-opencypher-lambda-connections "#best-practices-opencypher-lambda-connections")
- [Prefer directed to bi-directional edges in queries](best-practices-opencypher-directed-edges.md "best-practices-opencypher-directed-edges.md")
- [Neptune does not support
  multiple concurrent queries in a transaction](best-practices-opencypher-multiple-queries.md "best-practices-opencypher-multiple-queries.md")
- [Close driver objects when you're done](best-practices-opencypher-close-driver.md "best-practices-opencypher-close-driver.md")
- [Use explicit transaction modes for reading and writing](best-practices-opencypher-use-explicit-txs.md "best-practices-opencypher-use-explicit-txs.md")
- [Retry logic for exceptions](best-practices-opencypher-retry-logic.md "best-practices-opencypher-retry-logic.md")
- [Set multiple properties at once using a single SET clause](best-practices-content-0.md "best-practices-content-0.md")
- [Use parameterized queries](best-practices-content-2.md "best-practices-content-2.md")
- [Use flattened maps instead of nested maps in UNWIND clause](best-practices-content-3.md "best-practices-content-3.md")
- [Place more restrictive nodes on the left side in
  Variable-Length Path (VLP) expressions](best-practices-content-4.md "best-practices-content-4.md")
- [Avoid redundant node label checks by using granular relationship names](best-practices-content-5.md "best-practices-content-5.md")
- [Specify edge labels where possible](best-practices-content-6.md "best-practices-content-6.md")
- [Avoid using the WITH clause when possible](best-practices-content-7.md "best-practices-content-7.md")
- [Place restrictive filters as early in the query as possible](best-practices-content-8.md "best-practices-content-8.md")
- [Explicitly check whether properties exist](best-practices-content-9.md "best-practices-content-9.md")
- [Do not use named path (unless it is required)](best-practices-content-10.md "best-practices-content-10.md")
- [Avoid COLLECT(DISTINCT())](best-practices-content-11.md "best-practices-content-11.md")
- [Prefer the properties function over individual property lookup when
  retrieving all property values](best-practices-content-12.md "best-practices-content-12.md")
- [Perform static computations outside of the query](best-practices-content-13.md "best-practices-content-13.md")
- [Batch inputs using UNWIND instead of individual statements](best-practices-content-14.md "best-practices-content-14.md")
- [Prefer using custom IDs for node/relationship](best-practices-content-15.md "best-practices-content-15.md")
- [Avoid doing ~id computations in the query](best-practices-content-16.md "best-practices-content-16.md")
- [Updating/Merging multiple nodes](best-practices-merge-multiple-nodes.md "best-practices-merge-multiple-nodes.md")

## Create a new connection after failover

In case of a failover, the Bolt driver can continue connecting to the old writer
instance rather than the new active one, because the DNS name resolved to a specific
IP address.

To prevent this, close and then reconnect the `Driver` object after
any failover.

## Connection handling for

long-lived applications

When building long-lived applications, such as those running within containers or
on Amazon EC2 instances, instantiate a `Driver` object once and then reuse that
object for the lifetime of the application. The `Driver` object is thread
safe, and the overhead of initializing it is considerable.

## Connection handling for AWS Lambda

Bolt drivers are not recommended for use within AWS Lambda functions, because of their
connection overhead and management requirements. Use the [HTTPS endpoint](access-graph-opencypher-queries.md "access-graph-opencypher-queries.md") instead.
