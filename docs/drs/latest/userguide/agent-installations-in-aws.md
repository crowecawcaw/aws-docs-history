# Installing the AWS Replication Agent in

AWS

When installing an AWS Replication Agent on an AWS EC2 instance (when the source and
recovery servers are both in AWS Regions), you don't need to generate credentials.
Instead, you can use an instance profile with the required IAM policy:

- Go to the EC2 console and select your EC2 instance.
- From the top right-hand menu, select **Actions > Security >
  Modify IAM role**.
- Use a role that contains the [AWSElasticDisasterRecoveryEc2InstancePolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryEc2InstancePolicy.md") policy.

If none exists, click **Create new IAM role**, attach
the policy and return to the EC2 console window.

- Select your new role from the drop-down list and click **Update**.
