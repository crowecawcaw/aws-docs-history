# MLSEC04-BP03 Protect against data poisoning threats

Protect your machine learning models and data by implementing
security measures against data poisoning attacks, which can
compromise model performance and accuracy. Data poisoning occurs
through data injection (adding corrupt training data) or data
manipulation (changing existing data like labels), resulting in
inaccurate and weakened predictive capabilities. By identifying and
addressing corrupt data using security methods and anomaly detection
algorithms, you can maintain data integrity and protect against
threats including ransomware and malicious code in third-party
packages.

**Desired outcome:** You have
implemented robust protection mechanisms for your machine learning
training data and models. These protections include data validation
procedures, monitoring for data drift, version control for both data
and models, and rollback capabilities. Your ML systems can detect
potential poisoning attempts and maintain model performance
integrity through security best practices that protect data
throughout its lifecycle.

**Common anti-patterns:**

- Collecting training data from untrusted or unverified sources
  without validation.
- Neglecting to monitor data distributions for unexpected shifts.
- Deploying updated models without thorough testing against
  baseline performance.
- Failing to implement version control for both training data and
  models.
- Not having a rollback strategy for compromised models.

**Benefits of establishing this best
practice:**

- Improved model reliability and accuracy through clean, trusted
  data.
- Early detection of potential security breaches targeting
  training data.
- Reduced risk of deploying compromised models to production.
- Ability to quickly recover from poisoning incidents through
  rollback mechanisms.
- Enhanced overall ML system security and resilience.

**Risk level for not implementing this
practice:** High

## Implementation guidance

Data poisoning represents a security threat to machine learning
systems. When malicious actors manipulate training data, they can
compromise model integrity and cause downstream impacts on
decisions or predictions made by those models. You need to
implement comprehensive protections throughout your ML pipeline,
from data collection to model deployment and monitoring.

Start by establishing strict controls over data sources and
implementing validation procedures to detect anomalies before
training. During model development, implement monitoring for data
drift that could indicate poisoning attempts. Before deployment,
thoroughly compare new models against previous versions to
identify unexpected behavior changes. Finally, maintain versioned
copies of both training data and models to enable rapid recovery
from compromise.

By combining these defensive approaches, you create multiple
layers of protection that make your ML systems resilient against
data poisoning attempts.

### Implementation steps

1. **Use only trusted data sources for
   training data**. Verify the provenance of data used
   for training and implement audit controls that allow you to
   track changes to training data. This includes recording who
   made changes, what changes were made, and when they
   occurred. Before using data for training, validate its
   quality to identify potential outliers and incorrectly
   labeled samples that could indicate poisoning attempts.
2. **Look for underlying shifts in the
   patterns and distributions in training data**.
   Implement continuous monitoring for data drift to detect
   unexpected changes in data distributions. Use tools like
   [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/") to track these changes
   automatically. Deviations from established patterns can
   serve as early warning signs of unauthorized access or
   manipulation targeting training data.
3. **Identify model updates that
   negatively impact the results before moving them to
   production**. Compare newly trained models against
   previous versions using consistent test datasets. Look for
   unexpected performance changes, especially degradations in
   specific areas that weren't present in earlier model
   iterations. Use
   [Amazon SageMaker AI MLflow Model Registry](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to track model
   versions and their performance metrics.
4. **Have a rollback plan**.
   Implement versioning for both training data and models to
   enable quick recovery from compromised states. Use
   [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/") to maintain secure, versioned
   features for your ML models. The Feature Store provides a
   centralized repository for features with built-in security
   controls. Configure Amazon SageMaker AI MLflow Model Registry
   to support rollback capabilities so you can quickly revert
   to a known good model version if issues are detected with a
   newly deployed model.
5. **Use low-entropy classification
   cases**. Establish performance thresholds and
   monitor for unexpected classification patterns. Define
   boundaries for acceptable model behavior and create alerts
   when outputs deviate from expected patterns. This can
   identify subtle poisoning attempts that might otherwise go
   undetected through conventional testing.
6. **Implement end-to-end encryption for
   ML data**. Secure your training data, feature sets,
   and models using encryption both at rest and in transit. Use
   [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/") to manage encryption keys
   and apply them consistently across your ML pipeline.
   Encryption protects against unauthorized access that could
   lead to data poisoning.
7. **Regularly scan for vulnerabilities
   in ML dependencies**. Use tools like
   [Amazon Inspector](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/") to detect vulnerabilities in the software
   packages and dependencies used in your ML environment. Data
   poisoning can occur through compromised third-party
   libraries, so regular scanning can identify potential entry
   points for bad actors.
8. **Implement input validation for AI
   systems**. For AI models, validate inputs for
   potential poisoning attempts. Implement filtering and
   sanitization of inputs to block adversarial inputs that
   could manipulate model behavior or extract sensitive
   information.

## Resources

**Related documents:**

- [Bias
  drift for models in production](../../../sagemaker/latest/dg/clarify-model-monitor-bias-drift.md "../../../sagemaker/latest/dg/clarify-model-monitor-bias-drift.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Create,
  store, and share features with Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Automated
  monitoring of your machine learning models with Amazon SageMaker AI Model Monitor and sending predictions to human
  review workflows using Amazon A2I](https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/ "https://aws.amazon.com/blogs/machine-learning/automated-monitoring-of-your-machine-learning-models-with-amazon-sagemaker-model-monitor-and-sending-predictions-to-human-review-workflows-using-amazon-a2i/")
- [Amazon SageMaker AI Model Monitor– Fully Managed Automatic Monitoring
  for Your Machine Learning Models](https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/ "https://aws.amazon.com/blogs/aws/amazon-sagemaker-model-monitor-fully-managed-automatic-monitoring-for-your-machine-learning-models/")
- [7
  ways to improve security of your machine learning
  workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")
- [Building
  secure machine learning environments with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/building-secure-machine-learning-environments-with-amazon-sagemaker/")

**Related videos:**

- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")
- [Inawisdom:
  Machine Learning and Automated Model Retraining with SageMaker AI](https://www.youtube.com/watch?v=1kbWvlHBYLk&t=7s "https://www.youtube.com/watch?v=1kbWvlHBYLk&t=7s")

**Related examples:**

- [Amazon SageMaker AI Model Monitor Examples](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops "https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops")
- [Amazon SageMaker AI Feature Store Examples](https://github.com/aws-samples/amazon-sagemaker-feature-store-examples "https://github.com/aws-samples/amazon-sagemaker-feature-store-examples")
