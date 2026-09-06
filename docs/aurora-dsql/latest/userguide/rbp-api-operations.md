

# Aurora DSQL API Operations and Resource-Based Policies
<a name="rbp-api-operations"></a>

Resource-based policies in Aurora DSQL control access to specific API operations. The following sections list all Aurora DSQL API operations organized by category, with an indication of which ones support resource-based policies.

The *Supports RBP* column indicates whether the API operation is subject to resource-based policy evaluation when a policy is attached to the cluster.

## Tag APIs
<a name="rbp-tag-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [ListTagsForResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListTagsForResource.html) | Lists the tags for a Aurora DSQL resource | Yes | 
| [TagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_TagResource.html) | Adds tags to a Aurora DSQL resource | Yes | 
| [UntagResource](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UntagResource.html) | Removes tags from a Aurora DSQL resource | Yes | 

## Cluster management APIs
<a name="rbp-cluster-management-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [CreateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateCluster.html) | Creates a new cluster | No | 
| [DeleteCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteCluster.html) | Deletes a cluster | Yes | 
| [GetCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetCluster.html) | Retrieves information about a cluster | Yes | 
| [GetVpcEndpointServiceName](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetVpcEndpointServiceName.html) | Retrieves the VPC endpoint service name for a cluster | Yes | 
| [ListClusters](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListClusters.html) | Lists clusters in your account | No | 
| [UpdateCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_UpdateCluster.html) | Updates the configuration of a cluster | Yes | 

## Multi-Region property APIs
<a name="rbp-multi-region-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [AddPeerCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_AddPeerCluster.html) | Adds a peer cluster to a multi-region configuration | Yes | 
| [PutMultiRegionProperties](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_PutMultiRegionProperties.html) | Sets multi-region properties for a cluster | Yes | 
| [PutWitnessRegion](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_PutWitnessRegion.html) | Sets the witness region for a multi-region cluster | Yes | 

## Stream APIs
<a name="rbp-stream-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [CreateStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_CreateStream.html) | Creates a new change data capture stream | Yes | 
| [DeleteStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteStream.html) | Deletes a change data capture stream | No | 
| [GetStream](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetStream.html) | Retrieves information about a change data capture stream | No | 
| [ListStreams](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ListStreams.html) | Lists the change data capture streams in your account | Yes | 

## Resource-based policy APIs
<a name="rbp-policy-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [DeleteClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_DeleteClusterPolicy.html) | Deletes the resource-based policy from a cluster | Yes | 
| [GetClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetClusterPolicy.html) | Retrieves the resource-based policy for a cluster | Yes | 
| [PutClusterPolicy](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_PutClusterPolicy.html) | Creates or updates the resource-based policy for a cluster | Yes | 

## AWS Fault Injection Service APIs
<a name="rbp-fis-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [InjectError](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_InjectError.html) | Injects errors for fault injection testing | No | 

## Backup and restore APIs
<a name="rbp-backup-restore-apis"></a>


| API Operation | Description | Supports RBP | 
| --- | --- | --- | 
| [GetBackupJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html) | Retrieves information about a backup job | No | 
| [GetRestoreJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html) | Retrieves information about a restore job | No | 
| [StartBackupJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html) | Starts a backup job for a cluster | Yes | 
| [StartRestoreJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html) | Starts a restore job from a backup | No | 
| [StopBackupJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html) | Stops a running backup job | No | 
| [StopRestoreJob](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/backup-aurora-dsql.html) | Stops a running restore job | No | 