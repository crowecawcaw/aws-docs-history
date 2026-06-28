# AWS Config in AWS GovCloud (US)

AWS Config provides a detailed view of the resources associated with your AWS account, including how they are configured, how they are related to one another, and how the configurations and their relationships have changed over time.

AWS Config and AWS Config Rules are supported in the AWS GovCloud (US) Region.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How AWS Config differs

The following differences apply to AWS Config:

- For a list of rules supported in AWS GovCloud (US-East), see [List of AWS Config Managed Rules by Region Availability | AWS GovCloud (US-East)](../../../config/latest/developerguide/managing-rules-by-region-availability.md#aws-govcloud-us-east-section-head "../../../config/latest/developerguide/managing-rules-by-region-availability.md#aws-govcloud-us-east-section-head").
- For a list of rules supported in AWS GovCloud (US-West), see [List of AWS Config Managed Rules by Region Availability | AWS GovCloud (US-West)](../../../config/latest/developerguide/managing-rules-by-region-availability.md#aws-govcloud-us-west-section-head "../../../config/latest/developerguide/managing-rules-by-region-availability.md#aws-govcloud-us-west-section-head").
- AWS Config recording of third-party resources or custom resource types are not available.
- AWS Systems Manager documents (SSM documents) for AWS Config remediation actions are not available.

## Documentation

- [AWS Config documentation](../../../documentation/config.md "../../../documentation/config.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- AWS Config metadata is not permitted to contain export-controlled data. This includes the naming and configuration data that you enter when creating and managing your AWS Config settings.

For example, do not enter export-controlled data into user input fields such as the following:

    + Annotations for rule evaluations
    + Resource identifier
    + S3 bucket name
    + SNS topic name
    + Tag key
