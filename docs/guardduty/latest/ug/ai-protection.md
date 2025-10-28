# Protecting AI workloads with GuardDuty

Amazon GuardDuty [foundational threat
detection](guardduty_data-sources.md "guardduty_data-sources.md") and [Lambda Protection](lambda-protection.md "lambda-protection.md") helps you to better
secure and detect threats to AI workloads built on AWS.

The foundational GuardDuty threat detection monitors AWS CloudTrail management events to detect
suspicious and malicious activity in generative AI workloads created by using AWS
services, including [Amazon Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md") and [Amazon SageMaker AI](../../../sagemaker.md "../../../sagemaker.md"). For example, GuardDuty can identify
activities such as:

- Unusual removal of Amazon Bedrock security guardrails
- Change of model training data source that can potentially lead to data poisoning
  attack
- Suspicious Amazon Bedrock model invocation
- Unusual notebook instance or training job creation in SageMaker AI
- Exfiltrated Amazon Elastic Compute Cloud credentials that may have been used to call APIs in
  Amazon Bedrock, Amazon SageMaker AI, or self-managed AI workloads on EC2 instances, EKS clusters, or
  ECS tasks.
  GuardDuty Lambda Protection can help detect potential threats related Amazon Bedrock agents. This may include
  suspicious network activity such as cryptomining, and communicating with malicious command
  and control servers that can be caused by supply chain attack or complex prompting.

The following video shows how the associated findings would
look.
