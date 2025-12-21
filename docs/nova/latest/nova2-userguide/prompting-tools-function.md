# Tool calling systems

Tool calling is available for the Amazon Nova models by passing a tool configuration schema in
your request. The prompt for the model is going to be augmented with this tool configuration
so it is a highly impactful place to begin optimizing your tool calling system.

Consider these key principles:

- Tool definitions should be clear and concise. They should be easy to understand and
  the intent must be extremely apparent.
- Use key differentiators and boundary conditions to define when one tool should be used
  over another.
- Be critical the input argument types. Ask, do they make sense and would they be
  expected to be used in that fashion normally?
  **Use “Tool Choice” to control when a tool is called**

The tool choice parameter allows you to customize the behavior of tool calling with the
model. We recommend utilizing this for fine grained control on which tools are called and
when.

For example, for use cases like structured output, you might want a specific tool to be
called each time Amazon Nova is invoked. You can define the schema of your output as the tool and
then set the tool choice to the name of that tool.

```
{
   "toolChoice": {
        "tool": {
            "name": "name_of_tool"
        }
    }
}
```

For many agentic use cases, you might want to ensure that the model always selects one of
the available tools. To do so, you can set the tool choice to `any`, which will
call exactly one tool each time the model is invoked.

```
{
   "toolChoice": {
        "any": {}
    }
}
```

Lastly, for use cases where whether a tool is called is highly dependent on the context of
the conversation, you can set the tool choice to `auto`. This is the default
behavior and will leave the tool selection completely up to the model.

```
{
   "toolChoice": {
        "auto": {}
    }
}
```
