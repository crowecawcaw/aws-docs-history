# Hallucination mitigation in Amazon Q Business

A [hallucination](concepts-terms.md#hallucination "concepts-terms.md#hallucination"), in the machine learning context, is a
confident response by an AI (artificial intelligence) application environment that isn't
supported by its underlying data. Amazon Q Business includes a hallucination
prevention system that works in real-time during chat conversations.

The _hallucination mitigation_ feature helps ensure more accurate
retrieval augmented generation (RAG) responses from data connected to the
application—either through connected data sources, or files uploaded during chat
(up to 100,000 characters). During chat, Amazon Q Business evaluates a response
for hallucinations. If a hallucination is detected with high confidence, it corrects the
inconsistencies in its response real-time during chat and generates a new, edited
message.

To activate hallucination mitigation, use [Amazon Q Business admin controls and
guardrails](guardrails-global-controls.md "guardrails-global-controls.md").

Hallucination mitigation isn't supported for the following use cases:

- Applications where [chat orchestration](guardrails-global-controls.md#guardrails-global-orchestration "guardrails-global-controls.md#guardrails-global-orchestration") is enabled.
- [Plugin](plugins.md "plugins.md") workflows.
- Responses generated from tabular data, or from transcripts of images, audio
  and video. Hallucination mitigation applies only to responses generated from
  textual data.

###### Important

Activating hallucination mitigation will increase chat response latency.
