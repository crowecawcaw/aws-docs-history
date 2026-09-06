

# SageMaker Clarify explainability with SageMaker AI Autopilot
<a name="autopilot-explainability"></a>

Autopilot uses tools provided by Amazon SageMaker Clarify to help provide insights into how machine learning (ML) models make predictions. These tools can help ML engineers, product managers, and other internal stakeholders understand model characteristics. To trust and interpret decisions made on model predictions, both consumers and regulators rely on transparency in machine learning in order.

The Autopilot explanatory functionality uses a model-agnostic feature attribution approach. This approach determines the contribution of individual features or inputs to the model's output, providing insights into the relevance of different features. You can use it to understand why a model made a prediction after training, or use it to provide per-instance explanation during inference. The implementation includes a scalable implementation of [SHAP](https://papers.nips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf) (Shapley Additive Explanations). This implementation is based on the concept of a Shapley value from cooperative game theory, which assigns each feature an importance value for a particular prediction.

You can use SHAP explanations for the following: auditing and meeting regulatory requirements, building trust in the model, supporting human decision-making, or debugging and improving model performance.

For additional information on Shapley values and baselines, see [SHAP Baselines for Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.html).

For a guide to the Amazon SageMaker Clarify documentation, see [Guide to the SageMaker Clarify Documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html#clarify-fairness-and-explainability-toc).