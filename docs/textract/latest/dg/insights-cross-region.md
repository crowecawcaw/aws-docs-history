

# Cross-Region inference

Amazon Textract Insights uses cross-Region inference to route your requests to available compute in AWS Commercial Regions. You get improved throughput and resilience without any configuration. The Amazon Textract Core APIs continue to support in-Region processing and do not use cross-Region inference.

## How it works
<a name="insights-cr-how"></a>

With Amazon Textract Insights, your inference requests are automatically processed in the optimal AWS Region. This maximizes available compute resources and model availability, and delivers the best customer experience.

**Destination AWS Regions.** With Amazon Textract Insights, your inference requests are securely routed to available compute resources within the geographic area where the request originated. For example, inference requests originating in the United States are processed within the United States. The destination AWS Regions depend on the AWS Region you call and are listed in the following table.

**No configuration required.** Routing is handled automatically by the service. You do not select or pass a routing profile. Call the API in your AWS Region and the service resolves the appropriate inference destination for you.

## Where your data lives
<a name="insights-cr-data"></a>

During inference, your input and output might be processed outside the AWS Region where the request originated. All data is transmitted encrypted across Amazon's secure network.

The following table lists the inference destination AWS Regions that an Amazon Textract Insights customer might use for the corresponding source AWS Region.


**Inference destination AWS Regions by source AWS Region**  

| **Request source AWS Region** | **Inference destination AWS Regions** | 
| --- | --- | 
| US East (N. Virginia) (`us-east-1`) | US East (N. Virginia) (`us-east-1`)<br />US East (Ohio) (`us-east-2`)<br />US West (N. California) (`us-west-1`)<br />US West (Oregon) (`us-west-2`) | 
| US West (Oregon) (`us-west-2`) | US East (N. Virginia) (`us-east-1`)<br />US East (Ohio) (`us-east-2`)<br />US West (N. California) (`us-west-1`)<br />US West (Oregon) (`us-west-2`) | 

## Encryption and IAM are unaffected
<a name="insights-cr-encryption"></a>

Cross-Region inference does not change how encryption or access control are scoped:
+ Your Amazon S3 input and output locations remain in the AWS Region you call in. Buckets must be in the same AWS Region as the request.
+ A customer managed AWS KMS key remains scoped to your calling AWS Region.

Because routing is automatic and AWS Region-local for storage, you configure encryption and IAM exactly as you would for a single-Region workflow. See [Data protection and encryption](insights-data-protection.md).

## Latency under load
<a name="insights-cr-latency"></a>

During peak demand, cross-Region routing distributes work to the most available AWS Region in your geography for resilience. This improves overall throughput, but an individual job might see variable latency as a result. See [Performance and latency best practices](insights-performance.md).