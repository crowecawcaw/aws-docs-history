

# Geographic cross-region inference in AWS Agent Registry
<a name="registry-cross-region-inference"></a>

 AWS Agent Registry (Agent Registry) uses inference to generate embeddings for your registry record data. Agent Registry uses these embeddings for semantic matching when you run a hybrid or semantic search.

With geographic cross-region inference, Agent Registry optimizes compute and model availability for embedding generation and semantic matching. Your semantic searches stay responsive, even during periods of high demand. To do this, Agent Registry might use compute and inference resources outside your current AWS Region, but always within your broader geography, such as the US, Europe, or Asia Pacific. For example, a request made in US East (N. Virginia) (us-east-1) might be served from US East (Ohio) (us-east-2), but is always served from within the United States.

Your data remains stored only in the AWS Region where it originally resides. Your input prompts and output results can move to another AWS Region within the same geography for processing. Encryption protects all data in transit across the secure Amazon network.

For more information about geographic cross-region inference, see [Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html) in the *Amazon Bedrock User Guide*.

**Note**  
There is no additional cost for using cross-region inference. Amazon CloudWatch and AWS CloudTrail logs won’t specify the AWS Region in which inference occurs.

## Supported Regions
<a name="registry-cross-region-inference-supported-regions"></a>

The following Regions support Agent Registry with geographic cross-region inference, grouped by geography. Inference requests that originate in a Region stay within that Region’s geography.

 **Canada** 
+ Canada - Central (ca-central-1)

 **United States** 
+ US East - N. Virginia (us-east-1)
+ US East - Ohio (us-east-2)
+ US West - Oregon (us-west-2)

 **Europe** 
+ Europe - Frankfurt (eu-central-1)
+ Europe - Ireland (eu-west-1)
+ Europe - London (eu-west-2)

 **Asia Pacific** 
+ Asia Pacific - Tokyo (ap-northeast-1)
+ Asia Pacific - Sydney (ap-southeast-2)