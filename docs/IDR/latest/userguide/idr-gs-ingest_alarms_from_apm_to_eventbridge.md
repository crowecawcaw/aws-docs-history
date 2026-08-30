# Ingest Alarms from APMs with direct EventBridge integration

The following topic shows the process for sending alarms to
AWS Incident Detection and Response from Application Performance Monitoring (APM) tools that
have direct integration with Amazon EventBridge. For a complete list of APMs
that have direct integration with Amazon EventBridge, see [Amazon EventBridge
integrations](https://aws.amazon.com/eventbridge/integrations "https://aws.amazon.com/eventbridge/integrations").

You can deploy the provided [CloudFormation template](https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSaasEventBridgeIntegration.json "https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSaasEventBridgeIntegration.json") or manually setup this integration.
Before setting up the integration, verify that the AWS
service-linked role (SLR)
`AWSServiceRoleForHealth_EventProcessor`, is [created](idr-gs-access-prov.md "idr-gs-access-prov.md") in your accounts.

## Option 1: Using CloudFormation

A CloudFormation template is available to simplify the process of
creating the integration infrastructure required to ingest
alarms to AWS Incident Detection and Response from your APM with Amazon EventBridge
integration.

###### Note

- Additional costs are incurred for resources
  deployed through this CloudFormation template (eg: Lambda and
  EventBridge). For more information about the pricing of
  these services, see [AWS
  Pricing](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/").
- Deploy this CloudFormation template in every AWS account
  and Region where AWS Incident Detection and Response needs to ingest alarms.
  Incidents and Support Cases are opened on the AWS
  Account where the APM alert was received
  from.
- This document uses New Relic as an example,
  however the CloudFormation template can be used for any APM
  that has [SaaS integration with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-saas.md "../../../eventbridge/latest/userguide/eb-saas.md").
- After testing the integration, remove
  logger.info() statements from the
  `TransformLambdaFunction` to prevent
  the payload from appearing in Amazon CloudWatch Logs.

**Prerequisites for deploying this CloudFormation
template:**

- A Partner Event source must be setup in Amazon EventBridge. For
  instructions on setting up your APM as an event source,
  see [Receiving events from a SaaS partner with
  Amazon EventBridge](../../../eventbridge/latest/userguide/eb-saas.md "../../../eventbridge/latest/userguide/eb-saas.md") in the _Amazon EventBridge User
  Guide_.
- The `TransformLambdaFunction` (Lambda
  function) in the template must be modified to set
  `["detail"]["incident-detection-response-identifier"]`
  to the desired value based on the JSON path of the alert
  name in the APM payload.

**Prerequisite Steps:**

1. Open the EventBridge Console. Under the
   **Integration** menu, select
   **Partner event sources**.

   - Search for your APM in the Amazon EventBridge partners
     box.
   - Choose **Setup**, then follow
     the instructions provided.

     - **Note:** the
       last step is to choose **Associate with
       Event Bus** in the console for
       the Partner event source. Selecting this option
       automatically create a Partner Event Bus with the
       same name as the Partner event source (the names
       must match).

   - Copy the name of the Partner Event Bus or
     source. The Event Bus or source is used as a
     parameter, named
     `PartnerEventBusNameParameter`, when
     deploying the CloudFormation template.

     - **Example** for
       New Relic:
       `aws.partner/newrelic.com/1234567/source_name`

   - Copy the first part of the Partner Event Bus
     or source to input into the
     `PartnerEventBusPrefixParameter` when
     deploying the CloudFormation template.

     - Example for New Relic is
       `aws.partner/newrelic.com`

2. Download and edit the [CloudFormation template](https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSaasEventBridgeIntegration.json "https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSaasEventBridgeIntegration.json").

   - Locate the
     `TransformLambdaFunction` in the
     template
   - Under `def lambda_handler(event,
  context)` set
     `event["detail"]["incident-detection-response-identifier"]`
     to the json path where alarm name appears in the
     JSON payload of the APM alarm. Every APM will have
     a different path. Some examples can be seen below,
     however your specific payloads may differ.

     - **New Relic
       Example:**
       `event["detail"]["incident-detection-response-identifier"]
   = event["detail"]["workflowName"]`.
     - **Datadog
       Example:**
       `event["detail"]["incident-detection-response-identifier"]
   =
   event["detail"]["meta"]["monitor"]["name"]`
     - **Splunk
       Example:**
       `event["detail"]["incident-detection-response-identifier"]
   = event["detail"]["ruleName"]`

   - Save the CloudFormation template.

**Deploying the CloudFormation
Template:**

1. Open the CloudFormation console in your target account and
   Region.
2. Choose Create stack, With new resources
   (standard)

   - Select **Choose an existing
     template**, **Upload a template
     file**, **Choose file**,
     then upload the CloudFormation template you saved
     locally.

3. Specify stack details:

   - Enter a stack name
     (_Example:_
     `NewRelicIntegrationForIDR`).
   - Specify the **Parameter
     values** obtained during **Prerequisite
     completion**.

     - APMNameParameter
       (_Example_:
       `NewRelic`)
     - PartnerEventBusNameParameter
       (_Example_:
       `aws.partner/newrelic.com/1234567/source_name`)
     - PartnerEventBusPrefixParameter
       (_Example_:
       `aws.partner/newrelic.com`)

   - Choose **Next**.

4. Configure stack options:

   - Scroll to the bottom of the page and check the
     box to allow CloudFormation to create IAM resources with
     custom names.

5. Review and create:

   - Validate the parameter values are configured
     correctly and choose
     **Submit**.

6. The CloudFormation stack deploys the resources necessary to
   integrate your APM events to AWS Incident Detection and Response. Wait for the
   stack status to show
   `CREATE_COMPLETE`.
7. The CloudFormation stack creates the following resources,
   assuming the example values were input into the
   parameters for New Relic and was run in the US-EAST-1
   Region.

   - CustomEventBus:
     NewRelic-AWSIncidentDetectionResponse-EventBus
   - EventBridgeRule:
     aws.partner/newrelic.com/1234567/source\_name|NewRelic-AWSIncidentDetectionResponse-EventBridgeRule
   - TransformLambdaExecutionRole:
     IDR-TransformLambdaExecutionRole-us-east-1
   - TransformLambdaFunction:
     NewRelic-AWSIncidentDetectionResponse-Lambda-Transform
   - TransformLambdaPermission:
     NewRelicIntegrationForIDR-TransformLambdaPermission-[random\_string]

**Integration testing**

After deploying the stack, test the integration by sending a
test payload from your APM:

1. Navigate to the Lambda Console and select the
   `APMNameParameter-AWSIncidentDetectionResponse-Lambda-Transform`
   function. Choose the **Monitor**
   tab.
2. Look for a successful invocation in the metric
   graphs.
3. Choose **View Amazon CloudWatch Logs** to
   check Log streams for your test payload or any
   errors.

**Sharing Your Event Bus ARN to
AWS Incident Detection and Response**

1. Open the Amazon EventBridge Console. Select **Event
   buses**.
2. Copy the ARN of the **Custom event
   bus** created as part of the CloudFormation stack,
   (_example:
   `arn:aws:events:us-east-1:123456789123:event-bus/NewRelic-AWSIncidentDetectionResponse-EventBus`_.)

   - Add this ARN to the "EventBridge Event Bus
     ARN" field in the "Third-Party APM Alarms" section
     of your [Workload details - Alarm ingestion questions](idr-gs-questionnaire.md#idr-gs-alarm-questionnaire "idr-gs-questionnaire.md#idr-gs-alarm-questionnaire").

3. During the onboarding process, AWS Incident Detection and Response creates a
   managed EventBridge rule on this custom event bus to
   ingest your APM alarms.

## Option 2: Manual integration

![Diagram showing an example integration using a partner event bus or other AWS event bus sources.](/images/IDR/latest/userguide/images/example-int-partner-event-bus.png)

Complete the following steps for each AWS account and AWS
Region where AWS Incident Detection and Response needs to ingest alarms from. AWS Incident Detection and Response
recommends to set up alarms in the same AWS account and Region
as your application resources to make it quicker to identify and
investigate impacted resources. Incidents and Support Cases are
opened on the AWS Account where the APM alert was received
from.

1. Create an EventBridge partner event bus by setting up
   your APM as an Amazon EventBridge partner event source (for
   example,
   `aws.partner/apm_name/integrationName`).
   For guidelines on setting up your APM as an event
   source, see [Receiving events from a SaaS partner with
   Amazon EventBridge](../../../eventbridge/latest/userguide/eb-saas.md "../../../eventbridge/latest/userguide/eb-saas.md").
2. Perform one of the following:

   - (Recommended) Create an EventBridge custom
     event bus named
     `$YourApmName-AWSIncidentDetectionResponse-EventBus`.
   - (Alternative) Use the default EventBridge
     event bus instead of a custom event bus.
     AWS Incident Detection and Response will install a managed rule
     (`AWSHealthEventProcessorEventSource-DO-NOT-DELETE`)
     on the custom or default event bus through the
     `AWSServiceRoleForHealth_EventProcessor`
     SLR. The rule source will be the custom or default event
     bus, the rule destination will be AWS Incident Detection and Response, and the
     rule will match the pattern for ingesting 3rd party APM
     events.

3. Create an [Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
   function named
   `$YourApmName-AWSIncidentDetectionResponse-LambdaFunction`
   to transform your partner event bus events. The
   transformed events will match the managed rule
   `AWSHealthEventProcessorEventSource-DO-NOT-DELETE`.

   - Transformed events include a unique AWS Incident Detection and Response
     identifier, and sets the source and detail type of
     the event to the required values. This allows the
     transformed JSON payload structure to match the
     managed rule pattern.
   - Set the target of the Lambda function to either
     the custom event bus (Recommended) created in Step
     2 or to your default event bus.

4. Create an EventBridge rule and define the event
   patterns that match the list of events that you want to
   push to AWS Incident Detection and Response. The source of the rule is the partner
   event bus you created in Step 1
   (`aws.partner/apm_name/integrationName`).
   The target of the rule is the Lambda function you created
   in Step 3
   (`[apm_name]-AWSIncidentDetectionResponse-LambdaFunction`).
   For guidelines on defining your EventBridge rule, see
   [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md").

For a step by step example on how to set up partner event bus
integrations manually with AWS Incident Detection and Response, see [Integrating notifications from Datadog and
Splunk](example_integrating_notifications.md "example_integrating_notifications.md").
