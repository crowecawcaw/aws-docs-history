# AWS Auto Scaling in AWS GovCloud (US)

With AWS Auto Scaling, you can quickly discover the scalable AWS resources for your application and set up dynamic scaling. It uses Amazon EC2 Auto Scaling to scale your EC2 instances and Application Auto Scaling to scale resources from other services.The AWS Management Console provides a web interface for AWS Auto Scaling.

## How AWS Auto Scaling differs for AWS GovCloud (US)

- Predictive scaling is not available in the AWS GovCloud (US) Regions.
- The following CloudFormation resource is not available in the AWS GovCloud (US) Regions:
  - [AWS::AutoScalingPlans::ScalingPlan](govcloud-as.md "govcloud-as.md")

## Documentation for AWS Auto Scaling

For more information about anything in the above list, see the documentation for the specific service at [AWS documentation](https://aws.amazon.com/documentation/ "https://aws.amazon.com/documentation/").

For information about scaling Amazon EC2 instances in AWS GovCloud (US), see [Amazon EC2 Auto Scaling](govcloud-as.md "govcloud-as.md") in this guide.

For more information about AWS Auto Scaling and Application Auto Scaling, see [AWS Auto Scaling documentation](https://aws.amazon.com/documentation/autoscaling/ "https://aws.amazon.com/documentation/autoscaling/").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EC2 Auto Scaling is not permitted to contain export-controlled data.
- For example, do not enter export-controlled data in the following fields:
  - Scaling plan names
  - Scaling policy names
  - Scaling policy configurations
