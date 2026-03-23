# Agents

- **UI agent** - AI agent for web browser tasks. Used for dynamic and intelligent web automation. Simply write instructions to have it navigate websites, extract data, and generate structured outputs.
- **Custom agent** - AI agent for complex tasks. Create an agent that can understand instructions in natural language and take actions using available tools. Used for tasks that require reasoning, judgement, and dynamic planning.

## UI agents

UI agent is a native agent that understands natural language instructions to perform complex browser actions. It can autonomously navigate websites, click, type, read data, and produce structured outputs optimized for downstream automation steps. Example use cases include summarizing products on a webpage or fetching data by navigating websites.

### Properties

Title
Name of the step/UI agent

Instructions

In this field you write the prompt for the agent in natural language. Best practices while writing the prompt:

- Be clear and explicit about what you want.
- Structure the prompt. Start with mentioning the 'Task' or 'Role' first and then 'Instructions' to achieve the task with numbered steps
- Add constraints (e.g., only review the products section) and specify when to stop/end (e.g., stop when you find the relevant info)
- Provide positive and negative (don't do this) examples
- Specify length requirements (e.g., less that 100 words) or output format (e.g., date in MM/DD/YY format) clearly

Wrap the text in triple quotes (""") to write multiline prompts. For example:

```
"""Task: Locate the company's latest annual report.
* Visit the provided URL.
* Look for the annual report. The report may be titled 'Annual Report', 'Financial Report', 'Year in Review', or similar variations..."""
```

Structured Output (optional)
Agent Response: Name of the variable to assign the output of this operation

### How to configure structured output fields

**Adding fields**

- Click Add field to create a new output field
- Enter the Output name - this becomes the JSON property name
- Select the Type from the dropdown
- Check Required if the field must always be present
- Add a Description to guide the AI agent

**Field types**

- _String_ - Text values (Names, descriptions, summaries)
- _Number_ - Numeric values (Counts, scores, percentages)
- _Boolean_ - True/false values (Status flags, yes/no questions)
- _Object_ - Nested structure (Complex data groupings)
- _Array_ - List of items (Tags, categories, multiple values)
- _File_ - File references (Document attachments, images)
- _Data table_ - Tabular data (Structured datasets, reports)

**Working with complex types**

Objects and Arrays can contain nested fields:

- Click the expand arrow (▶) next to Object or Array fields
- Use Add field within the nested structure
- Keep nesting to 2-3 levels maximum for optimal performance

**Example configuration**

Here's a simple configuration for summarizing customer feedback:

```
{
  "orderId": "12345",
  "numberOfOrders": 3,
  "hasShipped": true,
  "orderDetails": {
    "quantity": 2,
    "productName": "ABC",
  },
  "tags": ["electronics", "urgent"]
}
```

This structure would be configured as:

- orderId (String, required)
- numberOfOrders (Number, required)
- hasShipped (Boolean, required)
- orderDetails (Object, required)
  - quantity (Number, required)
  - productName (String, required)

- tags (Array of Strings, Optional)

**Best practices**

- Use descriptive field names - Help the AI understand what data to extract
- Add clear descriptions - Provide context for complex fields
- Mark critical fields as required - Ensure essential data is always present
- Limit nesting depth - Keep structures simple for better performance
- Test your configuration - Verify the output matches your expectations by running the agent step and verifying the response.

**Important notes**

- JSON Knowledge: Unfamiliar with JSON? Learn the basics at json.org
- No validation: Currently, the system doesn't validate output structure - ensure your automation handles missing or malformed data

## Custom agents

Custom agent is an intelligent action that processes natural language inputs to automate complex steps using integrated tool-calling capabilities. It primarily uses integrations as its tool interface, while offering extensibility to use Code as tool, and other native actions like human-in-the-loop task. The agent delivers structured, predictable outputs optimized for seamless integration into downstream automation steps.

### Properties

- **Title**: Name of the step/custom agent
- **Mode**: A mode defines how the agent operates based on your use case. The three available modes are: Fast, Pro, and Custom. Fast is best for simple tasks like summarization, classification, and high-volume automations, and Pro is ideal for complex tasks that involve reasoning and orchestration of multiple tools or actions. Fast and Pro are fully managed modes that require no pre-setup needed in advance. In Custom Mode, you'll need a Bedrock runtime connector and can select the model you want to use (Explained below). This is ideal when you already have a prompt fine-tuned for a particular Bedrock model, specifically need a particular Bedrock model for the Agent, or want to include your own custom or fine-tuned model hosted on Bedrock. In Custom Mode, since you bring your own model from Bedrock via an integration, model inference is billed separately to the account associated with that Bedrock integration.
- **Instructions**: In this field you write the prompt for the agent in natural language. Best practices while writing the prompt:
  - Be clear and explicit about what you want.
  - Structure the prompt. Start with mentioning the 'Task' or 'Role' first and then 'Instructions' to achieve the task with numbered steps
  - To improve tool-call accuracy and guide the Agent, clearly specify in the prompt which tool to use at each step, if applicable.
  - Specify length requirements (e.g., less that 100 words) or output format (e.g., date in MM/DD/YY format) clearly
  - Wrap the text in triple quotes (""") to write multiline prompts. For example:

  ```
  """You are content summarization agent.
  Summarize the last two paragraphs of the provided text, focusing only on the main conclusion."""
  ```

- **Actions**: Action is a tool that enables the AI agent to interact with external systems or perform specific tasks. This is optional. You can run the custom agent without any actions. Below are the different actions which can be used in the custom agent
  - **General Actions**
    - **Create user task** - If enabled, this tool allows the Agent to trigger a Human-in-the-Loop (HITL) task whenever it gets stuck and needs assistance during execution. The Agent pauses and waits for human input. The HITL task is visible in the task center. For best results, the author can specify in the prompt exactly when the Agent should invoke HITL. This is selected by default. The automation runs until the task is finished.
    - **Code** - The Code action generates and executes python code within a restricted python environment, same as code actions, to solve tasks involving calculations, data manipulation, and file processing. Unlike code generators, it actively creates and runs scripts to accomplish objectives, working with Excel, PDF files, various data formats and available integrations
      - **Key Capabilities:**
        - **File Operations**: Process multi-tab Excel files, extract content, perform date calculations, apply conditional formatting, and upload results to S3
        - **Data Transformation**: Convert between JSON and table formats, transpose data, rename columns, and join tables
        - **Advanced Computations**: Generate numerical sequences and perform automated validation

  - **Integrations**: If you have added specific integration actions — such as Salesforce, MS Exchange, or Bedrock—to your automation group, their corresponding actions appear here to be use in the custom agent. The author can then select the relevant actions to use as tools for the agent.

  List of integrations which can be used as tools/actions in the custom agent

      - Amazon S3
      - Amazon Bedrock Data automation
      - Amazon Comprehend
      - Amazon Textract
      - Custom REST API
      - Custom MCP connector
      - Microsoft Outlook
      - Salesforce

- **Structured Output (optional)**

Configure your AI agent to return structured JSON output that downstream steps can process. This feature is ideal for text summarization, report generation, data transformation, and extracting statistics from unstructured content. This is an optional field. If you do not define structured output, the agent returns output in natural language by default. Use structured output when your output has a defined structure, such as a list, data table, or JSON.

###### Note

The structured output configuration for Custom agents follows the same format as UI agents. Refer to the UI agent structured output section for detailed configuration instructions.

- **Agent response**: Name of the variable to assign the output of the agent. The response follow your structured output format in a JSON schema if defined, otherwise is a free-form text.

### Using Custom Models in Custom Agent (Bring your own bedrock model)

Integrate your desired or custom fine-tuned models hosted in AWS Bedrock with Quick Suite automation workflows.

Before you begin, ensure you have the following:

- A fine-tuned model deployed and accessible in AWS Bedrock
- Quick Suite Admin access for creating connectors
- An IAM role with Bedrock permissions for invoking models
- Your model ID (for example, `us.anthropic.claude-3-5-sonnet-20241022-v2:0`)

**Step 1:** Create a Bedrock Runtime Action integration by following the detailed instructions in [AWS service action connectors](builtin-services-integration.md "builtin-services-integration.md")

**Step 2:** Set Up Your Automation Group

Create an automation group and connect the integration:

- **Create an automation group** - Follow the detailed instructions in [Setup tasks](getting-started-quick-automate.md#automate-setup-tasks "getting-started-quick-automate.md#automate-setup-tasks")
- **Configure integrations** - Follow the detailed instructions in [Setup tasks](getting-started-quick-automate.md#automate-setup-tasks "getting-started-quick-automate.md#automate-setup-tasks")
- Once configured, the connector appears in your available assets list

**Step 3:** Configure a Custom Agent

Add and configure a custom agent to use your fine-tuned model:

- Within your automation workflow, add a custom agent
- Configure the following agent settings:
  - **Agent Title**: Enter a descriptive name for your agent
  - **Instructions**: Enter custom prompts tailored to your use case
  - **Mode**: Select Custom
  - **Connector**: Choose your Bedrock Runtime connector (required when Custom mode is selected)
  - **Custom Model**: Enter your model ID (for example, `us.anthropic.claude-3-5-sonnet-20241022-v2:0`) - required when Custom mode is selected

**Next Steps**

Once configured, your custom agent uses the fine-tuned model to process requests according to the instructions you provided. You can now incorporate this agent into your Quick Automate workflows.

###### Note

Ensure your model ID is correctly formatted and matches the model deployed in your AWS Bedrock account. You can find your model ID in the AWS Bedrock console under your provisioned models.

### Custom agent testing

Custom agent testing enables you to test individual agents independently from the complete automation workflow. This capability helps you validate agent behavior, debug prompts, and iterate more efficiently without executing the entire workflow.

#### Prerequisites

- An automation workflow with at least one configured custom agent
- Appropriate permissions to run automations in your workspace

#### Start a test

- In the workflow canvas, hover over the agent card you want to test
- Choose the **Unit test** button that appears at the top of the card
- In the variable collection window that opens, review the automatically detected variables from your agent's prompt
  - The prompt preview displays all detected variables with highlighting

- Enter a value for each variable
  - Values must use valid expression syntax
  - If a value contains invalid syntax, an error message appears and prevents test execution

#### Monitor test execution

During test execution, you can monitor progress in the audit panel on the right side of the screen. The test skips all preceding workflow steps and executes only the selected agent. You get the same logging experience as a full workflow run.

#### Review test results

After the test completes, review the following information in the Test panel:

- Metrics Card (Monitor Tab at the top of the Test panel)
  - Total execution time
  - Number of tools used
  - Number of tasks created

- Logs in between
- Watch Variables Tab (Bottom accordion of the Test panel)
  - Input - View input variables and their values
  - Output - Examine output results from the agent execution
  - For structured outputs, click View Details button to choose the JSON viewer to open the View Output dialog box:
    - Fields Tab - Navigate data using the tree structure view
    - Fields - Highlight corresponding values by selecting tree nodes in Fields tab
    - Output fields - Corresponding values for the JSON keys

### Using Custom agent with Build with Assistant

The current tenet for custom agent is it has to be specifically mentioned to consistently get it invoked, here are the things needed in the prompt to make it appear:

```
- Function names: `use_inline_agent`
- Representation names: "Custom Agent", "Inline Agent" → use `use_inline_agent`
- Generic terms: "agentic skills" → default to `use_inline_agent`
```

Otherwise, the model is preferred to author the workflow deterministically.

Although, in practice, when no appropriate actions are available, planner might pick custom agent as a workaround. But to consistently invoke custom agent in the workflow, the above phrases are encouraged to use in the prompt.

### Examples of agent use cases

**Use Case 1: Email Classification and Assignment Agent**

**Role:** You are an Email Categorization and Assignment Agent

**Instructions:** Follow these steps:

- Step 1: Classify the incoming email based on the Category column of the provided reference table as knowledge
- Step 2: Use the email system to send a notification:
  - From: [system\_email]
  - To: [team\_distribution\_email]
  - Subject: [Classification Result]
  - Body: Include a brief summary explaining the classification reasoning and key points from the original email

- Step 3: For all valid categories (except 'unknown'), create a new case in Salesforce with:
  - Subject: [Original Email Subject]
  - Description: Summarized issue from email body
  - Priority: Based on content urgency (High/Medium/Low)
  - Type: Select appropriate type (Question/Problem/Feature Request/Other)
  - Status: 'New'
  - Category: [Classification result from Step 1]

- Step 4: If classified as 'unknown':
  - Escalate to supervisor for manual review
  - Add note explaining why classification was uncertain
  - Based on the category received from the supervisor, follow step 2 and 3 and stop
  - If the category received from the supervisor is unknown or invalid, stop
