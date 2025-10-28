# Create your guardrail

Amazon Bedrock Guardrails consists of a collection of different filtering policies that you can configure to
help avoid undesirable and harmful content and remove or mask sensitive information for
privacy protection.

You can configure the following policies in a guardrail:

- **Content filters** — You can configure thresholds to help block input prompts
  or model responses in natural language for text and separately for images containing harmful content such as: hate, insults,
  sexual, violence, misconduct (including criminal activity), and prompt attacks (prompt injection and jailbreaks). For example,
  an e-commerce site can design its online assistant to avoid using inappropriate language and/or images such as hate or violence.
- **Prompt attacks** — Can help you detect and
  filter prompt attacks and prompt injections. Helps detect prompts that are intended
  to bypass moderation, override instructions, or generate harmful content.
- **Denied topics** — You can define a set of topics to
  avoid within your generative AI application. For example, a banking assistant application can be
  designed to help avoid topics related to illegal investment advice.
- **Word filters** — You can configure a set of custom words or
  phrases (exact match) that you want to detect and block in the interaction between your users and generative AI applications.
  For example, you can detect and block profanity as well as specific custom words such as competitor names, or
  other offensive words.
- **Sensitive information filters** — Can help you detect sensitive content such as
  Personally Identifiable Information (PII) in standard formats or custom regex entities in user inputs and FM responses. Based
  on the use case, you can reject inputs containing sensitive information or redact them in FM responses. For example,
  you can redact users’ personal information while generating summaries from customer and agent conversation
  transcripts.
- **Contextual grounding checks** — Can help you detect and filter hallucinations
  in model responses if they are not grounded (factually inaccurate or add new information) in the source information or are
  irrelevant to the user’s query. For example, you can block or flag responses in RAG applications (retrieval-augmented
  generation), if the model responses deviate from the information in the retrieved passages or doesn’t answer the question
  by the user.
- **Automated reasoning checks** — Can help you validate that model responses
  adhere to logical rules and policies that you define. You can create policies using natural language that specify the
  reasoning requirements, and the guardrail will evaluate whether model outputs comply with these logical constraints.
  For example, you can ensure that a customer service chatbot only recommends products that are actually available in
  inventory, or verify that financial advice follows regulatory compliance rules.

###### Note

All blocked content from the above policies will appear as plain text in [Amazon Bedrock Model Invocation Logs](model-invocation-logging.md "model-invocation-logging.md"), if you have enabled
them. You can disable Amazon Bedrock Invocation Logs if you do not want your blocked content to appear as plain text in the logs.

A guardrail must contain at least one filter and messaging for when prompts and user
responses are blocked. You can opt to use the default messaging. You can add filters and
iterate on your guardrail later by following the steps at [Modify your guardrail](guardrails-edit.md "guardrails-edit.md").

###### Topics

- [Configure content filters for Amazon Bedrock Guardrails](guardrails-content-filters-overview.md "guardrails-content-filters-overview.md")
- [Block denied topics to help remove harmful content](guardrails-denied-topics.md "guardrails-denied-topics.md")
- [Remove a specific list of words and phrases from conversations with word filters](guardrails-word-filters.md "guardrails-word-filters.md")
- [Remove PII from conversations by using sensitive information filters](guardrails-sensitive-filters.md "guardrails-sensitive-filters.md")
- [Use contextual grounding check to filter hallucinations in responses](guardrails-contextual-grounding-check.md "guardrails-contextual-grounding-check.md")
- [Options for handling harmful
  content detected by Amazon Bedrock Guardrails](guardrails-harmful-content-handling-options.md "guardrails-harmful-content-handling-options.md")
- [Improve accuracy by adding Automated Reasoning checks in Amazon Bedrock Guardrails](guardrails-automated-reasoning-checks.md "guardrails-automated-reasoning-checks.md")
