# MLCOST-03: Identify if machine learning is the right solution

Evaluate if there are alternatives, such as a simple rule-based
approach, that could do a better job than ML. Weigh the cost of
adopting ML against the opportunity cost of not leaning on ML
transformation. Specialized resources, such as data scientist
time or model time-to-market, might be the most expensive and
constrained resources. The most cost-effective hardware choice
might not be cost optimized if it constrains experimentation and
development speed.

## Implementation plan

- Start simple:
  - Articulate your problem.
  - Identify your data sources.
  - Think about cost involved in: 
    - Designing or preparing your data for the model.
    - Data storage cost for ML.
    - Model training cost depending on the hardware.
      choice
    - Data labeling cost, if required.
    - Potential bias resulting in iterative model
      re-training leading to higher cost.
    - Potential cost of hosting the ML model.
    - Model maintenance costs.

  - Consider these data points to weigh the cost of
    adopting ML against the opportunity cost of not
    leaning on ML transformation.

- Use Amazon SageMaker AI Autopilot and SageMaker AI Clarify to
  validate that ML is the right solution.
  - **Baseline the
    solution** by reviewing how the problem is
    solved today. If a rules-based solution is available,
    then use it as a baseline. Selecting a simple ML model
    for baselining can also be done using JumpStart or AWS Marketplace. AWS also provides many pre-built
    solutions with one-click deploy for most common
    business use cases.
  - **Build a machine learning
    model** using
    [SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md")
    or
    [SageMaker AI
    Autopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development.md "../../../sagemaker/latest/dg/autopilot-automate-model-development.md") and compare the metrics of this
    solution against the baseline.
  - **Use**
    [SageMaker AI
    Clarify](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md") to explain the model that you have
    built using SageMaker AI or Autopilot.
  - **Identify** if the ML
    model is performing better than your existing solution
    or a rules-based approach before investing on an
    ML-based solution.

## Documents

- [Amazon SageMaker AI](../../../sagemaker/latest/dg/whatis.md "../../../sagemaker/latest/dg/whatis.md")
- [Amazon SageMaker AI Autopilot](../../../sagemaker/latest/dg/autopilot-automate-model-development.md "../../../sagemaker/latest/dg/autopilot-automate-model-development.md")
- [Amazon SageMaker AI Jumpstart](https://aws.amazon.com/sagemaker/jumpstart/ "https://aws.amazon.com/sagemaker/jumpstart/")
- [Amazon SageMaker AI Clarify](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md")
- [Machine
  Learning solutions in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning "https://aws.amazon.com/marketplace/solutions/machine-learning")
