# Tool choice best practices

###### Note

This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Sonic guide, visit [Tool configuration](../nova2-userguide/sonic-tool-configuration.md "../nova2-userguide/sonic-tool-configuration.md").

When implementing tools with Amazon Nova Sonic, we recommend following these best practices to ensure optimal performance:

- **Keep schema structure simple**: Limit top-level keys to 3 or fewer when possible.
- **Create distinct parameter names**: Use clear, semantically different names between similar parameters to avoid confusion (that is, don't use both "product_id" and "cart_item_id" if they serve different purposes).
- **Provide detailed tool descriptions**: Clearly describe each tool's purpose and when it should be used to help the model select the appropriate tool.
- **Define input schemas precisely**: Specify parameter types and include descriptions for each parameter. Clearly indicate which parameters are required versus optional.
- **Monitor context length**: Tool performance may degrade as context approaches larger tokens (that is, approximately 50K tokens). Consider breaking complex tasks into smaller steps when working with long contexts.
- **Implement error handling**: Prepare for cases when tool execution fails by including appropriate fallback behaviors.
- **Test thoroughly**: Verify your tools work across a variety of inputs and edge cases before deployment.
- **Greedy decoding parameters**: Set the value of temperature to 0 for tool use.
  We recommend that you avoid the following common issues:

- When you encounter JSON schema adherence failures, you might need to simplify your schema structure or provide clearer instructions.
- Be mindful that the model might omit optional parameters that would improve results (such as 'limit' parameters in queries).
  By following these guidelines, you can leverage the full capabilities of the Amazon Nova Sonic model's tool use features to create powerful conversational AI applications that can access external data sources and perform complex actions.
