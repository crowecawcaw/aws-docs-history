# Set up IAM permissions and roles for Lambda@Edge

To configure Lambda@Edge, you must have the following IAM permissions and roles for
AWS Lambda:

- [IAM permissions](#lambda-edge-permissions-required "#lambda-edge-permissions-required")
  – These permissions allow you to create your Lambda function and associate
  it with your CloudFront distribution.
- [A Lambda function
  execution role](#lambda-edge-permissions-function-execution "#lambda-edge-permissions-function-execution") (IAM role) – The Lambda service principals
  assume this role to execute your function.
- [Service-linked roles
  for Lambda@Edge](#using-service-linked-roles-lambda-edge "#using-service-linked-roles-lambda-edge") – The service-linked roles allow specific
  AWS services to replicate Lambda functions to AWS Regions and to enable CloudWatch
  to use CloudFront log files.

## IAM permissions required to associate Lambda@Edge functions with CloudFront distributions

In addition to the IAM permissions that you need for Lambda, you need the
following permissions to associate Lambda functions with CloudFront distributions:

- `lambda:GetFunction` – Grants permission to get
  configuration information for your Lambda function and a presigned URL to
  download a `.zip` file that contains the function.
- `lambda:EnableReplication*` – Grants permission to the
  resource policy so that the Lambda replication service can get the function
  code and configuration.
- `lambda:DisableReplication*` – Grants permission to the
  resource policy so that the Lambda replication service can delete the
  function.

###### Important

You must add the asterisk (`*`) at the end of the
`lambda:EnableReplication**\***` and `lambda:DisableReplication**\***` actions.

- For the resource, specify the ARN of the function version that you want to
  execute when a CloudFront event occurs, such as the following example:

`arn:aws:lambda:us-east-1:123456789012:function:`TestFunction`:2`

- `iam:CreateServiceLinkedRole` – Grants permission to
  create a service-linked role that Lambda@Edge uses to replicate Lambda
  functions in CloudFront. After you configure Lambda@Edge for the first time, the
  service-linked role is automatically created for you. You don't need to add
  this permission to other distributions that use Lambda@Edge.
- `cloudfront:UpdateDistribution` or
  `cloudfront:CreateDistribution` – Grants permission to
  update or create a distribution.

For more information, see the following topics:

- [Identity and Access Management for Amazon CloudFront](security-iam.md "security-iam.md")
- [Lambda resource access permissions](../../../lambda/latest/dg/intro-permission-model.md#lambda-intro-execution-role "../../../lambda/latest/dg/intro-permission-model.md#lambda-intro-execution-role") in the
  _AWS Lambda Developer Guide_

## Function execution role for service principals

You must create an IAM role that the `lambda.amazonaws.com` and
`edgelambda.amazonaws.com` service principals can assume when they
execute your function.

###### Tip

When you create your function in the Lambda console, you can choose to create a
new execution role by using an AWS policy template. This step
_automatically_ adds the required Lambda@Edge permissions
to execute your function. See [Step 5 in the
Tutorial: Creating a simple Lambda@Edge function](lambda-edge-how-it-works-tutorial.md#lambda-edge-how-it-works-tutorial-create-function "lambda-edge-how-it-works-tutorial.md#lambda-edge-how-it-works-tutorial-create-function").

For more information about creating an IAM role manually, see [Creating roles and attaching policies (console)](../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md "../../../IAM/latest/UserGuide/access_policies_job-functions_create-policies.md") in
the _IAM User Guide_.

###### Example: Role trust policy

You can add this role under the **Trust Relationship** tab in
the IAM console. Don't add this policy under the
**Permissions** tab.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "lambda.amazonaws.com",
 "edgelambda.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

For more information about the permissions that you need to grant to the execution
role, see [Lambda
resource access permissions](../../../lambda/latest/dg/intro-permission-model.md#lambda-intro-execution-role "../../../lambda/latest/dg/intro-permission-model.md#lambda-intro-execution-role") in the
_AWS Lambda Developer Guide_.

###### Notes

- By default, whenever a CloudFront event triggers a Lambda function, data is
  written to CloudWatch Logs. If you want to use these logs, the execution role
  needs permission to write data to CloudWatch Logs. You can use the predefined
  AWSLambdaBasicExecutionRole to grant permission to
  the execution role.

For more information about CloudWatch Logs, see [Edge function logs](edge-functions-logs.md "edge-functions-logs.md").

- If your Lambda function code accesses other AWS resources, such as
  reading an object from an S3 bucket, the execution role needs permission
  to perform that action.

## Service-linked roles for Lambda@Edge

Lambda@Edge uses IAM [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of
IAM role that is linked directly to a service. Service-linked roles are predefined by the
service and include all of the permissions that the service requires to call other AWS
services on your behalf.

Lambda@Edge uses the following IAM service-linked roles:

- **AWSServiceRoleForLambdaReplicator** – Lambda@Edge uses this role to allow
  Lambda@Edge to replicate functions to AWS Regions.

When you first add a Lambda@Edge trigger in CloudFront, a role named AWSServiceRoleForLambdaReplicator is created
automatically to allow Lambda@Edge to replicate functions to AWS Regions. This role is
required to use Lambda@Edge functions. The ARN for the AWSServiceRoleForLambdaReplicator role looks like the
following example:

`arn:aws:iam::123456789012:role/aws-service-role/replicator.lambda.amazonaws.com/AWSServiceRoleForLambdaReplicator`

- **AWSServiceRoleForCloudFrontLogger** – CloudFront uses this role to push log files
  into CloudWatch. You can use log files to debug Lambda@Edge validation errors.

The AWSServiceRoleForCloudFrontLogger role is created automatically when you add Lambda@Edge function
association to allow CloudFront to push Lambda@Edge error log files to CloudWatch. The ARN for the
AWSServiceRoleForCloudFrontLogger role looks like this:

`arn:aws:iam::account_number:role/aws-service-role/logger.cloudfront.amazonaws.com/AWSServiceRoleForCloudFrontLogger`

A service-linked role makes setting up and using Lambda@Edge easier because you don’t have to
manually add the necessary permissions. Lambda@Edge defines the permissions of its service-linked
roles, and only Lambda@Edge can assume the roles. The defined permissions include the trust
policy and the permissions policy. You can't attach the permissions policy to any other IAM
entity.

You must remove any associated CloudFront or Lambda@Edge resources before you can delete a
service-linked role. This helps protect your Lambda@Edge resources so that you don't remove a
service-linked role that is still required to access active resources.

For more information about service-linked roles, see [Service-linked roles for CloudFront](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked").

### Service-linked role permissions for Lambda@Edge

Lambda@Edge uses two service-linked roles, named **AWSServiceRoleForLambdaReplicator** and
**AWSServiceRoleForCloudFrontLogger**. The following sections describe the permissions for each
of these roles.

###### Contents

- [Service-linked role permissions for Lambda replicator](lambda-edge-permissions.md#slr-permissions-lambda-replicator "lambda-edge-permissions.md#slr-permissions-lambda-replicator")
- [Service-linked role permissions for CloudFront logger](lambda-edge-permissions.md#slr-permissions-cloudfront-logger "lambda-edge-permissions.md#slr-permissions-cloudfront-logger")

#### Service-linked role permissions for Lambda replicator

This service-linked role allows Lambda to replicate Lambda@Edge functions
to AWS Regions.

The AWSServiceRoleForLambdaReplicator service-linked role trusts the `replicator.lambda.amazonaws.com` service
to assume the role.

The role permissions policy allows Lambda@Edge to complete the following actions on the
specified resources:

- `lambda:CreateFunction` on `arn:aws:lambda:*:*:function:*`
- `lambda:DeleteFunction` on `arn:aws:lambda:*:*:function:*`
- `lambda:DisableReplication` on `arn:aws:lambda:*:*:function:*`
- `iam:PassRole` on `all AWS resources`
- `cloudfront:ListDistributionsByLambdaFunction` on `all AWS resources`

#### Service-linked role permissions for CloudFront logger

This service-linked role allows CloudFront to push log files into CloudWatch so that you can debug
Lambda@Edge validation errors.

The AWSServiceRoleForCloudFrontLogger service-linked role trusts the `logger.cloudfront.amazonaws.com`
service to assume the role.

The role permissions policy allows Lambda@Edge to complete the following actions on the
specified `arn:aws:logs:*:*:log-group:/aws/cloudfront/*` resource:

- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:PutLogEvents`

You must configure permissions to allow an IAM entity (such as a user, group, or role)
to delete the Lambda@Edge service-linked roles. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

### Creating service-linked roles for Lambda@Edge

You don’t typically manually create the service-linked roles for Lambda@Edge. The service
creates the roles for you automatically in the following scenarios:

- When you first create a trigger, the service creates the AWSServiceRoleForLambdaReplicator role (if it
  doesn’t already exist). This role allows Lambda to replicate Lambda@Edge functions to
  AWS Regions.

If you delete the service-linked role, the role will be created again when you add a
new trigger for Lambda@Edge in a distribution.

- When you update or create a CloudFront distribution that has a Lambda@Edge association, the
  service creates the AWSServiceRoleForCloudFrontLogger role (if the role doesn’t already exist). This role
  allows CloudFront to push your log files to CloudWatch.

If you delete the service-linked role, the role will be created again when you update
or create a CloudFront distribution that has a Lambda@Edge association.

To manually create these service-linked roles, you can run the following AWS Command Line Interface (AWS CLI)
commands:

###### To create the AWSServiceRoleForLambdaReplicator role

- Run the following command.

```
aws iam create-service-linked-role --aws-service-name replicator.lambda.amazonaws.com
```

###### To create the AWSServiceRoleForCloudFrontLogger role

- Run the following command.

```
aws iam create-service-linked-role --aws-service-name logger.cloudfront.amazonaws.com
```

### Editing Lambda@Edge service-linked roles

Lambda@Edge doesn't allow you to edit the AWSServiceRoleForLambdaReplicator or AWSServiceRoleForCloudFrontLogger service-linked roles.
After the service has created a service-linked role, you can't change the name of the role
because various entities might reference the role. However, you can use IAM to edit the role
description. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

### Supported AWS Regions for Lambda@Edge service-linked roles

CloudFront supports using service-linked roles for Lambda@Edge in the following
AWS Regions:

- US East (N. Virginia) – `us-east-1`
- US East (Ohio) – `us-east-2`
- US West (N. California) – `us-west-1`
- US West (Oregon) – `us-west-2`
- Asia Pacific (Mumbai) – `ap-south-1`
- Asia Pacific (Seoul) – `ap-northeast-2`
- Asia Pacific (Singapore) – `ap-southeast-1`
- Asia Pacific (Sydney) – `ap-southeast-2`
- Asia Pacific (Tokyo) – `ap-northeast-1`
- Europe (Frankfurt) – `eu-central-1`
- Europe (Ireland) – `eu-west-1`
- Europe (London) – `eu-west-2`
- South America (São Paulo) – `sa-east-1`
