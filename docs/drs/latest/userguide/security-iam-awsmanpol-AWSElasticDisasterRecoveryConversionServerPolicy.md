

# AWS managed policy: AWSElasticDisasterRecoveryConversionServerPolicy
<a name="security-iam-awsmanpol-AWSElasticDisasterRecoveryConversionServerPolicy"></a>

This policy is attached to the AWS Elastic Disaster Recovery Conversion Server's instance role. This policy allows AWS Elastic Disaster Recovery (AWS DRS) Conversion Servers, which are EC2 instances launched by AWS DRS, to communicate with the DRS service. An IAM role with this policy is attached (as an EC2 Instance Profile) by DRS to the DRS Conversion Servers, which are automatically launched and terminated by DRS when needed. DRS Conversion Servers are used by AWS Elastic Disaster Recovery when users choose to recover source servers using the AWS DRS console, CLI, or API. We do not recommend that you attach this policy to your users or roles.

 **Permissions details** 

To view the policy permission details see [AWSElasticDisasterRecoveryConversionServerPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryConversionServerPolicy.html) in the AWS Managed Policy Reference Guide.