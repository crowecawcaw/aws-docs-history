# General best practices

The following best practices mainly apply to the Amazon Nova text models, but you can apply them
to other models, in addition to modality-specific best practices.

For more information on how to prompt multimodal inputs, refer to [Prompting multimodal inputs](prompting-multimodal.md "prompting-multimodal.md"). For information on how
to prompt speech inputs, refer to [Voice conversation prompts](sonic-system-prompts.md "sonic-system-prompts.md").

## Understanding the roles

Amazon Nova models allow you to structure prompts through the use of three distinct roles:
system, user, and assistant.

- **System (optional)** – Although not mandatory, it
  establishes the overall behavioral parameters of the assistant. It can also be utilized to
  provide additional instructions and guidelines that the user wishes the model to adhere to
  throughout the conversation.
- **User** – Can optionally convey the context, tasks,
  instructions, and the desired outcome along with the user query.
- **Assistant** – Aids in guiding the model towards the
  intended response.

###### Topics

- [Create precise prompts](create-precise-prompts.md "create-precise-prompts.md")
- [Bring focus to sections of the prompt](prompting-bring-focus.md "prompting-bring-focus.md")
- [Using the system role](prompting-system-role.md "prompting-system-role.md")
- [Provide examples (few-shot prompting)](prompting-provide-examples.md "prompting-provide-examples.md")
- [Tool calling systems](prompting-tools-function.md "prompting-tools-function.md")
- [Advanced prompting techniques](advanced-prompting-techniques.md "advanced-prompting-techniques.md")
