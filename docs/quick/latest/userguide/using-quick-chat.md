

# Ask questions, explore data, and get insights with chat in AWS Quick

You can use AWS Quick chat to ask questions, interact with your Quick resources, and accomplish tasks through multiple agentic workflows using natural language. When you ask a question, Quick chat analyzes the data it can access to generate comprehensive responses.

Quick chat provides you with the following capabilities.

**Topics**
+ [Welcome message](#welcome-message)
+ [Suggested prompts](#suggested-prompts)
+ [Expand and collapse modes](#expand-collapse)
+ [Response preferences](#response-preferences)
+ [Agent picker](#agent-picker)
+ [Scoping response generation to specific data](#data-filter)
+ [Chatting with datasets](#chatting-with-datasets)
+ [Chatting with Topics](#chatting-with-topics)
+ [Web search](#web-search)
+ [Upload files and chat](#file-uploads)
+ [Slash commands](#slash-commands)
+ [Mentions](#mentions)
+ [All data and apps panel](#all-data-and-apps)
+ [Chat with a space](#chat-with-spaces)
+ [Flows](#chat-flows)
+ [Memory and response personalization](#chat-memory)
+ [Source citations](#review-source-citation)
+ [Copy responses](#copy-responses)
+ [Provide feedback](#provide-feedback)
+ [Artifact panel](#artifact-panel)
+ [Conversation management](#conversation-mgmt)
+ [Response events](#response-events)
+ [Explanations](#chat-explanations-summary)
+ [Contextual awareness](#contextual-awareness)
+ [Managing your preferences in AWS Quick](#user-preferences)
+ [Deep research](#deep-research)
+ [Running work in the background](#background-work)
+ [Chat features in the desktop app](#desktop-app-chat)
+ [AWS Quick chat explanations](chat-explanations.md)

## Welcome message
<a name="welcome-message"></a>

When you log in, AWS Quick chat displays a welcome message.

## Suggested prompts
<a name="suggested-prompts"></a>

To help you get started on interacting with your resources in chat, AWS Quick displays suggested prompts you can use to learn more about AWS Quick features. Use these to get started on your tasks. Once you select a prompt, AWS Quick guides you step-by-step through the information it needs from you to complete the task.

**Note**  
Suggested prompts are system generated for the system agent; you can't customize them. For custom agents, suggested prompts can be created and customized by the agent builder or owner.

## Expand and collapse modes
<a name="expand-collapse"></a>

To help enhance your productivity and streamline your chat interactions, AWS Quick offers two separate chat window display modes:
+ **Collapse mode** – The default chat window display. Use for easy access to chat from within all AWS Quick contexts.
+ **Expand mode** – Access chat in an expanded view. Use this mode to work in the chat window without any distractions.

You can open up the chat interface at any time by selecting the chat bubble icon from the top right navigation menu. You can also exit out of the chat at any time by selecting the cancel icon from the top navigation menu.

## Response preferences
<a name="response-preferences"></a>

AWS Quick chat provides multiple response modes that you choose based on your task. To switch between modes, use the response preferences selector in the chat input area.


| Mode | Description | Best for | 
| --- | --- | --- | 
| Fast | Optimized for speed on everyday tasks. Quick generates responses quickly with the lowest latency. | Quick questions and simple tasks where speed matters more than depth. | 
| Balanced | Balances quality and speed. Quick provides high-quality responses with moderate latency. | Most tasks, including writing assistance, summarization, and general day-to-day work. | 
| Smart | Provides the highest-quality responses, with the most thorough reasoning and longer response times. | Complex analysis, nuanced writing, detailed reasoning, and tasks that require high accuracy. | 

### Thinking effort
<a name="thinking-effort"></a>

You control the thinking effort independently from the response mode. Thinking effort determines how much reasoning Quick applies before it responds. Higher thinking effort enables deeper reasoning for complex code, strategic planning, and analysis.


| Level | Description | 
| --- | --- | 
| Off | Quick responds directly, with no extended reasoning. | 
| Low | Quick applies minimal reasoning before responding. | 
| Medium | Quick applies moderate reasoning, a good balance for most tasks. | 
| High | Quick applies extended reasoning for complex problems. | 

You can set thinking effort on **Balanced** and **Smart** modes. **Fast** mode responds without extended reasoning. To change the thinking effort, choose the response preferences selector in the chat input area, and then adjust the thinking effort picker.

## Agent picker
<a name="agent-picker"></a>

Chat agents in AWS Quick are conversational assistants that help users explore data, analyze information, and take actions. You can pick any agent you've created to use during chat, or use the system agent **My Assistant** for your conversations.

To learn more about agents, see [Working with agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html).

## Scoping response generation to specific data
<a name="data-filter"></a>

When you use AWS Quick, you can define what data you want your chat responses generated from using data filters. Data filters enable you to customize your chat's expertise area. The data available to your agent depends on whether it is bound to specific AWS Quick knowledge and integrations, or if it's unbounded (not connected to specific AWS Quick resources).

By default, an agent has knowledge of all your AWS Quick resources and its underlying large language model (LLM). While using chat, you can select between the following knowledge modes:
+ **All data and apps** – AWS Quick will use all available knowledge sources (including spaces, dashboards, datasets, topics, knowledge bases, action integrations, and LLM knowledge) to generate a response to your prompts.
+ **General knowledge** – AWS Quick will only use LLM knowledge to generate responses to your prompts. It won't use any knowledge from AWS Quick resources.
+ **Specific data and apps** – Chat with a specific or multiple spaces, dashboards, datasets, topics, knowledge bases, or actions. To choose specific resources, select **Choose resource**.

An agent with pre-defined knowledge, on the other hand, only has knowledge of existing AWS Quick resources already linked to it, and its underlying LLM knowledge. While chatting with an agent with pre-defined knowledge, you get the following knowledge modes:
+ **Pre-defined knowledge** – AWS Quick will use only the AWS Quick resource knowledge linked to the agent, and LLM knowledge, to generate responses. You can't change this setting. 
+ **Additional data and apps** – Chat with a specific or multiple spaces, dashboards, datasets, topics, or knowledge bases and actions. To choose specific resources, select **Choose resource**.

## Chatting with datasets
<a name="chatting-with-datasets"></a>

You can chat with your datasets in AWS Quick to ask questions and get insights from your data using natural language. To get started, you need to first create a dataset. For more information, see [Creating datasets](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html).

AWS Quick chat supports the following dataset types:
+ SPICE datasets
+ Direct Query datasets against Amazon Redshift, Athena, Aurora PostgreSQL, Amazon S3 Tables, Databricks, and Snowflake

**Note**  
Direct Query datasets against other data sources are not yet supported for chat.

For SPICE datasets, the size limit of 2 TB and 2 billion rows applies when chatting with the dataset.

## Chatting with Topics
<a name="chatting-with-topics"></a>

You can chat with your Topics in AWS Quick to ask natural language questions that span multiple datasets. When you select a Topic as your data context in chat, the LLM-powered chat agent uses the defined relationships, dataset enrichment metadata, and custom instructions to generate cross-dataset SQL queries and return unified answers.

To chat with a Topic, use the data filter to select **Specific data and apps** and choose your Topic from the list. Or navigate to the Topic and choose the chat icon.

The chat agent traverses relationships across datasets, identifying which tables contain the relevant columns, constructing SQL with appropriate joins, and returning a unified answer. You can view the generated SQL in the Explanation panel to verify the correct datasets and joins were used.

AWS Quick chat supports the following Topic types:
+ **New Topics (multi-dataset)** – The LLM-powered chat agent generates cross-dataset SQL with runtime joins. It can produce inner joins, left joins, outer joins, unions, and subqueries based on your defined relationships and custom instructions.
+ **Legacy Topics** – The legacy ML-based fuzzy search model selects one dataset from the Topic and queries only that single dataset. Cross-dataset queries are not supported.

For more information about creating and configuring Topics, see [Working with AWS Quick Sight Topics](topics.md).

## Web search
<a name="web-search"></a>

AWS Quick comes with built-in web search capability. AWS Quick chat automatically searches both your connected data sources and the web, providing comprehensive answers from either or both sources as needed. You can turn web search off for any query by choosing the globe icon in the chat panel. Any content retrieved from the web is appropriately cited in the final response.

**Note**  
Web search is available to users only if it has been enabled by admin.

## Upload files and chat
<a name="file-uploads"></a>

You can upload documents into AWS Quick chat and ask AWS Quick chat to summarize or analyze data based on the content of the uploaded documents.

When you start a new conversation, you can upload new files, choose from a saved list of recent documents, or drag and drop files directly into the conversation.

You can upload up to 20 files at one time with the following size limits:
+ 10 MB for images (`.jpeg`, `.png`)
+  10 MB for spreadsheet files (`.csv`, `.xls`, `.xlsx`)
+ 50 MB for other supported formats

Supported file types include:
+ Word (`.docx`)
+ Excel (`.xls`, `.xlsx`)
+ PowerPoint (`.ppt`, `.pptx`)
+ PDF (`.pdf`)
+  images (`.jpeg`, `.png`)
+ text files (`.csv`, `.txt`, `.rtf`, `.md`)
+ Outlook (`.msg`)
+ structured data files (`.json`, `.yaml`, `.xml`, `.vtt`, and common code files)

The total parsed content for all files combined has to be under 665,000 characters.

**Note**  
If your files exceed the file count and character count limits, you can upload them to a [space](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-spaces.html) instead.

Documents uploaded through the chat interface are deleted with the associated conversation after 365 days of inactivity.

**Note**  
Audio and video files are not supported as file uploads.

## Slash commands
<a name="slash-commands"></a>

You can run commands directly from the chat input area. To open the command menu, type a forward slash (/) at the start of your message, and then choose a command or continue typing to filter the list.


| Command | Description | 
| --- | --- | 
| /clear | Starts a new conversation with fresh context. Your current conversation is saved separately, not lost. | 
| /compact | Condenses the current conversation to free up context. | 
| /export | Exports the conversation as Markdown or PDF. | 
| /mode | Switches the response mode and thinking effort. | 
| /rename | Renames the current conversation. | 
| /copy | Copies the most recent response. | 
| /skills | Shows the available skills. | 
| /connectors | Shows and manages your connectors. | 
| /goal | Gives the agent a job to finish rather than a single question to answer. Quick keeps working on its own until the job is complete, checks its own work, and then hands it back. | 
| /help | Shows the list of available commands. | 

## Mentions
<a name="mentions"></a>

To reference a specific agent, an item in your message, or people from your knowledge graph, type an at sign (@), and then choose from the list that appears. Mentions let you direct your request to a particular agent or person, or point AWS Quick chat to a specific item, without leaving the chat input area.

## All data and apps panel
<a name="all-data-and-apps"></a>

The **All data and apps** panel shows the spaces, knowledge sources, and skills available to the current conversation, so you can add or adjust the resources the agent draws on. Each skill shows a status indicator that pairs an icon with text, such as **Active**, **Needs setup**, or **Error**, so status is clear without relying on color alone. 

## Chat with a space
<a name="chat-with-spaces"></a>

You can attach a space to your conversation to ground responses in your team's shared knowledge. While a space is attached, AWS Quick chat answers from the content in that space, which keeps the conversation within a scoped context for confidentiality or data compliance. This applies to everything in the space, including its files, datasets, dashboards, topics, and actions.

If the answer is not in the attached space, AWS Quick chat tells you so rather than answering from somewhere else. You can ask Quick to search more broadly, and it does so for the rest of that conversation until you change it again. A space you attach applies to that conversation only, so a new conversation starts with nothing attached.

To attach a space, choose the **Add context** icon in the chat input area, choose **Spaces**, and then select the space you want to use. For more information about spaces, see [Organize, collaborate, and share resources with spaces in AWS Quick](working-with-spaces.md).

## Flows
<a name="chat-flows"></a>

Use AWS Quick flows to create shortcuts for everyday, repetitive tasks you perform while chatting in AWS Quick. For example, if you find yourself using AWS Quick chat to create and copy edit product launch descriptions, you can use AWS Quick flows to generate an application that takes your draft content as input, and generates a polished draft—after content, style, and grammar review—as output.

You can run a flow directly from chat within a conversation. Within a single conversation, you can talk to a chat agent as well as run a flow.

To learn more about flows, see [Flows in AWS Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-flows.html).

## Memory and response personalization
<a name="chat-memory"></a>

Memory in AWS Quick chat helps personalize your conversations by remembering your preferences, context, and past interactions. Chat agents can reference this stored information to provide more personalized and contextually relevant responses without you needing to repeat information in every conversation, enabling more relevant and tailored responses over time.

When you interact with chat agents in AWS Quick, you can provide your preferences including:
+ Response style and format
+ Frequently accessed Dashboards, Spaces, integrations, and other AWS Quick assets
+ Context about your role and responsibilities
+ Common tasks and workflows you perform

This information is securely stored and fetched to enhance your future interactions with chat agents. Memories are specific to you and are not shared with other users. To get the most value from memory in chat, follow these best practices:
+ **Be explicit about your preferences** – Clearly state your preferences, priorities, and context when you want the chat agent to remember them. For example, "I prefer reports in table format" or "I work on the marketing team".
+ **Provide relevant context** – Share information about your role, responsibilities, and common tasks to help chat agents understand your needs better.
+ **Update your preferences** – As your priorities change, inform the chat agent about updates to ensure the stored information remains current and relevant.
+ **Review and refine** – If responses don't align with your expectations, provide feedback and clarify your preferences to improve future interactions.

You maintain control over your memory data. You can review chat memory by going to **Conversation History** and choosing **View Memories**.

Quick keeps memories per agent. The default assistant and each custom agent have their own memories, so a preference you set for one agent does not change how another agent behaves. Entities in your knowledge graph stay shared across agents. For more information about your knowledge graph and My context, see [Your knowledge graph and My context](knowledge-graph.md).

Quick records a memory in one of two ways, shown as its provenance:
+ **Told** – You stated it explicitly to Quick.
+ **Learned** – Quick inferred it from your activity or conversations.

Each memory shows a confidence score, how often it has been used, and its source. You can review, filter, and manage your memories, including boosting, forgetting, and editing them, from Preferences. For more information, see [Managing your memories](#manage-memories).

**Note**  
Chat memory has the following limitations:  
Chat memory isn't supported for accounts configured with [AWS KMS customer managed keys](https://docs.aws.amazon.com/quicksuite/latest/userguide/customer-managed-keys.html).

## Source citations
<a name="review-source-citation"></a>

AWS Quick chat responses provide in-text source citations in a numbered list. To view the source for a response, choose the number at the end of the sentence. The dialog box shows the title, URL, and a snippet from the source that was used to generate the response. Choose the URL to view the source document.

To view the full list of sources, choose **Sources** at the end of the response. You can use the source list to fact-check the response, or for deeper analysis. 

When a response draws on your memory, the **Sources** list includes the memories that shaped it. You can boost the memories that were helpful or remove the ones that were not.

## Copy responses
<a name="copy-responses"></a>

You can copy and save the responses for later review and analysis. To copy a response, choose the copy icon at the end of the response.

## Provide feedback
<a name="provide-feedback"></a>

You can provide direct feedback about the responses you received from AWS Quick chat by using the thumbs-up or thumbs-down button. Your feedback is used to help address technical issues in the web experience. 

If you select the thumbs-down button, you can choose from the following feedback options:
+ **Inaccurate, not factually correct**
+ **Incomplete answer**
+ **Didn't understand my question**
+ **Issue with sources**
+ **Too wordy**
+ **Offensive or unsafe language**
+ **Other**

You can also copy conversation details from the feedback window for further troubleshooting.

## Artifact panel
<a name="artifact-panel"></a>

An *artifact* in AWS Quick is defined as any AWS Quick generated content produced using AWS Quick's underlying large language model's (LLM) generative capabilities, for example: contracts, email drafts, social media posts, tables, interactive charts, code blocks, or any AWS Quick visuals.

AWS Quick stores any artifacts it generates as responses during chat in an artifact panel. You can access any artifacts created during your chat by selecting **View more** from below the artifact in chat.

You can download artifacts as text, CSV, code files, Word documents, Excel spreadsheets, PowerPoint presentations, PDFs, and infographics. Saving artifacts to a Space is not currently supported.

For more information about creating and downloading documents and visuals, see [Create documents and business visuals](document-and-visual-creation.md).

## Conversation management
<a name="conversation-mgmt"></a>

AWS Quick stores conversations for up to 365 days, and you can access them in the left navigation pane. Retention can be longer on some plans. For more information, see [Usage limits](usage-limits.md). You can perform the following tasks to manage your conversations:
+ **Start a new conversation** – Choose **\+** from the chat controls menu to start a new conversation.
+ **View conversation history** – Choose the clock icon to view all conversation history for the last 365 days. You can filter conversation history to specific agents.
+ **Organize conversations into folders** – You can create, rename, and delete folders, and drag conversations between them. Automatic cleanup can sort conversations into folders by topic.
+ **Pin conversations** – You can pin important conversations to keep them at the top of your conversation history.
+ **Search conversations** – You can search across all of your conversations from the search control.
+ **Archive conversations** – You can archive conversations that you no longer need without deleting them.
+ **Route related discussions into threads** – Quick can route related discussions into organized threads, and you can reply in a thread to branch a sub-conversation from a specific message.

Your conversations are kept in your AWS Quick account and are available across the web, desktop, and mobile, so you can continue a conversation on any surface where you use Quick.

You can also revise and rerun the messages in a conversation:
+ **Edit and rerun** – You can edit one of your earlier messages and submit it again, and Quick generates a new response from the edited message.
+ **Retry** – You can ask Quick to generate a new response to your most recent message.
+ **Branch navigation** – When you edit a message or retry a response, Quick keeps each version as a separate branch, and you can use the branch controls to move between versions and compare responses.

The **Context used** indicator shows how much of the conversation context window is in use, and it fills as the conversation grows. To free context during a long session, choose **Summarize** to compact the conversation history, or start a new conversation.

**Note**  
Sharing conversations with other users is not supported.

## Response events
<a name="response-events"></a>

For every natural language prompt AWS Quick chat receives, it generates real-time processing steps while the request is being fulfilled. These steps can be viewed as part of **Response events** during response generation, and are also accessible once AWS Quick has finished generating a response. Response events vary based on the chat interaction you're having (whether you're chatting with a file you've uploaded or with a AWS Quick resource) and capture any rewrites to your response before it's finalized. A response event also includes the system generated identifiers for your conversation—you can copy and save the information for troubleshooting.

## Explanations
<a name="chat-explanations-summary"></a>

When you chat with dashboards and datasets, each answer includes an Explanation that shows how the model arrived at each numerical claim, including the data sources, assumptions, filters, calculations, and SQL queries that the model used. Instead of manually verifying each answer by finding the original source and re-creating the logic, you can directly see the model's assumptions at the click of a button.

When you open an Explanation, you can see the following components:
+ **Found data in** – Displays the dashboards, sheets, or datasets where the insight came from.
+ **Filters** – Lists dashboard filter values that were used to arrive at the answer.
+ **Assumptions** – Unpacks any large language model (LLM)-derived definitions from either the data directly or from world knowledge.
+ **Calculation explained** – Shows any calculations that the model performed to arrive at the answer, presented in both natural language and as a math formula.
+ **Generated SQL** (datasets only) – Displays the specific SQL query that produced each numerical claim.

For more information and examples, see [AWS Quick chat explanations](chat-explanations.md).

## Contextual awareness
<a name="contextual-awareness"></a>

AWS Quick chat is context aware. It registers the AWS Quick resource you're interacting with and scopes your chat automatically to the resource. This way, when you start chatting, the resource you're interacting with is already included as a knowledge source for your chat.

If you navigate to a specific AWS Quick resource during an on-going chat, and that resource supports chat, AWS Quick chat will automatically register your new context and ask you whether you want to chat with the specific resource you have navigated to. If you want to continue chatting in the mode you're in, you can choose to **Ignore** the message. Or you can choose **Yes** to focus your chat on the specific resource you're interacting with. If you do so, AWS Quick automatically scopes your chat interactions to the resource in context.

## Managing your preferences in AWS Quick
<a name="user-preferences"></a>

User Preferences in AWS Quick gives you control over how Quick looks, feels, and works for you. You can customize your chat experience, set a default chat agent, personalize how Quick interacts with you, and manage your memories — all from a single settings modal.

### Customizing your chat experience
<a name="customize-chat-experience"></a>

You can set your default chat panel to open in either expanded or collapsed mode. By default, Quick automatically remembers your last used setting. For example, if you expand the chat panel during a session, Quick updates your default so the panel opens expanded the next time you return. You can also manually set your preferred default at any time from the Preferences modal.

### Setting your default chat agent
<a name="default-chat-agent"></a>

You can choose a preferred chat agent that greets you each time you open Quick. In addition to selecting a default agent, you can pre-select a default knowledge scope for My Assistant. The available knowledge scope options are:
+ **All data and apps** – Quick searches across all your connected data sources and applications.
+ **General knowledge** – Quick responds using general knowledge only, without searching your connected data.
+ **Specific data and apps** – Quick searches only the data sources and applications you specify.

Your selected agent and knowledge scope are applied automatically each time you start a new conversation.

### Personalizing your experience
<a name="personalize-experience"></a>

You can let Quick know what to call you and share your area of focus at work. Quick uses this context to personalize responses and make your experience more relevant to your role and responsibilities.

### Managing your memories
<a name="manage-memories"></a>

You can view and manage your memories directly from Preferences. Memories are insights that Quick learns from your conversations, or that you tell it directly, to personalize future interactions. Memories are kept per agent, so you can review them for all agents, the default chat agent, or a specific custom agent.

In the Memories section, you can search, filter, and sort your memories. The filters cover the following:
+ **Agent** – View memories for all agents, the default chat agent, or a specific custom agent.
+ **Type** – Filter by memory category, such as procedures, preferences, and profile facts. The available categories vary.
+ **Provenance** – Show only Told memories, only Learned memories, or both.
+ **Sort** – Sort by date created, confidence, or how often a memory has been referenced.

Choose a memory to open its details, which include the memory text, when it was created and last used, its confidence, its type, its Told or Learned provenance, and a timeline that traces what Quick used to form it. Each memory provides the following actions:
+ **Boost** – Raise confidence in the memory to the highest level so Quick uses it first in future responses.
+ **Forget** – Remove the memory. You can choose a reason, such as Too specific, Never said this, or Outdated, so Quick avoids re-learning it.
+ **Edit** – Update the memory's text. Use edit to fix a fact instead of deleting and re-teaching it.

Memory settings include a main toggle that controls whether Quick learns from your conversations, and a Forget all memories action that deletes every saved memory. Forgetting all memories cannot be undone and does not affect your knowledge graph. For more information about your knowledge graph, see [Your knowledge graph and My context](knowledge-graph.md).

### Accessing User Preferences
<a name="access-user-preferences"></a>

To access and configure your preferences:

1. Go to the top-right corner of the AWS Quick homepage.

1. Choose your account name.

1. Select **Preferences** from the dropdown menu.

1. Make your changes across any of the available sections.

1. Choose **Save** to apply your changes, or choose **Cancel** to discard them.

## Deep research
<a name="deep-research"></a>

Deep research provides structured, multi-step investigation. When you start deep research, AWS Quick chat investigates your question across multiple sources and compiles the results into a comprehensive deliverable. A research plan card appears in the conversation and shows live progress as Quick gathers information, generates figures, and finalizes the report.

Deep research is useful for the following tasks:
+ You can run market research and competitive analysis.
+ You can explore a technical topic in depth.
+ You can carry out strategic planning and investigation.
+ You can explore a problem from multiple angles.

To start deep research, ask Quick to research a topic or perform a comprehensive investigation. To follow along while Quick works, choose **View research progress** on the research plan card.

## Running work in the background
<a name="background-work"></a>

While AWS Quick chat is responding, you can send the task to the background and keep working in another conversation. To send the current task to the background, choose the send-to-background control. The task continues to run, and Quick notifies you when it finishes.

You can also queue follow-up messages while Quick is working. Queued items show a count, and you can send them immediately or remove them.

To monitor longer-running and background agent work across your assistant, see [Monitor and manage agents and flows with Mission Control](mission-control.md).

## Chat features in the desktop app
<a name="desktop-app-chat"></a>

The following chat capabilities are available when you use AWS Quick in the desktop app.

### Local folders
<a name="chat-local-folders"></a>

In the desktop app, you can give the agent access to local folders so that it can read, write, or search their contents. To add a folder or view the folders you have already granted access to, choose the **Add context** icon in the chat input area, choose **Local folders**, and then choose **Manage folders**. Quick opens the **Knowledge** tab, where adding a folder works the same as adding one from **Customize** > **Knowledge**. For more information, see [Knowledge](knowledge.md).

### Plan mode
<a name="plan-mode"></a>

In the desktop app, you can use plan mode for complex, multi-step tasks. When you turn on plan mode, AWS Quick chat breaks your request into a structured plan with individual steps before it runs them. You can review and change the plan before Quick proceeds. The plan appears in a panel next to your conversation and as a plan card in the chat.

Plan mode is useful for tasks such as the following:
+ You can generate a document that spans multiple files.
+ You can run a complex data analysis workflow.
+ You can manage a multi-step research project.
+ You can refactor code at a large scale.

### Coding agent sessions
<a name="coding-agent-sessions"></a>

In the desktop app, you can use coding agents such as Kiro or Claude to accomplish coding tasks directly inside a conversation. Local code execution in the desktop app runs in an isolated sandbox that blocks common coding commands, so you delegate those tasks to a coding agent. For information about connecting a coding agent, see [Work with integrations in AWS Quick](working-with-integrations.md).

### Session tabs
<a name="session-tabs"></a>

In the desktop app, documents and artifacts open in session tabs alongside the conversation. In a session tab, you can view and edit a rendered document, turn on selection mode to select text, images, and tables and add them as context for your next prompt, and act on the open document. You can open a document, download it, add it to a space, share it, or open it in chat. Multiple documents can stay open as tabs at the same time.

### Incognito mode
<a name="incognito-mode"></a>

In the desktop app, you can use incognito mode when you want a private conversation that does not update your memory or history. In an incognito conversation, AWS Quick chat does not read from or write to your long-term memory or knowledge graph, and your responses are not personalized from past conversations. The conversation does not appear in your recent conversations, and it is discarded when you leave it.

Inside an incognito conversation, Quick still follows the current conversation from turn to turn, and it can still search files that you have already indexed. It does not remember anything after you leave the conversation.

To start an incognito conversation, choose the **Incognito** control at the top right of the chat surface. A private-mode indicator appears while incognito mode is active.

**Note**  
Privacy is locked once a chat has messages, so turn on incognito mode before you begin. When you leave an incognito conversation, its contents are deleted and nothing is retained. If your administrator has set up chat log delivery, Quick still delivers incognito conversations to the log destination.

### Away From Keyboard (AFK) recap
<a name="afk-recap"></a>

In the desktop app, when you step away during a long-running task and return, AWS Quick chat shows an away-from-keyboard (AFK) recap. The recap summarizes what happened while you were away, so you can catch up quickly without scrolling through the full conversation. This recap is specific to a task running in the current conversation. For a summary of activity across your connected services while you were away, see [Stay on top of your work with your proactive feed](working-with-feed.md).

### Exporting a conversation
<a name="export-conversation"></a>

In the desktop app, you can export an entire conversation to share it or keep a record. To export the current conversation, use the **/export** command or the export action, and then choose **Markdown** or **PDF**.