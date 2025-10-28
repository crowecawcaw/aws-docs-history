# Admin controls and guardrails in Amazon Q Business

With Amazon Q Business, you can customize your application environment to your
organizational needs. Amazon Q Business offers application environment
_guardrails_ or _chat controls_ that you can
configure to control the end user chat experience.

Using the guardrails feature, you can define global controls and topic-level controls
for your application environment like the following:

- Control whether end users can upload files in chat to generate responses from
  uploaded files.
- Control whether chat responses will be personalized to end users based on
  information (address and job related information) associated with them in your
  IAM Identity Center instance.
- Specify whether all Amazon Q Business chat responses will be generated
  using only enterprise data or whether your application environment can also use its
  underlying large language model (LLM) to generate responses when it can’t find
  answers in your enterprise data.
- Allow Amazon Q Business to automatically orchestrate end user chat
  requests across any Amazon Q Business plugins and data sources you’ve
  configured.
- Allow Amazon Q Business to check its responses for
  hallucinations.
- Control how Amazon Q Business responds to specific topics in
  chat.
- Customize which users and groups Amazon Q Business topic-level controls
  apply to.

###### Topics

- [Key terms for Amazon Q Business
  guardrails and chat controls](guardrails-concepts.md "guardrails-concepts.md")
- [Using global controls in Amazon Q Business](guardrails-global-controls.md "guardrails-global-controls.md")
- [Using topic-level controls in Amazon Q Business](guardrails-topic-controls.md "guardrails-topic-controls.md")
- [Managing Amazon Q Business admin
  controls and guardrails](guardrails-management.md "guardrails-management.md")
