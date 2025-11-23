# Supported models reference

The following tables show the models for which SageMaker AI support inference optimization, and
they show the supported optimization techniques.

| Supported Llama models             | Model Name                          | Supported Data Formats for Quantization | Supports Speculative Decoding | Supports Fast Model Loading | Libraries Used for Compilation |
| ---------------------------------- | ----------------------------------- | --------------------------------------- | ----------------------------- | --------------------------- | ------------------------------ |
| Meta Llama 2 13B                   | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 2 13B Chat              | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 2 70B                   | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 2 70B Chat              | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 2 7B                    | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 2 7B Chat               | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 3 70B                   | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 3 70B Instruct          | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 3 8B                    | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Llama 3 8B Instruct           | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Meta Code Llama 13B                | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 13B Instruct       | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 13B Python         | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 34B                | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 34B Instruct       | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 34B Python         | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 70B                | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 70B Instruct       | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 70B Python         | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 7B                 | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 7B Instruct        | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Code Llama 7B Python          | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Meta Llama 2 13B Neuron            | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 2 13B Chat Neuron       | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 2 70B Neuron            | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 2 70B Chat Neuron       | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 2 7B Neuron             | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 2 7B Chat Neuron        | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3 70B Neuron            | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3 70B Instruct Neuron   | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3 8B Neuron             | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3 8B Instruct Neuron    | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Code Llama 70B Neuron         | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Code Llama 7B Neuron          | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Code Llama 7B Python Neuron   | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3.1 405B FP8            | None                                | Yes                                     | Yes                           | None                        |
| Meta Llama 3.1 405B Instruct FP8   | None                                | Yes                                     | Yes                           | None                        |
| Meta Llama 3.1 70B                 | INT4-AWQ<br>FP8                     | Yes                                     | Yes                           | None                        |
| Meta Llama 3.1 70B Instruct        | INT4-AWQ<br>FP8                     | Yes                                     | Yes                           | None                        |
| Meta Llama 3.1 8B                  | INT4-AWQ<br>FP8                     | Yes                                     | Yes                           | None                        |
| Meta Llama 3.1 8B Instruct         | INT4-AWQ<br>FP8                     | Yes                                     | Yes                           | None                        |
| Meta Llama 3.1 70B Neuron          | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3.1 70B Instruct Neuron | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3 1 8B Neuron           | None                                | No                                      | No                            | AWS Neuron                  |
| Meta Llama 3.1 8B Instruct Neuron  | None                                | No                                      | No                            | AWS Neuron                  |

| Supported Mistral models   | Model Name                          | Supported Data Formats for Quantization | Supports Speculative Decoding | Supports Fast Model Loading | Libraries Used for Compilation |
| -------------------------- | ----------------------------------- | --------------------------------------- | ----------------------------- | --------------------------- | ------------------------------ |
| Mistral 7B                 | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Mistral 7B Instruct        | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | AWS Neuron<br>TensorRT-LLM  |
| Mistral 7B Neuron          | None                                | No                                      | No                            | AWS Neuron                  |
| Mistral 7B Instruct Neuron | None                                | No                                      | No                            | AWS Neuron                  |

| Supported Mixtral models    | Model Name                          | Supported Data Formats for Quantization | Supports Speculative Decoding | Supports Fast Model Loading | Libraries Used for Compilation |
| --------------------------- | ----------------------------------- | --------------------------------------- | ----------------------------- | --------------------------- | ------------------------------ |
| Mixtral-8x22B-Instruct-v0.1 | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Mixtral-8x22B V1            | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Mixtral 8x7B                | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |
| Mixtral 8x7B Instruct       | INT4-AWQ<br>INT8-SmoothQuant<br>FP8 | Yes                                     | Yes                           | TensorRT-LLM                |

| Supported Model Architectures and EAGLE Type | Model Architecture Name | EAGLE Type |
| -------------------------------------------- | ----------------------- | ---------- |
| LlamaForCausalLM                             | EAGLE 3                 |
| Qwen3ForCausalLM                             | EAGLE 3                 |
| Qwen3NextForCausalLM                         | EAGLE 2                 |
| Qwen3MoeForCausalLM                          | EAGLE 3                 |
| Qwen2ForCausalLM                             | EAGLE 3                 |
| GptOssForCausalLM                            | EAGLE 3                 |
