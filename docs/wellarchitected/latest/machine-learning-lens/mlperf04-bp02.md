# MLPERF04-BP02 Explore alternatives for performance

improvement

Benchmarking your machine learning models allows you to
systematically improve performance by evaluating and comparing
different algorithms, features, and architectural resources. Use
this practice to identify the optimal combination and achieve your
desired performance metrics.

**Desired outcome:** You implement a
systematic approach to improving your machine learning model's
performance through benchmarking various techniques. You'll
establish a baseline model and methodically explore alternatives
including data volume increases, feature engineering, algorithm
selection, ensemble methods, and hyperparameter tuning. This results
in optimized models that provide higher accuracy and better business
value.

**Common anti-patterns:**

- Selecting a complex algorithm without establishing a baseline.
- Ignoring feature engineering in favor of only trying different
  algorithms.
- Using more data without understanding its quality or relevance.
- Focusing exclusively on accuracy while ignoring other important
  metrics.
- Manually testing hyperparameters without a systematic approach.

**Benefits of establishing this best
practice:**

- Improved model accuracy and performance.
- Better understanding of which factors most influence model
  performance.
- More efficient use of computational resources.
- Systematic approach to model improvement instead of random
  experimentation.
- Ability to document and reproduce experiments for future
  reference.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Performance improvement in machine learning requires a structured,
iterative approach. Benchmarking assists you in systematically
comparing different approaches and determining the most effective
path to improved model performance. Start by establishing a
baseline with simple algorithms and obvious features, then
methodically explore alternatives to improve upon that baseline.

You can explore multiple avenues for improving performance:
increasing data volume, engineering better features, selecting
more appropriate algorithms, combining models through ensemble
methods, and tuning hyperparameters. Each approach provides unique
benefits and may be more or less effective depending on your use
case. The key is to follow a systematic process, measure results
accurately, and document what you learn.

### Implementation steps

1. **Establish a baseline
   model**. Start with a simple architecture, obvious
   features, and a straightforward algorithm to create your
   baseline. Use
   [Amazon SageMaker AI built-in algorithms](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md") to quickly develop this
   initial model. This gives you a reference point for
   comparing future experiments and improvements.
2. **Set up experiment
   tracking**. Use
   [Amazon SageMaker AI Managed MLFlow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to organize, track, compare,
   and evaluate your machine learning experiments. Create a
   structured framework that tracks performance metrics,
   algorithm choices, features used, and hyperparameter
   settings so you can effectively compare results across
   different approaches.
3. **Test different
   algorithms**. Systematically test various
   algorithms, starting with simpler ones and progressively
   trying more complex options. SageMaker AI provides many
   built-in algorithms that you can compare. Document how each
   algorithm performs relative to your baseline and identify
   which ones show the most promise for your data and problem.
4. **Apply feature
   engineering**. Extract important signals in your
   data through feature engineering. This may include feature
   selection, transformation, creation of new features,
   normalization, and encoding techniques. Use
   [SageMaker AI
   Feature Store](../../../sagemaker/latest/dg/feature-store-create-feature-group.md "../../../sagemaker/latest/dg/feature-store-create-feature-group.md") to manage and share features across
   experiments and teams.
5. **Increase data volume and
   quality**. Evaluate whether adding more data or
   improving data quality could assist your model. More data
   often broadens the statistical range and improve model
   performance, but only if the additional data is relevant and
   of good quality.
6. **Implement ensemble
   methods**. Combine multiple models to leverage
   different strengths and compensate for individual
   weaknesses. Techniques like bagging, boosting, and stacking
   can often improve overall accuracy. SageMaker AI makes it
   simple to implement ensemble predictions from multiple
   models.
7. **Perform hyperparameter
   tuning**. Use
   [Amazon SageMaker AI Automatic Model Tuning](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md") to optimize your
   model's hyperparameters. This service automates the search
   through different hyperparameter combinations to find
   optimal values that improve model performance. You can run
   multiple HPO jobs in parallel to speed up the process.
8. **Evaluate improvements
   systematically**. For each change, rigorously
   evaluate whether performance has improved based on relevant
   metrics for your problem. Use SageMaker AI's evaluation tools
   to compare results across experiments and determine which
   approaches deliver the most gains.
9. **Optimize for production**.
   Once you've identified the best performing approach,
   optimize it for production deployment. Consider factors like
   inference latency, model size, and resource requirements
   alongside pure performance metrics.
10. **Document findings and
    methodology**. Create comprehensive documentation
    of your benchmarking process, including what worked, what
    didn't, and why. This provides valuable information for
    future model improvements and builds institutional
    knowledge.

## Resources

**Related documents:**

- [Built-in
  algorithms and pretrained models in Amazon SageMaker AI](../../../sagemaker/latest/dg/algos.md "../../../sagemaker/latest/dg/algos.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Automatic
  model tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [Use
  Feature Store with SDK for Python (Boto3)](../../../sagemaker/latest/dg/feature-store-create-feature-group.md "../../../sagemaker/latest/dg/feature-store-create-feature-group.md")
- [Feature
  Processing with Spark ML and Scikit-learn](../../../sagemaker/latest/dg/inference-pipeline-mleap-scikit-learn-containers.md "../../../sagemaker/latest/dg/inference-pipeline-mleap-scikit-learn-containers.md")
- [Running
  multiple HPO jobs in parallel on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/running-multiple-hpo-jobs-in-parallel-on-amazon-sagemaker/")
- [Optimizing
  portfolio value with Amazon SageMaker AI automatic model
  tuning](https://aws.amazon.com/blogs/machine-learning/optimizing-portfolio-value-with-amazon-sagemaker-automatic-model-tuning/ "https://aws.amazon.com/blogs/machine-learning/optimizing-portfolio-value-with-amazon-sagemaker-automatic-model-tuning/")

**Related videos:**

- [How
  To Efficiently Manage ML experiments using Amazon SageMaker AI ML
  Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k "https://www.youtube.com/watch?v=3xkz_5HOP6k")
- [Train
  large models on Amazon SageMaker AI for scale and
  performance](https://www.youtube.com/watch?v=cryA1LFwS98 "https://www.youtube.com/watch?v=cryA1LFwS98")

**Related examples:**

- [Feature
  Engineering Immersion Day Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab1-feature-engineering "https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab1-feature-engineering")
- [Ensemble
  Predictions From Multiple Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html")
- [Amazon SageMaker AI Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples "https://github.com/aws/amazon-sagemaker-examples")
