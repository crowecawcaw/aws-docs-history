# Invoke an AWS Lambda function with Step Functions

Learn how to use Step Functions to invoke Lambda functions either synchronously or asynchronously as part of an event-driven serverless application.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized Lambda integration

- The `Payload` field of the response is parsed from escaped Json to
  Json.
- If an exception is raised within the Lambda function, the Task will fail. For a
  practical example, see [Handling error conditions in a Step Functions
  state machine](tutorial-handling-error-conditions.md "tutorial-handling-error-conditions.md").

## Optimized Lambda APIs

- [`Invoke`](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md")

## Workflow Examples

The following includes a `Task` state that invokes a Lambda function.

```
{
   "StartAt":"CallLambda",
   "States":{
      "CallLambda":{
         "Type":"Task",
         "Resource":"arn:aws:states:::lambda:invoke",
         "Arguments":{
            "FunctionName":"arn:aws:lambda:`region`:`account-id`:function:`MyFunction`"
         },
         "End":true
      }
   }
}
```

The following includes a `Task` state that implements the [callback](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token") service integration pattern.

```
{
   "StartAt":"GetManualReview",
   "States":{
      "GetManualReview":{
         "Type":"Task",
         "Resource":"arn:aws:states:::lambda:invoke**.waitForTaskToken**",
         "Arguments":{
            "FunctionName":"arn:aws:lambda:`region`:`account-id`:function:`get-model-review-decision`",
            "Payload":{
               "model":"{% $states.input.my-model %}",
               "TaskToken": "{% $states.context.Task.Token %}"
            },
            "Qualifier":"prod-v1"
         },
         "End":true
      }
   }
}

```

When you invoke a Lambda function, the execution will wait for the function to complete. If you invoke the Lambda function with a callback task, the heartbeat timeout
does not start counting until after the Lambda function has completed executing and returned a result. As long as the Lambda function executes, the heartbeat
timeout is not enforced.

It is also possible to call Lambda asynchronously using the `InvocationType` parameter, as seen in the following example:

```
{

  "Comment": "A Hello World example of the Amazon States Language using Pass states",
  "StartAt": "Hello",
  "States": {
    "Hello": {
      "Type": "Task",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Arguments": {
        "FunctionName": "arn:aws:lambda:`region`:`account-id`:function:`echo`",
        "InvocationType": "Event"
      },
      "End": true
    }
  }
}

```

###### Note

For asynchronous invocations of Lambda functions, the heartbeat timeout period starts immediately.

When the `Task` result is returned, the function output is nested inside a dictionary of metadata.
For example:

```
{

   "ExecutedVersion":"$LATEST",
   "Payload":"`FUNCTION OUTPUT`",
   "SdkHttpMetadata":{
      "HttpHeaders":{
         "Connection":"keep-alive",
         "Content-Length":"4",
         "Content-Type":"application/json",
         "Date":"Fri, 26 Mar 2021 07:42:02 GMT",
         "X-Amz-Executed-Version":"$LATEST",
         "x-amzn-Remapped-Content-Length":"0",
         "x-amzn-RequestId":"0101aa0101-1111-111a-aa55-1010aaa1010",
         "X-Amzn-Trace-Id":"root=1-1a1a000a2a2-fe0101aa10ab;sampled=0"
      },
      "HttpStatusCode":200
   },
   "SdkResponseMetadata":{
      "RequestId":"6b3bebdb-9251-453a-ae45-512d9e2bf4d3"
   },
   "StatusCode":200
}
```

## Directly specified function resource

Alternatively, you can invoke a Lambda function by specifying a function ARN directly in the "Resource" field. When you invoke a Lambda function in this way, you can't specify `.waitForTaskToken`, and the task result contains only the function output.

```
{
   "StartAt":"CallFunction",
   "States":{
      "CallFunction": {
         "Type":"Task",
         "Resource":"arn:aws:lambda:`region`:`account-id`:function:`HelloFunction`",
         "End": true
      }
   }
}
```

With this form of integration, the function could succeed yet send a response that contains a `FunctionError` field. In that scenario, the workflow Task will fail.

You can invoke a specific Lambda function version or alias by specifying those options
in the ARN in the `Resource` field. See the following in the Lambda
documentation:

- [AWS Lambda
  versioning](../../../lambda/latest/dg/versioning-intro.md "../../../lambda/latest/dg/versioning-intro.md")
- [AWS Lambda aliases](../../../lambda/latest/dg/aliases-intro.md "../../../lambda/latest/dg/aliases-intro.md")

## IAM policies for calling AWS Lambda

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

In the following example, a state machine with two AWS Lambda task states which call `function1` and `function2`, the autogenerated policy includes `lambda:Invoke` permission for both functions.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": [
 "arn:aws:lambda:`us-east-1`:`123456789012`:function:myFn1",
 "arn:aws:lambda:`us-east-1`:`123456789012`:function:myFn2"
 ]
 }
 ]
}`

```
