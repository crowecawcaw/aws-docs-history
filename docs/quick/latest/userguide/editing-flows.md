

# Editing flows
<a name="editing-flows"></a>

After creating a flow, you can edit and configure it in the Flow editor.

## Accessing the Flow editor
<a name="accessing-flow-editor"></a>

1. Sign in to the Amazon Quick console.

1. In the navigation pane, choose **Flows**.

1. Find the flow you want to edit.

1. Choose the flow tile, or choose the ellipsis (⋮) and select **Open**.

## Configuring step types
<a name="configuring-step-types"></a>

Most steps with a prompt field support @ references to include data from previous steps. See each step's configuration for specific limitations.

### Configuring text input steps
<a name="configuring-input-text"></a>

In Editor mode, add or select a text input step. In the configuration panel, set the following:
+ **Title**: A name for the step.
+ **Placeholder**: Optional text that appears inside the input field when it is empty. This text is not used for the flow run.
+ **Default Value**: Optional. The value provided if the user doesn't enter an input.
+ **Allow override of default value**: Toggle to let users replace the default value at runtime.

### Configuring file upload steps
<a name="configuring-file-upload"></a>

In Editor mode, add or select a file upload step. In the configuration panel, set the following:
+ **Title**: A name for the step.
+ **Default file**: Optional. Upload a document, image, or video to use if the user doesn't provide one. You can upload one file per step.
+ **Allow override of default value**: Toggle to let users replace the default file at runtime.

### Configuring general knowledge steps
<a name="configuring-general-knowledge"></a>

In Editor mode, add or select a general knowledge step. In the configuration panel, set the following:
+ **Output preference**: Choose one:
  + **Fast responses** — Across image, video, and text inputs.
  + **Versatility and performance** — Balanced capabilities for diverse tasks.
+ **Prompt**: Write the prompt that instructs the model what to generate.
+ **Creativity Level**: Optional. Adjust the slider from low to high to control the randomness of the response.

For more information, see [General knowledge](ai-response-steps.md#general-knowledge-step).

### Configuring Quick data steps
<a name="configuring-quick-suite-data"></a>

In Editor mode, add or select a Quick data step. In the configuration panel, set the following:
+ **Prompt**: Write the prompt that instructs what content to retrieve.
+ **Link specific resources**: Select spaces and knowledge bases to get insights from. By default, responses are generated from all knowledge sources the user has access to.

### Configuring web search steps
<a name="configuring-web-steps"></a>

In Editor mode, add or select a web search step. In the configuration panel, set the following:
+ **Prompt**: Write the prompt that instructs what content to search for on the web.

### Configuring research steps
<a name="configuring-research-steps"></a>

In Editor mode, add or select a research step. In the configuration panel, set the following:
+ **Title**: A name for the step.
+ **Research objective**: Describe what you want to research.
+ **File uploads**: Optional. Upload default files to help guide your research.
+ **Research materials**:
  + **Preferred websites**: Optional. Specify websites or types of websites the agent should prioritize (for example, government websites, academic journals).
  + **Websites to avoid**: Optional. Specify websites or types of websites to exclude (for example, social media, blogs).
+ **Data and apps**: Select all data and apps, or choose specific ones.

### Configuring chat agent steps
<a name="configuring-chat-agent"></a>

In Editor mode, add or select a chat agent step. In the configuration panel, set the following:
+ **Title**: A name for the step.
+ **Chat agent**: Select the agent to use.
+ **Prompt instruction**: Write the prompt that instructs the agent.
+ **Data and apps**: Optionally narrow down the selected data and apps to refine your use case.
+ **Web search**: Toggle to enable or disable web search for the agent.

### Configuring UI Agent steps
<a name="configuring-ui-agent"></a>

In Editor mode, add or select a UI Agent step. In the configuration panel, set the following:
+ **Title**: A name for the step.
+ **UI Agent Instructions**: Write the instructions for the UI agent. Use single, complete URLs for faster, more accurate results.

### Configuring Create Image steps
<a name="configuring-output-image"></a>

In Editor mode, add or select a Create Image step. In the configuration panel, set the following:
+ **Prompt**: Describe the image to generate.
+ **Advanced settings**: Configure creativity level, exclude terms, and image seed.

### Configuring Dashboards and topics steps
<a name="configuring-output-quicksight"></a>

In Editor mode, add or select a Dashboards and topics step. In the configuration panel, set the following:
+ **Quick Sight source**: Choose from Dashboard or Topic.
+ **Prompt**: Describe the insights you want from your dashboard or topic.

For more information, see [Dashboards and topics](data-insight-steps.md#dashboards-and-topics-step).

### Configuring action steps
<a name="configuring-action-steps"></a>

In Editor mode, add or select an action step. In the configuration panel, set the following:
+ **Connector**: Select the connector to use (for example, Salesforce, Jira, Slack).
+ **Action**: Select the specific action to perform.
+ **Prompt**: Write prompt instructions to execute your actions.

For more information, see [Action steps](action-steps-in-flows.md).

### Configuring reasoning groups
<a name="configuring-reasoning-steps"></a>

In Editor mode, add or select a reasoning group. In the configuration panel, set the following:
+ **Instructions**: Write instructions that tell the model what to do, such as conditions, loops, or validation logic. You can reference the output of a previous step as the input to a loop or conditional statement.

## Prompt writing for steps
<a name="prompt-writing-output-steps"></a>

When writing prompts for steps, consider the following best practices:
+ Be clear and specific about what you want the model to generate.
+ Provide context to help the model understand the task.
+ Specify the desired format, tone, and style of the output.
+ Use specific language to control the output — for example, "respond in bullet points", "limit the response to three sentences", or "use a formal tone".
+ Use examples to illustrate the expected output when appropriate.

## Adding and removing steps
<a name="adding-removing-steps"></a>

### Adding steps
<a name="adding-steps"></a>

1. In the Flow editor, choose **Add step** from the toolbar.

1. Select the type of step you want to add.

1. Drag the step to the desired position in your flow.

1. Configure the step as needed.

### Removing steps
<a name="removing-steps"></a>

1. Select the step you want to remove.

1. Choose **Delete** from the context menu.

1. Confirm the deletion when prompted.

**Note**  
When you remove a step, any @ references to that step in other steps are also removed. You may need to update other steps to maintain your flow.

## Publishing changes
<a name="publishing-changes"></a>

After making changes to your flow, publish them to make them available to users.

1. In the Flow editor, choose **Save** to save your changes.

1. Choose **Publish**.

1. Choose **Publish** to confirm.

When you publish, the changes become immediately available to all users who have access to the flow.

## Updating Flow details
<a name="updating-flow-details"></a>

### Updating title and description
<a name="updating-title-description"></a>

1. In the Flow editor, directly edit the title and description in-line.

1. Choose **Save**.

1. Choose **Publish**.

### Viewing the original prompt
<a name="viewing-original-prompt"></a>

If your flow was created using a natural language prompt, you can view the original prompt:

1. In the Flow editor, select the kebab menu in the header.

1. Choose **View prompt**.

**Note**  
The original prompt is read-only. To create a new flow based on a modified prompt, use the natural language prompt method.

## Best practices for editing flows
<a name="best-practices-for-editing-flows"></a>
+ Test your changes thoroughly before publishing them to ensure they work as expected.
+ Use clear and descriptive names for steps to make your flow easier to understand and maintain.
+ Write detailed prompts and instructions to get the best results from AI models.
+ Use @ references to create dynamic flows that adapt to user inputs.
+ Consider the user experience when designing the flow of steps.
+ Document your changes in the publication description to maintain a clear history of updates.

Step configurations and available features may change over time. For the latest information, see the [Terminology and key concepts](terminology-and-key-concepts.md) and the [Amazon Quick Flows product page](https://aws.amazon.com/quicksight/q-apps/).