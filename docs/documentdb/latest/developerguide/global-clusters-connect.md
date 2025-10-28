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
from the primary region, you should connect to your primary cluster. We recommend that you
connect to your primary cluster using the cluster endpoint in replica set mode, with a read
preference of `secondaryPreferred=true`. This will route write traffic to your
primary cluster’s writer instance and read traffic to your primary cluster’s replica
instance.

For cross region, read only traffic, you should connect to one of your secondary clusters.
We recommend that you connect to your secondary cluster using the cluster endpoint in
replica set mode. Since all instances are read-only replica instances, you do not need to
specify a read preference. To minimize latency, choose whichever reader endpoint is in your
region or the region closest to you.
