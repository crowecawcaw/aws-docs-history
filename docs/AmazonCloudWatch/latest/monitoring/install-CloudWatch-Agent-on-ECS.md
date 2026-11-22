

# Install the CloudWatch agent on Amazon ECS

On Amazon ECS, you don't install the CloudWatch agent with the Amazon EC2 or manual methods. Instead, you run the agent as a container that you define in your Amazon ECS task definition. The agent runs alongside your application containers and sends metrics, logs, and traces to CloudWatch.

To set up Container Insights on Amazon ECS, see [Container Insights for Amazon ECS](deploy-container-insights-ECS.md).

To collect instance-level metrics on Amazon ECS, see [Deploying the CloudWatch agent to collect EC2 instance-level metrics on Amazon ECS](deploy-container-insights-ECS-instancelevel.md).

To receive OTLP data from your applications through the agent on Amazon ECS, see [Amazon CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md).