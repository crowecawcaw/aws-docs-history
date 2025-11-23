# MLPERF04-BP03 Establish a model performance evaluation

pipeline

Establish an end-to-end model performance evaluation pipeline that
captures key metrics to evaluate your model's success, align with
business KPIs, and automatically test performance when models or
data are updated.

**Desired outcome:** You can
systematically evaluate model performance through automated
pipelines that measure relevant metrics specific to your use case.
Your evaluation process runs automatically whenever model or data
updates occur, creating a continuous quality assessment. This
assists you in maintaining high-performing models that deliver
business value while providing transparency into model behavior and
performance over time.

**Common anti-patterns:**

- Relying solely on training accuracy without considering
  real-world performance metrics.
- Manual evaluation of models that leads to inconsistency.
- Using generic metrics that don't align with business KPIs.
- Waiting until deployment to evaluate model performance.
- Not establishing automated evaluation triggers when models or
  data change.

**Benefits of establishing this best
practice:**

- Verifies that models maintain expected performance levels over
  time.
- Provides data-driven decision making for model selection and
  deployment.
- Aligns machine learning outcomes with business objectives.
- Enables faster identification and resolution of performance
  degradation.
- Improves regulatory adherence through consistent evaluation
  protocols.
- Increases stakeholder confidence through transparent performance
  reporting.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model performance evaluation is critical to verify that your
machine learning solutions deliver on their intended business
outcomes. By establishing a robust, automated evaluation pipeline,
you can consistently assess how well your models perform against
business KPIs and make data-driven decisions about deployment
readiness.

Avoid relying solely on training accuracy without considering
real-world performance metrics. Many organizations use manual,
ad-hoc evaluation of models that leads to inconsistency, use
generic metrics that don't align with business KPIs, wait until
deployment to evaluate model performance, and fail to establish
automated evaluation runs when models or data change.

Your evaluation pipeline should incorporate metrics specific to
your use case. For regression problems, this might include Root
Mean Squared Error (RMSE). For classification tasks, accuracy,
precision, recall, F1 score, and area under the curve (AUC) are
common metrics. These technical metrics should tie directly to
business KPIs, helping stakeholders understand the model's
contribution to business goals.

Automating the evaluation process provides consistency and reduces
manual errors. When new data arrives or models are updated, your
pipeline should automatically run evaluations, providing
continuous feedback on model performance and enabling rapid
identification of any degradation issues.

### Implementation steps

1. **Define business objectives and
   evaluation criteria**. Begin by clearly defining
   what success means for your machine learning use case.
   Identify relevant business KPIs and determine which
   technical metrics (like accuracy, precision, recall, F1
   score, RMSE, AUC) best align with these business goals.
   Document these metrics and their target values to establish
   clear evaluation criteria.
2. **Create an end-to-end workflow with
   Amazon SageMaker AI Pipelines**. Start with a workflow
   template to establish an initial infrastructure for model
   training and deployment.
   [SageMaker AI
   Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md") can automate different steps of the ML
   workflow including data loading, data transformation,
   training, tuning, and deployment. Within SageMaker AI
   Pipelines, the
   [SageMaker AI
   Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md") tracks model versions and respective
   artifacts, including metadata and lineage data collected
   throughout the model development lifecycle.
3. **Implement model evaluation
   components in your pipeline**. Design dedicated
   evaluation steps within your pipeline that calculate
   relevant metrics for your model. Use
   [SageMaker AI
   Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md") jobs or custom Python scripts to perform
   evaluations on validation datasets. Store evaluation results
   in a central location for tracking performance over time.
4. **Set up automated prompts for
   evaluation**. Configure your pipeline to
   automatically initiate the evaluation process whenever
   there's a model update or new training data becomes
   available. This provides continuous quality assessment and
   identifies performance degradation early.
5. **Create visualization and reporting
   mechanisms**. Implement dashboards or reports that
   display model performance metrics in a straightforward
   format. Stakeholders can use visualizations to quickly
   assess model performance against business KPIs and make
   informed decisions about model deployment.
6. **Establish model approval
   workflows**. Define criteria for model approval
   based on evaluation results. Implement approval workflows in
   the SageMaker AI Model Registry that automatically promote
   models meeting performance thresholds to production, while
   flagging underperforming models for review.
7. **Implement A/B testing
   capabilities**. For production models, set up A/B
   testing infrastructure to compare performance of new models
   against baseline models using real-world data. This provides
   additional validation before fully deploying model updates.
8. **Monitor production model
   performance**. Use
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to continuously monitor
   deployed models for data drift, model drift, and performance
   degradation. Set up alerts when performance metrics fall
   below acceptable thresholds.
9. **Implement bias detection and
   fairness evaluation**. Use
   [Amazon SageMaker AI Clarify](../../../sagemaker/latest/dg/clarify-processing-job-run.md "../../../sagemaker/latest/dg/clarify-processing-job-run.md") to detect bias in your models and
   check fairness across different demographic groups. Include
   bias metrics as part of your evaluation criteria.
10. **Create feedback loops for continuous
    improvement**. Design mechanisms to capture
    feedback from production model performance and incorporate
    these insights into future model iterations. This creates a
    cycle of continuous improvement based on real-world
    performance.

## Resources

**Related documents:**

- [Amazon SageMaker AI Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
- [Define
  a pipeline](../../../sagemaker/latest/dg/define-pipeline.md "../../../sagemaker/latest/dg/define-pipeline.md")
- [Model
  Registration Deployment with Model Registry](../../../sagemaker/latest/dg/model-registry.md "../../../sagemaker/latest/dg/model-registry.md")
- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Fairness
  and Explainability with SageMaker AI Clarify](../../../sagemaker/latest/dg/clarify-processing-job-run.md "../../../sagemaker/latest/dg/clarify-processing-job-run.md")
- [Data
  transformation workloads with SageMaker AI Processing](../../../sagemaker/latest/dg/processing-job.md "../../../sagemaker/latest/dg/processing-job.md")
- [Building,
  automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/ "https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/")
- [Extend
  Amazon SageMaker AI Pipelines to include custom steps using
  callback steps](https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/ "https://aws.amazon.com/blogs/machine-learning/extend-amazon-sagemaker-pipelines-to-include-custom-steps-using-callback-steps/")

**Related videos:**

- [Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=Hvz2GGU3Z8g "https://www.youtube.com/watch?v=Hvz2GGU3Z8g")
- [How
  to create fully automated ML workflows with Amazon SageMaker AI
  Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg "https://www.youtube.com/watch?v=W7uabCTfLrg")

**Related examples:**

- [Orchestrate
  your build and train pipeline with SageMaker AI Pipelines](https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab6-mlops/pipelines "https://catalog.us-east-1.prod.workshops.aws/workshops/63069e26-921c-4ce1-9cc7-dd882ff62575/en-US/lab6-mlops/pipelines")
- [SageMaker AI
  Model Evaluation Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines")
- [MLOps
  with SageMaker AI Pipelines](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop "https://github.com/aws-samples/amazon-sagemaker-mlops-workshop")
