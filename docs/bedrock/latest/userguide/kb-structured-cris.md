# Cross-region inference for knowledge bases with structured data store

Starting May 10, 2026, Amazon Bedrock Knowledge Bases with structured data store will use cross-region
inference to process your API requests. With cross-Region inference, Amazon Bedrock Knowledge Bases will select a
AWS Region within your geography to process your inference request. This applies
to the [GenerateQuery](bedrock/latest/APIReference/API_agent-runtime_GenerateQuery.md "bedrock/latest/APIReference/API_agent-runtime_GenerateQuery.md"),
[Retrieve](bedrock/latest/APIReference/API_agent-runtime_Retrieve.md "bedrock/latest/APIReference/API_agent-runtime_Retrieve.md"), and
[RetrieveAndGenerate](bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md "bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.md")
API operations when used with a structured data store.

Cross-region inference requests stay within the AWS Regions that are part of the
geography where your data originally resides. For example, a request made within the US is
kept within AWS Regions in the US. Although your knowledge base data remains stored only
in the primary Region, input prompts and output results may be processed in another Region
within the same geography. All data is transmitted encrypted across Amazon's secure
network.

For the following Regions, geo-specific cross-region inference is not available, and
inference requests may be processed in Regions outside of the local geography:

- Asia Pacific (Seoul) (`ap-northeast-2`)
- Asia Pacific (Mumbai) (`ap-south-1`)
- Asia Pacific (Singapore) (`ap-southeast-1`)
- South America (São Paulo) (`sa-east-1`)

###### Note

There is no additional cost for using cross-region inference with knowledge bases
with structured data store.

Cross-region inference is automatically enabled for all knowledge bases with structured
data store. No configuration changes are required. For more information about cross-region
inference and supported Regions, see
[Route model inference requests across AWS Regions with cross-Region inference](cross-region-inference.md "cross-region-inference.md").
