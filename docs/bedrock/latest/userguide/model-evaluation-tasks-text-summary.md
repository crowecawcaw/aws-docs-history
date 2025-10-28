# Text summarization for model evaluation in Amazon Bedrock

Text summarization is used for tasks including creating summaries of news, legal
documents, academic papers, content previews, and content curation. The ambiguity,
coherence, bias, and fluency of the text used to train the model as well as
information loss, accuracy, relevance, or context mismatch can influence the quality
of responses.

###### Important

For text summarization, there is a known system issue that prevents Cohere
models from completing the toxicity evaluation successfully.

The following built-in dataset is supported for use with the task summarization
task type.

**Gigaword**

The Gigaword dataset consists of news article headlines. This dataset
is used in text summarization tasks.

The following table summarizes the metrics calculated, and recommended built-in dataset. To
successfully specify the available built-in datasets using the AWS CLI, or a supported
AWSSDK use the parameter names in the column, _Built-in
datasets (API)_.

| Available built-in datasets for text summarization in Amazon Bedrock | Task type                                                                                                   | Metric                                                                                                      | Built-in datasets (console) | Built-in datasets (API) | Computed metric |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------- | ----------------------- | --------------- | ----------------------------------------------------------------------------------------------------------- | ------------------ | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Text summarization                                                   | Accuracy                                                                                                    | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | `Builtin.Gigaword`          | BERTScore               |
| Toxicity                                                             | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | `Builtin.Gigaword`                                                                                          | Toxicity                    |                         | Robustness      | [Gigaword](https://huggingface.co/datasets/gigaword?row=3 "https://huggingface.co/datasets/gigaword?row=3") | `Builtin.Gigaword` | BERTScore and deltaBERTScore | To learn more about how the computed metric for each built-in dataset is calculated, see [Review model evaluation job reports and metrics in Amazon Bedrock](model-evaluation-report.md "model-evaluation-report.md") |
