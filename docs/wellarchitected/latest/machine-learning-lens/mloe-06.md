# MLOE-06: Establish model improvement strategies

Plan improvement drivers for optimizing model performance before
ML model development starts. Examples of improvement drivers
include: collecting more data, cross-validation, feature
engineering, tuning hyperparameters, and ensemble methods.

## Implementation plan

- **Use Amazon SageMaker AI
  Experiments** - Improvement strategies for ML
  experimentation follow a sequence from simple to more
  complex. Begin with minimal data cleaning and the most
  obvious data. Train a simple classical model using
  algorithms, such as linear regression or logistic
  regression, for classification tasks. Iterate by increasing
  the data processing and model complexity to improve
  metrics related to business value.
  [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") can help to organize multiple
  tests to compare different configurations and algorithms. A
  few sample approaches to experiment with include:

- **Use effective feature
  selection** - Work with subject matter experts to
  gain insight into the most significant features that will
  be related to the target values. Iteratively add more
  complex features, and remove less important features to
  improve model accuracy and robustness.
- **Use deep learning** - For
  a large volume training data, consider deep learning
  models to find previously unknown features and improve the
  model accuracy.
- **Consider ensemble
  methods** - Ensemble methods can add further
  improvements to accuracy by combining the best
  characteristics of various algorithms. However, there is a
  trade-off with computational performance and maintenance
  difficulty that should be considered for each specific
  business use case.
- **Consider AutoML** -
  Automatic machine learning, known as AutoML, removes the
  tedious, iterative, and time-consuming work across the
  machine learning workflow from data acquisition to model
  operationalization, so you can spend less time on low
  level details and more time on using ML to improve
  business outcomes. AutoML tools take care of sourcing and
  preparing data, engineering features, training and tuning
  models, deploying models, and ongoing model monitoring and
  updating. Amazon SageMaker AI Autopilot is an AutoML solution
  for tabular data.

- **Optimize
  hyperparameters** - Optimize hyperparameters for
  each algorithm to obtain the top performance before
  selection of the most appropriate.
  [Amazon SageMaker AI Hyperparameter](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md")
  [Optimization](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md")
  automates this process of selecting the top performance.

## Documents

- [Manage
  Machine Learning with Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md")
- [Perform
  Automatic Model Tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [Automate
  the experimental trials into SageMaker AI Pipelines by leveraging the native SageMaker AI Pipelines integration with experiments](../../../sagemaker/latest/dg/pipelines-experiments.md "../../../sagemaker/latest/dg/pipelines-experiments.md")
- [Automate
  model development with Amazon SageMaker AI Autopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development.md "../../../sagemaker/latest/dg/autopilot-automate-model-development.md")

## Blogs

- [Developing
  a business strategy by combining machine learning with sensitivity analysis](https://aws.amazon.com/blogs/machine-learning/developing-a-business-strategy-by-combining-machine-learning-with-sensitivity-analysis/ "https://aws.amazon.com/blogs/machine-learning/developing-a-business-strategy-by-combining-machine-learning-with-sensitivity-analysis/")
- [Amazon SageMaker AI Experiments – Organize, Track And Compare Your Machine Learning Trainings](https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-experiments-organize-track-and-compare-your-machine-learning-trainings/")
- [Code-free
  machine learning: AutoML with AutoGluon, Amazon SageMaker AI, and AWS Lambda](https://aws.amazon.com/blogs/machine-learning/code-free-machine-learning-automl-with-autogluon-amazon-sagemaker-and-aws-lambda/ "https://aws.amazon.com/blogs/machine-learning/code-free-machine-learning-automl-with-autogluon-amazon-sagemaker-and-aws-lambda/")

## Videos

- [Hyperparameter
  Tuning with Amazon SageMaker AI's Automatic Model Tuning](https://www.youtube.com/watch?v=ynYnZywayC4 "https://www.youtube.com/watch?v=ynYnZywayC4")

## Examples

- [Ensemble
  Predictions from Multiple Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html")
