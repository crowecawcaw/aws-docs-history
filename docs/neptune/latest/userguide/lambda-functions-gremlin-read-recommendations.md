# Recommendations for using Gremlin read-requests in Lambda

If you have one or more read replicas in your cluster, it's a good idea to balance
read requests across these replicas. One option is to use the [reader endpoint](feature-overview-endpoints.md "feature-overview-endpoints.md"). The reader endpoint
balances connections across replicas even if the cluster topology changes when you
add or remove replicas, or promote a replica to become the new primary instance.

However, using the reader endpoint can result in an uneven use of cluster resources
in some circumstances. The reader endpoint works by periodically changing the host that
the DNS entry points to. If a client opens a lot of connections before the DNS entry
changes, all the connection requests are sent to a single Neptune instance. This can
be the case with a high-throughput Lambda scenario where a large number of concurrent
requests to your Lambda function causes multiple execution contexts to be created, each
with its own connection. If those connections are all created nearly simultaneously,
the connections are likely to all point to the same replica in the cluster, and to
stay pointing to that replica until the execution contexts are recycled.

One way you can distribute requests across instances is to configure your Lambda
function to connect to an instance endpoint, chosen at random from a list of replica
instance endpoints, rather than the reader endpoint. The downside of this approach
is that it requires the Lambda code to handle changes in the cluster topology by
monitoring the cluster and updating the endpoint list whenever the membership of
the cluster changes.

If you are writing a Java Lambda function that needs to balance read requests
across instances in your cluster, you can use the [Gremlin client for Amazon Neptune](https://github.com/aws/neptune-gremlin-client "https://github.com/aws/neptune-gremlin-client"), a Java Gremlin client that is aware
of your cluster topology and which fairly distributes connections and requests across
a set of instances in a Neptune cluster. [This blog post](https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/ "https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/") includes a sample Java Lambda function that uses the Gremlin
client for Amazon Neptune.
