

# Working with chat
<a name="working-with-chat-desktop"></a>

Chat is the primary way you interact with Amazon Quick on desktop. You can ask questions, get help with tasks, analyze files, create documents, generate visualizations, and work with your connected services through natural language. The following sections describe the chat features available in the desktop application.

## Response preferences
<a name="desktop-response-preferences"></a>

Amazon Quick on desktop provides multiple response modes that you choose based on your task. To switch between modes, use the response preferences selector in the chat input area.


| Mode | Description | Best for | 
| --- | --- | --- | 
| Fast | Optimized for speed on everyday tasks. Responses are generated quickly with the lowest latency. | Quick questions and simple tasks where speed matters more than depth. | 
| Balanced | Balances quality and speed. Provides high-quality responses with moderate latency. | Most tasks, including writing assistance, summarization, and general day-to-day work. | 
| Smart | Highest-quality responses. Provides the most thorough reasoning, with longer response times. | Complex analysis, nuanced writing, detailed reasoning, and tasks that require high accuracy. | 

### Thinking effort
<a name="desktop-thinking-effort"></a>

You control the thinking effort independently from the response mode. Thinking effort determines how much reasoning Quick applies before it responds. Higher thinking effort enables deeper reasoning for complex code, strategic planning, and analysis.


| Level | Description | 
| --- | --- | 
| Off | No extended reasoning. Quick responds directly. | 
| Low | Minimal reasoning before responding. | 
| Medium | Moderate reasoning. A good balance for most tasks. | 
| High | Extended reasoning for complex problems. | 

You can set thinking effort on Balanced and Smart modes. Fast mode responds without extended reasoning. To change the thinking effort, choose the response preferences selector in the chat input area, and then adjust the thinking effort picker.

## Chat input
<a name="desktop-chat-input"></a>

You enter your messages in the chat input area at the bottom of the conversation. From the chat input area, you can attach files, add local folders, turn on web search, attach a space, run commands, and mention agents and items. To open the menu of context options, choose the \+ (Add context) icon.

### Attachments and file uploads
<a name="desktop-attachments"></a>

You can attach files directly to your chat messages for Quick to analyze, summarize, or reference. The desktop application supports common file types, including documents, spreadsheets, presentations, images, PDF files, and code files.

To attach a file, use one of the following methods.
+ Choose the \+ (Add context) icon in the chat input area, and then choose Upload files.
+ Drag and drop a file directly into the chat window.

Each attachment can be up to 50 MB. When you attach a file, Quick can read, analyze, and reference the file contents in its responses.

### Local folders
<a name="desktop-chat-local-folders"></a>

You can give the agent access to local folders for it to read, write, or search their contents. To add a folder or view the folders you have already granted access to, choose the \+ (Add context) icon in the chat input area, choose Local folders, and then choose Manage folders. This opens the Knowledge tab in Customize, where adding a folder works the same as choosing **Customize > Knowledge** and adding a folder there. For more information, see [Knowledge](knowledge-desktop.md).

### Web search
<a name="desktop-chat-web-search"></a>

You can turn on web search to allow Quick to search the internet for up-to-date information when it responds to your messages. When web search is on, Quick can retrieve current information from the web to supplement its responses.

To turn web search on or off, choose the \+ (Add context) icon in the chat input area, and then choose Web search. When web search is on, Quick includes citations from the web sources it references in its responses.

### Spaces
<a name="desktop-chat-spaces"></a>

You can attach a space to your conversation to give Quick access to shared team knowledge. Spaces contain curated collections of information that your team maintains in Amazon Quick. While it is attached, Amazon Quick answers from the content in that space and does not reach outside it on its own, so the conversation works within a narrow, scoped context for confidentiality or data compliance. This applies to everything in the space, including its files, datasets, dashboards, topics, and actions.

This is useful when you need answers grounded in your team's shared context, such as the following.
+ Project documentation
+ Company policies and procedures
+ Domain-specific knowledge bases
+ Team wikis and reference materials

If the answer is not in the attached space, Quick tells you so rather than answering from somewhere else. Ask Quick to search more broadly and it will, for the rest of that conversation until you change it again. A space you attach applies to that conversation only. Starting a new conversation starts with nothing attached, so you never inherit context from work you have already finished.

To attach a space, choose the \+ (Add context) icon in the chat input area, choose Spaces, and then select the space you want to use.

### Slash commands
<a name="desktop-slash-commands"></a>

You can run commands directly from the chat input area. To open the command menu, type a forward slash (/) at the start of your message, and then choose a command or continue typing to filter the list.


| Command | Description | 
| --- | --- | 
| /clear | Start a new conversation with fresh context. Your current chat is saved separately, not lost. | 
| /compact | Condense the current conversation to free up context. | 
| /export | Export the conversation as Markdown or PDF. | 
| /mode | Switch the response mode (Fast, Balanced, Smart) and thinking level (Off, Low, Medium, High). | 
| /rename | Rename the current conversation. | 
| /copy | Copy the most recent response. | 
| /skills | View the available skills. | 
| /connectors | View and manage your connectors. | 
| /goal | Give the agent a job to finish rather than a single question to answer. In a normal chat, it replies once and waits for you. With /goal, it keeps working on its own until the job is complete, double-checks its own work, and only then hands it back. | 
| /help | View the list of available commands. | 

### Mentions
<a name="desktop-mentions"></a>

To reference a specific agent, an item in your message, or people from your knowledge graph, type an at sign (@), and then choose from the list that appears. Mentions let you direct your request to a particular agent or person, or point Quick to a specific item, without leaving the chat input area.

## Citations and sources
<a name="desktop-citations-sources"></a>

When Quick uses information that is not part of model knowledge to answer a question, it cites where that information came from. Citations help you verify a response and explore the underlying sources.
+ Inline citations: Quick adds citation markers within its response. Choose a citation to open its source, such as a web page, a file, context, or a connected application.
+ Sources: Quick shows a Sources summary with the full set of sources that informed a response. Sources can include web pages, files, connected data, and the memories that shaped the response.

For responses informed by your memory, the Sources panel shows the memories that were used. You can boost the memories that were helpful or remove the ones that were not.

## Managing messages
<a name="desktop-managing-messages"></a>

You can revise and rerun the messages in a conversation.
+ Edit and rerun: edit one of your earlier messages and submit it again. Quick generates a new response from the edited message.
+ Retry: ask Quick to generate a new response to your most recent message.
+ Branch navigation: when you edit a message or retry a response, Quick keeps each version as a separate branch. Use the branch controls to move between the previous and next versions and compare responses.

Each message also supports inline actions. On a message you sent, you can copy it, edit it, or reply in a thread. Messages can carry emoji reactions, shown as a row of reaction pills. In a read-only transcript, copy remains available while edit and reply are hidden, and reply is not offered inside a thread.

## Running work in the background
<a name="desktop-background-work"></a>

While Quick is responding, you can send the task to the background and keep working in another conversation. To send the current task to the background, choose the send-to-background control, or press Ctrl\+B (Windows) or Cmd\+B (macOS). The task continues to run, and Quick notifies you when it finishes.

You can also queue follow-up messages while Quick is working. Queued items show a count and can be sent immediately or removed.

## Coding agent sessions
<a name="desktop-coding-agent-sessions"></a>

You can use coding agents such as Kiro, Claude, or other connected agents to accomplish coding tasks directly inside a conversation. The desktop application's local code execution runs in an isolated sandbox that blocks common coding commands, so you delegate those tasks to a coding agent. For information about connecting a coding agent, see [Connectors](connections-desktop.md).

## Plan mode
<a name="desktop-plan-mode"></a>

For complex, multi-step tasks, you can use plan mode. When you turn on plan mode, Quick breaks your request into a structured plan with individual steps before it executes. You can review and modify the plan before Quick proceeds with each step. The plan appears in a panel next to your conversation and as a plan card in the chat.

Plan mode is useful for tasks such as the following.
+ Multi-file document generation
+ Complex data analysis workflows
+ Multi-step research projects
+ Large-scale code refactoring

## Deep research
<a name="desktop-deep-research"></a>

Deep research provides structured, multi-step investigation. When you start deep research, Quick investigates your question across multiple sources and compiles the results into a comprehensive deliverable. A research plan card appears in the conversation and shows live progress as Quick gathers information, generates figures, and finalizes the report.

Deep research is useful for the following tasks.
+ Market research and competitive analysis
+ Technical topic deep dives
+ Strategic planning and investigation
+ Multi-angle problem exploration

To start deep research, ask Quick to research a topic or perform a comprehensive investigation. To follow along while Quick works, choose View research progress on the research plan card.

## Incognito mode
<a name="desktop-incognito-mode"></a>

Use incognito mode when you want a private conversation that does not update your memory or history. In an incognito conversation, Quick does not read from or write to your long-term memory or knowledge graph, and your responses are not personalized from past conversations. The conversation does not appear in Recents, and it is discarded with nothing retained when you leave it.

Inside an incognito conversation, Quick still follows the current conversation from turn to turn, and it can still search files that you have already indexed. It does not remember anything after you leave the conversation.

To start an incognito conversation, choose the Incognito control at the top right of the chat surface. A private-mode indicator appears while incognito is active.

**Note**  
Privacy is locked once a chat has messages. Turn on incognito before you begin. When you leave an incognito conversation, its contents are deleted and nothing is retained.

## Managing conversation context
<a name="desktop-context-meter"></a>

The Context used indicator shows how much of the conversation context window is in use. As the conversation grows, it fills. To free context during a long session, choose Summarize to compact the conversation history, or start a new conversation.

## Away From Keyboard (AFK) recap
<a name="desktop-afk-recap"></a>

When you step away during a long-running task and return, Quick shows an away-from-keyboard (AFK) recap. The recap summarizes what happened while you were away, so you can catch up quickly without scrolling through the full conversation. This recap is specific to a task running in the current conversation. For a summary of activity across your connected services while you were away, see the feed catch-up in [Activity feed](activity-feed-desktop.md).

## Managing conversations
<a name="desktop-managing-conversations"></a>

Quick keeps your conversation history in your Amazon Quick account, so it is available to you across the web, mobile, and desktop. You can organize, search, and manage your conversations with the following features.
+ Folders: organize your conversations into folders. You can create, rename, and delete folders, and drag conversations between them. Auto-clean up sorts chats into folders by topic.
+ Pinning: pin important conversations to keep them at the top of your chat history.
+ Search: search across all of your conversations from the search control in the sidebar.
+ Archive: archive conversations that you no longer need without deleting them.
+ Thread routing: Quick can route related discussions into organized threads for structured conversations, and you can reply in a thread to branch a sub-conversation from a specific message.

Your conversation history appears in the Recents section of the sidebar, organized by date.

## Creating documents and visuals
<a name="desktop-creating-documents-visuals"></a>

Quick generates documents directly from chat, including presentations (`.pptx`), Word documents (`.docx`), spreadsheets (`.xlsx`), PDF files, Markdown, and HTML, along with interactive data visualizations. Describe what you need. For example, "Create a presentation about our quarterly results." Generated items appear as artifacts that you can save locally or to your Library. For detailed information about supported formats, editing, visualizations, and best practices, see [Document and visual creation with Amazon Quick](document-and-visual-creation.md).

Quick can also generate and edit images from a text description. Generated images appear as artifacts you can save locally or add to a space.

## Session tabs
<a name="desktop-session-tabs"></a>

Documents and artifacts open in session tabs alongside the conversation. In a session tab you view and edit a rendered document, turn on selection mode to select text, images, and tables and add them as context for your next prompt, and act on the open document (open, download, add to a space, share, or open in chat). Multiple documents can stay open as tabs at once.

## All data and apps
<a name="desktop-all-data-and-apps"></a>

The All data and apps panel shows the spaces, local folders, and skills available to the current conversation, so you can add or adjust the resources the agent draws on. Skills show a status indicator.

## Exporting a conversation
<a name="desktop-exporting-conversation"></a>

You can export an entire conversation to share it or keep a record. To export the current conversation, use the /export command or the export action, and then choose Markdown or PDF.