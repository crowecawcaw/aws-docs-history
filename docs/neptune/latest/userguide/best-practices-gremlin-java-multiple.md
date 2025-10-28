# Add multiple read replica endpoints to a

Gremlin Java connection pool

When creating a Gremlin Java `Cluster` object, you can use the
`.addContactPoint()` method to add multiple read replica instances to the
connection pool's contact points.

```
Cluster.Builder readerBuilder = Cluster.build()
          .port(8182)
          .minConnectionPoolSize(…)
          .maxConnectionPoolSize(…)
          ………
          .addContactPoint("`reader-endpoint-1`")
          .addContactPoint("`reader-endpoint-2`")
```
