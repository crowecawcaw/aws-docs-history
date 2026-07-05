# sagemaker-model-explainability-job-network-isolation

Checks whether an Amazon SageMaker model explainability job definition has network isolation enabled. The rule is NON\_COMPLIANT if NetworkConfig.EnableNetworkIsolation is not set to true.

**Identifier:** SAGEMAKER\_MODEL\_EXPLAINABILITY\_JOB\_NETWORK\_ISOLATION

**Resource Types:** AWS::SageMaker::ModelExplainabilityJobDefinition

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
