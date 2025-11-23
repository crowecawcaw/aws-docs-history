# MLOPS01-BP03 Monitor model adherence to business

requirements

Machine learning models degrade over time due to changes in the real
world, such as _data drift_ and _concept
drift_. If not monitored, these changes could lead to
models becoming inaccurate or even obsolete over time. It's
important to have a periodic monitoring process in place to make
sure that your ML models continue to comply to your business
requirements and that deviations are captured and acted upon
promptly.

**Desired outcome:** You implement a
robust model monitoring framework that continuously evaluates model
performance against your business requirements. This enables early
detection of model drift, keeping your ML models accurate and
effective over time. You establish clear metrics tied to business
outcomes and have automated processes to respond to detected drifts,
minimizing potential negative impacts.

**Common anti-patterns:**

- Implementing monitoring without clear metrics tied to business
  requirements.
- Focusing only on technical metrics while ignoring business
  impact metrics.
- Lacking a clear action plan for when drift is detected.
- Monitoring models infrequently or irregularly.
- Not establishing thresholds for acceptable levels of drift.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation.
- Maintained alignment between model outputs and business goals.
- Reduced risk of financial or operational impact from degraded
  models.
- Increased stakeholder confidence in deployed ML systems.
- Improved model lifecycle management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model monitoring is a critical aspect of maintaining ML systems
that continue to deliver business value over time. As real-world
conditions evolve, your models can experience both data drift
(changes in the distribution of input data) and concept drift
(changes in the relationship between inputs and outputs). These
drifts can significantly impact model accuracy and reliability.

To effectively monitor model adherence to business requirements,
establish a comprehensive monitoring strategy that bridges
technical metrics with business outcomes. This involves defining
clear thresholds for acceptable performance, implementing
automated monitoring solutions, and creating response plans for
different drift scenarios.

Amazon SageMaker AI Model Monitor provides capabilities to
automatically monitor models in production and detect deviations
from the baseline. By using these capabilities, you can
proactively address potential issues before they impact your
business operations.

### Implementation steps

1. **Define relevant metrics aligned with
   business objectives.** Begin by clearly
   establishing the metrics that are most relevant to your
   business outcomes. Include both technical metrics (like
   accuracy, precision, and recall) and business metrics (like
   revenue impact and customer satisfaction). Make sure these
   metrics directly relate to the business requirements the
   model is expected to fulfill.
2. **Establish baseline performance and
   thresholds.** Create a performance baseline using
   your validation dataset. Using Amazon SageMaker AI Model
   Monitor, you can automatically generate statistics and
   constraints from your baseline data that define normal
   behavior. Set appropriate thresholds that will alert when
   model performance deviates beyond acceptable limits.
3. **Implement automated data quality
   monitoring.** Configure SageMaker AI Model Monitor to
   regularly check the quality of input data against the
   baseline. This can detect data drift that could affect model
   performance. Monitor features for statistical changes in
   distributions, missing values, or other quality issues.
4. **Configure model quality
   monitoring.** Set up monitoring for model outputs
   and quality metrics. SageMaker AI Model Monitor can track
   prediction distributions and performance metrics over time,
   alerting you when they deviate from expected patterns.
5. **Set up bias drift
   detection.** Use SageMaker AI Clarify integration with
   Model Monitor to detect changes in bias metrics over time.
   This keeps your model fair and unbiased as production data
   evolves.
6. **Create visualization
   dashboards.** Implement dashboards using Amazon CloudWatch, Amazon Managed Grafana, or use
   [Quick Suite with GenBI capabilities](https://aws.amazon.com/quicksight/generative-bi/ "https://aws.amazon.com/quicksight/generative-bi/") to automatically
   generate monitoring dashboards. These dashboards should
   present both technical and business metrics in an
   understandable format for stakeholders.
7. **Develop response protocols for drift
   detection.** Create clear action plans for
   different types and severities of detected drift. These
   might include automated retraining pipelines, manual
   reviews, or temporary fallback strategies depending on the
   scenario.
8. **Implement alert
   mechanisms.** Configure alerts using Amazon CloudWatch to notify appropriate team members when metrics
   exceed thresholds. Check that your alerts provide actionable
   information about the nature and potential impact of the
   drift.
9. **Establish regular review
   processes.** Schedule periodic reviews of
   monitoring results even when no alerts go off. This can
   identify gradual drifts that might not immediately alert but
   could impact performance over time.
10. **Document monitoring systems and
    processes.** Maintain comprehensive documentation
    of your monitoring setup, including metrics definitions,
    thresholds, alert configurations, and response protocols to
    preserve organizational knowledge.
11. **Leverage generative AI for root
    cause analysis.** Use generative AI capabilities to
    analyze complex patterns in your monitoring data and provide
    human-readable explanations of potential drift causes. Tools
    like
    [Amazon
    Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") can interpret changes in
    model behavior and suggest remediation approaches.

## Resources

**Related documents:**

- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Schema
  for Violations (constraint_violations.json file)](../../../sagemaker/latest/dg/model-monitor-interpreting-violations.md "../../../sagemaker/latest/dg/model-monitor-interpreting-violations.md")
- [Amazon SageMaker AI metrics in Amazon CloudWatch](../../../sagemaker/latest/dg/monitoring-cloudwatch.md "../../../sagemaker/latest/dg/monitoring-cloudwatch.md")
- [What
  is Amazon CloudWatch?](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/")
- [Amazon SageMaker AI ML Governance](https://aws.amazon.com/sagemaker/ml-governance/ "https://aws.amazon.com/sagemaker/ml-governance/")
