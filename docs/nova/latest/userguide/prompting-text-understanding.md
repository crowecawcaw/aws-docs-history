# Text understanding prompting best

practices

###### Note

This documentation is for Amazon Nova Version 1. For information on how to prompt Amazon Nova 2 text understanding models, visit [General best practices](../nova2-userguide/prompting-best-practices.md "../nova2-userguide/prompting-best-practices.md").

The Amazon Nova text generation models allow you to structure prompts through the use of
three distinct roles: system, user, and assistant. The system message, although not
mandatory, serves to establish the overall behavioral parameters of the assistant. It can
also be utilized to provide additional instructions and guidelines that the user wishes the
model to adhere to throughout the conversation. The user prompt can optionally convey the
context, tasks, instructions, and the desired outcome along with the user query. Moreover,
the assistant prompt aids in guiding the model towards the intended response.

- System (optional) — Establishes the overall behavioral parameters of the
  assistant.
- User — Conveys the context and specifies the outcome.
- Assistant — Aids in moving the model towards the intended solution.

###### Topics

- [Creating precise prompts](prompting-precision.md "prompting-precision.md")
- [Using the system role](prompting-system-role.md "prompting-system-role.md")
- [Give Amazon Nova time to think (chain-of-thought)](prompting-chain-of-thought.md "prompting-chain-of-thought.md")
- [Provide examples (few-shot prompting)](prompting-examples.md "prompting-examples.md")
- [Provide supporting text](prompting-support-text.md "prompting-support-text.md")
- [Bring focus to sections of the prompt](prompting-focus.md "prompting-focus.md")
- [Require structured output](prompting-structured-output.md "prompting-structured-output.md")
- [Utilizing long context windows](prompting-long-context.md "prompting-long-context.md")
- [Use external tools](prompting-tools.md "prompting-tools.md")
