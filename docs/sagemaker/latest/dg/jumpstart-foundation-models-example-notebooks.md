# Example

notebooks

For step-by-step examples on how to use publicly available JumpStart foundation models with
the SageMaker Python SDK, refer to the following notebooks on text generation,
image generation, and model customization.

###### Note

Proprietary and publicly available JumpStart foundation models have different SageMaker AI
Python SDK deployment workflows. Discover proprietary foundation
model example notebooks through Amazon SageMaker Studio Classic or the SageMaker AI console. For more
information, see [JumpStart foundation model usage](jumpstart-foundation-models-use.md "jumpstart-foundation-models-use.md").

You can clone the [Amazon SageMaker AI examples repository](https://github.com/aws/amazon-sagemaker-examples/tree/main/introduction_to_amazon_algorithms/jumpstart-foundation-models "https://github.com/aws/amazon-sagemaker-examples/tree/main/introduction_to_amazon_algorithms/jumpstart-foundation-models") to run the available JumpStart foundation model
examples in the Jupyter environment of your choice within Studio. For more
information on applications that you can use to create and access Jupyter in SageMaker AI, see
[Applications supported in Amazon SageMaker Studio](studio-updated-apps.md "studio-updated-apps.md").

## Time

series forecasting

You can use the Chronos models to forecast time series data. They're based on the
language model architecture. Use the [Introduction to SageMaker JumpStart - Time Series Forecasting with Chronos](https://github.com/aws/amazon-sagemaker-examples/blob/default/%20%20%20%20generative_ai/sm-jumpstart_time_series_forecasting.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/default/%20%20%20%20generative_ai/sm-jumpstart_time_series_forecasting.ipynb")
notebook to get started.

For information about the available Chronos models, see [Available foundation models](jumpstart-foundation-models-latest.md "jumpstart-foundation-models-latest.md").

## Text

generation

Explore text generation example notebooks, including guidance on general text
generation workflows, multilingual text classification, real-time batch inference,
few-shot learning, chatbot interactions, and more.

- [SageMaker JumpStart Foundation Models - HuggingFace Text2Text Generation with
  FLAN-T5 XL as an example](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-flan-t5.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-flan-t5.html")
- [SageMaker JumpStart Foundation Models - BloomZ: Multilingual Text Classification,
  Question and Answering, Code Generation, Paragraph rephrase, and
  More](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-bloomz.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-bloomz.html")
- [SageMaker JumpStart Foundation Models - HuggingFace Text2Text Generation Batch
  Transform and Real-Time Batch Inference](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-Batch-Transform.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text2text-generation-Batch-Transform.html")
- [SageMaker JumpStart Foundation Models - GPT-J, GPT-Neo Few-shot
  learning](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text-generation-few-shot-learning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text-generation-few-shot-learning.html")
- [SageMaker JumpStart Foundation Models - Chatbots](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text-generation-chatbot.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/text-generation-chatbot.html")
- [Introduction to SageMaker JumpStart - Text Generation with Mistral
  models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/mistral-7b-instruction-domain-adaptation-finetuning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/mistral-7b-instruction-domain-adaptation-finetuning.html")
- [Introduction to SageMaker JumpStart - Text Generation with Falcon
  models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/falcon-7b-instruction-domain-adaptation-finetuning.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/falcon-7b-instruction-domain-adaptation-finetuning.html")

## Image generation

Get started with text-to-image Stable Diffusion models, learn how to deploy an
inpainting model, and experiment with a simple workflow to generate images of your
dog.

- [Introduction to JumpStart - Text to Image](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart_text_to_image/Amazon_JumpStart_Text_To_Image.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart_text_to_image/Amazon_JumpStart_Text_To_Image.html")
- [Introduction to JumpStart Image editing - Stable Diffusion
  Inpainting](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart_inpainting/Amazon_JumpStart_Inpainting.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart_inpainting/Amazon_JumpStart_Inpainting.html")
- [Generate fun images of your dog](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart_text_to_image/custom_dog_image_generator.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart_text_to_image/custom_dog_image_generator.html")

## Model customization

Sometimes your use case requires greater foundation model customization for
specific tasks. For more information on model customization approaches, see [Foundation model
customization](jumpstart-foundation-models-customize.md "jumpstart-foundation-models-customize.md") or explore one of the
following example notebooks.

- [SageMaker JumpStart Foundation Models - Fine-tuning text generation GPT-J 6B
  model on domain specific dataset](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/domain-adaption-finetuning-gpt-j-6b.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/domain-adaption-finetuning-gpt-j-6b.html")
- [SageMaker JumpStart Foundation Models - HuggingFace Text2Text Instruction
  Fine-Tuning](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/instruction-fine-tuning-flan-t5.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/instruction-fine-tuning-flan-t5.html")
- [Retrieval-Augmented Generation: Question Answering using LangChain and
  Cohere’s Generate and Embedding Models from SageMaker
  JumpStart](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_Cohere+langchain_jumpstart.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_Cohere+langchain_jumpstart.html")
- [Retrieval-Augmented Generation: Question Answering using LLama-2,
  Pinecone and Custom Dataset](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_pinecone_llama-2_jumpstart.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_pinecone_llama-2_jumpstart.html")
- [Retrieval-Augmented Generation: Question Answering based on Custom
  Dataset with Open-sourced LangChain Library](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_langchain_jumpstart.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_langchain_jumpstart.html")
- [Retrieval-Augmented Generation: Question Answering based on Custom
  Dataset](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_jumpstart_knn.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_jumpstart_knn.html")
- [Retrieval-Augmented Generation: Question Answering using Llama-2 and
  Text Embedding Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_text_embedding_llama-2_jumpstart.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/question_answering_text_embedding_llama-2_jumpstart.html")
- [Amazon SageMaker JumpStart - Text Embedding and Sentence Similarity](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/text-embedding-sentence-similarity.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/jumpstart-foundation-models/question_answering_retrieval_augmented_generation/text-embedding-sentence-similarity.html")
