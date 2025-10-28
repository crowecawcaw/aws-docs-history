# AWS PCS clusters

An AWS PCS cluster consists of the following components:

- Managed instances of the HPC system scheduler software, such as the Slurm control daemon
  (`slurmctld`).
- Components that integrate with the HPC system scheduler to provision and manage Amazon EC2
  instances.
- Components that integrate with the HPC system scheduler to transmit logs and metrics
  to Amazon CloudWatch.
  These components run in an account managed by AWS. They work together to manage Amazon EC2
  instances in your customer account. AWS PCS provisions elastic network interfaces in your
  Amazon VPC subnet to provide connectivity from the scheduler software to Amazon EC2 instances (for example,
  to support scheduling batch jobs on them and enabling users to run scheduler commands to list and
  manage those jobs).

###### Topics

- [Creating a cluster in AWS PCS](working-with_clusters_create.md "working-with_clusters_create.md")
- [Updating a cluster in AWS PCS](working-with_clusters_update.md "working-with_clusters_update.md")
- [Deleting a cluster in AWS PCS](working-with_clusters_delete.md "working-with_clusters_delete.md")
- [Cluster size in AWS PCS](working-with_clusters_size.md "working-with_clusters_size.md")
- [Working with cluster secrets in
  AWS PCS](working-with_clusters_secrets.md "working-with_clusters_secrets.md")
