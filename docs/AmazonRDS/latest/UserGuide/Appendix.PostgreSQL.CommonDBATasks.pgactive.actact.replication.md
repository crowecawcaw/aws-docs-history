# Understanding active-active conflicts

When you use pgactive in active-active mode, writing to the same tables from multiple
nodes can create data conflicts. While some clustering systems use distributed locks to
prevent concurrent access, pgactive takes an optimistic approach that's better suited for
geographically distributed applications.

Some database clustering systems prevent concurrent data access by using distributed
locks. While this approach works when servers are in close proximity, it doesn't support
geographically distributed applications because it requires extremely low latency for good
performance. Instead of using distributed locks (a pessimistic approach), the pgactive
extension uses an optimistic approach. This means it:

- Helps you avoid conflicts when possible.
- Allows certain types of conflicts to occur.
- Provides conflict resolution when conflicts happen.
  This approach gives you more flexibility when building distributed applications.

## How conflicts happen

Inter-node conflicts arise from sequences of events that could not happen if all the
involved transactions occurred concurrently on the same node. Because the nodes only
exchange changes after transactions commit, each transaction is individually valid on the
node it committed on but would not be valid if run on another node that has done other work
in the meantime. Since pgactive apply essentially replays the transaction on the other
nodes, the replay operation can fail if there is a conflict between a transaction being
applied and a transaction that was committed on the receiving node.

The reason most conflicts can't happen when all transactions run on a single node is
that PostgreSQL has inter-transaction communication mechanisms to prevent it,
including:

- UNIQUE indexes
- SEQUENCEs
- Row and relation locking
- SERIALIZABLE dependency tracking

All of these mechanisms are ways to communicate between transactions to prevent
undesirable concurrency issues

pgactive achieves low latency and handles network partitions well because it doesn't use
a distributed transaction manager or lock manager. However, this means transactions on
different nodes run in complete isolation from each other. While isolation typically
improves database consistency, in this case, you need to reduce isolation to prevent
conflicts.

## Types of conflicts

Conflicts that can occur include:

###### Topics

- [PRIMARY KEY or UNIQUE conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict1 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict1")
- [INSERT/INSERT conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict2 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict2")
- [INSERTs that violate multiple UNIQUE constraints](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict3 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict3")
- [UPDATE/UPDATE conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict4 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict4")
- [UPDATE conflicts on the PRIMARY KEY](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict5 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict5")
- [UPDATEs that violate multiple UNIQUE constraints](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict6 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict6")
- [UPDATE/DELETE conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict7 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict7")
- [INSERT/UPDATE conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict8 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict8")
- [DELETE/DELETE conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict9 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict9")
- [Foreign Key Constraint conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict10 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict10")
- [Exclusion constraint conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict11 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict11")
- [Global data conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict12 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict12")
- [Lock conflicts and deadlock aborts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict13 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict13")
- [Divergent conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict14 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict14")

### PRIMARY KEY or UNIQUE conflicts

Row conflicts occur when multiple operations attempt to modify the same row key in
ways not possible on a single node. These conflicts represent the most common type of data
conflicts.

pgactive resolves detected conflicts through last-update-wins handling or your custom
conflict handler.

Row conflicts include:

- INSERT vs INSERT
- INSERT vs UPDATE
- UPDATE vs DELETE
- INSERT vs DELETE
- DELETE vs DELETE
- INSERT vs DELETE

### INSERT/INSERT conflicts

This most common conflict occurs when INSERTs on two different nodes create a tuple
with the same PRIMARY KEY values (or identical UNIQUE constraint values when no PRIMARY
KEY exists).

pgactivelink resolves INSERT conflicts by using the timestamp from the originating
host to keep the most recent tuple. You can override this default behavior with your
custom conflict handler. While this process requires no special administrator action, be
aware that pgactivelink discards one of the INSERT operations across all nodes. No
automatic data merging occurs unless your custom handler implements it.

The pgactivelink can only resolve conflicts involving a single constraint violation.
If an INSERT violates multiple UNIQUE constraints, you must implement additional conflict
resolution strategies.

### INSERTs that violate multiple UNIQUE constraints

An INSERT/INSERT conflict can violate multiple UNIQUE constraints, including the
PRIMARY KEY. pgactivelink can only handle conflicts that involve a single UNIQUE
constraint. When conflicts violate multiple UNIQUE constraints, the apply worker fails and
returns the following error:

`multiple unique constraints violated by remotely INSERTed tuple.`

In older versions, this situation generated a 'diverging uniqueness conflict' error
instead.

To resolve these conflicts, you must take manual action. Either DELETE the conflicting
local tuples or UPDATE them to remove conflicts with the new remote tuple. Be aware that
you might need to address multiple conflicting tuples. Currently, pgactivelink provides no
built-in functionality to ignore, discard, or merge tuples that violate multiple unique
constraints.

###### Note

For more information, see UPDATEs that violate multiple UNIQUE constraints.

### UPDATE/UPDATE conflicts

This conflict occurs when two nodes concurrently modify the same tuple without
changing its PRIMARY KEY. pgactivelink resolves these conflicts using last-update-wins
logic or your custom conflict handler, if defined. A PRIMARY KEY is essential for tuple
matching and conflict resolution. For tables without a PRIMARY KEY, pgactivelink rejects
UPDATE operations with the following error:

`Cannot run UPDATE or DELETE on table (tablename) because it does not have a
 primary key.`

### UPDATE conflicts on the PRIMARY KEY

pgactive has limitations when handling PRIMARY KEY updates. While you can perform
UPDATE operation on a PRIMARY KEY, pgactive can't automatically resolve conflicts using
last-update-wins logic for these operations. You must ensure that your PRIMARY KEY updates
don't conflict with existing values. If conflicts occur during PRIMARY KEY updates, they
become divergent conflicts that require your manual intervention. For more information
about handling these situations, see [Divergent conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict14 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict14").

### UPDATEs that violate multiple UNIQUE constraints

pgactivelink cannot apply last-update-wins conflict resolution when an incoming UPDATE
violates multiple UNIQUE constraints or PRIMARY KEY values. This behavior is similar to
INSERT operations with multiple constraint violations. These situations create divergent
conflicts that require your manual intervention. For more information, see [Divergent conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict14 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict14").

### UPDATE/DELETE conflicts

This conflicts occur when one node UPDATEs a row while another node simultaneously
DELETEs it. In this case a UPDATE/DELETE conflict occurs on replay. The resolution is to
discard any UPDATE that arrives after a DELETE, unless your custom conflict handler
specifies otherwise.

pgactivelink requires a PRIMARY KEY to match tuples and resolve conflicts. For tables
without a PRIMARY KEY, it rejects DELETE operations with the following error:

`Cannot run UPDATE or DELETE on table (tablename) because it does not have a
 primary key.`

###### Note

pgactivelink cannot distinguish between UPDATE/DELETE and INSERT/UPDATE conflicts.
In both cases, an UPDATE affects a nonexistent row. Due to asynchronous replication and
lack of replay ordering between nodes, pgactivelink can't determine if the UPDATE is for
a new row (INSERT not yet received) or a deleted row. In both scenarios, pgactivelink
discards the UPDATE.

### INSERT/UPDATE conflicts

This conflict can occur in multi-node environments. It happens when one node INSERTs a
row, a second node UPDATEs it, and a third node receives the UPDATE before the original
INSERT. By default, pgactivelink resolves these conflicts by discarding the UPDATE, unless
your custom conflict trigger specifies otherwise. Be aware that this resolution method can
result in data inconsistencies across nodes. For more information about similar scenarios
and their handling, see [UPDATE/DELETE conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict7 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict7").

### DELETE/DELETE conflicts

This conflict occurs when two different nodes concurrently delete the same tuple.
pgactivelink considers these conflicts harmless because both DELETE operations have the
same end result. In this scenario, pgactivelink safely ignores one of the DELETE
operations without affecting data consistency.

### Foreign Key Constraint conflicts

FOREIGN KEY constraints can cause conflicts when applying remote transactions to
existing local data. These conflicts typically occur when transactions are applied in a
different sequence than their logical order on the originating nodes.

By default, pgactive applies changes with session_replication_role as
`replica`, which bypasses foreign key checks during replication. In
active-active configurations, this can lead to foreign key violations. Most violations are
temporary and resolve once replication catches up. However, dangling foreign keys can
occur because pgactive doesn't support cross-node row locking.

This behavior is inherent to partition-tolerant asynchronous active-active systems.
For example, node A might insert a new child row while node B simultaneously deletes its
parent row. The system can't prevent this type of concurrent modification across
nodes.

To minimize foreign key conflicts, we recommend the following:

- Limit foreign key relationships to closely related entities.
- Modify related entities from a single node when possible.
- Choose entities that rarely require modification.
- Implement application-level concurrency control for modifications.

### Exclusion constraint conflicts

pgactive link doesn’t support exclusion constraints and restricts their
creation.

###### Note

If you convert an existing standalone database to a pgactivelink database, manually
drop all exclusion constraints.

In a distributed asynchronous system, it's not possible to guarantee that no set of
rows violates the constraint. This is because all transactions on different nodes are
fully isolated. Exclusion constraints can lead to replay deadlocks, where replay can't
progress from any node to another due to exclusion constraint violations.

If you force pgactive Link to create an exclusion constraint, or if you don't drop
existing ones when converting a standalone database to pgactive Link, replication is
likely to break. To restore replication progress, remove or alter the local tuples that
conflict with an incoming remote tuple so that the remote transaction can be
applied.

### Global data conflicts

When using pgactivelink, conflicts can occur when nodes have different global
PostgreSQL system-wide data, such as roles. These conflicts can cause operations—primarily
DDL—to succeed and commit on one node but fail to apply to other nodes.

If a user exists on one node but not another, replication issues can occur:

- Node1 has a user named `fred`, but this user doesn't exist on
  Node2
- When `fred` creates a table on Node1, the table is replicated with
  `fred` as the owner
- When this DDL command is applied to Node2, it fails because user `fred`
  doesn't exist
- This failure generates an ERROR in the PostgreSQL logs on Node2 and increments the
  `pgactive.pgactive_stats.nr_rollbacks` counter

**Resolution:** Create the user `fred` on
Node2. The user doesn't need identical permissions but must exist on both nodes.

If a table exists on one node but not another, data modification operations will
fail:

- Node1 has a table named `foo` that doesn't exist on Node2
- Any DML operations on the `foo` table on Node1 will fail when
  replicated to Node2

**Resolution:** Create the table `foo` on
Node2 with the same structure.

###### Note

pgactivelink doesn't currently replicate CREATE USER commands or DDL operations. DDL
replication is planned for a future release.

### Lock conflicts and deadlock aborts

Because pgactive apply processes operate like normal user sessions, they follow
standard row and table locking rules. This can result in pgactivelink apply processes
waiting on locks held by user transactions or by other apply processes.

The following types of locks can affect apply processes:

- Explicit table-level locking (LOCK TABLE ...) by user sessions
- Explicit row-level locking (SELECT ... FOR UPDATE/FOR SHARE) by user
  sessions
- Locking from foreign keys
- Implicit locking due to row UPDATEs, INSERTs, or DELETEs, either from local
  activity or apply from other servers

Deadlocks can occur between:

- A pgactivelink apply process and a user transaction
- Two apply processes

When deadlocks occur, PostgreSQL's deadlock detector terminates one of the problem
transactions. If the pgactivelink apply worker's process is terminated, it automatically
retries and typically succeeds.

###### Note

- These issues are temporary and generally don't require administrator
  intervention. If an apply process is blocked for an extended period by a lock on an
  idle user session, you can terminate the user session to resume replication. This
  situation is similar to when a user holds a long lock that affects another user
  session.
- To identify locking-related replay delays, enable the
  `log_lock_waits` facility in PostgreSQL.

### Divergent conflicts

Divergent conflicts occur when data that should be identical across nodes differs unexpectedly. While these conflicts shouldn't happen, not all can be reliably prevented in the current implementation.

###### Note

Modifying a row's PRIMARY KEY can cause divergent conflicts if another node changes the same row's key before all nodes process the change. Avoid changing primary keys, or restrict changes to one designated node.
For more information, see [UPDATE conflicts on the PRIMARY KEY](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict5 "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflict5").

Divergent conflicts involving row data typically require administrator intervention. To resolve these conflicts, you must manually adjust data on one node to match another while temporarily disabling replication
using `pgactive.pgactive_do_not_replicate`. These conflicts shouldn't occur when you use pgactive as documented and avoid settings or functions marked as unsafe.

As an administrator, you must manually resolve these conflicts. Depending on the conflict type, you'll need to use advanced options like `pgactive.pgactive_do_not_replicate`. Use these options with caution, as
improper use can worsen the situation. Due to the variety of possible conflicts, we can't provide universal resolution instructions.

Divergent conflicts occur when data that should be identical across different nodes
unexpectedly differs. While these conflicts shouldn't happen, not all such conflicts can
be reliably prevented in the current implementation.

## Avoiding or tolerating conflicts

In most cases, you can use appropriate application design to avoid conflicts or make
your application tolerant of conflicts.

Conflicts only occur when simultaneous operations happen on multiple nodes. To avoid
conflicts:

- Write to only one node
- Write to independent database subsets on each node (for example, assign each node a
  separate schema)

For INSERT vs INSERT conflicts, use Global sequences to prevent conflicts
entirely.

If conflicts are not acceptable for your use case, consider implementing distributed
locking at the application level. Often, the best approach is to design your application to
work with pgactive's conflict resolution mechanisms rather than trying to prevent all
conflicts. For more information, see [Types of conflicts](#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflicttypes "#Appendix.PostgreSQL.CommonDBATasks.pgactive.actact.conflicttypes").

## Conflict logging

pgactivelink logs conflict incidents in the
`pgactive.pgactive_conflict_history` table to help you diagnose and handle
active-active conflicts. Conflict logging to this table only occurs when you set
`pgactive.log_conflicts_to_table` to true. The pgactive extension also logs
conflicts to the PostgreSQL log file when log_min_messages is set to `LOG` or
`lower`, regardless of the `pgactive.log_conflicts_to_table`
setting.

Use the conflict history table to:

- Measure how frequently your application creates conflicts
- Identify where conflicts occur
- Improve your application to reduce conflict rates
- Detect cases where conflict resolutions don't produce desired results
- Determine where you need user-defined conflict triggers or application design
  changes

For row conflicts, you can optionally log row values. This is controlled by the
`pgactive.log_conflicts_to_table` setting. Note that:

- This is a global database-wide option
- There is no per-table control over row value logging
- No limits are applied to field numbers, array elements, or field lengths
- Enabling this feature may not be advisable if you work with multi-megabyte rows that
  might trigger conflicts

Since the conflict history table contains data from every table in the database (each
with potentially different schemas), logged row values are stored as JSON fields. The JSON
is created using `row_to_json`, similar to calling it directly from SQL.
PostgreSQL doesn't provide a `json_to_row` function, so you'll need
table-specific code (in PL/pgSQL, PL/Python, PL/Perl, etc.) to reconstruct a composite-typed
tuple from the logged JSON.

###### Note

Support for user-defined conflicts is planned as a future extension feature.
