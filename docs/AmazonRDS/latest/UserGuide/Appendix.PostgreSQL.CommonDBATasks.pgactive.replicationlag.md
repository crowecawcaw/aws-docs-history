

# Measuring replication lag among pgactive members
<a name="Appendix.PostgreSQL.CommonDBATasks.pgactive.replicationlag"></a>

You can use the following query to view the replication lag among the `pgactive` members. Run this query on every `pgactive` node to get the full picture.

```
    
app=> SELECT * FROM pgactive.pgactive_get_replication_lag_info();
│-[ RECORD 1 ]--------+---------------------------------------------
│node_name            | node2-app
│node_sysid           | 7481018224801653637
│application_name     | pgactive:7481018224801653637:send
│slot_name            | pgactive_16385_7481018224801653637_0_16385__
│active               | t
│active_pid           | 783486
│pending_wal_decoding | 0
│pending_wal_to_apply | 0
│restart_lsn          | 0/2108150
│confirmed_flush_lsn  | 0/2154690
│sent_lsn             | 0/2154690
│write_lsn            | 0/2154690
│flush_lsn            | 0/2154690
│replay_lsn           | 0/2154690
│-[ RECORD 2 ]--------+---------------------------------------------
│node_name            | node1-app
│node_sysid           | 7481018033434600853
│application_name     | pgactive:7481018033434600853:send
│slot_name            | pgactive_16385_7481018033434600853_0_16385__
│active               | t
│active_pid           | 783488
│pending_wal_decoding | 0
│pending_wal_to_apply | 0
│restart_lsn          | 0/20F5AD0
│confirmed_flush_lsn  | 0/214EF68
│sent_lsn             | 0/214EF68
│write_lsn            | 0/214EF68
│flush_lsn            | 0/214EF68
│replay_lsn           | 0/214EF68
```

Monitor the following diagnostics at a minimum:

active  
Set up alerts when active is false, which indicates that the slot isn't currently in use (the subscriber instance has disconnected from the publisher).

pending\_wal\_decoding  
In PostgreSQL's logical replication, WAL files are stored in binary format. The publisher must decode these WAL changes and convert them into logical changes (such as insert, update, or delete operations).  
The metric pending\_wal\_decoding shows the number of WAL files waiting to be decoded on the publisher side.  
This number can increase due to these factors:  
+ When the subscriber isn't connected, active status will be false and pending\_wal\_decoding will increase
+ The slot is active, but the publisher can't keep up with the volume of WAL changes

pending\_wal\_to\_apply  
The metric pending\_wal\_apply indicates the number of WAL files waiting to be applied on the subscriber side.  
Several factors can prevent the subscriber from applying changes and potentially cause a disk full scenario:  
+ Schema differences - for example, when you have changes in the WAL stream for a table named sample, but that table doesn't exist on the subscriber side
+ Values in the primary key columns were updated
+ Secondary unique indexes can cause data divergence