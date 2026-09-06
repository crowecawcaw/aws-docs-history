

# Metric name mapping: legacy to OTel
<a name="monitoring-detailed-observability-metric-mapping"></a>

For metrics that exist in both CloudWatch classic and OpenTelemetry, the underlying data is the same but the naming conventions differ. In CloudWatch classic, a single metric name such as `Invocations` is distinguished by its dimension set (for example, EndpointName alone versus EndpointName plus InstanceId). In OpenTelemetry, each granularity level has its own metric name (for example, `Invocations` versus `InvocationsByInstanceId`).

If you have existing alarms, dashboards, or queries built on CloudWatch classic metrics, use this reference to find the equivalent OpenTelemetry metric names when migrating to detailed observability. While metric names differ, the corresponding OpenTelemetry metrics carry the same labels.

## Concurrent requests metrics mapping
<a name="detailed-observability-mapping-concurrent"></a>


**Concurrent requests metrics mapping**  

| \# | CloudWatch classic metric | CloudWatch classic dimensions | OpenTelemetry metric | 
| --- | --- | --- | --- | 
| 1 | ConcurrentRequestsPerCopy | InferenceComponentName | ConcurrentRequestsPerCopy | 
| 2 | ConcurrentRequestsPerCopy | InferenceComponentName, Region, AvailabilityZone, InstanceType | ConcurrentRequestsPerCopyByAzByInstanceType | 
| 3 | ConcurrentRequestsPerModel | EndpointName, VariantName | ConcurrentRequestsPerModel | 
| 4 | ConcurrentRequestsPerModel | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | ConcurrentRequestsPerModelByAzByInstanceType | 

## Invocation metrics mapping
<a name="detailed-observability-mapping-invocation"></a>


**Invocation metrics mapping**  

| \# | CloudWatch classic metric | CloudWatch classic dimensions | OpenTelemetry metric | 
| --- | --- | --- | --- | 
| 5 | Invocations | EndpointName, VariantName | Invocations | 
| 6 | Invocations | EndpointName, VariantName, InstanceId | InvocationsByInstanceId | 
| 7 | Invocations | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | InvocationsByAzByInstanceType | 
| 8 | Invocations (IC) | InferenceComponentName | InvocationsForIc | 
| 9 | Invocations (IC) | InferenceComponentName, Region, AvailabilityZone, InstanceType | InvocationsForIcByAzByInstanceType | 
| 10 | Invocations (IC) | EndpointName, VariantName, InferenceComponentName, InstanceId, ContainerId | InvocationsForIcByInstanceIdByContainerId | 
| 11 | InvocationsPerCopy | InferenceComponentName | InvocationsPerCopy | 
| 12 | InvocationsPerCopy | InferenceComponentName, Region, AvailabilityZone, InstanceType | InvocationsPerCopyByAzByInstanceType | 
| 13 | InvocationsPerInstance | EndpointName, VariantName | InvocationsPerInstance | 
| 14 | InvocationsPerInstance | EndpointName, VariantName, InstanceId | InvocationsPerInstanceByInstanceId | 
| 15 | InvocationsPerInstance | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | InvocationsPerInstance​ByAzByInstanceType | 

## Error metrics mapping
<a name="detailed-observability-mapping-errors"></a>


**Error metrics mapping**  

| \# | CloudWatch classic metric | CloudWatch classic dimensions | OpenTelemetry metric | 
| --- | --- | --- | --- | 
| 16 | Invocation4XXErrors | EndpointName, VariantName | Invocation4XXErrors | 
| 17 | Invocation4XXErrors | EndpointName, VariantName, InstanceId | Invocation4XXErrorsByInstanceId | 
| 18 | Invocation4XXErrors | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | Invocation4XXErrorsByAzByInstanceType | 
| 19 | Invocation4XXErrors (IC) | InferenceComponentName | Invocation4XXErrorsForIc | 
| 20 | Invocation4XXErrors (IC) | InferenceComponentName, Region, AvailabilityZone, InstanceType | Invocation4XXErrorsForIcByAzByInstanceType | 
| 21 | Invocation4XXErrors (IC) | EndpointName, VariantName, InferenceComponentName, InstanceId, ContainerId | Invocation4XXErrorsForIcByInstanceIdByContainerId | 
| 22 | Invocation5XXErrors | EndpointName, VariantName | Invocation5XXErrors | 
| 23 | Invocation5XXErrors | EndpointName, VariantName, InstanceId | Invocation5XXErrorsByInstanceId | 
| 24 | Invocation5XXErrors | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | Invocation5XXErrorsByAzByInstanceType | 
| 25 | Invocation5XXErrors (IC) | InferenceComponentName | Invocation5XXErrorsForIc | 
| 26 | Invocation5XXErrors (IC) | InferenceComponentName, Region, AvailabilityZone, InstanceType | Invocation5XXErrorsForIcByAzByInstanceType | 
| 27 | Invocation5XXErrors (IC) | EndpointName, VariantName, InferenceComponentName, InstanceId, ContainerId | Invocation5XXErrorsForIcByInstanceIdByContainerId | 
| 28 | InvocationModelErrors | EndpointName, VariantName | InvocationModelErrors | 
| 29 | InvocationModelErrors | EndpointName, VariantName, InstanceId | InvocationModelErrorsByInstanceId | 
| 30 | InvocationModelErrors | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | InvocationModelErrorsByAzByInstanceType | 
| 31 | InvocationModelErrors (IC) | InferenceComponentName | InvocationModelErrorsForIc | 
| 32 | InvocationModelErrors (IC) | InferenceComponentName, Region, AvailabilityZone, InstanceType | InvocationModelErrorsForIcByAzByInstanceType | 
| 33 | InvocationModelErrors (IC) | EndpointName, VariantName, InferenceComponentName, InstanceId, ContainerId | InvocationModelErrorsForIcByInstanceIdByContainerId | 

## Latency metrics mapping
<a name="detailed-observability-mapping-latency"></a>


**Latency metrics mapping**  

| \# | CloudWatch classic metric | CloudWatch classic dimensions | OpenTelemetry metric | 
| --- | --- | --- | --- | 
| 34 | ModelLatency | EndpointName, VariantName | ModelLatency | 
| 35 | ModelLatency | EndpointName, VariantName, InstanceId | ModelLatencyByInstanceId | 
| 36 | ModelLatency | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | ModelLatencyByAzByInstanceType | 
| 37 | ModelLatency (IC) | InferenceComponentName | ModelLatencyForIc | 
| 38 | ModelLatency (IC) | InferenceComponentName, Region, AvailabilityZone, InstanceType | ModelLatencyForIcByAzByInstanceType | 
| 39 | ModelLatency (IC) | EndpointName, VariantName, InferenceComponentName, InstanceId, ContainerId | ModelLatencyForIcByInstanceIdByContainerId | 
| 40 | OverheadLatency | EndpointName, VariantName | OverheadLatency | 
| 41 | OverheadLatency | EndpointName, VariantName, InstanceId | OverheadLatencyByInstanceId | 
| 42 | OverheadLatency | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | OverheadLatencyByAzByInstanceType | 
| 43 | OverheadLatency (IC) | InferenceComponentName | OverheadLatencyForIc | 
| 44 | OverheadLatency (IC) | InferenceComponentName, Region, AvailabilityZone, InstanceType | OverheadLatencyForIcByAzByInstanceType | 
| 45 | OverheadLatency (IC) | EndpointName, VariantName, InferenceComponentName, InstanceId, ContainerId | OverheadLatencyForIcByInstanceIdByContainerId | 

## Bidirectional streaming metrics mapping
<a name="detailed-observability-mapping-streaming"></a>


**Bidirectional streaming metrics mapping**  

| \# | CloudWatch classic metric | CloudWatch classic dimensions | OpenTelemetry metric | 
| --- | --- | --- | --- | 
| 46 | MidStreamErrors | EndpointName, VariantName | MidStreamErrors | 
| 47 | FirstChunkLatency | EndpointName, VariantName | FirstChunkLatency | 
| 48 | FirstChunkLatency | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | FirstChunkLatencyByAzByInstanceType | 
| 49 | FirstChunkModelLatency | EndpointName, VariantName | FirstChunkModelLatency | 
| 50 | FirstChunkModelLatency | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | FirstChunkModelLatencyByAzByInstanceType | 
| 51 | FirstChunkOverheadLatency | EndpointName, VariantName | FirstChunkOverheadLatency | 
| 52 | FirstChunkOverheadLatency | EndpointName, VariantName, Region, AvailabilityZone, InstanceType | FirstChunkOverheadLatencyByAzByInstanceType | 

## Migration guidance
<a name="detailed-observability-mapping-migration"></a>
+ CloudWatch classic metrics continue publishing unchanged. Enabling detailed observability does not disable classic metrics.
+ Both CloudWatch classic metrics and OpenTelemetry metrics run in parallel. You can query both during your migration period.
+ Existing CloudWatch alarms on classic metrics continue to fire. Update alarms to OpenTelemetry metric names at your own pace.
+ Use OTel enrichment to make CloudWatch classic metrics PromQL-queryable alongside OpenTelemetry metrics in one SageMaker AI Insights Dashboard.