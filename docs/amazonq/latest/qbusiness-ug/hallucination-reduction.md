

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Hallucination mitigation in Amazon Q Business
<a name="hallucination-reduction"></a>

A [hallucination](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/concepts-terms.html#hallucination), in the machine learning context, is a confident response by an AI (artificial intelligence) application environment that isn't supported by its underlying data. Amazon Q Business includes a hallucination prevention system that works in real-time during chat conversations.

The *hallucination mitigation* feature helps ensure more accurate retrieval augmented generation (RAG) responses from data connected to the application—either through connected data sources, or files uploaded during chat (up to 100,000 characters). During chat, Amazon Q Business evaluates a response for hallucinations. If a hallucination is detected with high confidence, it corrects the inconsistencies in its response real-time during chat and generates a new, edited message.

To activate hallucination mitigation, use [Amazon Q Business admin controls and guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html).

Hallucination mitigation isn't supported for the following use cases:
+ Applications where [chat orchestration](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-orchestration) is enabled.
+ [Plugin](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html) workflows.
+ Responses generated from tabular data, or from transcripts of images, audio and video. Hallucination mitigation applies only to responses generated from textual data.

**Important**  
Activating hallucination mitigation will increase chat response latency.