# sagemaker-model-bias-job-isolation

Checks if Amazon SageMaker model bias job definitions have network isolation enabled. The rule is NON_COMPLIANT if configuration.NetworkConfig.EnableNetworkIsolation is false.

**Identifier:** SAGEMAKER_MODEL_BIAS_JOB_ISOLATION

**Resource Types:** AWS::SageMaker::ModelBiasJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** Only available in Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
