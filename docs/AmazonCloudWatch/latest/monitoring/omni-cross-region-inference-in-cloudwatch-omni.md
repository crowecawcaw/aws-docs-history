

# Cross-Region inference in CloudWatch Omni
<a name="omni-cross-region-inference-in-cloudwatch-omni"></a>

CloudWatch Omni includes features that use artificial intelligence (AI), such as the Omni agent, AI-assisted dashboard creation, and evaluations that score agent behavior with a judge model. When you use one of these features, CloudWatch Omni sends data from your space, such as telemetry content and your natural language input, to a large language model. CloudWatch Omni uses cross-Region inference to distribute that traffic across AWS Regions.

Your data remains stored only in your space's Region. When you use a feature that uses AI, your input and output might be processed outside of your space's Region. All data is transmitted encrypted across Amazon's secure network, using a minimum of TLS 1.2.

CloudWatch Omni uses geographic inference profiles, which keep processing within the geography that your space's Region belongs to. A request from a Region in the United States is processed in Regions in the United States, and a request from a Region in Europe is processed in Regions in Europe.

For how to control what content reaches your telemetry, see [Protect sensitive data](omni-data-protection.md). For how evaluations use judge models, see [Evaluators and evaluations](omni-agents-evaluators.md). For how CloudWatch Omni and the AWS services it calls on your behalf use your content, see [Opting out of using your data for service improvement](omni-opting-out-of-using-your-data-for-service-improvement.md).

**Where your requests are processed**

The following table shows which Regions can process requests from each space Region. The possible inference Regions are the destinations of the cross-Region inference profile, and can include AWS Regions where CloudWatch Omni itself is not available.


| Supported CloudWatch Omni geography | Space Region | Possible inference Regions | 
| --- | --- | --- | 
| United States (US) | US East (N. Virginia) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
|  | US West (Oregon) | US East (N. Virginia), US East (Ohio), US West (Oregon) | 
| Europe (EU) | Europe (Ireland) | Europe (Frankfurt), Europe (Ireland), Europe (Milan), Europe (Paris), Europe (Spain), Europe (Stockholm) | 

**Models that you choose**

You choose the model in the prompt playground and when you configure an evaluator. CloudWatch Omni lists the foundation models and cross-Region inference profiles that are available to you in your Region, and calls the model you select with your own credentials, in your own account.

The list includes global inference profiles. If you select a global inference profile, your request can be processed in any supported commercial AWS Region rather than only within your geography.

To restrict which Regions can process these requests, use IAM permissions on inference profiles or service control policies in your own account. For the managed policy that grants model inference, see [IAM policies to use CloudWatch Omni](omni-iam-policies-to-use-cloudwatch-omni.md).