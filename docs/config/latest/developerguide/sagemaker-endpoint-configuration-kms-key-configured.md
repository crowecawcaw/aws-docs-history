

# sagemaker-endpoint-configuration-kms-key-configured
<a name="sagemaker-endpoint-configuration-kms-key-configured"></a>

Checks if AWS Key Management Service (AWS KMS) key is configured for an Amazon SageMaker endpoint configuration. The rule is NON\_COMPLIANT if 'KmsKeyId' is not specified for the Amazon SageMaker endpoint configuration. 



**Identifier:** SAGEMAKER\_ENDPOINT\_CONFIGURATION\_KMS\_KEY\_CONFIGURED

**Resource Types:** AWS::SageMaker::EndpointConfig

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

kmsKeyArns (Optional)Type: String  
Comma-separated list of specific AWS KMS key ARNs allowed for an Amazon SageMaker endpoint configuration.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1445c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).