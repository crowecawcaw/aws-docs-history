# Feature Processor restrictions, limits,

and quotas

Amazon SageMaker Feature Store Feature Processing relies on SageMaker AI machine learning (ML) lineage tracking. The Feature Store
Feature Processor uses lineage contexts to represent and track Feature Processing Pipelines and
Pipeline versions. Each Feature Store Feature Processor consumes at least two lineage contexts (one for the
Feature Processing Pipeline and another for the version). If the input or output data source of a
Feature Processing Pipeline changes, an additional lineage context is created. You can update SageMaker AI
ML lineage limits by reaching out to AWS support for a limit increase. Default limits for
resources used by Feature Store Feature Processor are as follows. For information on SageMaker AI ML lineage
tracking, see [Amazon SageMaker ML Lineage Tracking](lineage-tracking.md "lineage-tracking.md").

For more information on SageMaker AI quotas, see [Amazon SageMaker AI endpoints and quotas](../../../general/latest/gr/sagemaker.md "../../../general/latest/gr/sagemaker.md").

Lineage limits per Region

- Contexts – 500 (soft limit)
- Artifacts – 6,000 (soft limit)
- Associations – 6,000 (soft limit)
  Training Limits per Region

- Longest run time for a training job – 432,000 seconds
- Maximum number of instances per training job – 20
- The maximum number of `CreateTrainingJob` requests that you can make, per
  second, in this account in the current Region – 1 TPS
- Keep alive period for cluster reuse – 3,600 seconds
  Maximum number of Pipelines and concurrent pipeline executions per Region

- Maximum number of pipelines allowed per account – 500
- Maximum number of concurrent pipeline executions allowed per account – 20
- Time at which pipeline executions time out – 672 hours
