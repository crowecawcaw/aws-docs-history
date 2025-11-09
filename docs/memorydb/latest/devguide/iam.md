# MemoryDB API permissions: Actions, resources, and conditions reference

When you set up [access
control](iam.md#iam.accesscontrol "iam.md#iam.accesscontrol") and write permissions policies to attach to an IAM policy (either identity-based or resource-based), use the following table as a reference. The table lists each
MemoryDB API operation and the corresponding actions for which you can grant
permissions to perform the action. You specify the actions in the policy's
`Action` field, and you specify a resource
value in the policy's `Resource` field. Unless indicated otherwise, the resource is required. Some fields include both a required resource and optional resources. When there is no resource ARN, the resource in the policy is a wildcard (\*).

###### Note

To specify an action, use the `memorydb:` prefix followed by the API
operation name (for example, `memorydb:DescribeClusters`).

Use the scroll bars to see the rest of the table.

MemoryDB API and required permissions
for actions | MemoryDB API operations | Required permissions (API actions) | Resources |
| --- | --- | --- |
| [BatchUpdateCluster](../APIReference/API_BatchUpdateCluster.md "../APIReference/API_BatchUpdateCluster.md") | `memorydb:BatchUpdateCluster` | Cluster |
| [CopySnapshot](../APIReference/API_CopySnapshot.md "../APIReference/API_CopySnapshot.md") | `memorydb:CopySnapshot`<br>`memorydb:TagResource`<br>`s3:GetBucketLocation`<br>`s3:ListAllMyBuckets` | Snapshot (Source, Target)<br>\*<br>\* |
| [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md") | `memorydb:CreateCluster`<br>`memorydb:TagResource`<br>`s3:GetObject`<br>NoteIf you use the `SnapshotArns` parameter, each member of the<br>`SnapshotArns` list requires its own `s3:GetObject`<br>permission with the `s3` ARN as its resource. | Parameter group. (Optional) cluster, snapshot, security group Ids and subnet group<br>`arn:aws:s3:::`my_bucket`/`snapshot1`.rdb`<br>Where `my_bucket`/`snapshot1` is an S3 bucket<br>and snapshot that you want to create the cluster from. |
| [CreateParameterGroup](../APIReference/API_CreateParameterGroup.md "../APIReference/API_CreateParameterGroup.md") | `memorydb:CreateParameterGroup`<br>`memorydb:TagResource` | Parameter group |
| [CreateSubnetGroup](../APIReference/API_CreateSubnetGroup.md "../APIReference/API_CreateSubnetGroup.md") | `memorydb:CreateSubnetGroup`<br>`memorydb:TagResource` | Subnet group | \* |
| [CreateSnapshot](../APIReference/API_CreateSnapshot.md "../APIReference/API_CreateSnapshot.md") | `memorydb:CreateSnapshot`<br>`memorydb:TagResource` | Snapshot, cluster |
| [CreateUser](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md") | `memorydb:CreateUser`<br>`memorydb:TagResource` | User |
| [CreateACL](../APIReference/API_CreateACL.md "../APIReference/API_CreateACL.md") | `memorydb:CreateACL`<br>`memorydb:TagResource` | Access Control List (ACL) |
| [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") | `memorydb:UpdateCluster` | Cluster |
| [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md") | `memorydb:DeleteCluster` | Cluster. (Optional) Snapshot |
| [DeleteParameterGroup](../APIReference/API_DeleteParameterGroup.md "../APIReference/API_DeleteParameterGroup.md") | `memorydb:DeleteParameterGroup` | Parameter group |
| [DeleteSubnetGroup](../APIReference/API_DeleteSubnetGroup.md "../APIReference/API_DeleteSubnetGroup.md") | `memorydb:DeleteSubnetGroup` | Subnet group |
| [DeleteSnapshot](../APIReference/API_DeleteSnapshot.md "../APIReference/API_DeleteSnapshot.md") | `memorydb:DeleteSnapshot` | Snapshot |
| [DeleteUser](../APIReference/API_DeleteUser.md "../APIReference/API_DeleteUser.md") | `memorydb:DeleteUser` | User |
| [DeleteACL](../APIReference/API_DeleteACL.md "../APIReference/API_DeleteACL.md") | `memorydb:DeleteACL` | ACL |
| [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") | `memorydb:DescribeClusters` | Cluster |
| [DescribeEngineVersions](../APIReference/API_DescribeEngineVersions.md "../APIReference/API_DescribeEngineVersions.md") | `memorydb:DescribeEngineVersions` | No Resource ARN: \* |
| [DescribeParameterGroups](../APIReference/API_DescribeParameterGroups.md "../APIReference/API_DescribeParameterGroups.md") | `memorydb:DescribeParameterGroups` | Parameter group |
| [DescribeParameters](../APIReference/API_DescribeParameters.md "../APIReference/API_DescribeParameters.md") | `memorydb:DescribeParameters` | Parameter group |
| [DescribeSubnetGroups](../APIReference/API_DescribeSubnetGroups.md "../APIReference/API_DescribeSubnetGroups.md") | `memorydb:DescribeSubnetGroups` | Subnet group | \* |
| [DescribeEvents](../APIReference/API_DescribeEvents.md "../APIReference/API_DescribeEvents.md") | `memorydb:DescribeEvents` | No Resource ARN: \* |
| [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") | `memorydb:DescribeClusters` | Cluster |
| [DescribeServiceUpdates](../APIReference/API_DescribeServiceUpdates.md "../APIReference/API_DescribeServiceUpdates.md") | `memorydb:DescribeServiceUpdates` | No Resource ARN: \* |
| [DescribeSnapshots](../APIReference/API_DescribeSnapshots.md "../APIReference/API_DescribeSnapshots.md") | `memorydb:DescribeSnapshots` | Snapshot |
| [DescribeUsers](../APIReference/API_DescribeUsers.md "../APIReference/API_DescribeUsers.md") | `memorydb:DescribeUsers` | User |
| [DescribeACLs](../APIReference/API_DescribeACLs.md "../APIReference/API_DescribeACLs.md") | `memorydb:DescribeACLs` | ACLs |
| [ListAllowedNodeTypeUpdates](../APIReference/API_ListAllowedNodeTypeUpdates.md "../APIReference/API_ListAllowedNodeTypeUpdates.md") | `memorydb:ListAllowedNodeTypeUpdates` | Cluster |
| [ListTags](../APIReference/API_ListTags.md "../APIReference/API_ListTags.md") | `memorydb:ListTags` | (Optional) cluster, snapshot |
| [UpdateParameterGroup](../APIReference/API_UpdateParameterGroup.md "../APIReference/API_UpdateParameterGroup.md") | `memorydb:UpdateParameterGroup` | Parameter group |
| [UpdateSubnetGroup](../APIReference/API_UpdateSubnetGroup.md "../APIReference/API_UpdateSubnetGroup.md") | `memorydb:UpdateSubnetGroup` | Subnet group |
| [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md") | `memorydb:UpdateCluster` | cluster. (Optional) Parameter group, Security group |
| [UpdateUser](../APIReference/API_UpdateUser.md "../APIReference/API_UpdateUser.md") | `memorydb:UpdateUser` | User |
| [UpdateACL](../APIReference/API_UpdateACL.md "../APIReference/API_UpdateACL.md") | `memorydb:UpdateACL` | ACL |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") | `memorydb:UntagResource` | (Optional) Cluster, snapshot |
| [ResetParameterGroup](../APIReference/API_ResetParameterGroup.md "../APIReference/API_ResetParameterGroup.md") | `memorydb:ResetParameterGroup` | Parameter group |
| [FailoverShard](../APIReference/API_FailoverShard.md "../APIReference/API_FailoverShard.md") | `memorydb:FailoverShard` | cluster, shard |
