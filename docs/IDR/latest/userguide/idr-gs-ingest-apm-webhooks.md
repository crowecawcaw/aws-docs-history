

# Ingest alarms from APMs without direct integration with EventBridge
<a name="idr-gs-ingest-apm-webhooks"></a>

AWS Incident Detection and Response supports using webhooks for alarm ingestion from third party APMs that don't have direct integration with Amazon EventBridge.

You can deploy a CloudFormation template or manually set up the integration. Before setting up the integration, verify that the AWS service-linked role (SLR) `AWSServiceRoleForHealth_EventProcessor`, is [created](https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-access-prov.html) in your accounts.

## Option 1: Using CloudFormation Template
<a name="idr-gs-apm-webhook-cfn"></a>

A CloudFormation template is available to simplify the process of creating the integration infrastructure required to ingest alarms to AWS Incident Detection and Response from your APM that does not have direct Amazon EventBridge integration.

**Considerations before deploying this CloudFormation Template**
+ This solution uses an API Gateway Lambda Authorizer to compare a secret token passed in the payload from your APM against a token in AWS Secrets Manager. If the token does not match, a policy with an explicit deny will be returned. For more information, see [Lambda Authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html).
+ Under the AWS Shared Responsibility model, it is your responsibility to ensure you use an authentication approach that meets your organization's security requirements. We recommend using AWS Secrets Manager or a similar service, instead of storing sensitive information like API keys or authorization tokens as hard-coded variables. For more information, see [Create and manage secrets with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html).
+ For an additional example of implementing Hash-Based Message Authentication Code (HMAC), see [receive-webhooks on the aws-samples Github page](https://github.com/aws-samples/webhooks/tree/main/receive-webhooks). For more information on implementing token authorization, see [example TOKEN authorizer Lambda function](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html#api-gateway-lambda-authorizer-token-lambda-function-create) from the API Gateway documentation.
+ The solution uses **RateLimit**, **BurstLimit**, and **Quota** in API Gateway to control request volumes. These tools limit how many requests can be processed in a set time. This helps prevent system overload and keeps the service stable. For more information on throttling, refer to the [API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html).
+ Consider using AWS Web Application Firewall (WAF) to protect the API Gateway from known bad IP addresses. This reduces the risk of attackers flooding the API with fake requests that could block real log events.
+ AWS Secrets Manager token values should be stored in your Application Performance Monitoring (APM) tool as an HTTP header. Ensure to rotate the token on a regular basis as a security best practice.
+ Additional costs will be incurred for resources deployed through this CloudFormation template (eg: Lambda and EventBridge). For more information about the pricing of these services, see [AWS Pricing](https://aws.amazon.com/pricing/).
+ After testing the integration, remove logger.info() statements from the `TransformLambdaFunction` (Lambda function) to prevent payloads from appearing in Amazon CloudWatch Logs.
+ Deploy this CloudFormation template in every AWS account and Region where AWS Incident Detection and Response needs to ingest alarms from.

**Preparing the CloudFormation Template:**

**Note:** The integration steps use Dynatrace as an example, however this template can be used for any APM that can send payloads to an API Gateway.

1. Download and open the [CloudFormation template](https://dcl74d3hc5lj1.cloudfront.net/apms/ThirdPartyApmWebhookIntegration.json).

1. Locate `APIGWUsagePlan` in the template. Review the values configured for `RateLimit`, `BurstLimit`, and `Quota Limit` which are set to 20, 50 & 2000 by default. Adjust the values to meet your requirements.

1. Locate `AuthorizerLambdaFunction` in the template. This Lambda function serves as an example of an authentication mechanism. It extracts a token value from a header called `authorizationToken`, which is passed from your APM. You can modify this code to align with your organization's security policies and APM requirements.

1. Locate the `TransformLambdaFunction` in the template. Replace the dictionary path, `raw_json["detail"]["ProblemTitle"]`, with the path to your alarm's name that is sent in the JSON payload from your APM. Leave this as is for Dynatrace.

**Deploying the CloudFormation template:**

1. Open the CloudFormation console in your target account and AWS Region.

1. Choose **Create stack, With new resources (standard)**.
   + Select **Choose an existing template**, **Upload a template file**, **Choose file**, then upload the CloudFormation template you saved locally.

1. Specify stack details:
   + Enter a stack name (*example, `DynatraceIntegrationForIDR`*.)
   + APMNameParameter (*example, `Dynatrace`*.)
   + Choose **Next**.

1. Configure stack options:
   + Scroll to the bottom of the page and check the box to allow CloudFormation to create IAM resources with custom names.

1. Review and create:
   + Validate the parameter values are configured correctly and choose Submit.

1. The CloudFormation stack deploy the resources necessary to integrate your APM events to AWS Incident Detection and Response. Wait until the CloudFormation Stack Status is **CREATE\_COMPLETE**.

1. The CloudFormation stack creates the below resources assuming the example value `Dynatrace` was input into the parameters and was executed in the US-EAST-1 Region.
   + Secret name: DynatraceMySecretTokenName (a random Secret value will be created against Secret key APMSecureToken)
   + API Gateway resources:
     + API Name: Dynatrace-AWSIncidentDetectionResponse-APIGW
     + Stage Name: Dynatrace-Stage-Prod
     + Authorizers: Dynatrace-APIGW-Authorizer
     + Usage plan: APIGW\_Throttling\_Plan
   + Lambda functions:
     + Function for authorization: Dynatrace-AWSIncidentDetectionResponse-Lambda-Authorizer
     + Function for transformation: Dynatrace-AWSIncidentDetectionResponse-Lambda-Transform
   + Custom EventBus Name: Dynatrace-AWSIncidentDetectionResponse-EventBus
   + IAM Role:
     + TransformLambdaExecutionRole: IDR-TransformLambdaExecutionRole-us-east-1
     + AuthorizerLambdaExecutionRole: IDR-AuthorizerLambdaExecutionRole-us-east-1

1. Record the Webhook URL and Token value:
   + Open the API Gateway console and choose your API Name created as part of the CloudFormation stack.
   + Choose Stages from the left-hand navigation, expand the stage name using the \+ sign, then choose POST. Record the **Invoke URL**. Configure this URL in your APM as the destination to send webhooks for alarm events.
   + Open the AWS Secrets Manager console and choose the Secret name created as part of the CloudFormation stack. (*Example: DynatraceMySecretTokenName.*)
     + In the Secret value tab, choose **Retrieve secret value**. You will see the Secret key as APMSecureToken. Record the Secret value. Do not share this secret value with anyone.

**Integration testing**

After deploying the stack, test the integration by sending a test payload from your APM:

1. Navigate to the Lambda Console and select `APMNameParameter-AWSIncidentDetectionResponse-Lambda-Transform` function. Choose the **Monitor** tab.

1. Look for a successful invocation in the metric graphs.

1. Choose **View Amazon CloudWatch Logs** to check Log streams for your test payload or any errors.

**Sharing Your Event Bus ARN to AWS Incident Detection and Response**

1. Open the Amazon EventBridge Console. Select Event buses.

1. Copy the ARN of the **Custom event bus** created as part of the CloudFormation stack, *example: `arn:aws:events:us-east-1:123456789123:event-bus/Dynatrace-AWSIncidentDetectionResponse-EventBus`*.
   + Add this ARN to the "EventBridge Event Bus ARN" field in the "Third-Party APM Alarms" section of your [Workload details - Alarm ingestion questions](idr-gs-questionnaire.md#idr-gs-alarm-questionnaire).

1. During the onboarding process, AWS Incident Detection and Response will create a Managed EventBridge rule on this custom event bus to ingest your APM alarms.

## Option 2: Manual integration
<a name="idr-gs-apm-webhook-manual"></a>

![Diagram showing an example of integration using API Gateway.](http://docs.aws.amazon.com/IDR/latest/userguide/images/example-int-api-gateway.png)


Use the following steps to set up integration with AWS Incident Detection and Response.

1. Create an Amazon API Gateway to accept the payload from your APM.

1. Define an Lambda function for authorization using an authentication token.

1. Perform one of the following:
   + (Recommended) Create an EventBridge custom event bus named `$YourApmName-AWSIncidentDetectionResponse-EventBus`.
   + (Alternative) Use the default EventBridge event bus instead of a custom event bus.

1. Define a Transform Lambda function to append the AWS Incident Detection and Response identifier to your payload. You can also use this function to filter for the events that you want to send to AWS Incident Detection and Response.
   + The API Gateway must invoke the Transform Lambda function which will transform the payload passed by the API Gateway.
   + The Transform Lambda Function must write transformed events in the event bus defined in point 3 above.

1. Set up your APM to send notifications to the URL generated from the API Gateway.