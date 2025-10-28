# GENOPS02-BP01 Monitor all application layers

Implement comprehensive monitoring and logging across all layers of
your generative AI application to maintain operational health,
provide reliability, and optimize performance. This best practice
aims to provide clear visibility into the application's behavior at
every level, from user interactions to core model performance. By
tracking key metrics, organizations can quickly identify and address
issues, enhance user experiences, and make data-driven decisions to
improve their AI systems.

**Desired outcome:** When
implemented, your organization closely monitors the performance of
generative AI workloads.

**Benefits of establishing this best
practice:**

- [Implement
  observability for actionable insights](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Monitor the
  performance of your generative AI workload at all layers of the
  application, increasing visibility into application operational
  state and facilitating the early intervention of operational
  issues.
- [Learn
  from all operational events and metrics](../framework/oe-design-principles.md "../framework/oe-design-principles.md") - Capturing
  fine-grained observations enables continuous improvement.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Generative AI applications have several layers. First and foremost
is the application layer, which is the software abstraction above
a foundation model. Then, there is a service layer, an optional
gateway that negotiates prompts and brokers responses back to the
application layer. Depending on the use case, the service layer
may interact with a prompt catalog, a vector data store, or
several guardrails before ultimately interacting with a foundation
model. Simple generative AI workloads may respond back to the
service layer and apply configured guardrails where appropriate
before ultimately responding back at the application layer. More
complex workloads may navigate a knowledge graph, run a prompt
flow, or initiate an agent. The different layers and scenarios for
a generative AI application to traverse require proactive
monitoring and application telemetry at each layer.

Managed services like Amazon Bedrock, Amazon Q Business, and
Amazon OpenSearch Service Serverless facilitate much of this monitoring on
your behalf. These managed services integrate well with monitoring
and logging services like Amazon CloudWatch and AWS CloudTrail.
Amazon SageMaker AI Inference Endpoints can also log to CloudWatch.
Evaluate different logging solutions that best suit your needs,
and implement monitoring at each layer of your custom generative
AI workflow.

### Implementation steps

1. Identify your application layers, including:
   - Application layer
   - Service layer
   - Foundation model layer
   - Additional layers (for example, prompt catalog, vector
     data store, or knowledge graph)

2. For application layer monitoring:
   - Enable logs and metrics in Amazon CloudWatch
   - For custom metrics, set up for application-specific
     events and performance indicators

3. For service layer monitoring:
   - Enable logs and metrics in Amazon CloudWatch
   - For request flow analysis, implement tracing with AWS X-Ray or use Amazon Bedrock Agent's tracing feature

4. For foundation model layer monitoring:
   - Use built-in monitoring in Amazon Bedrock or Amazon Q Business
   - Configure CloudWatch logging for Amazon SageMaker AI
     Inference Endpoints

5. For additional layer monitoring:
   - Enable logs and metrics in your chosen vector database,
     such as Amazon OpenSearch Service
   - Set up CloudWatch logs and metrics for prompt catalogs
     or knowledge graphs

6. Configure alerting and dashboards.
   - Set up CloudWatch alarms for critical metrics and
     thresholds
   - Create CloudWatch dashboards for key performance
     indicators

7. Configure security monitoring.
   - Enable AWS CloudTrail for API activity logging
   - Set up Amazon GuardDuty for threat detection

8. Continually optimize.
   - Review and analyze log data to identify improvements
   - Adjust monitoring configurations based on changing
     application needs and usage patterns

9. Consider additional logging solutions:
   - For log ingestion and transformation, consider Amazon Data Firehose
   - For as-needed querying, explore Amazon Athena for logs
     stored in Amazon S3

## Resources

Related practices:

- [OPS08-BP01](../operational-excellence-pillar/ops_workload_observability_analyze_workload_metrics.md "../operational-excellence-pillar/ops_workload_observability_analyze_workload_metrics.md")
- [OPS08-BP02](../operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.md "../operational-excellence-pillar/ops_workload_observability_analyze_workload_logs.md")
- [OPS08-BP03](../operational-excellence-pillar/ops_workload_observability_analyze_workload_traces.md "../operational-excellence-pillar/ops_workload_observability_analyze_workload_traces.md")
- [OPS08-BP04](../operational-excellence-pillar/ops_workload_observability_create_alerts.md "../operational-excellence-pillar/ops_workload_observability_create_alerts.md")
- [OPS08-BP05](../operational-excellence-pillar/ops_workload_observability_create_dashboards.md "../operational-excellence-pillar/ops_workload_observability_create_dashboards.md")

**Related guides, videos, and documentation:**

- [Using
  Amazon CloudWatch Metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md")
- [Using
  Amazon CloudWatch Dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md")
- [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
- [CloudWatch Logs Insights Query Examples](../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md "../../../AmazonCloudWatch/latest/logs/CWL_QuerySyntax-examples.md")
- [Publishing
  Custom Metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md")

**Related examples:**

- [Monitor
  the health and performance of Amazon Bedrock](../../../bedrock/latest/userguide/monitoring.md "../../../bedrock/latest/userguide/monitoring.md")
- [Metrics
  for monitoring Amazon SageMaker AI with Amazon CloudWatch](../../../sagemaker/latest/dg/monitoring-cloudwatch.md "../../../sagemaker/latest/dg/monitoring-cloudwatch.md")
- [Monitoring
  OpenSearch Serverless with Amazon CloudWatch](../../../opensearch-service/latest/developerguide/monitoring-cloudwatch.md "../../../opensearch-service/latest/developerguide/monitoring-cloudwatch.md")
- [Monitoring
  Amazon Q Business and Amazon Q Apps with Amazon CloudWatch](../../../amazonq/latest/qbusiness-ug/monitoring-cloudwatch.md "../../../amazonq/latest/qbusiness-ug/monitoring-cloudwatch.md")
- [Monitoring
  Amazon Q Developer with Amazon CloudWatch](../../../amazonq/latest/qdeveloper-ug/monitoring-cloudwatch.md "../../../amazonq/latest/qdeveloper-ug/monitoring-cloudwatch.md")

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Amazon Data Firehose](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")
- [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/")
- [Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/ "https://aws.amazon.com/opensearch-service/features/serverless/")
- [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/")
- [Amazon Q](https://aws.amazon.com/q/ "https://aws.amazon.com/q/")
