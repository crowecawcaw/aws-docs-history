Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Quotas

Your AWS account has default quotas, formerly referred to as _limits_, for each Amazon Web Service. Unless otherwise noted, each quota is Region-specific.
You can request a quota increase for all adjustable quotas mentioned in the tables below. For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md")

The following tables outline Amazon Fraud Detector quotas by component.

## Amazon Fraud Detector models

| Quota name                                       | Default quota | Adjustable |
| ------------------------------------------------ | ------------- | ---------- | ----------------------------------------------------------------- |
| Training data size                               | 5 GB          | No         |
| Models per account                               | 50            | No         |
| Versions per model                               | 200           | No         |
| Deployed model versions per account              | 5             | No         |
| Concurrent training jobs per account             | 3             | No         |
| Concurrent training jobs per model               | 1             | No         | ## Amazon Fraud Detector detectors / variables / outcomes / rules |
| Quota name                                       | Default quota | Adjustable |
| ---                                              | ---           | ---        |
| Variables per account                            | 5000          | No         |
| Rules per account                                | 5000          | No         |
| Lists per rule                                   | 3             | No         |
| Outcomes per account                             | 5000          | No         |
| Detectors per account                            | 100           | No         |
| Lists per detector                               | 30            | No         |
| Draft versions per detector                      | 100           | No         |
| Models per detector version                      | 10            | No         |
| Labels per account                               | 100           | No         |
| Event types per account                          | 100           | No         |
| Entity types per account                         | 100           | No         | ## Amazon Fraud Detector API                                      |
| Quota name                                       | Default quota | Adjustable |
| ---                                              | ---           | ---        |
| GetEventPrediction API calls per second          | 200 TPS       | Yes        |
| Size of payload per GetEventPrediction API call  | 256 KB        | No         |
| Number of inputs per GetEventPrediction API call | 5000          | No         |
