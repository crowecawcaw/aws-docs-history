# Detect and filter harmful content by using Amazon Bedrock Guardrails

Amazon Bedrock Guardrails provides safeguards that you can configure for your generative AI applications based
on your use cases and responsible AI policies. You can create multiple guardrails tailored
to different use cases and apply them across multiple foundation models (FMs), providing a
consistent user experience and standardizing safety and privacy controls across generative
AI applications. You can use guardrails for both model prompts and responses with natural
language.

You can use Amazon Bedrock Guardrails in multiple ways to help safeguard your generative AI applications. For
example:

- A chatbot application can use guardrails to help filter harmful user inputs and
  toxic model responses.
- A banking application can use guardrails to help block user queries or model
  responses associated with seeking or providing investment advice.
- A call center application to summarize conversation transcripts between users and
  agents can use guardrails to redact users’ personally identifiable information (PII)
  to protect user privacy.
  Amazon Bedrock Guardrails provides the following safeguards (also known as policies) to detect and filter
  harmful content:

- **Content filters** – Detect and filter harmful
  text or image content in input prompts or model responses. Filtering is done based
  on detection of certain predefined harmful content categories: Hate, Insults,
  Sexual, Violence, Misconduct and Prompt Attack. You also can adjust the filter
  strength for each of these categories. These categories are supported for both Classic
  and Standard [tiers](guardrails-tiers.md "guardrails-tiers.md"). With Standard tier,
  detection of undesirable content is extended to protection against harmful content
  introduced within code elements including comments, variable and function names, and
  string literals.
- **Denied topics** – Define a set of topics that
  are undesirable in the context of your application. The filter will help block them
  if detected in user queries or model responses. With [Standard tier](guardrails-tiers.md "guardrails-tiers.md"), detection of undesirable content
  is extended to protection against harmful content introduced within code elements
  including comments, variables and function names, and string literals.
- **Word filters** – Configure filters to help
  block undesirable words, phrases, and profanity (exact match). Such words can
  include offensive terms, competitor names, etc.
- **Sensitive information filters** – Configure
  filters to help block or mask sensitive information, such as personally identifiable
  information (PII), or custom regex in user inputs and model responses. Blocking or
  masking is done based on probabilistic detection of sensitive information in
  standard formats in entities such as SSN number, Date of Birth, address, etc. This
  also allows configuring regular expression based detection of patterns for
  identifiers.
- **Contextual grounding checks** – Help detect
  and filter hallucinations in model responses based on grounding in a source and
  relevance to the user query.
- **Automated Reasoning checks** – Can help you
  validate the accuracy of foundation model responses against a set of logical rules.
  You can use Automated Reasoning checks to detect hallucinations, suggest
  corrections, and highlight unstated assumptions in model responses.
  In addition to the above policies, you can also configure the messages to be returned to
  the user if a user input or model response is in violation of the policies defined in the
  guardrail.

Experiment and benchmark with different configurations and use the built-in test window to
ensure that the results meet your use-case requirements. When you create a guardrail, a
working draft is automatically available for you to iteratively modify. Experiment with
different configurations and use the built-in test window to see whether they are
appropriate for your use-case. If you are satisfied with a set of configurations, you can
create a version of the guardrail and use it with supported foundation models.

Guardrails can be used directly with FMs during the inference API invocation by specifying
the guardrail ID and the version. Guardrails can also be used directly through the
`ApplyGuardrail` API without invoking the foundation models. If a guardrail
is used, it will evaluate the input prompts and the FM completions against the defined
policies.

For retrieval augmented generation (RAG) or conversational applications, you might need to
evaluate only the user input in the input prompt while discarding system instructions,
search results, conversation history, or a few short examples. To selectively evaluate a
section of the input prompt, see [Apply tags to user input to filter content](guardrails-tagging.md "guardrails-tagging.md").

###### Topics

- [How Amazon Bedrock Guardrails works](guardrails-how.md "guardrails-how.md")
- [Supported Regions and models for Amazon Bedrock Guardrails](guardrails-supported.md "guardrails-supported.md")
- [Safeguard tiers for guardrails policies](guardrails-tiers.md "guardrails-tiers.md")
- [Languages supported by Amazon Bedrock Guardrails](guardrails-supported-languages.md "guardrails-supported-languages.md")
- [Prerequisites for using Amazon Bedrock Guardrails](guardrails-prereq.md "guardrails-prereq.md")
- [Set up permissions to use Amazon Bedrock Guardrails](guardrails-permissions.md "guardrails-permissions.md")
- [Create your guardrail](guardrails-components.md "guardrails-components.md")
- [Distribute guardrail inference across AWS Regions](guardrails-cross-region.md "guardrails-cross-region.md")
- [Apply cross-account safeguards with Amazon Bedrock Guardrails enforcements](guardrails-enforcements.md "guardrails-enforcements.md")
- [Test your guardrail](guardrails-test.md "guardrails-test.md")
- [View information about your guardrails](guardrails-view.md "guardrails-view.md")
- [Modify your guardrail](guardrails-edit.md "guardrails-edit.md")
- [Delete your guardrail](guardrails-delete.md "guardrails-delete.md")
- [Deploy your guardrail](guardrails-deploy.md "guardrails-deploy.md")
- [Use cases for Amazon Bedrock Guardrails](guardrails-use.md "guardrails-use.md")
