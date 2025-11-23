# RAISP02-BP03 Mitigate unwanted bias directly in the core AI

system design

Consider incorporating fairness mitigations such as sampling and
optimization methods during training, alignment and calibration
techniques that actively mitigate biased system responses, and
post-processing strategies that review and adjust outputs before
they reach users. The specific fairness strategies you use should
directly support the fairness goals in your release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Use sampling-based methods during training to improve model
   performance on underrepresented groups. Apply techniques like
   weighted sampling to give more importance to underrepresented
   examples, oversampling to create more training instances from
   minority groups, or stratified sampling to achieve balanced
   representation. Consider error-based weighted sampling where
   you identify groups that experience higher error rates on a
   validation set and sample datapoints from those groups at
   higher rates during training. These methods assist your model
   learn better patterns for each group instead of just the
   majority.
2. Consider using fairness metrics within the model loss function
   to guide model training to penalize unfair outputs.
3. Consider if demographic features or proxy features factor
   significantly into the model predictions by analyzing feature
   attributions for indications of a biased model. Consider using
   Amazon SageMaker AI Clarify for feature attributions and bias
   detection.

## Resources

**Related documents:**

- [Amazon
  AI Fairness and Explainability Whitepaper](https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf "https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf")
- [Fairness,
  model explainability and bias detection with SageMaker AI
  Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [Transform
  responsible AI from theory into practice](https://aws.amazon.com/ai/responsible-ai/ "https://aws.amazon.com/ai/responsible-ai/")
- [Automate
  model retraining with Amazon SageMaker AI Pipelines when drift is
  detected](https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/ "https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/")
- [Accenture
  Enterprise AI – Scaling Machine Learning and Deep Learning
  Models](../../../whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/monitoring-for-performance-and-bias.md "../../../whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/monitoring-for-performance-and-bias.md")
- [Amazon SageMaker AI AI: Prepare ML Data with Amazon SageMaker AI Data
  Wrangler](../../../sagemaker/latest/dg/data-wrangler.md "../../../sagemaker/latest/dg/data-wrangler.md")
- [NIST
  AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework "https://www.nist.gov/itl/ai-risk-management-framework")
- [ISO/IEC
  42001:2023 Information technology — Artificial intelligence —
  Management system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
- [Fairlearn](https://fairlearn.org/ "https://fairlearn.org/")
