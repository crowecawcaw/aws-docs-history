

# IAM instance profiles for AWS Parallel Computing Service
<a name="security-instance-profiles"></a>

Applications that run on an EC2 instance must include AWS credentials in any AWS API requests they make. We recommend you use an IAM role to manage temporary credentials on the EC2 instance. You can define an instance profile to do this, and attach it to your instances. For more information, see [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the *Amazon Elastic Compute Cloud User Guide*.

**Note**  
When you use the AWS Management Console to create an IAM role for Amazon EC2, the console creates an instance profile automatically and gives it the same name as the IAM role. If you use the AWS CLI, AWS API actions, or an AWS SDK to create the IAM role, you create the instance profile as a separate action. For more information, see [Instance profiles](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#ec2-instance-profile) in the *Amazon Elastic Compute Cloud User Guide*.

You must specify the Amazon Resource Name (ARN) of an instance profile when you create a compute node groups. You can choose different instance profiles for some or all compute node groups.

## Requirements
<a name="security-instance-profiles_requirements"></a>

### IAM role of the instance profile
<a name="security-instance-profiles_requirements_role"></a>

The IAM role associated with the instance profile must have `/aws-pcs/` in its path, or its name must start with `AWSPCS`. 

**Example IAM role ARNs**
+  `arn:aws:iam::*:role/AWSPCS-example-role-1` 
+  `arn:aws:iam::*:role/aws-pcs/example-role-2` 

### Permissions
<a name="security-instance-profiles_requirements_permissions"></a>

 The IAM role associated with the instance profile for AWS PCS must include the following policy.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "pcs:RegisterComputeNodeGroupInstance"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

------

## Additional policies
<a name="security-instance-profiles_additional-policies"></a>

Consider adding managed policies to the instance profile. For example:
+  [AmazonS3ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonS3ReadOnlyAccess.html) provides read-only access to all S3 buckets.
+ [AmazonSSMManagedInstanceCore](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.html) enables AWS Systems Manager service core functionality, such as remote access directly from the Amazon Management Console.
+ [CloudWatchAgentServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchAgentServerPolicy.html) contains permissions required to use AmazonCloudWatchAgent on servers.

You can also include your own IAM policies that support your specific use case. 