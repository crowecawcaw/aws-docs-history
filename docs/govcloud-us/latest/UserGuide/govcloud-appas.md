# Application Auto Scaling in AWS GovCloud (US)

Application Auto Scaling is a web service for developers and system administrators who need a solution for automatically scaling their scalable resources for individual AWS services beyond Amazon EC2.

## How Application Auto Scaling differs for AWS GovCloud (US)

- Application Auto Scaling notifications are not currently supported in the AWS Health Dashboard in the AWS GovCloud (US) Regions.
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

## Documentation for Application Auto Scaling

For more information about anything in the above list, see the documentation for the specific service at [AWS documentation](https://aws.amazon.com/documentation/ "https://aws.amazon.com/documentation/").

For information about scaling Amazon EC2 instances in AWS GovCloud (US), see [Amazon EC2 Auto Scaling](govcloud-as.md "govcloud-as.md")in this guide.

For more information about AWS Auto Scaling and Application Auto Scaling, see [AWS Auto Scaling documentation](https://aws.amazon.com/documentation/autoscaling/ "https://aws.amazon.com/documentation/autoscaling/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EC2 Auto Scaling is not permitted to contain export-controlled data.
- For example, do not enter export-controlled data in the following fields:
  - Scaling policy names
  - Scaling policy configuration
