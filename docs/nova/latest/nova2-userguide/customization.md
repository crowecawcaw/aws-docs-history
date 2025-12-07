# Customizing Amazon Nova 2.0 models

Amazon Nova offers the most comprehensive suite of customization options to adapt the
foundation models to your specific business needs, from simple fine-tuning in Amazon Bedrock to
advanced training pipelines in Amazon SageMaker.

###### Topics

- [Customization overview](#customization-overview "#customization-overview")
- [Customization platform availability](#customization-availability "#customization-availability")
- [Customization on Amazon Bedrock](#customization-bedrock "#customization-bedrock")
- [Customization on SageMaker AI](#customization-sagemaker "#customization-sagemaker")
- [With Amazon Bedrock](customize-fine-tune-bedrock.md "customize-fine-tune-bedrock.md")
- [With Amazon SageMaker AI](customize-fine-tune-sagemaker.md "customize-fine-tune-sagemaker.md")

## Customization overview

Model customization allows you to specialize Amazon Nova models for your domain, use cases and
quality requirements. You can choose from several customization techniques and platforms based
on your technical requirements, data availability and desired outcomes.

Customization techniques:

- **Continued Pre-Training (CPT)** - Teach models
  domain-specific knowledge using raw text data
- **Supervised Fine-Tuning (SFT)** - Customize through
  input-output examples
- **Reinforcement Fine-Tuning (RFT)** - Optimize using
  reward signals and human feedback
- **Distillation** - Transfer knowledge from larger to
  smaller models

## Customization platform availability

The following table summarizes the availability of customizations per platform.

| Platform                   | CPT | SFT | RFT | Distillation |
| -------------------------- | --- | --- | --- | ------------ |
| Amazon Bedrock             | No  | Yes | Yes | Yes          |
| SageMaker AI Training Jobs | No  | Yes | Yes | Yes          |
| SageMaker AI HyperPod      | Yes | Yes | Yes | Yes          |

## Customization on Amazon Bedrock

Amazon Bedrock provides a fully managed fine-tuning experience for Amazon Nova models, making it easy to
customize models without managing infrastructure.

Supported methods:

Supervised Fine-Tuning (SFT)

Teach models through input-output examples to customize response style, format and
task-specific behavior.

Reinforcement Fine-Tuning (RFT)

Maximize accuracy and align the model with real-world feedback and simulations using
reward signals.

Model Distillation

Transfers knowledge from larger "teacher" models to smaller "student" models. This
process creates efficient models that maintain a significant portion of the original
model's performance. The teacher model generates responses to diverse prompts and these
outputs train the student model to produce similar results. This approach is more
effective than standard fine-tuning when you lack sufficient high-quality labeled
data.

###### Note

For implementation details, see [Customization on Amazon Bedrock](../../../bedrock/latest/userguide/custom-models.md "../../../bedrock/latest/userguide/custom-models.md").

Key features:

- Fully managed infrastructure with no setup required
- Simple API-based training job submission
- Direct deployment to Amazon Bedrock inference endpoints

When to use Amazon Bedrock fine-tuning:

- You need quick customization with minimal setup
- Your use case fits standard fine-tuning patterns
- You prefer flexible customization from simple to increasingly complex training
- You want seamless integration with Amazon Bedrock inference

## Customization on SageMaker AI

SageMaker AI provides advanced training capabilities when you need full control over the
customization process, access to multiple training methods and the ability to build simple to
increasingly complex training pipelines.

Available training methods:

Continued Pre-Training (CPT)

Teaches models domain-specific knowledge at scale using raw text data. Ideal for
specialized technical fields, legal documents, medical literature, or any domain with
unique terminology and concepts. Requires large volumes of unlabeled text (billions of
tokens recommended).

Supervised Fine-Tuning (SFT)

Customizes models through direct input-output examples. Best for teaching specific
response styles, formats and task behaviors. Supports text, image and video inputs. You
can choose between Parameter Efficient Fine-Truning (PEFT) of Full Fine-Tuning methods.
The prior is suited for adapter-based customization with 2k-10k samples. The latter is
suited for full model customization with tens of thousands to hundreds of thousands of
samples.

Reinforcement Fine-Tuning (RFT)

Optimizes models using reward signals for complex problem-solving tasks like
domain-specific reasoning, code generation, and scientific analysis. Best used after SFT
establishes baseline capabilities. You can use regex patterns and custom python code for
verifiable rewards, or LLM-as-a-Judge for non-verifiable rewards. You can also integrate
any other custom reward functions through a Lambda function such as single-turn remote
reward functions in a customer's own environment.

Model Distillation

Transfers knowledge from larger "teacher" models to smaller "student" models. This
process creates efficient models that maintain a significant portion of the original
model's performance. The teacher model generates responses to diverse prompts and these
outputs train the student model to produce similar results. This approach is more
effective than standard fine-tuning when you lack sufficient high-quality labeled
data.

###### Note

For implementation details on distillation, see [Model
distillation](../userguide/customize-distill.md "../userguide/customize-distill.md").

Advanced capabilities:

- **Iterative training** - Chain multiple training methods
  (for example, SFT to RFT) with checkpoint reuse for targeted improvements
- **Reasoning Mode Support** - Train Nova 2 models with
  explicit reasoning steps for complex analytical tasks

Infrastructure options:

SageMaker AI Training Jobs

Managed training with automatic resource provisioning for streamlined model
customization workflows.

SageMaker AI HyperPod

Resilient, large-scale training clusters for enterprise workloads requiring maximum
control and scale.
