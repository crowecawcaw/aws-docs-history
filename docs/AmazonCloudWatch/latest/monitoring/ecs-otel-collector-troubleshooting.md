

# Troubleshooting
<a name="ecs-otel-collector-troubleshooting"></a>


| Issue | Cause and resolution | 
| --- | --- | 
| The collector exits with unable to detect task metadata endpoint. | The task metadata endpoint version 4 isn't available. Check the platform version or container agent version. For more information, see [Prerequisites](ecs-otel-collector-prerequisites.md). | 
| Logs show Partial success response with StartTimeUnixNano is required. | The metric\_start\_time processor is missing from the pipeline. Add it as shown in [Step 2: Create the collector configuration](ecs-otel-collector-config.md). | 
| HTTP 403 errors from monitoring.{{region}}.amazonaws.com. | The task role doesn't allow cloudwatch:PutMetricData, or you attached the policy to the task execution role instead of the task role. | 
| The service deployment doesn't complete, and the service event says insufficient memory available. | The container instance can't fit the larger task alongside the current one. See the note in [Step 3: Add the collector to your task definition](ecs-otel-collector-task-definition.md). | 
| Metrics appear twice. | Container Insights is also turned on for the cluster. For more information, see [Prerequisites](ecs-otel-collector-prerequisites.md). | 