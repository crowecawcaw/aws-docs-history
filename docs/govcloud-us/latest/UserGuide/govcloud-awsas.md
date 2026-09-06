

# AWS Auto Scaling in AWS GovCloud (US)
<a name="govcloud-awsas"></a>

With AWS Auto Scaling, you can quickly discover the scalable AWS resources for your application and set up dynamic scaling. It uses Amazon EC2 Auto Scaling to scale your EC2 instances and Application Auto Scaling to scale resources from other services.The AWS Management Console provides a web interface for AWS Auto Scaling.

## How AWS Auto Scaling differs
<a name="how_shared_aws_as_differs"></a>

The following differences apply to AWS Auto Scaling:
+ Predictive scaling is not available.
+ The following CloudFormation resource is not available in the AWS GovCloud (US) Regions:
  +  [AWS::AutoScalingPlans::ScalingPlan](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-as.html) 

## Documentation
<a name="govcloud-awsas-docs-2"></a>
+  [Amazon EC2 Auto Scaling in AWS GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-as.html) 
+  [AWS Auto Scaling documentation](https://docs.aws.amazon.com/documentation/autoscaling/) 

## Export-controlled content
<a name="govcloud-awsas-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Auto Scaling is not permitted to contain export-controlled data.
+ For example, do not enter export-controlled data in the following fields:
  + Scaling plan names
  + Scaling policy names
  + Scaling policy configurations