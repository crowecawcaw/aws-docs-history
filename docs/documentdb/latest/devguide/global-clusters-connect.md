# Connect to an Amazon DocumentDB global cluster

How you connect to a global cluster depends on whether you need to write to the cluster
or read from the cluster:

- For read-only requests or queries, you connect to the reader endpoint for the
  cluster in your AWS Region.
- To run data manipulation language (DML) or data definition language (DDL)
  statements, you connect to the cluster endpoint for the primary cluster. This
  endpoint might be in a different AWS Region than your application.
  When you view a global cluster in the console, you can see all the general-purpose
  endpoints associated with all of its clusters.

How you connect to a global cluster depends on whether you need to write to the database
or read from the database. For DDL, DML and read operations that you would like to serve
from the primary Region, connect to your primary cluster using the cluster endpoint in replica set mode, with a read
preference of `secondaryPreferred=true`. This routes write traffic to your
primary cluster’s writer instance and read traffic to your primary cluster’s replica
instance.

For cross-Region, read-only traffic, connect to one of your secondary clusters using the cluster endpoint in
replica set mode. Because all instances are read-only replica instances, specify a
read preference other than `primary` (for example, `secondary`,
`secondaryPreferred`, or `nearest`). To minimize latency, choose whichever reader endpoint is in your
Region or the Region closest to you.
