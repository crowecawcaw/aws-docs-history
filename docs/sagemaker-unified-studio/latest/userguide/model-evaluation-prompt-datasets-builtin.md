# Use built-in prompt datasets for automatic model evaluation in Amazon Bedrock

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
type. To learn more about how automatic metrics are computed, see [Review a model model evaluation job in Amazon Bedrock](model-evaluation-report.md "model-evaluation-report.md").

Available built-in datasets for automatic model evaluation jobs in
Amazon Bedrock| Task type | Metric | Built-in datasets | Computed metric |
| --- | --- | --- | --- |
| General text generation | Accuracy | [TREX](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") | Real world knowledge (RWK) score |
| Robustness | [BOLD](https://github.com/amazon-science/bold "https://github.com/amazon-science/bold") | Word error rate | | [TREX](https://hadyelsahar.github.io/t-rex/ "https://hadyelsahar.github.io/t-rex/") |
| [WikiText2](https://huggingface.co/datasets/wikitext "https://huggingface.co/datasets/wikitext") | | Toxicity | [RealToxicityPrompts](https://github.com/allenai/real-toxicity-prompts "https://github.com/allenai/real-toxicity-prompts") | Toxicity |
| [BOLD](https://github.com/amazon-science/bold "https://github.com/amazon-science/bold") |
| Text summarization | Accuracy | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | BERTScore |
| Toxicity | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | Toxicity | | Robustness | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | BERTScore and deltaBERTScore |
| Question and answer | Accuracy | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | NLP-F1 |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") | | [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") | | Robustness | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | F1 and deltaF1 |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") | | [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") | | Toxicity | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | Toxicity |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") | | [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") | | Text classification | Accuracy | [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") | Accuracy (Binary accuracy from classification_accuracy_score) |
| Robustness | [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") | classification_accuracy_score and delta_classification_accuracy_score | To learn more about the requirements for creating and examples of custom prompt datasets, see [Use custom prompt dataset for model evaluation in Amazon Bedrock in SageMaker Unified Studio](model-evaluation-prompt-datasets-custom.md "model-evaluation-prompt-datasets-custom.md").
