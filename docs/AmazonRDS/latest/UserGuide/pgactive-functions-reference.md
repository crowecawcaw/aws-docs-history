# pgactive functions reference

Following, you can find a list of pgactive functions with their parameters, return values,
and practical usage notes to help you effectively use them:

## get_last_applied_xact_info

Retrieves the last applied transaction information for a specified node.

**Arguments**

- sysid (text) - timeline OID
- dboid (OID)

**Return type**

It records the following:

- last_applied_xact_id (OID)
- last_applied_xact_committs (timestamp with time zone)
- last_applied_xact_at (timestamp with time zone)

**Usage notes**

Use this function to retrieve the last applied transaction information for a
specified node.

## pgactive_apply_pause

Pauses the replication apply process.

**Arguments**

None

**Return type**

boolean

**Usage notes**

Call this function to pause the replication apply process.

## pgactive_apply_resume

Resumes the replication apply process.

**Arguments**

None

**Return type**

void

**Usage notes**

Call this function to resume the replication apply process.

## pgactive_is_apply_paused

Checks if replication apply is currently paused.

**Arguments**

None

**Return type**

boolean

**Usage notes**

Use this function to check if replication apply is currently paused.

## pgactive_create_group

Creates a pgactive group by converting a standalone database into the initial node.

**Arguments**

- node_name (text)
- node_dsn (text)
- apply_delay integer DEFAULT NULL::integer - replication_sets text[] DEFAULT
  ARRAY[‘default’::text]

**Return type**

void

**Usage notes**

Creates a pgactive group by converting a standalone database into the initial
node. The function performs sanity checks before transforming the node into a pgactive
node. Before using this function, ensure that your PostgreSQL cluster has sufficient
`max_worker_processes` available to support pgactive background
workers.

## pgactive_detach_nodes

Removes specified nodes from the pgactive group.

**Arguments**

- p_nodes (text[])

**Return type**

void

**Usage notes**

Use this function to remove specified nodes from the pgactive group.

## pgactive_exclude_table_replication_set

Excludes a specific table from replication.

**Arguments**

- p_relation (regclass)

**Return type**

void

**Usage notes**

Use this function to exclude a specific table from replication.

## pgactive_get_replication_lag_info

Retrieves detailed replication lag information, including node details, WAL status, and LSN values.

**Arguments**

None

**Return type**

SETOF record - node_name text - node_sysid text - application_name text -
slot_name text - active boolean - active_pid integer - pending_wal_decoding bigint -
Approximate size of WAL in bytes to be decoded on the sender node -
pending_wal_to_apply bigint - Approximate size of WAL in bytes to be applied on
receiving node - restart_lsn pg_lsn - confirmed_flush_lsn pg_lsn - sent_lsn pg_lsn -
write_lsn pg_lsn - flush_lsn pg_lsn - replay_lsn pg_lsn

**Usage notes**

Call this function to retrieve replication lag information, including node
details, WAL status, and LSN values.

## pgactive_get_stats

Retrieves pgactive replication statistics.

**Arguments**

None

**Return type**

SETOF record - rep_node_id oid - rilocalid oid - riremoteid text - nr_commit
bigint - nr_rollback bigint - nr_insert bigint - nr_insert_conflict bigint - nr_update
bigint - nr_update_conflict bigint - nr_delete bigint - nr_delete_conflict bigint -
nr_disconnect bigint

**Usage notes**

Use this function to retrieve pgactive replication statistics.

## pgactive_get_table_replication_sets

Gets replication set configuration for a specific relation.

**Arguments**

- relation (regclass)

**Return type**

SETOF record

**Usage notes**

Call this function to get replication set configuration for a specific
relation.

## pgactive_include_table_replication_set

Includes a specific table in replication.

**Arguments**

- p_relation (regclass)

**Return type**

void

**Usage notes**

Use this function to include a specific table in replication.

## pgactive_join_group

Adds a node to an existing pgactive group.

**Arguments**

- node_name (text)
- node_dsn (text)
- join_using_dsn (text)
- apply_delay (integer, optional)
- replication_sets (text[], default: ['default'])
- bypass_collation_check (boolean, default: false)
- bypass_node_identifier_creation (boolean, default: false)
- bypass_user_tables_check (boolean, default: false)

**Return type**

void

**Usage notes**

Call this function to add a node to an existing pgactive group. Ensure your
PostgreSQL cluster has sufficient max_worker_processes for pgactive background
workers.

## pgactive_remove

Removes all pgactive components from the local node.

**Arguments**

- force (boolean, default: false)

**Return type**

void

**Usage notes**

Call this function to remove all pgactive components from the local node.

## pgactive_snowflake_id_nextval

Generates node-specific unique sequence values.

**Arguments**

- regclass

**Return type**

bigint

**Usage notes**

Use this function to generate node-specific unique sequence values.

## pgactive_update_node_conninfo

Updates connection information for a pgactive node.

**Arguments**

- node_name_to_update (text)
- node_dsn_to_update (text)

**Return type**

void

**Usage notes**

Use this function to update connection information for a pgactive node.

## pgactive_wait_for_node_ready

Monitors the progress of group creation or joining operations.

**Arguments**

- timeout (integer, default: 0)
- progress_interval (integer, default: 60)

**Return type**

void

**Usage notes**

Call this function to monitor the progress of group creation or joining
operations.
