

# Geographic cross-region inference in AWS Agent Registry
<a name="registry-cross-region-inference"></a>

 AWS Agent Registry (Agent Registry) uses inference to generate embeddings for your registry record data. Agent Registry uses these embeddings for semantic matching when you run a hybrid or semantic search.

With geographic cross-region inference, you get optimized compute and model availability for embedding generation and semantic matching. Your semantic searches stay responsive, even during periods of high demand. To do this, Agent Registry might use compute and inference resources outside your current AWS Region, but always within your broader geography, such as the US, the European Union (EU), or Asia Pacific. For example, US East (Ohio) might serve a request made in US East (N. Virginia), but an AWS Region within the United States always serves the request.

For requests that originate in an EU Region, such as Europe (Frankfurt) or Europe (Ireland), Agent Registry uses only AWS Regions within the EU. Europe (London) is outside the EU, so Agent Registry doesn’t process requests from EU Regions in Europe (London). Europe (London) and available AWS Regions within the EU might process requests that originate in Europe (London). For more information about cross-region inference for EU data processing, see [Unlocking AI flexibility in Europe: A guide to cross-region inference for EU data processing and model access](https://aws.amazon.com/blogs/machine-learning/unlocking-ai-flexibility-in-europe-a-guide-to-cross-region-inference-for-eu-data-processing-and-model-access/) on the * AWS Machine Learning Blog*.

Your data remains stored only in the AWS Region where it originally resides. Your input prompts and output results can move to another AWS Region within the same geography for processing. Encryption protects all data in transit across the secure Amazon network.

For more information about geographic cross-region inference, see [Geographic cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html) in the *Amazon Bedrock User Guide*.

**Note**  
There is no additional cost for using cross-region inference. Amazon CloudWatch and AWS CloudTrail logs won’t specify the AWS Region in which inference occurs.

## Supported Regions
<a name="registry-cross-region-inference-supported-regions"></a>

The following Regions support Agent Registry with geographic cross-region inference, grouped by geography:

 **Canada** 
+ Canada - Central (ca-central-1)

 **United States** 
+ US East - N. Virginia (us-east-1)
+ US East - Ohio (us-east-2)
+ US West - Oregon (us-west-2)

 **European Union (EU)** 
+ Europe - Frankfurt (eu-central-1)
+ Europe - Ireland (eu-west-1)

 **United Kingdom** 
+ Europe - London (eu-west-2)

 **Asia Pacific** 
+ Asia Pacific - Tokyo (ap-northeast-1)
+ Asia Pacific - Sydney (ap-southeast-2)