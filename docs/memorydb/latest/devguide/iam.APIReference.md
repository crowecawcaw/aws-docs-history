

# MemoryDB API permissions: Actions, resources, and conditions reference
<a name="iam.APIReference"></a>

When you set up [access control](iam.md#iam.accesscontrol) and write permissions policies to attach to an IAM policy (either identity-based or resource-based), use the following table as a reference. The table lists each MemoryDB API operation and the corresponding actions for which you can grant permissions to perform the action. You specify the actions in the policy's `Action` field, and you specify a resource value in the policy's `Resource` field. Unless indicated otherwise, the resource is required. Some fields include both a required resource and optional resources. When there is no resource ARN, the resource in the policy is a wildcard (\*).

**Note**  
To specify an action, use the `memorydb:` prefix followed by the API operation name (for example, `memorydb:DescribeClusters`).

Use the scroll bars to see the rest of the table.


**MemoryDB API and required permissions for actions**  

| MemoryDB API operations | Required permissions (API actions) | Resources  | 
| --- | --- | --- | 
| [BatchUpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_BatchUpdateCluster.html) | `memorydb:BatchUpdateCluster` | Cluster | 
| [CopySnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CopySnapshot.html) | `memorydb:CopySnapshot`<br />`memorydb:TagResource`<br />`s3:GetBucketLocation`<br />`s3:ListAllMyBuckets` | Snapshot (Source, Target)<br />\*<br />\* | 
| [CreateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateCluster.html) | `memorydb:CreateCluster`<br />`memorydb:TagResource`<br />`s3:GetObject` If you use the `SnapshotArns` parameter, each member of the `SnapshotArns` list requires its own `s3:GetObject` permission with the `s3` ARN as its resource.  | Parameter group. (Optional) cluster, snapshot, security group Ids and subnet group<br />`arn:aws:s3:::{{my_bucket}}/{{snapshot1}}.rdb`<br />Where {{my\_bucket}}/{{snapshot1}} is an S3 bucket and snapshot that you want to create the cluster from. | 
| [CreateParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateParameterGroup.html) | `memorydb:CreateParameterGroup`<br />`memorydb:TagResource` | Parameter group | 
| [CreateSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSubnetGroup.html) | `memorydb:CreateSubnetGroup`<br />`memorydb:TagResource` | Subnet group | \* | 
| [CreateSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateSnapshot.html) | `memorydb:CreateSnapshot`<br />`memorydb:TagResource` | Snapshot, cluster | 
| [CreateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateUser.html)  | `memorydb:CreateUser`<br />`memorydb:TagResource` | User | 
| [CreateACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_CreateACL.html)  | `memorydb:CreateACL`<br />`memorydb:TagResource` | Access Control List (ACL) | 
| [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html) | `memorydb:UpdateCluster` | Cluster | 
| [DeleteCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteCluster.html) | `memorydb:DeleteCluster` | Cluster. (Optional) Snapshot | 
| [DeleteParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteParameterGroup.html) | `memorydb:DeleteParameterGroup` | Parameter group | 
| [DeleteSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSubnetGroup.html) | `memorydb:DeleteSubnetGroup` | Subnet group | 
| [DeleteSnapshot](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteSnapshot.html) | `memorydb:DeleteSnapshot` | Snapshot | 
| [DeleteUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteUser.html)  | `memorydb:DeleteUser` | User | 
| [DeleteACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteACL.html)  | `memorydb:DeleteACL` | ACL | 
| [DescribeClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html) | `memorydb:DescribeClusters` | Cluster | 
| [DescribeEngineVersions](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEngineVersions.html) | `memorydb:DescribeEngineVersions` | No Resource ARN: \* | 
| [DescribeParameterGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameterGroups.html) | `memorydb:DescribeParameterGroups` | Parameter group | 
| [DescribeParameters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeParameters.html) | `memorydb:DescribeParameters` | Parameter group | 
| [DescribeSubnetGroups](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSubnetGroups.html) | `memorydb:DescribeSubnetGroups` | Subnet group | \* | 
| [DescribeEvents](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeEvents.html) | `memorydb:DescribeEvents` | No Resource ARN: \* | 
| [DescribeClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeClusters.html) | `memorydb:DescribeClusters` | Cluster | 
| [DescribeServiceUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeServiceUpdates.html) | `memorydb:DescribeServiceUpdates` | No Resource ARN: \* | 
| [DescribeSnapshots](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeSnapshots.html) | `memorydb:DescribeSnapshots` | Snapshot | 
| [DescribeUsers](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeUsers.html)  | `memorydb:DescribeUsers` | User | 
| [DescribeACLs](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeACLs.html)  | `memorydb:DescribeACLs` | ACLs | 
| [ListAllowedNodeTypeUpdates](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListAllowedNodeTypeUpdates.html) | `memorydb:ListAllowedNodeTypeUpdates` | Cluster | 
| [ListTags](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ListTags.html) | `memorydb:ListTags` | (Optional) cluster, snapshot | 
| [UpdateParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateParameterGroup.html) | `memorydb:UpdateParameterGroup` | Parameter group | 
| [UpdateSubnetGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateSubnetGroup.html) | `memorydb:UpdateSubnetGroup` | Subnet group | 
| [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html) | `memorydb:UpdateCluster` | cluster. (Optional) Parameter group, Security group | 
| [UpdateUser](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateUser.html)  | `memorydb:UpdateUser` | User | 
| [UpdateACL](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateACL.html)  | `memorydb:UpdateACL` | ACL | 
| [UntagResource](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UntagResource.html) | `memorydb:UntagResource` | (Optional) Cluster, snapshot | 
| [ResetParameterGroup](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_ResetParameterGroup.html) | `memorydb:ResetParameterGroup` | Parameter group | 
| [FailoverShard](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_FailoverShard.html) | `memorydb:FailoverShard` | cluster, shard | 