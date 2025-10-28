# Performing disaster recovery Amazon Neptune

A Neptune global database provides more comprehensive failover capabilities than
a standalone Neptune DB cluster does. Using a global database, you can plan for
and recover from disaster fairly quickly. Disaster recovery is generally assessed
using evaluation of the recovery-time objective (RTO) and the recovery-point objective
(RPO):

- **Recovery-time objective (RTO)**   —  
  This is how fast a system returns to a working state after a disaster. In other
  words, RTO measures downtime. For a Neptune global database, RTO can be in the
  order of minutes.
- **Recovery-point objective (RPO)**   —  
  The amount of time during which data is being lost. For a Neptune global database,
  RPO is typically measured in seconds (see [Performing managed planned failovers
  for Neptune global databases](#neptune-gdb-managed-failover "#neptune-gdb-managed-failover")).
  For a Neptune global database, there are two different approaches to failover:

- **Detach-and-promote (manual unplanned recovery)**   —  
  To recover from an unplanned outage or to do disaster-recovery testing (DR testing),
  perform a cross-region detach-and-promote on one of the secondary DB clusters in the global database.
  The RTO for this manual process depends on how quickly you can perform the tasks listed in
  [Detach and promote](#neptune-gdb-detach-and-promote "#neptune-gdb-detach-and-promote"). The
  RPO is typically a number of seconds, but this depends on the storage replication lag
  across the network at the time of the failure.
- **Managed planned failover**   —  
  This approach is intended for operational maintenance and other planned operational
  procedures such as relocating the primary DB cluster of the global database to one
  of the secondary regions. Because this process synchronizes secondary DB clusters
  with the primary before making any other changes, RPO is effectively 0 (that is,
  there is no data loss). See [Performing managed planned failovers
  for Neptune global databases](#neptune-gdb-managed-failover "#neptune-gdb-managed-failover").

## Detach-and-promote a Neptune global database

in the case of an unplanned outage

In the very rare situation where your Neptune global database experiences an
unexpected outage in its primary AWS Region, your primary Neptune DB cluster and its
writer node become unavailable, and the replication between the primary cluster and
the secondaries ceases. To minimize both the resulting downtime (RTO) and data loss
(RPO), quickly perform a cross-region detach-and-promote to reconstruct the global
database.

###### Tip

It's a good idea to understand this process before using it, and have a
plan in place to proceed quickly at the first sign of a region-wide issue.

- Use Amazon CloudWatch regularly to track lag times for the secondary clusters
  so that you can identify the secondary region with the smallest lag time if you
  need to fail over.
- Make sure to test your plan to check that your procedures are
  complete and accurate.
- Use a simulated environment to make sure your staff is trained and ready
  to perform a DR failover rapidly if it ever becomes necessary.

###### To fail over to a secondary cluster after an unplanned outage in the primary region

1. Stop issuing mutation queries and other write operations on the primary DB
   cluster.
2. Identify a DB cluster in a secondary AWS Region to use as the new primary
   DB cluster of the global database. If the global database has two or more secondary
   AWS Regions, choose the secondary cluster that has the smallest lag time.
3. Detach that secondary DB cluster that you chose from the Neptune global database.

Removing a secondary DB cluster from a Neptune global database immediately stops the
replication of data from the primary to that secondary and promotes it to a standalone
DB cluster with full read/write capabilities. Any other secondary clusters in the global
database will still be available and can accept read calls from your application.

Before recreating the Neptune global database, you will also have to detach the
other secondary clusters to avoid data inconsistencies among the clusters (see [Removing a cluster](neptune-gdb-detaching.md "neptune-gdb-detaching.md")). 4. Reconfigure your application to send all write operations to the standalone Neptune
DB cluster that you chose to become the new primary cluster, using its new endpoint.
If you accepted the default names when you created the Neptune global database, you
can change the endpoint by removing the `-ro` from the cluster's endpoint
string in your application.

For example, the secondary cluster's endpoint
`my-global.cluster-**ro**-aaaaaabbbbbb.us-west-1.neptune.amazonaws.com`
becomes `my-global.cluster-aaaaaabbbbbb.us-west-1.neptune.amazonaws.com` when
that cluster is detached from the global database.

This Neptune DB cluster becomes the primary cluster of a new Neptune
global database when you start adding regions to it in the next step. 5. Add an AWS Region to the DB cluster. When you do this, the replication
process from primary to secondary begins. See [Adding secondary global
database regions to a primary region in Amazon Neptune](neptune-gdb-setup.md#neptune-gdb-attaching "neptune-gdb-setup.md#neptune-gdb-attaching") . 6. Add more AWS Regions as needed to recreate the topology needed to support your
application.

Make sure that application writes are sent to the correct Neptune DB cluster before,
during, and after making these changes. Doing this avoids data inconsistencies among the DB
clusters in the Neptune global database (these are known as split-brain issues).

## Performing managed planned failovers

for Neptune global databases

Managed planned failover lets you relocate the primary cluster of your Neptune
global database to a different AWS Region whenever you choose. Some organizations
will want to rotate their primary cluster locations on a regular basis.

###### Note

The managed planned failover process described here is intended to be
used on a healthy Neptune global database. To recover from an unplanned outage
or to do disaster recovery (DR) testing, follow the [detach and promote](#neptune-gdb-detach-and-promote "#neptune-gdb-detach-and-promote") process instead.

During a managed planned failover, your primary cluster is failed over to your
choice of secondary region while your global database's existing replication
topology is preserved. Before the managed planned failover process begins,
the global database synchronizes all secondary clusters with its primary cluster.
After ensuring that all clusters are synchronized, the managed planned failover
begins. The DB cluster in the primary region becomes read-only, and
the chosen secondary cluster promotes one of its read-only instances to full
writer status, thus allowing the cluster to assume the role of primary cluster.
Because all secondary clusters were synchronized with the primary at the start
of the process, the new primary continues operations for the global database
without losing any data. The database is only unavailable for a short time while
the primary and selected secondary clusters are assuming their new roles.

To optimize application availability, perform the failover during nonpeak
hours, at a time when writes to the primary DB cluster are minimal. Also, take
the following steps before starting the failover:

- Take applications offline wherever possible to reduce writes
  to the primary cluster.
- Check lag times for all secondary Neptune DB clusters in
  the global database and choose the secondary with the least overall lag time
  to become the primary. Use Amazon CloudWatch to view the `NeptuneGlobalDBProgressLag`
  metric for all secondaries. This metric tells you how far a secondary is behind
  the primary DB cluster, in milliseconds. Its value is directly proportional to
  the time Neptune will take to complete the failover. In other words, the
  larger the lag value, the longer the failover outage will be, so choose the
  secondary with the least lag. See [Neptune CloudWatch Metrics](cw-metrics.md "cw-metrics.md") for more information.

During a managed planned failover, the chosen secondary DB cluster is
promoted to its new role as primary but it doesn't inherit the complete
configuration of the primary DB cluster. A mismatch in configuration can
lead to performance issues, workload incompatibilities, and other anomalous
behavior. To avoid such issues, resolve the following kinds of configuration
differences between global database clusters before failover:

- **Configure parameters
  in the new primary to match the current primary**.
- **Configure monitoring tools, options, and alarms**   —  
  Configure the DB cluster that will be the new primary with the same logging
  ability, alarms, and so on that the current primary has.
- **Configure integrations with other AWS services**   —  
  If your Neptune global database integrates with AWS services, such as AWS Identity and Access Management (IAM),
  Amazon S3, or AWS Lambda, make sure these are configured as needed to integrate with
  the new primary DB cluster.

When the failover process completes and the promoted DB cluster is ready to
handle write operations for the global database, make sure to change your application(s)
to use the the new endpoint for the new primary.

### Using the AWS CLI to initiate managed planned failover

Use the [failover-global-cluster](../../../cli/latest/reference/rds/failover-global-cluster.md "../../../cli/latest/reference/rds/failover-global-cluster.md")
CLI command (which wraps the [FailoverGlobalCluster](api-global-dbs.md#FailoverGlobalCluster "api-global-dbs.md#FailoverGlobalCluster") API) to fail over your Neptune global
database:

```
aws neptune failover-global-cluster \
  --region `(the region where the primary cluster is located)` \
  --global-cluster-identifier `(global database ID)` \
  --target-db-cluster-identifier `(the ARN of the secondary DB cluster to promote)`
```
