

# AI in Connect Customer
<a name="ai-in-connect"></a>

Connect Customer includes features that use AI, such as contact summarization, semantic rule matching, and performance evaluations. These features use AI models through [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html).

## Amazon Bedrock
<a name="ai-bedrock"></a>

Amazon Bedrock is a managed service that provides AI models from leading AI companies and Amazon. Amazon Bedrock includes a broad set of capabilities to use AI models with security and privacy. The models available on Amazon Bedrock never store, log, or share customer prompts (input) and responses (output), and never use this data to train these models.

For more information about how Amazon Bedrock protects your data, refer to [Data Protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) in the Amazon Bedrock documentation.

## Model selection
<a name="ai-model-selection"></a>

For many features, Connect Customer fully manages the underlying AI, including model selection, prompt definition, and capacity provisioning. These features will change the underlying model over time to unlock new capabilities, improve feature performance, and ensure feature availability as existing models approach [end of life](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html).

## Cross-region inference
<a name="ai-cross-region-inference"></a>

Model inference is the process of a model generating an output (response) from a given input (prompt). To use an optimal model for each feature, Connect Customer might use [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for data processing. This means Connect Customer will automatically select the optimal AWS Region to process inference requests. The available AWS Regions vary based on the Region of your Connect Customer instance. All data is transmitted encrypted across Amazon's secure network and does not traverse the public internet.

The following tables lists the Inference regions that a Connect Customer instance might use:


| Connect Customer Instance Region | Inference Regions | 
| --- | --- | 
| US East (N. Virginia) (us-east-1) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| US West (Oregon) (us-west-2) | US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Africa (Cape Town) (af-south-1) | Africa (Cape Town) (af-south-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Seoul) (ap-northeast-2) | Asia Pacific (Seoul) (ap-northeast-2)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Singapore) (ap-southeast-1) | Asia Pacific (Singapore) (ap-southeast-1)<br />[Commercial AWS Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#available-regions) | 
| Asia Pacific (Sydney) (ap-southeast-2) | Asia Pacific (Sydney) (ap-southeast-2)<br />Asia Pacific (Melbourne) (ap-southeast-4) | 
| Asia Pacific (Tokyo) (ap-northeast-1) | Asia Pacific (Tokyo) (ap-northeast-1)<br />Asia Pacific (Osaka) (ap-northeast-3) | 
| Canada (Central) (ca-central-1) | Canada (Central) (ca-central-1)<br />US East (N. Virginia) (us-east-1)<br />US East (Ohio) (us-east-2)<br />US West (Oregon) (us-west-2) | 
| Europe (Frankfurt) (eu-central-1) | Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| Europe (London) (eu-west-2) | Europe (London) (eu-west-2)<br />Europe (Frankfurt) (eu-central-1)<br />Europe (Ireland) (eu-west-1)<br />Europe (Milan) (eu-south-1)<br />Europe (Paris) (eu-west-3)<br />Europe (Spain) (eu-south-2)<br />Europe (Stockholm) (eu-north-1) | 
| AWS GovCloud (US-West) (us-gov-west-1) | AWS GovCloud (US-West) (us-gov-west-1)<br />AWS GovCloud (US-East) (us-gov-east-1) | 

### Agentic CX designer
<a name="ai-cross-region-inference-agentic-cx-designer"></a>

Certain nodes in the Agentic CX designer may use additional inference Regions. This applies only to the **User input** and **User choice** nodes. All other nodes in the Agentic CX designer use the inference Regions listed in the preceding table.

The **User input** and **User choice** nodes may use the following inference Regions:


| Connect Customer Instance Region | Inference Regions | 
| --- | --- | 
| Asia Pacific (Sydney) (ap-southeast-2) | AWS Regions in Asia Pacific | 
| Asia Pacific (Tokyo) (ap-northeast-1) | AWS Regions in Asia Pacific | 

## Regulatory compliance
<a name="ai-regulatory-compliance"></a>

Connect Customer and Amazon Bedrock are in-scope for many of [AWS compliance programs](https://aws.amazon.com/compliance/services-in-scope/). If you have specific questions regarding compliance, contact customer support.