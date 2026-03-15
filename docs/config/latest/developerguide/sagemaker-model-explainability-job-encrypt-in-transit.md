# sagemaker-model-explainability-job-encrypt-in-transit

Checks if Amazon SageMaker model explainability job definitions have inter-container traffic encryption enabled when instance count is 2 or greater. The rule is NON_COMPLIANT if configuration.NetworkConfig.EnableInterContainerTrafficEncryption is false.

**Identifier:** SAGEMAKER_MODEL_EXPLAINABILITY_JOB_ENCRYPT_IN_TRANSIT

**Resource Types:** AWS::SageMaker::ModelExplainabilityJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
