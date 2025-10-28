# Dataset file types and input data

format

Instruction-based fine-tuning uses labeled datasets to improve the performance of
pre-trained LLMs on specific natural language processing (NLP) tasks. The labeled examples are
formatted as prompt-response pairs and phrased as instructions.

To learn about the supported dataset file types, see [Supported dataset file
types](#autopilot-llms-finetuning-dataset-format "#autopilot-llms-finetuning-dataset-format").

To learn about input data format, see [Input data format for
instruction-based fine-tuning](#autopilot-llms-finetuning-input-format "#autopilot-llms-finetuning-input-format").

## Supported dataset file

types

Autopilot supports instruction-based fine-tuning datasets formatted as CSV files (default)
or as Parquet files.

- **CSV** (comma separated values) is a row-based file
  format that stores data in human readable plaintext, which is a popular choice for data
  exchange as it is supported by a wide range of applications.
- **Parquet** is a binary, column-based file format where
  the data is stored and processed more efficiently than in human readable file formats
  such as CSV. This makes it a better option for big data problems.

###### Note

The dataset may consist of multiple files, each of which must adhere to a specific
template. For information on how to format your input data, see [Input data format for
instruction-based fine-tuning](#autopilot-llms-finetuning-input-format "#autopilot-llms-finetuning-input-format").

## Input data format for

instruction-based fine-tuning

Each file in the dataset must adhere to the following format:

- The dataset must contain exactly two comma-separated and named columns,
  `input` and `output`. Autopilot does not allow any additional
  columns.
- The `input` columns contain the prompts, and their corresponding
  `output` contains the expected answer. Both the `input` and
  `output` are in string format.

The following example illustrates the input data format for instruction-based
fine-tuning in Autopilot.

```
input,output
"<prompt text>","<expected generated text>"
```

###### Note

We recommend using datasets with a minimum of 1000 rows to ensure optimal learning and
performance of the model.

Additionally, Autopilot sets a maximum limit on the number of rows in the dataset and the
context length based on the type of model being used.

- The limits on the number of rows in a dataset apply to the cumulative count of rows
  across all files within the dataset, including multiple files. If there are two [channel types](../APIReference/API_AutoMLChannel.md "../APIReference/API_AutoMLChannel.md") defined (one for training and one for validation), the limit
  applies to the total number of rows across all datasets within both channels. When the
  number of rows exceeds the threshold, the job fails with a validation error.
- When the length of the input or output of a row in the dataset exceeds the limit set
  on the context of the language model, it is automatically truncated. If more than 60% of
  the rows in the dataset are truncated, whether in their input or output, Autopilot fails
  the job with a validation error.

The following table presents those limits for each model.

| JumpStart Model ID                               | `BaseModelName` in API request | Row Limit   | Context Length Limit |
| ------------------------------------------------ | ------------------------------ | ----------- | -------------------- |
| huggingface-textgeneration-dolly-v2-3b-bf16      | `Dolly3B`                      | 10,000 rows | 1024 tokens          |
| huggingface-textgeneration-dolly-v2-7b-bf16      | `Dolly7B`                      | 10,000 rows | 1024 tokens          |
| huggingface-textgeneration-dolly-v2-12b-bf16     | `Dolly12B`                     | 10,000 rows | 1024 tokens          |
| huggingface-llm-falcon-7b-bf16                   | `Falcon7B`                     | 1,000 rows  | 1024 tokens          |
| huggingface-llm-falcon-7b-instruct-bf16          | `Falcon7BInstruct`             | 1,000 rows  | 1024 tokens          |
| huggingface-llm-falcon-40b-bf16                  | `Falcon40B`                    | 10,000 rows | 1024 tokens          |
| huggingface-llm-falcon-40b-instruct-bf16         | `Falcon40BInstruct`            | 10,000 rows | 1024 tokens          |
| huggingface-text2text-flan-t5-large              | `FlanT5L`                      | 10,000 rows | 1024 tokens          |
| huggingface-text2text-flan-t5-xl                 | `FlanT5XL`                     | 10,000 rows | 1024 tokens          |
| huggingface-text2text-flan-t5-xxll               | `FlanT5XXL`                    | 10,000 rows | 1024 tokens          |
| meta-textgeneration-llama-2-7b                   | `Llama2-7B`                    | 10,000 rows | 2048 tokens          |
| meta-textgeneration-llama-2-7b-f                 | `Llama2-7BChat`                | 10,000 rows | 2048 tokens          |
| meta-textgeneration-llama-2-13b                  | `Llama2-13B`                   | 7,000 rows  | 2048 tokens          |
| meta-textgeneration-llama-2-13b-f                | `Llama2-13BChat`               | 7,000 rows  | 2048 tokens          |
| huggingface-llm-mistral-7b                       | `Mistral7B`                    | 10,000 rows | 2048 tokens          |
| huggingface-llm-mistral-7b-instruct              | `Mistral7BInstruct`            | 10,000 rows | 2048 tokens          |
| huggingface-textgeneration1-mpt-7b-bf16          | `MPT7B`                        | 10,000 rows | 1024 tokens          |
| huggingface-textgeneration1-mpt-7b-instruct-bf16 | `MPT7BInstruct`                | 10,000 rows | 1024 tokens          |
