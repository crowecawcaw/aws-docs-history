# Question and answer for model evaluation in Amazon Bedrock

Question and answer is used for tasks including generating automatic help-desk
responses, information retrieval, and e-learning. If the text used to train the
foundation model contains issues including incomplete or inaccurate data, sarcasm or
irony, the quality of responses can deteriorate.

###### Important

For question and answer, there is a known system issue that prevents Cohere
models from completing the toxicity evaluation successfully.

The following built-in datasets are recommended for use with the question andg
answer task type.

**BoolQ**

BoolQ is a dataset consisting of yes/no question and answer pairs. The
prompt contains a short passage, and then a question about the passage.
This dataset is recommended for use with question and answer task
type.

**Natural Questions**

Natural questions is a dataset consisting of real user questions
submitted to Google search.

**TriviaQA**

TriviaQA is a dataset that contains over 650K
question-answer-evidence-triples. This dataset is used in question and
answer tasks.

The following table summarizes the metrics calculated, and recommended built-in dataset.

Available built-in datasets for the question and answer task type in
Amazon Bedrock| Task type | Metric | Built-in datasets | Computed metric |
| --- | --- | --- | --- |
| Question and answer | Accuracy | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | NLP-F1 |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") | | [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") | | Robustness | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | F1 and deltaF1 |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") | | [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") | | Toxicity | [BoolQ](https://github.com/google-research-datasets/boolean-questions "https://github.com/google-research-datasets/boolean-questions") | Toxicity |
| [NaturalQuestions](https://github.com/google-research-datasets/natural-questions "https://github.com/google-research-datasets/natural-questions") | | [TriviaQA](https://nlp.cs.washington.edu/triviaqa/ "https://nlp.cs.washington.edu/triviaqa/") | To learn more about how the computed metric for each built-in dataset is calculated, see [Review a model model evaluation job in Amazon Bedrock](model-evaluation-report.md "model-evaluation-report.md")
