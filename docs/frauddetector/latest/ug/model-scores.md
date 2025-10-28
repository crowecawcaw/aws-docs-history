Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Model scores

Amazon Fraud Detector generates model scores differently for different model types.

For **Account Takeover Insights (ATI)** models, Amazon Fraud Detector uses only aggregated value (a value calculated by combining a set of raw variables) to generate the model score. A score of -1 is generated for the first event of a new entity, indicating an _unknown risk_.
This is because for a new entity, the values used for calculating the aggregate will be zero or null. Account Takeeover Insights (ATI) model generates model scores between 0 and 1000 for all subsequent events for the same entity and for existing entities, where 0 indicates _low fraud risk_ and 1000 indicates _high fraud risk_.
For ATI models, the model scores are directly related to the challenge rate (CR). For example, a score of 500 corresponds to an estimated 5% challenge rate whereas a score of 900 corresponds to an estimated 0.1% challenge rate.

For **Online Fraud Insights (OFI)** and **Transaction Fraud Insights (TFI)** models, Amazon Fraud Detector uses both aggregated value (a value calculated by combining a set of raw variables) and raw value (the value provided for the variable) to generate the model scores.
The model scores can be between 0 and 1000, where 0 indicates _low fraud risk_ and 1000 indicates _high fraud risk_. For the OFI and TFI models, the model scores are directly related to the false positive rate (FPR). For example, a score of 600 corresponds to an estimated 10% false positive
rate whereas a score of 900 corresponds to an estimated 2% false positive rate. The following table provides details of how certain model scores correlate to estimated false positive rates.

| Model score | Estimated FPR |
| ----------- | ------------- |
| 975         | 0.50%         |
| 950         | 1%            |
| 900         | 2%            |
| 860         | 3%            |
| 775         | 5%            |
| 700         | 7%            |
| 600         | 10%           |
