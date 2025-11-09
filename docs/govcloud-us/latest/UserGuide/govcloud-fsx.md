# Amazon FSx in AWS GovCloud (US)

Amazon FSx makes it easy and cost effective to launch and run popular file systems. With Amazon FSx, you can leverage the rich feature sets and fast performance of widely-used open source and commercially-licensed file systems, while avoiding time-consuming administrative tasks like hardware provisioning, software configuration, patching, and backups. It provides cost-efficient capacity and high levels of reliability, and it integrates with other AWS services so that you can manage and use the file systems in cloud-native ways. Amazon FSx let you choose between three widely-used file systems: NetApp ONTAP, Windows File Server, and Lustre.

## How Amazon FSx differs for AWS GovCloud (US)

- Amazon FSx for Lustre Persistent_2 is not available.
- For Amazon FSx for OpenZFS, the following features aren’t available:
  - Single-AZ 2 deployment type
  - Amazon S3 access points

- Amazon File Cache is not available for Amazon FSx.

## Documentation for Amazon FSx

[Amazon FSx documentation](../../../fsx/index.md "../../../fsx/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Resource Tags.
- ClientRequestTokens.
- FSx for Windows File Server file system configuration fields:
  - Self-managed Active Directory user names
  - Self-managed Active Directory domain names
  - Self-managed Active Directory organizational unit distinguished names
  - DNS aliases

- FSx for Lustre file system configuration fields:
  - S3 import and export data paths
