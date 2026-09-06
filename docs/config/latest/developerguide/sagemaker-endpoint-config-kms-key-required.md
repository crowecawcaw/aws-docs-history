

# sagemaker-endpoint-config-kms-key-required
<a name="sagemaker-endpoint-config-kms-key-required"></a>

Checks whether SageMaker endpoint configurations are encrypted with a customer-managed KMS key. The rule is NON\_COMPLIANT if KmsKeyId is not set on the endpoint configuration. 



**Identifier:** SAGEMAKER\_ENDPOINT\_CONFIG\_KMS\_KEY\_REQUIRED

**Resource Types:** AWS::SageMaker::EndpointConfig

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), Asia Pacific (Thailand), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), Europe (Zurich) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1447c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).