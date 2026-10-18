

# Restrict access to an AWS Lambda Web Function origin
<a name="private-content-restricting-access-to-lambda-web"></a>

You can use origin access control (OAC) to restrict access to an AWS Lambda Web Function origin. A Lambda Web Function provides its own regional or global HTTPS endpoint, which you use as the origin domain for your CloudFront distribution. For more information about Lambda Web Functions, see [AWS Lambda Web Functions](https://docs.aws.amazon.com/lambda/latest/dg/web-functions.html) in the *AWS Lambda Developer Guide*.

**Note**  
OAC with Lambda Web Functions is not supported for global endpoints that include opt-in Regions. If the endpoint routes a request to an opt-in Region, CloudFront cannot sign the request for that Region. The origin then returns an HTTP 403 (Forbidden) error. All Regions associated with the global endpoint must be Regions that are enabled by default.

For information about using OAC with a Lambda function URL origin, see [Restrict access to an AWS Lambda function URL origin](private-content-restricting-access-to-lambda.md).

## Prerequisites
<a name="oac-prerequisites-lambda-web"></a>

Before you create and set up OAC, you must have a CloudFront distribution with a Lambda Web Function as the origin. The origin domain name is the hostname of the Lambda Web Function's endpoint. CloudFront identifies the [endpoint type](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-endpoints.html#web-functions-endpoint-types) from the hostname:
+ Regional endpoint (`HomeRegion` and `PerRegion` endpoint types) – The hostname ends in `.lambda-web.{{AWS-Region}}.on.aws`
+ Global endpoint (`MultiRegion` endpoint type) – The hostname ends in `.lambda-web.global.on.aws`

Your configuration must also meet the following requirements:
+ **Endpoint auth type** – The endpoint's auth type must be `IamAuth`. With `IamAuth`, the endpoint uses AWS Identity and Access Management (IAM) to authenticate and authorize requests. For requests from CloudFront, authorization is based on the Lambda Web Function's resource-based policy. CloudFront signs requests on the viewer's behalf, and the endpoint validates the signature. For more information, see [CloudFront integration](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-endpoint-access-control.html#web-functions-endpoint-access-control-cloudfront) in the *AWS Lambda Developer Guide*.
+ **Cache policy** – If your Lambda Web Function uses the viewer's `Authorization` header, you must add the header to the [cache policy](controlling-the-cache-key.md). This requirement applies to every cache behavior that uses the origin. For `GET` and `HEAD` requests, CloudFront removes the `Authorization` header before forwarding the request unless the header is in the cache policy. For more information, see [HTTP request headers and CloudFront behavior (custom and Amazon S3 origins)](RequestAndResponseBehaviorCustomOrigin.md#request-custom-headers-behavior).
+ **Origin request policy** – Use an origin request policy that excludes the viewer's `Host` header. Lambda Web Function endpoints expect the `Host` header to contain the origin domain name, not the domain name of the CloudFront distribution. If the `Host` header contains the distribution's domain name, the endpoint returns an HTTP 404 (Not Found) error. If you use a managed origin request policy, use `AllViewerExceptHostHeader`, not `AllViewer`. For more information, see [AllViewerExceptHostHeader](using-managed-origin-request-policies.md#managed-origin-request-policy-all-viewer-except-host-header).

**Note**  
Lambda@Edge origin request and origin response triggers are not supported on cache behaviors that use a Lambda Web Function origin with OAC. This applies to regional and global endpoints, and to origins that are accessed directly or through an origin group. CloudFront rejects a distribution configuration that contains both.

## Grant CloudFront permission to access the Lambda Web Function
<a name="oac-permission-to-access-lambda-web"></a>

Attach a resource-based policy to the Lambda Web Function that allows the CloudFront service principal (`cloudfront.amazonaws.com`) to invoke the endpoint. The IAM action for invoking an endpoint is `lambda:InvokeWebFunctionEndpoint`. The policy is attached to the Lambda Web Function, but each statement can scope the `Resource` to a specific endpoint ARN. Use a `Condition` element to allow CloudFront to access the endpoint only when the request is on behalf of the CloudFront distribution that contains the origin.

**Example Resource-based policy for CloudFront OAC**  

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowCloudFrontOACAccess",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "lambda:InvokeWebFunctionEndpoint",
            "Resource": "arn:aws:lambda:us-east-1:{{111122223333}}:web-function/{{my-function}}/endpoint/{{prod}}",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:cloudfront::{{111122223333}}:distribution/{{EDFDVBD6EXAMPLE}}"
                }
            }
        }
    ]
}
```

To attach the resource-based policy, use the **put-resource-policy** command with the *function* ARN (not an endpoint ARN):

```
aws lambda-web put-resource-policy \
  --resource-arn "arn:aws:lambda:us-east-1:{{111122223333}}:web-function/{{my-function}}" \
  --policy file://policy.json \
  --region us-east-1
```

You can review or remove the policy with the **get-resource-policy** and **delete-resource-policy** commands.

**Note**  
For endpoints that span more than one Region, Lambda replicates policy changes to all Regions that serve the endpoint. A new or updated policy can take a short time to take effect in every Region. For more information, see [Replication and eventual consistency](https://docs.aws.amazon.com/lambda/latest/dg/web-functions-permissions.html#web-functions-permissions-resource-policy-replication) in the *AWS Lambda Developer Guide*.

## Create the origin access control
<a name="create-oac-lambda-web"></a>

To create an origin access control (OAC), you can use the AWS Management Console, CloudFormation, the AWS CLI, or the CloudFront API.

------
#### [ Console ]

**To create an origin access control**

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Origin access**.

1. Choose **Create control setting**.

1. On the **Create control setting** form, do the following:

   1. In the **Details** pane, enter a **Name** and (optionally) a **Description** for the origin access control.

   1. Choose **Lambda** from the **Origin type** dropdown. This origin type is used for both Lambda function URLs and Lambda Web Functions.

   1. If your origin is a global endpoint (the hostname ends in `.lambda-web.global.on.aws`), select the **Use SigV4a signing protocol** option. For a regional endpoint (the hostname ends in `.lambda-web.{{AWS-Region}}.on.aws`), leave this option cleared.

   1. For **Signing behavior**, choose **Always sign, preserve viewer authorization**. This option appears under **Sign requests (recommended)**, which is selected by default. Lambda Web Function origins support only this signing behavior. For more information, see [Signing behavior](#oac-signing-behavior-lambda-web).

1. Choose **Create**.

**To add an origin access control to a Lambda Web Function origin in a distribution**

1. Open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. Choose a distribution with a Lambda Web Function origin that you want to add the OAC to, then choose the **Origins** tab.

1. Select the Lambda Web Function origin that you want to add the OAC to, then choose **Edit**.

1. For **Origin access**, choose **Origin access control settings (recommended)**.

1. From the **Origin access control** dropdown menu, choose the OAC that you want to use.

1. Choose **Save changes**.

The distribution starts deploying to all of the CloudFront edge locations. When an edge location receives the new configuration, it signs all requests that it sends to the Lambda Web Function origin.

------
#### [ CLI ]

Use the **create-origin-access-control** command. For a regional endpoint (the hostname ends in `.lambda-web.{{AWS-Region}}.on.aws`), use the `sigv4` signing protocol:

```
aws cloudfront create-origin-access-control \
    --origin-access-control-config '{
        "Name": "my-lambda-web-oac",
        "Description": "OAC for Lambda Web Function origin",
        "SigningProtocol": "sigv4",
        "SigningBehavior": "always-amz-auth",
        "OriginAccessControlOriginType": "lambda"
    }'
```

For a global endpoint (the hostname ends in `.lambda-web.global.on.aws`), use the `sigv4a` signing protocol:

```
aws cloudfront create-origin-access-control \
    --origin-access-control-config '{
        "Name": "my-lambda-web-global-oac",
        "Description": "OAC for global Lambda Web Function origin",
        "SigningProtocol": "sigv4a",
        "SigningBehavior": "always-amz-auth",
        "OriginAccessControlOriginType": "lambda"
    }'
```

------
#### [ CloudFormation ]

Specify the following values in the `OriginAccessControlConfig`:
+ `SigningProtocol`: `sigv4` (regional endpoint) or `sigv4a` (global endpoint)
+ `SigningBehavior`: `always-amz-auth`
+ `OriginAccessControlOriginType`: `lambda`

**Example CloudFormation template**  

```
Type: AWS::CloudFront::OriginAccessControl
Properties:
  OriginAccessControlConfig:
    Description: An optional description for the origin access control
    Name: my-lambda-web-oac
    OriginAccessControlOriginType: lambda
    SigningBehavior: always-amz-auth
    SigningProtocol: sigv4a
```

For more information, see [AWS::CloudFront::OriginAccessControl](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudfront-originaccesscontrol.html) in the *AWS CloudFormation User Guide*.

------

OAC takes effect for every request only after the distribution finishes deploying. For an endpoint that spans more than one Region, the resource-based policy that you attached earlier must also finish replicating to every Region that serves the endpoint. Until both complete, some requests can receive a transient HTTP 403 response from the origin. These errors resolve automatically after the distribution finishes deploying and the policy finishes replicating.

## Signing behavior
<a name="oac-signing-behavior-lambda-web"></a>

Lambda Web Function origins support only the `always-amz-auth` signing behavior (**Always sign, preserve viewer authorization** in the console). CloudFront always signs all requests that it sends to the Lambda Web Function, but it does not replace the `Authorization` header from the viewer request. Instead, CloudFront adds its signature in a dedicated CloudFront header and passes the viewer's `Authorization` header to the origin unmodified. With this behavior, your Lambda Web Function can receive the viewer's original `Authorization` header (for example, to perform its own authentication or authorization). CloudFront still signs every request that it sends to the origin. To forward the viewer's `Authorization` header, you must add it to a [cache policy](controlling-the-cache-key.md) for every cache behavior that uses the origin.

The other signing behaviors (`always`, `never`, and `no-override`) are not supported for Lambda Web Function origins. The `always-amz-auth` signing behavior is not supported for any other origin type, including Lambda function URL origins.

For `PUT`, `POST`, and `PATCH` requests, CloudFront signs the origin request with an unsigned payload (`UNSIGNED-PAYLOAD`). The request body is not covered by the CloudFront signature. The signature still covers the request method, path, query string, and the headers that identify your distribution. The endpoint can therefore verify that each request comes from CloudFront on behalf of your distribution before it invokes your Lambda Web Function. The request body is protected in transit by the HTTPS connection between CloudFront and the endpoint. You do not need to include an `x-amz-content-sha256` header in requests to CloudFront. If a viewer sends one, CloudFront does not use it when signing the origin request.