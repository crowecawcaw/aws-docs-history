

# Creating an AI model invocation configuration profile in AWS AppConfig

An *AI model invocation configuration profile* is a strongly typed configuration that defines the settings for a call to an AI model. This includes the model identifier, inference parameters, messages (such as system prompts and example conversation turns), and provider-specific custom parameters. By storing these settings as configuration instead of hardcoding them in application code, you can gradually tune inference parameters against an existing model, migrate to different models or model versions incrementally, and iterate on prompts — all through configuration deployments rather than code deployments. You can also configure Amazon CloudWatch alarms or integrate with third-party observability solutions such as Datadog or New Relic to automatically roll back model configuration changes when unexpected changes in operational metrics, application metrics, or token usage are detected.

AWS AppConfig stores AI model invocation configurations in the AWS AppConfig hosted configuration store using the `AWS.AppConfig.AIModelInvocation` type. AWS AppConfig validates configuration data against the AI model invocation schema at creation and deployment time. If validation fails, AWS AppConfig rejects the operation.

AI model invocation configuration profiles use the same AWS AppConfig deployment, retrieval, and rollback capabilities available to feature flag and freeform configuration profiles. Your application retrieves the deployed configuration from AWS AppConfig Agent and maps the canonical fields to the wire format required by your AI provider.

**Note**  
To manage prompts independently of the model configuration, use an AWS AppConfig *AI prompt* configuration profile. Prompts change more frequently than model parameters. Separating them lets you iterate on a prompt without redeploying the model configuration. For more information about AI prompt configuration profiles, see [Creating an AI prompt configuration profile in AWS AppConfig](appconfig-creating-ai-prompt-configuration.md).

## AI model invocation schema reference
<a name="appconfig-ai-model-schema"></a>

The AI model invocation schema is strongly typed for a select set of fields that are common across AI providers. A field is included in the typed schema only when it meets three criteria:

1. The field is part of the model call.

1. The field is common across AI providers.

1. The field is validatable.

Any parameter that does not meet all three criteria can be passed through the `customParameters` field.

The following table describes the top-level fields in the AI model invocation schema.


**AI model invocation schema fields**  

| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| schemaVersion | String | Yes | Schema version of the AI model invocation type. Allows the schema to evolve without requiring a new configuration profile type. | 
| model | String | Yes | Model identifier to invoke. For example, anthropic.claude-sonnet-5. | 
| inferenceParameters | Object | No | Inference parameters that control model output. See [Inference parameters](#appconfig-ai-model-inference-parameters). | 
| customParameters | Object | No | Freeform JSON passthrough for provider-specific parameters not covered by the typed schema. See [Custom parameters](#appconfig-ai-model-custom-parameters). | 
| messages | Array | No | Messages that prime the model, such as a system prompt and example conversation turns (few-shot). See [Messages](#appconfig-ai-model-messages). | 

### Inference parameters
<a name="appconfig-ai-model-inference-parameters"></a>

The typed inference parameters mirror the `InferenceConfiguration` used by the Amazon Bedrock Converse API. These parameters represent the cross-provider common set. Provider-specific parameters such as `topK` or reasoning effort settings should be placed in `customParameters`.


**Inference parameters**  

| Field | Type | Constraints | Description | 
| --- | --- | --- | --- | 
| temperature | Float | Minimum value of 0 | Controls sampling randomness. A lower value makes the model more likely to choose higher-probability tokens. A higher value increases diversity in the generated response. | 
| topP | Float | Minimum value of 0. Maximum value of 1. | Nucleus sampling. The model considers only the tokens that make up the top topP percentage of the probability distribution. | 
| maxTokens | Integer | Minimum value of 1 | Maximum number of tokens to generate in the response. | 
| stopSequences | Array of strings | Each string must be non-empty | Sequences of characters that cause the model to stop generating the response. | 

### Messages
<a name="appconfig-ai-model-messages"></a>

The `messages` array contains messages that you author to prime the model. To provide a system prompt, add a message with the `system` role. To provide few-shot examples, add a sample question and its ideal answer as `user` and `assistant` messages. Your application appends the user's actual message at runtime. The user's real-time input is not stored in the configuration.

Each message object contains the following fields:
+ `role` – (Required) The speaker of the message. Common values include `system`, `user`, and `assistant`. This field is an open string to support any provider's role values.
+ `content` – (Required) The message content.

### Custom parameters
<a name="appconfig-ai-model-custom-parameters"></a>

The `customParameters` field is a freeform JSON object for provider-specific parameters not covered by the typed schema. Use this field for capabilities such as extended thinking, reasoning effort, output format configuration, or any other parameter unique to your AI provider.

AWS AppConfig validates that `customParameters` is well-formed JSON, but does not validate its contents. This design allows you to use any provider-specific parameter without waiting for a schema update.

The following example shows `customParameters` used to configure Anthropic's extended thinking and output effort settings:

```json
"customParameters": {
    "thinking": { "type": "enabled", "budget_tokens": 4000 },
    "output_config": { "effort": "high" }
}
```

## Example AI model invocation configuration
<a name="appconfig-ai-model-example"></a>

The following example defines a support agent using a Claude model on Amazon Bedrock with conservative inference parameters, a system prompt, and example conversation turns.

```json
{
  "schemaVersion": "1",
  "model": "anthropic.claude-sonnet-5",
  "inferenceParameters": {
    "temperature": 0.7,
    "topP": 0.9,
    "maxTokens": 4000,
    "stopSequences": []
  },
  "customParameters": {
    "thinking": { "type": "enabled", "budget_tokens": 4000 },
    "output_config": { "effort": "high" }
  },
  "messages": [
    { "role": "system", "content": "You are a helpful AWS support agent." },
    { "role": "user", "content": "How do I create an S3 bucket?" },
    { "role": "assistant", "content": "Run: aws s3 mb s3://your-bucket-name" }
  ]
}
```

## Creating an AI model invocation configuration profile (console)
<a name="appconfig-creating-ai-model-console"></a>

Create an AI model invocation configuration profile to store your model settings in AWS AppConfig so you can change them without redeploying your application. Before you begin, create an AWS AppConfig application to save the profile under. For more information about creating an application, see [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md).

Creating the profile in the console has two parts: you name the profile, and then you define the model settings.

**To name a new AI model invocation configuration profile**

1. Open the AWS Management Console and search for AWS AppConfig.

1. On the AWS AppConfig console dashboard, choose **Create**.

1. Choose **AI model invocation configuration profile**.

1. For **Save under application resource**, choose the application that the configuration profile belongs to.

1. For **Configuration profile name**, enter a name for the profile.

1. (Optional) Expand **Description** and enter a description.

**To define the model settings and save the profile**

1. In the **AI model invocation definition** section, for **Model**, enter the model identifier (for example, `anthropic.claude-sonnet-5`).

1. (Optional) For **Inference parameters**, enter values for temperature, top P, maximum tokens, and stop sequences.

1. (Optional) In the **Messages** section, add a system prompt or example conversation turns by specifying a **Role** and **Content** for each message.

1. (Optional) In the **Custom parameters** section, enter any provider-specific parameters as JSON.

1. Choose **Next**.

1. On the **Review and save** page, review the configuration, and then choose **Save and continue to deploy**.

AWS AppConfig creates the configuration profile and its first hosted configuration version. To make the configuration available to your application, deploy it. For more information about deploying, see [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).

## Creating an AI model invocation configuration profile (command line)
<a name="appconfig-creating-ai-model-commandline"></a>

Use the to create an AI model invocation configuration profile and upload your configuration data. Before you begin, install and configure the , and create an AWS AppConfig application to save the profile under.

**To create an AI model invocation configuration profile by using the**

1. Run the following command to create the configuration profile.

   ```bash
   aws appconfig create-configuration-profile \
       --application-id {{application-id}} \
       --name {{profile-name}} \
       --description "{{profile-description}}" \
       --location-uri hosted \
       --type AWS.AppConfig.AIModelInvocation
   ```

   Replace the following values:
   + {{application-id}} – The ID of the AWS AppConfig application to save the profile under.
   + {{profile-name}} – A name for the configuration profile.
   + {{profile-description}} – (Optional) A description of the configuration profile.

   The response includes an `Id` value. You use this value as the configuration profile ID in the next step.

1. Save your configuration JSON to a file (for example, `ai-model-config.json`), and then run the following command to create a hosted configuration version from it.

   ```bash
   aws appconfig create-hosted-configuration-version \
       --application-id {{application-id}} \
       --configuration-profile-id {{configuration-profile-id}} \
       --content-type "application/json" \
       --content file://ai-model-config.json \
       output.json
   ```

   Replace {{configuration-profile-id}} with the `Id` value from the previous step.

   AWS AppConfig validates the configuration data against the AI model invocation schema. If validation succeeds, the command writes the new version's metadata to `output.json`.

1. Deploy the configuration. For more information about deploying, see [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).

## Retrieving an AI model invocation configuration
<a name="appconfig-ai-model-retrieving"></a>

Your application retrieves the deployed AI model invocation configuration from AWS AppConfig Agent the same way it retrieves any other configuration. The agent exposes the configuration at a local HTTP endpoint.

The following example shows how an application fetches the deployed AI model invocation configuration and maps the canonical fields to a Amazon Bedrock `Converse` request.

```javascript
// 1. Fetch the deployed AI model invocation configuration from AppConfig Agent
const res = await fetch(
  "http://localhost:2772/applications/myapp/environments/prod/configurations/support-agent"
);
const cfg = await res.json();

// 2. Map canonical fields to the Bedrock Converse request
const system = cfg.messages
  .filter((m) => m.role === "system")
  .map((m) => ({ text: m.content }));
const messages = cfg.messages
  .filter((m) => m.role !== "system")
  .map((m) => ({ role: m.role, content: [{ text: m.content }] }));

// 3. Invoke the model
await client.send(new ConverseCommand({
  modelId: cfg.model,
  system,
  messages: [...messages, { role: "user", content: [{ text: userInput }] }],
  inferenceConfig: cfg.inferenceParameters,
  additionalModelRequestFields: cfg.customParameters,
}));
```

**Important**  
The mapping from canonical AI model invocation fields to the provider's wire format is performed by your application code. AWS AppConfig stores and delivers the configuration data but does not call the AI provider on your behalf.