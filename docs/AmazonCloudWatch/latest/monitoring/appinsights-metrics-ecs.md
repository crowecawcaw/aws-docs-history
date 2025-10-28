# Amazon Elastic Container Service (Amazon ECS)

CloudWatch Application Insights supports the following metrics:

###### Metrics

- [CloudWatch built-in
  metrics](#appinsights-metrics-ecs-built-in-metrics "#appinsights-metrics-ecs-built-in-metrics")
- [Container
  Insights metrics](#appinsights-metrics-ecs-container-insights-metrics "#appinsights-metrics-ecs-container-insights-metrics")
- [Container Insights Prometheus metrics](#appinsights-metrics-ecs-container-insights-prometheus "#appinsights-metrics-ecs-container-insights-prometheus")

## CloudWatch built-in

metrics

CPUReservation

CPUUtilization

MemoryReservation

MemoryUtilization

GPUReservation

## Container

Insights metrics

ContainerInstanceCount

CpuUtilized

CpuReserved

DeploymentCount

DesiredTaskCount

MemoryUtilized

MemoryReserved

NetworkRxBytes

NetworkTxBytes

PendingTaskCount

RunningTaskCount

ServiceCount

StorageReadBytes

StorageWriteBytes

TaskCount

TaskSetCount

instance_cpu_limit

instance_cpu_reserved_capacity

instance_cpu_usage_total

instance_cpu_utilization

instance_filesystem_utilization

instance_memory_limit

instance_memory_reserved_capacity

instance_memory_utilization

instance_memory_working_set

instance_network_total_bytes

instance_number_of_running_tasks

## Container Insights Prometheus metrics

**Java JMX metrics**

java_lang_memory_heapmemoryusage_used

java_lang_memory_heapmemoryusage_committed

java_lang_operatingsystem_openfiledescriptorcount

java_lang_operatingsystem_maxfiledescriptorcount

java_lang_operatingsystem_freephysicalmemorysize

java_lang_operatingsystem_freeswapspacesize

java_lang_threading_threadcount

java_lang_classloading_loadedclasscount

java_lang_threading_daemonthreadcount

java_lang_garbagecollector_collectiontime_copy

java_lang_garbagecollector_collectiontime_ps_scavenge

java_lang_garbagecollector_collectiontime_parnew

java_lang_garbagecollector_collectiontime_marksweepcompact

java_lang_garbagecollector_collectiontime_ps_marksweep

java_lang_garbagecollector_collectiontime_concurrentmarksweep

java_lang_garbagecollector_collectiontime_g1_young_generation

java_lang_garbagecollector_collectiontime_g1_old_generation

java_lang_garbagecollector_collectiontime_g1_mixed_generation

java_lang_operatingsystem_committedvirtualmemorysize
