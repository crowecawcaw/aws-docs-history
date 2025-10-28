# Troubleshooting the Neptune Blue/Green solution

The following information highlights issues that can arise during
the Blue/Green solution deployment process, such as conflicts with existing clusters, the need to enable Neptune
streams, ongoing bulk load operations, and version compatibility requirements. By addressing these potential
problems, you can ensure a smooth and successful deployment of the Neptune Blue/Green solution.

###### Errors raised by the Neptune Blue/Green solution

- **`Cluster with id = `(blue_green_deployment_id)` already exists`**   –  
  There is an existing cluster with identifier `(blue_green_deployment_id)`.

Provide a new deployment ID or set the deployment mode to `resume`
if the cluster was created in a previous Neptune Blue/Green run.

- **`Streams should be enabled on the source Cluster for Blue Green Deployment`**   –  
  Enable [Neptune streams](streams-using-enabling.md "streams-using-enabling.md") on the blue (source) cluster.
- **`No Bulkload should be in progress on source cluster: `(cluster_id)``**   –  
  The Neptune Blue/Green solution terminates if it identifies an ongoing bulk load.

This is to ensure that the sync process is able to catch up with writes
being made. Avoid or cancel any ongoing bulk load job before starting the Neptune Blue/Green solution.

- **`Blue Green deployment requires instances to be in sync with db cluster parameter group`**   –  
  Any changes to cluster parameter group should be in sync throughout the DB cluster. See
  [Amazon Neptune parameter groups](parameter-groups.md "parameter-groups.md").
- **`Invalid target engine version for Blue Green Deployment`**   –  
  The target engine version must be listed as active in [Engine releases for Amazon Neptune](engine-releases.md "engine-releases.md"), and must be higher than the current engine release
  of the source (blue) cluster.
