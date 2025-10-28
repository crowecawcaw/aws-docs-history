# STIG hardening script downloads

Amazon groups STIG hardening scripts together into operating system related bundles for
each release. Bundles are archive files that are appropriate for the target operating
system where they download and run. Linux script bundles are stored as TAR files
(.tgz file extension). Windows script bundles are stored as ZIP files (.zip file
extension).

Amazon stores the script bundles in the EC2 Windows S3 `STIG` bucket in each
AWS Region. The Linux bundles do not have a separate bucket. Use SSL/TLS to communicate
with AWS resources. We require TLS 1.2 and recommend TLS 1.3.

###### Topics

- [IAM prerequisites for STIG downloads](#ec2-stig-download-iam-prereq "#ec2-stig-download-iam-prereq")
- [STIG download bundle details](#ec2-stig-download-details "#ec2-stig-download-details")
- [Linux STIG version history](#ec2-linux-version-hist "#ec2-linux-version-hist")
- [Windows STIG version history](#ec2-windows-version-hist "#ec2-windows-version-hist")

## IAM prerequisites for STIG downloads

The IAM role that you associate with your instance profile must have
`s3:GetObject` permissions to download the script bundles from Amazon S3.
You can add the following example policy to your instance profile role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DownloadSTIGScriptBundles",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::aws-windows-downloads*/STIG/*.zip",
                "arn:aws:s3:::aws-windows-downloads*/STIG/*.tgz"
            ]
        }
    ]
}
```

To add the STIG download policy example to your instance profile role as an inline
policy, follow the [Update the permissions policy for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy") process in the
_AWS Identity and Access Management User Guide_. For more information about instance profile roles, see
[Use instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md").

## STIG download bundle details

###### Important

With few exceptions, the STIG hardening scripts that the Systems Manager document downloads
do not install third-party packages. If third-party packages are already installed on
the instance or the `InstallPackage` parameter is set to `yes`,
related STIGs that Amazon EC2 supports for that package are applied.

When you run the following command from the AWS CLI, Amazon S3 downloads the latest STIG
hardening script bundle file from the bucket.

```
`aws s3 cp s3://aws-windows-downloads-`region`/STIG/`operating system`/Latest/`bundle-name` `destination-directory``
```

###### Example: Download to a temporary directory

This example shows a Linux bundle that's downloaded to the `/tmp` directory

```
aws s3 cp s3://aws-windows-downloads-`us-east-1`/STIG/`Linux`/Latest/`LinuxAWSConfigureSTIG.tgz` `/tmp`
```

Patterns and examples for download file storage paths and bundle file names are as
follows:

###### Download file storage path

`s3://aws-windows-downloads-`<region>`/STIG/`<operating system>`/Latest/`<bundle file name>``

###### Download path variables

region

AWS Region (Each Region has its own download bucket.)

operating system

The operating system platform of the instance where STIGs are applied –
either `Linux` or `Windows`.

bundle file name

The format is `<os bundle name>`.`<file extension>`.

os bundle name

The standard name prefix for the operating system bundle is either
`LinuxAWSConfigureSTIG` or `AWSConfigureSTIG`.
To maintain backwards compatibility, the download for Windows doesn't
include a platform prefix.

file extension

Compressed file format `tgz` (Linux) or `zip` (Windows).

###### Example bundle file names

- `LinuxAWSConfigureSTIG.tgz`
- `AWSConfigureSTIG.zip`

## Linux STIG version history

This section logs version history for Linux script bundles that are updated quarterly.
To see the changes and published versions for a quarter, choose the title to expand the
information. If there are no changes for the quarter, you'll see that reflected in the title.

Added support for the SUSE Linux Enterprise Server (SLES) operating system and
Amazon Linux 2023. Updated the following STIG versions and applied STIGS for the
2025 third quarter release for all compliance levels (low/medium/high):

###### STIG-Build-Linux version 1.0.x

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 4
- RHEL 9 STIG Version 2 Release 5
- Amazon Linux 2023 STIG Version 1 Release 1
- SLES 12 STIG Version 3 Release 3
- SLES 15 STIG Version 2 Release 5
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 3
- Ubuntu 22.04 STIG Version 2 Release 5
- Ubuntu 24.04 STIG Version 1 Release 2
  Updated the following STIG versions, applied STIGS for the 2025 second quarter release:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 3
- RHEL 9 STIG Version 2 Release 4
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 2
- Ubuntu 22.04 STIG Version 2 Release 4
- Ubuntu 24.04 STIG Version 1 Release 1

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 3
- RHEL 9 STIG Version 2 Release 4
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 2
- Ubuntu 22.04 STIG Version 2 Release 4
- Ubuntu 24.04 STIG Version 1 Release 1

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 3
- RHEL 9 STIG Version 2 Release 4
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 2
- Ubuntu 22.04 STIG Version 2 Release 4
- Ubuntu 24.04 STIG Version 1 Release 1
  Updated the following STIG versions, applied STIGS for the 2025 first quarter release,
  and added support for Ubuntu 24.04:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 2
- RHEL 9 STIG Version 2 Release 3
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 2
- Ubuntu 22.04 STIG Version 2 Release 3
- Ubuntu 24.04 STIG Version 1 Release 1

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 2
- RHEL 9 STIG Version 2 Release 3
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 2
- Ubuntu 22.04 STIG Version 2 Release 3
- Ubuntu 24.04 STIG Version 1 Release 1

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 2
- RHEL 9 STIG Version 2 Release 3
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 2
- Ubuntu 22.04 STIG Version 2 Release 3
- Ubuntu 24.04 STIG Version 1 Release 1
  Updated the following STIG versions, applied STIGS for the 2024 fourth quarter release,
  and added information about two new input parameters for the Linux components:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 1
- RHEL 9 STIG Version 2 Release 2
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 1
- Ubuntu 22.04 STIG Version 2 Release 2

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 1
- RHEL 9 STIG Version 2 Release 2
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 1
- Ubuntu 22.04 STIG Version 2 Release 2

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 15
- RHEL 8 STIG Version 2 Release 1
- RHEL 9 STIG Version 2 Release 2
- Ubuntu 18.04 STIG Version 2 Release 15
- Ubuntu 20.04 STIG Version 2 Release 1
- Ubuntu 22.04 STIG Version 2 Release 2
  There were no changes for Linux component STIGS for the 2024 third quarter release.

Updated STIG versions and applied STIGS for the 2024 second quarter release.
Also added support for RHEL 9, CentOS Stream 9, and Ubuntu 22.04, as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 14
- RHEL 8 STIG Version 1 Release 14
- RHEL 9 STIG Version 1 Release 3
- Ubuntu 18.04 STIG Version 2 Release 14
- Ubuntu 20.04 STIG Version 1 Release 12
- Ubuntu 22.04 STIG Version 1 Release 1

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 14
- RHEL 8 STIG Version 1 Release 14
- RHEL 9 STIG Version 1 Release 3
- Ubuntu 18.04 STIG Version 2 Release 14
- Ubuntu 20.04 STIG Version 1 Release 12
- Ubuntu 22.04 STIG Version 1 Release 1

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 14
- RHEL 8 STIG Version 1 Release 14
- RHEL 9 STIG Version 1 Release 3
- Ubuntu 18.04 STIG Version 2 Release 14
- Ubuntu 20.04 STIG Version 1 Release 12
- Ubuntu 22.04 STIG Version 1 Release 1
  Updated STIG versions and applied STIGS for the 2024 first quarter release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 14
- RHEL 8 STIG Version 1 Release 13
- Ubuntu 18.04 STIG Version 2 Release 13
- Ubuntu 20.04 STIG Version 1 Release 11

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 14
- RHEL 8 STIG Version 1 Release 13
- Ubuntu 18.04 STIG Version 2 Release 13
- Ubuntu 20.04 STIG Version 1 Release 11

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 14
- RHEL 8 STIG Version 1 Release 13
- Ubuntu 18.04 STIG Version 2 Release 13
- Ubuntu 20.04 STIG Version 1 Release 11
  Updated STIG versions and applied STIGS for the 2023 fourth quarter release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 13
- RHEL 8 STIG Version 1 Release 12
- Ubuntu 18.04 STIG Version 2 Release 12
- Ubuntu 20.04 STIG Version 1 Release 10

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 13
- RHEL 8 STIG Version 1 Release 12
- Ubuntu 18.04 STIG Version 2 Release 12
- Ubuntu 20.04 STIG Version 1 Release 10

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 13
- RHEL 8 STIG Version 1 Release 12
- Ubuntu 18.04 STIG Version 2 Release 12
- Ubuntu 20.04 STIG Version 1 Release 10
  Updated STIG versions and applied STIGS for the 2023 third quarter release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 12
- RHEL 8 STIG Version 1 Release 11
- Ubuntu 18.04 STIG Version 2 Release 11
- Ubuntu 20.04 STIG Version 1 Release 9

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 12
- RHEL 8 STIG Version 1 Release 11
- Ubuntu 18.04 STIG Version 2 Release 11
- Ubuntu 20.04 STIG Version 1 Release 9

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 12
- RHEL 8 STIG Version 1 Release 11
- Ubuntu 18.04 STIG Version 2 Release 11
- Ubuntu 20.04 STIG Version 1 Release 9
  Updated STIG versions and applied STIGS for the 2023 second quarter release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 11
- RHEL 8 STIG Version 1 Release 10
- Ubuntu 18.04 STIG Version 2 Release 11
- Ubuntu 20.04 STIG Version 1 Release 8

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 11
- RHEL 8 STIG Version 1 Release 10
- Ubuntu 18.04 STIG Version 2 Release 11
- Ubuntu 20.04 STIG Version 1 Release 8

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 11
- RHEL 8 STIG Version 1 Release 10
- Ubuntu 18.04 STIG Version 2 Release 11
- Ubuntu 20.04 STIG Version 1 Release 8
  Updated STIG versions and applied STIGS for the 2023 first quarter release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 10
- RHEL 8 STIG Version 1 Release 9
- Ubuntu 18.04 STIG Version 2 Release 10
- Ubuntu 20.04 STIG Version 1 Release 7

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 10
- RHEL 8 STIG Version 1 Release 9
- Ubuntu 18.04 STIG Version 2 Release 10
- Ubuntu 20.04 STIG Version 1 Release 7

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 10
- RHEL 8 STIG Version 1 Release 9
- Ubuntu 18.04 STIG Version 2 Release 10
- Ubuntu 20.04 STIG Version 1 Release 7
  Updated STIG versions and applied STIGS for the 2022 fourth quarter release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 9
- RHEL 8 STIG Version 1 Release 8
- Ubuntu 18.04 STIG Version 2 Release 9
- Ubuntu 20.04 STIG Version 1 Release 6

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 9
- RHEL 8 STIG Version 1 Release 8
- Ubuntu 18.04 STIG Version 2 Release 9
- Ubuntu 20.04 STIG Version 1 Release 6

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 9
- RHEL 8 STIG Version 1 Release 8
- Ubuntu 18.04 STIG Version 2 Release 9
- Ubuntu 20.04 STIG Version 1 Release 6
  There were no changes for Linux component STIGS for the 2022 third quarter release.

Introduced Ubuntu support, updated STIG versions and applied STIGS for the 2022 second quarter
release as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 7
- RHEL 8 STIG Version 1 Release 6
- Ubuntu 18.04 STIG Version 2 Release 6 (new)
- Ubuntu 20.04 STIG Version 1 Release 4 (new)

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 7
- RHEL 8 STIG Version 1 Release 6
- Ubuntu 18.04 STIG Version 2 Release 6 (new)
- Ubuntu 20.04 STIG Version 1 Release 4 (new)

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 7
- RHEL 8 STIG Version 1 Release 6
- Ubuntu 18.04 STIG Version 2 Release 6 (new)
- Ubuntu 20.04 STIG Version 1 Release 4 (new)
  Refactored to include better support for containers. Combined the previous AL2 script with
  RHEL 7. Updated STIG versions and applied STIGS for the 2022 first quarter release
  as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 6
- RHEL 8 STIG Version 1 Release 5

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 6
- RHEL 8 STIG Version 1 Release 5

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 6
- RHEL 8 STIG Version 1 Release 5
  Updated STIG versions, and applied STIGS for the 2021 fourth quarter release
  as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 5
- RHEL 8 STIG Version 1 Release 4

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 5
- RHEL 8 STIG Version 1 Release 4

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 5
- RHEL 8 STIG Version 1 Release 4
  Updated STIG versions, and applied STIGS for the 2021 third quarter release
  as follows:

###### Linux STIG Low (Category III)

- RHEL 7 STIG Version 3 Release 4
- RHEL 8 STIG Version 1 Release 3

###### Linux STIG Medium (Category II)

- RHEL 7 STIG Version 3 Release 4
- RHEL 8 STIG Version 1 Release 3

###### Linux STIG High (Category I)

- RHEL 7 STIG Version 3 Release 4
- RHEL 8 STIG Version 1 Release 3

## Windows STIG version history

This section logs version history for Windows script bundles that are updated quarterly.
To see the changes and published versions for a quarter, choose the title to expand the
information. If there are no changes for the quarter, you'll see that reflected in the title.

### 2025 Q3 changes - 9/04/2025 (no changes):

There were no changes for Windows component STIGS for the 2025 third quarter release.

Updated STIG versions and applied STIGS for the 2025 Q2 release as follows:

###### Windows STIG Low (Category III)

- Windows Server 2022 STIG Version 2 Release 4
- Windows Server 2019 STIG Version 3 Release 4
- Windows Server 2016 STIG Version 2 Release 10
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 6
- Windows Firewall STIG Version 2 Release 2
- Internet Explorer 11 STIG Version 2 Release 5
- Microsoft Edge STIG Version 2 Release 2 (Windows Server 2022 only)

###### Windows STIG Medium (Category II)

- Windows Server 2022 STIG Version 2 Release 4
- Windows Server 2019 STIG Version 3 Release 4
- Windows Server 2016 STIG Version 2 Release 10
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 6
- Windows Firewall STIG Version 2 Release 2
- Internet Explorer 11 STIG Version 2 Release 5
- Microsoft Edge STIG Version 2 Release 2 (Windows Server 2022 only)
- Defender STIG Version 2 Release 4

###### Windows STIG High (Category I)

- Windows Server 2022 STIG Version 2 Release 4
- Windows Server 2019 STIG Version 3 Release 4
- Windows Server 2016 STIG Version 2 Release 10
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 6
- Windows Firewall STIG Version 2 Release 2
- Internet Explorer 11 STIG Version 2 Release 5
- Microsoft Edge STIG Version 2 Release 2 (Windows Server 2022 only)
- Defender STIG Version 2 Release 4
  Updated STIGS for Internet Explorer 11 STIG Version 2 Release 5 for all STIG
  components for the 2025 first quarter release.

Updated STIG versions and applied STIGS for the 2024 Q4 release as follows:

###### Windows STIG Low (Category III)

- Windows Server 2022 STIG Version 2 Release 2
- Windows Server 2019 STIG Version 3 Release 2
- Windows Server 2016 STIG Version 2 Release 9
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 2
- Windows Firewall STIG Version 2 Release 2
- Internet Explorer 11 STIG Version 2 Release 5
- Microsoft Edge STIG Version 2 Release 2 (Windows Server 2022 only)

###### Windows STIG Medium (Category II)

- Windows Server 2022 STIG Version 2 Release 2
- Windows Server 2019 STIG Version 3 Release 2
- Windows Server 2016 STIG Version 2 Release 9
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 2
- Windows Firewall STIG Version 2 Release 2
- Internet Explorer 11 STIG Version 2 Release 5
- Microsoft Edge STIG Version 2 Release 2 (Windows Server 2022 only)
- Defender STIG Version 2 Release 4

###### Windows STIG High (Category I)

- Windows Server 2022 STIG Version 2 Release 2
- Windows Server 2019 STIG Version 3 Release 2
- Windows Server 2016 STIG Version 2 Release 9
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 2
- Windows Firewall STIG Version 2 Release 2
- Internet Explorer 11 STIG Version 2 Release 5
- Microsoft Edge STIG Version 2 Release 2 (Windows Server 2022 only)
- Defender STIG Version 2 Release 4
  There were no changes for Windows component STIGS for the 2024 third quarter release.

There were no changes for Windows component STIGS for the 2024 second quarter release.

There were no changes for Windows component STIGS for the 2024 first quarter release.

There were no changes for Windows component STIGS for the 2023 fourth quarter release.

There were no changes for Windows component STIGS for the 2023 third quarter release.

There were no changes for Windows component STIGS for the 2023 second quarter release.

There were no changes for Windows component STIGS for the 2023 first quarter release.

Updated STIG versions and applied STIGS for the 2022 Q4 release as follows:

###### Windows STIG Low (Category III)

- Windows Server 2022 STIG Version 1 Release 1
- Windows Server 2019 STIG Version 2 Release 5
- Windows Server 2016 STIG Version 2 Release 5
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 2
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 2 Release 3
- Microsoft Edge STIG Version 1 Release 6 (Windows Server 2022 only)

###### Windows STIG Medium (Category II)

- Windows Server 2022 STIG Version 1 Release 1
- Windows Server 2019 STIG Version 2 Release 5
- Windows Server 2016 STIG Version 2 Release 5
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 2
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 2 Release 3
- Microsoft Edge STIG Version 1 Release 6 (Windows Server 2022 only)
- Defender STIG Version 2 Release 4 (Windows Server 2022 only)

###### Windows STIG High (Category I)

- Windows Server 2022 STIG Version 1 Release 1
- Windows Server 2019 STIG Version 2 Release 5
- Windows Server 2016 STIG Version 2 Release 5
- Windows Server 2012 R2 MS STIG Version 3 Release 5
- Microsoft .NET Framework 4.0 STIG Version 2 Release 2
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 2 Release 3
- Microsoft Edge STIG Version 1 Release 6 (Windows Server 2022 only)
- Defender STIG Version 2 Release 4 (Windows Server 2022 only)
  There were no changes for Windows component STIGS for the 2022 third quarter release.

Updated STIG versions and applied STIGS for the 2022 Q2 release.

###### Windows STIG Low (Category III)

- Windows Server 2019 STIG Version 2 Release 4
- Windows Server 2016 STIG Version 2 Release 4
- Windows Server 2012 R2 MS STIG Version 3 Release 3
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 1 Release 19

###### Windows STIG Medium (Category II)

- Windows Server 2019 STIG Version 2 Release 4
- Windows Server 2016 STIG Version 2 Release 4
- Windows Server 2012 R2 MS STIG Version 3 Release 3
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 1 Release 19

###### Windows STIG High (Category I)

- Windows Server 2019 STIG Version 2 Release 4
- Windows Server 2016 STIG Version 2 Release 4
- Windows Server 2012 R2 MS STIG Version 3 Release 3
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 1 Release 19
  There were no changes for Windows component STIGS for the 2022 first quarter release.

Updated STIG versions and applied STIGS for the 2021 fourth quarter release.

###### Windows STIG Low (Category III)

- Windows Server 2019 STIG Version 2 Release 3
- Windows Server 2016 STIG Version 2 Release 3
- Windows Server 2012 R2 MS STIG Version 3 Release 3
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 1 Release 19

###### Windows STIG Medium (Category II)

- Windows Server 2019 STIG Version 2 Release 3
- Windows Server 2016 STIG Version 2 Release 3
- Windows Server 2012 R2 MS STIG Version 3 Release 3
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 1 Release 19

###### Windows STIG High (Category I)

- Windows Server 2019 STIG Version 2 Release 3
- Windows Server 2016 STIG Version 2 Release 3
- Windows Server 2012 R2 MS STIG Version 3 Release 3
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 2 Release 1
- Internet Explorer 11 STIG Version 1 Release 19
  Updated STIG versions and applied STIGS for the 2021 third quarter release.

###### Windows STIG Low (Category III)

- Windows Server 2019 STIG Version 2 Release 2
- Windows Server 2016 STIG Version 2 Release 2
- Windows Server 2012 R2 MS STIG Version 3 Release 2
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 1 Release 7
- Internet Explorer 11 STIG Version 1 Release 19

###### Windows STIG Medium (Category II)

- Windows Server 2019 STIG Version 2 Release 2
- Windows Server 2016 STIG Version 2 Release 2
- Windows Server 2012 R2 MS STIG Version 3 Release 2
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 1 Release 7
- Internet Explorer 11 STIG Version 1 Release 19

###### Windows STIG High (Category I)

- Windows Server 2019 STIG Version 2 Release 2
- Windows Server 2016 STIG Version 2 Release 2
- Windows Server 2012 R2 MS STIG Version 3 Release 2
- Microsoft .NET Framework 4.0 STIG Version 2 Release 1
- Windows Firewall STIG Version 1 Release 7
- Internet Explorer 11 STIG Version 1 Release 19
