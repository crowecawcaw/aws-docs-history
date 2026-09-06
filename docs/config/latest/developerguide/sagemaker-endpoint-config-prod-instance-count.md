

# sagemaker-endpoint-config-prod-instance-count
<a name="sagemaker-endpoint-config-prod-instance-count"></a>

Checks if Amazon SageMaker endpoint configurations have production variants `InitialInstanceCount` set to a value greater than 1. The rule is NON\_COMPLIANT if production variants `InitialInstanceCount` is equal to 1. 



**Identifier:** SAGEMAKER\_ENDPOINT\_CONFIG\_PROD\_INSTANCE\_COUNT

**Resource Types:** AWS::SageMaker::EndpointConfig

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), Mexico (Central), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1449c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).