

# kms-cmk-not-scheduled-for-deletion
<a name="kms-cmk-not-scheduled-for-deletion"></a>

Checks if AWS Key Management Service (AWS KMS) keys are not scheduled for deletion in AWS KMS. The rule is NON\_COMPLIANT if KMS keys are scheduled for deletion. 



**Identifier:** KMS\_CMK\_NOT\_SCHEDULED\_FOR\_DELETION

**Resource Types:** AWS::KMS::Key

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Europe (Milan), Asia Pacific (Taipei) Region

**Parameters:**

kmsKeyIds (Optional)Type: String  
(Optional) Comma-separated list of specific customer managed key IDs not to be scheduled for deletion. If you do not specify any keys, the rule checks all the keys.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1051c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).