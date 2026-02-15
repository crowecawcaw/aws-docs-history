# Submit prompts and generate responses with model inference

Inference refers to the process of generating an output from an input provided to a model.

Amazon Bedrock offers a suite of foundation models that you can use to generate outputs of the following modalities. To see modality support by foundation model, refer to [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

| Output modality | Description                                                                                                                                                                                                                                                           | Example use cases                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| Text            | Provide text input and generate various types of text                                                                                                                                                                                                                 | Chat, question-and-answering, brainstorming, summarization, code<br>generation, table creation, data formatting, rewriting                          |
| Image           | Provide text or input images and generate or modify images                                                                                                                                                                                                            | Image generation, image editing, image variation                                                                                                    |
| Video           | Provide text or reference images and generate a video                                                                                                                                                                                                                 | Video generation, image conversion to video                                                                                                         |
| Embeddings      | Provide text, images, or both text and images and generate a vector of<br>numeric values that represent the input. The output vector can be compared<br>to other embeddings vectors to determine semantic similarity (for text) or<br>visual similarity (for images). | Text and image search, query, categorization, recommendations,<br>personalization, [knowledge base creation](knowledge-base.md "knowledge-base.md") |

###### Topics

- [Learn about use cases for different model inference methods](inference-methods.md "inference-methods.md")
- [How inference works in Amazon Bedrock](inference-how.md "inference-how.md")
- [Influence response generation with inference parameters](inference-parameters.md "inference-parameters.md")
- [Supported Regions and models for running model inference](inference-supported.md "inference-supported.md")
- [Prerequisites for running model inference](inference-prereq.md "inference-prereq.md")
- [Generate responses in the console using playgrounds](playgrounds.md "playgrounds.md")
- [Enhance model responses with model reasoning](inference-reasoning.md "inference-reasoning.md")
- [Optimize model inference for latency](latency-optimized-inference.md "latency-optimized-inference.md")
- [Generate responses using OpenAI APIs](bedrock-mantle.md "bedrock-mantle.md")
- [Submit prompts and generate responses using the API](inference-api.md "inference-api.md")
- [Get validated JSON results from models](structured-output.md "structured-output.md")
- [Use a computer use tool to complete an Amazon Bedrock model response](computer-use.md "computer-use.md")
