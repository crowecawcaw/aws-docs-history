

# SMOPS02-BP03 Implement centralized logging to aggregate logs from all components of your streaming stack
<a name="smops02-bp03"></a>

To provide full visibility and operational efficiency across your streaming video stack, implement a centralized logging solution. By aggregating logs from all components of your streaming stack, including third-party integrations and custom applications, you gain a complete view of your system's performance and behavior.

**Desired outcome:**
+ A unified logging system that enables efficient troubleshooting, correlation of events across the streaming workflow, and historical analysis of operational patterns.

**Benefits of establishing this best practice:**
+ Faster troubleshooting through consolidated log access
+ Improved correlation of events across distributed systems
+ Enhanced ability to perform root cause analysis
+ Better historical insights for ongoing improvement

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Centralized logging that captures data from all components of the streaming video workflow provides the foundation for efficient troubleshooting and operational analysis.

Infrastructure logs from Amazon EC2 instances, containers from Amazon ECS or Amazon EKS, Lambda functions, and load balancers establish baseline visibility into the compute and network layer. Media processing logs from encoders (AWS Elemental MediaLive, AWS Elemental MediaConvert), packaging services (AWS Elemental MediaPackage), and transcoding jobs provide insight into content transformation workflows. Delivery logs from content delivery network (CDN) access logs, origin server logs, and edge function logs reveal content distribution performance. Application logs from API gateways, custom applications, and third-party integrations capture business logic behavior. Player logs including player error logs, quality of experience data, and user interaction events complete the picture.

Consider using Amazon OpenSearch Service for a strong, scalable log aggregation solution with powerful search and analytics capabilities, or Amazon CloudWatch Logs for a fully-managed service that requires less implementation effort. For multi-account and Multi-Region streaming workloads, Amazon CloudWatch cross-account cross-Region log centralization aggregates logs from across your AWS accounts and Regions into a single location, simplifying operational visibility across distributed streaming infrastructure.

### Implementation steps
<a name="implementation-steps"></a>

1. **Define logging standards:** Define logging standards and formats across your streaming stack so logs remain consistent and support effective correlation.

1. **Configure log collection:** Configure log collection from all components, including:
+ Infrastructure
+ Media processing
+ Delivery
+ Application
+ Player layers

1. **Implement a centralized logging solution:** Implement a centralized logging solution using Amazon OpenSearch Service or Amazon CloudWatch Logs based on your scale and analysis requirements.

1. **Create log filters:** Create log filters and search capabilities to enable rapid identification of relevant log entries during troubleshooting.

1. **Set up log-based alerts:** Set up log-based alerts for critical errors to enable proactive detection of issues before they impact viewers.

1. **Establish log retention policies:** Establish log retention policies that balance storage costs with the need for historical analysis and compliance requirements.

1. **Implement log analysis workflows:** Implement log analysis workflows to extract operational insights and identify patterns for ongoing improvement.

## Resources
<a name="resources"></a>

**Related documents**
+ [Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)
+ [Amazon CloudWatch cross-account cross-region log centralization](https://aws.amazon.com/about-aws/whats-new/2025/09/amazon-cloudwatch-cross-account-cross-region-log-centralization/)

**Related services**
+ [Amazon CloudWatch Logs](https://aws.amazon.com/cloudwatch/)
+ [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
+ [AWS Lambda](https://aws.amazon.com/lambda/)
+ [Amazon S3](https://aws.amazon.com/s3/)
+ [Amazon Kinesis Data Firehose](https://aws.amazon.com/firehose/)