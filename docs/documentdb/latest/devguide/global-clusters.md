# Overview of Amazon DocumentDB global clusters

## What is a global cluster?

A global cluster consists of one primary Region and up to 10 read-only secondary
Regions. You issue write operations directly to the primary cluster in the primary Region
and Amazon DocumentDB automatically replicates the data to the secondary Regions using
dedicated infrastructure. Latency is typically under a second.

## How are global clusters useful?

- **Recovery from Region-wide outages** — In the
  event of a Region-wide outage, you can promote one of the secondary clusters to a
  primary cluster within minutes, with a typical Recovery Time Objective (RTO) of under
  a minute. The Recovery Point Objective (RPO) is typically measured in seconds, but
  this depends on the lag across the network at the time of the failure.
- **Global reads with local latency** — If you
  have offices around the world, you can use a global cluster to keep your main sources
  of information updated in the primary Region. Offices in your other Regions can
  access the information in their own Region, with local latency.
- **Scalable secondary clusters** — You can
  scale your secondary clusters by adding more read-only instances to a secondary
  Region. The secondary cluster is read-only, so it can support up to 16 read-only
  replica instances rather than the usual limit of 15 for a single cluster.
- **Fast replication from primary to secondary
  clusters** — The replication performed by a global cluster has
  little performance impact on the primary database cluster. The resources of the DB
  instances are fully devoted to serve application read and write workloads.
- **Change streams** — You can read change
  streams from a secondary cluster in global clusters, reducing the load on the
  primary cluster and allowing you to scale read workloads from secondary Regions.

## What are the current limitations of global clusters?

- Global clusters are not supported on Amazon DocumentDB v3.6.
- Global clusters are supported on all instance types except db.t3, db.t4g, and db.r4.
- Global clusters are not available in the following Regions: South America (São Paulo), Europe (Milan), China (Beijing), and China (Ningxia).
- Switchover and global failover are not supported when Regions are on different engine versions.
  Manual failover is supported when there's an engine version mismatch.
- Only the primary cluster performs write operations. Clients that perform write
  operations connect to the cluster endpoint of the primary cluster.
- You can have a maximum of 10 secondary Regions and one primary Region for your
  cluster.
- A secondary cluster cannot be stopped. A primary cluster cannot be stopped if it
  has secondary clusters associated with it. Only a regional cluster that has no
  secondary clusters can be stopped.
- Replicas attached to the secondary cluster can restart under certain
  circumstances. If the primary Region's instance restarts or fails over, replicas in
  the secondary Region also restart. The cluster is then unavailable until all replicas
  are back in sync with the primary database cluster's writer instance. This behavior
  is expected. Be sure that you understand the impact to your global cluster before
  making changes to your primary cluster.

###### Topics

- [Quick start guide](global-clusters.get-started.md "global-clusters.get-started.md")
- [Managing global clusters](global-clusters.manage.md "global-clusters.manage.md")
- [Connecting global clusters](global-clusters-connect.md "global-clusters-connect.md")
- [Monitoring global clusters](global-clusters-monitor.md "global-clusters-monitor.md")
- [Disaster recovery](global-clusters-disaster-recovery.md "global-clusters-disaster-recovery.md")
