

# secretsmanager-using-cmk
<a name="secretsmanager-using-cmk"></a>

Checks if all secrets in AWS Secrets Manager are encrypted using the AWS managed key (`aws/secretsmanager`) or a customer managed key that was created in AWS Key Management Service (AWS KMS). The rule is COMPLIANT if a secret is encrypted using a customer managed key. This rule is NON\_COMPLIANT if a secret is encrypted using `aws/secretsmanager`. 

**Note**  
This rule does not have access to cross-account customer managed keys and evaluates secrets as NON\_COMPLIANT when a cross-account key is used.

**Identifier:** SECRETSMANAGER\_USING\_CMK

**Resource Types:** AWS::SecretsManager::Secret

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
Comma-separated list of KMS key Amazon Resource Names (ARNs) to check if the keys are used in the encryption.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1513c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).