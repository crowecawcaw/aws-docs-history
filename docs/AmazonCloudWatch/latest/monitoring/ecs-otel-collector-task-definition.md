

# Step 3: Add the collector to your task definition

Add the following container definition to each task definition that you want to monitor. Replace {{region}} with your Region, and set the `OTEL_CONFIG` value to the configuration from step 2.

```json
{
  "name": "otel-collector",
  "image": "otel/opentelemetry-collector-contrib:0.165.0",
  "essential": false,
  "cpu": 128,
  "memory": 256,
  "command": ["--config", "env:OTEL_CONFIG"],
  "environment": [
    { "name": "AWS_REGION", "value": "{{region}}" },
    { "name": "OTEL_CONFIG", "value": "{{configuration from step 2}}" }
  ],
  "logConfiguration": {
    "logDriver": "awslogs",
    "options": {
      "awslogs-group": "/ecs/otel-collector",
      "awslogs-region": "{{region}}",
      "awslogs-stream-prefix": "otel"
    }
  }
}
```

Amazon ECS sets the task metadata endpoint address (`ECS_CONTAINER_METADATA_URI_V4`) in every container, so the collector needs no networking configuration.

Setting `essential` to `false` keeps a collector failure from stopping your application. To store a larger configuration outside the task definition, you can keep it in SSM Parameter Store and pass it with `secrets` instead of `environment`.

**Note**  
Adding the sidecar makes each task larger. On Amazon EC2, a rolling deployment can't place the new task if the container instance doesn't have room for the old and new tasks at the same time. Add capacity, or temporarily lower `minimumHealthyPercent` for the service.