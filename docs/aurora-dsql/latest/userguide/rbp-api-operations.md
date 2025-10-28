# Aurora DSQL API Operations and Resource-Based Policies

Resource-based policies in Aurora DSQL control access to specific API operations. The following sections list all Aurora DSQL API operations organized by category, with an indication of which ones support resource-based policies.

The _Supports RBP_ column indicates whether the API operation is subject to resource-based policy evaluation when a policy is attached to the cluster.

## Tag APIs

| API Operation                                                                                                                    | Description                                                | Supports RBP |
| -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------ | ----------------------------------- |
| [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")                   | Lists the tags for a Aurora DSQL resource                  | Yes          |
| [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")                                           | Adds tags to a Aurora DSQL resource                        | Yes          |
| [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")                                     | Removes tags from a Aurora DSQL resource                   | Yes          | ## Cluster management APIs          |
| API Operation                                                                                                                    | Description                                                | Supports RBP |
| ---                                                                                                                              | ---                                                        | ---          |
| [CreateCluster](../APIReference/API_CreateCluster.md "../APIReference/API_CreateCluster.md")                                     | Creates a new cluster                                      | No           |
| [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md")                                     | Deletes a cluster                                          | Yes          |
| [GetCluster](../APIReference/API_GetCluster.md "../APIReference/API_GetCluster.md")                                              | Retrieves information about a cluster                      | Yes          |
| [GetVpcEndpointServiceName](../APIReference/API_GetVpcEndpointServiceName.md "../APIReference/API_GetVpcEndpointServiceName.md") | Retrieves the VPC endpoint service name for a cluster      | Yes          |
| [ListClusters](../APIReference/API_ListClusters.md "../APIReference/API_ListClusters.md")                                        | Lists clusters in your account                             | No           |
| [UpdateCluster](../APIReference/API_UpdateCluster.md "../APIReference/API_UpdateCluster.md")                                     | Updates the configuration of a cluster                     | Yes          | ## Multi-Region property APIs       |
| API Operation                                                                                                                    | Description                                                | Supports RBP |
| ---                                                                                                                              | ---                                                        | ---          |
| [AddPeerCluster](../APIReference/API_AddPeerCluster.md "../APIReference/API_AddPeerCluster.md")                                  | Adds a peer cluster to a multi-region configuration        | Yes          |
| [PutMultiRegionProperties](../APIReference/API_PutMultiRegionProperties.md "../APIReference/API_PutMultiRegionProperties.md")    | Sets multi-region properties for a cluster                 | Yes          |
| [PutWitnessRegion](../APIReference/API_PutWitnessRegion.md "../APIReference/API_PutWitnessRegion.md")                            | Sets the witness region for a multi-region cluster         | Yes          | ## Resource-based policy APIs       |
| API Operation                                                                                                                    | Description                                                | Supports RBP |
| ---                                                                                                                              | ---                                                        | ---          |
| [DeleteClusterPolicy](../APIReference/API_DeleteClusterPolicy.md "../APIReference/API_DeleteClusterPolicy.md")                   | Deletes the resource-based policy from a cluster           | Yes          |
| [GetClusterPolicy](../APIReference/API_GetClusterPolicy.md "../APIReference/API_GetClusterPolicy.md")                            | Retrieves the resource-based policy for a cluster          | Yes          |
| [PutClusterPolicy](../APIReference/API_PutClusterPolicy.md "../APIReference/API_PutClusterPolicy.md")                            | Creates or updates the resource-based policy for a cluster | Yes          | ## AWS Fault Injection Service APIs |
| API Operation                                                                                                                    | Description                                                | Supports RBP |
| ---                                                                                                                              | ---                                                        | ---          |
| [InjectError](../APIReference/API_InjectError.md "../APIReference/API_InjectError.md")                                           | Injects errors for fault injection testing                 | No           | ## Backup and restore APIs          |
| API Operation                                                                                                                    | Description                                                | Supports RBP |
| ---                                                                                                                              | ---                                                        | ---          |
| [GetBackupJob](../APIReference/API_GetBackupJob.md "../APIReference/API_GetBackupJob.md")                                        | Retrieves information about a backup job                   | No           |
| [GetRestoreJob](../APIReference/API_GetRestoreJob.md "../APIReference/API_GetRestoreJob.md")                                     | Retrieves information about a restore job                  | No           |
| [StartBackupJob](../APIReference/API_StartBackupJob.md "../APIReference/API_StartBackupJob.md")                                  | Starts a backup job for a cluster                          | Yes          |
| [StartRestoreJob](../APIReference/API_StartRestoreJob.md "../APIReference/API_StartRestoreJob.md")                               | Starts a restore job from a backup                         | No           |
| [StopBackupJob](../APIReference/API_StopBackupJob.md "../APIReference/API_StopBackupJob.md")                                     | Stops a running backup job                                 | No           |
| [StopRestoreJob](../APIReference/API_StopRestoreJob.md "../APIReference/API_StopRestoreJob.md")                                  | Stops a running restore job                                | No           |
