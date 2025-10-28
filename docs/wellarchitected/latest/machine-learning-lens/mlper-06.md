# MLPER-06: Explore alternatives for performance improvement

Perform benchmarks to improve the machine learning model
performance. Benchmarking in ML involves evaluation and
comparison of ML workloads with different algorithms, features,
and architecture resources. It enables identifying the
combination with optimal performance.

Options you can use when benchmarking include:

- Use more data to broaden the statistical range and improve
  the success metric of the model.
- Apply feature engineering to extract important signals in
  the data for the model.
- Make alternative algorithm selections for an optimal fit to
  the specifics of the data.
- Ensemble methods that combine the different advantages of
  multiple models.
- Tune the hyperparameters for a given algorithm to calibrate
  the model for the data.

## Implementation plan

- **Use Amazon SageMaker AI Experiments
  to optimize algorithms and features** -Begin with
  a simple architecture, obvious features, and a simple
  algorithm to establish a baseline. Amazon SageMaker AI
  provides
  [built-in
  algorithms](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") for developing a baseline model. Use
  [Amazon SageMaker AI Experiments](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md") to organize, track, compare,
  and evaluate your machine learning experiments. Test
  different algorithms with increasing complexity to observe
  performance. Combine models into an ensemble to increase
  accuracy, but consider the potential loss of efficiency as
  a trade-off. Refine the features by selection and modify
  parameters to optimize model performance. Tune the model’s
  hyperparameters to optimize performance using
  [Amazon SageMaker AI Hyperparameter Optimization](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md") to automate
  the search.

## Documents

- [Improving
  Model Accuracy](../../../machine-learning/latest/dg/improving-model-accuracy.md "../../../machine-learning/latest/dg/improving-model-accuracy.md")
- [Evaluating
  ML Models](../../../machine-learning/latest/dg/evaluating_models.md "../../../machine-learning/latest/dg/evaluating_models.md")
- [Feature
  Processing with Spark ML and Scikit-learn](../../../sagemaker/latest/dg/inference-pipeline-mleap-scikit-learn-containers.md "../../../sagemaker/latest/dg/inference-pipeline-mleap-scikit-learn-containers.md")
- [Perform
  Automatic Model Tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [Amazon SageMaker AI Experiments: Track and Compare Tutorial](../../../sagemaker/latest/dg/experiments-mnist.md "../../../sagemaker/latest/dg/experiments-mnist.md")

## Blogs

- [Running
  multiple HPO jobs in parallel on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/")
- [Optimizing
  portfolio value with Amazon SageMaker AI automatic model
  tuning](https://aws.amazon.com/blogs/machine-learning/optimizing-portfolio-value-with-amazon-sagemaker-automatic-model-tuning/ "https://aws.amazon.com/blogs/machine-learning/optimizing-portfolio-value-with-amazon-sagemaker-automatic-model-tuning/")
- [Utilizing
  XGBoost training reports to improve your models](https://aws.amazon.com/blogs/machine-learning/utilizing-xgboost-training-reports-to-improve-your-models/ "https://aws.amazon.com/blogs/machine-learning/utilizing-xgboost-training-reports-to-improve-your-models/")

## Videos

- [Tune
  your ML models to the highest accuracy with automatic
  model tuning](https://www.youtube.com/watch?v=T056YRprQIw "https://www.youtube.com/watch?v=T056YRprQIw")
- [Organize,
  Track, and Evaluate ML Training Runs With Amazon SageMaker AI
  Experiments](https://www.youtube.com/watch?v=zLOMYKZGxK0 "https://www.youtube.com/watch?v=zLOMYKZGxK0")

## Examples

- [Feature
  Engineering Immersion Day Workshop](https://sagemaker-immersionday.workshop.aws/lab1.html "https://sagemaker-immersionday.workshop.aws/lab1.html")
- [Improving
  Forecast Accuracy with Machine Learning](https://aws.amazon.com/solutions/implementations/improving-forecast-accuracy-with-machine-learning/ "https://aws.amazon.com/solutions/implementations/improving-forecast-accuracy-with-machine-learning/")
- [Ensemble
  Predictions From Multiple Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html")
