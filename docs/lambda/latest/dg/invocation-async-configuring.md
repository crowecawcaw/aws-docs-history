# Configuring error handling settings for Lambda asynchronous invocations

Use the following settings to configure how Lambda handles errors and retries for asynchronous function invocations:

- [MaximumEventAgeInSeconds](../api/API_PutFunctionEventInvokeConfig.md#lambda-PutFunctionEventInvokeConfig-request-MaximumEventAgeInSeconds "../api/API_PutFunctionEventInvokeConfig.md#lambda-PutFunctionEventInvokeConfig-request-MaximumEventAgeInSeconds"): The maximum amount of time, in seconds, that Lambda keeps an event in the asynchronous event queue before discarding it.
- [MaximumRetryAttempts](../api/API_PutFunctionEventInvokeConfig.md#lambda-PutFunctionEventInvokeConfig-request-MaximumRetryAttempts "../api/API_PutFunctionEventInvokeConfig.md#lambda-PutFunctionEventInvokeConfig-request-MaximumRetryAttempts"): The maximum number of times that Lambda retries events when the function returns an error.
  Use the Lambda console or AWS CLI to configure error handling settings on a function, a version, or an alias.

Console

###### To configure error handling

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose a function.
3. Choose **Configuration** and then choose **Asynchronous
   invocation**.
4. Under **Asynchronous invocation**, choose **Edit**.
5. Configure the following settings.
   - **Maximum age of event** – The maximum amount of time Lambda retains an event
     in the asynchronous event queue, up to 6 hours.
   - **Retry attempts** – The number of times Lambda retries when the function
     returns an error, between 0 and 2.

6. Choose **Save**.

AWS CLI
To configure asynchronous invocation with the AWS CLI, use the [put-function-event-invoke-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-event-invoke-config.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/put-function-event-invoke-config.html") command. The following example configures a function with a maximum event age of 1 hour and no retries.

```
aws lambda put-function-event-invoke-config \
  --function-name error \
  --maximum-event-age-in-seconds `3600` \
  --maximum-retry-attempts `0`
```

The `put-function-event-invoke-config` command overwrites any existing configuration on the function, version, or alias. To configure an option without resetting others, use [update-function-event-invoke-config](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-event-invoke-config.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-event-invoke-config.html"). The following example configures Lambda to send a record to a standard
SQS queue named `destination` when an event can't be processed.

```
aws lambda update-function-event-invoke-config \
  --function-name my-function \
  --destination-config '{"OnFailure":{"Destination": "`arn:aws:sqs:us-east-1:123456789012:``destination`"}}'
```

You should see the following output:

```
{
    "LastModified": 1573686021.479,
    "FunctionArn": "arn:aws:lambda:us-east-1:123456789012:function:my-function:$LATEST",
    "MaximumRetryAttempts": 0,
    "MaximumEventAgeInSeconds": 3600,
    "DestinationConfig": {
        "OnSuccess": {},
        "OnFailure": {}
    }
}
```

When an invocation event exceeds the maximum age or fails all retry attempts, Lambda discards it. To retain a
copy of discarded events, configure a failed-event [destination](invocation-async-retain-records.md#invocation-async-destinations "invocation-async-retain-records.md#invocation-async-destinations").
