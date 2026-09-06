

# Ingesting Third Party Application Performance Monitoring Alarms
<a name="idr-gs-ingest-apm-alarms"></a>

AWS Incident Detection and Response supports alarm ingestion from third-party Application Performance Monitoring(APM) tools through Amazon EventBridge. This integration provides flexibility by ingesting APM alerts, allowing routing of APM events via various AWS services to an Amazon EventBridge event bus in your account.

Integration path examples:
+ Source (APM) → AWS Service (Example: Amazon API Gateway or Amazon SNS) → Transform Lambda Function → Custom Amazon EventBridge Event Bus → AWS Incident Detection and Response
+ Source (APM) → Partner Amazon EventBridge Event Bus → Transform Lambda Function → Custom Amazon EventBridge Event Bus → AWS Incident Detection and Response

AWS Incident Detection and Response installs a managed rule on the custom event bus to ingest alerts sent to it by Transform Lambda Functions. It's important to note that for SaaS Amazon EventBridge Integrations, the partner event bus isn't the event bus that has a managed rule installed. For a complete list of APMs with partner integrations to Amazon EventBridge, see [Amazon EventBridge integrations](https://aws.amazon.com/eventbridge/integrations).

**Example integration using a partner event bus or other AWS event bus sources**

The following diagram shows an example integration using a partner event bus or other AWS event bus sources.

![Diagram showing an example integration using a partner event bus or other AWS event bus sources.](http://docs.aws.amazon.com/IDR/latest/userguide/images/example-int-partner-event-bus.png)


For a complete list of APMs with partner integrations to Amazon EventBridge, see [Amazon EventBridge integrations](https://aws.amazon.com/eventbridge/integrations/).

**Example integration using Amazon API Gateway**

The following diagram shows an example of integration using a API Gateway.

![Diagram showing an example of integration using API Gateway.](http://docs.aws.amazon.com/IDR/latest/userguide/images/example-int-api-gateway.png)


**Example integration using Amazon Simple Notification Service**

The following diagram shows an example of integration using a Amazon SNS.

![Diagram showing an example of integration using Amazon SNS.](http://docs.aws.amazon.com/IDR/latest/userguide/images/example-int-sns.png)


To simplify the integration process, AWS Incident Detection and Response provides CloudFormation templates for the most commonly used integration types. These templates automate the setup of AWS resources, and necessary IAM roles.

CloudFormation Templates and instructions to manually create various integration types can be found in the corresponding integration documentation below:
+ [Ingest Alarms from APMs with direct EventBridge integration](idr-gs-ingest_alarms_from_apm_to_eventbridge.md)
+ [Ingest alarms from APMs without direct integration with EventBridge](idr-gs-ingest-apm-webhooks.md)
+ [Ingest Alarms from APMs with direct Amazon SNS integration](idr-gs-ingest-apm-sns.md)

**Note**  
The CloudFormation templates require modifications. These modifications are explained in the preceding topics. For more information on the required payload format for sending APM alerts to AWS Incident Detection and Response see [Payload Requirements For Ingesting APM Alerts with EventBridge](idr-gs-apm-payload-requirements.md).