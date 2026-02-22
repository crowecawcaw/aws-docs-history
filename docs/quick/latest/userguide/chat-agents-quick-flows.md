# Chat agents in Amazon Quick Flows

Amazon Quick Flows allows you to utilize your chat agents in Quick to generate outputs for any step. This feature enables your flows to utilize customized agents to explore data, analyze information, and take actions, in the context of a workflow.

Chat agents contain domain-specific knowledge, custom instructions, and connected tools that represent institutional expertise. When you integrate chat agents into your flows, you can automatically apply this specialized knowledge across multiple workflows without recreating it. For example, if you built a sales assistant chat agent that understands product details, follows brand guidelines, and knows sales best practices, you can embed this agent in your outreach flow to ensure consistent, high-quality communication at scale.

## Adding a chat agent to your flow

To use a chat agent in your flow, follow these steps:

1. In the flow Editor mode, select the **+ Add step** button.
2. From the step menu, choose **Chat agent**.
3. Configure this step by selecting:
   1. **Title**: Clear, descriptive name for what this step does
   2. **Chat agent**: From the dropdown, select an agent you already have access to.
   3. **Prompt instruction**: Guidance in natural language on what you seek the chat agent to accomplish in this step. Like in chat, you can select the scope of data and apps you want to give access to with the option to use web search. Remember, this is a single-turn ask from the chat agent. In other words, the chat agent will respond for the task you instruct it to do, but will not support a back-and-forth conversation in the same step.

###### Tip

Use an @reference in your instructions to get dynamic inputs from users or utilize outputs of previous steps in the workflow. You can also reference the response from your chat agent in later steps like to send customers the email drafted by the Sales Assistant.

## Related topics

For more information about related features and capabilities, see the following topics:

- [Creating flows](creating-flows.md "creating-flows.md")
- [Editing flows](editing-flows.md "editing-flows.md")
