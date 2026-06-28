# Application Auto Scaling in AWS GovCloud (US)

Application Auto Scaling is a web service for developers and system administrators who need a solution for automatically scaling their scalable resources for individual AWS services beyond Amazon EC2.

## Region availability

This service is available in the following AWS GovCloud (US) Regions:

- AWS GovCloud (US-West)
- AWS GovCloud (US-East)

## How Application Auto Scaling differs

The following differences apply to Application Auto Scaling:

- Application Auto Scaling notifications are not currently supported in the AWS Health Dashboard.
- The following resources are not currently supported for Application Auto Scaling in the AWS GovCloud (US-West) Region:

  - Amazon Neptune clusters
  - Spot Fleet requests
  - Custom resources

- The following resources are not currently supported for Application Auto Scaling in the AWS GovCloud (US-East) Region:

  - Amazon Comprehend document classification and entity recognizer endpoints
  - Amazon Neptune clusters
  - SageMaker AI endpoint variants
  - Spot Fleet requests
  - Custom resources

## Documentation

- [Amazon EC2 Auto Scaling in AWS GovCloud (US)](govcloud-as.md "govcloud-as.md")
- [AWS Auto Scaling documentation](../../../documentation/autoscaling.md "../../../documentation/autoscaling.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Auto Scaling is not permitted to contain export-controlled data.
- For example, do not enter export-controlled data in the following fields:

  - Scaling policy names
  - Scaling policy configuration
