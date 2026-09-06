

# Dropping tempfiles on a read replica
<a name="Appendix.Oracle.CommonDBATasks.dropping-tempfiles-replica"></a>

You can't drop an existing temporary tablespace on a read replica. You can change the tempfile storage on a read replica from Amazon EBS to the instance store, or from the instance store to Amazon EBS. To achieve these goals, do the following:

1. Drop the current tempfiles in the temporary tablespace on the read replica.

1. Create new tempfiles on different storage.

To drop the tempfiles, use the Amazon RDS procedure `rdsadmin.rdsadmin_util. drop_replica_tempfiles`. You can use this procedure only on read replicas. The `drop_replica_tempfiles` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_tablespace_name` | varchar | — | Yes | The name of the temporary tablespace on your read replica. | 

Assume that a temporary tablespace named {{temp01}} resides in the instance store on your read replica. Drop all tempfiles in this tablespace by running the following command.

```
EXEC rdsadmin.rdsadmin_util.drop_replica_tempfiles(p_tablespace_name => '{{temp01}}');
```

For more information, see [Storing temporary data in an RDS for Oracle instance store](CHAP_Oracle.advanced-features.instance-store.md).