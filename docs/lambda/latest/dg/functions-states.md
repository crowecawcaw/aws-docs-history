# Lambda function states

Lambda includes a [State](../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State "../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State") field in the function configuration for all
functions to indicate when your function is ready to invoke. `State` provides information about the current status of the function, including whether you can successfully invoke the function. Function
states do not change the behavior of function invocations or how your function runs the code.

###### Note

Function state definitions differ slightly for [SnapStart](snapstart.md "snapstart.md") functions. For more information, see [Lambda SnapStart and function states](snapstart-activate.md#snapstart-function-states "snapstart-activate.md#snapstart-function-states").

In many cases, a DynamoDB table is an ideal way to retain state between invocations since it provides low-latency data access and can scale
with the Lambda service. You can also store data in
[Amazon EFS for Lambda](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/ "https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/") if you are using this service, and this provides low-latency access to file system storage.

Function states include:

- `Pending` – After Lambda creates the function, it sets the state to pending. While in pending state, Lambda attempts to create or configure resources for the function, such as VPC or EFS resources.
  Lambda does not invoke a function during pending state. Any invocations or other API actions that operate on the function will fail.
- `Active` – Your function transitions to active state after Lambda completes resource configuration and provisioning.
  Functions can only be successfully invoked while active.
- `Failed` – Indicates that resource configuration or provisioning encountered an error.
- `Inactive` – A function becomes inactive when it has been idle
  long enough for Lambda to reclaim the external resources that were configured for it.
  When you try to invoke a function that is inactive, the invocation fails and Lambda
  sets the function to pending state until the function resources are recreated.
  If Lambda fails to recreate the resources, the function returns to the inactive state.
  You might need to resolve any errors and redeploy your function to
  restore it to the active state.
  If you are using SDK-based automation workflows or calling Lambda’s service APIs directly, ensure that you check a function's state before invocation to verify that it is active.
  You can do this with the Lambda API action [GetFunction](../api/API_GetFunction.md "../api/API_GetFunction.md"), or by configuring a waiter using the
  [AWS SDK for Java 2.0](https://github.com/aws/aws-sdk-java-v2 "https://github.com/aws/aws-sdk-java-v2").

```
`aws lambda get-function --function-name my-function --query 'Configuration.[State, LastUpdateStatus]'`
```

You should see the following output:

```
[
 "Active",
 "Successful"
]
```

The following operations fail while function creation is pending:

- [Invoke](../api/API_Invoke.md "../api/API_Invoke.md")
- [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md")
- [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md")
- [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md")

## Function states during updates

Lambda has two operations for updating functions:

- [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md"): Updates the function's deployment package
- [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md"): Updates the function's configuration

Lambda uses the [LastUpdateStatus](../api/API_FunctionConfiguration.md#lambda-Type-FunctionConfiguration-LastUpdateStatus "../api/API_FunctionConfiguration.md#lambda-Type-FunctionConfiguration-LastUpdateStatus") attribute to track the progress of these update operations. While an update is in progress (when `"LastUpdateStatus": "InProgress"`):

- The function's [State](../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State "../api/API_GetFunctionConfiguration.md#lambda-GetFunctionConfiguration-response-State") remains `Active`.
- Invocations continue to use the function's previous code and configuration until the update completes.
- The following operations fail:
  - [UpdateFunctionCode](../api/API_UpdateFunctionCode.md "../api/API_UpdateFunctionCode.md")
  - [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md")
  - [PublishVersion](../api/API_PublishVersion.md "../api/API_PublishVersion.md")
  - [TagResource](../api/API_TagResource.md "../api/API_TagResource.md")

###### Example GetFunctionConfiguration response

The following example is the result of [GetFunctionConfiguration](../api/API_GetFunctionConfiguration.md "../api/API_GetFunctionConfiguration.md") request on a function undergoing an update.

```
{
    "FunctionName": "my-function",
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function",
    "Runtime": "nodejs24.x",
    "VpcConfig": {
        "SubnetIds": [
            "subnet-071f712345678e7c8",
            "subnet-07fd123456788a036",
            "subnet-0804f77612345cacf"
        ],
        "SecurityGroupIds": [
            "sg-085912345678492fb"
        ],
        "VpcId": "vpc-08e1234569e011e83"
    },
    `"State": "Active",
 "LastUpdateStatus": "InProgress"`,
    ...
}
```
