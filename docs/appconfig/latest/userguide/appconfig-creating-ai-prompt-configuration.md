

# Creating an AI prompt configuration profile in AWS AppConfig

An *AI prompt configuration profile* lets you manage an AI prompt as a first-class, reusable artifact in AWS AppConfig. Prompts are versioned and iterated independently of any AI model invocation configuration or freeform configuration.

In generative AI applications, prompts tend to change far more frequently than model selection or inference parameters. By storing prompts as their own configuration type, you can iterate on prompt content without redeploying your model configuration. AWS AppConfig deployment strategies let you roll out prompt changes gradually — for example, to 10% of your workload, then 20%, then 30% — so you can measure the impact of each change on operations, customer experience, and token usage before it reaches all traffic. If an alarm in Amazon CloudWatch, Datadog, New Relic, or another observability solution detects an unexpected change, AWS AppConfig automatically rolls back to the previous prompt version. You can also reuse a single prompt across multiple AI model configurations.

AI prompt configuration profiles use the `AWS.AppConfig.AIPrompt` configuration type. Prompt content is stored as plain text in the AWS AppConfig hosted configuration store. You can use any text format for your prompt content, including Markdown, plain text, or structured text with your own conventions.

**Note**  
With the AI model invocation configuration profile type (`AWS.AppConfig.AIModelInvocation`), you can include a system prompt inline by adding a message with the `system` role to the `messages` array, or by using `customParameters`. Use an AI prompt configuration profile when you need to manage prompts on a separate deployment cadence from your model configuration, or when you want to reuse the same prompt across multiple AI model invocation configurations. For more information about AI model invocation configuration profiles, see [Creating an AI model invocation configuration profile in AWS AppConfig](appconfig-creating-ai-model-configuration.md).

## Benefits of AI prompt configuration profiles
<a name="appconfig-ai-prompt-benefits"></a>

AI prompt configuration profiles provide the following benefits:
+ Version and deploy prompt changes without modifying your model configuration or application code.
+ Deploy prompt changes more often than model or infrastructure changes, because prompt updates carry lower risk than changes to model selection or inference parameters.
+ Share a single prompt across multiple AI model invocation configurations or applications. Update the prompt in one place, and all consumers receive the new version on the next deployment.
+ Roll out prompt changes to a percentage of traffic at a time by using AWS AppConfig deployment strategies. Configure alarms in Amazon CloudWatch, Datadog, New Relic, or other observability solutions to monitor operational metrics, customer experience, and token usage, and automatically roll back if unexpected changes are detected.

## Example prompt content
<a name="appconfig-ai-prompt-example"></a>

The following example shows prompt content for an AWS support agent. The content uses Markdown formatting, but you can use any text format.

```markdown
# AWS Support Agent

You are a helpful AWS support agent. Follow these guidelines:

- Always provide accurate, up-to-date information about AWS services
- Include relevant CLI commands and code examples when helpful
- If you're unsure about something, say so rather than guessing
- Reference official AWS documentation when appropriate

## Response Format

Use clear, structured responses with headings and bullet points when appropriate.

**Important:** Never share or expose customer account details, credentials,
or internal system information.
```

## Creating an AI prompt configuration profile (console)
<a name="appconfig-creating-ai-prompt-console"></a>

Create an AI prompt configuration profile to store a prompt in AWS AppConfig so you can update it without redeploying your application or your model configuration. Before you begin, create an AWS AppConfig application to save the profile under. For more information about creating an application, see [Creating a namespace for your application in AWS AppConfig](appconfig-creating-namespace.md).

Creating the profile in the console has two parts: you set up the profile, and then you enter the prompt content.

**To set up a new AI prompt configuration profile**

1. Open the AWS Management Console and search for AWS AppConfig.

1. On the AWS AppConfig console dashboard, choose **Create**.

1. Choose **AI prompt configuration profile**.

1. For **Save under application resource**, choose the application that the configuration profile belongs to.

1. In the **Configuration profile** section, for **Configuration profile name**, enter a name.

1. (Optional) Expand **Description** and enter a description.

1. (Optional) Expand **Additional options** and complete the following, as necessary.

   1. In the **Encryption** list, choose an AWS Key Management Service (AWS KMS) key. This customer managed key encrypts new configuration data versions in the AWS AppConfig hosted configuration store.

   1. In the **Tags** section, choose **Add new tag**, and then specify a key and optional value.

**To enter the prompt content and save the profile**

1. Choose **Next**.

1. In the prompt editor, enter your prompt content. You can use any text format, including Markdown or plain text.

1. Choose **Next**.

1. On the **Review and save** page, review the details, and then choose **Save and continue to deploy**.

AWS AppConfig creates the configuration profile and its first hosted configuration version. To make the prompt available to your application, deploy it. For more information about deploying, see [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).

## Creating an AI prompt configuration profile (command line)
<a name="appconfig-creating-ai-prompt-commandline"></a>

Use the to create an AI prompt configuration profile and upload your prompt content. Before you begin, install and configure the , and create an AWS AppConfig application to save the profile under.

**To create an AI prompt configuration profile by using the**

1. Run the following command to create an AI prompt configuration profile.

   ```bash
   aws appconfig create-configuration-profile \
     --application-id {{application-id}} \
     --name {{profile-name}} \
     --description "{{profile-description}}" \
     --location-uri hosted \
     --type AWS.AppConfig.AIPrompt
   ```

   Replace the following values:
   + {{application-id}} – The ID of the AWS AppConfig application to save the profile under.
   + {{profile-name}} – A name for the configuration profile.
   + {{profile-description}} – (Optional) A description of the configuration profile.

   The response includes an `Id` value. You use this value as the configuration profile ID in the next step.

1. Save your prompt to a text file (for example, `my-prompt.txt`), and then run the following command to create a hosted configuration version from it.

   ```bash
   aws appconfig create-hosted-configuration-version \
     --application-id {{application-id}} \
     --configuration-profile-id {{configuration-profile-id}} \
     --content-type "text/plain" \
     --content file://my-prompt.txt \
     output.json
   ```

   Replace {{configuration-profile-id}} with the `Id` value from the previous step. If the command succeeds, it writes the new version's metadata to `output.json`.

1. Deploy the configuration. For more information about deploying, see [Deploying feature flags and configuration data in AWS AppConfig](deploying-feature-flags.md).

## Retrieving AI prompt configuration data
<a name="appconfig-ai-prompt-retrieving"></a>

Your application retrieves the deployed prompt by calling the local endpoint exposed by AWS AppConfig Agent. The agent caches the deployed configuration and returns the prompt content as plain text.

The following example shows how to retrieve a deployed AI prompt configuration from AWS AppConfig Agent.

```javascript
// Retrieve the deployed prompt from AWS AppConfig Agent
const promptResponse = await fetch(
  "http://localhost:2772/applications/myapp/environments/prod/configurations/support-agent-prompt"
);
const promptText = await promptResponse.text();

// Use the prompt as the system instruction in your model call
const body = JSON.stringify({
  system: promptText,
  messages: [{ role: "user", content: userInput }],
});
```

You can also retrieve the prompt alongside an AI model invocation configuration to combine independently managed prompts with model settings. The following example retrieves both configurations and merges them at runtime.

```javascript
// Retrieve the AI model invocation configuration and prompt separately
const [modelRes, promptRes] = await Promise.all([
  fetch("http://localhost:2772/applications/myapp/environments/prod/configurations/support-agent"),
  fetch("http://localhost:2772/applications/myapp/environments/prod/configurations/support-agent-prompt"),
]);
const modelCfg = await modelRes.json();
const promptText = await promptRes.text();

// Combine: use the model config for model settings, the prompt config for the system prompt
await client.send(new ConverseCommand({
  modelId: modelCfg.model,
  system: [{ text: promptText }],
  messages: [
    ...modelCfg.messages
      .filter((m) => m.role !== "system")
      .map((m) => ({ role: m.role, content: [{ text: m.content }] })),
    { role: "user", content: [{ text: userInput }] },
  ],
  inferenceConfig: modelCfg.inferenceParameters,
  additionalModelRequestFields: modelCfg.customParameters,
}));
```

For more information about retrieving configuration data, see [Retrieving feature flags and configuration data in AWS AppConfig](retrieving-feature-flags.md).