# MLSEC-11: Protect against adversarial and malicious activities

Add protection inside and outside of the deployed code to detect
malicious inputs that might result in incorrect predictions.
Automatically detect unauthorized changes by examining the
inputs in detail. Repair and validate the inputs before they are
added back to the pool.

## Implementation plan

- **Evaluate the robustness of the
  algorithm** - Evaluate your use case and
  determine bad predictions or classifications. Use
  sensitivity analysis to evaluate the robustness of the
  algorithm against increasingly perturbed inputs to
  understand susceptibility to manipulated inputs.
- **Build for robustness from the
  start** - Select diverse features to improve the
  algorithm’s ability to handle outliers. Consider using
  models in an ensemble for increased diversity in decisions
  and for robustness around decision points.
- **Identify repeats** -
  Detect similar repeated inputs to the model to indicate
  possible threats to the decision boundaries using Amazon SageMaker AI Model Monitor to run a SageMaker AI processing job
  on a periodic interval to analyze the inference data. This
  can take the form of model brute forcing, where threats
  iterate only a limited set of variables to determine what
  influences decision points and derive feature importance.
- **Lineage tracking** - If
  retraining on untrusted or unvalidated inputs, make sure
  any model skew is traced back to the data and pruned
  before retraining a replacement model.
- **Use secure inference API
  endpoints** - Host the model so that a consumer
  of the model can perform inference against it securely.
  Permit consumers using the API to define the relationship,
  restrict access to the base model, and provide monitoring
  of model interactions.

## Documents

- [Deep
  ensembles](../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/deep-ensembles.md "../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/deep-ensembles.md")
- [Empirical
  demonstration of deterministic overconfidence](../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/app-b.md "../../../prescriptive-guidance/latest/ml-quantifying-uncertainty/app-b.md")
- [Making
  Machine Learning Robust Against Adversarial Inputs](https://cacm.acm.org/magazines/2018/7/229030-making-machine-learning-robust-against-adversarial-inputs/fulltext "https://cacm.acm.org/magazines/2018/7/229030-making-machine-learning-robust-against-adversarial-inputs/fulltext")

## Blogs

- [7
  ways to improve security of your machine learning
  workflows](https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/ "https://aws.amazon.com/blogs/security/7-ways-to-improve-security-of-your-machine-learning-workflows/")
- [Run
  ensemble ML models on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/part-7-model-hosting-patterns-in-amazon-sagemaker-run-ensemble-ml-models-on-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/part-7-model-hosting-patterns-in-amazon-sagemaker-run-ensemble-ml-models-on-amazon-sagemaker/")

## Videos

- [Security
  and Privacy of Machine Learning](https://www.youtube.com/watch?v=Af9WM5WUChg "https://www.youtube.com/watch?v=Af9WM5WUChg")

## Examples

- [Evasion
  Attacks against Banking Fraud Detection Systems](https://www.usenix.org/conference/raid2020/presentation/carminati "https://www.usenix.org/conference/raid2020/presentation/carminati")
- [Adversarial
  Robustness Libraries](https://github.com/EthicalML/awesome-production-machine-learning#adversarial-robustness-libraries "https://github.com/EthicalML/awesome-production-machine-learning#adversarial-robustness-libraries")
- [SecML:
  A library for Secure and Explainable Machine
  Learning](https://secml.readthedocs.io/en/latest/ "https://secml.readthedocs.io/en/latest/")
