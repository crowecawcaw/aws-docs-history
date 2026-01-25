# Use Lambda functions as targets of an Application Load Balancer

You can register your Lambda functions as targets and configure a listener rule to
forward requests to the target group for your Lambda function. When the load balancer
forwards the request to a target group with a Lambda function as a target, it invokes
your Lambda function and passes the content of the request to the Lambda function, in
JSON format.

The load balancer invokes the Lambda function directly instead of using a
network connection. Therefore, there are no requirements for the outbound rules of
the Application Load Balancer security groups.

###### Limits

- The Lambda function and target group must be in the same account and in the
  same Region.
- The maximum size of the request body that you can send to a Lambda function is
  1 MB. For related size limits, see [HTTP header limits](../userguide/how-elastic-load-balancing-works.md#http-header-limits "../userguide/how-elastic-load-balancing-works.md#http-header-limits").
- The maximum size of the response JSON that the Lambda function can send is 1
  MB.
- WebSockets are not supported. Upgrade requests are rejected with an HTTP 400
  code.
- Local Zones are not supported.
- Automatic Target Weights (ATW) is not supported.

###### Contents

- [Prepare the Lambda function](#prepare-lambda-function "#prepare-lambda-function")
- [Create a target group for the Lambda function](#create-lambda-target-group "#create-lambda-target-group")
- [Receive events from the load
  balancer](#receive-event-from-load-balancer "#receive-event-from-load-balancer")
- [Respond to the load balancer](#respond-to-load-balancer "#respond-to-load-balancer")
- [Multi-value headers](#multi-value-headers "#multi-value-headers")
- [Enable health checks](#enable-health-checks-lambda "#enable-health-checks-lambda")
- [Register the Lambda function](#register-lambda-function "#register-lambda-function")
- [Deregister the Lambda function](#deregister-lambda-function "#deregister-lambda-function")
  For a demo, see [Lambda
  target on Application Load Balancer](https://exampleloadbalancer.com/lambda_demo.html "https://exampleloadbalancer.com/lambda_demo.html").

## Prepare the Lambda function

The following recommendations apply if you are using your Lambda function with an
Application Load Balancer.

###### Permissions to invoke the Lambda function

If you create the target group and register the Lambda function using the
AWS Management Console, the console adds the required permissions to your Lambda function
policy on your behalf. Otherwise, after you create the target group and register
the function using the AWS CLI, you must use the [add-permission](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md") command
to grant Elastic Load Balancing permission to invoke your Lambda function. We recommend that you
use the `aws:SourceAccount` and `aws:SourceArn` condition
keys to restrict function invocation to the specified target group. For more
information, see [The confused deputy
problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _IAM User Guide_,

```
aws lambda add-permission \
    --function-name `lambda-function-arn-with-alias-name` \
    --statement-id `elb1` \
    --principal elasticloadbalancing.amazonaws.com \
    --action lambda:InvokeFunction \
    --source-arn `target-group-arn` \
    --source-account `target-group-account-id`
```

###### Lambda function versioning

You can register one Lambda function per target group. To ensure that you can
change your Lambda function and that the load balancer always invokes the
current version of the Lambda function, create a function alias and include the
alias in the function ARN when you register the Lambda function with the load
balancer. For more information, see [AWS Lambda function aliases](../../../lambda/latest/dg/configuration-aliases.md "../../../lambda/latest/dg/configuration-aliases.md")
in the _AWS Lambda Developer Guide_.

###### Function timeout

The load balancer waits until your Lambda function responds or times out. We
recommend that you configure the timeout of the Lambda function based on your
expected run time. For information about the default timeout value and how to
change it, see [Configure Lambda
function timeout](../../../lambda/latest/dg/configuration-timeout.md "../../../lambda/latest/dg/configuration-timeout.md"). For information about the maximum timeout
value that you can configure, see [AWS Lambda
quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md").

## Create a target group for the Lambda function

Create a target group, which is used in request routing. If the request content
matches a listener rule with an action to forward it to this target group, the load
balancer invokes the registered Lambda function.

Console

###### To create a target group and register the Lambda function

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose **Create target group**.
4. For **Choose a target type**, select
   **Lambda function**.
5. For **Target group name**, enter a name for
   the target group.
6. (Optional) To enable health checks, choose
   **Enable** in the **Health
   checks** section.
7. (Optional) Expand **Tags**. For each tag, choose
   **Add new tag** and enter a tag key and a tag value.
8. Choose **Next**.
9. If you are ready to register the Lambda function, choose
   **Select a Lambda function** and choose the Lambda function
   from the list, or choose **Enter a Lambda function ARN**
   and enter the ARN of the Lambda function,

If you are not ready to register the Lambda function, choose
**Register Lambda function later** and register the
target later on. For more information, see [Register targets](target-group-register-targets.md#register-targets "target-group-register-targets.md#register-targets"). 10. Choose **Create target group**.

AWS CLI

###### To create a target group of type lambda

Use the [create-target-group](../../../cli/latest/reference/elbv2/create-target-group.md "../../../cli/latest/reference/elbv2/create-target-group.md") command.

```
aws elbv2 create-target-group \
    --name `my-target-group` \
    --target-type lambda
```

###### To register the Lambda function

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`lambda-function-arn`
```

CloudFormation

###### To create a target group and register the Lambda function

Define a resource of type [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md").
If you aren't ready to register the Lambda function now, you
can omit the `Targets` property and add it later on.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: `my-target-group`
      TargetType: lambda
      Tags:
        - Key: '`department`'
          Value: '`123`'
      Targets:
        - Id: !Ref myLambdaFunction
```

## Receive events from the load

balancer

The load balancer supports Lambda invocation for requests over both HTTP and
HTTPS. The load balancer sends an event in JSON format. The load balancer adds the
following headers to every request: `X-Amzn-Trace-Id`,
`X-Forwarded-For`, `X-Forwarded-Port`, and
`X-Forwarded-Proto`.

If the `content-encoding` header is present, the load balancer Base64
encodes the body and sets `isBase64Encoded` to `true`.

If the `content-encoding` header is not present, Base64 encoding
depends on the content type. For the following types, the load balancer sends the
body as is and sets `isBase64Encoded` to `false`: text/\*,
application/json, application/javascript, and application/xml. Otherwise, the load
balancer Base64 encodes the body and sets `isBase64Encoded` to
`true`.

The following is an example event.

```
{
    "requestContext": {
        "elb": {
            "targetGroupArn": "arn:aws:elasticloadbalancing:`region`:`123456789012`:targetgroup/`my-target-group`/`6d0ecf831eec9f09`"
        }
    },
    "httpMethod": "GET",
    "path": "/",
    "queryStringParameters": {`parameters`},
    "headers": {
        "accept": "text/html,application/xhtml+xml",
        "accept-language": "`en-US`,en;q=0.8",
        "content-type": "text/plain",
        "cookie": "`cookies`",
        "host": "`lambda-846800462-us-east-2.elb.amazonaws.com`",
        "user-agent": "`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)`",
        "x-amzn-trace-id": "`Root=1-5bdb40ca-556d8b0c50dc66f0511bf520`",
        "x-forwarded-for": "`72.21.198.66`",
        "x-forwarded-port": "`443`",
        "x-forwarded-proto": "`https`"
    },
    "isBase64Encoded": `false`,
    "body": "`request_body`"
}

```

## Respond to the load balancer

The response from your Lambda function must include the Base64 encoding status,
status code, and headers. You can omit the body.

To include a binary content in the body of the response, you must Base64 encode
the content and set `isBase64Encoded` to `true`. The load
balancer decodes the content to retrieve the binary content and sends it to the
client in the body of the HTTP response.

The load balancer does not honor hop-by-hop headers, such as
`Connection` or `Transfer-Encoding`. You can omit the
`Content-Length` header because the load balancer computes it before
sending responses to clients.

The following is an example response from a **nodejs** based Lambda function.

```
{
    "isBase64Encoded": `false`,
    "statusCode": `200`,
    "statusDescription": "`200 OK`",
    "headers": {
        "Set-cookie": "`cookies`",
        "Content-Type": "application/json"
    },
    "body": "Hello from Lambda (optional)"
}
```

For Lambda function templates that work with Application Load Balancers, see [application-load-balancer-serverless-app](https://github.com/aws/elastic-load-balancing-tools/tree/master/application-load-balancer-serverless-app "https://github.com/aws/elastic-load-balancing-tools/tree/master/application-load-balancer-serverless-app") on github. Alternatively, open the [Lambda console](https://console.aws.amazon.com/lambda "https://console.aws.amazon.com/lambda"), choose **Applications**, **Create a
application**, and select one of the following from the AWS Serverless Application Repository:

- ALB-Lambda-Target-UploadFiletoS3
- ALB-Lambda-Target-BinaryResponse
- ALB-Lambda-Target-WhatisMyIP

## Multi-value headers

If requests from a client or responses from a Lambda function contain headers with
multiple values or contains the same header multiple times, or query parameters with
multiple values for the same key, you can enable support for multi-value header
syntax. After you enable multi-value headers, the headers and query parameters
exchanged between the load balancer and the Lambda function use arrays instead of
strings. If you do not enable multi-value header syntax and a header or query
parameter has multiple values, the load balancer uses the last value that it
receives.

###### Contents

- [Requests with multi-value
  headers](#multi-value-headers-request "#multi-value-headers-request")
- [Responses with multi-value
  headers](#multi-value-headers-response "#multi-value-headers-response")
- [Enable multi-value headers](#enable-multi-value-headers "#enable-multi-value-headers")

### Requests with multi-value

headers

The names of the fields used for headers and query string parameters differ
depending on whether you enable multi-value headers for the target group.

The following example request has two query parameters with the same
key:

```
http://www.example.com?&myKey=val1&myKey=val2
```

With the default format, the load balancer uses the last value sent by the
client and sends you an event that includes query string parameters using
`queryStringParameters`. For example:

```
"queryStringParameters": { "myKey": "val2"},
```

If you enable multi-value headers, the load balancer uses both key values sent
by the client and sends you an event that includes query string parameters using
`multiValueQueryStringParameters`. For example:

```
"multiValueQueryStringParameters": { "myKey": ["val1", "val2"] },
```

Similarly, suppose that the client sends a request with two cookies in the
header:

```
"cookie": "name1=value1",
"cookie": "name2=value2",
```

With the default format, the load balancer uses the last cookie sent by the
client and sends you an event that includes headers using `headers`.
For example:

```
"headers": {
    "cookie": "name2=value2",
    ...
},
```

If you enable multi-value headers, the load balancer uses both cookies sent by
the client and sends you an event that includes headers using
`multiValueHeaders`. For example:

```
"multiValueHeaders": {
    "cookie": ["name1=value1", "name2=value2"],
    ...
},
```

If the query parameters are URL-encoded, the load balancer does not decode
them. You must decode them in your Lambda function.

### Responses with multi-value

headers

The names of the fields used for headers differ depending on whether you
enable multi-value headers for the target group. You must use
`multiValueHeaders` if you have enabled multi-value headers and
`headers` otherwise.

With the default format, you can specify a single cookie:

```
{
  "headers": {
      "Set-cookie": "cookie-name=cookie-value;Domain=myweb.com;Secure;HttpOnly",
      "Content-Type": "application/json"
  },
}
```

If you enable multi-value headers, you must specify multiple cookies as
follows:

```
{
  "multiValueHeaders": {
      "Set-cookie": ["cookie-name=cookie-value;Domain=myweb.com;Secure;HttpOnly","cookie-name=cookie-value;Expires=May 8, 2019"],
      "Content-Type": ["application/json"]
  },
}
```

The load balancer might send the headers to the client in a different order
than the order specified in the Lambda response payload. Therefore, do not count
on headers being returned in a specific order.

### Enable multi-value headers

You can enable or disable multi-value headers for a target group with the
target type `lambda`.

Console

###### To enable multi-value headers

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Attributes** tab, choose
   **Edit**.
5. Enable **Multi value headers**.
6. Choose **Save changes**.

AWS CLI

###### To enable multi-value headers

Use the [modify-target-group-attributes](../../../cli/latest/reference/elbv2/modify-target-group-attributes.md "../../../cli/latest/reference/elbv2/modify-target-group-attributes.md") command with the
`lambda.multi_value_headers.enabled` attribute.

```
aws elbv2 modify-target-group-attributes \
    --target-group-arn `target-group-arn` \
    --attributes "Key=lambda.multi_value_headers.enabled,Value=true"
```

CloudFormation

###### To enable multi-value headers

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource
to include the `lambda.multi_value_headers.enabled`
attribute.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      TargetType: lambda
      Tags:
        - Key: 'department'
          Value: '123'
      Targets:
        - Id: !Ref myLambdaFunction
      TargetGroupAttributes:
        - Key: "lambda.multi_value_headers.enabled"
          Value: "true"
```

## Enable health checks

By default, health checks are disabled for target groups of type
`lambda`. You can enable health checks in order to implement DNS
failover with Amazon Route 53. The Lambda function can check the health of a downstream
service before responding to the health check request. If the response from the
Lambda function indicates a health check failure, the health check failure is passed
to Route 53. You can configure Route 53 to fail over to a backup application stack.

You are charged for health checks as you are for any Lambda function
invocation.

The following is the format of the health check event sent to your Lambda
function. To check whether an event is a health check event, check the value of the
user-agent field. The user agent for health checks is
`ELB-HealthChecker/2.0`.

```
{
    "requestContext": {
        "elb": {
            "targetGroupArn": "arn:aws:elasticloadbalancing:`region`:`123456789012`:targetgroup/`my-target-group`/`6d0ecf831eec9f09`"
        }
    },
    "httpMethod": "GET",
    "path": "/",
    "queryStringParameters": {},
    "headers": {
        "user-agent": "ELB-HealthChecker/2.0"
    },
    "body": "",
    "isBase64Encoded": false
}
```

Console

###### To enable health checks for a lambda target group

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Health checks** tab, choose
   **Edit**.
5. For **Health checks**, select
   **Enable**.
6. (Optional) Update the health check settings as needed.
7. Choose **Save changes**.

AWS CLI

###### To enable health checks for a lambda target group

Use the [modify-target-group](../../../cli/latest/reference/elbv2/modify-target-group.md "../../../cli/latest/reference/elbv2/modify-target-group.md") command.

```
aws elbv2 modify-target-group \
    --target-group-arn `target-group-arn` \
    --health-check-enabled
```

CloudFormation

###### To enable health checks for a lambda target group

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: my-target-group
      TargetType: lambda
      HealthCheckEnabled: true
      Tags:
        - Key: 'department'
          Value: '123'
      Targets:
        - Id: !Ref myLambdaFunction
```

## Register the Lambda function

You can register a single Lambda function with each target group. To replace a
Lambda function, we recommend that you create a new target group, register the new
function with the new target group, and update the listener rules to use the new
target group.

Console

###### To register a Lambda function

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Targets** tab, if there is no Lambda function
   registered, choose **Register target**.
5. Select the Lambda function or enter its ARN.
6. Choose **Register**.

AWS CLI

###### To register a Lambda function

Use the [register-targets](../../../cli/latest/reference/elbv2/register-targets.md "../../../cli/latest/reference/elbv2/register-targets.md") command.

```
aws elbv2 register-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`lambda-function-arn`
```

CloudFormation

###### To register a Lambda function

Update the [AWS::ElasticLoadBalancingV2::TargetGroup](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-targetgroup.md") resource.

```
Resources:
  myTargetGroup:
    Type: 'AWS::ElasticLoadBalancingV2::TargetGroup'
    Properties:
      Name: `my-target-group`
      TargetType: lambda
      Tags:
        - Key: '`department`'
          Value: '`123`'
      Targets:
        - Id: !Ref myLambdaFunction
```

## Deregister the Lambda function

If you no longer need to send traffic to your Lambda function, you can deregister
it. After you deregister a Lambda function, in-flight requests fail with HTTP 5XX
errors.

To replace a Lambda function, we recommend that you create a new target group,
register the new function with the new target group, and update the listener rules
to use the new target group.

Console

###### To deregister a Lambda function

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**,
   choose **Target Groups**.
3. Choose the name of the target group to open its details
   page.
4. On the **Targets** tab, select the
   target and choose **Deregister**.
5. When prompted for confirmation, choose
   **Deregister**.

AWS CLI

###### To deregister a Lambda function

Use the [deregister-targets](../../../cli/latest/reference/elbv2/deregister-targets.md "../../../cli/latest/reference/elbv2/deregister-targets.md") command.

```
aws elbv2 deregister-targets \
    --target-group-arn `target-group-arn` \
    --targets Id=`lambda-function-arn`
```
