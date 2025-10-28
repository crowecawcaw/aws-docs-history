# AWS managed policy:

AWSElasticDisasterRecoveryConversionServerPolicy

This policy is attached to the AWS Elastic Disaster Recovery conversion server’s instance role.

This policy allows AWS Elastic Disaster Recovery (AWS DRS) Conversion Servers, which are EC2
instances launched by AWS DRS, to communicate with the DRS service. An IAM
role with this policy is attached (as an EC2 instance Profile) by DRS to the DRS
Conversion Servers, which are automatically launched and terminated by DRS, when
needed. We do not recommend that you attach this policy to your users or roles.
DRS Conversion Servers are used by Elastic Disaster Recovery when users choose
to recover source servers using the AWS DRS console, CLI, or API.

This policy is attached to the AWS Elastic Disaster Recovery Conversion
server’s instance role. This policy allows the AWS DRS Conversion Server, which
are EC2 instances launched by AWS DRS, to communicate with AWS DRS. An IAM
role with this policy is attached (as an EC2 Instance Profile) by AWS DRS to the
AWS DRS conversion servers, which are automatically launched and terminated by
AWS DRS, when needed. We do not recommend that you attach this policy to your
users or roles. AWS DRS conversion servers are used by Elastic Disaster Recovery
when users choose to recover source servers using the AWS DRS console, CLI, or
API.

**Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryConversionServerPolicy](../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryConversionServerPolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryConversionServerPolicy.md") in the AWS Managed Policy Reference Guide.
