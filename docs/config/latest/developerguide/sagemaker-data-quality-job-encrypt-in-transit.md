# sagemaker-data-quality-job-encrypt-in-transit

Checks if Amazon SageMaker data quality job definitions have inter-container traffic encryption enabled when the instance count is 2 or greater. The rule is NON_COMPLIANT if configuration.NetworkConfig.EnableInterContainerTrafficEncryption is false.

**Identifier:** SAGEMAKER_DATA_QUALITY_JOB_ENCRYPT_IN_TRANSIT

**Resource Types:** AWS::SageMaker::DataQualityJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
