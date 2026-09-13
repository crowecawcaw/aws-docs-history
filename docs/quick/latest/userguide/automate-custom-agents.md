

# Custom agents
<a name="automate-custom-agents"></a>

Custom agent is an intelligent action that processes natural language inputs to automate complex steps. It uses integrated tool-calling capabilities with integrations as its primary tool interface. It also offers extensibility to use Code as a tool and other native actions like human-in-the-loop task. The agent delivers structured, predictable outputs optimized for downstream automation steps.

## Properties
<a name="custom-agent-properties"></a>
+ **Title**: Name of the step/custom agent
+ **Mode**: A mode defines how the agent operates based on your use case. The three available modes are Fast, Pro, and Custom. Fast is best for simple tasks like summarization, classification, and high-volume automations. Pro is ideal for complex tasks that involve reasoning and orchestration of multiple tools or actions. Fast and Pro are fully managed modes that require no pre-setup in advance. Custom Mode requires a Bedrock runtime connector and lets you select the model you want to use. For more information, see [Using Custom Models in Custom Agent (Bring your own bedrock model)](#custom-agent-byom). Custom Mode is ideal when you have a prompt fine-tuned for a particular Bedrock model, need a specific Bedrock model for the Agent, or want to use your own custom or fine-tuned model hosted on Bedrock. In Custom Mode, you bring your own model from Bedrock through an integration. Model inference is billed separately to the account associated with that Bedrock integration.
+ **Instructions**: In this field you write the prompt for the agent in natural language. Best practices while writing the prompt:
  + Be clear and explicit about what you want.
  + Structure the prompt. Start with mentioning the 'Task' or 'Role' first and then 'Instructions' to achieve the task with numbered steps
  + To improve tool-call accuracy and guide the Agent, clearly specify in the prompt which tool to use at each step, if applicable.
  + Specify length requirements (e.g., less that 100 words) or output format (e.g., date in MM/DD/YY format) clearly
  + Wrap the text in triple quotes (""") to write multiline prompts. For example:

    ```
    """You are content summarization agent.
    Summarize the last two paragraphs of the provided text, focusing only on the main conclusion."""
    ```
+ **Actions**: Action is a tool that enables the AI agent to interact with external systems or perform specific tasks. This is optional. You can run the custom agent without any actions. The following actions can be used in the custom agent.
  + **General Actions**
    + **Create user task** - If enabled, this tool allows the Agent to trigger a Human-in-the-Loop (HITL) task when it gets stuck during execution. The Agent pauses and waits for human input. The HITL task is visible in the task center. For best results, specify in the prompt exactly when the Agent should invoke HITL. This action is selected by default. The automation runs until the task is finished.
    + **Code** - The Code action generates and executes Python code within a restricted Python environment, same as code actions. It solves tasks involving calculations, data manipulation, and file processing. Unlike code generators, it actively creates and runs scripts to accomplish objectives. It works with Excel, PDF files, various data formats, and available integrations.
      + **Key Capabilities:**
        + **File Operations**: Process multi-tab Excel files, extract content, perform date calculations, apply conditional formatting, and upload results to S3
        + **Data Transformation**: Convert between JSON and table formats, transpose data, rename columns, and join tables
        + **Advanced Computations**: Generate numerical sequences and perform automated validation
  + **Integrations**: If you have added specific integration actions — such as Salesforce, MS Exchange, or Bedrock—to your automation group, their corresponding actions appear here to be use in the custom agent. The author can then select the relevant actions to use as tools for the agent.

    List of integrations which can be used as tools/actions in the custom agent
    + Amazon S3
    + Amazon Bedrock Data automation
    + Amazon Comprehend
    + Amazon Textract
    + Custom REST API
    + Custom MCP connector
    + Microsoft Outlook
    + Salesforce
+ **Structured Output (optional)**

  Configure your AI agent to return structured JSON output that downstream steps can process. This feature is ideal for text summarization, report generation, data transformation, and extracting statistics from unstructured content. This is an optional field. If you do not define structured output, the agent returns output in natural language by default. Use structured output when your output has a defined structure, such as a list, data table, or JSON.
**Note**  
The structured output configuration for Custom agents follows the same format as UI agents. Refer to the UI agent structured output section for detailed configuration instructions.
+ **Agent response**: Name of the variable to assign the output of the agent. The response follow your structured output format in a JSON schema if defined, otherwise is a free-form text.

## Using Custom Models in Custom Agent (Bring your own bedrock model)
<a name="custom-agent-byom"></a>

Integrate your desired or custom fine-tuned models hosted in AWS Bedrock with Quick Suite automation workflows.

Before you begin, ensure you have the following:
+ A fine-tuned model deployed and accessible in AWS Bedrock
+ Quick Suite Admin access for creating connectors
+ An IAM role with Bedrock permissions for invoking models
+ Your model ID (for example, `us.anthropic.claude-3-5-sonnet-20241022-v2:0`)

**Step 1:** Create a Bedrock Runtime Action integration by following the detailed instructions in [AWS service connectors](builtin-services-integration.md)

**Step 2:** Set Up Your Automation Group

Create an automation group and connect the integration:
+ **Create an automation group** - Follow the detailed instructions in [Setup tasks](getting-started-quick-automate.md#automate-setup-tasks)
+ **Configure integrations** - Follow the detailed instructions in [Setup tasks](getting-started-quick-automate.md#automate-setup-tasks)
+ Once configured, the connector appears in your available assets list

**Step 3:** Configure a Custom Agent

Add and configure a custom agent to use your fine-tuned model:
+ Within your automation workflow, add a custom agent
+ Configure the following agent settings:
  + **Agent Title**: Enter a descriptive name for your agent
  + **Instructions**: Enter custom prompts tailored to your use case
  + **Mode**: Select Custom
  + **Connector**: Choose your Bedrock Runtime connector (required when Custom mode is selected)
  + **Custom Model**: Enter your model ID (for example, `us.anthropic.claude-3-5-sonnet-20241022-v2:0`) - required when Custom mode is selected

**Next Steps**

Once configured, your custom agent uses the fine-tuned model to process requests according to the instructions you provided. You can now incorporate this agent into your Quick Automate workflows.

**Note**  
Ensure your model ID is correctly formatted and matches the model deployed in your AWS Bedrock account. You can find your model ID in the AWS Bedrock console under your provisioned models.

## Custom agent testing
<a name="custom-agent-testing"></a>

Custom agent testing enables you to test individual agents independently from the complete automation workflow. This capability helps you validate agent behavior, debug prompts, and iterate more efficiently without executing the entire workflow.

### Prerequisites
<a name="custom-agent-testing-prerequisites"></a>
+ An automation workflow with at least one configured custom agent
+ Appropriate permissions to run automations in your workspace

### Start a test
<a name="custom-agent-testing-start"></a>
+ In the workflow canvas, hover over the agent card you want to test
+ Choose the **Unit test** button that appears at the top of the card
+ In the variable collection window that opens, review the automatically detected variables from your agent's prompt
  + The prompt preview displays all detected variables with highlighting
+ Enter a value for each variable
  + Values must use valid expression syntax
  + If a value contains invalid syntax, an error message appears and prevents test execution

### Monitor test execution
<a name="custom-agent-testing-monitor"></a>

During test execution, you can monitor progress in the audit panel. The test skips all preceding workflow steps and executes only the selected agent. You get the same logging experience as a full workflow run.

### Review test results
<a name="custom-agent-testing-results"></a>

After the test completes, review the following information in the Test panel:
+ Metrics Card (Monitor Tab in the Test panel)
  + Total execution time
  + Number of tools used
  + Number of tasks created
+ Logs in between
+ Watch Variables Tab (Variables accordion in the Test panel)
  + Input - View input variables and their values
  + Output - Examine output results from the agent execution
  + For structured outputs, choose **View Details** to open the View Output dialog box:
    + Fields Tab - Navigate data using the tree structure view
    + Fields - Highlight corresponding values by selecting tree nodes in Fields tab
    + Output fields - Corresponding values for the JSON keys

## Using Custom agent with Build with Assistant
<a name="custom-agent-build-with-assistant"></a>

The current tenet for custom agent is it has to be specifically mentioned to consistently get it invoked, here are the things needed in the prompt to make it appear:

```
- Function names: `use_inline_agent`
- Representation names: "Custom Agent", "Inline Agent" → use `use_inline_agent`
- Generic terms: "agentic skills" → default to `use_inline_agent`
```

Otherwise, the model is preferred to author the workflow deterministically.

Although, in practice, when no appropriate actions are available, planner might pick custom agent as a workaround. But to consistently invoke custom agent in the workflow, the above phrases are encouraged to use in the prompt.

## Examples of agent use cases
<a name="custom-agent-examples"></a>

**Use Case 1: Email Classification and Assignment Agent**

**Role:** You are an Email Categorization and Assignment Agent

**Instructions:** Follow these steps:
+ Step 1: Classify the incoming email based on the Category column of the provided reference table as knowledge
+ Step 2: Use the email system to send a notification:
  + From: [system\_email]
  + To: [team\_distribution\_email]
  + Subject: [Classification Result]
  + Body: Include a brief summary explaining the classification reasoning and key points from the original email
+ Step 3: For all valid categories (except 'unknown'), create a new case in Salesforce with:
  + Subject: [Original Email Subject]
  + Description: Summarized issue from email body
  + Priority: Based on content urgency (High/Medium/Low)
  + Type: Select appropriate type (Question/Problem/Feature Request/Other)
  + Status: 'New'
  + Category: [Classification result from Step 1]
+ Step 4: If classified as 'unknown':
  + Escalate to supervisor for manual review
  + Add note explaining why classification was uncertain
  + Based on the category received from the supervisor, follow step 2 and 3 and stop
  + If the category received from the supervisor is unknown or invalid, stop

## Using knowledge bases with custom agents
<a name="custom-agent-knowledge-bases"></a>

In Amazon Quick Automate, you can connect knowledge bases to custom agents to enable AI-powered retrieval and question answering over your organization's documents. By linking a Quick space to your automation group, custom agents can search and retrieve information from the knowledge bases within that space.

Use this for automations that need to reference organizational knowledge — such as answering questions from policy documents, summarizing reports, or classifying content based on reference data.

Knowledge bases index your documents for semantic search, so the custom agent retrieves only the most relevant passages rather than processing entire files. This makes retrieval faster and more accurate, especially across large document sets.

### Prerequisites
<a name="custom-agent-kb-prerequisites"></a>
+ A Quick space with one or more knowledge bases configured. For more information, see [Organize, collaborate, and share resources with spaces in Amazon Quick](working-with-spaces.md).
+ An automation group where you are an owner
+ Owner-level access to the space you want to link

### Link a space to your automation group
<a name="custom-agent-kb-link-space"></a>

Before a custom agent can access knowledge bases, you must link the space that contains those knowledge bases to your automation group. Linking a space grants the automation group permission to access the knowledge bases and files within that space.

To link a space to an automation group:

1. In the **Automations** tab, go to the **Projects** page.

1. Choose **Groups** and select the group you want to attach the space to.
**Tip**  
You can also choose **Create group** to create a new automation group.

1. In the **Assets** section, choose **Add**, and then choose **Spaces**.

1. Select the space that contains the knowledge bases you want to use, and then choose **Add**.

The space now appears in the automation group's connections list. Custom agents in this automation group can access the knowledge bases and files within the linked space. Other resources in the space are not available to automations.

**Note**  
If the space shows **Limited access** after being added, it means not all knowledge bases are shared with the automation group. This can happen if knowledge bases were added to the space after linking, or if not all knowledge bases were shared initially. To resolve this, refresh the space connection to share all resources with the automation group. You do not need to reconfigure the Knowledge tab on individual custom agents.

### Add knowledge to a custom agent
<a name="custom-agent-kb-add-knowledge"></a>

After linking a space to your automation group, you can configure a custom agent to use the knowledge bases within that space. The workflow must be in the same automation group where you attached the space.

To add knowledge to a custom agent:

1. In the workflow builder, add a **Custom Agent** step. You can either drag and drop a Custom Agent node onto the canvas, or chat with the automation assistant to build this step.

1. In the agent properties panel, choose **Knowledge**, and then choose **Add**.

1. A picker opens showing available spaces linked to the automation group. Select one or more spaces that contain the knowledge bases you want the agent to use.

1. Choose **Save**.

The custom agent can now search and retrieve content from the knowledge bases in the selected spaces when the automation runs.

When you attach a space, all knowledge bases inside that space automatically become available to the agent. You don't need to attach each knowledge base individually. At runtime, the agent queries each knowledge base independently and combines the results in its response.

**Note**  
If the automation group owner loses access to a specific knowledge base within the space, that knowledge base is skipped during queries and the workflow editor displays a warning badge on the space attachment.

### Writing instructions for knowledge base queries
<a name="custom-agent-kb-instructions"></a>

When a custom agent has knowledge bases attached, it automatically searches and retrieves relevant content based on your instructions. Write instructions that clearly describe what information the agent should find or how it should use the knowledge base content.

Best practices:
+ Be specific about what information to retrieve or summarize
+ Reference the type of content you expect the agent to find (for example, "Search the policy documents for..." or "Find information about...")
+ Specify how the agent should use the retrieved information in its response
+ Include fallback instructions for when the knowledge base doesn't contain relevant content

### Example: Customer inquiry agent with knowledge base
<a name="custom-agent-kb-example"></a>

The following example shows how to configure a custom agent that uses a knowledge base to answer customer inquiries based on company documentation.

**Setup:**
+ A space containing a knowledge base with product documentation and FAQ content
+ The space is linked to the automation group
+ The space is added as knowledge to the custom agent

**Instructions:**

```
"""You are a customer support agent.

Task: Answer the customer inquiry using information from the knowledge base.

Instructions:
1. Search the knowledge base for information relevant to the customer's question.
2. Provide a clear, concise answer based on the retrieved content.
3. If the knowledge base does not contain relevant information, respond with:
   "I don't have enough information to answer this question. Please escalate to a human agent."

Constraints:
- Only use information found in the knowledge base. Do not make up answers.
- Keep responses under 200 words.
- Include the source document name when referencing specific information."""
```

**Structured output:**

```
{
  "answer": "The response to the customer inquiry",
  "sourceDocument": "Name of the document used",
  "confidence": "high/medium/low",
  "escalationNeeded": false
}
```

## Using datasets with custom agents
<a name="custom-agent-datasets"></a>

In Amazon Quick Automate, you can connect datasets to custom agents so that an agent can answer natural-language questions about your data. The underlying query returns a list of data tables and a string output from the API call. You can then convert this output into a desired data structure, either by prompting the custom agent or by using the structured output feature of the custom agent.

Dataset Q&A (querying datasets) is an agentic action that you use with the custom agent. A custom agent can query multiple datasets, but it runs one query at a time.

Use datasets for data-driven question-answering automations. For example, you can build an agent that answers questions such as "which customers have unpaid invoices over $10,000" by querying an invoices dataset and returning the matching rows.

### Prerequisites
<a name="custom-agent-datasets-prerequisites"></a>
+ Owner-level access to the dataset you want to attach
+ A dataset that does not use row-level security (RLS) or column-level security (CLS). Datasets with RLS or CLS are not supported.
+ An automation group where you are an owner
+ Datasets attached to the automation group for run-as-service mode, or datasets shared with your user ID for run-as-user mode

### Attach a dataset to your automation group
<a name="custom-agent-datasets-attach-group"></a>

Before a custom agent can query a dataset, you must attach the dataset to your automation group. You must already have access to the dataset as an owner. Attaching the dataset to the automation group does not grant you access to it.

To attach a dataset to an automation group:

1. In the **Automations** tab, go to the **Projects** page.

1. Choose **Groups** and select the group you want to attach the dataset to.
**Tip**  
You can also choose **Create group** to create a new automation group.

1. In the **Assets** section, choose **Add**, and then choose **Datasets**. The picker opens with **Actions**, **Credentials**, **Spaces**, and **Datasets** tabs.

1. On the **Datasets** tab, select the dataset you want to use, and then choose **Add**. You can search your Quick assets. Datasets that you cannot use appear disabled, and you can hover over one to see the reason, such as needing to be an owner.

The dataset now appears in the automation group's assets and connections list. Custom agents in this automation group can query it.

**Note**  
You must be the owner of the dataset to use it. Datasets that use row-level security (RLS) or column-level security (CLS) are not supported.

### Add datasets to a custom agent
<a name="custom-agent-datasets-add"></a>

After you attach one or more datasets to your automation group, you can configure a custom agent to query them. The workflow must be in the same automation group where you attached the datasets. After you add the Custom Agent step, you add the dataset from the agent's properties panel on the **Datasets** tab.

To add datasets to a custom agent:

1. In the workflow builder, add a **Custom Agent** step. You can either chat with the automation assistant to build this step, or drag and drop a Custom Agent node onto the canvas.

1. In the agent properties panel, choose the **Datasets** tab.

1. Add one or more datasets directly on the **Datasets** tab.

1. Choose **Save**.

A custom agent can use multiple datasets, but it runs one query at a time. If you connect a Quick space that contains a dataset, the agent can query that dataset as well. For more information about spaces, see [Organize, collaborate, and share resources with spaces in Amazon Quick](working-with-spaces.md).

### Query a dataset with the agent
<a name="custom-agent-datasets-query"></a>

After you add a dataset to the custom agent, you can ask the agent a question about the data. When the automation runs, or when you test the agent, the agent queries the attached dataset and returns a response based on the results.

To query a dataset:

1. In the agent **Instructions**, write a prompt that asks a question about the data. For example, ask a natural-language question about records in the dataset.

1. Run the automation, or use the agent unit test to run the agent. For more information about testing an agent, see [Custom agent testing](#custom-agent-testing).

The agent queries the dataset and returns the answer.

To return the results in a specific format that downstream steps can process, such as a JSON object or a data table, configure the Structured Output option for the agent. Structured output is optional and returns structured JSON. The structured output configuration for custom agents follows the same format as UI agents. In your prompt, instruct the agent to produce output that matches the structured output schema.

### Use datasets in a space with a custom agent
<a name="custom-agent-datasets-via-space"></a>

Instead of attaching datasets directly on the agent's **Datasets** tab, you can add your datasets to a Quick space, attach the space to your automation group, and then attach the space to the custom agent on the **Knowledge** tab. The agent can then query the datasets in that space based on your instructions. This approach is useful when you already organize datasets, and other knowledge, in a space.

To use datasets in a space:

1. Add your dataset or datasets to a Quick space. For more information about spaces, see [Organize, collaborate, and share resources with spaces in Amazon Quick](working-with-spaces.md).

1. Attach the space to your automation group. In the **Automations** tab, on the **Projects** page, choose **Groups** and select your group. In the **Assets** section, choose **Add**, and then choose **Spaces**. Select the space and choose **Add**.

1. In the workflow builder, add a **Custom Agent** step. You can either chat with the automation assistant to build this step, or drag and drop a Custom Agent node onto the canvas.

1. In the agent properties panel, choose the **Knowledge** tab, choose **Add**, select the space that contains your datasets, and then choose **Save**.

1. In the agent **Instructions**, write a prompt that asks a question about the data in the space's datasets.

When the automation runs, the agent queries the datasets in the attached space and returns the results. The datasets must still meet the dataset requirements. You must be an owner of each dataset, and datasets that use row-level security (RLS) or column-level security (CLS) are not supported.

### Writing instructions for dataset queries
<a name="custom-agent-datasets-instructions"></a>

When a custom agent has datasets attached, it automatically determines the relevant dataset and constructs the query based on your instructions. Write instructions that clearly describe what data the agent should retrieve and how it should present the results.

Best practices:
+ Be specific about what data to retrieve, such as the columns, records, or aggregations you expect in the results.
+ Include filters, calculation definitions, or metric logic in the prompt to improve query accuracy.
+ Specify the output format so that downstream steps can process the results.

### Example: Invoice analysis agent with a dataset
<a name="custom-agent-datasets-example"></a>

The following example shows how to configure a custom agent that queries a dataset to answer questions about outstanding invoices.

**Setup:**
+ A dataset that contains customer invoice records, including customer name, invoice amount, and payment status
+ The dataset is attached to the automation group
+ The dataset is added to the custom agent on the Datasets tab

**Instructions:**

```
"""You are an invoice analysis agent.

Task: Answer the user's question by querying the invoices dataset.

Instructions:
1. Identify the relevant dataset and construct a query for the user's request.
2. For the request "Show me customers with unpaid invoices over $10,000",
   filter for records where payment status is unpaid and invoice amount is
   greater than 10000.
3. Return the results as a data table with customer name and invoice amount.

Constraints:
- Only use data found in the dataset. Do not make up values.
- Sort the results by invoice amount in descending order."""
```

**Output:**

The agent returns a data table similar to the following:

```
| Customer name        | Invoice amount |
|----------------------|----------------|
| Example Corp         | 24,500         |
| AnyCompany Retail    | 15,200         |
| AnyCompany Financial | 11,750         |
```