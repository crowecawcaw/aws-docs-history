# MLSEC05-BP01 Protect against adversarial and malicious

activities

Machine learning systems must be robust against adversarial inputs
designed to manipulate their behavior. Implementing protection
mechanisms both inside and outside of your deployed models can
detect malicious inputs that could lead to incorrect predictions,
allowing you to automatically identify unauthorized changes, repair
compromised inputs, and validate data before it's used for further
training.

**Desired outcome:** You can detect,
mitigate, and protect your ML models from adversarial exploits that
attempt to manipulate inputs, preserving model integrity and
providing reliable predictions. Your ML systems incorporate robust
validation processes, ensemble approaches, and monitoring
capabilities that maintain consistent performance even when faced
with deliberately perturbed or malicious inputs.

**Common anti-patterns:**

- Implementing ML models without considering potential adversarial
  threats.
- Focusing solely on model performance metrics without evaluating
  robustness.
- Using single model architectures that are vulnerable to targeted
  threats.
- Retraining models with unvalidated inputs that may contain
  adversarial examples.
- Exposing ML models through unsecured endpoints without
  monitoring capabilities.

**Benefits of establishing this best
practice:**

- Improved model robustness against input manipulation attempts.
- Enhanced detection of potential security threats targeting ML
  systems.
- Greater reliability in model predictions even under adversarial
  conditions.
- Protection against data poisoning during model retraining.
- Reduced vulnerability to model extraction and inference threats.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Adversarial threats against machine learning models involve
deliberately crafting inputs to cause incorrect predictions or
undesirable behaviors. These threats can range from subtle
perturbations that are imperceptible to humans but cause model
errors, to more sophisticated techniques that exploit model
vulnerabilities. Building protection against adversarial
activities requires a multi-layered approach combining robust
model design, comprehensive monitoring, and secure deployment
strategies.

When implementing defenses, you need to understand the specific
vulnerabilities in your models and the potential impact of
adversarial threats on your business outcomes. This requires
conducting thorough evaluations of model behavior under different
threats scenarios and implementing appropriate countermeasures
based on your risk profile. Both pre-deployment testing and
continuous monitoring during production are essential components
of a comprehensive protection strategy.

Adversarial robustness should be considered from the beginning of
your ML development process rather than as an afterthought. By
incorporating adversarial training, ensemble methods, and input
validation techniques during model development, you can create
systems that are inherently more resistant to threats.
Additionally, implementing proper access controls, monitoring
systems, and incident response procedures can establish a secure
operational environment for your ML models.

### Implementation steps

1. **Evaluate the robustness of your
   algorithm**. Conduct sensitivity analysis to
   understand how your model responds to perturbed inputs. Test
   your model with increasingly modified data points to
   identify decision boundaries that might be vulnerable to
   manipulation. Use adversarial testing frameworks to simulate
   potential threats and measure their impact on model
   performance. Document the types of perturbations that cause
   incorrect predictions to inform your defense strategy.
2. **Build for robustness from the
   start**. Select diverse features during model
   design to improve resilience against outliers and
   adversarial examples. Implement ensemble methods by
   combining multiple models with different architectures or
   training approaches to increase decision diversity. Consider
   techniques like adversarial training where you intentionally
   incorporate adversarial examples into your training data to
   make your models more resistant to threats.
3. **Identify repeats and suspicious
   patterns**. Deploy
   [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/") to continuously analyze
   inference data and detect unusual patterns such as repeated
   similar inputs that may indicate probing threats. Set up
   alerts for anomalous input distributions that differ from
   training data. Monitor for evidence of model brute-forcing,
   where bad actors systematically vary limited sets of input
   features to determine decision boundaries and derive feature
   importance.
4. **Implement experiment and model
   tracking**. Maintain comprehensive records of data
   provenance and model versions to trace model skew back to
   potentially compromised data sources. Before retraining
   models with new data, implement validation processes to
   identify and remove adversarial examples. Use
   [Amazon SageMaker AI MLflow](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md") to document relationships between
   datasets, algorithms, and model artifacts throughout the ML
   lifecycle.
5. **Use secure inference API
   endpoints**. Host models behind properly secured
   API endpoints that implement authentication, authorization,
   and input validation. Configure
   [Amazon SageMaker AI endpoints](../../../sagemaker/latest/dg/realtime-endpoints-manage.md "../../../sagemaker/latest/dg/realtime-endpoints-manage.md") with appropriate security
   controls including VPC isolation,
   [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") roles with least privilege, and encryption for
   data in transit and at rest. Implement rate limiting and
   request validation to block abuse of model APIs. Monitor API
   usage patterns to detect potential exploitation attempts.
6. **Implement continuous model
   monitoring**. Set up
   [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/") to track data and concept
   drift that may indicate adversarial manipulation. Configure
   automatic alerts when inference data patterns deviate from
   training baselines. Periodically reevaluate model robustness
   as new threat techniques emerge in the security landscape.
7. **Establish incident response
   procedures**. Develop clear protocols for
   responding to detected adversarial threats against your ML
   systems. Define procedures for model rollback, data
   quarantine, and forensic analysis when suspicious activities
   are identified. Document lessons learned from security
   incidents to continuously improve protection strategies.
8. **Apply input validation
   guardrails**. For AI models, implement robust input
   validation and filtering mechanisms to block injection
   exploits. Implement custom guardrails to protect against
   harmful inputs that may manipulate model behavior. Monitor
   input patterns and responses to detect attempts to bypass
   security controls.

## Resources

**Related documents:**

- [Deep
  ensembles](../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/deep-ensembles.md "../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/deep-ensembles.md")
- [Empirical
  demonstration of deterministic overconfidence](../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/app-b.md "../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/app-b.md")
- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Accelerate
  generative AI development using managed MLflow on Amazon SageMaker AI](../../../sagemaker/latest/dg/mlflow.md "../../../sagemaker/latest/dg/mlflow.md")
- [Security
  and compliance](../../../whitepapers/latest/ml-best-practices-public-sector-organizations/security-and-compliance.md "../../../whitepapers/latest/ml-best-practices-public-sector-organizations/security-and-compliance.md")
- [7
  ways to improve security of your machine learning
  workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")
- [Run
  ensemble ML models on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/part-7-model-hosting-patterns-in-amazon-sagemaker-run-ensemble-ml-models-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/part-7-model-hosting-patterns-in-amazon-sagemaker-run-ensemble-ml-models-on-amazon-sagemaker/")
- [Securing
  Amazon SageMaker AI Studio connectivity using a private
  VPC](https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/ "https://aws.amazon.com/blogs/machine-learning/securing-amazon-sagemaker-studio-connectivity-using-a-private-vpc/")
