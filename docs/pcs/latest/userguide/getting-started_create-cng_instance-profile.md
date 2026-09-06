

# Create an instance profile for AWS PCS
<a name="getting-started_create-cng_instance-profile"></a>

Compute node groups require an instance profile when they are created. If you use the AWS Management Console to create a role for Amazon EC2, the console automatically creates an instance profile and gives it the same name as the role. For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *AWS Identity and Access Management User Guide*.

 In the following procedure, you use the AWS Management Console to create a role for Amazon EC2, which also creates the instance profile for your compute node groups. 

**To create the role and instance profile**
+ Navigate to the [IAM console](https://console.aws.amazon.com/iam).
+ Under **Access management**, choose **Roles**.
+ Choose **Create role**.
+ Under **Select trusted entity**:
  + For **Trusted entity type**, select **AWS service**
  + Under **Use case**, select **EC2**.
    + Then, under **Choose a use case** for the specified service, choose **EC2**.
  + Choose **Next**.
+ Under **Add permissions**:
  + In **Permissions policies**, search for **AWSPCSComputeNodePolicy**. This AWS managed policy grants the one permission a node needs to register with, and connect to, your AWS PCS cluster.
  + Check the box beside **AWSPCSComputeNodePolicy** to add it to the role.
  + In **Permissions policies**, search for **AmazonSSMManagedInstanceCore**. This AWS managed policy lets you connect to nodes with Amazon EC2 Systems Manager (SSM), so you can reach them without opening SSH or managing key pairs.
  + Check the box beside **AmazonSSMManagedInstanceCore** to add it to the role.
  + In **Permissions policies**, search for **AmazonS3ReadOnlyAccess**. This AWS managed policy lets nodes download the node lifecycle action scripts from Amazon S3, including the scripts that AWS maintains to mount storage and forward logs.
  + Check the box beside **AmazonS3ReadOnlyAccess** to add it to the role.
  + In **Permissions policies**, search for **CloudWatchAgentServerPolicy**. This AWS managed policy lets the `configure-cloudwatch-logs` node lifecycle action create log streams and forward each node's lifecycle action logs to Amazon CloudWatch Logs.
  + Check the box beside **CloudWatchAgentServerPolicy** to add it to the role.
  + Choose **Next**.
+ Under **Name, review, and create**:
  + Under **Role details**:
    + For **Role name**, enter `AWSPCS-getstarted-role`.
  + Choose **Create role**.