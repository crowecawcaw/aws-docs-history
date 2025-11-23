# MLREL03-BP04 Establish data bias detection and

mitigation

Detect and mitigate bias to avoid inaccurate model results.
Establish bias detection methodologies at data preparation stage
before training starts. Monitor, detect, and mitigate bias after the
model is in production. Establish feedback loops to track the drift
over time and initiate a re-training.

**Desired outcome:** You can identify
and address biases in your machine learning data and models,
providing fair and accurate predictions. You have established
systematic approaches for detecting bias before training and
continuously monitoring bias in production. Your AI systems produce
more reliable, fair, and trustworthy results through automated
detection and mitigation processes.

**Common anti-patterns:**

- Waiting until after model deployment to consider bias detection.
- Using a single bias metric for each use case without
  understanding context-specific requirements.
- Focusing only on training data bias and ignoring bias that may
  emerge in production.
- Failing to establish feedback mechanisms to monitor and address
  drift over time.
- Treating bias detection as a one-time activity rather than an
  ongoing process.

**Benefits of establishing this best
practice:**

- Improves model accuracy and fairness across different
  demographic groups.
- Reduces risk of deploying models with harmful or discriminatory
  outcomes.
- Enhances transparency and explainability for model predictions.
- Increases trust from users and stakeholders in AI systems.
- Improves adherence to emerging AI regulations and ethical
  guidelines.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Bias in machine learning models can lead to unfair or inaccurate
outcomes that disproportionately impact certain groups. You need a
systematic approach to detect and mitigate bias throughout the
machine learning lifecycle. This begins with careful analysis of
your training data to identify potential imbalances or historical
biases that could be propagated by your models. By implementing
bias detection methodologies before training, you can address
issues early in the development process.

Once your models are in production, ongoing monitoring is
essential as new data patterns may introduce unexpected biases
over time. Setting up automated detection systems allows you to
continuously evaluate model fairness and take corrective actions
when necessary. Building feedback loops provides the data needed
to understand how bias manifests in real-world applications and
informs model retraining strategies.

Amazon SageMaker AI provides comprehensive tools like SageMaker AI
Clarify to implement bias detection and mitigation strategies
throughout the ML lifecycle. These tools offer quantitative
metrics to measure different types of bias and provide
explanations for model predictions to understand and address the
root causes of unfairness.

### Implementation steps

1. **Understand different types of
   bias**. Begin by educating your team about various
   forms of bias that can affect machine learning models,
   including selection bias, measurement bias, aggregation
   bias, and evaluation bias. Educate your team members on how
   bias can be introduced at different stages of the ML
   lifecycle and the potential impacts on model predictions.
2. **Analyze your training
   data**. Use
   [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") to examine your training data for
   potential bias before model development. Analyze the
   distribution of sensitive attributes and identify imbalances
   or correlations that could lead to unfair outcomes. Address
   data imbalances through techniques like resampling,
   weighting, or generating synthetic data for underrepresented
   groups.
3. **Select appropriate bias
   metrics**. Choose bias metrics that align with your
   specific use case and fairness requirements. SageMaker AI
   Clarify provides multiple pre-training bias metrics
   including class imbalance, difference in proportions of
   labels, and conditional demographic disparity. For
   post-training, metrics like disparate impact, difference in
   positive proportions across predicted labels, and accuracy
   difference can evaluate model fairness.
4. **Run SageMaker AI Clarify processing
   jobs**. Integrate
   [SageMaker AI
   Clarify processing jobs](../../../sagemaker/latest/dg/clarify-processing-job-run.md "../../../sagemaker/latest/dg/clarify-processing-job-run.md") into your ML pipeline to
   analyze bias and provide explainability. Configure these
   jobs to calculate bias metrics on your training data and
   model predictions, identifying potential issues before
   deployment.
5. **Implement bias mitigation
   strategies**. Address identified biases using
   techniques like preprocessing (modifying training data),
   in-processing (incorporating fairness constraints during
   training), or post-processing (adjusting model outputs).
   Experiment with different approaches and measure their
   impact on both fairness metrics and model performance.
6. **Set up production
   monitoring**. Configure
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to continuously track bias
   metrics on production data. Create alerts that alarm when
   bias metrics exceed predefined thresholds, enabling prompt
   investigation and remediation of emerging issues.
7. **Establish feedback loops**.
   Implement mechanisms to collect and analyze feedback on
   model predictions, particularly focusing on cases where bias
   may be present. Use this feedback to improve your
   understanding of real-world bias patterns and inform model
   retraining strategies.
8. **Generate model governance
   reports**. Use SageMaker AI Clarify to create
   comprehensive reports on model fairness and explainability
   for stakeholders, including risk and compliance-aligned
   teams and external regulators. These reports should document
   your bias detection and mitigation efforts, providing
   transparency into your responsible AI practices.
9. **Conduct regular model
   reviews**. Schedule periodic reviews of your
   models' fairness performance, bringing together
   cross-functional teams to evaluate bias metrics, examine
   challenging cases, and decide on necessary interventions or
   improvements.

## Resources

**Related documents:**

- [Run
  SageMaker AI Clarify Processing Jobs for Bias Analysis and
  Explainability](../../../sagemaker/latest/dg/clarify-processing-job-run.md "../../../sagemaker/latest/dg/clarify-processing-job-run.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Fairness,
  model explainability and bias detection with SageMaker AI
  Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency
  of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/ "https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/")
- [Build
  a secure enterprise machine learning platform on AWS](../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md "../../../whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.md")

**Related videos:**

- [Introducing
  Amazon SageMaker AI Clarify, part 1 - Bias detection](https://www.youtube.com/watch?v=jvcPZmnXaxo "https://www.youtube.com/watch?v=jvcPZmnXaxo")
- [Introducing
  Amazon SageMaker AI Clarify, part 2 - Model explainability](https://www.youtube.com/watch?v=1IGMG_c280E "https://www.youtube.com/watch?v=1IGMG_c280E")
- [Responsible
  use of artificial intelligence and machine learning](https://pages.awscloud.com/Responsible-Use-of-Artificial-Intelligence-and-Machine-Learning_2022_1007-MCL_OD.html "https://pages.awscloud.com/Responsible-Use-of-Artificial-Intelligence-and-Machine-Learning_2022_1007-MCL_OD.html")

**Related examples:**

- [Amazon SageMaker AI Clarify: ML Bias Detection and Explainability](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify")
- [Amazon SageMaker AI Model Monitoring](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops")
