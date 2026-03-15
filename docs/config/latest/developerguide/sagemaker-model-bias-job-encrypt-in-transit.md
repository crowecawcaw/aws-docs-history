# sagemaker-model-bias-job-encrypt-in-transit

Checks if Amazon SageMaker model bias job definitions have inter-container traffic encryption enabled when the instance count is 2 or greater. The rule is NON_COMPLIANT if configuration.NetworkConfig.EnableInterContainerTrafficEncryption is false.

**Identifier:** SAGEMAKER_MODEL_BIAS_JOB_ENCRYPT_IN_TRANSIT

**Resource Types:** AWS::SageMaker::ModelBiasJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** Only available in Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
