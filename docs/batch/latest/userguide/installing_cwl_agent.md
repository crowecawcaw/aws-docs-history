

# Install and configure the CloudWatch agent
<a name="installing_cwl_agent"></a>

You can create an Amazon EC2 launch template that includes CloudWatch monitoring. For more information, see [ Launch an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#lt-initiate-launch-template) and [ Advanced details](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html#lt-advanced-details) in the *Amazon EC2 User Guide*.

You can also install the CloudWatch agent on an existing Amazon EC2 AMI and then specify the image in the AWS Batch first-run wizard. For more information, see [ Installing the CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html) and [Getting started with AWS Batch tutorials](Batch_GetStarted.md).

**Note**  
Launch templates are not supported on AWS Fargate resources.