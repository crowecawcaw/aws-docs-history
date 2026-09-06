

# Log REST API calls to Amazon Data Firehose in API Gateway
<a name="apigateway-logging-to-kinesis"></a>

To help debug issues related to client access to your API, you can log API calls to Amazon Data Firehose. For more information about Firehose, see [What Is Amazon Data Firehose?](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html).

For access logging, you can only enable CloudWatch or Firehose—you can't enable both. However, you can enable CloudWatch for execution logging and Firehose for access logging.

**Topics**
+ [Firehose log formats for API Gateway](#apigateway-kinesis-log-formats)
+ [Permissions for Firehose logging](#set-up-kinesis-access-logging-permissions)
+ [Set up Firehose access logging by using the API Gateway console](#set-up-kinesis-access-logging-using-console)

## Firehose log formats for API Gateway
<a name="apigateway-kinesis-log-formats"></a>

Firehose logging uses the same format as [CloudWatch logging](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html).

## Permissions for Firehose logging
<a name="set-up-kinesis-access-logging-permissions"></a>

When Firehose access logging is enabled on a stage, API Gateway creates a service-linked role in your account if the role doesn't exist already. The role is named `AWSServiceRoleForAPIGateway` and has the `APIGatewayServiceRolePolicy` managed policy attached to it. For more information about service-linked roles, see [Using Service-Linked Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

**Note**  
The name of your Firehose stream must be `amazon-apigateway-{{{your-stream-name}}}`.

## Set up Firehose access logging by using the API Gateway console
<a name="set-up-kinesis-access-logging-using-console"></a>

To set up API logging, you must have deployed the API to a stage. You must also have created a Firehose stream. 

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1.  Do one of the following:

   1.  Choose an existing API, and then choose a stage.

   1.  Create an API and deploy it to a stage.

1. In the main navigation pane, choose **Stages**.

1.  In the **Logs and tracing** section, choose **Edit**.

1. To enable access logging to a Firehose stream:

   1. Turn on **Custom access logging**.

   1. For **Access log destination ARN**, enter the ARN of a Firehose stream. The ARN format is `arn:aws:firehose:{{{region}}}:{{{account-id}}}:deliverystream/amazon-apigateway-{{{your-stream-name}}}`.
**Note**  
The name of your Firehose stream must be `amazon-apigateway-{{{your-stream-name}}}`.

   1. For **Log format**, enter a log format. You can choose **CLF**, **JSON**, **XML**, or **CSV**. To learn more about example log formats, see [CloudWatch log formats for API Gateway](set-up-logging.md#apigateway-cloudwatch-log-formats).

1. Choose **Save changes**.

API Gateway is now ready to log requests to your API to Firehose. You don't need to redeploy the API when you update the stage settings, logs, or stage variables. 