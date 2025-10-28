# GENPERF03-BP01 Use managed solutions for model hosting and

customization

There are several industry-leading model providers, and each offers
different model families and sizes. When selecting a model,
consistent performance can be achieved by selecting the appropriate
model family and size for your use case.

**Desired outcome:** When
implemented, this best practice facilitates model hosting and
customization for highly performant generative AI workloads.

**Benefits of establishing this best
practice:**
[Use
serverless architectures](../framework/rel-dp.md "../framework/rel-dp.md") - Serverless architectures enable
the performance of infrastructure-bound workloads, without the
operational overhead.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Foundation models often require customization to suit your domain.
The recommended approach to initially adapt a domain is through
prompt engineering without altering model weights. You can use
RAG, which augments the model's outputs with relevant information
grounded from supplied domain specific sources. Where these
options are not sufficient, consider customizing models using
managed model customization workflows.

Customizing foundation models is an advanced distributed computing
task that requires compute and memory intensive jobs to be run for
long periods of time. These tasks require the most performant
infrastructure to operate at high performance for extended periods
of time. As the job continues for extended time, there are
potential for job-halting issues to arise. Consider using managed
solutions for model customization that automate model
customization workflows to perform at maximum performance without
manual intervention. Fine-tuning, continuous pre-training, and
model distillation are three popular, time-consuming model
customization tasks. These tasks improve model performance but are
subject themselves to performance considerations, as they require
a significant amount of compute and time to complete. Consider
using the managed workflows for model customization on Amazon Bedrock to customize models in the most performant way.

Some customers may be developing a foundation model from scratch,
provisioning and orchestrating the infrastructure needed for
foundation model pre-training themselves. Consider automating and
managing this process through Amazon SageMaker AI HyperPod, a
foundation model pre-training workflow automation service. This
capability automatically handles performance considerations common
to model pre-training, which helps you verify that the model
pre-training job and final artifact are as performant and useful
as possible.

Customers have the ability to bring open-source models from model
hubs like HuggingFace to their AWS environment through
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/ "https://aws.amazon.com/sagemaker-ai/jumpstart/"). Models imported from services like
HuggingFace are hosted on Amazon SageMaker AI Inference Endpoints.
This capability allows customers to manage the underlying
infrastructure manually. Manual infrastructure hosting requires
owners to manage endpoints and preserve the model's performance
for the duration of the model's usefulness. Instead of manually
optimizing model infrastructure and uptime, consider importing the
model to a managed model hosting service like Amazon Bedrock using
Amazon Bedrock Custom Model Import. This capability automates the
performance management and maintenance of hosted models in your
AWS environment, reducing the undifferentiated heavy lifting of
model hosting.

### Implementation steps

1. For models hosted on Amazon Bedrock, identify the model you
   wish to customize. Keep in mind that not all models support
   this capability.
2. Run the managed model customization workflow matching your
   required use case.
3. For custom models, provision a model pre-training workflow
   on Amazon SageMaker AI HyperPod.

## Resources

**Related practices:**

- [PERF02-BP01](../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md "../performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.md")

**Related guides, videos, and documentation:**

- [Amazon SageMaker AI HyperPod](../../../sagemaker/latest/dg/sagemaker-hyperpod.md "../../../sagemaker/latest/dg/sagemaker-hyperpod.md")
- [Customize
  your model to improve its performance for your use case](../../../bedrock/latest/userguide/custom-models.md "../../../bedrock/latest/userguide/custom-models.md")

**Related examples:**

- [Amazon Bedrock
  Model Customization Workshop](https://github.com/aws-samples/amazon-bedrock-customization-workshop "https://github.com/aws-samples/amazon-bedrock-customization-workshop")
- [Customize
  models in Amazon Bedrock with your own data using fine-tuning
  and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/ "https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/")
