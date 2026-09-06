

# GuardDuty AI Protection finding types
<a name="findings-ai-protection"></a>

When you enable AI Protection, GuardDuty analyzes AWS CloudTrail management events and data events from Amazon Bedrock and Amazon SageMaker AI. GuardDuty uses this data to detect potentially suspicious activity that targets your AI workloads. When GuardDuty detects a potential threat, it generates one of the following finding types. The `Resource type` for these findings is `AccessKey`, and the finding identifies the IAM identity that invoked the model.

Each finding also includes details about the affected AI resources in the `resource` object of the finding. The [Impact:IAMUser/AnomalousModelInvocation](#ai-protection-anomalousmodelinvocation) and [Impact:IAMUser/CostHarvesting](#ai-protection-costharvesting) findings include a `resource.modelDetails` list that identifies the invoked Amazon Bedrock or Amazon SageMaker AI models. The [Impact:IAMUser/PromptInjection.Direct](#ai-protection-promptinjection-direct) finding includes a `resource.bedrockGuardrailDetails` object that describes the Amazon Bedrock Guardrail that intervened. You can view these details in the GuardDuty console or in the finding JSON.

The [Impact:IAMUser/AnomalousModelInvocation](#ai-protection-anomalousmodelinvocation) and [Impact:IAMUser/CostHarvesting](#ai-protection-costharvesting) finding types apply to both Amazon Bedrock and Amazon SageMaker AI model invocations. The [Impact:IAMUser/PromptInjection.Direct](#ai-protection-promptinjection-direct) finding type applies to Amazon Bedrock workloads that use Amazon Bedrock Guardrails.

**Topics**
+ [Impact:IAMUser/AnomalousModelInvocation](#ai-protection-anomalousmodelinvocation)
+ [Impact:IAMUser/CostHarvesting](#ai-protection-costharvesting)
+ [Impact:IAMUser/PromptInjection.Direct](#ai-protection-promptinjection-direct)

## Impact:IAMUser/AnomalousModelInvocation
<a name="ai-protection-anomalousmodelinvocation"></a>

### An IAM identity invoked an Amazon Bedrock or Amazon SageMaker AI model in a way that deviates from the established baseline for the identity or account.
<a name="ai-protection-anomalousmodelinvocation_description"></a>

**Default severity: Low**
+ **Feature: **AI Protection

This finding informs you that an IAM identity invoked an Amazon Bedrock or Amazon SageMaker AI model in a way that deviates from the historical activity of the identity or account. This activity might indicate that a threat actor is using compromised credentials to access foundation models in your account. For example, the actor might probe a model, craft adversarial inputs, or run automated requests.

GuardDuty establishes a baseline of normal model invocation activity for each IAM identity and AWS account that invokes Amazon Bedrock or Amazon SageMaker AI. GuardDuty profiles features of the invocation activity, including the following:
+ The model invocation API that the identity called
+ The model that the identity invoked
+ The source IP address and its associated Autonomous System Number (ASN) organization
+ The user agent that made the request

When GuardDuty observes activity that deviates significantly from this baseline, it generates this finding. Examples include invocations from a previously unseen IP address, a previously unseen user agent, or a model that the identity has never invoked. The finding includes a `resource.modelDetails` list identifying the models involved in the suspicious activity. Each entry contains a `modelId` representing an Amazon Bedrock foundation model, inference profile, provisioned, custom, or imported model ARN, Amazon Bedrock Marketplace endpoint, prompt resource, or Amazon SageMaker AI endpoint name.

This finding maps to the [MITRE ATLAS technique AML.T0040 - AI Model Inference API Access](https://atlas.mitre.org/techniques/AML.T0040) on the MITRE ATLAS website.

**Remediation recommendations:**

If this activity is unexpected, your credentials may be compromised. For more information, see [Remediating potentially compromised AWS credentials](compromised-creds.md).

To reduce the risk of unauthorized model invocations, restrict which identities can invoke models. Scope access to the following model invocation APIs to only the principals and models that require them:
+ `bedrock:InvokeModel`
+ `bedrock:InvokeModelWithResponseStream`
+ `bedrock:Converse`
+ `bedrock:ConverseStream`
+ `bedrock-mantle:CreateInference`
+ `sagemaker:InvokeEndpoint`
+ `sagemaker:InvokeEndpointAsync`
+ `sagemaker:InvokeEndpointWithResponseStream`

To deny model inference across your organization where it isn't needed, you can use a service control policy (SCP). For more information, see [Identity-based policy examples for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html) in the *Amazon Bedrock User Guide* and [Amazon SageMaker AI identity-based policy examples](https://docs.aws.amazon.com/sagemaker/latest/dg/security_iam_id-based-policy-examples.html) in the *Amazon SageMaker AI Developer Guide*.

## Impact:IAMUser/CostHarvesting
<a name="ai-protection-costharvesting"></a>

### An IAM identity invoked an Amazon Bedrock or Amazon SageMaker AI model with anomalous token volumes that might indicate a cost harvesting attack.
<a name="ai-protection-costharvesting_description"></a>

**Default severity: Low**
+ **Feature: **AI Protection

This finding informs you that an IAM identity invoked an Amazon Bedrock or Amazon SageMaker AI model with input or output token volumes that deviate significantly from the baseline for the identity or account. In a cost harvesting attack, a threat actor sends computationally expensive inputs to a model to inflate the operating costs of the AI workload, without necessarily exfiltrating data. These inputs might include excessively long or deliberately malformed prompts.

GuardDuty establishes a baseline of average input token volume and average output token volume for each IAM identity and account that invokes Amazon Bedrock or Amazon SageMaker AI models. When GuardDuty observes invocations with token counts that exceed this baseline, and correlates the volume anomaly with other unusual signals, GuardDuty generates this finding. The finding reports the anomalous activity in the `service.detection` object, including the observed invocation and token volumes that deviated from the baseline. It also includes a `resource.modelDetails` list identifying the targeted models. Each entry contains a `modelId` representing an Amazon Bedrock foundation model, inference profile, provisioned, custom, or imported model ARN, Amazon Bedrock Marketplace endpoint, prompt resource, or Amazon SageMaker AI endpoint name.

This finding maps to the [MITRE ATLAS technique AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) on the MITRE ATLAS website.

**Remediation recommendations:**

If this activity is unexpected for the associated identity, the credentials might have been compromised and used to drive up the cost of your AI workloads. For more information, see [Remediating potentially compromised AWS credentials](compromised-creds.md). Review the model invocations associated with the identity, and restrict access to the affected models by scoping access to the following model invocation APIs to only the principals that require them:
+ `bedrock:InvokeModel`
+ `bedrock:InvokeModelWithResponseStream`
+ `bedrock:Converse`
+ `bedrock:ConverseStream`
+ `bedrock-mantle:CreateInference`
+ `sagemaker:InvokeEndpoint`
+ `sagemaker:InvokeEndpointAsync`
+ `sagemaker:InvokeEndpointWithResponseStream`

To detect and contain abnormal spend, you can use [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html), including budget actions that apply a restrictive IAM policy when a budget threshold is exceeded, and [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html). To attribute Amazon Bedrock costs to specific workloads, you can attach cost allocation tags to an [application inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html).

## Impact:IAMUser/PromptInjection.Direct
<a name="ai-protection-promptinjection-direct"></a>

### An Amazon Bedrock Guardrail detected a direct prompt injection attempt in an invocation made by an IAM identity.
<a name="ai-protection-promptinjection-direct_description"></a>

**Default severity: Low**
+ **Feature: **AI Protection

This finding informs you that an Amazon Bedrock Guardrail configured for an Amazon Bedrock workload in your account detected a direct prompt injection attempt. In a direct prompt injection attack, a threat actor crafts a malicious prompt as input to a foundation model. The prompt makes the model ignore its original instructions and follow the attacker's instructions instead. Prompt injection can give an attacker initial access to carry out additional steps against an AI application, such as exfiltrating data, calling unauthorized tools, or bypassing safety controls.

GuardDuty generates this finding when an Amazon Bedrock Guardrail intervenes on an invocation because it detected a prompt attack with high confidence. To enable GuardDuty to detect direct prompt injection, configure an Amazon Bedrock Guardrail with a [prompt attack content filter](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html). To ensure that the guardrail evaluates invocations across your environment, enforce it broadly instead of relying on individual applications to attach it to each request. You can enforce a guardrail for all Amazon Bedrock model invocations in an account, or across your organization by using Amazon Bedrock policies in AWS Organizations. For more information, see [Apply cross-account safeguards with Amazon Bedrock Guardrails enforcements](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-enforcements.html) in the *Amazon Bedrock User Guide*. When a guardrail evaluates an invocation, Amazon Bedrock records the evaluation in AWS CloudTrail data events, which GuardDuty analyzes to generate this finding.

The finding includes a `resource.bedrockGuardrailDetails` object that describes the guardrail that intervened. The following table describes the fields in this object.


| Field | Description | 
| --- | --- | 
| `guardrails` | A list of the guardrails that evaluated the invocation. Each entry includes the Amazon Resource Name (`arn`) and the `version` of the guardrail. Multiple guardrails can appear when both an account-enforced or organization-enforced guardrail and a request-level guardrail evaluate the same invocation. | 
| `guardrailAction` | The action that the guardrail took. GuardDuty generates this finding when the value is `GUARDRAIL_INTERVENED`. | 
| `guardrailSource` | The content that the guardrail evaluated. `INPUT` indicates a prompt sent to the model, and `OUTPUT` indicates a response from the model. | 
| `contentPolicyFilters` | A list of the content policy filters that the guardrail applied. For this finding type, an entry has a `type` of `PROMPT_ATTACK` and a `confidence` of `HIGH`. The `action` is `BLOCKED` if the guardrail blocked the content, or `NONE` if the guardrail detected the prompt attack but was configured only to report it. | 

This finding maps to the [MITRE ATLAS technique AML.T0051 - LLM Prompt Injection](https://atlas.mitre.org/techniques/AML.T0051) on the MITRE ATLAS website.

**Remediation recommendations:**

Review the prompt that triggered the guardrail intervention and the IAM identity that submitted the prompt. If the activity is unexpected for the associated identity, the credentials might have been compromised. For more information, see [Remediating potentially compromised AWS credentials](compromised-creds.md). If the guardrail detected but did not block the prompt attack, consider setting the prompt attack content filter's action to **Block** rather than **Detect** so that the guardrail blocks the content. For more information, see [Options for handling harmful content detected by Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-harmful-content-handling-options.html) in the *Amazon Bedrock User Guide*. You can also restrict access to the Amazon Bedrock invocation APIs for the affected identity.