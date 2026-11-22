

# Cross-Region inference for Amazon Textract Insights

**Note**  
The Amazon Textract Core APIs process your data only in the AWS Region where you call them. Amazon Textract Insights can run inference in another AWS Commercial Region, as described in [Cross-Region inference](insights-cross-region.md).

Amazon Textract Insights uses cross-Region inference to automatically select the optimal AWS Region to process your inference requests. This maximizes available compute resources and model availability, and delivers the best customer experience. Amazon Textract Insights securely routes your inference requests to available compute resources within the geographic area where the request originated, as follows: inference requests originating in the United States are processed within the United States. Routing is automatic and requires no configuration.

During inference, your input and output might be processed outside that AWS Region. All data is transmitted encrypted across Amazon's secure network. Your input and output Amazon S3 buckets and any customer managed AWS KMS key stay in the AWS Region you call, so you configure IAM and AWS KMS the same way you would for a single-Region workflow.

Amazon Textract Insights checks your permissions only in the AWS Region you call. It also reads your input, writes your output, and uses your AWS KMS key only in that AWS Region. You don't need to grant IAM permissions in the other AWS Regions where inference runs. A service control policy that denies other AWS Regions, for example one that uses `aws:RequestedRegion`, doesn't block cross-Region inference as long as it allows the AWS Region you call.

AWS CloudTrail records Amazon Textract Insights API calls, such as `StartDocumentInsights` and `GetDocumentInsights`, in the AWS Region you call, even when inference runs in another AWS Region. Amazon S3 and AWS KMS events for your input, output, and key are also recorded in that AWS Region. CloudTrail events don't identify the AWS Region where inference ran.

For the AWS Regions where each request can be processed, see [Cross-Region inference](insights-cross-region.md). For how routing affects job latency, see [Performance and latency best practices](insights-performance.md).