

# Lambda Web Function endpoint access control
<a name="web-functions-endpoint-access-control"></a>

You can control access to your AWS Lambda Web Function endpoints using the `AuthType` you set on each endpoint. Depending on the authentication type, you can also attach a resource-based policy to the Web Function to control who can invoke an endpoint.

When you configure an endpoint, you specify one of the following `AuthType` options:

`IamAuth`  
With this authentication type, Lambda uses AWS Identity and Access Management (IAM) to authenticate and authorize requests based on the caller's identity policy and the Web Function's resource-based policy. Either the caller signs requests directly with AWS Signature Version 4 (SigV4), or with Signature Version 4a (SigV4a) for `MultiRegion` endpoints, or an AWS service such as Amazon CloudFront signs on their behalf when it fronts the endpoint (see [CloudFront integration](#web-functions-endpoint-access-control-cloudfront)). Choose this option when you want Lambda to enforce IAM-based access control on your endpoint.

`ApplicationManaged`  
Lambda doesn't authenticate or authorize requests. Every request reaches your function, and your function code is responsible for any authentication. Choose this option for public endpoints, or when you handle authentication in your own code.

The IAM action for invoking an endpoint is `lambda:InvokeWebFunctionEndpoint`.

You set an endpoint's authentication type with the `--auth-type` parameter when you create the endpoint (`create-web-function-endpoint`), and you can change it later with `update-web-function-endpoint`. For the create command, see [Creating an endpoint](web-functions-endpoints.md#web-functions-endpoint-create). For the properties that you can change, see [Updating an endpoint](web-functions-endpoints.md#web-functions-endpoint-update).

## Using the `IamAuth` authentication type
<a name="web-functions-endpoint-access-control-iam"></a>

If you choose the `IamAuth` authentication type, callers must sign each request with SigV4 (SigV4a for `MultiRegion` endpoints) and must be permitted to invoke the endpoint. Depending on who makes the request, you grant this permission with a resource-based policy on the Web Function, an identity-based policy on the caller, or both.

If the caller is in the same AWS account as the Web Function, they can be granted `lambda:InvokeWebFunctionEndpoint` through either an identity-based policy or the function's resource-based policy. If the caller is in a different account, they need both an identity-based policy granting the action and a resource-based policy on the function that allows them.

Resource-based policies are attached to the Web Function, but each statement can scope the `Resource` to a specific endpoint ARN. The following resource-based policy allows the `InvokeRole` role in account `222233334444` to invoke the `prod` endpoint of `my-function`:

**Example Cross-account resource-based policy**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::222233334444:role/InvokeRole"
            },
            "Action": "lambda:InvokeWebFunctionEndpoint",
            "Resource": "arn:aws:lambda:us-east-1:111122223333:web-function/my-function/endpoint/prod"
        }
    ]
}
```

To attach the resource-based policy, use `put-resource-policy` with the function ARN (not an endpoint ARN):

```
aws lambda-web put-resource-policy \
    --resource-arn "arn:aws:lambda:us-east-1:111122223333:web-function/my-function" \
    --policy file://policy.json \
    --region us-east-1
```

You can review or remove the policy with `get-resource-policy` and `delete-resource-policy`.

A Web Function has one resource-based policy, and `put-resource-policy` replaces it. To add a statement, such as the CloudFront statement in [CloudFront integration](#web-functions-endpoint-access-control-cloudfront), get the current policy with `get-resource-policy`, add the statement to its `Statement` array, and pass the returned `revisionId` with `--revision-id`. If someone changed the policy after you read it, the request fails with a `ConflictException` instead of overwriting their change.

To allow invoking all endpoints of a function, use a wildcard in the resource ARN:

```
"Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/endpoint/*"
```

Replace the Region, account ID, and function name with your own values. Keep `endpoint/*` at the end.

### Granting invoke permission to a principal
<a name="web-functions-endpoint-access-control-iam-grant"></a>

A caller needs `lambda:InvokeWebFunctionEndpoint` to invoke an endpoint. For a caller in the same account as the Web Function, granting this action in the caller's identity-based policy is sufficient. No resource-based policy is required. For a caller in a different account, this identity-based policy is required in addition to a resource-based policy on the function that allows them.

Attach the following policy to the IAM role or user that will invoke the endpoint:

**Example Identity-based policy to invoke an endpoint**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lambda:InvokeWebFunctionEndpoint",
            "Resource": "arn:aws:lambda:us-east-1:111122223333:web-function/my-function/endpoint/prod"
        }
    ]
}
```

### Signing requests
<a name="web-functions-endpoint-access-control-signing"></a>

Lambda doesn't provide a dedicated SDK for invoking endpoints. You send standard HTTP requests and sign them yourself with SigV4 or SigV4a, using the service name `lambda`. Note the following:
+ Every signed request must include the `X-Amz-Content-SHA256` header, including requests with no body. Lambda doesn't read the request body when it validates the signature, so it uses this header value as the payload hash. Requests without it are rejected with `403 Forbidden`.
+ If you aren't signing the body (for example, when streaming), use the literal value `UNSIGNED-PAYLOAD` for `X-Amz-Content-SHA256`. Lambda doesn't support chunked body signing.
+ Lambda doesn't check the request body against the `X-Amz-Content-SHA256` value. The signature covers the header value, not the body content. If you need body integrity protection beyond TLS, implement it in your application.
+ Regional endpoints (`HomeRegion`, `PerRegion`) use SigV4 with the endpoint's Region. `MultiRegion` endpoints use AWS Signature Version 4a (SigV4a), which signs for a set of Regions instead of one Region. Use the Region set `*`.
+ If an `IamAuth` request returns `403 Forbidden`, check that the request is signed with SigV4 (or SigV4a), includes the `X-Amz-Content-SHA256` header, and uses unexpired credentials, and that your policies allow `lambda:InvokeWebFunctionEndpoint` on the endpoint ARN.

For more information about signing requests, see [Signing AWS API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html).

After Lambda validates the SigV4 or SigV4a signature, it removes the `Authorization` header before forwarding the request to your function. If you want your function to receive the `Authorization` header on an `IamAuth` endpoint, send requests through CloudFront, which signs them on your behalf (see [CloudFront integration](#web-functions-endpoint-access-control-cloudfront)).

### CloudFront integration
<a name="web-functions-endpoint-access-control-cloudfront"></a>

You can use Amazon CloudFront origin access control (OAC) to put a CloudFront distribution in front of an `IamAuth` endpoint. With OAC, CloudFront signs each origin request on the viewer's behalf, so callers don't sign requests themselves. CloudFront doesn't use the `Authorization` header to sign the origin request, so it can pass your `Authorization` header through to the function.

Lambda removes any `Authorization` value that is itself an AWS signature (a value that starts with `AWS4-`). This lets you keep your application's authentication (for example, JWT or cookies) while CloudFront signs every origin request. To do this, configure the distribution to forward the `Authorization` header. For more information, see [Restricting access to an AWS origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-origin.html).

The endpoint domain stays reachable on the internet, and Lambda also accepts direct signed requests from any principal that your policies allow.

This requires the endpoint's authentication type to be `IamAuth`. Create the origin access control with origin type `lambda` and signing behavior `always-amz-auth`. CloudFront rejects other signing behaviors for Web Function origins.

**Note**  
Lambda doesn't authenticate requests to an `ApplicationManaged` endpoint or evaluate the Web Function's resource-based policy for them. Such an endpoint stays publicly reachable at its own domain, even behind CloudFront.

To allow CloudFront to invoke the endpoint, attach a resource-based policy to the Web Function that grants the CloudFront service principal (`cloudfront.amazonaws.com`) the `lambda:InvokeWebFunctionEndpoint` action. Use an `aws:SourceArn` condition to allow only your specific distribution:

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
            "Resource": "arn:aws:lambda:us-east-1:111122223333:web-function/my-function/endpoint/prod",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:cloudfront::111122223333:distribution/<distribution-id>"
                }
            }
        }
    ]
}
```

## Using the `ApplicationManaged` authentication type
<a name="web-functions-endpoint-access-control-appmanaged"></a>

When an endpoint's authentication type is `ApplicationManaged`, anyone with the endpoint's domain can invoke your function. Lambda performs no authentication or authorization.

Choose `ApplicationManaged` when you want your endpoint to be publicly reachable, for example, to serve requests directly from a web browser. You can also choose it when you handle authentication in your own code, such as OAuth 2.0, OpenID Connect, or a custom token scheme.

With this authentication type:
+ Lambda allows all callers to invoke the endpoint. It doesn't evaluate a resource-based policy for these requests.
+ Lambda forwards the caller's `Authorization` header to your function, so your code can validate it. If the header contains an AWS Signature Version 4 (SigV4) signature, Lambda removes it, along with any `X-Amz-Security-Token` header, so that AWS credentials aren't passed to your function code.
+ Your function is responsible for all authentication and authorization.

**Note**  
For `ApplicationManaged` endpoints, Lambda doesn't evaluate the Web Function's resource-based policy for invoke requests. You can't use a resource-based policy to restrict who invokes an `ApplicationManaged` endpoint. To restrict invocation, use `IamAuth` instead. The resource-based policy still applies to management actions. For example, it can grant another account permission to update the endpoint. For more information, see [Resource-based policies](web-functions-permissions.md#web-functions-permissions-resource-policy).

## Governance and access control
<a name="web-functions-endpoint-access-control-governance"></a>

You can control who can configure endpoints.

Lambda supports the following IAM actions for managing endpoints:
+ `lambda:CreateWebFunction` – Create a Web Function and configure its initial endpoint, including its `AuthType`.
+ `lambda:CreateWebFunctionEndpoint` – Create an endpoint and set its `AuthType`.
+ `lambda:UpdateWebFunctionEndpoint` – Update an endpoint, including its `AuthType`.
+ `lambda:GetWebFunctionEndpoint` – View an endpoint's configuration.
+ `lambda:ListWebFunctionEndpoints` – List the endpoints of a Web Function.
+ `lambda:DeleteWebFunctionEndpoint` – Delete an endpoint.

To allow or deny an action based on an authentication type, use a condition key. `lambda:Request/WebFunctionAuthType` applies to `CreateWebFunction`, `CreateWebFunctionEndpoint`, and `UpdateWebFunctionEndpoint`. `lambda:Resource/WebFunctionAuthType` applies to `InvokeWebFunctionEndpoint` (on `IamAuth` endpoints), `UpdateWebFunctionEndpoint`, `GetWebFunctionEndpoint`, and `DeleteWebFunctionEndpoint`. For details, see [Condition keys](#web-functions-endpoint-access-control-condition-keys).

### Restricting public endpoints in an organization
<a name="web-functions-endpoint-access-control-scp"></a>

If you administer an AWS Organization and want to prevent developers from creating public endpoints, use a service control policy (SCP) that denies creating or updating endpoints with the `ApplicationManaged` authentication type. Use the `lambda:Request/WebFunctionAuthType` condition key, which reflects the authentication type in the request:

**Example SCP denying public endpoints**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "lambda:CreateWebFunction",
                "lambda:CreateWebFunctionEndpoint",
                "lambda:UpdateWebFunctionEndpoint"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "lambda:Request/WebFunctionAuthType": "ApplicationManaged"
                }
            }
        }
    ]
}
```

The policy includes `lambda:CreateWebFunction` because that operation creates the initial endpoint from the request's `endpointConfig`. With this policy in place, `aws lambda-web deploy` fails with an access denied error unless the developer adds `--auth-type IamAuth`. By default, the command creates an `ApplicationManaged` endpoint.

### Condition keys
<a name="web-functions-endpoint-access-control-condition-keys"></a>

For fine-grained access control, Lambda supports the following condition context keys:
+ `lambda:Request/WebFunctionAuthType` – The authentication type specified in a request. Available during `CreateWebFunction`, `CreateWebFunctionEndpoint`, and `UpdateWebFunctionEndpoint`. Use it to control which authentication types can be configured.
+ `lambda:Resource/WebFunctionAuthType` – The authentication type currently configured on an endpoint, with the values `IamAuth` and `ApplicationManaged`. Available during `InvokeWebFunctionEndpoint`, `UpdateWebFunctionEndpoint`, `DeleteWebFunctionEndpoint`, and `GetWebFunctionEndpoint`. For `InvokeWebFunctionEndpoint`, Lambda evaluates the key only on `IamAuth` endpoints, because requests to `ApplicationManaged` endpoints aren't authorized with IAM.
+ `aws:ResourceTag/${TagKey}` – Filters access by the tags on the Web Function. Endpoints and revisions inherit the parent function's tags, so you can use ABAC to control invoke access.

**Example Allow invoke only on endpoints of a tagged function**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "lambda:InvokeWebFunctionEndpoint",
            "Resource": "arn:aws:lambda:us-east-1:111122223333:web-function/*/endpoint/prod",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/Environment": "Production"
                }
            }
        }
    ]
}
```