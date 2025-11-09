# Questions

| HCL_OE4: How do you track model<br>revisions and ensure traceability of your ML<br>artifacts? |
| --------------------------------------------------------------------------------------------- |
|                                                                                               |

Employ version control for source code, data, and ML artifacts
to ensure traceability and reliability of production ML
deployments. Version control and traceability may be required by
applicable regulatory frameworks, if for example models are
deployed in support of medical devices.

| HCL_SEC16. How does your organization<br>review, accept, and manage the licenses of open-source<br>software dependencies? |
| ------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                           |

Data science in healthcare often depends on open-source
libraries for data processing, model development, training, and
hosting. Establish a process to review the privacy and license
agreements for all software and ML libraries needed throughout
the ML lifecycle. Verify that these agreements comply with your
organization’s legal, privacy, and security requirements.

| HCL_SEC17. Does your organization<br>deidentify heath data used for machine learning, or otherwise<br>limit access to sensitive, identifiable health<br>data? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                               |

Many ML workflows do not require identified health data.
Applying ML to deidentified data is one way to develop
AI-powered applications without compromising privacy or data
security. Cloud services like the
[Amazon Comprehend Medical DetectPHI API](../../../comprehend-medical/latest/dev/textanalysis-phi.md "../../../comprehend-medical/latest/dev/textanalysis-phi.md") can streamline
generating deidentified datasets.

| HCL_REL4: How does your organization<br>identify and limit biases in training data and statistical<br>models? |
| ------------------------------------------------------------------------------------------------------------- |
|                                                                                                               |

Statistical models trained on real-world health data are
susceptible to biases. Health data may inadvertently be
collected from populations of individuals with similar
characteristics, such as median household income, social
determinants of health, and access to care. Care setting and
health insurance coverage may also impart biases. For example,
treatment cohorts may exhibit higher household income because
such individuals may have greater access to advanced care.

Trained models may be misleading if biases are not quantified
and mitigated. Also, models may be inaccurate when trained on
biased data and applied to settings with different
distributions. Examine data distributions and
[perform
analyses](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") to quantify and mitigate biases before training
models.

| HCL_PERF10: What processes do you use<br>to monitor model performance after deployment and protect<br>against drift? |
| -------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                      |

Health data is often complex, and subject to temporal variations
in quality and concept expression. Model performance may degrade
over time due to data quality, model quality, and concept drift.
Create a baseline for data quality, and
[automate
monitoring performance](../../../sagemaker/latest/dg/model-monitor-data-quality.md "../../../sagemaker/latest/dg/model-monitor-data-quality.md") in production. Automate alerts for
changes in data quality or distributions, such as age deciles
and prevalence of relevant chronic diseases.
[SageMaker AI
Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/") provides an end-to-end framework model
monitoring and lifecycle management.
