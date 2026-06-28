# AWS Auto Scaling in AWS GovCloud (US)

With AWS Auto Scaling, you can quickly discover the scalable AWS resources for your application and set up dynamic scaling. It uses Amazon EC2 Auto Scaling to scale your EC2 instances and Application Auto Scaling to scale resources from other services.The AWS Management Console provides a web interface for AWS Auto Scaling.

## How AWS Auto Scaling differs

The following differences apply to AWS Auto Scaling:

- Predictive scaling is not available.
- The following CloudFormation resource is not available in the AWS GovCloud (US) Regions:

  - [AWS::AutoScalingPlans::ScalingPlan](govcloud-as.md "govcloud-as.md")

## Documentation

- [Amazon EC2 Auto Scaling in AWS GovCloud (US)](govcloud-as.md "govcloud-as.md")
- [AWS Auto Scaling documentation](../../../documentation/autoscaling.md "../../../documentation/autoscaling.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Auto Scaling is not permitted to contain export-controlled data.
- For example, do not enter export-controlled data in the following fields:

  - Scaling plan names
  - Scaling policy names
  - Scaling policy configurations
