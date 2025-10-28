# Trying to access storage

Learn about the troubleshooting tips for trying to access storage.

## Using an external Amazon FSx for Lustre file system

Make sure that traffic is allowed between the cluster and file system. The file system must be associated with
a security group that allows inbound and outbound TCP traffic through ports 988, 1021, 1022, and 1023. For more information about how
to set up security groups, see [FileSystemId](SharedStorage-v3.md#yaml-SharedStorage-FsxLustreSettings-FileSystemId "SharedStorage-v3.md#yaml-SharedStorage-FsxLustreSettings-FileSystemId").

## Using an external Amazon Elastic File System file system

Make sure that traffic is allowed between the cluster and file system. The file system must be associated with
a security group that allows inbound and outbound TCP traffic through ports 988, 1021, 1022, and 1023. For more information about how
to set up security groups, see [FileSystemId](SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-FileSystemId "SharedStorage-v3.md#yaml-SharedStorage-EfsSettings-FileSystemId").
