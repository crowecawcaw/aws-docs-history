# Prompt

engineering for foundation models

Prompt engineering is the process of designing and refining the prompts or input
stimuli for a language model to generate specific types of output. Prompt
engineering involves selecting appropriate keywords, providing context, and shaping
the input in a way that encourages the model to produce the desired response and is
a vital technique to actively shape the behavior and output of foundation
models.

Effective prompt engineering is crucial for directing model behavior and achieving
desired responses. Through prompt engineering, you can control a model’s tone,
style, and domain expertise without more involved customization measures like
fine-tuning. We recommend dedicating time to prompt engineering before you consider
fine-tuning a model on additional data. The goal is to provide sufficient context
and guidance to the model so that it can generalize and perform well on unseen or
limited data scenarios.

## Zero-shot learning

Zero-shot learning involves training a model to generalize and make
predictions on unseen classes or tasks. To perform prompt engineering in
zero-shot learning environments, we recommend constructing prompts that
explicitly provide information about the target task and the desired output
format. For example, if you want to use a foundation model for zero-shot text
classification on a set of classes that the model did not see during training, a
well-engineered prompt could be: `"Classify the following text as either
 sports, politics, or entertainment: `[input
text]`."` By explicitly specifying the target classes and
the expected output format, you can guide the model to make accurate predictions
even on unseen classes.

## Few-shot learning

Few-shot learning involves training a model with a limited amount of data for
new classes or tasks. Prompt engineering in few-shot learning environments
focuses on designing prompts that effectively use the limited available training
data. For example, if you use a foundation model for an image classification
task and only have a few examples of a new image class, you can engineer a
prompt that includes the available labeled examples with a placeholder for the
target class. For example, the prompt could be: `"[image 1], [image 2], and
 [image 3] are examples of `[target class]`.
 Classify the following image as `[target
class]`"`. By incorporating the limited labeled examples
and explicitly specifying the target class, you can guide the model to
generalize and make accurate predictions even with minimal training data.

## Supported inference parameters

Changing inference parameters might also affect the responses to your prompts.
While you can try to add as much specificity and context as possible to your
prompts, you can also experiment with supported inference parameters. The
following are examples of some commonly supported inference parameters:

| Inference Parameter | Description                                                                                                                                                                                                                                                                                                                                       |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_new_tokens`    | The maximum output length of a foundation model response. Valid values: integer, range: Positive integer.                                                                                                                                                                                                                                         |
| `temperature`       | Controls the randomness in the output. Higher temperature results in an output sequence with low-probability words and lower temperature results in output sequence with high-probability words. If `temperature=0`, the response is made up of only the highest probability words (greedy decoding). Valid values: float, range: Positive float. |
| `top_p`             | In each step of text generation, the model samples from the smallest possible set of words with a cumulative probability of `top_p`. Valid values: float, range: 0.0, 1.0.                                                                                                                                                                        |
| `return_full_text`  | If `True`, then the input text is part of the generated output text. Valid values: boolean, default: False.                                                                                                                                                                                                                                       | For more information on foundation model inference, see [Deploy publicly available foundation models with the JumpStartModel class](jumpstart-foundation-models-use-python-sdk-model-class.md "jumpstart-foundation-models-use-python-sdk-model-class.md"). If prompt engineering is not sufficient to adapt your foundation model to specific business needs, domain-specific language, target tasks, or other requirements, you can consider fine-tuning your model on additional data or using Retrieval Augmented Generation (RAG) to augment your model architecture with enhanced context from archived knowledge sources. For more information, see [Foundation models and hyperparameters for fine-tuning](jumpstart-foundation-models-fine-tuning.md "jumpstart-foundation-models-fine-tuning.md") or [Retrieval Augmented Generation](jumpstart-foundation-models-customize-rag.md "jumpstart-foundation-models-customize-rag.md"). |
