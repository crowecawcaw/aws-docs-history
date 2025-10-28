# Manually installing the Amazon EFS client

You can manually install the Amazon EFS client on Amazon EC2 (EC2) Linux instances and on
EC2 Mac instances running macOS Big Sur, macOS Monterey, and macOS Ventura. For a list of
the distributions that support Amazon EFS client, see [Supported distributions](using-amazon-efs-utils.md#efs-utils-supported-distros "using-amazon-efs-utils.md#efs-utils-supported-distros")

The installation procedures for supported operating systems are described in the following
sections.

###### Topics

- [Installing the Amazon EFS client on Amazon EC2 Linux
  instances](#installing-efs-utils-amzn-linux "#installing-efs-utils-amzn-linux")
- [Installing the Amazon EFS client on other Linux
  distributions](#installing-other-distro "#installing-other-distro")
- [Installing the Amazon EFS client on EC2 Mac instances
  running macOS Big Sur, macOS Monterey, or macOS Ventura](#install-efs-utils-macOS "#install-efs-utils-macOS")

## Installing the Amazon EFS client on Amazon EC2 Linux

instances

The `amazon-efs-utils` package for installing on Amazon EC2 Linux instances
from the following locations:

- The Amazon Machine Images (AMI) package repositories for Amazon Linux. The following
  instructions are for installing the `amazon-efs-utils` package from the
  AMI package repositories.
- The AWS [efs-utils](https://github.com/aws/efs-utils "https://github.com/aws/efs-utils") GitHub repository.
  For more information about installing the `amazon-efs-utils` package from
  GitHub, see [Installing the Amazon EFS client on other Linux
  distributions](#installing-other-distro "#installing-other-distro").

###### Note

- If you're using AWS Direct Connect, you can find installation instructions in [Prerequisites](mounting-fs-mount-helper-direct.md#efs-onpremises "mounting-fs-mount-helper-direct.md#efs-onpremises").
- The Amazon Linux 1 (AL1) AMI reached its end-of-life on December 31, 2023 and is not
  supported for `amazon-efs-utils` packages released in April 2024 and later
  (version 2.0 and later). We recommend that you upgrade applications to Amazon Linux 2023
  (AL2023), which includes long-term support until 2028.

###### To install the `amazon-efs-utils` package from the AMI package

repository on EC2 Linux instances

1. Make sure that you've created an AL2023 or Amazon Linux 2 (AL2) EC2 instance. For
   information on how to do this, see [Step 1: Launch an
   instance](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md#ec2-launch-instance").
2. Access the terminal for your instance through Secure Shell (SSH), and log in with the
   appropriate user name. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.
3. Run the following command to install the `amazon-efs-utils` package.

```
sudo yum install -y amazon-efs-utils
```

## Installing the Amazon EFS client on other Linux

distributions

If you don't want to get the `amazon-efs-utils` package from the Amazon Linux
AMI package repositories, it is also available on GitHub.

After you clone the package, you can build and install `amazon-efs-utils` using one of the
following methods, depending on the package type supported by your Linux distribution:

- **RPM** – This package type is supported by AL2023,
  Amazon Linux 2, Red Hat Linux, CentOS, and similar.
- **DEB** – This package type is supported by Ubuntu,
  Debian, and similar.

For instructions on installing the `amazon-efs-utils` package for other
Linux distributions, see [On other
Linux distributions](https://github.com/aws/efs-utils?tab=readme-ov-file#on-other-linux-distributions "https://github.com/aws/efs-utils?tab=readme-ov-file#on-other-linux-distributions") in the `amazon-efs-utils` README on
Github.

## Installing the Amazon EFS client on EC2 Mac instances

running macOS Big Sur, macOS Monterey, or macOS Ventura

The `amazon-efs-utils` package is available for installation on
EC2 Mac instances running macOS Big Sur, macOS Monterey, or macOS Ventura.

For instructions on installing the `amazon-efs-utils` package on Mac
instances, see [On MacOS Big Sur, macOS Monterey, macOS Sonoma and macOS Ventura distribution](https://github.com/aws/efs-utils?tab=readme-ov-file#on-macos-big-sur-macos-monterey-macos-sonoma-and-macos-ventura-distribution "https://github.com/aws/efs-utils?tab=readme-ov-file#on-macos-big-sur-macos-monterey-macos-sonoma-and-macos-ventura-distribution") in the
`amazon-efs-utils` README on Github.

### Next steps

After installs `amazon-efs-utils` on your EC2 instance, proceed to the next steps for mounting your file system:

- [Install botocore](install-botocore.md "install-botocore.md") so that you can use Amazon CloudWatch to
  monitor your file system's mount status.
- [Upgrade to the latest version of stunnel](upgrading-stunnel.md "upgrading-stunnel.md") to enable
  encryption of data in transit.
- [Mount your file system](efs-mount-helper.md "efs-mount-helper.md") using the EFS mount helper.
