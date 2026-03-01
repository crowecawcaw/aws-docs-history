# Deleting a replication group

If you no longer need one of your clusters with replicas (called _replication groups_ in the API/CLI), you can delete it.
When you delete a replication group, ElastiCache deletes all of the nodes in that group.

After you have begun this operation, it cannot be interrupted or canceled.

###### Warning

- When you delete an ElastiCache for Redis OSS cluster, your manual snapshots are retained.
  You will also have an option to create a final snapshot before the cluster is deleted.
  Automatic cache snapshots are not retained.
- `CreateSnapshot` permission is required to create a final snapshot.
  Without this permission, the API call will fail with an `Access Denied` exception.

## Deleting a Replication Group (Console)

To delete a cluster that has replicas,
see [Deleting a cluster in ElastiCache](Clusters.md "Clusters.md").

## Deleting a Replication Group (AWS CLI)

Use the command delete-replication-group to
delete a replication group.

```
aws elasticache delete-replication-group --replication-group-id `my-repgroup`
```

A prompt asks you to confirm your decision. Enter
_y_ (yes) to start the operation immediately.
After the process starts, it is irreversible.

```

   After you begin deleting this replication group, all of its nodes will be deleted as well.
   Are you sure you want to delete this replication group? [Ny]`y`

REPLICATIONGROUP  my-repgroup  My replication group  deleting
```

## Deleting a replication group (ElastiCache API)

Call DeleteReplicationGroup with the
`ReplicationGroup` parameter.

###### Example

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=DeleteReplicationGroup
   &ReplicationGroupId=my-repgroup
   &Version=2014-12-01
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20141201T220302Z
   &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
   &X-Amz-Date=20141201T220302Z
   &X-Amz-SignedHeaders=Host
   &X-Amz-Expires=20141201T220302Z
   &X-Amz-Credential=<credential>
   &X-Amz-Signature=<signature>
```

###### Note

If you set the `RetainPrimaryCluster` parameter to `true`,
all of the read replicas will be deleted, but the primary cluster will be retained.
