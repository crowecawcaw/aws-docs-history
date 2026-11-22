

# DevOps Agent Memories

Memories hold the facts AWS DevOps Agent knows about your Agent Space, such as the recurring root causes of an alarm or how your services connect. Agents read the memories that match their task, so they spend fewer steps rediscovering your environment during an investigation. Memories differ from [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills-index.md). A skill is a procedure that you give the agent. A memory is what the agent has learned or been told, from facts about your environment to lessons about how to use its tools.

## What are memories
<a name="what-are-memories"></a>

A *memory* is a single Markdown file that records one piece of knowledge about your Agent Space. Examples include the recurring root causes of an alarm, a known quirk in your environment, or how your team prefers to receive answers.

Each memory is versioned. Every update creates a new version, and earlier versions stay available, so you can see how a memory changed over time.

A *memory store* groups related memories by topic. Each store has a name and a description, and agents read the description to decide whether to open it.

Stores come from two places, and agents use both kinds the same way:
+ **Managed stores:** AWS DevOps Agent creates and maintains these as it learns from activity in your Agent Space. For more information, see [Managed memories](devops-agent-memories-managed-memories.md).
+ **Custom stores:** You create these for the knowledge that matters to a team, a service, or a recurring problem. You can fill them by hand, upload files, import files with Chat, or sync them from a source such as Confluence. For more information, see [Custom memories](devops-agent-memories-custom-memories.md).

### How memories differ from skills and agent instructions
<a name="how-memories-differ-from-skills-and-agent-instructions"></a>

Choose where to put knowledge by what you want the agent to do with it:
+ **Agent instructions** are rules that you write for every session. For example: "Start every investigation by querying the service's CloudWatch Logs for errors in the 30 minutes before the alarm fired." The agent loads instructions at the start of every session. For more information, see [Agent instructions](about-aws-devops-agent-agent-instructions.md).
+ **Skills** are procedures that you write or import, which the agent follows when they apply to the task, such as the steps to investigate Amazon RDS latency. For more information, see [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills-index.md).
+ **Memories** are facts and lessons that the agent uses when they apply to the task, such as a monitor's recurring root causes or a query pattern that worked in past investigations. The learning agent writes most memories, and you can add your own.

The agent reads a skill or a memory only when it applies to the task, but it follows agent instructions in every session. Put a rule that must always apply in agent instructions.

## How agents find memories
<a name="how-agents-find-memories"></a>

When a session starts, the agent receives the name and description of each store, but not what's inside. From there, it finds what it needs in three ways:
+ **Browsing:** The agent compares its task with each store's description. When a store matches, it reads the descriptions of the memories inside and opens only the ones that match.
+ **Searching:** When the agent doesn't know which store holds what it needs, it searches your memories by meaning, then opens the closest matches. For more information, see [Searching memories](#searching-memories).
+ **Following relationships:** After the agent reads a memory, it can open the ones linked to it. For more information, see [Knowledge graph](#knowledge-graph).

Browsing and searching both work from names and descriptions, and the agent reads a memory's content only when it opens it. This keeps the agent's context small while all of your memories stay within reach, and it's why a specific description matters. For more information about writing descriptions, see [Writing effective descriptions](devops-agent-memories-custom-memories.html#writing-effective-descriptions).

## Knowledge graph
<a name="knowledge-graph"></a>

AWS DevOps Agent links related memories across your stores into a *knowledge graph*. Each link in the graph is a *relationship*, which connects two memories and records why they are related and the evidence for it. For example, a relationship can connect two alarms that fired during the same incident, a monitor and the upstream component that caused its alarms, or an alarm and a reflection on a past mistake. When an agent reads a memory, it can follow these links to the connected ones.

The learning agent builds and refreshes the knowledge graph. For more information, see [Build knowledge graph](devops-agent-memories-managed-memories.html#build-knowledge-graph). For more information about browsing the graph, see [Viewing memories and the knowledge graph](#viewing-memories-and-the-knowledge-graph).

## Searching memories
<a name="searching-memories"></a>

Search on the **Memories** tab looks at the name and description of each store and memory, not at their content. Each search runs two kinds of matching at once:
+ **Text match:** Finds stores and memories whose name or description contains the exact text you typed. Matching isn't case sensitive. Search treats your query as plain text, so wildcards and regular expressions don't work.
+ **Semantic match:** Finds memories whose name or description is close in meaning to your query, even when it uses different words. For example, `cart pods keep running out of memory` can find a memory named `checkout/pod-eviction`.

Results appear in one list, with text matches first and semantic matches after them. Words from your query are highlighted wherever they appear in a result. A semantic match can have no highlighted words, because it matched by meaning rather than by wording. Each memory in the results shows its store and whether that store is **Managed** or **Custom**.

**To search memories:**

1. On the **Knowledge** page in the DevOps Agent web app, choose the **Memories** tab.

1. In **Search memory stores**, enter at least three characters. To find a memory whose name you know, type part of the name. To find a memory when you don't know its name, describe the problem in a few words, such as `checkout latency spikes at night`.

1. Choose a result to open it. If there are more than 10 results, choose **Show more**.

To search one store, open the store and enter your query in **Find memories**. The results keep the store's folders, with the best matches at the top: text matches first, then semantic matches. Folders open to show every result, and the memory you have open stays open.

Agents use the same semantic search during their work.

## Viewing memories and the knowledge graph
<a name="viewing-memories-and-the-knowledge-graph"></a>

You view stores and their contents on the **Knowledge** page in the DevOps Agent web app.

**To view memories:**

1. On the **Knowledge** page, choose the **Memories** tab. Each store shows its name, description, and agent type scope.

1. Choose **View** next to a store. The store page lists its memories in folders, with each one's name, description, version number, and last modified date.

1. Choose **View** next to a memory. The memory page shows its content, creation date, and last modified date.

1. To see an earlier version, choose it from the version selector.

**To view the knowledge graph:**

1. On the **Memories** tab, choose **Relationships** instead of **All memories**. The graph shows each memory that links to another. Memories without relationships don't appear in the graph; you can find them under **All memories**. Each node is colored by its store and sized by its number of links.

1. To find a memory in the graph, use **Find a memory**.

1. Choose a memory to see its relationships, or choose a relationship to see its type, **Why they are linked**, and **Evidence**.

To see one memory's relationships, open it and choose **Relationships** instead of **Memory content**. The view shows the memory and the ones it links to directly, based on its latest version.

A relationship has one of these types: **Same incident**, **Correlated alarm**, **Upstream component**, **Past mistake**, **Condition definition**, or **Runnable check**. A **Correlated alarm** relationship applies in both directions. The other types point from one memory to another.

If the learning agent hasn't built the knowledge graph for your Agent Space yet, the view shows **No knowledge graph yet**. When the learning agent rebuilds the graph, the view shows the previous graph until the new one is ready.

## Editing memories with Chat
<a name="editing-memories-with-chat"></a>

You can create, update, and delete memories by asking AWS DevOps Agent in Chat. Chat writes to your stores directly. Chat can't change the relationships in the knowledge graph. When you change a memory, the learning agent judges its relationships again the next time it builds the graph.

**Examples:**
+ "Remember that the storage service is called Orders Storage Service." Chat creates or updates a memory in the `directives` store.
+ "Update the memory for the canary alarm to note that it is flaky during deployments." Chat updates that alarm's memory in the `monitors` store.
+ "In the payments-runbook store, remember that the checkout latency alarm spikes during nightly batch jobs." Chat adds a memory to a custom store.
+ "Delete the memory about the old database connection string." Chat removes it.
+ "Create a memory store called network-quirks and add a note that the eu-west-1 NAT gateway drops idle connections after 350 seconds." Chat creates the store and its first memory.

## Activating and deactivating memories
<a name="activating-and-deactivating-memories"></a>

You can deactivate a store or a single memory without deleting it.

**To activate or deactivate a memory store:**

1. On the **Memories** tab, use the toggle next to the memory store.

1. While a store is inactive, agents don't read anything in it.

**To activate or deactivate a memory:**

1. Open the store that contains the memory.

1. Use the toggle next to the memory.

1. While a memory is inactive, agents skip it.

## Memory limits
<a name="memory-limits"></a>

For more information about the limits on stores, memories per store, and memory size, see [Quotas](quotas.md).