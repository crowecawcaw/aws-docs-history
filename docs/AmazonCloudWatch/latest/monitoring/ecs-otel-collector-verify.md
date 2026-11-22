

# Step 4: Verify that metrics arrive

1. In the Amazon ECS console, confirm that the `otel-collector` container is running in the task.

1. Check the collector's log group. At the `warn` level, a healthy collector logs little or nothing. A `Partial success response` message means that CloudWatch rejected some data points, and the message gives the reason. An HTTP 403 error means that the task role doesn't allow `cloudwatch:PutMetricData`.

1. In the CloudWatch console, open Query Studio and run the following PromQL query. Within a few minutes, it returns one series for each running task.

   ```
   count by ("@resource.aws.ecs.service.name") ({"ecs.task.memory.utilized"})
   ```