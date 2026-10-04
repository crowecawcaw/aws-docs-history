

# What no alarm covers
<a name="mon-build-a-dashboard"></a>

No dashboard is deployed. The alarms above cover stream processing thoroughly and the rest of the platform barely, so the following are unwatched until you watch them. None of these is a defect in the Guidance; they are the choices a production deployment makes for itself.


| Component | Metrics worth a dashboard | 
| --- | --- | 
| Managed Streaming for Apache Kafka | Broker CPU, disk usage per broker, under-replicated partitions, and offline partitions. Disk filling is the failure that stops ingestion outright. | 
| DynamoDB | Throttled requests and consumed capacity per table, plus `SystemErrors`. The platform’s tables are on-demand billing, so throttling indicates a partition-key hot spot rather than a provisioning shortfall. | 
| ElastiCache for Redis | Cache hit rate, evictions, and memory used. Live vehicle state is served from Redis, so evictions surface as vehicles that look offline. | 
| Lambda | Errors, throttles, duration and concurrent executions across the API and command handlers. | 
| API Gateway | 4XX and 5XX rates, latency, and integration latency, separated for the Fleet Management, Commands and Connected Services APIs. | 
| ECS services | Running task count against desired count, plus task CPU and memory. A simulation worker that cannot start looks like an empty demonstration. | 
| AWS IoT Core | Connect and publish success rates, and rule execution failures, which is where certificate and policy problems surface. | 

Two platform-specific signals deserve a place alongside the AWS service metrics. **A sustained nonzero `TripsClosed` rate** in the `CMS/TripSweeper` namespace means trip closure is failing upstream and the hourly sweeper is masking it — see [Closing trips that never close](trip-lifecycle.md#trip-stuck-sweeper). And **vehicles whose last-known state is stale** while their connection status reads connected indicate that telemetry is arriving at the platform but not completing its path through processing.