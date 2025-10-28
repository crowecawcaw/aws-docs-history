# Required permissions for Amazon EMR WAL

For your cluster to connect to Amazon EMR WAL, the instance profile for the cluster
requires certain IAM permissions:

- Amazon EMR WAL uses the [AWSServiceRoleForEMRWAL](../ManagementGuide/using-service-linked-roles-wal.md "../ManagementGuide/using-service-linked-roles-wal.md") service-linked role to
  retrieve a cluster status. Amazon EMR automatically creates this service-linked role
  when you create a WAL workspace, or HBase will create the service-linked role
  when you configure a workspace for Amazon EMR WAL and the service-linked role doesn't
  yet exist.

Before you can enable Amazon EMR WAL for a cluster, you must configure the
permissions to allow automatic creation of the
AWSServiceRoleForEMRWAL service-linked role. For more
information and an example statement that adds this capability, see [Using service-linked roles for write-ahead logging](../ManagementGuide/using-service-linked-roles-wal.md#using-service-linked-roles-permissions-wal "../ManagementGuide/using-service-linked-roles-wal.md#using-service-linked-roles-permissions-wal").

- Because Amazon EMR WAL uses HBase Write Ahead Log (WAL), your clusters must use
  HBase WAL. The following are the minimum IAM permissions that you need to run
  HBase. Add these to the permissions policy for your instance profile:

```
emrwal:DeleteWal
emrwal:CreateWal
emrwal:CreateWorkspace
emrwal:AppendEdit
emrwal:ReplayEdits
emrwal:GetCurrentWalTime
emrwal:CompleteWalFlush
emrwal:ListWALs
emrwal:DescribeWAL
emrwal:TrimWAL
emrwal:ArchiveWAL
emrwal:ArchiveWALCheckPoint
```

###### Note

If you scope permissions for Amazon EMR WAL to only the minimal set, some [EMRWAL CLI](emrwalcli-ref.md "emrwalcli-ref.md") commands won't
have the necessary permissions to run.
