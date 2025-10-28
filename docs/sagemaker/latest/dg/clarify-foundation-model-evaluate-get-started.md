# Get started with model

evaluations

A large language model (LLM) is a machine learning model that can analyze and generate
natural language text. If you want to evaluate an LLM, SageMaker AI provides the following three
options that you can choose:

- Set up manual evaluations for a human workforce using Studio.
- Evaluate your model with an algorithm using
  Studio.
- Automatically evaluate your model with a customized work flow using the
  `fmeval` library.
  You can either use an algorithm to automatically evaluate your foundation model or ask
  a human work team to evaluate the models' responses.

Human work teams can evaluate and compare up to two models concurrently using metrics
that indicate preference for one response over another. The work flow, metrics, and
instructions for a human evaluation can be tailored to fit a particular use case. Humans
can also provide a more refined evaluation than an
algorithmic
evaluation.

You can also use an algorithm to evaluate your LLM using benchmarks to rapidly score
your model responses in Studio. Studio provides a guided work flow to evaluate
responses from a JumpStart model using pre-defined metrics. These metrics are
specific to generative AI tasks. This guided flow uses built-in or custom datasets to
evaluate your LLM.

Alternatively, you can use the `fmeval` library to create a more customized
work flow using automatic evaluations than what is available in Studio. Using
Python code and the `fmeval` library, you can evaluate any
text-based LLM, including models that were created outside of JumpStart.

The following topics provide an overview of foundation model evaluations, a summary of
the automatic and human
Foundation
Model Evaluation (FMEval) work flows, how to run them, and how to view
an analysis report of your results. The automatic evaluation topic shows how to
configure and run both a starting and customized evaluation.

**Topics**

- [Using prompt datasets and available evaluation dimensions in model evaluation jobs](clarify-foundation-model-evaluate-overview.md "clarify-foundation-model-evaluate-overview.md")
- [Foundation model
  evaluation summary](clarify-foundation-model-evaluate-overview.md#clarify-foundation-model-evaluate-summary "clarify-foundation-model-evaluate-overview.md#clarify-foundation-model-evaluate-summary")
- [Create a model evaluation job that uses human workers](clarify-foundation-model-evaluate-human.md "clarify-foundation-model-evaluate-human.md")
- [Automatic model evaluation](clarify-foundation-model-evaluate-auto.md "clarify-foundation-model-evaluate-auto.md")
