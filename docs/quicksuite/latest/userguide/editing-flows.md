# Editing flows

Once you've created your flow, you can edit and configure it to meet your specific
requirements. This section describes how to modify your flow's components, structure, and
settings.

## Accessing the Flow editor

To edit an existing flow:

1. Sign in to the Amazon Quick Suite console.
2. In the navigation pane, choose _Flows_.
3. Find the flow you want to edit.
4. Choose the flow name to open it in the Flow editor.

The Flows editor provides a visual interface where you can modify your flow's components,
connections, and settings.

## Configuring step types

Each type of step in a flow has specific configuration options. This section describes
how to configure each step type.

### Configuring input text steps

Input text steps collect text input from users. To configure an input text step:

1. Select the input text step in the Flow editor.
2. In the configuration panel, set the following options:
   - _Label_: The text that appears above the input field.
   - _Placeholder_: Optional text that appears inside the input field
     when it's empty.
   - _Default value_: Optional text that pre-fills the input field.
   - _Required_: Toggle to specify whether the input is required.

3. Choose _Save_ to save your changes.

### Configuring file upload steps

File upload steps allow users to upload files to your flow. To configure a file upload
step:

1. Select the file upload step in the Flow editor.
2. In the configuration panel, set the following options:
   - _Label_: The text that appears above the upload control.
   - _Upload default file_: Upload a default file that can be used during flow run.
   - _Allow override of default files_: Enable runtime users to override default files.

3. Choose _Save_ to save your changes.

###### Note

File uploads are processed according to the capabilities of the selected model. Some
models have limitations on file types and sizes they can process.

### Configuring general knowledge steps

General knowledge steps display text responses from models to users. To configure a general knowledge step:

1. Select the general knowledge step from the add step menu in the Flow editor.
2. In the configuration panel, set the following options:
   - _Output preference_: Choose output response preference from Faster responses or Versatility and Performance.
   - _Prompt_: Write the prompt that instructs the model what to generate. You can use @ references to include data from previous steps.
   - _Advanced settings_: Configure model specific parameters such as creativity level to manage randomness of the LLM response.

3. Choose _Save_ to save your changes.

### Configuring Quick suite data steps

Quick suite data steps display text responses from internet search to users. To configure a Quick suite data:

1. Select the Quick suite data step from the add step menu in the Flow editor.
2. In the configuration panel, set the following options:
   - _Prompt_: Write the prompt that instructs what content to generate from the web. You can use @ references to include data from previous steps.
   - _Link specific resources_: Select spaces and knowledge bases that you would like to get insights from. By default, responses are generated from all knowledge sources user has access to.

3. Choose _Save_ to save your changes.

### Configuring web steps

Web steps display text responses from internet search to users. To configure a web step:

1. Select the web step from the add step menu in the Flow editor.
2. In the configuration panel, set the following options:
   - _Prompt_: Write the prompt that instructs what content to generate from the web. You can use @ references to include data from previous steps.

3. Choose _Save_ to save your changes.

For more information about writing effective prompts, see [Prompt writing for output steps](#prompt-writing-output-steps "#prompt-writing-output-steps").

### Configuring output image steps

Output image steps generate and display images to users. To configure an output image
step:

1. Select the output image step in the Flow editor.
2. In the configuration panel, set the following options:
   - _Prompt_: Write the prompt that describes the image to generate.
     You can use @ references to include data from previous steps.
   - _Advanced settings_: Configure mode-specific parameters such as creativity level (defines the randomness of the LLM response), Exclude (a parameter to define what not to include), and image seed (control the determinism of the images generated).

3. Choose _Save_ to save your changes.

### Configuring output Quick Sight steps

Output Quick Sight steps display Quick Sight visualizations to users. To
configure an output Quick Sight step:

1. Select the output Quick Sight step in the Flow editor.
2. In the configuration panel, set the following options:
   - _Quick Sight source_: Choose from Dashboard or a Topic.
   - _Prompt_: Describe insights you want to get from your Quick Sight dashboard or topic. You can use @ references to include data from previous steps.

3. Choose _Apply_ to save your changes.

For more information about integrating Quick visualizations in your flows, see [Amazon Quick Sight steps in flows](amazon-quick-sight-steps-in-flows.md "amazon-quick-sight-steps-in-flows.md").

### Configuring action steps

Action steps perform operations in connected systems. To configure an action step:

1. Select the action step in the Flow editor.
2. In the configuration panel, set the following options:
   - _Action connector_: Select the connector to use (e.g.,
     Salesforce, Jira, Slack).
   - _Action_: Select the specific action to perform.
   - _Prompt_: Write prompt instructions to execute your actions. You can use @ references to include data from previous steps.

3. Choose _Apply_ to save your changes.

For more information about configuring action steps, see [Action steps in flows](action-steps-in-flows.md "action-steps-in-flows.md").

### Configuring reasoning groups

Reasoning groups process information using AI models. To configure a reasoning group:

1. Select the reasoning group in the Flow editor.
2. In the configuration panel, set the following options:
   - _Instructions_: Write the instructions that tell the model what
     to do with the inputs. You can use @ references to include data from previous steps.

3. Choose _Apply_ to save your changes.

## Prompt writing for output steps

Writing effective prompts is essential for getting the desired results from output steps.
This section provides guidance on writing prompts and using @ references.

### Prompt writing basics

When writing prompts for output steps, consider the following best practices:

- Be clear and specific about what you want the model to generate.
- Provide context to help the model understand the task.
- Specify the desired format, tone, and style of the output.
- Use examples to illustrate the expected output when appropriate.

Example prompt for a customer support response:

```

You are a helpful customer support agent for a software company.
Write a response to the customer's inquiry below.
Be professional, empathetic, and solution-oriented.
Include specific steps the customer can follow to resolve their issue.

Customer inquiry: @{input_text}

```

### Using @ references

@ references allow you to include data from previous steps in your prompts. To use an @
reference:

1. In the prompt field, type the @ symbol (@).
2. A dropdown menu will appear showing available references from previous steps.
3. Select the reference you want to include.
4. The reference will be inserted in the format @{step_id}.

You can use @ references in various ways:

- Include user input: `@{input_text}`
- Include file content: `@{file_upload}`
- Include action results: `@{action_step}`

###### Example Prompt with multiple @ references

```

Analyze the customer's message: @{customer_input}

Consider the customer's account information:
- Account type: @{account_info.type}
- Subscription status: @{account_info.status}
- Support level: @{account_info.support_level}

Based on this information, provide a personalized response that addresses the customer's concerns and offers appropriate solutions.

```

## Adding and removing steps

You can add new steps to your flow or remove existing ones as needed.

### Adding steps

To add a new step to your flow:

1. In the Flow editor, choose _Add step_ from the toolbar.
2. Select the type of step you want to add from the dropdown menu.
3. Drag the step to the desired position in your flow.
4. Configure the step as needed.
5. Connect the step to other steps in your flow using @ reference of existing steps.

### Removing steps

To remove a step from your flow:

1. Select the step you want to remove.
2. Choose _Delete_ from the context menu.
3. Confirm the deletion when prompted.

###### Note

When you remove a step, any connections to and from that step are also removed. You
may need to reconnect other steps to maintain the flow of your application.

## Sequential flow

Quick Flows uses a sequential flow model, where steps are run in a specific order based
on their connections.

To create a sequential flow:

1. Arrange your steps in the order you want them to run.
2. Connect each step to the next by dragging a connection from the output port of one
   step to the input port of the next.
3. Ensure that all steps are connected in a logical sequence, with no disconnected
   steps.

The sequential flow determines:

- The order in which steps are presented to users
- The data flow between steps
- The availability of @ references from previous steps

## Quick Suite data vs general knowledge

When configuring reasoning groups and output steps, you can choose between using Quick Suite data and general knowledge.

### Knowledge sources

Quick Suite data

Uses your organization's knowledge base to provide responses based on your
company's specific information, documents, and data.

General knowledge

Uses the model's built-in knowledge to provide responses based on general
information available during the model's training.

### Output preference details

Instead of selecting specific models, you can choose output preferences that optimize the AI response for your specific needs. When configuring output preferences, consider:

- _Faster responses_: Optimized for speed, providing quicker results when time is critical for your workflow.
- _Versatility and Performance_: Balanced approach that handles a wide range of tasks effectively across different use cases.

The system automatically selects the most appropriate Amazon Bedrock model based on your chosen preference and the specific requirements of your flow. For more information about output preferences and model abstraction, see [Using response preferences in General knowledge step](using-response-preferences-in-general-knowledge-step.md "using-response-preferences-in-general-knowledge-step.md").

### Spaces details

Spaces are containers for company knowledge that can be used in your flows. You can create and configure spaces with specific knowledge sources (if you have Author Pro or Reader Pro tier access), such as:

- Document repositories
- Wikis and knowledge bases
- Databases and structured data
- Custom data sources

When configuring a reasoning group or output step, you can select which space to use as
the knowledge source. This determines what information is available to the model when
processing inputs and generating outputs.

## Publishing changes

After making changes to your flow, you need to publish them to make them available to
users.

1. In the Flow editor, choose _Save_ to save your changes.
2. Choose _Publish_ to publish your changes.
3. Choose _Publish_ to confirm.

When you publish changes to a flow:

- The changes become immediately available to all users who have access to the flow.

## Updating Flow details

You can update your flow's title, description, and view the original prompt used to
create it (if applicable).

### Updating title and description

To update your flow's title and description:

1. In the Flow editor, directly edit title and description of your flow in-line.
2. Choose _Save_ to apply your changes.
3. Choose _Publish_ to publish your changes.

### Viewing the original prompt

If your flow was created using a natural language prompt, you can view the original
prompt:

1. In the Flow editor, select the kebab menu in the header.
2. From the options displayed in the menu, choose _View prompt_.
3. The original prompt used to create the flow is displayed.

###### Note

The original prompt is read-only and cannot be modified. If you want to create a new
Flow based on a modified prompt, you can create a new flow using the natural language
prompt method.

## Best practices for editing flows

Consider these best practices when editing your flows:

- Test your changes thoroughly before publishing them to ensure they work as expected.
- Use clear and descriptive names for steps to make your flow easier to understand and
  maintain.
- Write detailed prompts and instructions to get the best results from AI models.
- Use @ references to create dynamic flows that adapt to user inputs.
- Consider the user experience when designing the flow of steps.
- Document your changes in the publication description to maintain a clear history of
  updates.
