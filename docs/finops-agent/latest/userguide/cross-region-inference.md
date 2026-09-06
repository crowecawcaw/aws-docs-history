

AWS FinOps Agent is in preview release and is subject to change.

# Amazon Bedrock usage and cross-region inference
<a name="cross-region-inference"></a>

During preview, AWS FinOps Agent runs in the US East (N. Virginia) Region (`us-east-1`). Your data, including context files, conversations, memory, and artifacts, remains stored in `us-east-1`.

AWS FinOps Agent uses Amazon Bedrock cross-region inference to improve performance and reliability. Cross-region inference requests are kept within the geography where the request originated. For example, requests from AWS Regions in the United States stay within AWS Regions in the United States. Agent inference may be processed outside the specific Region but remains within the same geography. All data is encrypted in transit. Cross-region inference does not change where your data is stored.