# AWS managed policy:

EMRDescribeClusterPolicyForEMRWAL

You can't attach `EMRDescribeClusterPolicyForEMRWAL` to your IAM
entities. This policy is attached to a service-linked role that allows Amazon EMR to
perform actions on your behalf. For more information on this service-linked
role, see [Using service-linked roles with Amazon EMR for write-ahead
logging](using-service-linked-roles-wal.md "using-service-linked-roles-wal.md").

This policy grants read-only permissions that allow the WAL service for Amazon EMR
to find and return the status of a cluster. For more information about Amazon EMR
WAL, see [Write-ahead logs (WAL) for
Amazon EMR](../ReleaseGuide/emr-hbase-wal.md "../ReleaseGuide/emr-hbase-wal.md").

**Permissions details**

This policy includes the following permissions:

- `emr` – Allows principals to describe cluster status
  from Amazon EMR. This is required so that Amazon EMR can confirm when a cluster
  has terminated and then, after thirty days, clean up any WAL logs left
  behind by the cluster.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:DescribeCluster"
 ],
 "Resource": [
 "*"
 ],
 "Sid": "AllowELASTICMAPREDUCEDescribecluster"
 }
 ]
}`

```
