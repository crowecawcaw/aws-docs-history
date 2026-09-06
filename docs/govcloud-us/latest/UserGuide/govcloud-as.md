

# Amazon EC2 Auto Scaling in AWS GovCloud (US)
<a name="govcloud-as"></a>

Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Auto Scaling groups. You can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size. You can specify the maximum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes above this size.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon EC2 Auto Scaling differs
<a name="govcloud-as-diffs"></a>

The following differences apply to Amazon EC2 Auto Scaling:
+ Amazon EC2 provides other restrictions. For more information, see [Amazon EC2 documentation.](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-ec2.html) 
+ You can access Amazon EC2 Auto Scaling using the Amazon EC2 Auto Scaling API and command line interface (CLI) as well as the Amazon EC2 console.
+ Target tracking using high resolution metrics is not available.

## Documentation
<a name="govcloud-as-docs"></a>
+  [Amazon EC2 Auto Scaling documentation](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 

## Export-controlled content
<a name="govcloud-as-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Auto Scaling is not permitted to contain export-controlled data.
+ For example, do not enter export-controlled data in the following fields:
  + Capacity group tag names
  + Capacity group tag name values
  + Capacity group names
  +  Amazon EC2 Security Group names
  + Scaling policies
  + Launch notifications
  + Notification topics
  + Policy documents