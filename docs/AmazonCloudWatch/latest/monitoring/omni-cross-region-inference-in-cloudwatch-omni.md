

# Cross-Region inference in CloudWatch Omni
<a name="omni-cross-region-inference-in-cloudwatch-omni"></a>

CloudWatch Omni includes features that use artificial intelligence (AI), such as the Omni agent, AI-assisted dashboard creation, and evaluations that score agent behavior with a judge model. When you use one of these features, CloudWatch Omni sends data from your space, such as telemetry content and your natural language input, to a large language model. CloudWatch Omni uses cross-Region inference to distribute that traffic across AWS Regions.

Your data remains stored only in your space's Region. When you use a feature that uses AI, your input and output might be processed outside of your space's Region. All data is transmitted encrypted across Amazon's secure network, using a minimum of TLS 1.2.

For most space Regions, CloudWatch Omni uses geographic inference profiles, which keep processing within the geography that your space's Region belongs to:
+ Requests from a space in the United States are processed within the United States.
+ Requests from a space in Canada are processed within Canada or the United States.
+ Requests from a space in Europe are processed within Europe. Europe (London) is a possible inference Region only for requests from a space in Europe (London).
+ Requests from a space in Australia are processed within Australia.
+ Requests from a space in Japan are processed within Japan.

For how to control what content reaches your telemetry, see [Protect sensitive data](omni-data-protection.md). For how evaluations use judge models, see [Evaluators and evaluations](omni-agents-evaluators.md). For how CloudWatch Omni and the AWS services it calls on your behalf use your content, see [Opting out of using your data for service improvement](omni-opting-out-of-using-your-data-for-service-improvement.md).

## Global cross-Region inference for specific Regions
<a name="omni-cross-region-inference-in-cloudwatch-omni-global-cross-region-inference-for-specific-regions"></a>

For spaces in the following Regions, the geography-based routing described previously doesn't apply. Instead, CloudWatch Omni selects the optimal Region globally to process your requests.
+ Asia Pacific (Mumbai) – `ap-south-1`
+ Asia Pacific (Singapore) – `ap-southeast-1`
+ South America (São Paulo) – `sa-east-1`

## Where your requests are processed
<a name="omni-cross-region-inference-in-cloudwatch-omni-where-your-requests-are-processed"></a>

The following table shows which Regions can process requests from each space Region. The possible inference Regions are the destinations of the cross-Region inference profile, and can include AWS Regions where CloudWatch Omni itself is not available.


| Supported CloudWatch Omni geography | Space Region | Possible inference Regions | 
| --- | --- | --- | 
| United States (US) | US East (N. Virginia) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| United States (US) | US West (Oregon) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| Canada | Canada (Central) | Canada (Central), US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| Europe (EU) | Europe (Frankfurt) | Europe (Frankfurt), Europe (Ireland), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm) | 
| Europe (EU) | Europe (Ireland) | Europe (Frankfurt), Europe (Ireland), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm) | 
| Europe (EU) | Europe (London) | Europe (Frankfurt), Europe (Ireland), Europe (London), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm) | 
| Australia | Asia Pacific (Sydney) | Asia Pacific (Melbourne), Asia Pacific (Sydney) | 
| Japan | Asia Pacific (Tokyo) | Asia Pacific (Osaka), Asia Pacific (Tokyo) | 
| Global | Asia Pacific (Mumbai) | Selected globally | 
| Global | Asia Pacific (Singapore) | Selected globally | 
| Global | South America (São Paulo) | Selected globally | 

## Models that you choose
<a name="omni-cross-region-inference-in-cloudwatch-omni-models-that-you-choose"></a>

You choose the model in the prompt playground and when you configure an evaluator. CloudWatch Omni lists the foundation models and cross-Region inference profiles that are available to you in your Region, and calls the model you select with your own credentials, in your own account.

The list includes global inference profiles. If you select a global inference profile, the optimal Region to process your request is selected globally rather than only within your geography.

To restrict which Regions can process these requests, use IAM permissions on inference profiles or service control policies in your own account. For the managed policy that grants model inference, see [IAM policies to use CloudWatch Omni](omni-iam-policies-to-use-cloudwatch-omni.md).