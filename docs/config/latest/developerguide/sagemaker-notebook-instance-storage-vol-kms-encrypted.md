

# sagemaker-notebook-instance-storage-vol-kms-encrypted
<a name="sagemaker-notebook-instance-storage-vol-kms-encrypted"></a>

Checks whether an Amazon SageMaker notebook instance is configured with a customer managed AWS KMS key for storage volume encryption. The rule is NON\_COMPLIANT if KmsKeyId is not set or is empty. 



**Identifier:** SAGEMAKER\_NOTEBOOK\_INSTANCE\_STORAGE\_VOL\_KMS\_ENCRYPTED

**Resource Types:** AWS::SageMaker::NotebookInstance

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1501c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).