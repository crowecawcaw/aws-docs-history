# Ingest Alarms from APMs with direct Amazon SNS integration

If your APM supports sending alarms to Amazon SNS topics you can follow
this guide to ingest your APM alarms to AWS Incident Detection and Response.

You can deploy the provided [CloudFormation template](https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSnsIntegration.json "https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSnsIntegration.json") or manually set up this integration. Before
setting up the integration, verify that the AWS service-linked role
(SLR) `AWSServiceRoleForHealth_EventProcessor`, is [created](idr-gs-access-prov.md "idr-gs-access-prov.md")
in your accounts.

## Option 1: Using CloudFormation

A CloudFormation template is available to simplify the process of creating
the integration infrastructure required to ingest alarms to
AWS Incident Detection and Response from your APM with Amazon SNS integration.

###### Note

- Additional costs will be incurred for resources
  deployed through this CloudFormation template (eg: Lambda and
  EventBridge). For more information about the pricing of
  these services, see [AWS
  Pricing](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/").
- This CloudFormation template must be deployed in every AWS
  account and Region that alarms need to be ingested by
  AWS Incident Detection and Response from.
- The examples provided in this document are for
  Grafana, however this template can be used for any APM
  that has direct integration with Amazon Simple Notification Service.
- For security reasons, AWS recommends removing
  `logger.info()` statements from the
  `TransformLambdaFunction` to prevent the
  payload from being logged in Amazon CloudWatch Logs.

**Prerequisites for deploying this CloudFormation
template:**

- A **Standard** Amazon Simple Notification Service topic must be created to receive alarm events
  from your APM. [Create an SNS topic in the Amazon Simple Notification Service
  console](../../../sns/latest/dg/sns-create-topic.md#create-topic-aws-console "../../../sns/latest/dg/sns-create-topic.md#create-topic-aws-console").
- The `TransformLambdaFunction` in the template
  must be modified to set
  `["detail"]["incident-detection-response-identifier"]`
  to the desired value based on the APM being used.

**Prerequisite completion:**

1. Open the Amazon SNS Console, then select Topics. Copy the ARN
   of the **Standard** Amazon SNS topic created to receive alarm events from your
   APM.

   - Example:
     `arn:aws:sns:eu-west-1:012345678912:<your-apm-name>-sns`

2. Download and open the [CloudFormation template](https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSnsIntegration.json "https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmSnsIntegration.json")

   - Locate the `TransformLambdaFunction` in
     the template

     - Under `def lambda_handler(event,
   context)` set
       `event["detail"]["incident-detection-response-identifier"]`
       to the json path where the alarm name appears in
       the JSON payload of the SNS record.

       - Any event sent to the
         `TransformLambdaFunction` via SNS has a
         parent payload structure as
         `event["Records"][n]["Sns"]["Message"]`.
         The actual payload origin from the source (APM) is
         wrapped inside the parent structure.
       - **Example for
         Grafana:**
         `event["Records"][n]["Sns"]["Message"]["alerts"][n]["labels"]["alertname"]`

**Deploying the CloudFormation
Template:**

1. Navigate to the CloudFormation console in the account and Region
   you need to set up the integration in.
2. Navigate to CloudFormation.

   - Choose Create stack, With new resources
     (standard)

     - Select Choose an existing template, Upload a
       template file, Choose file, then upload the CloudFormation
       template you saved locally.

3. Specify stack details:

   - Enter a stack name _Example:_
     `<your-apm-name>IntegrationForIDR`
   - Specify the Parameter values obtained during
     **Prerequisite
     completion**

     - APMNameParameter
       _Example:_
       `Grafana`
     - TriggerSNSParameter
       _Example:_
       `arn:aws:sns:eu-west-1:012345678912:<your-apm-name>-sns`

   - Choose Next.

4. Configure stack options:

   - Scroll to the bottom of the page and acknowledge
     the checkbox to allow CloudFormation to create IAM
     resources with custom names.

5. Review and create:

   - Validate the parameter values are configured
     correctly, then choose Submit.

6. The CloudFormation stack will deploy the resources necessary to
   integrate your APM events to AWS Incident Detection and Response. Wait until the CloudFormation
   Stack Status is **CREATE\_COMPLETE**.
7. The CloudFormation stack creates the below resources assuming the
   example values were input into the parameters for Grafana
   and was executed in the EU-WEST-1 Region.

   - CustomEventBus:
     Grafana-AWSIncidentDetectionResponse-EventBus
   - SNSSubscription:
     arn:aws:sns:eu-west-1:012345678912:grafana-sns:[random\_string]
   - TransformLambdaExecutionRole:
     IDR-TransformLambdaExecutionRole-eu-west-1
   - TransformLambdaFunction:
     Grafana-AWSIncidentDetectionResponse-Lambda-Transform
   - TransformLambdaPermission:
     GrafanaIntegrationForIDR-TransformLambdaPermission-[random\_string]

**Integration testing**

After the CloudFormation stack is deployed successfully, you can validate
the integration by sending a test payload from your APM. Once the
test payload is sent from your APM:

1. Navigate to the Lambda Console and select the
   `APMNameParameter-AWSIncidentDetectionResponse-Lambda-Transform`
   function. Then, choose the Monitor tab.
2. A successful invocation should be observed in the metric
   graphs.
3. Select View Amazon CloudWatch Logs. You can verify from the Log
   events in the Log streams to confirm that the test payload
   sent from your APM is present, or if any errors were
   encountered.

**Sharing Your Event Bus ARN to
AWS Incident Detection and Response**

1. Navigate to the Amazon EventBridge Console. Select Event
   buses.
2. Record the ARN of the **Custom event
   bus** deployed as part of the CloudFormation stack, for
   example:
   `arn:aws:events:eu-west-1:012345678912:event-bus/Grafana-AWSIncidentDetectionResponse-EventBus`.

   - Provide the ARN of this Custom event bus to
     AWS Incident Detection and Response in the "EventBridge Event Bus ARN" field
     of the "Third-Party APM Alarms" section of the [Workload details - Alarm ingestion questions](idr-gs-questionnaire.md#idr-gs-alarm-questionnaire "idr-gs-questionnaire.md#idr-gs-alarm-questionnaire").

3. During the onboarding process, AWS Incident Detection and Response will create a
   Managed EventBridge rule on this custom event bus to ingest
   your APM alarms.

## Option 2: Manual integration

![Diagram showing an example of integration using Amazon SNS.](/images/IDR/latest/userguide/images/example-int-sns.png)

1. Open the Amazon SNS Console and create a **Standard** Amazon SNS topic
   named `[apm_name]-sns` to receive alarm events
   from your APM. Ensure you select **Standard** (not FIFO) as the topic type. Note the ARN of the Amazon SNS topic created.
2. Perform one of the following:

   - (Recommended) Create an EventBridge custom event
     bus named
     `[apm_name]-AWSIncidentDetectionResponse-EventBus`.
   - (Alternative) Use the default EventBridge event
     bus instead of a custom event bus.
     AWS Incident Detection and Response will install a managed rule
     (`AWSHealthEventProcessorEventSource-DO-NOT-DELETE`)
     on the custom or default event bus through the
     `AWSServiceRoleForHealth_EventProcessor` SLR.
     The rule source will be the custom or default event bus, the
     rule destination will be AWS Incident Detection and Response, and the rule will match
     the pattern for ingesting 3rd party APM events.

3. Create an [Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md")
   function named
   `$YourApmName-AWSIncidentDetectionResponse-LambdaFunction`
   to transform your SNS payloads.

   - Transformed events must meet the payload
     requirements as set out in [Payload Requirements For Ingesting APM Alerts with EventBridge](idr-gs-apm-payload-requirements.md "idr-gs-apm-payload-requirements.md")
   - Set the target of the Lambda function to either the
     custom event bus (Recommended) created in Step 2 or
     to your default event bus.

4. Set the SNS topic as a trigger for your Lambda function
   `$YourApmName-AWSIncidentDetectionResponse-LambdaFunction`.

   - In the "Add Triggers" page, search for
     "SNS".
   - Add the ARN of your dedicated SNS Topic created in
     Step 1.
   - Choose "Add".

5. Follow your APM documentation to set up an SNS destination
   for your APM payloads that need to be ingested by
   AWS Incident Detection and Response.

AWS Incident Detection and Response will install a managed rule
(`AWSHealthEventProcessorEventSource-DO-NOT-DELETE`)
on the custom or default event bus through the
`AWSServiceRoleForHealth_EventProcessor` SLR. The
rule source will be the custom or default event bus, the rule
destination will be AWS Incident Detection and Response, and the rule will match the pattern
for ingesting 3rd party APM events.
