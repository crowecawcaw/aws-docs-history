# Evaluation recipe

examples

Amazon Nova provides four types of evaluation recipes, which are available in the
HyperPod recipes GitHub repository.

These recipes enable you to evaluate the fundamental capabilities of Amazon Nova models
across a comprehensive suite of text-only benchmarks. They are provided in the format
`xxx_general_text_benchmark_eval.yaml`.

These recipes enable you to evaluate the fundamental capabilities of Amazon Nova models
across a comprehensive suite of multi-modality benchmarks. They are provided in the
format `xxx_general_multi_modal_benchmark_eval.yaml`.

These recipes enable you to bring your own dataset for benchmarking and compare
model outputs to reference answers using different types of metrics. They are provided
in the format `xxx_bring_your_own_dataset_eval.yaml`.

The following are the bring your own dataset requirements:

- File format requirements
  - You must include a single `gen_qa.jsonl` file containing
    evaluation examples.
  - Your dataset must be uploaded to an S3 location where SageMaker AI training job can
    access it.
  - The file must follow the required schema format for a general Q&A
    dataset.

- Schema format requirements - Each line in the JSONL file must be a JSON object
  with the following fields:

      + `query`: (Required) String containing the question or instruction
       that needs an answer
      + `response`: (Required) String containing the expected model
       output
      + `system`: (Optional) String containing the system prompt that
       sets the behavior, role, or personality of the AI model before it processes the
       query
      + `metadata`: (Optional) String containing metadata associated with
       the entry for tagging purposes.

  Here is a bring your own data set example entry

```
`{
 "system":"You are a english major with top marks in class who likes to give minimal word responses: ",
 "query":"What is the symbol that ends the sentence as a question",
 "response":"?"
}
{
 "system":"You are a pattern analysis specialist that provides succinct answers: ",
 "query":"What is the next number in this series? 1, 2, 4, 8, 16, ?",
 "response":"32"
}
{
 "system":"You have great attention to detail that follows instructions accurately: ",
 "query":"Repeat only the last two words of the following: I ate a hamburger today and it was kind of dry",
 "response":"of dry"
}`
```

To use your custom dataset, modify your evaluation recipe with the following
required fields, do not change any of the content:

```
`evaluation:
 task: gen_qa
 strategy: gen_qa
 metric: all`
```

The following limitations apply:

- Only one JSONL file is allowed per evaluation.
- The file must strictly follow the defined schema.
- Context length limit: For each sample in the dataset, the context length
  (including system + query prompts) should be less than 3.5k.
  Amazon Nova LLM as a Judge is a model evaluation feature that enables customers to
  compare the quality of responses from one model to a baseline model response on a custom
  dataset. It takes in a dataset with prompts, baseline responses, and challenger
  responses, and uses a Nova Judge model to provide a winrate metric based on [Bradley-Terry
  probability](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") with pairwise comparisons.

The recipes are provided in the format `xxx_llm_judge_eval.yaml`.

The following are the LLM as a Judge requirements:

- File format requirements
  - Include a single `llm_judge.jsonl` file containing evaluation
    examples. The file name must be `llm_judge.jsonl`.
  - Your dataset must be uploaded to an S3 location that [SageMaker AI
    HyperPod RIG](nova-hp-cluster.md "nova-hp-cluster.md") can access.
  - The file must follow the required schema format for the
    `llm_judge.jsonl` dataset.
  - The input dataset should ensure all records are under 12k context
    length.

- Schema format requirements - Each line in the JSONL file must be a JSON object
  with the following fields:

      + `prompt`: (Required) A string containing the prompt for the
       generated response.
      + `response_A`: A string containing the baseline response.
      + `response_B`: A string containing the alternative response be
       compared with baseline response.

  Here is an LLM as a judge example entry

```
`{
"prompt": "What is the most effective way to combat climate change?",
"response_A": "The most effective way to combat climate change is through a combination of transitioning to renewable energy sources and implementing strict carbon pricing policies. This creates economic incentives for businesses to reduce emissions while promoting clean energy adoption.",
"response_B": "We should focus on renewable energy. Solar and wind power are good. People should drive electric cars. Companies need to pollute less."
}
{
"prompt": "Explain how a computer's CPU works",
"response_A": "CPU is like brain of computer. It does math and makes computer work fast. Has lots of tiny parts inside.",
"response_B": "A CPU (Central Processing Unit) functions through a fetch-execute cycle, where instructions are retrieved from memory, decoded, and executed through its arithmetic logic unit (ALU). It coordinates with cache memory and registers to process data efficiently using binary operations."
}
{
"prompt": "How does photosynthesis work?",
"response_A": "Plants do photosynthesis to make food. They use sunlight and water. It happens in leaves.",
"response_B": "Photosynthesis is a complex biochemical process where plants convert light energy into chemical energy. They utilize chlorophyll to absorb sunlight, combining CO2 and water to produce glucose and oxygen through a series of chemical reactions in chloroplasts."
}`
```

To use your custom dataset, modify your evaluation recipe with the following
required fields, don't change any of the content:

```
`evaluation:
 task: llm_judge
 strategy: judge
 metric: all`
```

The following limitations apply:

- Only one JSONL file is allowed per evaluation.
- The file must strictly follow the defined schema.
- Amazon Nova Judge models are the same across all model family specifications (that
  is, Lite, Micro, and Pro).
- Custom judge models are not supported at this time.
- Context length limit: For each sample in the dataset, the context length
  (including system + query prompts) should be less than 7k.
  Nova LLM Judge for multi-modal (image), short for Nova MM_LLM Judge, is a model
  evaluation feature that enables you to compare the quality of responses from one model
  against a baseline model's responses using a custom dataset. It accepts a dataset
  containing prompts, baseline responses, and challenger responses, and images in the form
  of Base64-encoded string, then uses a Nova Judge model to provide a win rate metric
  based on [Bradley-Terry](https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model "https://en.wikipedia.org/wiki/Bradley%E2%80%93Terry_model") probability through pairwise comparisons. Recipe format:
  `xxx_mm_llm_judge _eval.yaml`.

**Nova LLM dataset requirements**

File format:

- Single `mm_llm_judge.jsonl` file containing evaluation examples. The
  file name must be exactly `llm_judge.jsonl`.
- Your must upload your dataset to an S3 location where SageMaker training jobs can
  access it.
- The file must follow the required schema format for the
  `mm_llm_judge` dataset.
- The input dataset should ensure all records are under 12 k context length,
  excluding the image's attribute.
  Schema format - Each line in the `.jsonl` file must be a JSON object with
  the following fields.

- Required fields.

`prompt`: String containing the prompt for the generated
response.

`images`: Array containing a list of objects with data attributes
(values are Base64-encoded image strings).

`response_A`: String containing the baseline response.

`response_B`: String containing the alternative response be compared
with baseline response.
Example entry

For readability, the following example includes new lines and indentation, but in
the actual dataset, each record should be on a single line.

```
{
  "prompt": "what is in the image?",
  "images": [
    {
      "data": "data:image/jpeg;Base64,/9j/2wBDAAQDAwQDAwQEAwQFBAQFBgo..."
    }
  ],
  "response_A": "a dog.",
  "response_B": "a cat.",
}
{
  "prompt": "how many animals in echo of the images?",
  "images": [
    {
      "data": "data:image/jpeg;Base64,/9j/2wBDAAQDAwQDAwQEAwQFBAQFBgo..."
    },
    {
      "data": "data:image/jpeg;Base64,/DKEafe3gihn..."
    }
  ],
  "response_A": "The first image contains one cat and the second image contains one dog",
  "response_B": "The first image has one aminal and the second has one animal",
}
```

To use your custom dataset, modify your evaluation recipe with the following
required fields, don't change any of the content:

```
evaluation:
  task: mm_llm_judge
  strategy: judge
  metric: all
```

**Limitations**

- Only one `.jsonl` file is allowed per evaluation.
- The file must strictly follow the defined schema.
- Nova MM Judge models only support image reference.
- Nova MM Judge models are the same across Amazon Nova Lite
  specifications.
- Custom judge models are not currently supported.
- Amazon S3 image URI is not supported.
- The input dataset should ensure all records are under 12 k context length,
  excluding images attribute.
