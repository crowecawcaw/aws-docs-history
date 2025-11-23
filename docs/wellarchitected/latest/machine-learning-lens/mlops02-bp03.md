# MLOPS02-BP03 Establish model improvement strategies

Planning improvement drivers for optimizing machine learning model
performance is essential before development begins. By establishing
a clear strategy for model enhancement, you can systematically
improve your ML models through techniques like data collection,
cross-validation, feature engineering, hyperparameter tuning, and
ensemble methods.

**Desired outcome:** By implementing
this best practice, you establish a systematic approach for
improving your machine learning models. You create a structured
methodology for experimentation that allows you to progressively
enhance model performance by testing different improvement
strategies. You gain visibility into which approaches yield the best
results for your specific use case, enabling you to make data-driven
decisions about model development and optimization.

**Common anti-patterns:**

- Starting with overly complex models without establishing a
  baseline performance.
- Ignoring data quality issues and focusing solely on model
  complexity.
- Making arbitrary hyperparameter changes without systematic
  experimentation.
- Neglecting to document experimental results and configurations.
- Implementing advanced techniques without understanding
  fundamental model performance issues.

**Benefits of establishing this best
practice:**

- Enables structured experimentation and measurable model
  improvements.
- Provides clarity on which improvement strategies deliver the
  best results.
- Reduces time spent on ineffective optimization approaches.
- Creates a systematic pathway from simple to more advanced
  modeling techniques.
- Identifies the most important features and data for your
  specific business problem.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Effective model improvement requires a structured approach that
follows a progression from simple to complex. Begin by
establishing clear performance metrics tied to your business
objectives, as these will guide your improvement efforts. Develop
a baseline model using straightforward algorithms and minimal
feature engineering to set initial performance benchmarks.

Organizing your experiments systematically is crucial. Document
your approach, model configurations, and results to track
improvements and understand the impact of different strategies.
This documentation serves as institutional knowledge that can
guide future model development and improvement efforts.

Work closely with domain experts who understand the business
context. Their insights can identify key features, validate model
outputs, and align your improvements with business objectives.
Remember that model improvement is an iterative process requiring
patience and methodical experimentation.

### Implementation steps

1. **Create a baseline model with minimal
   complexity**. Start with minimal data cleaning and
   the most obvious data features. Train simple classical
   models using algorithms like linear regression or logistic
   regression for classification tasks. This establishes a
   performance benchmark against which you can measure
   improvements. Use
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") to quickly develop these baseline models.
2. **Organize and track experiments using
   MLFlow on Amazon SageMaker AI**. Use
   [Amazon SageMaker AI MLFlow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to organize and track multiple
   tests comparing different configurations and algorithms.
   This allows you to maintain a structured approach to
   experimentation and compare results across different model
   versions so you can identify which changes lead to
   meaningful improvements.
3. **Implement effective feature
   selection**. Collaborate with subject matter
   experts to identify the most significant features related to
   target values. Iteratively add more complex features and
   remove less important ones to improve model accuracy and
   robustness. Test different feature engineering techniques
   such as one-hot encoding, normalization, and dimensionality
   reduction to understand their impact on model performance.
4. **Consider deep learning for complex
   patterns**. When you have large volumes of training
   data, consider deep learning models to discover previously
   unknown features and improve model accuracy.
   [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/") provides built-in algorithms for deep
   learning and supports popular frameworks like TensorFlow and
   PyTorch, making it simpler to experiment with neural network
   architectures.
5. **Explore ensemble methods**.
   Ensemble methods can provide further accuracy improvements
   by combining the best characteristics of various algorithms.
   Consider techniques like random forests, gradient boosting,
   or stacking different models. Be aware of the tradeoffs with
   computational performance and maintenance complexity,
   evaluating whether these approaches align with your specific
   business use case.
6. **Apply automatic machine learning
   (AutoML)**. Use
   [Amazon SageMaker AI Canvas](https://aws.amazon.com/sagemaker/canvas/ "https://aws.amazon.com/sagemaker/canvas/") for no-code/low-code ML model
   development with natural language support for data
   exploration and preparation. Canvas includes
   [Amazon Q integration](../../../sagemaker/latest/dg/canvas-q-integration.md "../../../sagemaker/latest/dg/canvas-q-integration.md") for conversational data analysis and
   can directly deploy models to production.
7. **Optimize hyperparameters
   systematically**. Fine-tune hyperparameters for
   each algorithm to obtain optimal performance. Use
   [Amazon SageMaker AI Hyperparameter Optimization](../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md "../../../sagemaker/latest/dg/automatic-model-tuning-how-it-works.md") to automate
   this process through techniques like Bayesian optimization,
   grid search, or random search to find the most effective
   parameter combinations.
8. **Integrate experiments into automated
   workflows**.
   [Automate
   your experimental trials using SageMaker AI Pipelines](../../../sagemaker/latest/dg/pipelines-experiments.md "../../../sagemaker/latest/dg/pipelines-experiments.md") by
   using the integration with experiments. This fosters
   reproducibility and creates a systematic approach to model
   improvement that can be incorporated into your ML operations
   workflow.
9. **Use generative AI for synthetic data
   creation**. For scenarios with limited training
   data, use generative AI techniques like generative
   adversarial networks (GANs) to create synthetic data that
   can expand your training dataset.
   [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/") provides an expanded library of
   pre-built generative AI models and more industry-specific
   solutions, while
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") offers foundation models that can augment
   your training data, especially for scenarios with limited or
   imbalanced datasets.
10. **For generative AI workloads, apply
    foundation models with RAG for knowledge-intensive
    tasks**. For tasks requiring domain knowledge,
    implement retrieval-augmented generation (RAG) using
    [Amazon
    Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") to enhance foundation models with your
    organization's specific information, combining the power of
    large language models with your proprietary data.

## Resources

**Related documents:**

- [Amazon SageMaker AI Experiments in Studio Classic](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md")
- [Accelerate
  generative AI development using managed MLFlow on SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md")
- [Automatic
  model tuning with SageMaker AI](../../../sagemaker/latest/dg/automatic-model-tuning.md "../../../sagemaker/latest/dg/automatic-model-tuning.md")
- [SageMaker AI
  JumpStart pretrained models](../../../sagemaker/latest/dg/studio-jumpstart.md "../../../sagemaker/latest/dg/studio-jumpstart.md")
- [Amazon SageMaker AI Experiments Integration](../../../sagemaker/latest/dg/pipelines-experiments.md "../../../sagemaker/latest/dg/pipelines-experiments.md")
- [Create,
  store, and share features with Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [LLM
  experimentation at scale using Amazon SageMaker AI Pipelines and
  MLFlow](https://aws.amazon.com/blogs/machine-learning/llm-experimentation-at-scale-using-amazon-sagemaker-pipelines-and-mlflow/ "https://aws.amazon.com/blogs/machine-learning/llm-experimentation-at-scale-using-amazon-sagemaker-pipelines-and-mlflow/")

**Related examples:**

- [Amazon SageMaker AI Experiments Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments")
- [Hyperparameter
  Tuning Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning "https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning")
- [Ensemble
  Predictions from Multiple Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html")
- [Amazon SageMaker AI Autopilot Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot "https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot")
