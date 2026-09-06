

# AI Security Best Practices standard in Security Hub CSPM
<a name="standards-ai-security"></a>

The AI Security Best Practices standard is a set of automated security checks that detect when deployed AI resources do not align with security best practices. Developed by AWS security experts, this standard provides a curated set of controls that help you identify areas where your AI workloads deviate from recommended security configurations.

In AWS Security Hub CSPM, the AI Security Best Practices standard includes controls that continuously evaluate your resources. The controls cover security domains including but not limited to network isolation, encryption at rest and in transit, VPC placement, AWS KMS key usage, and private registry requirements. Each control is assigned a category that reflects the security function that the control applies to. For a list of categories and additional details, see [Control categories in Security Hub CSPM](control-categories.md).

The AI Security Best Practices standard has the following Amazon Resource Name (ARN): `arn:aws:securityhub:{{region}}::standards/ai-security-best-practices/v/1.0.0`, where {{region}} is the Region code for the applicable AWS Region. You can also use the [GetEnabledStandards](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_GetEnabledStandards.html) operation of the Security Hub CSPM API to retrieve the ARN of a standard that's currently enabled.

## Controls that apply to the standard
<a name="ai-security-standard-controls"></a>

The following list specifies which AWS Security Hub CSPM controls apply to the AI Security Best Practices standard (v1.0.0). To review the details of a control, choose the control.
+ [[Bedrock.1] Amazon Bedrock data sources should be encrypted with customer managed AWS KMS keys](bedrock-controls.md#bedrock-1)
+ [[BedrockAgentCore.1] Bedrock AgentCore runtimes should be configured with VPC network mode](bedrockagentcore-controls.md#bedrockagentcore-1)
+ [[BedrockAgentCore.2] Bedrock AgentCore Gateways should require authorization for inbound requests](bedrockagentcore-controls.md#bedrockagentcore-2)
+ [[BedrockAgentCore.3] Bedrock AgentCore Memory should be encrypted with customer managed AWS KMS keys](bedrockagentcore-controls.md#bedrockagentcore-3)
+ [[BedrockAgentCore.4] Bedrock AgentCore Gateway should be encrypted with customer managed AWS KMS keys](bedrockagentcore-controls.md#bedrockagentcore-4)
+ [[BedrockAgentCore.5] Bedrock AgentCore custom browsers should not use public network mode](bedrockagentcore-controls.md#bedrockagentcore-5)
+ [[BedrockAgentCore.6] Bedrock AgentCore custom browsers should have session recording enabled](bedrockagentcore-controls.md#bedrockagentcore-6)
+ [[BedrockAgentCore.7] Bedrock AgentCore custom code interpreters should use a private network configuration](bedrockagentcore-controls.md#bedrockagentcore-7)
+ [[SageMaker.1] Amazon SageMaker notebook instances should not have direct internet access](sagemaker-controls.md#sagemaker-1)
+ [[SageMaker.2] SageMaker notebook instances should be launched in a custom VPC](sagemaker-controls.md#sagemaker-2)
+ [[SageMaker.3] Users should not have root access to SageMaker notebook instances](sagemaker-controls.md#sagemaker-3)
+ [[SageMaker.4] SageMaker endpoint production variants should have an initial instance count greater than 1](sagemaker-controls.md#sagemaker-4)
+ [[SageMaker.5] SageMaker models should have network isolation enabled](sagemaker-controls.md#sagemaker-5)
+ [[SageMaker.8] SageMaker notebook instances should run on supported platforms](sagemaker-controls.md#sagemaker-8)
+ [[SageMaker.9] SageMaker data quality job definitions should have inter-container traffic encryption enabled](sagemaker-controls.md#sagemaker-9)
+ [[SageMaker.10] SageMaker model explainability job definitions should have inter-container traffic encryption enabled](sagemaker-controls.md#sagemaker-10)
+ [[SageMaker.11] SageMaker data quality job definitions should have network isolation enabled](sagemaker-controls.md#sagemaker-11)
+ [[SageMaker.12] SageMaker model bias job definitions should have network isolation enabled](sagemaker-controls.md#sagemaker-12)
+ [[SageMaker.13] SageMaker model quality job definitions should have inter-container traffic encryption enabled](sagemaker-controls.md#sagemaker-13)
+ [[SageMaker.14] SageMaker monitoring schedules should have network isolation enabled](sagemaker-controls.md#sagemaker-14)
+ [[SageMaker.15] SageMaker model bias job definitions should have inter-container traffic encryption enabled](sagemaker-controls.md#sagemaker-15)
+ [[SageMaker.16] SageMaker models should use private registry in VPC for primary containers](sagemaker-controls.md#sagemaker-16)
+ [[SageMaker.17] SageMaker feature group offline stores should be encrypted with AWS KMS keys](sagemaker-controls.md#sagemaker-17)
+ [[SageMaker.18] SageMaker feature group online stores with standard storage should be encrypted with AWS KMS keys](sagemaker-controls.md#sagemaker-18)
+ [[SageMaker.19] SageMaker models should use private registry in VPC for multi-container inference pipelines](sagemaker-controls.md#sagemaker-19)
+ [[SageMaker.20] SageMaker model explainability job definitions should have network isolation enabled](sagemaker-controls.md#sagemaker-20)
+ [[SageMaker.21] SageMaker notebook instances should be encrypted with customer managed AWS KMS keys](sagemaker-controls.md#sagemaker-21)
+ [[SageMaker.22] SageMaker monitoring schedules should have inter-container traffic encryption enabled](sagemaker-controls.md#sagemaker-22)
+ [[SageMaker.23] SageMaker inference experiments should have instance storage volume encrypted with customer managed AWS KMS keys](sagemaker-controls.md#sagemaker-23)
+ [[SageMaker.24] SageMaker inference experiments should have data storage encrypted with customer managed AWS KMS keys](sagemaker-controls.md#sagemaker-24)
+ [[SageMaker.25] SageMaker model quality job definitions should have network isolation enabled](sagemaker-controls.md#sagemaker-25)