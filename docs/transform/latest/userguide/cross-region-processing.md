

# Cross-region processing in AWS Transform
<a name="cross-region-processing"></a>

The following sections describe how cross-region inference and cross-region calls are used to provide the AWS Transform service. 

## Cross-region inference
<a name="cross-region-inference"></a>

AWS Transform is powered by Amazon Bedrock, and uses cross-region inference to distribute traffic across different AWS Regions to enhance large language model (LLM) inference performance and reliability. With cross-region inference, you get:
+ Increased throughput and resilience during high demand periods
+ Improved performance 
+ Access to newly launched AWS Transform capabilities and features that rely on the most powerful LLMs hosted on Amazon Bedrock

Cross-region inference requests are kept within the AWS Regions that are part of the geography where the data originally resides. For example, a request made from a AWS Transform configuration in the US is kept within the AWS Regions in the US. Although cross-region inferencing doesn’t change where your data is stored, your requests and output results may move outside of the Region where the data originally resides. All data will be encrypted while transmitted across Amazon's secure network. There's no additional cost for using cross-region inference. 

Cross region inference doesn’t affect where your data is stored. For information on where data is stored when you use AWS Transform, see [Data protection in AWS Transform](data-protection.md). 

### Supported regions for AWS Transform cross-region inference
<a name="inference-regions"></a>

Certain requests you make to AWS Transform might require cross-region calls. The following table describes what Regions your requests may be routed to depending on the geography where the request originated. 


| Source Region | Destination Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (Paris) (eu-west-3) | 
| Asia Pacific (Mumbai) (ap-south-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Seoul) (ap-northeast-2)<br />Asia Pacific (Osaka) (ap-northeast-3)<br />Asia Pacific (Mumbai) (ap-south-1)<br />Asia Pacific (Hyderabad) (ap-south-2)<br />Asia Pacific (Singapore) (ap-southeast-1)<br />Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3) | 
| Asia Pacific (Seoul) (ap-northeast-2) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Seoul) (ap-northeast-2)<br />Asia Pacific (Osaka) (ap-northeast-3)<br />Asia Pacific (Mumbai) (ap-south-1)<br />Asia Pacific (Hyderabad) (ap-south-2)<br />Asia Pacific (Singapore) (ap-southeast-1)<br />Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Europe (London) (eu-west-2) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2)<br />Europe (Paris) (eu-west-3) | 
| Canada (Central) (ca-central-1) | Commercial AWS Regions \+ Canada (Central) (ca-central-1) | 
| South America (São Paulo) (sa-east-1) | Commercial AWS Regions \+ South America (São Paulo) (sa-east-1) | 

For a complete list of Regions where you can use AWS Transform, see [Supported Regions for AWS Transform](regions.md).

## Cross-Region knowledge
<a name="cross-region-knowledge"></a>

When you ask a general question about AWS Transform services, transformation workflows, or related AWS documentation, AWS Transform might make cross-region requests to US East (Virginia) (us-east-1) for US regions or Europe (Frankfurt) (eu-central-1) for all other regions to retrieve documentation and fulfill your request. For example, when you ask questions about how to use other AWS services such as Lambda, AWS Transform might make a cross-region call to retrieve relevant AWS documentation to respond to your question. The following table describes what Regions your requests may be routed to depending on the geography where the request originated.


| Source Region | Destination Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1) | 
| Europe (London) (eu-west-2) | Europe (Frankfurt) (eu-central-1) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Europe (Frankfurt) (eu-central-1) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Europe (Frankfurt) (eu-central-1) | 
| Asia Pacific (Seoul) (ap-northeast-2) | Europe (Frankfurt) (eu-central-1) | 
| Asia Pacific (Mumbai) (ap-south-1) | Europe (Frankfurt) (eu-central-1) | 
| Canada (Central) (ca-central-1) | Europe (Frankfurt) (eu-central-1) | 
| South America (São Paulo) (sa-east-1) | Europe (Frankfurt) (eu-central-1) | 

This setting is enabled by default. An account administrator can modify this setting. Disabling this feature results in the loss of access to features that require AWS Transform to retrieve knowledge from other regions. This might result in less accurate responses. 

To disable cross-region calls made by AWS Transform:

1. When first setting up AWS Transform, navigate to the **Get Started** page and complete the configuration. For for an existing AWS Transform configuration, navigate to the **Settings** page.

1. Toggle **Enable cross-region calls to answer general AWS related questions** to the *off* position.

## AWS Transform for Windows cross-region inference
<a name="cross-region-windows"></a>

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:


| Source Region | Inference Destination Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (Paris) (eu-west-3) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Seoul) (ap-northeast-2) | All commercial regions | 
| Asia Pacific (Mumbai) (ap-south-1) | All commercial regions | 
| Canada (Central) (ca-central-1) | All commercial regions | 

## AWS Transform for Migrations cross-region inference
<a name="cross-region-migrations"></a>

The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:


| Source Region | Inference Destination Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | All commercial regions | 
| Europe (Frankfurt) (eu-central-1) | All commercial regions | 
| Europe (London) (eu-west-2) | All commercial regions | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Seoul) (ap-northeast-2) | All commercial regions | 
| Asia Pacific (Mumbai) (ap-south-1) | All commercial regions | 
| Canada (Central) (ca-central-1) | All commercial regions | 

## AWS Transform for mainframe cross-region inference
<a name="cross-region-mainframe"></a>

AWS Transform for mainframe uses Amazon Bedrock geographic cross-region inference. This means that some of your calls might be routed to AWS Regions outside of your source region. The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:


| Source Region | Inference Destination Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (Paris) (eu-west-3) | 
| Europe (London) (eu-west-2) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2)<br />Europe (Paris) (eu-west-3) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Seoul) (ap-northeast-2) | All commercial regions | 
| Asia Pacific (Mumbai) (ap-south-1) | All commercial regions | 
| Canada (Central) (ca-central-1) | Canada (Central) (ca-central-1)<br />US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| South America (São Paulo) (sa-east-1) | All commercial regions | 

## AWS Transform Custom
<a name="cross-region-custom"></a>

AWS Transform custom uses Amazon Bedrock geographic cross-region inference. This means that some of your calls might be routed to AWS Regions outside of your source region. The following table shows the source Regions from which you can call the inference profile and the destination Regions to which the requests can be routed:


| Source Region | Inference Destination Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (Paris) (eu-west-3) | 
| Europe (London) (eu-west-2) | Europe (Frankfurt) (eu-central-1)<br />Europe (Stockholm) (eu-north-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Spain) (eu-south-2)<br />Europe (Ireland) (eu-west-1)<br />Europe (London) (eu-west-2)<br />Europe (Paris) (eu-west-3) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | All commercial regions | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Seoul) (ap-northeast-2) | All commercial regions | 
| Asia Pacific (Mumbai) (ap-south-1) | All commercial regions | 
| Canada (Central) (ca-central-1) | Canada (Central) (ca-central-1)<br />US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 