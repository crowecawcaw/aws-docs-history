# SageMaker AI Training Jobs

Customizing Amazon Nova models with Amazon SageMaker Training Jobs follows a
structured workflow designed to simplify the complex process of fine-tuning large language
models. This end-to-end workflow encompasses model training, evaluation, and deployment for
inference. For more information, see [Customizing Amazon Nova models](../../../sagemaker/latest/dg/nova-model.md "../../../sagemaker/latest/dg/nova-model.md") in the
_Amazon SageMaker AI Developer Guide_.

With Amazon SageMaker AI, you can fine-tune existing pre-trained foundation models, such as Amazon Nova,
without training your own models from scratch. The following sections detail the fine-tuning
options in SageMaker AI when working with Amazon Nova foundation models.

###### Topics

- [Full-rank
  fine-tuning](#custom-fine-tune-models-sagemaker-full-rank "#custom-fine-tune-models-sagemaker-full-rank")
- [Low-rank adapter
  fine-tuning](#custom-fine-tune-models-sagemaker-low-rank "#custom-fine-tune-models-sagemaker-low-rank")
- [Direct preference
  optimization](#custom-fine-tune-models-sagemaker-pref-opt "#custom-fine-tune-models-sagemaker-pref-opt")
- [Distillation](#customize-fine-tune-sagemaker-distill "#customize-fine-tune-sagemaker-distill")

## Full-rank

fine-tuning

Full-rank fine-tuning modifies all foundation model parameters to optimize its
performance for specific tasks or domains. This comprehensive approach updates the
entire model architecture, enabling deeper adaptations than adapter-based methods. For
more information, see [Fine-tune foundation
models](../../../sagemaker/latest/dg/canvas-fm-chat-fine-tune.md "../../../sagemaker/latest/dg/canvas-fm-chat-fine-tune.md").

###### How full-rank fine-tuning works

During full-rank fine-tuning, the model learns by updating all its parameters
using your training data. This process of full-rank fine-tuning:

- Allows the model to develop specialized knowledge for your domain.
- Enables significant changes to the model’s underlying representations.
- Requires more computational resources compared to adapter-based methods but
  can achieve better task-specific performance.

###### When to choose full-rank fine-tuning

We recommend using full-rank fine-tuning in the following scenarios:

- When LoRA PEFT fine-tuning doesn’t achieve the desired performance
  levels.
- For specialized domains that require deep expertise (such as medical, legal,
  or technical fields).
- When you have large, high-quality datasets for your use case.
- When accuracy requirements outweigh computational cost considerations.
- For applications that require significant deviation from the base model’s
  behavior.

## Low-rank adapter

fine-tuning

The most effective and cost-efficient method to enhance base model performance is
through low-rank adapter parameter-efficient fine-tuning (LoRA PEFT). The underlying
principle of LoRA PEFT is that only a small number of additional weights requires
updating to adapt it to new tasks or domains.

LoRA PEFT efficiently fine-tunes foundation models by introducing low-rank, trainable
weight matrices into specific model layers, reducing the number of trainable parameters
while maintaining model quality. A LoRA PEFT adapter augments the base foundation model
by incorporating lightweight adapter layers that modify the model’s weights during
inference, while keeping the original model parameters intact. This approach is also
considered one of the most cost-effective fine-tuning techniques. For more information,
see [Fine-tune models with adapter inference components](../../../sagemaker/latest/dg/realtime-endpoints-adapt.md "../../../sagemaker/latest/dg/realtime-endpoints-adapt.md").

###### When to choose LoRA PEFT

We recommend using LoRA PEFT in the following scenarios:

- You should generally start with LoRA PEFT over other fine-tuning methods
  because it's a fast training procedure.
- LoRA PEFT is effective in cases where the base model's performance is already
  satisfactory. In this case, the goal of LoRA PEFT is to enhance its capabilities
  across multiple related tasks, such as text summarization or language
  translation. LoRA PEFT's regularization properties also help prevent overfitting
  and mitigate the risks of the model "forgetting" the source domain. This ensures
  the model remains versatile and adaptable to various applications.
- You can use LoRA PEFT for instruction fine-tuning scenarios with relatively
  small datasets. LoRA PEFT performs better with smaller, task-specific datasets
  than broader, larger datasets.
- For large, labeled datasets that exceed the Amazon Bedrock customization data
  limits, you can use LoRA PEFT on SageMaker AI to generate better results.
- If you've already achieved promising results through Amazon Bedrock fine-tuning, LoRA
  PEFT on SageMaker AI can help further optimize the model hyperparameters.

## Direct preference

optimization

Direct preference optimization (DPO) is an efficient fine-tuning method for foundation
models that uses paired comparison data to align model outputs with human preferences.
This approach provides the direct optimization of model behavior based on human feedback
about which responses are more desirable.

###### Why DPO matters

Foundation models trained on large-scale data often generate outputs that might be
factually correct but fail to align with specific user needs, organizational values,
or safety requirements. DPO addresses this gap by allowing you to do the
following:

- Fine-tune models toward desired behavior patterns.
- Reduce unwanted outputs or harmful responses.
- Align model responses with brand voice and communication guidelines.
- Improve response quality based on domain expert feedback.

###### How DPO works

DPO uses paired examples where human evaluators indicate which of two possible
responses is preferred. The model learns to maximize the likelihood of generating
preferred responses while minimizing undesired ones. You can implement DPO by using
either of the following techniques:

- **Full-rank DPO**: Updates all model parameters
  to optimize for preferred responses.
- **LoRA-based DPO**: Uses lightweight adapters to
  learn preference alignments, requiring fewer computational resources.

###### When to choose DPO

We recommend using DPO in the following scenarios:

- Optimizing for subjective outputs that require alignment with specific human
  preferences.
- Adjusting the model’s tone, style, or content characteristics to match desired
  response patterns.
- Making targeted improvements to an existing model based on user feedback and
  error analysis.
- Maintaining consistent output quality across different use cases.
- Implementing safety guardrails through preferred response patterns.
- Training with reward-free reinforcement learning.
- Using only preference data instead of graded or labeled data.
- Improving the model in nuanced alignment tasks, such as helpfulness,
  harmlessness, or honesty.

DPO is effective for iteratively refining model behavior through carefully curated
preference datasets that demonstrate desired versus undesired outputs. The method’s
flexibility in supporting full-rank and LoRA-based approaches lets you choose the most
suitable implementation based on your computational resources and specific
requirements.

## Distillation

Model distillation is a method that transfers knowledge from large, advanced models to smaller, efficient ones. With Amazon Nova models, a larger "teacher" model (like Amazon Nova Pro or Amazon Nova Premier) passes its capabilities to a smaller "student" model (like Amazon Nova Lite or Amazon Nova Micro). This creates a customized model that maintains high performance while using fewer resources.

For information on how to complete this using SageMaker AI Training Jobs, see [Amazon Nova distillation](../../../sagemaker/latest/dg/nova-distillation.md "../../../sagemaker/latest/dg/nova-distillation.md").
