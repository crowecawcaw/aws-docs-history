# Custom models in Neptune ML

Neptune ML lets you define your own custom model implementations using Python. You
can train and deploy custom models using Neptune ML infrastructure very much as you do
for the built-in models, and use them to obtain predictions through graph queries.

###### Note

[Real-time inductive
inference](machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference "machine-learning-overview-evolving-data.md#inductive-vs-transductive-inference") is not currently supported for custom models.

You can start implementing a custom model of your own in Python by following the [Neptune
ML toolkit examples](https://github.com/awslabs/neptuneml-toolkit/tree/main/examples/custom-models/ "https://github.com/awslabs/neptuneml-toolkit/tree/main/examples/custom-models/"), and by using the model components provided in the
Neptune ML toolkit. The following sections provide more details.

###### Contents

- [Overview of custom models in Neptune ML](machine-learning-custom-model-overview.md "machine-learning-custom-model-overview.md")
  - [When to use a custom model
    in Neptune ML](machine-learning-custom-model-overview.md#machine-learning-custom-models-when-to-use "machine-learning-custom-model-overview.md#machine-learning-custom-models-when-to-use")
  - [Workflow for developing
    and using a custom model in Neptune ML](machine-learning-custom-model-overview.md#machine-learning-custom-model-workflow "machine-learning-custom-model-overview.md#machine-learning-custom-model-workflow")

- [Custom model development in Neptune ML](machine-learning-custom-model-development.md "machine-learning-custom-model-development.md")
  - [Custom model training script development in Neptune ML](machine-learning-custom-model-development.md#machine-learning-custom-model-training-script "machine-learning-custom-model-development.md#machine-learning-custom-model-training-script")
  - [Custom model transform script development in Neptune ML](machine-learning-custom-model-development.md#machine-learning-custom-model-transform-script "machine-learning-custom-model-development.md#machine-learning-custom-model-transform-script")
  - [Custom model-hpo-configuration.json file in Neptune ML](machine-learning-custom-model-development.md#machine-learning-custom-model-hpo-configuration-file "machine-learning-custom-model-development.md#machine-learning-custom-model-hpo-configuration-file")
  - [Local testing of your custom model implementation in Neptune ML](machine-learning-custom-model-development.md#machine-learning-custom-model-testing "machine-learning-custom-model-development.md#machine-learning-custom-model-testing")
