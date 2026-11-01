

# Using the AWS Coding Plugin for SAP ABAP chat panel
<a name="using-chat"></a>

The Coding Plugin chat panel is where you work with Kiro inside Eclipse. You open it as an Eclipse view, type a prompt, and Kiro replies in the same panel. With separate tabs, you can hold more than one conversation at a time. With the selector bar, you can set the model and mode Kiro uses.

## Opening the chat panel
<a name="using-chat-opening"></a>

The chat panel opens as an Eclipse view, and holds each conversation in a tab in that view.

**To open the chat panel**

1. Choose **Window**, **Show View**, **Other…​**.

1. Choose AWS Coding Plugin Chat, and then choose **Open**.

You can also open the panel from Quick Access: press  Ctrl 3  (macOS:  Cmd 3 ), type AWS Coding Plugin Chat, and then press Enter.

## Sending a prompt
<a name="using-chat-sending"></a>

With the chat panel open, you send a prompt from the input field at the bottom of the panel.

**To send a prompt**

1. Enter your prompt in the input field at the bottom of the panel.

1. (Optional) Choose up to five documents to attach to the prompt, so Kiro has more context. To work around this limit, Kiro can also read files directly from your filesystem.

1. Choose **Send**, or press Enter.

To write a prompt that spans several lines, press  Shift Enter  to start a new line without sending the prompt.

Kiro responds in the same tab. The response streams in as Kiro works, and any permission prompt for a tool call appears inline in the conversation (see [Kiro Permissions](kiro-permissions.md)).

## Working across multiple tabs
<a name="using-chat-tabs"></a>

Each tab holds its own conversation with Kiro. You can open up to 10 tabs and run them at the same time. While Kiro works in one tab, you can send a prompt in another. A reply always stays on the tab you sent it from. Closing a tab stops the work running in it. When you reopen the chat panel, it restores your most recently used tabs.

There are three exceptions to the parallelism between tabs:
+  **A pending permission prompt.** When a tab is waiting for you to approve or deny a tool call, you cannot submit a new prompt in another tab. A banner directs you to respond to the pending prompt first.
+  **A running spec.** Kiro runs one spec at a time, so while a spec task is executing it serializes the work in your other tabs.
+  **A turn already running in another tab.** Kiro runs one turn at a time across all tabs, so a prompt you submit while another tab’s turn is running waits for that turn to finish. Until yours starts, the Coding Plugin shows `Waiting — another tab’s turn is running…`.

## The selector bar
<a name="using-chat-selector"></a>

A selector bar at the bottom of the chat panel lets you choose the model and mode Kiro uses for a conversation, and shows how much the conversation costs to run.

The model and mode lists are a view onto what your Kiro backend offers, so the available choices come from Kiro, not from the plug-in. For what the models are and how they differ, see [Models](https://kiro.dev/docs/models/) in the Kiro documentation.

Kiro’s models are general-purpose and are not tuned specifically for SAP ABAP, but the larger, more capable models show strong knowledge of SAP ABAP coding practices. SAP ABAP development involves many tool calls across many objects, so prefer a model with a context window of about 1 million tokens. A stronger model can do better on reasoning-heavy work such as authoring a spec. A smaller, lower-cost model is often enough for implementing the spec. This is a fast-moving area, so experiment to find the models that work best for you.

## Monitoring credit usage
<a name="using-chat-credit-usage"></a>

Coding Plugin shows how your Kiro credits are being spent in several places:
+  **Total.** A credit meter at the bottom of the window shows your account’s overall usage.
+  **Per tab.** Hovering over a tab header shows that conversation’s credit usage in a tooltip.
+  **Per turn.** Each turn’s credit usage is shown on the tab.
+  **Per spec.** Coding Plugin tracks estimated credit usage for each spec. This is not shown in the UI. Ask Kiro about a spec’s usage to see it.

For what a credit is and how usage maps to your Kiro plan, see [Pricing](pricing.md).

## Copying content from a conversation
<a name="using-chat-copying"></a>

You can copy content out of a conversation at three levels:
+  **A code block.** Each code block in a reply has a **Copy** button that copies that block’s code to the clipboard.
+  **A turn.** Each turn has a **Copy as Markdown** button in its footer that copies that one exchange as Markdown.
+  **The whole conversation.** Open the context menu for the tab’s heading and choose **Copy entire transcript** to copy the full conversation to the clipboard.

## Managing context
<a name="using-chat-context"></a>

A context meter in the chat panel shows how much of the conversation’s context window is in use. As a conversation grows, Kiro compacts its earlier history to stay within that window, so a long conversation can continue without you starting over. For more on how Kiro manages context and compacts history, see [Compaction](https://kiro.dev/docs/compaction/) in the Kiro documentation.