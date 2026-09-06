

# Aurora PostgreSQL pg\_columnmask data movement scenarios
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement"></a>

`pg_columnmask` behavior varies across different data movement operations depending on whether the operation occurs at the storage, logical, or application layer. Storage-level operations (such as cloning) behave differently from logical operations (such as `pg_dump`) and application-level operations (such as FDW queries). This section describes masking behavior for common scenarios including replication, backups, exports, and migrations, and explains the security implications for each.

**Topics**
+ [Aurora Global Database and Read Replicas](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.RR)
+ [Database clone and snapshot restore](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.Clones)
+ [Logical replication](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.LogRep)
+ [Blue/Green deployments](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.BlueGreen)
+ [Zero-ETL and CDC streams](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.ZETL)
+ [AWS Database Migration Service](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.DMS)
+ [Data exports](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.DataExport)
+ [Views and materialized views](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.Views)
+ [Data dump and restore](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.DDR)
+ [Foreign data wrapper](#AuroraPostgreSQL.Security.DynamicMasking.DataMovement.FDQ)

## Aurora Global Database and Read Replicas
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.RR"></a>

Aurora `pg_columnmask` policies are stored in database system tables within the cluster volume. All replicas access the same policies and return consistently masked results. For Aurora Global Database deployments, `pg_columnmask` policies replicate to secondary AWS Regions along with other database system tables, ensuring consistent data protection across regions. During failover scenarios, all `pg_columnmask` policies remain intact and functional.

## Database clone and snapshot restore
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.Clones"></a>

Aurora Fast Clone and snapshot restore operations preserve all `pg_columnmask` policies, roles, and configurations as part of the database system tables. The cloned or restored database inherits all existing policies from the source cluster. After cloning or restoration, each database cluster maintains independent `pg_columnmask` policies.

## Logical replication
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.LogRep"></a>

During initial synchronization, logical replication uses standard SQL COPY operations, and `pg_columnmask` policies are enforced based on the replication user's permissions. During ongoing CDC (change data capture), masking policies are not applied and unmasked data is replicated through WAL records. Users with `pg_create_subscription` privileges can potentially exfiltrate unmasked data by setting up replication to a system they control.

## Blue/Green deployments
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.BlueGreen"></a>

During snapshot restoration, `pg_columnmask` policies are automatically included. The green environment starts with an identical copy of all policies from the blue environment. During replication from blue to green, data is not masked. Subsequent masking policy changes (DDL commands) on the blue cluster do not replicate to the green cluster and invalidate RDS blue/green deployments.

## Zero-ETL and CDC streams
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.ZETL"></a>

Data replication is not affected by `pg_columnmask` policies. Zero-ETL supports DDL replication but doesn't replicate `pg_columnmask` or RLS policies. No masking policies are applied to replicated data in Zero-ETL.

## AWS Database Migration Service
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.DMS"></a>

Initial data sync is masked or unmasked based on the user selected for the DMS task. CDC data is always unmasked. While `pg_columnmask` related internal RLS policies may be migrated, they won't function on non-pg\_columnmask-enabled targets.

## Data exports
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.DataExport"></a>

`pg_columnmask` treats exports like any other query operation—masking is applied based on the executing user's permissions. This applies to SQL commands like COPY, SELECT INTO, CREATE TABLE AS, and Aurora PostgreSQL's S3 export functionality. 

**Note**  
When masked users export data, the resulting files contain masked values that may violate database constraints when restored.

## Views and materialized views
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.Views"></a>

Keep the following considerations in mind when using views:
+ **Regular views** – Always use `INVOKER` semantics. The current user's masking policies apply when querying the view, regardless of who created the view.
+ **Materialized views** – When refreshed, the masking policies of the materialized view owner apply, not the policies of the user performing the refresh. If the owner has masking policies, the materialized view always contains masked data.

## Data dump and restore
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.DDR"></a>

`pg_dump` operates as a regular database user and applies masking policies based on the connecting user's permissions. If a masked user performs a dump, the backup file contains masked data. `pg_columnmask` policies are included in the dump as part of the database schema. Successful restoration requires that all referenced roles exist in the target database and that the target has the `pg_columnmask` extension installed.

**Note**  
Starting with PostgreSQL 18, `pg_dump` supports the `—no-policies` option which excludes both Row Level Security (RLS) and `pg_columnmask` masking policies from database dumps. For more information, see [pg\_dump](https://www.postgresql.org/docs/current/app-pgdump.html).

## Foreign data wrapper
<a name="AuroraPostgreSQL.Security.DynamicMasking.DataMovement.FDQ"></a>

When using foreign data wrappers, masking policies on remote tables are applied based on the mapped user's permissions on the source server, not the local querying user's permissions, and while you can access masked remote data through FDW, you cannot create DDM or RLS policies directly on foreign tables in your local database.