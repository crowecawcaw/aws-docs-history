# Use custom prompt

dataset for model evaluation in Amazon Bedrock in SageMaker Unified Studio

You can use a custom prompt dataset in model evaluation jobs.

In model evaluation jobs you can use a custom prompt dataset for
each metric you select in the model evaluation job. Custom datasets use the JSON
line format (`.jsonl`), and each line must be a valid JSON object.
There can be up to 1000 prompts in your dataset per automatic evaluation
job.

You must use the following keys in a custom dataset.

- `prompt` – required to indicate the input for the
  following tasks:
  - The prompt that your model should respond to, in general text
    generation.
  - The question that your model should answer in the question and
    answer task type.
  - The text that your model should summarize in text
    summarization task.
  - The text that your model should classify in classification
    tasks.

- `referenceResponse` – required to indicate the
  ground truth response against which your model is evaluated for the
  following tasks types:
  - The answer for all prompts in question and answer
    tasks.
  - The answer for all accuracy, and robustness
    evaluations.

- `category`– (optional) generates evaluation scores
  reported for each category.
  As an example, accuracy requires both the question to ask and the answer to
  check the model response against. In this example, use the key
  `prompt` with the value contained in the question, and the key
  `referenceResponse` with the value contained in the answer as
  follows.

```
{
    "prompt": "Bobigny is the capital of",
    "referenceResponse": "Seine-Saint-Denis",
    "category": "Capitals"
}
```

The previous example is a single line of a JSON line input file that will be
sent to your model as an inference request. Model will be invoked for every such
record in your JSON line dataset. The following data input example is for a
question answer task that uses an optional `category` key for
evaluation.

```
{"prompt":"Aurillac is the capital of", "category":"Capitals", "referenceResponse":"Cantal"}
{"prompt":"Bamiyan city is the capital of", "category":"Capitals", "referenceResponse":"Bamiyan Province"}
{"prompt":"Sokhumi is the capital of", "category":"Capitals", "referenceResponse":"Abkhazia"}
```
