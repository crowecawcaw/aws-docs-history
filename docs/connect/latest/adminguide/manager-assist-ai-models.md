

# AI models and data processing for manager assist
<a name="manager-assist-ai-models"></a>

Manager assist is built on foundation models in Amazon Bedrock. It uses foundation models to interpret questions written in plain language, identify the relevant metrics, retrieve data, and generate responses.

**Important**  
Although responses are grounded in the data in your instance, AI-generated responses might contain inaccuracies. Always validate critical insights against your Connect Customer reports and dashboards.

## Cross-Region inference
<a name="manager-assist-cross-region-inference"></a>

Manager assist uses cross-Region inference to select the optimal AWS Region for processing your data. Cross-Region inference improves the customer experience by maximizing the available resources and model availability. If you do not want your data processed in a Region other than the one that you selected, contact AWS Support.

For more information, see [Increase throughput with cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) in the *Amazon Bedrock User Guide*.

## Responsible AI
<a name="manager-assist-responsible-ai"></a>
+ It inherits automated abuse detection from Amazon Bedrock.
+ Guardrails prevent the generation of harmful or off-topic content.
+ Responses are grounded in the metrics data in your Connect Customer instance.
+ The read-only architecture prevents unintended modifications to your instance.