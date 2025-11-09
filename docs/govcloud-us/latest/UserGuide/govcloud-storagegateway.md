# AWS Storage Gateway in AWS GovCloud (US)

AWS Storage Gateway is a service that connects an on-premises software appliance with cloud-based storage to provide seamless and secure integration between your on-premises IT environment and the AWS storage infrastructure in the cloud.

## How AWS Storage Gateway differs for AWS GovCloud (US)

- A file gateway created inside AWS GovCloud (US) cannot connect to a bucket outside of the AWS GovCloud (US) Regions.
- A file gateway created outside of AWS GovCloud (US) cannot connect to a bucket inside AWS GovCloud (US).
- TLS-enabled endpoint are available.
- [AWS Storage Gateway Hardware Appliance](../../../storagegateway/latest/userguide/HardwareAppliance.md "../../../storagegateway/latest/userguide/HardwareAppliance.md") is not supported for use with the AWS Storage Gateway service running in the AWS GovCloud (US) Region.

## Documentation for AWS Storage Gateway

[AWS Storage Gateway documentation](../../../storagegateway/index.md "../../../storagegateway/index.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Storage Gateway metadata is not permitted to contain export-controlled data. This metadata includes all configuration data that you enter when creating and maintaining your gateway in AWS Storage Gateway, including but not limited to:

      + Storage Gateway name
      + Tape barcode
      + The name of the iSCSI initiator configured for CHAP

  Do not enter export-controlled data into the following console fields:

      + Resource tag: Key
      + Resource tag: Value

## AWS Storage Gateway AMI Information

The following table lists the available AWS Storage Gateway AMIs in the AWS GovCloud (US) Regions.

| Gateway Type | AMI ID                     |
| ------------ | -------------------------- |
| File Gateway | ami-0b5d2a6a us-gov-west-1 |
