# AWS Transfer Family SFTP connectors

An AWS Transfer Family SFTP connector establishes a connection with a remote SFTP server to transfer
files between Amazon storage and a remote server, using the SFTP protocol. You can send
files from Amazon S3 to an external, partner-owned SFTP server, retrieve files from a partner's
SFTP server to Amazon S3 or list, delete, rename or move files on the remote server. SFTP
connectors support two egress types: service managed (using AWS managed infrastructure)
and VPC (routing through your VPC using Amazon VPC Lattice ). Using SFTP connectors, you can build
automated, event-driven file transfer workflows in AWS .

The following video provides a brief introduction to Transfer Family
SFTP connectors.

###### Topics

- [Creating SFTP connectors](configure-sftp-connector.md "configure-sftp-connector.md")
- [VPC connectivity for SFTP connectors](sftp-connectors-vpc-overview.md "sftp-connectors-vpc-overview.md")
- [Using SFTP connectors](transfer-sftp-connectors.md "transfer-sftp-connectors.md")
- [Monitoring SFTP connectors](track-connector-progress.md "track-connector-progress.md")
- [Managing SFTP connectors](manage-sftp-connectors.md "manage-sftp-connectors.md")
- [Scaling and quotas for
  SFTP connectors](scale-and-limits-sftp-connector.md "scale-and-limits-sftp-connector.md")
- [Reference architectures using SFTP
  connectors](reference-architectures.md "reference-architectures.md")
