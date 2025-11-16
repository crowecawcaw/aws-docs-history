# How inference works in Amazon Bedrock

When you submit an input to a model, the model predicts a probable sequence of tokens that follows, and returns that sequence as the output. Amazon Bedrock provides you the capability of running inference with the foundation model of your choice. When you run inference, you provide the following inputs:

- **Prompt** – An input provided to the model in
  order for it to generate a response. For information about writing prompts, see
  [Prompt engineering concepts](prompt-engineering-guidelines.md "prompt-engineering-guidelines.md"). For information about
  protecting against prompt injection attacks, see [Prompt injection security](prompt-injection.md "prompt-injection.md").
- **Model** – You make requests to a model to run inference on a prompt. The model that you choose also specifies a level of throughput, which defines the number and rate of input and output tokens that you can process. You can make requests to the following types of models:
  - **Base model** – A foundation model to run inference with. Requests are sent to a single AWS Region. For model IDs, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md"). For more information about the foundation models that are available in Amazon Bedrock, see [Amazon Bedrock foundation model information](foundation-models-reference.md "foundation-models-reference.md").
  - **Inference profile** – A foundation model to run inference with. Requests are made to the model in a multiple AWS Regions. For inference profile IDs, see [Supported Regions and models for inference profiles](inference-profiles-support.md "inference-profiles-support.md").

  ###### Note

  Models differ in their base model and inference profile availability by Region and by API method. For more information, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md") and individual model pages in the [Foundation model reference](foundation-models-reference.md "foundation-models-reference.md").
  - **Provisioned Throughput** – A foundation model for which you've purchased dedicated throughput. For more information, see [Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock](prov-throughput.md "prov-throughput.md")
  - **Custom model** – A foundation model whose weights have been modified through model customization. For more information, see [Customize your model to improve its performance for your use case](custom-models.md "custom-models.md").

- **Inference parameters** – A set of values that can be adjusted to limit or influence the model response. For information about inference parameters, see [Influence response generation with inference parameters](inference-parameters.md "inference-parameters.md") and [Inference request parameters and response fields for foundation models](model-parameters.md "model-parameters.md").

## Invoking models in different AWS Regions

When you invoke a model, you choose the AWS Region in which to invoke it. The quotas for the frequency and size of the requests that you can make depend on the Region. You can find these quotas by searching for the following quotas at [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock"):

- On-demand model inference requests per minute for `${Model}`
- On-demand InvokeModel tokens per minute for `${Model}`

You can also invoke an inference profile instead of the foundation model itself. An inference profile defines a model and one or more Regions to which the inference profile can route model invocation requests. By invoking an inference profile that includes multiple Regions, you can increase your throughput. For more information, see [Increase throughput with cross-Region
inference](cross-region-inference.md "cross-region-inference.md"). To see the quotas for the frequency and size of the requests that you can make with an inference profile, search for the following quotas at [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock"):

- Cross-Region InvokeModel requests per minute for `${Model}`
- Cross-Region InvokeModel tokens per minute for `${Model}`
- Global Cross-Region InvokeModel requests per minute for `${Model}`
- Global Cross-Region InvokeModel tokens per minute for `${Model}`

Requests made to a Region may be served out of local zones that share the same parent Region. For example, requests made to US East (N. Virginia) (us-east-1) may be served out of any local zone associated with it, such as Atlanta, US (us-east-1-atl-2a).

The same principle applies when using cross-Region inference. For example, requests made to the US Anthropic Claude 3 Haiku inference profile may be served out of any local zone whose parent Region is in US, such as Seattle, US (us-west-2-sea-1a). When new local zones are added to AWS, they will be also be added to the corresponding cross-Region inference endpoint.

To see a list of local endpoints and the parent Regions they're associated with, see [AWS Local Zones Locations](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ "https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/").

When you invoke a cross-Region inference profile in Amazon Bedrock, your request originates from a source Region and is automatically routed to one of the destination Regions
defined in that profile, optimizing for performance. The destination Regions for Global cross-Region inference profile includes all commercial Regions.

Global cross-Region inference profile for a specific model can change over time as AWS adds more commercial Regions where your requests can be processed.
However, if an inference profile is tied to a geography (such as US, EU, or APAC), its destination Region list will never change. AWS might create new inference
profiles that incorporate new Regions. You can update your systems to use these inference profiles by changing the IDs in your setup to the new ones.

###### Note

The destination Regions in a cross-Region inference profile can include **opt-in Regions**, which are Regions that you must
explicitly enable at AWS account or Organization level. To learn more, see [Enable or disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md").
When using a cross-Region inference profile, your inference request can be routed to any of the destination Regions in the profile, even if you did not opt-in to such Regions in your account.

Service Control Policies (SCPs) and AWS Identity and Access Management (IAM) policies work together to control where cross-Region inference is allowed. Using SCPs, you can control which
Regions Amazon Bedrock can use for inference, and using IAM policies, you can define which users or roles have permission to run inference. If any destination Region in a
cross-Region inference profile is blocked in your SCPs, the request will fail even if other Regions remain allowed. To ensure efficient operation with cross-region inference,
you can update your SCPs and IAM policies to allow all required Amazon Bedrock inference actions (for example, `bedrock:InvokeModel*` or `bedrock:CreateModelInvocationJob`)
in all destination Regions included in your chosen inference profile. To learn more, see [https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/](https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/ "https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/")Enabling Amazon Bedrock cross-Region inference in multi-account environments.
