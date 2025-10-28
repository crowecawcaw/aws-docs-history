# Receiving model logs and

metrics

To receive logs and metrics from custom model training or inference, members must
have [created
an ML Configuration](create-custom-ml-collaboration.md "create-custom-ml-collaboration.md") with a valid role that provides the necessary
CloudWatch permissions (see [Create a service role for custom ML modeling - ML
Configuration](ml-roles.md#ml-roles-custom-configure "ml-roles.md#ml-roles-custom-configure")).

**System metric**

System metrics for both training and inference, such as CPU and memory
utilization, are published to all members in the collaboration with valid ML
Configurations. These metrics can be viewed as the job progresses via CloudWatch
Metrics in the `/aws/cleanroomsml/TrainedModels` or
`/aws/cleanroomsml/TrainedModelInferenceJobs` namespaces,
respectively.

**Model logs**

Access to the model logs is provided by the privacy configuration policy of each
configured model algorithm. The model author sets the privacy configuration policy
when associating a configured model algorithm (either via the console or the
`CreateConfiguredModelAlgorithmAssociation` API) to a collaboration.
Setting the privacy configuration policy controls which members can receive the
model logs.

Additionally, the model author can set a filter pattern in the privacy
configuration policy to filter log events. All logs that a model container sends to
`stdout` or `stderr` and that match the filter pattern (if
set), are sent to Amazon CloudWatch Logs. Model logs are available in CloudWatch log
groups `/aws/cleanroomsml/TrainedModels` or
`/aws/cleanroomsml/TrainedModelInferenceJobs`, respectively.

**Custom defined metrics**

When you configure a model algorithm (either via the console or the
`CreateConfiguredModelAlgorithm` API), the model author can provide
specific metric names and regex statements to search for in the output logs. These
can be viewed as the job progresses via CloudWatch Metrics in the
`/aws/cleanroomsml/TrainedModels` namespace. When associating a
configured model algorithm, the model author can set an optional noise level in the
metrics privacy configuration to avoid outputting raw data while still providing
visibility into custom metric trends. If a noise level is set, the metrics are
published at the end of the job rather than in real time.
