# Evaluate a text generation

foundation model in Studio

###### Note

Foundation Model Evaluations (FMEval) is in preview release for Amazon SageMaker Clarify and is subject to
change.

###### Important

In order to use SageMaker Clarify Foundation Model Evaluations, you must upgrade to the new Studio experience.
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The foundation evaluation feature can only be used in the updated
experience. For information about how to update Studio, see [Migration from Amazon SageMaker Studio Classic](studio-updated-migrate.md "studio-updated-migrate.md"). For
information about using the Studio Classic application, see [Amazon SageMaker Studio Classic](studio.md "studio.md").

Amazon SageMaker JumpStart has integrations with SageMaker Clarify Foundation Model Evaluations (FMEval) in Studio. If a JumpStart model
has built-in evaluation capabilities available, you can choose
**Evaluate** in the upper right corner of the model detail page in
the JumpStart Studio UI. For more information on navigating the JumpStart Studio UI, see
[Open and use JumpStart in Studio](studio-jumpstart.md#jumpstart-open-use-studio "studio-jumpstart.md#jumpstart-open-use-studio"),

Use Amazon SageMaker JumpStart to evaluate text-based foundation models with FMEval. You can use these
model evaluations to compare model quality and responsibility metrics for one model,
between two models, or between different versions of the same model, to help you
quantify model risks. FMEval can evaluate text-based models that perform the following
tasks:

- **Open-ended generation** – The production of
  natural human responses to text that does not have a pre-defined
  structure.
- **Text summarization** – The generation of a
  concise and condensed summary while retaining the meaning and key information
  contained in larger text.
- **Question Answering** – The generation of an
  answer in natural language to a question.
- **Classification** – The assignment of a
  class, such as `positive` versus `negative` to a text
  passage based on its content.
  You can use FMEval to automatically evaluate model responses based on specific
  benchmarks. You can also evaluate model responses against your own criteria by bringing
  your own prompt datasets. FMEval provides a user interface (UI) that guides you through
  the setup and configuration of an evaluation job. You can also use the FMEval library
  inside your own code.

Every evaluation requires quota for two instances:

- Hosting instance – An instance that hosts and deploys an LLM.
- Evaluation instance – An instance that is used to prompt and perform an
  evaluation of an LLM on the hosting instance.
  If your LLM is already deployed, provide the endpoint, and SageMaker AI will use your
  **hosting instance** to host and deploy the LLM.

If you are evaluating a JumpStart model that is not yet deployed to your account,
FMEval creates a temporary **hosting instance** for you in
your account, and keeps it deployed only for the length of your evaluation. FMEval uses
the default instance that JumpStart recommends for the chosen LLM as your hosting
instance. You must have sufficient quota for this recommended instance.

Every evaluation also uses an evaluation instance to provide prompts to and score the
responses from the LLM. You must also have sufficient quota and memory to run the
evaluation algorithms. The quota and memory requirements of the evaluation instance are
generally smaller than those required for a hosting instance. We recommend selecting the
`ml.m5.2xlarge` instance. For more information about quota and memory,
see [Resolve errors when
creating a model evaluation job in Amazon SageMaker AI](clarify-foundation-model-evaluate-troubleshooting.md "clarify-foundation-model-evaluate-troubleshooting.md").

Automatic evaluations can be used to score LLMs across the following
dimensions:

- Accuracy – For text summarization, question answering, and text
  classification
- Semantic robustness – For open-ended generation, text summarization and
  text classification tasks
- Factual knowledge – For open-ended generation
- Prompt stereotyping – For open-ended generation
- Toxicity – For open-ended generation, text summarization, and question
  answering
  You can also use human evaluations to manually evaluate model responses. The FMEval UI
  guides you through a workflow of selecting one or more models, provisioning resources,
  and writing instructions for and contacting your human workforce. After the human
  evaluation is complete, the results are displayed in FMEval.

You can access model evaluation through the JumpStart landing page in Studio by
selecting a model to evaluate and then choosing **Evaluate**. Note that
not all JumpStart models have evaluation capabilities available. For more information about
how to configure, provision and run FMEval, see [What are
Foundation Model Evaluations?](clarify-foundation-model-evaluate.md "clarify-foundation-model-evaluate.md")
