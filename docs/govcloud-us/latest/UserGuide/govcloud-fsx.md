# Amazon FSx in AWS GovCloud (US)

Amazon FSx makes it easy and cost effective to launch and run popular file systems. With Amazon FSx, you can leverage the rich feature sets and fast performance of widely-used open source and commercially-licensed file systems, while avoiding time-consuming administrative tasks like hardware provisioning, software configuration, patching, and backups. It provides cost-efficient capacity and high levels of reliability, and it integrates with other AWS services so that you can manage and use the file systems in cloud-native ways. Amazon FSx let you choose between three widely-used file systems: NetApp ONTAP, Windows File Server, and Lustre.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Amazon FSx differs

The following differences apply to Amazon FSx:

- Amazon FSx for Lustre Persistent 2 with the Intelligent-Tiering storage class is not available.
- For Amazon FSx for OpenZFS, the following features are not available:

  - Single-AZ 2 deployment type
  - Amazon S3 access points

- Amazon File Cache is not available for Amazon FSx.

## Documentation

- [Amazon FSx documentation](../../../fsx/index.md "../../../fsx/index.md")

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
