# MLOPS03-BP02 Create tracking and version control

mechanisms

Machine learning model development requires robust tracking and
version control mechanisms due to its iterative and exploratory
nature. By implementing proper tracking systems, you can maintain
visibility of your experiments, data processing techniques, and
model versions while enabling reproducibility and collaboration.

**Desired outcome:** You have
comprehensive tracking of ML model development with experiment
tracking capabilities, version-controlled data processing code, and
a model registry that enables you to identify the best performing
models. Your development processes are reproducible, collaborative,
and automated with CI/CD pipelines for model deployment.

**Common anti-patterns:**

- Manually tracking experiments in spreadsheets or documents.
- Not documenting data processing steps or model configurations.
- Keeping models and datasets in local environments without
  version control.
- Starting new experiments from scratch instead of building on
  previous work.

**Benefits of establishing this best
practice:**

- Enhanced reproducibility of experiments and model training.
- Improved collaboration among data science teams.
- Better visibility into the performance of different model
  iterations.
- Faster identification of the best performing models.
- Ability to roll back to previous model versions if needed.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning development involves experimenting with multiple
combinations of data, algorithms, and parameters while observing
how incremental changes impact model accuracy. Without proper
tracking and version control, you risk losing valuable insights
and the ability to reproduce successful experiments.

To address these challenges, you need a systematic approach to
track experiments, version control your code and data processing
techniques, and manage model deployment. AWS SageMaker AI provides
integrated tools for experiment tracking, version control, and
model registry that can streamline your machine learning
operations.

By implementing proper tracking and versioning mechanisms, you can
document your model development journey, track performance metrics
across experiments, and reliability reproduce and deploy your
models. This creates a foundation for continuous improvement of
your machine learning applications.

### Implementation steps

1. **Track your ML experiments with
   SageMaker AI Experiments**. Use Amazon SageMaker AI
   Experiments to you create, manage, analyze, and compare your
   machine learning experiments. SageMaker AI Experiments
   automatically tracks inputs, parameters, configurations, and
   results of your iterations as runs. You can assign, group,
   and organize these runs into experiments. SageMaker AI
   Experiments integrates with Amazon SageMaker AI Studio,
   providing a visual interface to browse active and past
   experiments, compare runs on key performance metrics, and
   identify the best-performing models.
2. **Process data with SageMaker AI
   Processing**. For analyzing data, documenting
   processing, and evaluating ML models, use
   [Amazon SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md"). This capability can be used for
   feature engineering, data validation, model evaluation, and
   model interpretation. SageMaker AI Processing provides a
   standardized way to run your data processing workloads,
   fostering consistency and reproducibility.
3. **Use SageMaker AI Unified Studio for
   enhanced collaboration**. Use
   [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/") with enhanced collaborative
   features and team sharing capabilities for integrated data
   and AI workflows. The unified solution provides improved
   debugging and monitoring capabilities, VS Code server
   integration, and enhanced project sharing. This approach
   keeps your data processing code and documentation accessible
   while facilitating better collaboration and version tracking
   across teams.
4. **Use SageMaker AI Model
   Registry**. Catalog, manage, and deploy models
   using SageMaker AI Model Registry. Create a model group and,
   for each run of your ML pipeline, create a model version
   that you register in the model group. The Model Registry
   provides a centralized repository for model versions, making
   it more straightforward to track model lineage, compare
   model performance, and promote models to production.
5. **Implement CI/CD for model
   deployment**. Automate your model deployment
   process using CI/CD pipelines for consistent and reliable
   deployments. SageMaker AI Pipelines can be used to create
   end-to-end workflows that include model building,
   evaluation, and deployment steps. Implement CI/CD for model
   deployment to thoroughly test your models before they are
   deployed to production, reducing the risk of
   deployment-related issues.
6. **Integrate data version
   control**. Use tools like Data Version Control
   (DVC) in conjunction with SageMaker AI Experiments to track
   both your model code and the datasets used for training and
   evaluation. With these tools, you can completely reproduce
   your machine learning experiments.
7. **Create model cards for
   documentation**. For each model version in your
   registry, create comprehensive
   [SageMaker AI
   Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md") with enhanced documentation and
   governance capabilities that document the model's purpose,
   training data, performance metrics, limitations, and usage
   guidelines. This documentation helps users understand when
   and how to use specific model versions and supports improved
   model governance.

## Resources

**Related documents:**

- [Amazon SageMaker AI Experiments in Studio Classic](../../../sagemaker/latest/dg/experiments.md "../../../sagemaker/latest/dg/experiments.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Git
  repositories with SageMaker AI Notebook Instances](../../../sagemaker/latest/dg/nbi-git-repo.md "../../../sagemaker/latest/dg/nbi-git-repo.md")
- [MLOps
  Automation With SageMaker AI Projects](../../../sagemaker/latest/dg/sagemaker-projects.md "../../../sagemaker/latest/dg/sagemaker-projects.md")
- [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Data
  transformation workloads with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")

**Related examples:**

- [SageMaker AI
  Experiment Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments")
- [SageMaker AI
  Model Registry Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines")
- [Amazon SageMaker AI processing](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html")
