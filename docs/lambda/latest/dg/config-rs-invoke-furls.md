# Invoking a response streaming enabled function using Lambda function URLs

###### Note

You must invoke your function using a function URL to stream the responses.

You can invoke response streaming enabled functions by changing the invoke mode of your
function's URL. The invoke mode determines which API operation Lambda uses to invoke your
function. The available invoke modes are:

- `BUFFERED` – This is the default option. Lambda invokes your function
  using the `Invoke` API operation. Invocation results are available when the
  payload is complete. The maximum payload size is 6 MB.
- `RESPONSE_STREAM` – Enables your function to stream payload results
  as they become available. Lambda invokes your function using the
  `InvokeWithResponseStream` API operation. The maximum response payload size
  is 200 MB.
  You can still invoke your function without response streaming by directly calling the
  `Invoke` API operation. However, Lambda streams all response payloads for
  invocations that come through the function's URL until you change the invoke mode to
  `BUFFERED`.

Console

###### To set the invoke mode of a function URL (console)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose the name of the function that you want to set the invoke mode for.
3. Choose the **Configuration** tab, and then choose **Function
   URL**.
4. Choose **Edit**, then choose **Additional
   settings**.
5. Under **Invoke mode**, choose your desired invoke mode.
6. Choose **Save**.

AWS CLI
**To set the invoke mode of a function's URL (AWS CLI)**

```
aws lambda update-function-url-config \
  --function-name `my-function` \
  --invoke-mode RESPONSE_STREAM
```

AWS CloudFormation
**To set the invoke mode of a function's URL (AWS CloudFormation)**

```
MyFunctionUrl:
  Type: AWS::Lambda::Url
  Properties:
    AuthType: AWS_IAM
    InvokeMode: RESPONSE_STREAM
```

For more information about configuring function URLs, see [Lambda function URLs](urls-configuration.md "urls-configuration.md").
