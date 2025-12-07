# Enabling tenant isolation for Lambda functions

To activate tenant isolation mode, create a new Lambda function. You cannot enable tenant isolation on existing functions.

###### Topics

- [Enabling tenant isolation (console)](#tenant-isolation-console "#tenant-isolation-console")
- [Enabling tenant isolation (AWS CLI)](#tenant-isolation-cli "#tenant-isolation-cli")
- [Enabling tenant isolation (API)](#tenant-isolation-api "#tenant-isolation-api")
- [Enabling tenant isolation (CloudFormation)](#tenant-isolation-cfn "#tenant-isolation-cfn")

## Enabling tenant isolation (console)

###### To create a Lambda function using the console

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose **Create function**.
3. Select **Author from scratch**.
4. In the **Basic information** pane, for **Function name**, enter
   `image-analysis`.
5. For **Runtime**, choose any of the [supported Lambda runtimes](lambda-runtimes.md#runtimes-supported "lambda-runtimes.md#runtimes-supported").
6. Under additional configurations, **Tenant isolation mode**,
   select **Enable**.
7. Review your settings, and choose **Create function**.

## Enabling tenant isolation (AWS CLI)

**Create function with tenant isolation**

When creating a new function using the CLI, add the `--tenancy-config
 '{"TenantIsolationMode": "PER_TENANT"}'` option to your [create-function](../../../cli/latest/reference/lambda/create-function.md "../../../cli/latest/reference/lambda/create-function.md") request. Example:

```
`aws lambda create-function \
 --function-name `image-analysis` \
 --runtime `nodejs24.x` \
 --zip-file fileb://image-analysis-function.zip \
 --handler image-analysis-function.handler \
 --role `arn:aws:iam:123456789012:role/execution-role` \
 --tenancy-config '{"TenantIsolationMode": "PER_TENANT"}'`
```

## Enabling tenant isolation (API)

###### To enable tenant isolation using the Lambda API

1. Create a new function with tenant isolation enabled by using the [CreateFunction](../api/API_CreateFunction.md "../api/API_CreateFunction.md") API action with the `TenancyConfig` parameter.
2. Confirm that tenant isolation is enabled for the function by using the [GetFunctionConfiguration](../api/API_GetFunctionConfiguration.md "../api/API_GetFunctionConfiguration.md") action. If the response shows that `TenantIsolationMode` is `PER_TENANT`, then tenant isolation is enabled for the function:

```
"TenancyConfig": {
        "TenantIsolationMode": "PER_TENANT"
     }
```

Invoke the function version with the [Invoke](../api/API_Invoke.md "../api/API_Invoke.md") action. For more information, see [Invoking Lambda functions with tenant isolation](tenant-isolation-invoke.md "tenant-isolation-invoke.md").

## Enabling tenant isolation (CloudFormation)

The following CloudFormation template creates a new Lambda function with tenant isolation enabled:

```
`MyLambdaFunction:
 Type: AWS::Lambda::Function
 Properties:
 FunctionName: `my-sample-python-lambda`
 Runtime: `python3.14`
 Role: !GetAtt LambdaExecutionRole.Arn
 Handler: index.lambda_handler
 TenancyConfig:
 TenantIsolationMode: PER_TENANT
 Code:
 ZipFile: |
 import json

 def lambda_handler(event, context):
 return {
 'statusCode': `200`,
 'body': json.dumps(f'Hello from Lambda! Tenant-ID: {context.tenant_id}')
 }
 Timeout: `10`
 MemorySize: `128``
```
