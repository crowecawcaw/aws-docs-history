

# Model lifecycle
<a name="model-lifecycle"></a>

This page describes the model lifecycle policy for models launched on Amazon Bedrock on or after September 7, 2026. For models launched before this date, see [Model lifecycle (Legacy)](model-lifecycle-legacy.md).

Every model on Amazon Bedrock has one of three states: **Active**, **Legacy**, or **End-of-Life (EOL)**. You can see the status of a model in the console, and when you make a [GetFoundationModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetFoundationModel.html) or [ListFoundationModels](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListFoundationModels.html) call, the state is shown in the `modelLifecycle` field in the response.

Before using a model, review the [model card](model-cards.md) for its EOL policy, including how much notice you will receive before the model is deprecated. Every model card shows two things:

1. An **EOL no sooner than** date: the model will not reach EOL before this date.

1. The **Legacy period**: the notice period before EOL. There are two Legacy periods: 6 months and 45 days. Most models have a 6-month Legacy period.

When a model enters its Legacy period, the EOL date of the model is added to the model card.

**Note**  
Model lifecycle dates are specific to Amazon Bedrock and may differ from dates published by model providers (such as Anthropic or Cohere). For Amazon Bedrock usage, only the dates on the model card apply.

## Active
<a name="active-versions"></a>

**Active** — The model provider is actively working on this version. In most cases, model providers sunset a model after newer versions become available. For a list of currently active models and their supported regions, see [Regional availability](models-region-compatibility.md). For model specific details, see [Model cards](model-cards.md).

## Legacy and end-of-life (EOL) models
<a name="versions-for-legacy-and-eol"></a>

**Legacy** — The model is scheduled for retirement. At the beginning of the Legacy period, we notify you of the EOL date for the model. You can keep using the model, but you should migrate to an Active model before the EOL date. Once the Legacy period begins, new customers can't adopt the model, and existing customers may lose access after 15 days of inactivity. You can't create a new [Provisioned Throughput](prov-throughput.md) for models in the Legacy state.

**EOL** — After the EOL date, the model is removed from all AWS Regions and requests made to it will fail, unless there is a private arrangement between you and the provider for continued access. Migrate to an Active model before the EOL date; migration will not happen automatically.

**Customized Models and Lifecycle Behavior**

When a foundation model transitions to the Legacy state, customization capabilities become restricted. If you previously fine-tuned or customized the model before it entered the Legacy state, you may:
+ Create a new custom model deployment for on-demand inference.
+ Continue using any existing on-demand deployments or any existing Provisioned Throughput (PT) endpoints, provided they were created before the model entered Legacy state.

However, after the model is in Legacy state, you cannot create new fine-tuning jobs on that model. You cannot create new Provisioned Throughput (PT) endpoints. New customers cannot start using the Legacy model and existing customers may lose access after 15 days of inactivity.

Because Legacy models are scheduled for retirement, customers are strongly encouraged to begin transitioning workloads and customized deployments to an Active model as soon as the Legacy announcement is made, and complete migration before the model's End-of-Life (EOL) date.