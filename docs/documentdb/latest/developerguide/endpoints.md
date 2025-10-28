# Understanding Amazon DocumentDB endpoints

You can use Amazon DocumentDB (with MongoDB compatibility) endpoints to connect to a cluster or instance.
Amazon DocumentDB has three different types of endpoints, each with its own purpose.

###### Topics

- [Finding a cluster's endpoints](db-cluster-endpoints-find.md "db-cluster-endpoints-find.md")
- [Finding an instance's endpoint](db-instance-endpoint-find.md "db-instance-endpoint-find.md")
- [Connecting to endpoints](endpoints-connecting.md "endpoints-connecting.md")

**Cluster endpoint**

A cluster endpoint is an endpoint for an Amazon DocumentDB cluster that connects to the current primary instance for the cluster. Each Amazon DocumentDB cluster
has a single cluster endpoint and one primary instance. In case of a failover, the cluster endpoint is remapped to the new primary
instance.

**Reader endpoint**

A reader endpoint is an endpoint for an Amazon DocumentDB cluster that connects to one of the available replicas for that cluster. Each Amazon DocumentDB cluster
has a reader endpoint. If there is more than one replica, the reader endpoint directs each connection request to one of the Amazon DocumentDB
replicas.

**Instance endpoint**

An instance endpoint is an endpoint that connects to a specific instance. Each instance in a cluster, regardless of whether it is a primary or
replica instance, has its own unique instance endpoint. It is best to not use instance endpoints in your application. This is because they can
change roles in case of a failover, thus requiring code changes in your application.
