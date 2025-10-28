# Foundation models and

hyperparameters for fine-tuning

Foundation models are computationally expensive and trained on a large, unlabeled
corpus. Fine-tuning a pre-trained foundation model is an affordable way to take
advantage of their broad capabilities while customizing a model on your own small,
corpus. Fine-tuning is a customization method that involved further training and
does change the weights of your model.

Fine-tuning might be useful to you if you need:

- to customize your model to specific business needs
- your model to successfully work with domain-specific language, such as
  industry jargon, technical terms, or other specialized vocabulary
- enhanced performance for specific tasks
- accurate, relative, and context-aware responses in applications
- responses that are more factual, less toxic, and better-aligned to
  specific requirements
  There are two main approaches that you can take for fine-tuning depending on your
  use case and chosen foundation model.

1. If you're interested in fine-tuning your model on domain-specific data,
   see [Fine-tune a large language model (LLM) using domain adaptation](jumpstart-foundation-models-fine-tuning-domain-adaptation.md "jumpstart-foundation-models-fine-tuning-domain-adaptation.md").
2. If you're interested in instruction-based fine-tuning using prompt and
   response examples, see [Fine-tune a large language model (LLM) using prompt instructions](jumpstart-foundation-models-fine-tuning-instruction-based.md "jumpstart-foundation-models-fine-tuning-instruction-based.md").

## Foundation

models available for fine-tuning

You can fine-tune any of the following JumpStart foundation models:

- Bloom 3B
- Bloom 7B1
- BloomZ 3B FP16
- BloomZ 7B1 FP16
- Code Llama 13B
- Code Llama 13B Python
- Code Llama 34B
- Code Llama 34B Python
- Code Llama 70B
- Code Llama 70B Python
- Code Llama 7B
- Code Llama 7B Python
- CyberAgentLM2-7B-Chat (CALM2-7B-Chat)
- Falcon 40B BF16
- Falcon 40B Instruct BF16
- Falcon 7B BF16
- Falcon 7B Instruct BF16
- Flan-T5 Base
- Flan-T5 Large
- Flan-T5 Small
- Flan-T5 XL
- Flan-T5 XXL
- Gemma 2B
- Gemma 2B Instruct
- Gemma 7B
- Gemma 7B Instruct
- GPT-2 XL
- GPT-J 6B
- GPT-Neo 1.3B
- GPT-Neo 125M
- GPT-NEO 2.7B
- LightGPT Instruct 6B
- Llama 2 13B
- Llama 2 13B Chat
- Llama 2 13B Neuron
- Llama 2 70B
- Llama 2 70B Chat
- Llama 2 7B
- Llama 2 7B Chat
- Llama 2 7B Neuron
- Mistral 7B
- Mixtral 8x7B
- Mixtral 8x7B Instruct
- RedPajama INCITE Base 3B V1
- RedPajama INCITE Base 7B V1
- RedPajama INCITE Chat 3B V1
- RedPajama INCITE Chat 7B V1
- RedPajama INCITE Instruct 3B V1
- RedPajama INCITE Instruct 7B V1
- Stable Diffusion 2.1

## Commonly supported fine-tuning hyperparameters

Different foundation models support different hyperparameters when
fine-tuning. The following are commonly-supported hyperparameters that can
further customize your model during training:

| Inference Parameter           | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `epoch`                       | The number of passes that the model takes through the fine-tuning dataset during training. Must be an integer greater than 1.                                                                                                                                                                                                                                                                        |
| `learning_rate`               | The rate at which the model weights are updated after working through each batch of fine-tuning training examples. Must be a positive float greater than 0.                                                                                                                                                                                                                                          |
| `instruction_tuned`           | Whether to instruction-train the model or not. Must be `'True'` or `'False'`.                                                                                                                                                                                                                                                                                                                        |
| `per_device_train_batch_size` | The batch size per GPU core or CPU for training. Must be a positive integer.                                                                                                                                                                                                                                                                                                                         |
| `per_device_eval_batch_size`  | The batch size per GPU core or CPU for evaluation. Must be a positive integer.                                                                                                                                                                                                                                                                                                                       |
| `max_train_samples`           | For debugging purposes or quicker training, truncate the number of training examples to this value. Value -1 means that the model uses all of the training samples. Must be a positive integer or -1.                                                                                                                                                                                                |
| `max_val_samples`             | For debugging purposes or quicker training, truncate the number of validation examples to this value. Value -1 means that the model uses all of the validation samples. Must be a positive integer or -1.                                                                                                                                                                                            |
| `max_input_length`            | Maximum total input sequence length after tokenization. Sequences longer than this will be truncated. If -1, `max_input_length` is set to the minimum of 1024 and the `model_max_length` defined by the tokenizer. If set to a positive value, `max_input_length` is set to the minimum of the provided value and the `model_max_length` defined by the tokenizer. Must be a positive integer or -1. |
| `validation_split_ratio`      | If there is no validation channel, ratio of train-validation split from the training data. Must be between 0 and 1.                                                                                                                                                                                                                                                                                  |
| `train_data_split_seed`       | If validation data is not present, this fixes the random splitting of the input training data to training and validation data used by the model. Must be an integer.                                                                                                                                                                                                                                 |
| `preprocessing_num_workers`   | The number of processes to use for the pre-processing. If `None`, main process is used for pre-processing.                                                                                                                                                                                                                                                                                           |
| `lora_r`                      | Low-rank adaptation (LoRA) r value, which acts as the scaling factor for weight updates. Must be a positive integer.                                                                                                                                                                                                                                                                                 |
| `lora_alpha`                  | Low-rank adaptation (LoRA) alpha value, which acts as the scaling factor for weight updates. Generally 2 to 4 times the size of `lora_r`. Must be a positive integer.                                                                                                                                                                                                                                |
| `lora_dropout`                | Dropout value for low-rank adaptation (LoRA) layers Must be a positive float between 0 and 1.                                                                                                                                                                                                                                                                                                        |
| `int8_quantization`           | If `True`, model is loaded with 8 bit precision for training.                                                                                                                                                                                                                                                                                                                                        |
| `enable_fsdp`                 | If `True`, training uses Fully Sharded Data Parallelism.                                                                                                                                                                                                                                                                                                                                             | You can specify hyperparameter values when you fine-tune your model in Studio. For more information, see [Fine-tune a model in Studio](jumpstart-foundation-models-use-studio-updated-fine-tune.md "jumpstart-foundation-models-use-studio-updated-fine-tune.md"). You can also override default hyperparameter values when fine-tuning your model using the SageMaker Python SDK. For more information, see [Fine-tune publicly available foundation models with the JumpStartEstimator class](jumpstart-foundation-models-use-python-sdk-estimator-class.md "jumpstart-foundation-models-use-python-sdk-estimator-class.md"). |
