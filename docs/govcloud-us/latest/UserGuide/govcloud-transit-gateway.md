# AWS Transit Gateway in AWS GovCloud (US)

A transit gateway is a network transit hub that interconnects your virtual private clouds (VPC) and on-premises networks.

## How AWS Transit Gateway differs for AWS GovCloud (US)

- You can’t visualize your global network in geographic map view in Transit Gateway Network Manager console.
- Inter-Region peering is only supported between AWS GovCloud (US-East) and AWS GovCloud (US-West). You can’t create an Inter-Region peering between a AWS GovCloud (US) Region and any other AWS Region.

## Documentation for AWS Transit Gateway

[Transit Gateway documentation](../../../vpc.md#aws-transit-gateway "../../../vpc.md#aws-transit-gateway")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Transit gateway metadata is not permitted to contain export-controlled data. This metadata includes all of the configuration data that you enter when setting up and maintaining your transit gateways. This applies to free-text entry fields for transit gateway resources, including but not limited to:
  - Resource names
  - Resource descriptions
  - Tag keys and values
