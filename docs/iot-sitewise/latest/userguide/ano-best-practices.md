# Best practices

## Understand the minimum date range

Use a minimum of 14 days for training data duration. However, we recommend that you
include a longer period of data in many cases.

Ensure that your training dataset spans a timeframe during which the asset operated
under all of its normal operating modes. This approach helps AWS IoT SiteWise accurately distinguish
between expected behavior and true anomalies.

If your training data doesn't represent all typical operating modes, AWS IoT SiteWise might
incorrectly flag unfamiliar but normal patterns as anomalies, which increases false
positives.

## Sampling for high-frequency data and

consistency between training and inference

If your sensors generate data at a frequency higher than 1 Hz (more than one reading per
second), apply sampling during training. Sampling reduces data volume while preserving
essential trends, which enables efficient processing and improves model generalization by
minimizing the impact of noise or transient fluctuations.

AWS IoT SiteWise native anomaly detection currently doesn't support data ingested at rates below 1 Hz. Verify that
your data meets this minimum frequency requirement before you configure anomaly
detection.

Additionally, AWS IoT SiteWise uses the sampling rate that you configure during training for
inference as well. To maintain consistency and ensure accurate anomaly detection results,
choose a sampling rate that aligns with both your operational needs and the behavior of your
sensor data.

Find more details about how to set sampling rate at [Sample rate configuration](adv-training-configs.md#sample-rate-configuration "adv-training-configs.md#sample-rate-configuration").

## Labeling recommendations

Accurate and consistent labeling of anomalies is essential for effective model
evaluation and continuous improvement. Consider the following best practices when you label
anomalies:

- **Consolidate related anomalies:** Don't label closely
  occurring anomalies as separate events, if they're part of the same underlying issue.
  For example, if anomalies occur within 1–2 days of each other and the same root cause
  drives them, treat them as a single anomaly window. This approach helps the model better
  learn the pattern of abnormal behavior, and reduces noise in your evaluation
  data.
- **Label anomaly windows, not just points:** Instead of
  marking individual data points as anomalous, label the entire window that reflects
  abnormal behavior from deviation onset to recovery. This approach provides clearer
  boundaries and improves model alignment with actual operational issues.
- **Exclude uncertain periods:** If you're unsure whether
  a period is anomalous, leave it unlabeled. Ambiguous labels can confuse the model and
  degrade its accuracy over time.

Find more details about how to add labels at [Label your data](adv-training-configs.md#ano-labeling-data "adv-training-configs.md#ano-labeling-data").
