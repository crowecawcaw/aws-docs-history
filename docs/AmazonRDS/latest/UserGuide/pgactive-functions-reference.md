

# pgactive functions reference
<a name="pgactive-functions-reference"></a>

Following, you can find a list of pgactive functions with their parameters, return values, and practical usage notes to help you effectively use them:

## get\_last\_applied\_xact\_info
<a name="get-last-applied-xact-info"></a>

Retrieves the last applied transaction information for a specified node.

**Arguments**  
+ sysid (text) - timeline OID
+ dboid (OID)

**Return type**  
It records the following:  
+ last\_applied\_xact\_id (OID)
+ last\_applied\_xact\_committs (timestamp with time zone)
+ last\_applied\_xact\_at (timestamp with time zone)

**Usage notes**  
Use this function to retrieve the last applied transaction information for a specified node.

## pgactive\_apply\_pause
<a name="pgactive-apply-pause"></a>

Pauses the replication apply process.

**Arguments**  
None

**Return type**  
boolean

**Usage notes**  
Call this function to pause the replication apply process.

## pgactive\_apply\_resume
<a name="pgactive-apply-resume"></a>

Resumes the replication apply process.

**Arguments**  
None

**Return type**  
void

**Usage notes**  
Call this function to resume the replication apply process.

## pgactive\_is\_apply\_paused
<a name="pgactive-is-apply-paused"></a>

Checks if replication apply is currently paused.

**Arguments**  
None

**Return type**  
boolean

**Usage notes**  
Use this function to check if replication apply is currently paused.

## pgactive\_create\_group
<a name="pgactive-create-group"></a>

Creates a pgactive group by converting a standalone database into the initial node.



**Arguments**  
+ node\_name (text)
+ node\_dsn (text)
+ apply\_delay integer DEFAULT NULL::integer - replication\_sets text[] DEFAULT ARRAY[‘default’::text]

**Return type**  
void

**Usage notes**  
Creates a pgactive group by converting a standalone database into the initial node. The function performs sanity checks before transforming the node into a pgactive node. Before using this function, ensure that your PostgreSQL cluster has sufficient `max_worker_processes` available to support pgactive background workers.

## pgactive\_detach\_nodes
<a name="pgactive-detach-nodes"></a>

Removes specified nodes from the pgactive group.

**Arguments**  
+ p\_nodes (text[])

**Return type**  
void

**Usage notes**  
Use this function to remove specified nodes from the pgactive group.

## pgactive\_exclude\_table\_replication\_set
<a name="pgactive-exclude-table-replication-set"></a>

Excludes a specific table from replication.

**Arguments**  
+ p\_relation (regclass)

**Return type**  
void

**Usage notes**  
Use this function to exclude a specific table from replication.

## pgactive\_get\_replication\_lag\_info
<a name="pgactive-get-replication-lag-info"></a>

Retrieves detailed replication lag information, including node details, WAL status, and LSN values.

**Arguments**  
None

**Return type**  
SETOF record - node\_name text - node\_sysid text - application\_name text - slot\_name text - active boolean - active\_pid integer - pending\_wal\_decoding bigint - Approximate size of WAL in bytes to be decoded on the sender node - pending\_wal\_to\_apply bigint - Approximate size of WAL in bytes to be applied on receiving node - restart\_lsn pg\_lsn - confirmed\_flush\_lsn pg\_lsn - sent\_lsn pg\_lsn - write\_lsn pg\_lsn - flush\_lsn pg\_lsn - replay\_lsn pg\_lsn

**Usage notes**  
Call this function to retrieve replication lag information, including node details, WAL status, and LSN values.

## pgactive\_get\_stats
<a name="pgactive-get-stats"></a>

Retrieves pgactive replication statistics.

**Arguments**  
None

**Return type**  
SETOF record - rep\_node\_id oid - rilocalid oid - riremoteid text - nr\_commit bigint - nr\_rollback bigint - nr\_insert bigint - nr\_insert\_conflict bigint - nr\_update bigint - nr\_update\_conflict bigint - nr\_delete bigint - nr\_delete\_conflict bigint - nr\_disconnect bigint

**Usage notes**  
Use this function to retrieve pgactive replication statistics.

## pgactive\_get\_table\_replication\_sets
<a name="pgactive-get-table-replication-sets"></a>

Gets replication set configuration for a specific relation.

**Arguments**  
+ relation (regclass)

**Return type**  
SETOF record

**Usage notes**  
Call this function to get replication set configuration for a specific relation.

## pgactive\_include\_table\_replication\_set
<a name="pgactive-include-table-replication-set"></a>

Includes a specific table in replication.

**Arguments**  
+ p\_relation (regclass)

**Return type**  
void

**Usage notes**  
Use this function to include a specific table in replication.

## pgactive\_join\_group
<a name="pgactive-join-group"></a>

Adds a node to an existing pgactive group.

**Arguments**  
+ node\_name (text)
+ node\_dsn (text)
+ join\_using\_dsn (text)
+ apply\_delay (integer, optional)
+ replication\_sets (text[], default: ['default'])
+ bypass\_collation\_check (boolean, default: false)
+ bypass\_node\_identifier\_creation (boolean, default: false)
+ bypass\_user\_tables\_check (boolean, default: false)

**Return type**  
void

**Usage notes**  
Call this function to add a node to an existing pgactive group. Ensure your PostgreSQL cluster has sufficient max\_worker\_processes for pgactive background workers.

## pgactive\_remove
<a name="pgactive-remove"></a>

Removes all pgactive components from the local node.

**Arguments**  
+ force (boolean, default: false)

**Return type**  
void

**Usage notes**  
Call this function to remove all pgactive components from the local node.

## pgactive\_snowflake\_id\_nextval
<a name="pgactive-snowflake-id-nextval"></a>

Generates node-specific unique sequence values.

**Arguments**  
+ regclass

**Return type**  
bigint

**Usage notes**  
Use this function to generate node-specific unique sequence values.

## pgactive\_update\_node\_conninfo
<a name="pgactive-update-node-conninfo"></a>

Updates connection information for a pgactive node.

**Arguments**  
+ node\_name\_to\_update (text)
+ node\_dsn\_to\_update (text)

**Return type**  
void

**Usage notes**  
Use this function to update connection information for a pgactive node.

## pgactive\_wait\_for\_node\_ready
<a name="pgactive-wait-for-node-ready"></a>

Monitors the progress of group creation or joining operations.

**Arguments**  
+ timeout (integer, default: 0)
+ progress\_interval (integer, default: 60)

**Return type**  
void

**Usage notes**  
Call this function to monitor the progress of group creation or joining operations.