

# Cross-Region processing in the AWS assistant
<a name="cross-region-processing"></a>

## Request-processing Regions
<a name="request-processing-regions"></a>

The AWS assistant processes your requests in the following Regions:
+ At the Free tier, the AWS assistant processes requests in US East (N. Virginia).
+ At the Pro tier, the AWS assistant processes requests in US East (N. Virginia) by default. You can choose to process requests in Europe (Frankfurt) instead.

The Region selected in the AWS Management Console doesn't determine where the AWS assistant processes your requests.

## Cross-Region inference
<a name="cross-region-inference"></a>

The AWS assistant is powered by Amazon Bedrock. It uses cross-Region inference to distribute traffic across AWS Regions. This improves large language model (LLM) performance and reliability. With cross-Region inference, you get:
+ More throughput and resilience during periods of high demand
+ Better performance
+ Access to new capabilities that rely on the most capable LLMs hosted on Amazon Bedrock

Cross-Region inference keeps your requests within the Regions in the geography where your data resides. For example, a request from an Amazon Q Developer profile that you created in the United States stays within the United States Regions listed in [Inference Regions by geography](#inference-regions).

Some features and integrations might perform inference in Regions other than the Region where you created your profile.

Cross-Region inference doesn't change where your data is stored. However, your requests and results might move outside the Region where your data resides. The AWS assistant encrypts all data while it moves across the Amazon network. Cross-Region inference has no additional cost.

For information about where data is stored, see [Data storage in the AWS assistant](data-storage.md).

### Inference Regions by geography
<a name="inference-regions"></a>

The following list shows the Regions where the AWS assistant might route your requests, based on the geography where the request originated.

**Europe**  
Europe (Frankfurt) (`eu-central-1`), Europe (Stockholm) (`eu-north-1`), Europe (Ireland) (`eu-west-1`), and Europe (Paris) (`eu-west-3`)

**United States**  
US East (N. Virginia) (`us-east-1`), US East (Ohio) (`us-east-2`), and US West (Oregon) (`us-west-2`)

For the Regions where you can use the AWS assistant, see [Supported AWS Regions for the AWS assistant](regions.md).

## Cross-Region calls
<a name="cross-region-calls"></a>

Some requests require the AWS assistant to make API calls from one Region to another. For example, a question about resources in several Regions requires calls to each of those Regions. A response that needs information from a global AWS service endpoint can also result in calls outside the Region where your data is stored.

You can use IAM policies to deny actions that the AWS assistant performs on your behalf, including cross-Region calls. This also turns off capabilities that require calls on your behalf in the current Region. To restrict calls to specific Regions, use the `aws:RequestedRegion` global condition key. To restrict the actions that the AWS assistant calls, use the `aws:CalledVia` global condition key. For example policies, see [Identity-based policy examples for the AWS assistant](security-iam-examples.md).