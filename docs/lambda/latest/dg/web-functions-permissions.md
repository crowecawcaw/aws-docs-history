

# Lambda Web Function permissions
<a name="web-functions-permissions"></a>

Lambda Web Functions use AWS Identity and Access Management (IAM) to control what your application code can do (the execution role) and who can access your Web Function (resource-based policies). This page explains how to configure each type.
+ **Execution role** – An IAM role that your Web Function code assumes to access AWS services such as Amazon CloudWatch Logs, DynamoDB, or Amazon S3.
+ **Resource-based policies** – A policy attached to your Web Function. It defines which IAM principals or AWS services can perform Web Function actions, such as invoking an endpoint whose authentication type is `IamAuth`, which means Lambda authenticates requests with IAM. For more information, see [Authentication type](web-functions-endpoints.md#web-functions-endpoint-auth). An IAM principal in another account also needs identity-based permission.

The following diagram shows the identities that need permissions and what each one uses. The deployer calls Lambda management actions and needs `iam:PassRole` on the execution role. The code uploader needs `s3:PutObject` on the versioned Amazon S3 bucket, and Lambda reads the code object version. Lambda can encrypt your Web Function code and environment variables with an optional customer managed AWS KMS key. Your code runs with the execution role, which grants access to Amazon CloudWatch Logs and your dependencies. An endpoint caller needs `lambda:InvokeWebFunctionEndpoint` for an `IamAuth` endpoint, or application credentials for an `ApplicationManaged` endpoint.

![The deployer, code uploader, and endpoint caller each need different permissions to reach the Web Function control plane, the Amazon S3 code bucket, and the execution environment.](https://docs.aws.amazon.com/lambda/latest/dg/images/web-functions-permissions-actors.png)


## Execution role
<a name="web-functions-permissions-execution-role"></a>

The execution role is an IAM role that Lambda assumes when it runs your Web Function code. Your application uses this role's permissions to interact with other AWS services. At minimum, your Web Function needs permission to write logs to Amazon CloudWatch Logs so you can monitor your application. If your application reads from DynamoDB, writes to Amazon S3, or calls other AWS services, you add those permissions to the execution role.

### Creating an execution role
<a name="web-functions-permissions-execution-role-create"></a>

To create an execution role for your Web Function, create an IAM role with a trust policy that allows the Lambda service principal to assume it, and attach a permissions policy that grants the access your application needs.

**To create an execution role (AWS CLI)**

1. Create a file named `trust-policy.json` with the following trust policy. This policy allows the Lambda service principal to assume the role on your behalf.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Principal": {
                   "Service": "lambda.amazonaws.com"
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

1. Create the role.

   ```
   aws iam create-role \
       --role-name {{my-web-function-role}} \
       --assume-role-policy-document file://trust-policy.json
   ```

1. Attach the AWS Lambda basic execution role managed policy. This policy grants permissions to create log groups, log streams, and write log events to Amazon CloudWatch Logs.

   ```
   aws iam attach-role-policy \
       --role-name {{my-web-function-role}} \
       --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
   ```

If you prefer to create a custom permissions policy instead of using the managed policy, the minimum permissions your Web Function needs for logging are:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:/aws/lambda/web/{{my-web-app}}:*",
                "arn:aws:logs:*:{{111122223333}}:log-group:/aws/lambda/web/{{my-web-app}}.local:*"
            ]
        }
    ]
}
```

The policy covers two log groups. Lambda writes in-Region logs to the `.local` log group and then centralizes them into the log group without the suffix in the home Region. The centralized log group ARN uses the home Region. The `.local` ARN uses a Region wildcard because Lambda writes to that group in every Region where an endpoint serves traffic. This lets one execution role support endpoints with different Region sets. If the role cannot write to the `.local` log group in a Region, Lambda does not deliver logs from that Region. If you use a custom log group, replace both ARNs with your log group name and your log group name followed by `.local`. For more information, see [Log groups](web-functions-logging.md#web-functions-logging-log-groups).

### Adding permissions for other services
<a name="web-functions-permissions-execution-role-additional"></a>

If your application accesses other AWS services, add the corresponding permissions to the execution role. The following example adds read access to a DynamoDB table and write access to an Amazon S3 bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:{{us-east-1}}:{{111122223333}}:log-group:/aws/lambda/web/{{my-web-app}}:*",
                "arn:aws:logs:*:{{111122223333}}:log-group:/aws/lambda/web/{{my-web-app}}.local:*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:Query"
            ],
            "Resource": "arn:aws:dynamodb:{{us-east-1}}:{{111122223333}}:table/{{my-table}}"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::{{my-output-bucket}}/*"
        }
    ]
}
```

The IAM identity that creates a Web Function or revision uses its own permissions, not the execution role. That identity needs `lambda:CreateWebFunction` or `lambda:CreateWebFunctionRevision`, `iam:PassRole` on the execution role, and read access to the deployment package in Amazon S3. For the Amazon S3 permissions, see [Caller permissions](web-functions-code-s3.md#web-functions-code-s3-caller-permissions). If you use a customer managed key to encrypt your Web Function code and environment variables, that identity also needs AWS KMS permissions. For more information, see [Encryption at rest for Web Functions](web-functions-encryption.md).

## Resource-based policies
<a name="web-functions-permissions-resource-policy"></a>

A resource-based policy is a JSON policy document that you attach to your Web Function. It can grant any Web Function action except `lambda:CreateWebFunction` to IAM principals or AWS services. For example, it can grant `lambda:InvokeWebFunctionEndpoint` for an `IamAuth` endpoint. It can also grant management actions such as `lambda:GetWebFunction`, `lambda:CreateWebFunctionRevision`, and `lambda:UpdateWebFunctionEndpoint`.

The policy attachment and its statements use different resource ARNs:
+ **Web Function ARN** – Use this ARN with `PutResourcePolicy`, `GetResourcePolicy`, and `DeleteResourcePolicy`, and in the `Resource` element of a statement that grants an action on the Web Function itself, such as `lambda:GetWebFunction`, `lambda:CreateWebFunctionRevision`, or `lambda:CreateWebFunctionEndpoint`. For example, `arn:aws:lambda:us-east-1:111122223333:web-function/my-function`. For an action on an existing endpoint, such as `lambda:UpdateWebFunctionEndpoint`, use the endpoint ARN. For an action on an existing revision, such as `lambda:DeleteWebFunctionRevision`, use the revision ARN. To cover all endpoints of the Web Function, use `arn:aws:lambda:us-east-1:111122223333:web-function/my-function/endpoint/*`.
+ **Endpoint ARN** – Use this ARN in the `Resource` element of a policy statement that grants `lambda:InvokeWebFunctionEndpoint`. For example, `arn:aws:lambda:us-east-1:111122223333:web-function/my-function/endpoint/prod`.

For an IAM principal in the same account, either the principal's identity-based policy or the Web Function's resource-based policy can grant permission. For an IAM principal in another account, both policies must grant permission. This applies to both invoke and management actions.

To allow or deny actions based on the tags of a Web Function, use attribute-based access control (ABAC). For the supported condition keys, see [Tagging Web Functions](web-functions-configuration-tags.md).

**Note**  
Web Functions don't support `AddPermission`, `RemovePermission`, or `GetPolicy`. Manage the policy with `PutResourcePolicy`, `GetResourcePolicy`, and `DeleteResourcePolicy`.

Use resource-based policies when:
+ You want to grant invoke access to a principal in a different AWS account (cross-account invocation).
+ You want to grant invoke access to an AWS service such as CloudFront.
+ You want to let a principal in another AWS account manage the Web Function, for example to create revisions or update endpoints.
+ For same-account invocation, you cannot modify the caller's IAM policy (for example, when the caller is managed by another team).

### Public policies are not allowed
<a name="web-functions-permissions-resource-policy-public"></a>

You cannot attach a public resource-based policy to a Web Function. If a policy is public, the request fails with a `ValidationException`.

In this section, *public* describes a policy that grants access to an unspecified set of principals. It does not describe the endpoint's network accessibility or authentication type.

**What makes a policy public**

A policy is public unless it restricts who can call the resource to a well-specified set of principals. Lambda assumes that the policy is public and then evaluates whether it qualifies as non-public. A policy is public if it allows a principal that any AWS customer could assume. The most common case is an unrestricted wildcard principal, as in the following example. Lambda rejects this policy with a `ValidationException`. Don't use it.

```
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "lambda:InvokeWebFunctionEndpoint",
  "Resource": "arn:aws:lambda:{{us-west-2}}:{{123456789012}}:web-function/{{my-web-function}}/endpoint/{{prod}}"
}
```

The following restrictions do not make a policy non-public:
+ IP address conditions. Narrowing `aws:SourceIp` to a CIDR range is not sufficient.
+ Federated principals. A `Principal` block that names a federated identity provider does not restrict access to a well-specified set of identities.
+ Condition keys that describe the resource. Keys such as the endpoint's authentication type describe how the resource is configured, not who is calling, so they cannot restrict the principal.

There are two ways to make a policy non-public.

#### Specify principals in the Principal block
<a name="web-functions-permissions-resource-policy-public-principals"></a>

List one or more fully specified principals in the `Principal` block. The values must not contain wildcards or policy variables. The number of principals does not matter.

```
{
  "Effect": "Allow",
  "Principal": {
    "AWS": [
      "{{123456789012}}",
      "{{111122223333}}"
    ]
  },
  "Action": "lambda:InvokeWebFunctionEndpoint",
  "Resource": "arn:aws:lambda:{{us-west-2}}:{{123456789012}}:web-function/{{my-web-function}}/endpoint/{{prod}}"
}
```

An IAM principal in another account also needs identity-based permission to invoke the endpoint.

#### Use a trusted condition key
<a name="web-functions-permissions-resource-policy-public-trusted-keys"></a>

Constrain one of the following condition keys to a fixed value. These keys identify the authenticated caller and cannot be set by the requester.
+ `aws:PrincipalAccount`
+ `aws:PrincipalArn`
+ `aws:PrincipalOrgID`
+ `aws:PrincipalOrgPaths`
+ `aws:SourceAccount`
+ `aws:SourceArn`
+ `aws:SourceOrgID`
+ `aws:SourceOrgPaths`
+ `aws:SourceVpc`
+ `aws:SourceVpcArn`
+ `aws:SourceVpce`
+ `aws:VpceAccount`
+ `aws:VpceOrgID`
+ `aws:VpceOrgPaths`
+ `aws:Ec2InstanceSourceVpc`
+ `aws:UserId`
+ `aws:PrincipalServiceName`
+ `aws:PrincipalServiceNamesList`
+ `aws:PrincipalIsAWSService`
+ `lambda:SourceFunctionArn`

Naming a trusted key is not sufficient on its own. You must also constrain the value:
+ String values must not contain wildcards or policy variables.
+ ARN values must not contain wildcards or policy variables in the first five fields of the ARN: `arn`, the partition, the service, the Region, and the account ID. Wildcards in the resource portion are allowed.
+ `aws:PrincipalIsAWSService` must be set to `true`.

The following policy grants principals in your organization the resource-based permission required to invoke the endpoint and is not considered public. An IAM principal in another account also needs identity-based permission.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOrgAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "lambda:InvokeWebFunctionEndpoint",
      "Resource": "arn:aws:lambda:{{us-west-2}}:{{123456789012}}:web-function/{{my-web-function}}/endpoint/{{prod}}",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "{{o-a1b2c3d4e5}}"
        }
      }
    }
  ]
}
```

### Cross-account access
<a name="web-functions-permissions-resource-policy-cross-account"></a>

The following resource-based policy grants a specific IAM role in another account permission to invoke one endpoint of your Web Function. The role also needs identity-based permission to invoke the endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCrossAccountInvoke",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{444455556666}}:role/{{caller-role}}"
            },
            "Action": "lambda:InvokeWebFunctionEndpoint",
            "Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/endpoint/{{prod}}"
        }
    ]
}
```

For cross-account invocation to succeed, all of the following must be true:
+ The caller's identity-based policy grants `lambda:InvokeWebFunctionEndpoint` permission on the endpoint ARN.
+ The resource-based policy on the Web Function grants the caller permission (as shown above).
+ The endpoint uses `IamAuth` authentication so that Lambda evaluates the caller's credentials.

### Granting access to an AWS service
<a name="web-functions-permissions-resource-policy-service"></a>

The following resource-based policy grants the CloudFront service principal permission to invoke your Web Function. Use this policy when you configure a CloudFront distribution with your Web Function endpoint as the origin.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowCloudFrontInvoke",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudfront.amazonaws.com"
            },
            "Action": "lambda:InvokeWebFunctionEndpoint",
            "Resource": "arn:aws:lambda:{{us-east-1}}:{{111122223333}}:web-function/{{my-function}}/endpoint/{{prod}}",
            "Condition": {
                "ArnLike": {
                    "aws:SourceArn": "arn:aws:cloudfront::{{111122223333}}:distribution/{{EDFDVBD6EXAMPLE}}"
                }
            }
        }
    ]
}
```

The `aws:SourceArn` condition restricts access to a specific CloudFront distribution. Without this condition, any CloudFront distribution in any account could invoke your Web Function.

### Replication and eventual consistency
<a name="web-functions-permissions-resource-policy-replication"></a>

When you attach or update a resource-based policy on a Web Function that has **MultiRegion** or **PerRegion** endpoints, Lambda replicates the policy to all replica AWS Regions where the endpoints operate. This replication is eventually consistent.

During the replication window, Lambda might evaluate requests in replica Regions against the previous version of the policy. This means:
+ A newly added permission may not take effect in all Regions immediately.
+ Lambda might still honor a recently removed permission in some Regions until replication completes.

There is no customer-visible completion signal for policy replication. Test the expected allow or deny behavior in every endpoint Region before relying on the new policy. For emergency containment, update traffic routing, or set the endpoint's `throttleConfig.rateLimit` to `0` to block all traffic while the policy change propagates. For more information, see [Throttling](web-functions-scaling.md#web-functions-scaling-throttling).

For **HomeRegion** endpoints, the policy applies only in the home Region and does not require cross-Region replication. A change can still take a short time to take effect.

## Permissions for configuring networking
<a name="web-functions-permissions-networking"></a>

The identity that configures networking needs permission to create or update the relevant Lambda resources. It also needs permission to pass the required roles and connector. Depending on the operation, permissions include:
+ `lambda:CreateNetworkConnector`
+ `lambda:UpdateNetworkConnector`
+ `lambda:GetNetworkConnector`
+ `lambda:CreateWebFunction`
+ `lambda:CreateWebFunctionRevision`
+ `lambda:UpdateWebFunctionEndpoint`
+ `lambda:PassNetworkConnector`
+ `iam:PassRole`

The caller must have `lambda:PassNetworkConnector` on the referenced connector whenever a `create-web-function` or `create-web-function-revision` call sets `egressNetworkConnectorArn`. Scope this permission to approved connector resources. Scope `iam:PassRole` to approved execution roles, which you pass when you create a Web Function or revision, and to approved operator roles, which you pass when you create or update a network connector. For the operator role permissions policy, see [Operator role permissions](web-functions-networking.md#web-functions-networking-vpc-operator-role).