

# Creating flows
<a name="creating-flows"></a>

 You can create flows using natural language, the visual editor, by duplicating an existing flow, or from a chat agent conversation. 

## Prerequisites for creating flows
<a name="prerequisites-for-creating-flows"></a>

 Before creating a flow, ensure that you meet the requirements described in [Prerequisites for Quick Flows](prerequisites-for-quick-flows.md). 

## Creating a flow using natural language prompt (NLP)
<a name="creating-flow-using-nlp"></a>

 The natural language prompt method lets you describe your desired flow in plain language, and Amazon Quick Flows generates a flow based on your description. 

1. Sign in to the Quick console.

1. In the navigation pane, choose **Flows**.

1. Choose **Create Flow**. You see a page where you can enter a natural language prompt or use a sample prompt.

1. In the prompt field, describe the flow you want to create. Be as specific as possible about:
   + The purpose of the flow
   + The inputs it should accept
   + The processing it should perform
   + The outputs it should produce
   + The actions it should take

1. Choose **Generate Flow**.

1. Review the generated flow and make any necessary adjustments.

1. Switch to **Run mode** to test your flow. If the flow is ready for use, you can share or publish it.

**Note**  
The quality of the generated flow depends on the clarity and specificity of your prompt. You may need to refine your prompt or make manual adjustments to achieve your desired outcome.

## Creating a flow from scratch (blank flow)
<a name="creating-flow-from-scratch"></a>

Creating a flow from scratch gives you complete control over the design and functionality of your flow.

1. Sign in to the Quick web experience.

1. In the navigation pane, choose **Flows**.

1. Choose **Create Flow**.

1. Create a blank flow.

1. Enter a name and optional description for your flow.

1. In the Flow builder, add and configure the steps you need:
   + Add user input steps to collect text or files from users.
   + Add AI response steps to generate content from chat agents, web search, general knowledge, or image generation.
   + Add data insight steps to get responses from Quick data or dashboards and topics.
   + Add reasoning groups to control how steps run with conditions, loops, or validation.
   + Add action steps to read or write to connected applications.

1. Choose **Save** to save your flow.

For more information about the different components you can use in a flow, see [Terminology and key concepts](terminology-and-key-concepts.md).

## Creating a flow by duplicating an existing flow
<a name="creating-flow-by-duplicating"></a>

Duplicating a flow creates a copy that you can modify for your own purposes.

1. Sign in to the Quick console.

1. In the navigation pane, choose **Flows**.

1. Find the flow you want to duplicate.

1. Choose the ellipsis (⋮) next to the flow name, then choose **Duplicate**.

1. Modify the name and optionally the description for your purposes.

1. Make any necessary modifications to the flow.

1. Choose **Save** to save your flow.

**Note**  
When you duplicate a flow, all components, connections, and configurations are copied. However, you may need to reconfigure certain settings, such as authentication for connectors.

## Creating a flow from an agent conversation
<a name="creating-flow-from-conversation"></a>

You can create a flow from a conversation with a chat agent. For example, if you have been working through a task like reading an email, augmenting it with internal or web knowledge, and drafting a response, you can convert that conversation into a reusable flow.

1. Sign in to the Quick console.

1. Start a conversation with a chat agent.

1. Work through the task you want to automate.

1. Choose the Quick Flows icon in the chat bar.

1. Choose **Create Flow from conversation**. Amazon Quick Flows interprets the interactions in your conversation and brings you to the Create flow screen with a generated natural language prompt, name, and description.

1. Review and edit the prompt, name, and description as needed.

1. Choose **Generate Flow**.

1. Review the generated flow and make any necessary adjustments.

1. Choose **Save** to save your flow.

## Flow creation requirements
<a name="flow-creation-requirements"></a>

When creating a flow, keep the following requirements in mind:

Flow name  
Flow names must be unique within your Quick account and can contain up to 128 characters.

Flow components  
A valid flow must have at least one output step or action step.

Reasoning groups  
Each reasoning group must have at least one instruction that defines what the AI model should do with the inputs.

Action steps  
Action steps require proper authentication and configuration before they can be used in a flow.

## Next steps
<a name="next-steps-after-creating-flow"></a>

After creating a flow, you can:
+ Test your flow to ensure it works as expected.
+ Publish your flow to make it available to users. See [Publishing changes](versioning.md#publishing-your-flow).
+ Share your flow with specific users or groups. See [Sharing flows](sharing-flows.md).
+ Monitor your flow's usage and performance. See [Progress tracker](interacting-with-flows-in-runtime-mode.md#progress-tracker).