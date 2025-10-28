# Working with cluster secrets in

AWS PCS

As part of creating a cluster, AWS PCS creates a cluster secret that is required to
connect to the job scheduler on the cluster. You also create AWS PCS compute node groups,
which define sets of instances to launch in response to scaling events. AWS PCS configures
instances launched by those compute node groups with the cluster secret so they can connect to the
job scheduler. There are cases where you might want to configure Slurm clients manually. Examples
include building a persistent login node or setting up a workflow manager with job management
capabilities.

AWS PCS stores the cluster secret as a [managed secret](../../../secretsmanager/latest/userguide/integrating_pcs.md "../../../secretsmanager/latest/userguide/integrating_pcs.md") with the prefix `pcs!` in
AWS Secrets Manager. The cost of the secret is included in the charge for using AWS PCS. You can rotate cluster secrets through AWS Secrets Manager to maintain security compliance and remediate potential security compromises.

###### Topics

- [Use AWS Secrets Manager to find the
  cluster secret](working-with_clusters_secrets_find_secrets-manager.md "working-with_clusters_secrets_find_secrets-manager.md")
- [Use AWS PCS to find the cluster
  secret](working-with_clusters_secrets_find_pcs.md "working-with_clusters_secrets_find_pcs.md")
- [Get the Slurm cluster secret](working-with_clusters_secrets_get.md "working-with_clusters_secrets_get.md")
- [Rotating cluster secrets in AWS PCS](cluster-secret-rotation.md "cluster-secret-rotation.md")
