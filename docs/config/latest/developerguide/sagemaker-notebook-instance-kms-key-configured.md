

# sagemaker-notebook-instance-kms-key-configured
<a name="sagemaker-notebook-instance-kms-key-configured"></a>

Checks if an AWS Key Management Service (AWS KMS) key is configured for an Amazon SageMaker notebook instance. The rule is NON\_COMPLIANT if 'KmsKeyId' is not specified for the SageMaker notebook instance. 



**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_KMS\_KEY\_CONFIGURED

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

kmsKeyArns (Optional)Type: String  
Comma-separated list of AWS KMS key ARNs allowed for an Amazon SageMaker notebook instance.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1495c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).