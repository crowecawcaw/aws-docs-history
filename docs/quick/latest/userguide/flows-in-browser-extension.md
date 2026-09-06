

# Using Amazon Quick Flows in the browser extension
<a name="flows-in-browser-extension"></a>

Amazon Quick Flows in the browser extension enables you to run pre-defined workflows directly within your web browsing context. You can invoke flows that you've created or that have been shared with you, pass web page content as input, and execute multi-step workflows without leaving your browser.

When you use flows in the browser extension, you can:
+ Invoke flows explicitly from the browser extension interface.
+ Pass web pages as context to your flows.
+ View flow execution history in your browser extension.

## Prerequisites
<a name="flows-browser-prerequisites"></a>

Before using flows in the browser extension, ensure you have:
+ Appropriate permissions to execute flows in your Amazon Quick account.

## Invoking flows
<a name="invoking-flows-browser"></a>

You can invoke flows from the browser extension to run workflows on the web pages you're viewing.

**To invoke a flow in the browser extension:**

1. Open the Amazon Quick browser extension.

1. In the chat interface, choose the **Flows** icon.

1. Select a flow from the list or use the search bar to search through your flows.

1. The flow begins execution in the browser extension chat.

1. When prompted, select the tab you want to include as context and choose **Confirm**.

When a flow is active, the browser extension displays a progress tracker showing the current step. The dropdown menu on the progress tracker shows all steps in the flow.

## Flow execution process
<a name="flows-execution-process-browser"></a>

Once a flow is invoked in your browser extension, you interact with the flow through natural language chat as follows:

1. You're greeted with a summary of its capabilities.

1. You're prompted for required inputs through chat messages.

1. The extension displays outputs and results in the chat interface.

1. The extension shows a progress tracker indicating completed and remaining steps.

To view flow capabilities, see the [flows documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-flows.html).

## Flow execution history
<a name="flow-execution-history-browser"></a>

All flow executions in the browser extension are recorded in your conversation history. You can view past executions and resume incomplete flows. To view flow execution history:

1. In the browser extension, go to menu and choose the **Conversation history** icon.

1. Select a conversation that includes a flow execution.

1. The conversation displays the flow execution details, including all inputs and outputs.

If you closed the browser extension while a flow was running, you can resume the flow by selecting it from your history.

## Stopping flow execution
<a name="stopping-flow-execution-browser"></a>

You can stop a flow at any time during execution. To stop a running flow:

1. While the flow is running, choose the **End** button in the progress tracker.

1. The flow stops at the current step and you can continue your conversation with your My Assistant or Chat agent.