

# Set up CloudWatch logging for REST APIs in API Gateway
<a name="set-up-logging"></a>

To help debug issues related to request execution or client access to your API, you can enable Amazon CloudWatch Logs to log API calls. For more information about CloudWatch, see [Monitor REST API execution with Amazon CloudWatch metrics](monitoring-cloudwatch.md).

There are two types of API logging in CloudWatch:
+ **Execution logging** – API Gateway logs the actions taken to process API requests, including errors and execution traces. You can also configure Amazon CloudWatch Logs delivery to route execution logs to your own destinations.
+ **Access logging** – You log who accessed your API and how. You create your own log group, choose a log format, and specify which `$context` variables to include.

You can enable execution logging and access logging independently of each other.

## Permissions for CloudWatch logging
<a name="set-up-access-logging-permissions"></a>

To enable CloudWatch Logs, you must grant API Gateway permission to read and write logs to CloudWatch for your account. The [AmazonAPIGatewayPushToCloudWatchLogs](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAPIGatewayPushToCloudWatchLogs.html) managed policy has all the required permissions.

**Note**  
API Gateway calls AWS Security Token Service in order to assume the IAM role, so make sure that AWS STS is enabled for the Region. For more information, see [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html).

To grant these permissions to your account, create an IAM role with `apigateway.amazonaws.com` as its trusted entity, attach the preceding policy to the IAM role, and set the IAM role ARN on the [cloudWatchRoleArn](https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateAccount.html#cloudWatchRoleArn) property on your [Account](https://docs.aws.amazon.com/apigateway/latest/api/API_GetAccount.html). You must set the [cloudWatchRoleArn](https://docs.aws.amazon.com/apigateway/latest/api/API_UpdateAccount.html#cloudWatchRoleArn) property separately for each AWS Region in which you want to enable CloudWatch Logs.

If you receive an error when setting the IAM role ARN, check your AWS Security Token Service account settings to make sure that AWS STS is enabled in the Region that you're using. For more information about enabling AWS STS, see [Managing AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate) in the *IAM User Guide*.

**Topics**
+ [Permissions for CloudWatch logging](#set-up-access-logging-permissions)
+ [Execution logging for REST APIs](rest-api-execution-logging.md)
+ [Access logging for REST APIs](set-up-access-logging.md)