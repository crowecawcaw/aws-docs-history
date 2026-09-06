

# redshift-serverless-namespace-cmk-encryption
<a name="redshift-serverless-namespace-cmk-encryption"></a>

Checks if Amazon Redshift Serverless namespaces are encrypted by customer managed AWS KMS keys. The rule is NON\_COMPLIANT if a namespace is not encrypted by a customer managed key. Optionally, you can specify a list of KMS keys for rule to check. 



**Identifier:** REDSHIFT\_SERVERLESS\_NAMESPACE\_CMK\_ENCRYPTION

**Resource Types:** AWS::RedshiftServerless::Namespace

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), Canada West (Calgary) Region

**Parameters:**

kmsKeyArns (Optional)Type: CSV  
Comma-separated list of Amazon Resource Names (ARNs) of customer managed keys for the rule to check. If provided, the rule is NON\_COMPLIANT if an Amazon Redshift Serverless namespace is not encrypted with one of these KMS keys.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1321c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).