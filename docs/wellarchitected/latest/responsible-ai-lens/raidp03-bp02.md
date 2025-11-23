# RAIDP03-BP02 Minimize unwanted bias in your datasets

When assessing the quality of a dataset, determine whether it
appropriately represents the demographics of the expected range of
system users. Consider datasets that include self-reported
demographic labels. Calculate if datasets contain sufficient
representation across demographic groups to enable statistically
valid fairness assessments or fairness outcomes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Analyze the demographic composition of your datasets to
   identify which groups may be over- or under-represented for
   your use case.
2. Consider using self-reported demographic labels. For example,
   consider using survey responses or user-provided information
   rather than algorithmic or human predictions of demographic
   information.
3. Calculate statistical power for each demographic group in your
   evaluation datasets by working backwards from your release
   criteria. For instance, determine whether you have enough
   examples per group to answer each release criteria question
   with the required statistical confidence.
4. Address representation gaps by collecting additional data from
   underrepresented groups or using techniques like stratified
   sampling, where a population is divided into subgroups, or
   "strata," based on shared characteristics, and then
   a random sample is taken from each subgroup to verify
   representation.
5. Validate that your bias mitigation efforts don't introduce new
   fairness concerns. For example, check if balancing one
   demographic dimension inadvertently creates imbalances across
   intersectional groups.

## Resources

**Related documents:**

- [Metrics
  for Dataset Demographic Bias: A Case Study on Facial
  Expression Recognition](https://arxiv.org/html/2303.15889v2 "https://arxiv.org/html/2303.15889v2")
- [Responsible
  AI question bank: A comprehensive tool for AI risk
  assessment](https://arxiv.org/pdf/2408.11820 "https://arxiv.org/pdf/2408.11820")
- [A Review
  of Machine Learning Techniques in Imbalanced Data and Future
  Trends](https://arxiv.org/pdf/2310.07917 "https://arxiv.org/pdf/2310.07917")
- [A survey
  on learning from imbalanced data streams: taxonomy, challenges, empirical study, and reproducible experimental
  framework](https://arxiv.org/pdf/2204.03719 "https://arxiv.org/pdf/2204.03719")
- [A Survey
  on Small Sample Imbalance Problem: Metrics, Feature Analysis,
  and Solutions](https://arxiv.org/pdf/2504.14800 "https://arxiv.org/pdf/2504.14800")
- [Amazon SageMaker AI Clarify: Machine Learning Bias Detection and
  Explainability in the Cloud](https://arxiv.org/pdf/2109.03285 "https://arxiv.org/pdf/2109.03285")
- [Fairness,
  model explainability and bias detection with SageMaker AI
  Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")
- [Data
  Curation Practices to Minimize Bias in Medical AI.](https://towardsdatascience.com/data-curation-practices-to-minimize-bias-in-medical-ai-379bf6983de2/ "https://towardsdatascience.com/data-curation-practices-to-minimize-bias-in-medical-ai-379bf6983de2/")
- [DSAP:
  Analyzing bias through demographic comparison of
  datasets](https://www.sciencedirect.com/science/article/pii/S1566253524005384 "https://www.sciencedirect.com/science/article/pii/S1566253524005384")
- [Mitigating
  Bias in Training Data with Synthetic Data](https://keymakr.com/blog/mitigating-bias-in-training-data-with-synthetic-data/ "https://keymakr.com/blog/mitigating-bias-in-training-data-with-synthetic-data/")
- [A
  framework to mitigate bias and improve outcomes in the new age
  of AI](https://aws.amazon.com/blogs/publicsector/framework-mitigate-bias-improve-outcomes-new-age-ai/ "https://aws.amazon.com/blogs/publicsector/framework-mitigate-bias-improve-outcomes-new-age-ai/")
- [Balance
  your data for machine learning with Amazon SageMaker AI Data
  Wrangler](https://aws.amazon.com/blogs/machine-learning/balance-your-data-for-machine-learning-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/balance-your-data-for-machine-learning-with-amazon-sagemaker-data-wrangler/")
- [How
  Clarify helps machine learning developers detect unintended
  bias](https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias "https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias")
- [Generate
  Reports for Bias in Pre-training Data in SageMaker AI
  Studio](../../../sagemaker/latest/dg/clarify-data-bias-reports-ui.md "../../../sagemaker/latest/dg/clarify-data-bias-reports-ui.md")
- [Get
  Insights On Data and Data Quality](../../../sagemaker/latest/dg/data-wrangler-data-insights.md "../../../sagemaker/latest/dg/data-wrangler-data-insights.md")
- [Build
  an enterprise synthetic data strategy using Amazon
  Bedrock](https://aws.amazon.com/blogs/machine-learning/build-an-enterprise-synthetic-data-strategy-using-amazon-bedrock/ "https://aws.amazon.com/blogs/machine-learning/build-an-enterprise-synthetic-data-strategy-using-amazon-bedrock/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.2 Data for development and enhancement
  of AI system
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems
