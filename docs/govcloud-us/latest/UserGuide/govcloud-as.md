# Amazon EC2 Auto Scaling in AWS GovCloud (US)

Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application. You create collections of EC2 instances, called Auto Scaling groups. You can specify the minimum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes below this size. You can specify the maximum number of instances in each Auto Scaling group, and Amazon EC2 Auto Scaling ensures that your group never goes above this size.

## How Amazon EC2 Auto Scaling differs for AWS GovCloud (US)

- Amazon EC2 provides other restrictions. For more information, see [Amazon Elastic Compute Cloud documentation.](govcloud-ec2.md "govcloud-ec2.md")
- You can access Amazon EC2 Auto Scaling using the Amazon EC2 Auto Scaling API and command line interface (CLI) as well as the Amazon EC2 console.
- Target tracking using high resolution metrics is not available in AWS GovCloud (US).

## Documentation for Amazon EC2 Auto Scaling

[Amazon EC2 Auto Scaling documentation](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- Amazon EC2 Auto Scaling is not permitted to contain export-controlled data.
- For example, do not enter export-controlled data in the following fields:
  - Capacity group tag names
  - Capacity group tag name values
  - Capacity group names
  - Amazon EC2 Security Group names
  - Scaling policies
  - Launch notifications
  - Notification topics
  - Policy documents
