# FunctionUrlConfig

Creates an AWS Lambda function URL with the specified configuration parameters. A Lambda
function URL is an HTTPS endpoint that you can use to invoke your function.

By default, the function URL that you create uses the `$LATEST` version of your
Lambda function. If you specify an `AutoPublishAlias` for your Lambda function, the
endpoint connects to the specified function alias.

For more information, see [Lambda function URLs](../../../lambda/latest/dg/lambda-urls.md "../../../lambda/latest/dg/lambda-urls.md") in the _AWS Lambda Developer Guide_.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
AuthType: `String`
Cors: `Cors`
InvokeMode: `String`
```

## Properties

`AuthType`

The type of authorization for your function URL. To use AWS Identity and Access Management (IAM) to
authorize requests, set to `AWS_IAM`. For open access, set to
`NONE`.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`AuthType` property of an `AWS::Lambda::Url`
resource.

`Cors`

The cross-origin resource sharing (CORS) settings for your function URL.

_Type_: [Cors](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-url-cors.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Cors` property of an `AWS::Lambda::Url` resource.

`InvokeMode`

The mode that your function URL will be invoked. To have your function return the
response after invocation completes, set to `BUFFERED`. To have your function
stream the response, set to `RESPONSE_STREAM`. The default value is
`BUFFERED`.

_Valid values_: `BUFFERED` or
`RESPONSE_STREAM`

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed
directly to the [`InvokeMode`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.md#cfn-lambda-url-invokemode "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-url.md#cfn-lambda-url-invokemode") property of an `AWS::Lambda::Url` resource.

## Examples

### Function

URL

The following example creates a Lambda function with a function URL. The function URL uses
IAM authorization.

#### YAML

```
HelloWorldFunction:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: hello_world/
    Handler: index.handler
    Runtime: nodejs20.x
    FunctionUrlConfig:
      AuthType: AWS_IAM
      InvokeMode: RESPONSE_STREAM

Outputs:
  MyFunctionUrlEndpoint:
      Description: "My Lambda Function URL Endpoint"
      Value:
        Fn::GetAtt: HelloWorldFunctionUrl.FunctionUrl

```
