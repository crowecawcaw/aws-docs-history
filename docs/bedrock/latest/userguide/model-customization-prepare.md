# Prepare your training datasets for fine-tuning and continued

pre-training

To prepare training and validation datasets for your custom model, you create `.jsonl` files, where each
line is a JSON object corresponding to a record. Before you can begin a model customization job, you
must at minimum prepare a training dataset. The files you create must conform to the format for the
customization method and model that you choose. The records in it must conform to size requirements depending
your model.

For information about model requirments, see [Model requirements for training and validation
datasets](model-training-validation-requirements.md "model-training-validation-requirements.md"). To see the
default quotas that apply for training and validation datasets used for customizing different models, see the
**Sum of training and validation records** quotas in [Amazon Bedrock endpoints and quotas](../../../general/latest/gr/bedrock.md "../../../general/latest/gr/bedrock.md") in the AWS General Reference.

Whether a validation dataset is supported and the format of your training and validation dataset depend on the
following factors.

- The type of fine-tuning customization job (Fine-tuning or Continued Pre-training).
- The input and output modalities of the data.
  For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

###### Topics

- [Supported modalities for fine-tuning and continued
  pre-training](#model-customization-data-support "#model-customization-data-support")
- [Model requirements for training and validation
  datasets](model-training-validation-requirements.md "model-training-validation-requirements.md")
- [Prepare data for fine-tuning text-to-text models](preparing-text-data.md "preparing-text-data.md")
- [Prepare data for fine-tuning image and text processing models](preparing-image-text-data.md "preparing-image-text-data.md")
- [Prepare data for fine-tuning image generation and embedding
  models](preparing-image-generation-data.md "preparing-image-generation-data.md")
- [Prepare datasets for continued pre-training](dataset-prep-continued-pretraining.md "dataset-prep-continued-pretraining.md")

## Supported modalities for fine-tuning and continued

pre-training

The following sections describe the different fine-tuning and pre-training capabilities supported by each
model, organized by their input and output modalities. For information about fine-tuning Amazon Nova models, see [Fine-tuning Amazon Nova models](../../../nova/latest/userguide/customize-fine-tune.md "../../../nova/latest/userguide/customize-fine-tune.md").

**Text-to-Text models**

Text-to-Text models can be fine-tuned for various text-based tasks, including both conversational and
non-conversational applications. For information about preparing data for fine-tuning Text-to-Text models, see [Prepare data for fine-tuning text-to-text models](preparing-text-data.md "preparing-text-data.md").

The following non-conversational models are optimized for tasks like summarization, translation, and
question answering:

- Amazon Titan Text G1 - Express
- Amazon Titan Text G1 - Lite
- Amazon Titan Text Premier
- Cohere Command
- Cohere Command Light
- Meta Llama 3.1 8B Instruct
- Meta Llama 3.1 70B Instruct

The following conversational models are designed for single-turn and multi-turn interactions. If a model uses the Converse API, your fine-tuning dataset must follow the Converse API message format and include system,
user, and assistant messages. For examples, see [Prepare data for fine-tuning text-to-text models](preparing-text-data.md "preparing-text-data.md"). For more information about Converse API operations, see [Carry out a conversation with the
Converse API operations](conversation-inference.md "conversation-inference.md").

- Anthropic Claude 3 Haiku
- Meta Llama 3.2 1B Instruct (Converse API format)
- Meta Llama 3.2 3B Instruct (Converse API format)
- Meta Llama 3.2 11B Instruct Vision (Converse API format)
- Meta Llama 3.2 90B Instruct Vision (Converse API format)
- Meta Llama 3.3 70B Vision Instruct (Converse API format)

**Text-Image-to-Text & Text-to-Image model**s

The following models support fine-tuning for image generation and text-image processing. These models
process or generate images based on textual input, or generate text based on both textual and image
inputs. For information about preparing data for fine-tuning Text-Image-to-Text & Text-to-Image models models, see [Prepare data for fine-tuning image and text processing models](preparing-image-text-data.md "preparing-image-text-data.md").

- Amazon Titan Image Generator G1 V1
- Meta Llama 3.2 11B Instruct Vision
- Meta Llama 3.2 90B Instruct Vision
- Meta Llama 3.3 70B Vision Instruct

**Image-to-Embeddings**

The following models support fine-tuning for tasks like classification and retrieval. These models
generate numerical representations (embeddings) from image inputs. For information about preparing data for fine-tuning Image-to-Embeddings models, see [Prepare data for fine-tuning image generation and embedding
models](preparing-image-generation-data.md "preparing-image-generation-data.md").

- Amazon Titan Multimodal Embeddings G1
- Amazon Titan Image Generator G1 V1

**Continued Pre-training: Text-to-Text**

The following models can be used for continued pre-training. These models support continued
pre-training on domain-specific data to enhance their base knowledge. For information about preparing data for Continued Pre-training for Text-to-Text models, see [Prepare datasets for continued pre-training](dataset-prep-continued-pretraining.md "dataset-prep-continued-pretraining.md").

- Amazon Titan Text G1 - Express
- Amazon Titan Text G1 - Lite
