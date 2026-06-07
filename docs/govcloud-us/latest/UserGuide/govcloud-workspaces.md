# Amazon WorkSpaces in AWS GovCloud (US)

Amazon WorkSpaces is a managed, secure cloud desktop service. You can use Amazon WorkSpaces to provision Windows, Amazon Linux 2, Ubuntu, Red Hat Enterprise Linux (RHEL), or Rocky Linux desktops in just a few minutes and quickly scale to provide thousands of desktops to workers across the globe. You can pay either monthly or hourly, just for the WorkSpaces you launch, which helps you save money when compared to traditional desktops and on-premises virtual desktop infrastructure (VDI) solutions. Amazon WorkSpaces helps you eliminate the complexity in managing hardware inventory and OS versions and patches which helps simplify your desktop delivery strategy. With Amazon WorkSpaces, your users get a fast, responsive desktop of their choice that they can access anywhere, anytime, from any supported device.

## How Amazon WorkSpaces differs

The following differences apply to Amazon WorkSpaces:

- The Amazon WorkSpaces Application Manager console is not available.
- The Web Access client (from browser) does not support PCoIP WorkSpaces.
- The cross-Region redirection feature is not available.
- The **Forgot Password** option and the **Welcome Email** feature are not available in the AWS GovCloud (US) Regions. Users cannot reset their own passwords and users with new WorkSpaces will not receive a welcome email.
- Amazon WorkSpaces Advisor is not available.

## Documentation

- [Amazon WorkSpaces documentation](../../../workspaces.md "../../../workspaces.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon WorkSpaces metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your WorkSpaces.

Do not enter export-controlled data in the following console fields:

    + AMI descriptions
    + Resource tags
    + If importing export-controlled images, do not use pre-signed URLs for the CLI argument
    + Key pairs created using HTTP
