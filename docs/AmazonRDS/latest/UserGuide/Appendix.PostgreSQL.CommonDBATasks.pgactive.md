

# Using pgactive to support active-active replication
<a name="Appendix.PostgreSQL.CommonDBATasks.pgactive"></a>

The `pgactive` extension uses active-active replication to support and coordinate write operations on multiple RDS for PostgreSQL databases. Amazon RDS for PostgreSQL supports the `pgactive` extension on the following versions: 
+ RDS for PostgreSQL 17.0 and all higher versions
+ RDS for PostgreSQL 16.1 and higher 16 versions
+ RDS for PostgreSQL 15.4-R2 and higher 15 versions
+ RDS for PostgreSQL 14.10 and higher 14 versions
+ RDS for PostgreSQL 13.13 and higher 13 versions
+ RDS for PostgreSQL 12.17 and higher 12 versions
+ RDS for PostgreSQL 11.22

**Note**  
When there are write operations on more than one database in a replication configuration, conflicts are possible. For more information, see [Handling conflicts in active-active replication](Appendix.PostgreSQL.CommonDBATasks.pgactive.handle-conflicts.md)

**Topics**
+ [Limitations for the pgactive extension](#Appendix.PostgreSQL.CommonDBATasks.pgactive.requirements-limitations)
+ [Initializing the pgactive extension capability](Appendix.PostgreSQL.CommonDBATasks.pgactive.basic-setup.md)
+ [Setting up active-active replication for RDS for PostgreSQL DB instances](Appendix.PostgreSQL.CommonDBATasks.pgactive.setup-replication.md)
+ [Measuring replication lag among pgactive members](Appendix.PostgreSQL.CommonDBATasks.pgactive.replicationlag.md)
+ [Configuring parameter settings for the pgactive extension](Appendix.PostgreSQL.CommonDBATasks.pgactive.parameters.md)
+ [Understanding active-active conflicts](Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.replication.md)
+ [Understanding the pgactive schema](Appendix.PostgreSQL.CommonDBATasks.pgactive.schema.md)
+ [pgactive functions reference](pgactive-functions-reference.md)
+ [Handling conflicts in active-active replication](Appendix.PostgreSQL.CommonDBATasks.pgactive.handle-conflicts.md)
+ [Handling sequences in active-active replication](Appendix.PostgreSQL.CommonDBATasks.pgactive.handle-sequences.md)

## Limitations for the pgactive extension
<a name="Appendix.PostgreSQL.CommonDBATasks.pgactive.requirements-limitations"></a>
+ All tables require a Primary Key, otherwise Update's and Delete's aren't allowed. The values in the Primary Key column shouldn't be updated.
+ Sequences may have gaps and sometimes might not follow an order. Sequences are not replicated. For more information, see [Handling sequences in active-active replication](Appendix.PostgreSQL.CommonDBATasks.pgactive.handle-sequences.md).
+ DDL and large objects are not replicated.
+ Secondary unique indexes can cause data divergence.
+ Collation needs to be identical on all node in the group.
+ Load balancing across nodes is an anti-pattern.
+ Large transactions can cause replication lag.