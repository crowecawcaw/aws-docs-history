# Installing the Amazon EFS client

We recommend that you install the Amazon EFS client (`amazon-efs-utils`), an
open-source collection of tools for Amazon EFS. The Amazon EFS client includes a _mount helper_, which is a program that helps simplify mounting EFS file
systems. The client also enables the ability to use Amazon CloudWatch to monitor an EFS file
system's mount status, and it includes tooling that makes it easier to perform encryption of data
in transit for Amazon EFS file systems.

You can manually install the Amazon EFS client on Amazon EC2 (EC2) instances running [supported distributions](#efs-utils-supported-distros "#efs-utils-supported-distros"). For certain supported
operating systems, you can alternatively configure AWS Systems Manager to automatically install or update
the package. For a list of distributions that you can use with AWS Systems Manager, see [Systems Manager supported operating systems](manage-efs-utils-with-aws-sys-manager.md#sys-mgr-support-matrix "manage-efs-utils-with-aws-sys-manager.md#sys-mgr-support-matrix").

###### Important

We recommend that you always use the most current version of
`amazon-efs-utils` to ensure access to its full capabilities. For example,
mounting with IPv6 addresses is supported in versions 2.3 or later, but not in earlier
versions.

###### Topics

- [Dependencies for EFS tools](#utils-dependencies "#utils-dependencies")
- [Supported distributions](#efs-utils-supported-distros "#efs-utils-supported-distros")
- [Manually installing the Amazon EFS client](installing-amazon-efs-utils.md "installing-amazon-efs-utils.md")
- [Automatically installing or updating
  Amazon EFS client using AWS Systems Manager](manage-efs-utils-with-aws-sys-manager.md "manage-efs-utils-with-aws-sys-manager.md")
- [Installing and upgrading botocore](install-botocore.md "install-botocore.md")
- [Upgrading stunnel](upgrading-stunnel.md "upgrading-stunnel.md")
- [Enabling FIPS mode](fips-enabling.md "fips-enabling.md")

## Dependencies for EFS tools

The following dependencies exist for `amazon-efs-utils` and are installed
when you install the `amazon-efs-utils` package:

- NFS client
  - `nfs-utils` for RHEL, CentOS, Amazon Linux, and Fedora distributions
  - `nfs-common` for Debian and Ubuntu distributions

- Network relay (stunnel package, version 4.56 or later)
- Python (version 3.4 or later)
- OpenSSL 1.0.2 or newer

###### Note

By default, when using the EFS mount helper with Transport Layer Security (TLS), the
mount helper enforces certificate
hostname checking. The EFS mount helper uses the `stunnel` program for its TLS functionality.
Some versions of Linux don't include a version of `stunnel` that supports these TLS features by
default. When using one of those Linux versions, mounting an EFS file system using TLS
fails.

After you've installed the `amazon-efs-utils` package, upgrade stunnel.
See [Upgrading stunnel](upgrading-stunnel.md "upgrading-stunnel.md").

You can use AWS Systems Manager to manage Amazon EFS clients and automate the tasks required to install or
update the amazon-efs-utils package on your EC2 instances. For more information, see [Automatically installing or updating
Amazon EFS client using AWS Systems Manager](manage-efs-utils-with-aws-sys-manager.md "manage-efs-utils-with-aws-sys-manager.md").

For issues with encryption, see [Troubleshooting encryption](troubleshooting-efs-encryption.md "troubleshooting-efs-encryption.md").

## Supported distributions

The Amazon EFS client has been verified against the following Linux and Mac distributions:

| Distribution                                                                                                                                                                                       | Package type | `init` system |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Linux 2023 (AL2023)                                                                                                                                                                         | rpm          | `systemd`     |
| Amazon Linux 2 (AL2)                                                                                                                                                                               | rpm          | `systemd`     |
| CentOS 8                                                                                                                                                                                           | rpm          | `systemd`     |
| Amazon Linux 1 (AL1) 2017.09NoteAL1 AMI reached its end-of-life on December 31, 2023 and is not supported for `amazon-efs-utils` packages released in April 2024 or later (version 2.0 and later). | rpm          | `upstart`     |
| Debian 11                                                                                                                                                                                          | deb          | `systemd`     |
| Fedora 29 - 32                                                                                                                                                                                     | rpm          | `systemd`     |
| macOS Big Sur                                                                                                                                                                                      |              | `launchd`     |
| macOS Monterey                                                                                                                                                                                     |              | `launchd`     |
| macOS Ventura                                                                                                                                                                                      |              | `launchd`     |
| macOS Sonoma                                                                                                                                                                                       |              | `launchd`     |
| OpenSUSE Leap, Tumbleweed                                                                                                                                                                          | rpm          | `systemd`     |
| Oracle8                                                                                                                                                                                            | rpm          | `systemd`     |
| Red Hat Enterprise Linux (RHEL) 8, 9                                                                                                                                                               | rpm          | `systemd`     |
| SUSE Linux Enterprise Server (SLES) 12, 15                                                                                                                                                         | rpm          | `systemd`     |
| Ubuntu 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS                                                                                                                                                  | deb          | `systemd`     | For a complete list of supported distributions that the package has been verified against, see the `amazon-efs-utils` [README](https://github.com/aws/efs-utils/blob/master/README.md "https://github.com/aws/efs-utils/blob/master/README.md") on Github. |
