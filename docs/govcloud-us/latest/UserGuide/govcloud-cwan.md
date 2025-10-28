# AWS Cloud WAN in AWS GovCloud (US)

AWS Cloud WAN is a managed wide-area networking (WAN) service that you can use to build,
manage, and monitor a unified global network that connects resources running across your
cloud and on-premises environments.

## How AWS Cloud WAN differs for AWS GovCloud (US)

- Direct Connect gateway attachments are not supported.

## Documentation for AWS Cloud WAN

[AWS Cloud WAN documentation](../../../network-manager/latest/cloudwan/what-is-cloudwan.md "../../../network-manager/latest/cloudwan/what-is-cloudwan.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains
how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings.
The list can be used as a guide to help meet applicable customer compliance obligations.
Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Cloud WAN gateway metadata is not permitted to contain export-controlled data.
  This metadata includes all of the configuration data that you enter when setting
  up and maintaining your global and core networks. This applies to free-text
  entry fields for Cloud WAN resources, including but not limited to:
  - Resource names
  - Resource descriptions
  - Tag keys and values
