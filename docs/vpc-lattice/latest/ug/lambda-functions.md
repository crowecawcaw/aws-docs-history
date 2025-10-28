# Lambda functions as targets in VPC Lattice

You can register your Lambda functions as targets with a VPC Lattice target group, and
configure a listener rule to forward requests to the target group for your Lambda
function. When the service forwards the request to a target group with a Lambda function
as a target, it invokes your Lambda function and passes the content of the request to the
Lambda function, in JSON format.

###### Limitations

- The Lambda function and target group must be in the same account and in the
  same Region.
- The maximum size of the request body that you can send to a Lambda function is
  6 MB.
- The maximum size of the response JSON that the Lambda function can send is 6
  MB.
- The protocol must be HTTP or HTTPS.

## Prepare the Lambda function

The following recommendations apply if you are using your Lambda function with a
VPC Lattice service.

###### Permissions to invoke the Lambda function

When you create the target group and register the Lambda function using the
AWS Management Console or the AWS CLI, VPC Lattice adds the required permissions to your Lambda
function policy on your behalf.

You can also add permissions on your own using the following API call:

```
aws lambda add-permission \
  --function-name `lambda-function-arn-with-alias-name` \
  --statement-id `vpc-lattice` \
  --principal vpc-lattice.amazonaws.com \
  --action lambda:InvokeFunction \
  --source-arn `target-group-arn`
```

###### Lambda function versioning

You can register one Lambda function per target group. To ensure that you can
change your Lambda function and that the VPC Lattice service always invokes the
current version of the Lambda function, create a function alias and include the
alias in the function ARN when you register the Lambda function with the
VPC Lattice service. For more information, see [Lambda function versions](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") and
[Create an alias for a Lambda function](../../../lambda/latest/dg/configuration-aliases.md "../../../lambda/latest/dg/configuration-aliases.md")
in the _AWS Lambda Developer Guide_.

## Create a target group for the Lambda

function

Create a target group, which is used in request routing. If the request content
matches a listener rule with an action to forward it to this target group, the
VPC Lattice service invokes the registered Lambda function.

###### To create a target group and register the Lambda function using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Choose **Create target group**.
4. For **Choose a target type**, select **Lambda
   function**.
5. For **Target group name**, enter a name for the target group.
6. For **Lambda event structure version**, choose a version.
   For more information, see [Receive events from the VPC Lattice
   service](#receive-event-from-service "#receive-event-from-service").
7. (Optional) To add tags, expand **Tags**, choose **Add
   new tag**, and enter the tag key and tag value.
8. Choose **Next**.
9. For **Lambda function**, do one of the following:
   - Select an existing Lambda function.
   - Create a new Lambda function and select it.
   - Register the Lambda function later.

10. Choose **Create target group**.

###### To create a target group and register the Lambda function using the

AWS CLI

Use the [create-target-group](../../../cli/latest/reference/vpc-lattice/create-target-group.md "../../../cli/latest/reference/vpc-lattice/create-target-group.md")
and [register-targets](../../../cli/latest/reference/vpc-lattice/register-targets.md "../../../cli/latest/reference/vpc-lattice/register-targets.md") commands.

## Receive events from the VPC Lattice

service

The VPC Lattice service supports Lambda invocation for requests over both HTTP and
HTTPS. The service sends an event in JSON format, and adds the
`X-Forwarded-For` header to every request.

###### Base64 encoding

The service Base64 encodes the body if the `content-encoding` header
is present and the content type is not one of the following:

- `text/*`
- `application/json`
- `application/xml`
- `application/javascript`

If the `content-encoding` header is not present, Base64 encoding
depends on the content type. For the content types above, the service sends the
body as is, without Base64 encoding.

###### Event structure format

When you create or update a target group of type `LAMBDA`, you can
specify the version of the event structure that your Lambda function receives.
The possible versions are `V1` and `V2`.

###### Example event: V2

```
{
    "version": "2.0",
    "path": "/",
    "method": "GET|POST|HEAD|...",
    "headers": {
        "`header-key`": ["`header-value`", ...],
        ...
    },
    "queryStringParameters": {
        "`key`": ["`value`", ...]
    },
    "body": "`request-body`",
    "isBase64Encoded": true|false,
    "requestContext": {
        "serviceNetworkArn": "arn:aws:vpc-lattice:`region`:`123456789012`:servicenetwork/`sn-0bf3f2882e9cc805a`",
        "serviceArn": "arn:aws:vpc-lattice:`region`:`123456789012`:service/`svc-0a40eebed65f8d69c`",
        "targetGroupArn": "arn:aws:vpc-lattice:`region`:`123456789012`:targetgroup/`tg-6d0ecf831eec9f09`",
        "identity": {
            "sourceVpcArn": "arn:aws:ec2:`region`:`123456789012`:vpc/`vpc-0b8276c84697e7339`",
            "type": "AWS_IAM",
            "principal": "arn:aws:iam::`123456789012`:assumed-role/`my-role`/`my-session`",
            "principalOrgID": "`o-50dc6c495c0c9188`",
            "sessionName": "`i-0c7de02a688bde9f7`",
            "x509IssuerOu": "`string`",
            "x509SanDns": "`string`",
            "x509SanNameCn": "`string`",
            "x509SanUri": "`string`",
            "x509SubjectCn": "`string`"
        },
        "region": "`region`",
        "timeEpoch": "`1690497599177430`"
    }
}
```

`body`
The body of the request. Present only if the protocol is HTTP, HTTPS, or gRPC.

`headers`
The HTTP headers of the request. Present only if the protocol is HTTP, HTTPS, or gRPC.

`identity`

The identity information. The following are possible fields.

- `principal` – The authenticated principal. Present only if AWS authentication is successful.
- `principalOrgID` – The ID of the organization for the authenticated principal. Present only if AWS authentication is successful.
- `sessionName` – The name of the authenticated session. Present only if AWS authentication is successful.
- `sourceVpcArn` – The ARN of the VPC where the request originated. Present
  only if the source VPC can be identified.
- `type` – The value is `AWS_IAM` if an auth policy is used and AWS authentication is successful.

If Roles Anywhere credentials are used and authentication is
successful, the following are possible fields.

- `x509IssuerOu` – The issuer (OU).
- `x509SanDns` – The subject alternative name (DNS).
- `x509SanNameCn` – The issuer alternative name (Name/CN).
- `x509SanUri` – The subject alternative name (URI).
- `x509SubjectCn` – The subject name (CN).

`isBase64Encoded`
Indicates whether the body was base64 encoded. Present only if the protocol is HTTP, HTTPS, or
gRPC and the request body is not already a string.

`method`
The HTTP method of the request. Present only if the protocol is HTTP, HTTPS, or gRPC.

`path`
The path of the request. Present only if the protocol is HTTP, HTTPS, or gRPC.

`queryStringParameters`
The HTTP query string parameters. Present only if the protocol is HTTP, HTTPS, or gRPC.

`serviceArn`
The ARN of the service that receives the request.

`serviceNetworkArn`
The ARN of the service network that delivers the request.

`targetGroupArn`
The ARN of the target group that receives the request.

`timeEpoch`
The time, in microseconds.

###### Example event: V1

```
{
    "raw_path": "`/path/to/resource`",
    "method": "GET|POST|HEAD|...",
    "headers": {"`header-key`": "`header-value`", ... },
    "query_string_parameters": {"`key`": "`value`", ...},
    "body": "`request-body`",
    "is_base64_encoded": true|false
}
```

## Respond to the VPC Lattice service

The response from your Lambda function must include the Base64 encoding status,
status code, and headers. You can omit the body.

To include a binary content in the body of the response, you must Base64 encode
the content and set `isBase64Encoded` to `true`. The service
decodes the content to retrieve the binary content and sends it to the client in the
body of the HTTP response.

The VPC Lattice service does not honor hop-by-hop headers, such as
`Connection` or `Transfer-Encoding`. You can omit the
`Content-Length` header because the service computes it before
sending responses to clients.

The following is an example response from a Lambda function:

```
{
    "isBase64Encoded": `false`,
    "statusCode": `200`,
    "headers": {
        "Set-cookie": "`cookies`",
        "Content-Type": "application/json"
    },
    "body": "Hello from Lambda (optional)"
}
```

## Multi-value headers

VPC Lattice supports requests from a client or responses from a Lambda function
that contain headers with multiple values or contain the same header
multiple times. VPC Lattice passes all values to the targets.

In the following example, there are two headers named header1
with different values.

```
header1 = value1
header1 = value2
```

With a V2 event structure, VPC Lattice sends the values in a list. For example:

```
"header1": ["value1", "value2"]
```

With a V1 event structure, VPC Lattice combines the values into a single string. For example:

```
"header1": "value1, value2"
```

## Multi-value query string parameters

VPC Lattice supports query parameters with multiple values for the same key.

In the following example, there are two parameters named QS1 with different values.

```
http://www.example.com?&QS1=value1&QS1=value2
```

With a V2 event structure, VPC Lattice sends the values in a list. For example:

```
"QS1": ["value1", "value2"]
```

With a V1 event structure, VPC Lattice uses the last value passed. For example:

```
"QS1": "value2"
```

## Deregister the Lambda function

If you no longer need to send traffic to your Lambda function, you can deregister
it. After you deregister a Lambda function, in-flight requests fail with HTTP 5XX
errors.

To replace a Lambda function, we recommend that you create a new target group,
register the new function with the new target group, and update the listener rules
to use the new target group instead of the existing one.

###### To deregister a Lambda function using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. On the navigation pane, under **VPC Lattice**, choose
   **Target groups**.
3. Choose the name of the target group to open its details page.
4. On the **Targets** tab, choose
   **Deregister**.
5. When prompted for confirmation, enter `confirm` and then
   choose **Deregister**.

###### To deregister the Lambda function using the AWS CLI

Use the [deregister-targets](../../../cli/latest/reference/vpc-lattice/deregister-targets.md "../../../cli/latest/reference/vpc-lattice/deregister-targets.md") command.
