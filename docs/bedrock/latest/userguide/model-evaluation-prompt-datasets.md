# Use prompt datasets for model evaluation in Amazon Bedrock

To create an automatic model evaluation job you must specify a prompt dataset.
The prompts are then used during inference with the model you select to evaluate. Amazon Bedrock provides built-in datasets that can be used in automatic model evaluations, or you can bring your own prompt dataset.

Use the following sections to learn more about available built-in prompt datasets and
creating your custom prompt datasets.

## Use built-in prompt datasets for automatic model evaluation in Amazon Bedrock

Amazon Bedrock provides multiple built-in prompt datasets that you can use in an automatic
model evaluation job. Each built-in dataset is based off an open-source dataset. We
have randomly down sampled each open-source dataset to include only 100
prompts.

When you create an automatic model evaluation job and choose a **Task
type** Amazon Bedrock provides you with a list of recommended metrics. For each
metric, Amazon Bedrock also provides recommended built-in datasets. To learn more about
available task types, see [Model evaluation task types in Amazon Bedrock](model-evaluation-tasks.md "model-evaluation-tasks.md").

**Bias in Open-ended Language Generation Dataset (BOLD)**

The Bias in Open-ended Language Generation Dataset (BOLD) is a dataset
that evaluates fairness in general text generation, focusing on five
domains: profession, gender, race, religious ideologies, and political
ideologies. It contains 23,679 different text generation prompts.

**RealToxicityPrompts**

RealToxicityPrompts is a dataset that evaluates toxicity. It attempts
to get the model to generate racist, sexist, or otherwise toxic
language. This dataset contains 100,000 different text generation
prompts.

**T-Rex : A Large Scale Alignment of Natural Language with Knowledge Base
Triples (TREX)**

TREX is dataset consisting of Knowledge Base Triples (KBTs) extracted
from Wikipedia. KBTs are a type of data structure used in natural
language processing (NLP) and knowledge representation. They consist of
a subject, predicate, and object, where the subject and object are
linked by a relation. An example of a Knowledge Base Triple (KBT) is
"George Washington was the president of the United States". The subject
is "George Washington", the predicate is "was the president of", and the
object is "the United States".

**WikiText2**

WikiText2 is a HuggingFace dataset that contains prompts used in
general text generation.

**Gigaword**

The Gigaword dataset consists of news article headlines. This dataset
is used in text summarization tasks.

**BoolQ**

BoolQ is a dataset consisting of yes/no question and answer pairs. The
prompt contains a short passage, and then a question about the passage.
This dataset is recommended for use with question and answer task
type.

**Natural Questions**

Natural question is a dataset consisting of real user questions
submitted to Google search.

**TriviaQA**

TriviaQA is a dataset that contains over 650K
question-answer-evidence-triples. This dataset is used in question and
answer tasks.

**Women's E-Commerce Clothing Reviews**

Women's E-Commerce Clothing Reviews is a dataset that contains
clothing reviews written by customers. This dataset is used in text
classification tasks.

In the following table, you can see the list of available datasets grouped task
type. To learn more about how automatic metrics are computed, see [Review metrics for an automated model evaluation
job in Amazon Bedrock (console)](model-evaluation-report-programmatic.md "model-evaluation-report-programmatic.md").

Available built-in datasets for automatic model evaluation jobs in
Amazon Bedrock| Task type | Metric | Built-in datasets | Computed metric |
| --- | --- | --- | --- |
| General text generation | Accuracy | [TREX](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") | Real world knowledge (RWK) score |
| Robustness | [BOLD](https://github.com/amazon-science/bold "https://github.com/amazon-science/bold") | Word error rate |
| [TREX](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") |
| [WikiText2](https://huggingface.co/datasets/wikitext "https://huggingface.co/datasets/wikitext") |
| Toxicity | [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts "https://github.com/allenai/real-toxicity-prompts") | Toxicity |
| [BOLD](https://github.com/amazon-science/bold "https://github.com/amazon-science/bold") |
| Text summarization | Accuracy | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | BERTScore |
| Toxicity | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | Toxicity |
| Robustness | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | BERTScore and deltaBERTScore |
| Question and answer | Accuracy | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | NLP-F1 |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") |
| [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") |
| Robustness | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | F1 and deltaF1 |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") |
| [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") |
| Toxicity | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | Toxicity |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") |
| [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") |
| Text classification | Accuracy | [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") | Accuracy (Binary accuracy from<br>classification_accuracy_score) |
| Robustness | [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") | classification_accuracy_score and<br>delta_classification_accuracy_score |

To learn more about the requirements for creating and examples of custom prompt
datasets, see [Use custom prompt dataset for model evaluation in Amazon Bedrock](#model-evaluation-prompt-datasets-custom "#model-evaluation-prompt-datasets-custom").

## Use custom prompt dataset for model evaluation in Amazon Bedrock

You can create a custom prompt dataset in an automatic model evaluation jobs. Custom prompt datasets must be stored in Amazon S3, and use the JSON line format and use the `.jsonl` file extension. Each line must be a valid JSON object. There can be up to 1000 prompts in your dataset per automatic evaluation job.

For job created using the console you must update the Cross Origin Resource Sharing (CORS) configuration on the S3 bucket. To learn more about the required CORS permissions, see [Required Cross Origin Resource Sharing
(CORS) permissions on S3 buckets](model-evaluation-security-cors.md "model-evaluation-security-cors.md").

You must use the following keys value pairs in a custom dataset.

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

As an example, accuracy requires both the question asked, and a answer to check the model's response against. In this example, use the key `prompt` with the value contained in the question, and the key`referenceResponse` with the value contained in the answer as follows.

```
{
  "prompt": "Bobigny is the capital of",
  "referenceResponse": "Seine-Saint-Denis",
  "category": "Capitals"
}
```

The previous example is a single line of a JSON line input file that will be sent to your model as an inference request. Model will be invoked for every such record in your JSON line dataset. The following data input example is for a question answer task that uses an optional `category` key for evaluation.

```
{"prompt":"Aurillac is the capital of", "category":"Capitals", "referenceResponse":"Cantal"}
{"prompt":"Bamiyan city is the capital of", "category":"Capitals", "referenceResponse":"Bamiyan Province"}
{"prompt":"Sokhumi is the capital of", "category":"Capitals", "referenceResponse":"Abkhazia"}
```
