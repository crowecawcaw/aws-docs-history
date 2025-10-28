# Evaluate the performance of an Amazon Bedrock model

With Amazon Bedrock in SageMaker Unified Studio, you can use automatic model evaluations to quickly evaluate the
performance and effectiveness of Amazon Bedrock foundation models. To
evaluate a model you create an evaluation job. Model evaluation jobs support common use
cases for large language models (LLMs) such as text generation, text classification,
question answering, and text summarization. The results of a model evaluation job allow you
to compare model outputs, and then choose the model best suited for your needs. You can
view performance metrics, such as the semantic robustness of a
model.
Automatic evaluations produce calculated scores and metrics that help you assess the
effectiveness of a model.

Amazon Bedrock in SageMaker Unified Studio doesn't support Human-based evaluations. For more information,
see [Model evaluation jobs](../../../bedrock/latest/userguide/model-evaluation.md "../../../bedrock/latest/userguide/model-evaluation.md")
in the _Amazon Bedrock user guide_.

###### Important

In Amazon Bedrock in SageMaker Unified Studio, you can view the model evaluation jobs in your project.
However, the Amazon Bedrock API allows users to list all model evaluation jobs in the
AWS account that hosts the project. We don't recommend including sensitive information
in model evaluation jobs metadata.

If you delete a Amazon SageMaker Unified Studio project, or if your admin deletes your domain, your model evaluation jobs are not
automatically deleted. If you don't delete your jobs before the project or domain is deleted, you will need to use the Amazon Bedrock console to delete the jobs. Contact
your administrator if you don't have access to the Amazon Bedrock in SageMaker Unified Studio console.

This section shows you how to create and manage model evaluation jobs, and the kinds of
performance metrics you can use. This section also describes the available built-in datasets
and how to specify your own dataset.

###### Topics

- [Create a model evaluation
  job with Amazon Bedrock](model-evaluation-jobs-management-create.md "model-evaluation-jobs-management-create.md")
- [Model evaluation task types in Amazon Bedrock](model-evaluation-tasks.md "model-evaluation-tasks.md")
- [Use prompt datasets for model evaluation in Amazon Bedrock](model-evaluation-prompt-datasets.md "model-evaluation-prompt-datasets.md")
- [Review a model model evaluation job in Amazon Bedrock](model-evaluation-report.md "model-evaluation-report.md")
