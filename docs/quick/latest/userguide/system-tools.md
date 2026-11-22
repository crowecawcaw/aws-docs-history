

# Built-in system tools

AWS Quick includes built-in system tools that provide core capabilities such as web search, file operations, browser automation, image generation, and code execution. You turn each tool on or off individually and configure granular permission controls.

## Managing permissions
<a name="system-tools-web-permissions"></a>

Each system tool has an on/off toggle and an actions menu. Choose the ellipsis (actions menu), and then choose **Manage permissions** to set the tool's access level and adjust its per-operation permissions. To turn a tool on or off, use its toggle.

### Access levels
<a name="system-tools-web-access-levels"></a>

You set one of three access levels:


| Access level | Description | 
| --- | --- | 
| Always allow | Quick has full read and write access to this tool. Operations run without prompting you for confirmation. | 
| Ask each time | Quick asks for your confirmation before performing any operation with this tool. | 
| Always deny | Quick cannot perform any operation with this tool. | 

Below the access level, each tool lists its operations grouped into read and write, and you set each independently, for example **Always allow** overall but a specific write operation set to **Ask each time**.

**To manage permissions for a tool**

1. Find the system tool, choose the ellipsis (actions menu), and then choose **Manage permissions**.

1. Set the access level, and adjust individual operation permissions.

1. Close the panel. Changes take effect immediately.

## System tool permissions
<a name="system-tools-web-tool-permissions"></a>

AWS Quick uses the same access levels for system tools and for connectors to third-party services. You can turn each one on or off and set each operation to **Always allow**, **Ask each time**, or **Always deny**.

Quick stores your permission choices and applies them whenever an agent acts on your behalf, including scheduled agents. An agent can take only the actions that you allow, and you can review or change these permissions at any time.

## Available system tools
<a name="system-tools-web-available"></a>

The built-in system tools include:
+ Web Search: find current information from the internet through search and fetch URL operations, with citations. These requests run in the AWS Quick agent runtime and reach the internet from AWS-managed infrastructure. Fetch URL can return a cached copy of a page.
+ File operations: download files from URLs. Downloads from URLs run in the AWS Quick agent runtime, which retrieves the file and makes it available in your conversation.
+ Browser Automation: launch a browser, navigate, interact with elements, fill forms, take screenshots, and extract text. Remote managed browser automation runs a browser in the AWS Quick agent runtime and reaches the internet from AWS-managed infrastructure.
+ Image Generation: generate and edit images with Amazon Nova Canvas, including remove background, variations, and outpaint (extending an image beyond its original boundaries).
+ Engram Builder: analyze your writing across messages and conversations to build a personality profile (an engram), so Quick can write in your style. Operations: get, list, save, and delete engrams.
+ Knowledge and memory: query and build the knowledge graph, and recall learned patterns.
+ Agent management: create, update, delete, and trigger routines from chat.
+ Task management: break complex requests into parallel background sub-tasks, organized into groups, with progress tracking.
+ Chat and notifications: surface contextual suggestion pills, message reactions, notifications for events such as task completion, and briefing summaries.
+ Transcription: convert audio and video files to text so Quick can summarize, quote, or answer questions about their contents. The Transcribe media operation transcribes an audio or video file (for example, .mp3, .mp4, .wav, .flac, .m4a, or .ogg) to text. Use it when you want Quick to work with recordings such as meeting captures, voice memos, screen recordings, podcast clips, or interview audio as if they were text.
+ Explainability: produce a structured account of how Quick arrived at its answer. The Emit explanation operation returns an explanation that includes assumptions (what Quick took as given), sources (which datasets, files, connectors, or memories were consulted), calculations (the steps that produced the result), and limitations (known caveats or places where the answer is uncertain). Use it when you want to see the reasoning behind an answer, share it, or check the assumptions before acting.
+ Knowledge search: find and cite content across the knowledge bases and spaces you have access to. Operations include searching across indexed content by keyword or meaning, reading the full content of a specific file, and reporting indexing status.
+ Working with your data: answer questions in natural language about the datasets and dashboards you connect through Quick spaces. Quick can answer questions from datasets (run analytical queries and return an answer with the underlying data), read dashboards (interpret and summarize the data behind a dashboard visual), and discover data (browse the catalog of datasets and dashboards available to you). Which datasets and dashboards Quick can see depends on your organization's permissions.

All system tools are turned on by default, with write operations set to **Ask each time**. You can restrict or turn off any tool at any time. Changes take effect immediately, in existing and new conversations and agent runs.

### Code execution
<a name="system-tool-web-code-execution"></a>

The Code Execution tool writes and runs Python or JavaScript in a sandbox. Each language comes with a set of pre-installed libraries, and Quick can use them for any task they support. A persistent namespace carries variables across runs within a conversation.