

# GuardDuty AI Protection
<a name="ai-protection"></a>

GuardDuty AI Protection extends Amazon GuardDuty threat detection to AI workloads built on AWS. When you enable AI Protection, GuardDuty analyzes AWS CloudTrail data events from Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker AI, along with AWS CloudTrail management events. GuardDuty uses this data to detect potentially suspicious activity that targets foundation models and the applications that invoke them. When GuardDuty identifies a potential threat, it generates one or more [AI Protection finding types](findings-ai-protection.md).

When you enable AI Protection, GuardDuty can detect the following types of threats:
+ Anomalous invocations of Amazon Bedrock or Amazon SageMaker AI models that deviate from the established baseline for an identity or account, such as invocations from an unusual IP address, an unusual API, or an unusual model.
+ Cost harvesting attacks, in which a threat actor sends computationally expensive inputs to an Amazon Bedrock or Amazon SageMaker AI model to inflate the token consumption and operating costs of the account.
+ Direct prompt injection attempts, in which a threat actor crafts a malicious prompt to make a foundation model ignore its original instructions. This detection requires Amazon Bedrock Guardrails and applies only to Amazon Bedrock workloads.

**Note**  
The finding types that GuardDuty can generate in an AWS Region depend on which AI services are available in that Region:  
The [Impact:IAMUser/AnomalousModelInvocation](findings-ai-protection.md#ai-protection-anomalousmodelinvocation) and [Impact:IAMUser/CostHarvesting](findings-ai-protection.md#ai-protection-costharvesting) finding types require Amazon Bedrock or Amazon SageMaker AI. In Regions where Amazon Bedrock isn't available, GuardDuty generates these finding types from Amazon SageMaker AI model invocations only.
The [Impact:IAMUser/PromptInjection.Direct](findings-ai-protection.md#ai-protection-promptinjection-direct) finding type requires Amazon Bedrock Guardrails. It isn't available in Regions where Amazon Bedrock Guardrails isn't supported.
For the list of Regions where each finding type is supported, see [Region-specific feature availability](guardduty_regions.md#gd-regional-feature-availability).

**Tip**  
To get the most security value from AI Protection, enforce Amazon Bedrock Guardrails for prompt attacks across all accounts in your AWS organization. Use [AWS Organizations Amazon Bedrock policies](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html) to manage these guardrail settings centrally. This enables uniform protection across all accounts with centralized control and management. When a prompt attack guardrail is enforced, GuardDuty creates prompt injection findings. For more information, see [Impact:IAMUser/PromptInjection.Direct](findings-ai-protection.md#ai-protection-promptinjection-direct).

To detect threats to your AI workloads, you must enable AI Protection in your GuardDuty account. For information about enabling AI Protection, see [Enabling AI Protection in multiple-account environments](ai-protection-enable-multiple-accounts.md) for multiple-account environments or [Enabling AI Protection for a standalone account](ai-protection-enable-standalone-account.md).

**Topics**
+ [How AI Protection works](#ai-protection-how-it-works)
+ [Pricing for AI Protection](#ai-protection-pricing)
+ [Additional threat detections for AI workloads](#ai-protection-foundational)
+ [Enabling AI Protection in multiple-account environments](ai-protection-enable-multiple-accounts.md)
+ [Enabling AI Protection for a standalone account](ai-protection-enable-standalone-account.md)

## How AI Protection works
<a name="ai-protection-how-it-works"></a>

When you enable AI Protection for an account or across your organization, GuardDuty automatically begins collecting AWS CloudTrail data events from the AI services in the monitored accounts. You don't need to create a trail, enable data event logging, or make any changes to your AI applications.

To collect the data events, GuardDuty creates an AWS CloudTrail [service-linked channel](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-service-linked-channels.html) in each monitored account. The service-linked channel streams AWS CloudTrail data events for Amazon Bedrock, Amazon Bedrock AgentCore, and Amazon SageMaker AI, and related AI resources to GuardDuty for analysis. Because GuardDuty creates and manages this channel:
+ GuardDuty configures the channel's data event settings, and the account owner can't modify them. This means threat detection doesn't depend on the account owner configuring or maintaining a trail.
+ Each monitored account can confirm that the channel is active in the CloudTrail console (under **Settings**, **Service-linked channels**) or by calling the AWS CloudTrail [ListChannels](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ListChannels.html) API operation.

GuardDuty uses two detection methods to generate AI Protection findings, depending on the finding type:
+ For the [Impact:IAMUser/AnomalousModelInvocation](findings-ai-protection.md#ai-protection-anomalousmodelinvocation) and [Impact:IAMUser/CostHarvesting](findings-ai-protection.md#ai-protection-costharvesting) finding types, GuardDuty uses an anomaly detection machine learning (ML) model to analyze the collected events and establish a baseline of normal model invocation activity for each IAM identity and AWS account. GuardDuty generates a finding when it detects activity that deviates significantly from this baseline.
+ For the [Impact:IAMUser/PromptInjection.Direct](findings-ai-protection.md#ai-protection-promptinjection-direct) finding type, GuardDuty generates a finding when Amazon Bedrock Guardrails evaluates a prompt and detects a prompt attack, based on the resulting AWS CloudTrail data event.

For more information about AWS CloudTrail data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

## Pricing for AI Protection
<a name="ai-protection-pricing"></a>

When you enable GuardDuty AI Protection, GuardDuty charges for the volume of AWS CloudTrail data events that it analyzes, measured in GB. GuardDuty creates the service-linked channel at no additional CloudTrail charge to you. The cost of collecting these data events is included in your AI Protection usage cost. You also continue to incur standard usage costs for GuardDuty and any other enabled protection plans. For current pricing and examples, see [Amazon GuardDuty pricing](https://aws.amazon.com/guardduty/pricing/).

## Additional threat detections for AI workloads
<a name="ai-protection-foundational"></a>

In addition to the AI Protection plan, the Amazon GuardDuty Foundational and [Lambda Protection](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html) plans offer detections to help you secure and detect threats to AI workloads built on AWS.

The GuardDuty Foundational plan monitors AWS CloudTrail management events to detect suspicious and malicious activity in AI workloads created by using AWS services, including [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/). For example, GuardDuty can identify activities such as:
+ Unusual removal of Amazon Bedrock security guardrails
+ A change to a model training data source that can potentially lead to a data poisoning attack
+ Disabled logging for Amazon Bedrock model invocations that might indicate attempts to evade detection
+ Unusual notebook instance or training job creation in Amazon SageMaker AI
+ Exfiltrated Amazon Elastic Compute Cloud credentials that might have been used to call APIs in Amazon Bedrock, Amazon SageMaker AI, or self-managed AI workloads on Amazon EC2 instances, Amazon EKS clusters, or Amazon ECS tasks.

GuardDuty Lambda Protection can help detect potential threats related to Amazon Bedrock agents. This might include suspicious network activity such as cryptomining, and communication with malicious command and control servers. These threats can be caused by a supply chain attack or complex prompting.