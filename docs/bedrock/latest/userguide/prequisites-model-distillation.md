# Choose teacher and student models for distillation

For Model Distillation, you choose a teacher and student model.

- **Choose a teacher model**

Choose a teacher model that's significantly larger and more capable than the student model, and
whose accuracy you want to achieve for your use case. To make distillation more effective, choose a
model that's already trained on tasks similar to your use case.

For some teacher models, you can choose a Cross-Region inference profile ([Increase throughput with cross-Region
inference](cross-region-inference.md "cross-region-inference.md")).
Cross-Region inference automatically selects the optimal AWS Region
within your geography to process your inference request. This improves customer experience by
maximizing available resources and model availability. To use a Cross-Region inference profile, your service role must
have permissions to invoke the inference profile in an AWS Region, in addition to the model in each Region
in the inference profile. For a policy example, see [(Optional) Permissions to create a Distillation job with a cross-region inference profile](custom-model-job-access-security.md#custom-models-cross-region-inference-profile-permissions "custom-model-job-access-security.md#custom-models-cross-region-inference-profile-permissions").

- **Choose a student model**

Choose a student model that's significantly smaller in size than the teacher model. The student model must be one of the student models paired with your teacher model in the following table.
The following section lists the supported models and regions for Amazon Bedrock Model Distillation.
After you choose your teacher and student models, you prepare and optimize your training datasets
for distillation. For more information, see [Prepare your training datasets for
distillation](distillation-prepare-datasets.md "distillation-prepare-datasets.md").

## Supported models and Regions for Amazon Bedrock Model Distillation

The following table shows which models and AWS Regions Amazon Bedrock Model Distillation supports for teacher and student
models. If you use a Cross Region Inference Profile, only System Inference Profiles are supported for model distillation.
For more information, see [Increase throughput with cross-Region
inference](cross-region-inference.md "cross-region-inference.md").

| Provider      | Teacher                                   | Teacher ID                                | Inference profile support            | Student                                                                                                   | Student ID                                                                                                                                     | Region                |
| ------------- | ----------------------------------------- | ----------------------------------------- | ------------------------------------ | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Amazon        | Nova Pro                                  | amazon.nova-pro-v1:0                      | Both                                 | Nova LiteNova Micro                                                                                       | amazon.nova-lite-v1:0:300kamazon.nova-micro-v1:0:128k                                                                                          | US East (N. Virginia) |
| Nova Premier  | amazon.nova-premier-v1:0                  | Inference profile only                    | Nova LiteNova MicroNova Pro          | amazon.nova-lite-v1:0:300kamazon.nova-micro-v1:0:128kamazon.nova-pro-v1:0:300k                            | US East (N. Virginia)                                                                                                                          |
| Anthropic     | Claude 3.5 v1                             | anthropic.claude-3-5-sonnet-20240620-v1:0 | Both                                 | Claude 3 Haiku                                                                                            | anthropic.claude-3-haiku-20240307-v1:0:200k                                                                                                    | US West (Oregon)      |
| Claude 3.5 v2 | anthropic.claude-3-5-sonnet-20241022-v2:0 | Both                                      | Claude 3 Haiku                       | anthropic.claude-3-haiku-20240307-v1:0:200k                                                               | US West (Oregon)                                                                                                                               |
| Meta          | Llama 3.1 405B                            | meta.llama3-1-405b-instruct-v1:0          | On demand                            | Llama 3.1 8BLlama 3.1 70BLlama 3.2 1BLlama 3.3 70B                                                        | meta.llama3-1-8b-instruct-v1:0:128kmeta.llama3-1-70b-instruct-v1:0:128kmeta.llama3-2-1b-instruct-v1:0:128kmeta.llama3-3-70b-instruct-v1:0:128k | US West (Oregon)      |
| Llama 3.1 70B | meta.llama3-1-70b-instruct-v1:0           | Both                                      | Llama 3.1 8BLlama 3.2 1BLlama 3.2 3B | meta.llama3-1-8b-instruct-v1:0:128kmeta.llama3-2-1b-instruct-v1:0:128kmeta.llama3-2-3b-instruct-v1:0:128k | US West (Oregon)                                                                                                                               |
| Llama 3.3 70B | meta.llama3-3-70b-instruct-v1:0           | Inference profile only                    | Llama 3.1 8BLlama 3.2 1BLlama 3.2 3B | meta.llama3-1-8b-instruct-v1:0:128kmeta.llama3-2-1b-instruct-v1:0:128kmeta.llama3-2-3b-instruct-v1:0:128k | US West (Oregon)                                                                                                                               |

###### Note

- For Claude and Llama models, the distillation job is run in
  US West (Oregon). You can either buy [provisioned throughput](prov-throughput.md "prov-throughput.md") in
  US West (Oregon) or [copy distilled model](copy-model.md "copy-model.md") to another
  Region and then buy [provisioned
  throughput](prov-throughput.md "prov-throughput.md").
- For Nova models, you run distillation job in US East (N. Virginia). For
  inference, you need to buy [provisioned throughput](prov-throughput.md "prov-throughput.md") in
  US East (N. Virginia). You can't copy Nova models to other Regions.
