# Amazon EFS integration

Amazon Elastic File System (Amazon EFS) provides serverless, fully elastic file storage so that you can share
file data without provisioning or managing storage capacity and performance. With Amazon EFS, you
can create a file system and then mount it in your VPC through the NFS versions 4.0 and 4.1
(NFSv4) protocol. Then you can use the EFS file system like any other POSIX-compliant file
system. For general information, see [What is Amazon Elastic File System?](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md") and the AWS
blog [Integrate Amazon RDS for Oracle with Amazon EFS](https://aws.amazon.com//blogs/database/integrate-amazon-rds-for-oracle-with-amazon-efs/ "https://aws.amazon.com//blogs/database/integrate-amazon-rds-for-oracle-with-amazon-efs/").

###### Topics

- [Overview of Amazon EFS integration](#oracle-efs-integration.overview "#oracle-efs-integration.overview")
- [Configuring network permissions for
  RDS for Oracle integration with Amazon EFS](oracle-efs-integration.md "oracle-efs-integration.md")
- [Configuring IAM permissions for RDS for Oracle integration with Amazon EFS](oracle-efs-integration.md "oracle-efs-integration.md")
- [Adding the EFS_INTEGRATION option](oracle-efs-integration.md "oracle-efs-integration.md")
- [Configuring Amazon EFS file system
  permissions](oracle-efs-integration.md "oracle-efs-integration.md")
- [Transferring files between RDS for Oracle
  and an Amazon EFS file system](oracle-efs-integration.md "oracle-efs-integration.md")
- [Removing the EFS_INTEGRATION option](oracle-efs-integration.md "oracle-efs-integration.md")
- [Troubleshooting Amazon EFS
  integration](oracle-efs-integration.md "oracle-efs-integration.md")

## Overview of Amazon EFS integration

With Amazon EFS, you can transfer files between your RDS for Oracle DB instance and an EFS file system. For
example, you can use EFS to support the following use cases:

- Share a file system between applications and multiple database servers.
- Create a shared directory for migration-related files, including transportable
  tablespace data files. For more information, see [Migrating using Oracle transportable
  tablespaces](oracle-migrating-tts.md "oracle-migrating-tts.md").
- Store and share archived redo log files without allocating additional storage
  space on the server.
- Use Oracle Database utilities such as `UTL_FILE` to read and write
  files.

### Advantages to Amazon EFS

integration

When you choose an EFS file system over alternative data transfer solutions, you get
the following benefits:

- You can transfer Oracle Data Pump files between Amazon EFS and your RDS for Oracle DB instance.
  You don’t need to copy these files locally because Data Pump imports directly
  from the EFS file system. For more information, see [Importing data into Oracle on Amazon RDS](Oracle.Procedural.md "Oracle.Procedural.md").
- Data migration is faster than using a database link.
- You avoid allocating storage space on your RDS for Oracle DB instance to hold the
  files.
- An EFS file systems can automatically scale storage without requiring you to
  provision it.
- Amazon EFS integration has no minimum fees or setup costs. You pay only for what
  you use.
- Amazon EFS integration supports two forms of encryption: encryption of data in
  transit and encryption at rest. Encryption of data in transit is enabled by
  default using TLS version 1.2. You can enable encryption of data at rest when
  creating an Amazon EFS file system. For more information, see [Encrypting
  data at rest](../../../efs/latest/ug/encryption-at-rest.md "../../../efs/latest/ug/encryption-at-rest.md") in the _Amazon Elastic File System User
  Guide_.

### Requirements for Amazon EFS

integration

Make sure that you meet the following requirements:

- Your database must run database version 19.0.0.0.ru-2022-07.rur-2022-07.r1 or
  higher.
- Your DB instance and your EFS file system must be in the same AWS Region, VPC, and
  AWS account. RDS for Oracle doesn't support cross-account and cross-Region access
  for EFS.
- Your VPC must have both **DNS Resolution** and **DNS
  Hostnames** enabled. For more information, see [DNS attributes in your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-support") in the _Amazon Virtual Private Cloud User
  Guide_.
- If you use a DNS name in the `mount` command, make sure your VPC
  configured to use the DNS server provided by Amazon. Custom DNS servers aren't
  supported.
- You must use non-RDS solutions to back up your EFS file system. RDS for Oracle
  doesn't support automated backups or manual DB snapshots of an EFS file system.
  For more information, see [Backing up your Amazon EFS file
  systems](../../../efs/latest/ug/efs-backup-solutions.md "../../../efs/latest/ug/efs-backup-solutions.md").
