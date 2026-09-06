

# AWS managed policy: AWSElasticDisasterRecoveryReadOnlyAccess
<a name="security-iam-awsmanpol-AWSElasticDisasterRecoveryReadOnlyAccess"></a>

You can attach the AWSElasticDisasterRecoveryReadOnlyAccess policy to your IAM identities.

This policy provides permissions to all read-only public APIs of AWS Elastic Disaster Recovery (AWS DRS), as well as some read-only APIs of other AWS services that are required to make full read-only use of the DRS console. This includes:
+ **AWS Elastic Disaster Recovery (read-only)** – View all DRS resources such as Source Servers, Recovery Instances, Recovery Snapshots, recovery plans, recovery plan executions, and post-launch actions.
+ **IAM (read-only)** – List IAM roles in your account.
+ **EC2 (read-only)** – View EC2 instance details, launch templates, security groups, and subnets related to your recovery environment.
+ **SSM (read-only)** – View Systems Manager configurations such as post-launch action settings and automation executions.

Attach this policy to your users or roles. This policy is ideal for team members who need visibility into your disaster recovery setup, such as auditors or monitoring teams, without the ability to make changes.

 **Permissions details** 

To view the policy permission details see [AWSElasticDisasterRecoveryReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryReadOnlyAccess.html) in the AWS Managed Policy Reference Guide.