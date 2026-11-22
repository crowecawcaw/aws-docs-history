

# Custom memories

You can create your own memory stores for the knowledge that matters to a team, a service, or a recurring problem. For example, a store can hold the procedures your team follows for a routine task, your runbooks and postmortems, or the context behind a report you produce every week. Agents use a custom store the same way they use a managed store. They read the store's description during a task, and when the store matches, they open the memories they need. For more information about how agents read memories, see [DevOps Agent Memories](about-aws-devops-agent-devops-agent-memories-index.md).

Custom stores count toward the same limits as managed stores. For more information about the limits on memory stores and memories, see [Quotas](quotas.md).

## Creating a memory store
<a name="creating-a-memory-store"></a>

Give each store a name and a description. Agents use the description to decide when to open the store, so write it with care. You can create a memory store in the console or through Chat.

**To create a memory store (console):**

1. On the **Knowledge** page in the DevOps Agent web app, choose the **Memories** tab.

1. Choose **Add store**.

1. In **Create memory store**, enter a name and a description, and then choose **Create store**.

**To create a memory store (Chat):**

Ask AWS DevOps Agent. For example:
+ "Create a memory store named payments-runbook that holds standing guidance for investigating the payments service."
+ "Create a memory store named operational-procedures that holds the standard runbooks for our routine maintenance tasks."
+ "Create a memory store named weekly-report-context with the sections, sources, and format our weekly operations report should follow."

## Writing effective descriptions
<a name="writing-effective-descriptions"></a>

Agents decide whether to open a store or a memory from its description, before they read anything inside it. When you import files with Chat, Chat proposes a description for each memory and each new store in its plan, and you review them before it saves anything. When you create a store through Chat, Chat drafts the store's description for you. You write a description yourself only when you create a store in the console or upload a memory file.

A good description states what the store or memory holds and when agents should use it. For example:
+ **Too vague:** "Payments notes."
+ **Effective:** "Standing runbooks, known issues, and escalation contacts for the payments service. Read when investigating checkout, billing, or refund incidents."

A description can be up to 1,024 characters. If agents don't use a store that you expect them to use, improve its description first. You can also ask Chat to rewrite it.

## What to put in a memory store
<a name="what-to-put-in-a-memory-store"></a>

Put lasting knowledge in a memory store: facts about your environment, recurring root causes, conventions and directives, and the findings and summaries from past work. Store the conclusion that is worth recalling later, not the raw data behind it.

A memory store doesn't hold working notes for a single investigation, and it doesn't cache a tool's output. During an investigation, the agent already keeps tool output in its working context, so you can't save a raw result to a store and read it back later in the same investigation. Record the fact that the result established instead, such as "The checkout service calls the payments API synchronously." Agents can reuse that fact in later sessions.

For the best results:
+ Keep each memory to one fact or lesson, so agents can read exactly what they need.
+ Store what stays true across investigations. Leave one-time working data in the investigation that produced it.

## Adding knowledge from your own sources
<a name="adding-knowledge-from-your-own-sources"></a>

Your team likely keeps operational knowledge elsewhere already, such as runbooks, postmortems, design docs, or a wiki. You can bring it into a custom memory store in three ways:
+ [Upload memory files](#uploading-memory-files) that are already in the memory format.
+ [Import other files with Chat](#importing-files-with-chat), which converts them into memories.
+ [Keep a store in sync with a source](#syncing-a-source-with-a-custom-agent) by running a custom agent, such as the Confluence memory sync agent.

### Uploading memory files
<a name="uploading-memory-files"></a>

You can upload Markdown files that are already in the memory format into a custom store. Each file starts with a frontmatter block that sets `name` and `description`. The `metadata` and `claim` fields are optional. The `name` is the memory's path in the store. Use lowercase words separated by hyphens, and use `/` to place the memory in a folder. For example:

```
---
name: services/payments-api
description: Runbook for the payments API. Read when investigating checkout or payment failures.
claim:
- id: C1
  text: The payments API retries a declined card once before it returns an error.
  provenance:
  - note: From the payments team runbook.
    source:
    - {}
---
The payments API retries a declined card once before it returns an error.
Escalate sustained 5xx errors to the payments on-call engineer.
```

A *claim* is one fact in the memory, with a note on where it came from. Agents use claims to cite a memory's facts, and the learning agent uses them to keep facts current one at a time. When you include claims, give each one an `id`, its `text`, and a `provenance` list. When you upload a file, AWS DevOps Agent records your upload as each claim's source.

**To upload memory files:**

1. On the **Memories** tab of the **Knowledge** page, open the custom store that you want to add to.

1. Choose **Upload memories**. You can upload only to custom stores.

1. Add up to 20 files, and then choose **Review**. Memory files (`.md`, up to 100 KB) upload as they are, and other files go to Chat.

1. Review the plan. The plan marks each file as **New**, **Updates existing**, **For Chat** (not in the memory format), or **Error** (a problem such as a name that another file in the upload already uses). A file whose name matches an existing memory in the store updates that memory as a new version, and the earlier version stays in its history. The upload skips files marked **For Chat** or **Error** and shows the reason for each.

1. Choose **Upload *N* memories**. Agents use the new memories from their next run.

If some uploads fail, choose **Retry failed** to send only those files again. If some files aren't in the memory format, choose **Fix *N* files in Chat**, and Chat converts them into memories for the store.

To replace a single memory with a new file, open the memory, choose its **⋯** menu, and then choose **Update memory**. The file must use the memory format and keep the memory's name. The previous version stays in the memory's history.

### Importing files with Chat
<a name="importing-files-with-chat"></a>

Chat can convert files that aren't in the memory format into memories. It accepts notes, docs, runbooks, and postmortems in Markdown, PDF, Word, Excel, CSV, HTML, text, JSON, YAML, logs, code, and images. Chat turns each file into one or more memories and suggests a store for each, or a new store. Chat saves nothing until you confirm its plan.

Chat saves memories only to custom stores, never to `directives` or another managed store. It splits a long file into several memories, named `<name>/part-1`, `<name>/part-2`, and so on. A new store that Chat creates counts toward your memory store limit.

**To import files with Chat:**

1. On the **Memories** tab of the **Knowledge** page, in the **Custom memory stores** section, choose **Import memories with Chat**.

1. Add up to 20 files of up to 3.75 MB each. You can add up to 5 PDF, Word, or Excel files at a time.

1. Choose **Continue in Chat**.

1. Review the name, description, and store that Chat proposes for each memory. Confirm the plan, or ask Chat to change it.

To change an existing memory through Chat, open the memory, choose its **⋯** menu, and then choose **Edit with Chat**.

### Syncing a source with a custom agent
<a name="syncing-a-source-with-a-custom-agent"></a>

To keep a store current as a source changes, run a custom agent on a schedule that reads the source and writes to the store. The Confluence memory sync agent does this for a Confluence Cloud page tree or space. It turns each operational page into one memory, places the memories in folders that match the Confluence tree, and keeps an `overview` memory that lists the synced pages. Later runs update only the pages that changed. The agent reads Confluence and never changes it.

**Prerequisites:**
+ The Atlassian MCP server (`https://mcp.atlassian.com/v2/mcp`), connected to your Agent Space as an MCP server. The agent can read only the pages that the connected identity can read. For more information, see [Connecting MCP Servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md).
+ A custom memory store for the synced pages. Use one store for each Confluence tree.

**To create the Confluence memory sync agent from its template:**

1. On the **Agents** page, in the **Custom agents** section, open Chat. Under **Start from a template**, choose **Sync Confluence into memory**. Or ask Chat directly, for example: `Set up the confluence-memory-sync custom agent from its template.`

1. Chat checks for the Atlassian MCP tools and a memory store, helps you set up anything that's missing, and creates the `confluence-memory-sync` custom agent.

1. Run the agent with a prompt that names the Confluence URL and the store. For example:

``` Sync https://example.atlassian.net/wiki/spaces/ENG/pages/123456/Runbooks into the eng-runbooks memory store. ```

Each run reads pages for up to 45 minutes, so a large tree takes several runs. Each run's report states how many pages are still pending. To finish a large tree and keep the store current, add a scheduled trigger with the same prompt. A store holds up to 200 memories, so one store holds up to 198 synced pages plus the `overview` and `sync-state` memories. To sync a larger tree, split it into smaller trees, each with its own store.

You can also create the agent by importing its system prompt from the [AWS DevOps Agent Tools repository](https://github.com/aws/tools-for-devops-agent/tree/main/custom-agents/confluence-memory-sync) on the GitHub website. For more information, see [Importing a custom agent from a repository](custom-agents-creating-a-custom-agent.html#importing-a-custom-agent-from-a-repository).

## Deleting a memory store
<a name="deleting-a-memory-store"></a>

You can delete a custom memory store that you no longer need. You can't delete a managed store.
+ **In Chat:** Chat doesn't delete a store that still contains memories. It asks you to delete the memories first. Delete the memories, and then delete the store.
+ **In the console:** Deleting a store also deletes every memory in it. You can't undo this, so confirm that you chose the right store.

To delete a store in Chat, ask AWS DevOps Agent. For example:

```
Delete the network-quirks memory store.
```