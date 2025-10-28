# Oracle Cloud Infrastructure (OCI) Managed Backup to Amazon S3

When you create an Oracle Database@AWS database, VPC Lattice creates a resource configuration called
`odb-managed-s3-backup-access`. This resource configuration represents an
OCI managed backup of your databases to Amazon S3 and only enables connectivity to Amazon S3
buckets owned by OCI. Traffic between the ODB Network and S3 never leaves the Amazon
network.
