

# System tools
<a name="system-tools-desktop"></a>

Amazon Quick on desktop includes built-in system tools that provide core capabilities such as web search, file operations, browser automation, image generation, and code execution. You enable or disable each tool individually and configure granular permission controls. Manage system tools in **Customize**, on the **Connectors** tab.

## Managing permissions
<a name="desktop-settings-manage-permissions"></a>

In the connectors table, each system tool has an enable/disable toggle and an actions menu. Choose the ellipsis (actions menu), and then choose **Manage permissions** to set the tool's access level and adjust its per-operation permissions. To turn a tool on or off, use its enable/disable toggle.

### Access levels
<a name="system-tools-access-levels"></a>

You set one of three access levels:


| Access level | Description | 
| --- | --- | 
| Always Allow | Quick has full read and write access to this tool. Operations run without prompting you for confirmation. | 
| Ask Each Time | Quick asks for your confirmation before performing any operation with this tool. | 
| Always Deny | Quick cannot perform any operation with this tool. | 

Below the access level, each tool lists its operations grouped into read and write, and you set each independently, for example Always Allow overall but a specific write operation set to Ask Each Time.

**To manage permissions for a tool**

1. Choose **Customize** in the navigation, and then choose the **Connectors** tab.

1. Find the system tool in the connectors table, choose the ellipsis (actions menu), and then choose **Manage permissions**.

1. Set the access level, and adjust individual operation permissions.

1. Close the panel. Changes take effect immediately.

## System tool permissions
<a name="desktop-security-tool-permissions"></a>

Amazon Quick on desktop uses the same access levels for system tools, for connectors to third-party services such as Slack, Microsoft Outlook, and Gmail, and for local tools that run on your computer. You can turn each one on or off and set each operation to **Always Allow**, **Ask Each Time**, or **Always Deny**.

Quick stores your permission choices and applies them whenever an agent acts on your behalf, including scheduled agents. An agent can take only the actions that you allow, and you can review or change these permissions at any time.

## Available system tools
<a name="system-tools-available"></a>

The built-in system tools include:
+ Web Search: find current information from the internet through search and fetch-URL operations, with citations.
+ File operations: download files from URLs and open local files in their default applications.
+ Browser Automation: launch a browser, navigate, interact with elements, fill forms, take screenshots, and extract text. It supports a default mode, which uses a separate browser instance with a copy of your profile, and a use-your-own-browser mode.
+ Image Generation: generate and edit images with Amazon Nova Canvas, including remove background, variations, and outpaint (extending an image beyond its original boundaries).
+ Engram Builder: analyze your writing across messages and conversations to build a personality profile (an engram), so Quick can write in your style. Operations: get, list, save, and delete engrams.
+ Knowledge and memory: query and build the knowledge graph, and recall learned patterns.
+ Agent management: create, update, delete, and trigger routines from chat.
+ Task management: break complex requests into parallel background sub-tasks, organized into groups, with progress tracking.
+ Chat and notifications: surface contextual suggestion pills, message reactions, desktop notifications for events such as task completion, and briefing summaries on the Home screen.
+ Transcription: convert audio and video files to text so Quick can summarize, quote, or answer questions about their contents. The Transcribe media operation transcribes an audio or video file (for example, .mp3, .mp4, .wav, .flac, .m4a, or .ogg) to text. Use it when you want Quick to work with recordings such as meeting captures, voice memos, screen recordings, podcast clips, or interview audio as if they were text.
+ Explainability: produce a structured account of how Quick arrived at its answer. The Emit explanation operation returns an explanation that includes assumptions (what Quick took as given), sources (which datasets, files, connectors, or memories were consulted), calculations (the steps that produced the result), and limitations (known caveats or places where the answer is uncertain). Use it when you want to see the reasoning behind an answer, share it, or check the assumptions before acting.
+ File indexing and search: find and cite content across the folders you have granted access to. Operations include Search files (search across indexed files by keyword or meaning), Read document (return the full content of a specific file), Check indexing (report indexing status for a folder or file), and Approve indexing (approve or skip a pending indexing operation). For how folders are indexed, see [Knowledge](knowledge-desktop.md).
+ Working with your data: answer questions in natural language about the datasets and dashboards you connect through Quick spaces. Quick can answer questions from datasets (run analytical queries and return an answer with the underlying data), read dashboards (interpret and summarize the data behind a dashboard visual), and discover data (browse the catalog of datasets and dashboards available to you). Which datasets and dashboards Quick can see depends on your organization's permissions.

All system tools are turned on by default, with write operations set to **Ask Each Time**. You can restrict or turn off any tool at any time. Changes take effect immediately, in existing and new conversations and agent runs. For information about the controls that administrators set, see [Administrator and user controls](desktop-security.md#desktop-admin-user-controls).

### Code execution
<a name="system-tool-code-execution"></a>

The Code Execution tool writes and runs Python in a sandbox for data analysis, calculations, file processing, chart generation, and automation. A persistent namespace carries variables across runs within a conversation, and pre-installed packages are available. Sandbox file access follows your folder permissions, plus system temporary directories.