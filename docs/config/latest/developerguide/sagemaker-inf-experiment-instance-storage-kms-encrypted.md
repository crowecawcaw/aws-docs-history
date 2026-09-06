

# sagemaker-inf-experiment-instance-storage-kms-encrypted
<a name="sagemaker-inf-experiment-instance-storage-kms-encrypted"></a>

Checks whether a SageMaker inference experiment is configured with a customer-managed AWS KMS key for instance storage volume encryption. The rule is NON\_COMPLIANT if KmsKey is not set or is empty. 



**Identifier:** SAGEMAKER\_INF\_EXPERIMENT\_INSTANCE\_STORAGE\_KMS\_ENCRYPTED

**Resource Types:** AWS::SageMaker::InferenceExperiment

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1467c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).