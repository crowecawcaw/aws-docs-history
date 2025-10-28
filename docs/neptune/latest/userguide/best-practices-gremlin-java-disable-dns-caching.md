# Disable DNS caching in the Java Virtual Machine

In an environment where you want to load-balance requests across multiple read
replicas, you need to disable DNS caching in the Java Virtual Machine (JVM) and provide
Neptune's reader endpoint while creating the cluster. Disabling the JVM DNS cache ensures
that DNS is resolved again for every new connection so that the requests are distributed
across all of the read replicas. You can do this in your application's initialization
code with the following line:

```
java.security.Security.setProperty("networkaddress.cache.ttl", "0");
```

However, a more complete and robust solution for load-balancing is provided by the
[Amazon Gremlin Java client code](https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-gremlin-client "https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-gremlin-client") on GitHub. The Amazon Java Gremlin client is aware
of your cluster topology and fairly distributes connections and requests across
a set of instances in your Neptune cluster. See [this blog post](https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/ "https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/") for a sample Java Lambda function that uses that client.
