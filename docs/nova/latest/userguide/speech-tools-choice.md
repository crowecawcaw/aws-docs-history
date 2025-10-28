# Controlling how tools are chosen

Amazon Nova Sonic supports three tool choice parameters to help you manage tool execution. You can control which tool the model uses by specifying the `toolChoice` parameter.

- **Tool** - The `tool` option ensures that the specific named tool is called exactly once at the beginning of the response generation. For example, if you specify a knowledge base tool, the model will query this knowledge base before responding, regardless of whether it thinks the tool is needed.
- **Any** - The `any` option ensures at least one of the available tools is called at the beginning of the response generation, while allowing the model to select the most appropriate one. This is useful when you have multiple knowledge bases or tools and want to ensure the model leverages at least one of them without specifying which one.
- **Auto** - With `auto`, the model has complete flexibility to determine whether any tools are needed at the beginning of the response generation and can call multiple tools if required. This is also the default behavior.
  For more information, see [Tool use with Amazon Nova](tool-choice.md "tool-choice.md").

###### Multi-tool sequence behavior

Amazon Nova Sonic handles tool execution intelligently within each response cycle. When you use the `tool` option, the model will first execute the specified tool, then evaluate whether additional tools are needed before generating its final response. Similarly, with the `any` option, the model first selects and calls one tool from the available options, then decides if additional tool calls would be needed before proceeding to generate its answer.

In all cases, the model manages the entire tool execution sequence within a single response generation cycle, determining when sufficient information has been gathered to generate an appropriate response.

Consider the following example scenarios:

Knowledge base example

- With `toolChoice: "knowledge_tool"`, the model will always query the specified knowledge base first, then possibly use other tools before responding if needed.
- With `toolChoice: "any"` and multiple knowledge bases available, the model will select the most relevant knowledge base, query it, and then possibly consult additional sources if needed.
- With `toolChoice: "auto"`, the model may skip knowledge lookups entirely for questions it can answer directly, or query multiple knowledge bases for complex questions.

Multi-functional assistant example

- A virtual assistant with weather, calendar, and knowledge tools could use `toolChoice: "auto"` to flexibly respond to diverse queries, calling only the necessary tools.
- Using `toolChoice: "any"` would ensure at least one tool is always used, even for queries the model could potentially answer directly.

To learn more, please refer to [Tool Choice](tool-choice.md "tool-choice.md").
