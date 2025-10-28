# Increase throughput with cross-Region inference

With cross-Region inference, you can choose either a cross-Region inference profile tied to a specific geography (such as US or EU), or you can choose a global inference profile.
When you choose an inference profile tied to a specific geography, Amazon Bedrock automatically selects the optimal commercial AWS Region within that geography to process your
inference request. With global inference profiles, Amazon Bedrock automatically selects the optimal commercial AWS Region to process the request, which optimizes
available resources and increases model throughput.

When running model inference in on-demand mode, your requests might be restricted by service quotas or during peak usage times. Cross-Region inference
enables you to seamlessly manage unplanned traffic bursts by utilizing compute across different AWS Regions. With cross-Region inference, you can
distribute traffic across multiple AWS Regions, enabling higher throughput.

You can also increase throughput for a model by purchasing [Provisioned Throughput](prov-throughput.md "prov-throughput.md"). Inference profiles currently don't support Provisioned Throughput.

To see the Regions and models with which you can use inference profiles to run cross-Region inference, refer to [Supported Regions and models for inference profiles](inference-profiles-support.md "inference-profiles-support.md").

Cross-region (system-defined) inference profiles are named after the model that they support and defined by the Regions that they support. To understand how a cross-region inference profile handles your requests, review the following definitions:

- **Source Region** – The Region from which you make the API request that specifies the inference profile.
- **Destination Region** – A Region to which the Amazon Bedrock service can route the request from your source Region.
  When you invoke a cross-Region inference profile in Amazon Bedrock, your request originates from a source Region and is automatically routed to one of the destination Regions defined in that profile, optimizing for performance. The destination Regions for Global cross-Region inference profiles include all commercial Regions.

###### Note

The destination Regions in a cross-Region inference profile can include _opt-in Regions_, which are Regions that you must explicitly enable at AWS account or Organization level.
To learn more, see [Enable or disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md"). When using a cross-Region inference profile,
your inference request can be routed to any of the destination Regions in the profile, even if you did not opt-in to such Regions in your account.

Service Control Policies (SCPs) and AWS Identity and Access Management (IAM) policies work together to control where cross-Region inference is allowed. Using SCPs,
you can control which Regions Amazon Bedrock can use for inference, and using IAM policies, you can define which users or roles have permission to run inference.
If any destination Region in a cross-Region inference profile is blocked in your SCPs, the request will fail even if other Regions remain allowed. To
ensure efficient operation with cross-region inference, you can update your SCPs and IAM policies to allow all required Amazon Bedrock inference actions
(for example, `bedrock:InvokeModel*` or `bedrock:CreateModelInvocationJob`) in all destination Regions included in your chosen
inference profile. To learn more, see [Enabling Amazon Bedrock cross-Region inference in multi-account environments.](https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/ "https://aws.amazon.com/blogs/machine-learning/enable-amazon-bedrock-cross-region-inference-in-multi-account-environments/")

###### Note

Some inference profiles route to different destination Regions depending on the source Region from which you call it. For example, if you call `us.anthropic.claude-3-haiku-20240307-v1:0` from US East (Ohio), it can route requests to `us-east-1`, `us-east-2`, or `us-west-2`, but if you call it from US West (Oregon), it can route requests to only `us-east-1` and `us-west-2`.

To check the source and destination Regions for an inference profile, you can do one of the following:

- Expand the corresponding section in the [list of supported cross-region inference profiles](inference-profiles-support.md "inference-profiles-support.md").
- Send a [GetInferenceProfile](../APIReference/API_GetInferenceProfile.md "../APIReference/API_GetInferenceProfile.md") request with an [Amazon Bedrock control plane endpoint](../../../general/latest/gr/bedrock.md#br-cp "../../../general/latest/gr/bedrock.md#br-cp") from a source Region and specify the Amazon Resource Name (ARN) or ID of the inference profile in the `inferenceProfileIdentifier` field. The `models` field in the response maps to a list of model ARNs, in which you can identify each destination Region.

###### Note

Global cross-Region inference profile for a specific model can change over time as AWS adds more commercial Regions where your requests can be processed.
However, if an inference profile is tied to a geography (such as US, EU, or APAC), its destination Region list will never change. AWS might create new inference
profiles that incorporate new Regions. You can update your systems to use these inference profiles by changing the IDs in your setup to the new ones.

The Global cross-region inference profile is currently only supported on Anthropic Claude Sonnet 4 model for the following source Regions:
US West (Oregon), US East (N. Virginia), US East (Ohio), Europe (Ireland), and Asia Pacific (Tokyo). The destination Regions for Global inference profile
include all commercial AWS Regions.

Note the following information about cross-Region inference:

- There's no additional routing cost for using cross-Region inference. The price is calculated based on the Region from which you call an inference profile. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
- Global Cross-Region inference profiles provide higher throughput than an inference profile tied to a particular geography. An inference profile
  tied to a particular geography offers higher throughput than single-region inference.
- To see the default quotas for cross-Region throughput when using inference profiles tied to a geography (such as US, EU and APAC), refer to the
  **Cross-region model inference requests per minute for ${Model}** and **Cross-region model inference tokens per minute for ${Model}**
  values in [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") in the _AWS General Reference_.
- To see the default quotas for cross-Region throughput when using Global inference profiles, refer to the **Global Cross-region model inference requests
  per minute for ${Model}** and **Global Cross-region model inference tokens per minute for ${Model}** values in
  [Amazon Bedrock service quotas](../../../general/latest/gr/bedrock.md#limits_bedrock "../../../general/latest/gr/bedrock.md#limits_bedrock") in the _AWS General Reference_.

You can request, view, and manage quotas for the Global Cross-Region Inference Profile from the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/bedrock/quotas?region=us-east-1 "https://console.aws.amazon.com/servicequotas/home/services/bedrock/quotas?region=us-east-1")
or by using AWS CLI commands in the **US East (N. Virginia) Region**.
Note that Global Cross-Region inference quotas will not appear in the Service Quotas console or AWS CLI for other source Regions listed in the Global Inference Profile.

- Cross-Region inference requests to an inference profile tied to a geography (e.g. US, EU and APAC) are kept within the AWS Regions that are part of the
  geography where the data originally resides. For example, a request made within the US is kept within the AWS Regions in the US. Although the data remains
  stored only in the source Region, your input prompts and output results might move outside of your source Region during cross-Region inference. All data will
  be transmitted encrypted across Amazon’s secure network.
- AWS Services powered by Amazon Bedrock may also use CRIS. See service-specific documentation for more details.

## Use a cross-Region (system-defined) inference profile

To use cross-Region inference, you include an [inference profile](inference-profiles.md "inference-profiles.md") when running model inference in the following ways:

- **On-demand model inference** – Specify the ID of the inference profile as the `modelId` when sending an [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md"), [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md"), [Converse](../APIReference/API_runtime_Converse.md "../APIReference/API_runtime_Converse.md"), or [ConverseStream](../APIReference/API_runtime_ConverseStream.md "../APIReference/API_runtime_ConverseStream.md") request. An inference profile defines one or more Regions to which it can route inference requests originating from your source Region. Use of cross-Region inference increases throughput and performance by dynamically routing model invocation requests across the Regions defined in inference profile. Routing factors in user traffic, demand and utilization of resources. For more information, see [Submit prompts and generate responses with model inference](inference.md "inference.md")
- **Batch inference** – Submit requests asynchronously with batch inference by specifying the ID of the inference profile as the `modelId` when sending a [CreateModelInvocationJob](../APIReference/API_CreateModelInvocationJob.md "../APIReference/API_CreateModelInvocationJob.md") request. Using an inference profile lets you utilize compute across multiple AWS Regions and achieve faster processing times for your batch jobs. After the job is complete, you can retrieve the output files from the Amazon S3 bucket in the source Region.
- **Agents** – Specify the ID of the inference profile in the `foundationModel` field in a [CreateAgent](../APIReference/API_agent_CreateAgent.md "../APIReference/API_agent_CreateAgent.md") request. For more information, see [Create and configure agent manually](agents-create.md "agents-create.md").
- **Knowledge base response generation** – You can use cross-Region inference when generating a response after querying a knowledge base. For more information, see [Test your knowledge base with queries and responses](knowledge-base-test.md "knowledge-base-test.md").
- **Model evaluation** – You can submit an inference profile as a model to evaluate when submitting a model evaluation job. For more information, see [Evaluate the performance of Amazon Bedrock resources](evaluation.md "evaluation.md").
- **Prompt management** – You can use cross-Region inference when generating a response for a prompt you created in Prompt management. For more information, see [Construct and store reusable prompts with Prompt management in Amazon Bedrock](prompt-management.md "prompt-management.md")
- **Prompt flows** – You can use cross-Region inference when generating a response for a prompt you define inline in a prompt node in a prompt flow. For more information, see [Build an end-to-end generative AI workflow with Amazon Bedrock Flows](flows.md "flows.md").

###### Note

Global inference profile is supported for On-demand model inference, Batch inference, Agents, Model evaluation, Prompt management, and Prompt flows.

To learn how to use an inference profile to send model invocation requests across Regions, see [Use an inference profile in model invocation](inference-profiles-use.md "inference-profiles-use.md").

To learn more about cross-Region inference, see [Getting started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/").
