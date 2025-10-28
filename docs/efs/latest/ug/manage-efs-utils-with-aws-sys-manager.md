# Automatically installing or updating

Amazon EFS client using AWS Systems Manager

You can use AWS Systems Manager to simplify the management of the Amazon EFS client
(`amazon-efs-utils`). AWS Systems Manager is an AWS service that you can use to view
and control your infrastructure on AWS. With AWS Systems Manager you can automate the tasks required to
install or update the `amazon-efs-utils` package on your Amazon EC2 (EC2)
instances. The Systems Manager capabilities like Distributor and State Manager enable you to automate the
following processes:

- Maintaining version control over the Amazon EFS client.
- Centrally storing and systematically distributing the Amazon EFS client to your Amazon EC2
  instances.
- Automate the process of keeping your EC2 instances in a defined state.
  For more information, see the [_AWS Systems Manager User Guide_](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md").

## What the Amazon EFS client does during installation

You use the Amazon EFS client to automate monitoring Amazon CloudWatch logs for file system mount status
and upgrade `stunnel` to the latest version for selected Linux distributions.
When you install the Amazon EFS client on your Amazon EC2 instances using Systems Manager, it takes the following
actions:

- Installs the `botocore` package using the same steps described in [Installing and upgrading botocore](install-botocore.md "install-botocore.md"). The Amazon EFS client uses
  `botocore` to monitor the EFS file system mount status.
- Enables the monitoring of EFS file system mount status in CloudWatch logs by updating
  `efs-utils.conf`. For more information, see [Monitoring mount attempt successes and failures](how-to-monitor-mount-status.md "how-to-monitor-mount-status.md").
- For EC2 instances running `RHEL7` or `CentOS7`, the Amazon EFS
  client automatically upgrades `stunnel` as described in [Upgrading stunnel](upgrading-stunnel.md "upgrading-stunnel.md"). Upgrading
  `stunnel` is required in order to successfully mount an EFS file system
  using TLS, and the `stunnel` version shipped with `RHEL7` and
  `CentOS7` does not support the Amazon EFS client
  (`amazon-efs-utils`).

## Systems Manager supported operating systems

Your EC2 instances must be running one of the following operating systems in order
to be used with AWS Systems Manager to automatically update or install the Amazon EFS client.

| Platform                                                                                                                                                                                                                                                                                                                             | Platform version    | Architecture                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- | ------------------------------------------------------------- |
| Amazon Linux 2023 (AL2023)                                                                                                                                                                                                                                                                                                           | AL2023              | x86_64, arm64 (Graviton2 or later processors)                 |
| Amazon Linux 2 (AL2)                                                                                                                                                                                                                                                                                                                 | 2.0                 | x86_64, arm64 (Amazon Linux 2, A1 instance types)             |
| Amazon Linux 1 (AL1) NoteAmazon Linux 1 (AL1) AMI reached its end-of-life on December 31, 2023 and is not supported for `amazon-efs-utils` packages released in April 2024 and later (version 2.0 and later). We recommend that you upgrade applications to Amazon Linux 2023 (AL2023), which includes long-term support until 2028. | 2017.09, 2018.03    | x86_64                                                        |
| CentOS                                                                                                                                                                                                                                                                                                                               | 7, 8                | x86_64                                                        |
| Red Hat Enterprise Linux (RHEL)                                                                                                                                                                                                                                                                                                      | 8, 9                | x86_64, arm64                                                 |
| SUSE Linux Enterprise Server (SLES)                                                                                                                                                                                                                                                                                                  | 12, 15              | x86_64                                                        |
| Ubuntu Server                                                                                                                                                                                                                                                                                                                        | 16.04, 18.04, 20.04 | x86_64, arm64 (Ubuntu Server 16 and later, A1 instance types) |
