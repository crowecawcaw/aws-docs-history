# sagemaker-model-multicontainer-private-registry

This rule checks if SageMaker models with multi-container inference pipelines pull images from VPC-based private registry. The rule is NON_COMPLIANT if any container configuration does not have ImageConfig or has RepositoryAccessMode set to Platform.

**Identifier:** SAGEMAKER_MODEL_MULTICONTAINER_PRIVATE_REGISTRY

**Resource Types:** AWS::SageMaker::Model

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), Middle East (Bahrain), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
