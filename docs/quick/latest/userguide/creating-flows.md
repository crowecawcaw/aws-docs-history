# Creating flows

After enabling Amazon Quick Flows in the Amazon Quick management console, users with creator permissions and an appropriate Amazon Quick license can create flows using several different methods. This section describes the various ways to create a flow and the requirements for each method.

## Prerequisites for creating flows

Before you can create a flow, ensure that you have:

- Creator permissions in Quick.
- Access to the Amazon Quick Flows feature, which must be enabled by your administrator.
- A supported web browser. For more information about browser requirements, see [Browser requirements](prerequisites-for-quick-flows.md#browser-requirements "prerequisites-for-quick-flows.md#browser-requirements").

## Creating a flow using natural language prompt (NLP)

The natural language prompt method allows you to describe your desired flow in plain language, and Amazon Quick Flows will generate a flow based on your description.

1. Sign in to the Quick console.
2. In the navigation pane, choose _Flows_.
3. Choose _Create Flow_. Once you select creating a flow, you see a page where you can enter a natural language prompt or use a sample prompt.
4. In the prompt field, describe the flow you want to create. Be as specific as possible about:
   - The purpose of the flow
   - The inputs it should accept
   - The processing it should perform
   - The outputs or actions it should produce

5. Choose _Generate Flow_.
6. Review the generated flow and make any necessary adjustments.
7. Preview the flow to test its functionality and ensure it works as expected. If the flow is ready for use, you can share or publish it with individuals, groups, or all users who have appropriate access permissions.

###### Note

The quality of the generated flow depends on the clarity and specificity of your natural language prompt. You may need to refine your prompt or make manual adjustments to the flow to achieve your desired outcome.

## Creating a flow from scratch (blank flow)

Creating a flow from scratch gives you complete control over the design and functionality of your flow.

1. Sign in to the Quick web experience.
2. In the navigation pane, choose _Flows_.
3. Choose _Create Flow_.
4. Create a blank flow.
5. Enter a name and optional description for your flow.
6. In the Flow builder, add and configure the steps you need:
   - Add input steps to collect information from users.
   - Add reasoning groups to process information using AI models.
   - Add output steps to get AI-generated responses from Quick data, Quick Sight dashboards and topics, Web search, UI Agent, or General knowledge.
   - Add action steps to perform operations in connected systems.
   - Add image step to generate professional grade content from text and image inputs.

7. Choose _Save_ to save your flow.

For more information about the different components you can use in a flow, see [Terminology and key concepts](terminology-and-key-concepts.md "terminology-and-key-concepts.md").

## Creating a flow by duplicating an existing flow

Duplicating a flow allows you to copy an existing flow. This helps users to understand how the flow was created and easily create flows based on others' ideas.

1. Sign in to the Quick console.
2. In the navigation pane, choose _Flows_.
3. Find the flow you want to duplicate.
4. Choose the ellipsis (⋮) next to the flow name, then choose _Duplicate_.
5. Enter a name and optional description for the new flow.
6. Make any necessary modifications to the duplicated flow.
7. Choose _Save_ to save your flow.

###### Note

When you duplicate a flow, all components, connections, and configurations are copied to the new flow. However, you may need to reconfigure certain settings, such as authentication for action connectors.

## Creating a flow from an agent conversation

You can create a flow directly from a conversation with Amazon Q by using the Quick Flows icon in the chat bar.

1. Sign in to the Quick console.
2. Start a conversation with Amazon Quick Agent in the chat interface.
3. Discuss the flow you want to create, including its purpose, inputs, processing, and outputs.
4. When you're ready to create the flow, click the Quick Flows icon in the chat bar.
5. Choose _Create Flow from conversation_.
6. Enter a name and optional description for the flow.
7. Choose _Create_.
8. Review the generated flow and make any necessary adjustments.
9. Choose _Save_ to save your flow.

This method is particularly useful when you want to explore ideas and possibilities through conversation before creating a flow.

## Flow creation requirements

When creating a flow, keep the following requirements in mind:

Flow name

Flow names must be unique within your Quick account and can contain up to 128 characters.

Flow components

A valid flow must have at least one input step and one output step or action step.

Reasoning groups

Each reasoning group must have at least one instruction that defines what the AI model should do with the inputs.

Action steps

Action steps require proper authentication and configuration before they can be used in a flow.

## Next steps

After creating a flow, you can:

- Test your flow to ensure it works as expected. .
- Publish your flow to make it available to users. See [Publishing your flow](versioning.md#publishing-your-flow "versioning.md#publishing-your-flow").
- Share your flow with specific users or groups. See [Sharing flows](sharing-flows.md "sharing-flows.md").
- Monitor your flow's usage and performance. See [What is a progress tracker?](interacting-with-flows-in-runtime-mode.md#progress-tracker "interacting-with-flows-in-runtime-mode.md#progress-tracker").
