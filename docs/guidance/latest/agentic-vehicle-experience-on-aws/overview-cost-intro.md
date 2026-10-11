

# Cost Considerations
<a name="overview-cost-intro"></a>

AVX costs are driven primarily by three components:
+  **Amazon Bedrock model invocations** — every agent turn invokes Claude Sonnet via Bedrock. Voice conversations via Nova 2 Sonic incur per-minute audio-processing charges in addition to token charges. Cost scales with conversation volume and average turn count.
+  **Amazon Bedrock Knowledge Base retrieval** — each `knowledge()` tool call performs a vector search against the ADP Knowledge Base, which stores its vectors in Amazon S3 Vectors and is billed by usage.
+  **Amazon Connect usage** — voice contacts incur per-minute charges; chat contacts incur per-message charges. Tier-2 agent seats carry a per-seat-per-month charge.

AgentCore runtime, API Gateway, Lambda, and DynamoDB costs are modest relative to Bedrock and Connect at typical contact-center volumes.

Detailed cost estimates — including a per-component breakdown, assumptions, and guidance on how to use the [AWS Pricing Calculator](https://calculator.aws/) for your workload — are in the [Plan Your Deployment](plan-your-deployment.md) chapter.

**Note**  
AVX uses the ADP Bedrock Knowledge Base as a shared resource when both guidances are deployed together. Its vector storage and ingestion are billed to the ADP account; if ADP is already deployed for analytical workloads, that cost is not incremental to AVX.