# AWS managed policy:

AWSElasticDisasterRecoveryRecoveryInstancePolicy

This policy is attached to the instance role of AWS Elastic Disaster Recovery's recovery instance.

This policy allows the AWS Elastic Disaster Recovery (AWS DRS) recovery instance, which are EC2
instances launched by AWS DRS - to communicate with the AWS DRS service, and to
be able to failback to their original source infrastructure. An IAM role with
this policy is attached (as an Amazon EC2 Instance Profile) by AWS DRS to the AWS DRS
recovery instances. We do not recommend that you attach this policy to your
users or roles.

**Permissions details**

To view the policy permission details see [AWSElasticDisasterRecoveryRecoveryInstancePolicy](../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryRecoveryInstancePolicy.md "../../../aws-managed-policy/latest/reference/AWSElasticDisasterRecoveryRecoveryInstancePolicy.md") in the AWS Managed Policy Reference Guide.
