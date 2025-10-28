# Troubleshoot custom identity provider issues

This section describes possible solutions for issues related to custom identity
providers with Transfer Family.

###### Topics

- [Troubleshoot API Gateway integration
  errors](#api-gateway-errors "#api-gateway-errors")
- [Troubleshoot Lambda function
  timeouts](#lambda-timeout-issues "#lambda-timeout-issues")
- [Troubleshoot consistent Lambda timeout
  issues](#lambda-timeout-auth "#lambda-timeout-auth")
- [Troubleshoot KeyError exceptions](#keyerror-logs "#keyerror-logs")

## Troubleshoot API Gateway integration

errors

Description

Users cannot authenticate with your Transfer Family server, and when testing your identity
provider, you see errors such as:

```
{
    "Response": "",
    "StatusCode": 500,
    "Message": "Internal server error"
}
```

Cause

API Gateway integration errors can occur due to:

- Incorrect API Gateway configuration
- Lambda function errors not being properly handled
- Permission issues between API Gateway and Lambda
- Malformed responses from the Lambda function

Solution

To troubleshoot API Gateway integration errors:

1. Check your Lambda function logs for detailed error information:
   - In the CloudWatch console, navigate to **Log groups** >
     **/aws/lambda/your-function-name**
   - Look for error messages or stack traces that indicate the root
     cause

2. Verify that your Lambda function returns properly formatted
   responses:

```
{
    "Role": "arn:aws:iam::123456789012:role/TransferUserRole",
    "HomeDirectory": "/mybucket/home/username"
}
```

3. Enable detailed CloudWatch logging for API Gateway:
   - In the API Gateway console, select your API and choose
     **Stages**
   - Select your stage and under **Logs/Tracing**,
     enable **CloudWatch Logs**
   - Set the log level to **ERROR** or
     **INFO**

4. Test your API Gateway endpoint directly:

```
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/prod/servers/your-server-id/users/username/config \
    -H "Content-Type: application/json" \
    -d '{"Password": "password"}'
```

5. Verify permissions between API Gateway and Lambda:
   - Ensure API Gateway has permission to invoke your Lambda
     function
   - Check that the execution role for your Lambda function has
     necessary permissions

## Troubleshoot Lambda function

timeouts

Description

When users attempt to authenticate with your Transfer Family server using a custom identity
provider, they experience long delays followed by authentication failures. In your
Lambda logs, you see timeout errors.

Cause

Lambda functions used for custom identity providers have a default timeout of 3
seconds. If your authentication logic takes longer than this timeout (for example,
when querying external databases or making API calls to third-party identity
providers), the function will time out and authentication will fail.

Solution

To resolve Lambda timeout issues:

1. Increase the Lambda function timeout:
   - In the Lambda console, navigate to your function and select the
     **Configuration** tab
   - Under **General configuration**, click
     **Edit**
   - Increase the timeout value (up to 15 seconds is recommended for
     authentication functions)

2. Optimize your Lambda function code:
   - Use connection pooling for database queries
   - Implement caching for frequently accessed data
   - Minimize external API calls during authentication

3. Consider using Lambda Provisioned Concurrency to eliminate cold
   starts:

```
aws lambda put-provisioned-concurrency-config \
    --function-name my-authentication-function \
    --qualifier prod \
    --provisioned-concurrent-executions 5
```

4. Monitor Lambda performance using CloudWatch metrics and set up alarms for
   duration thresholds

## Troubleshoot consistent Lambda timeout

issues

Description

Users experience consistent timeouts when using a Lambda function for authentication.

Cause

Lambda can’t reach the corresponding AWS service used to authenticate (such as DynamoDB, Secrets Manager, or other identity provider).

Solution

Verify that subnets can reach AWS services. Or, if connecting to an internet identity provider (such as Okta), verify that the Lambda function’s subnet can reach the internet via a NAT Gateway

## Troubleshoot `KeyError` exceptions

Description

In your Transfer Family log entries, you notice ‘KeyError’ exceptions.

Cause

The most likely cause is that user or `identity_provider` record is malformed or missing required fields.

Solution

Review the `ERRORS` log, located in `/aws/transfer/`your-server-id`` log group for clues.
