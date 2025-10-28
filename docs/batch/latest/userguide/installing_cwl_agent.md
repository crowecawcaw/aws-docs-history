# Install and configure the CloudWatch agent

You can create an Amazon EC2 launch template that includes CloudWatch monitoring. For more
information, see [Launch
an instance from a launch template](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md#lt-initiate-launch-template "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md#lt-initiate-launch-template") and [Advanced
details](../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md#lt-advanced-details "../../../AWSEC2/latest/UserGuide/ec2-launch-templates.md#lt-advanced-details") in the _Amazon EC2 User Guide_.

You can also install the CloudWatch agent on an existing Amazon EC2 AMI and then specify the image
in the AWS Batch first-run wizard. For more information, see [Installing the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md "../../../AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.md") and [Getting started with AWS Batch tutorials](Batch_GetStarted.md "Batch_GetStarted.md").

###### Note

Launch templates are not supported on AWS Fargate resources.
