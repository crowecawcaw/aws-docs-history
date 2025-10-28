# Understand options for evaluating large

language models with SageMaker Clarify

###### Important

In order to use SageMaker Clarify Foundation Model Evaluations, you must upgrade to the new Studio experience.
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The foundation evaluation feature can only be used in the updated
experience. For information about how to update Studio, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md"). For
information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

Using Amazon SageMaker Clarify you can evaluate large language models (LLMs) by creating model evaluation jobs. A model evaluation job allows you to evaluate and compare model quality and responsibility metrics for text-based foundation models from JumpStart. Model evaluation jobs also support the use of JumpStart models that have already been deployed to an endpoint.

You can create a model evaluation job using three different approaches.

- Create automated model evaluation jobs in Studio – Automatic model evaluation jobs allow you to quickly evaluate a model's ability to perform a task. You can either provide your own custom prompt dataset that you've tailored to a specific use case, or you can use an available built-in dataset.
- Create a model evaluation jobs that use human workers in Studio – Model evaluation jobs that use human workers allow you to bring human input to the model evaluation process. They can be employees of your company or a group of subject-matter experts from your industry.
- Create an automated model evaluation job using the `fmeval` library – Creating a job using the `fmeval` gives you the most fine-grained control over your model evaluation jobs. It also supports the use of LLMs outside of AWS or non-JumpStart based models from other services.
  Model evaluation jobs support common use cases for LLMs such as text generation, text classification, question and answering, and text summarization.

- **Open-ended generation** – The production of
  natural human responses to text that does not have a pre-defined structure.
- **Text summarization** – The generation of a
  concise and condensed summary while retaining the meaning and key information that's
  contained in larger text.
- **Question answering** – The generation of a
  relevant and accurate response to a prompt.
- **Classification** – Assigning a category,
  such as a label or score, to text based on its content.
  The following topics describe the available model evaluation tasks, and the kinds of metrics you can use. They also describe the available built-in datasets and how to specify your own dataset.

###### Topics

- [What are foundation model evaluations?](clarify-foundation-model-evaluate-whatis.md "clarify-foundation-model-evaluate-whatis.md")
- [Get started with model
  evaluations](clarify-foundation-model-evaluate-get-started.md "clarify-foundation-model-evaluate-get-started.md")
- [Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md")
- [Create a model evaluation job that uses human workers](clarify-foundation-model-evaluate-human.md "clarify-foundation-model-evaluate-human.md")
- [Automatic model evaluation](clarify-foundation-model-evaluate-auto.md "clarify-foundation-model-evaluate-auto.md")
- [Understand the results of your model
  evaluation job](clarify-foundation-model-evaluate-results.md "clarify-foundation-model-evaluate-results.md")
- [Customize your workflow using the fmeval library](clarify-foundation-model-evaluate-auto-lib-custom.md "clarify-foundation-model-evaluate-auto-lib-custom.md")
- [Model evaluation notebook
  tutorials](clarify-foundation-model-evaluate-auto-tutorial.md "clarify-foundation-model-evaluate-auto-tutorial.md")
- [Resolve errors when
  creating a model evaluation job in Amazon SageMaker AI](clarify-foundation-model-evaluate-troubleshooting.md "clarify-foundation-model-evaluate-troubleshooting.md")
