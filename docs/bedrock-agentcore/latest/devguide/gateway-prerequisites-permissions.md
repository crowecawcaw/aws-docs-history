# Set up permissions for AgentCore Gateway

Amazon Bedrock AgentCore Gateway can connect to both AWS resources and external
services. This means that along with the standard AWS Identity and Access Management (IAM)
for managing permissions in Amazon Bedrock AgentCore Gateway, the permissions model supports
additional external authentication mechanisms.

When working with Gateways, there are three main categories of permissions to
consider:

1. [Gateway management permissions](#gateway-management-permissions "#gateway-management-permissions") -
   Permissions needed to create and manage Gateways
2. [Gateway Access Permissions or Inbound Auth
   Configuration](#gateway-access-permissions "#gateway-access-permissions") - Who can invoke what via the MCP protocol
3. [Gateway execution permissions](#gateway-execution-permissions "#gateway-execution-permissions") - Permissions provided to a service role to allow the Amazon Bedrock AgentCore service to perform actions on behalf of the identity that invokes the gateway.

###### Topics

- [Gateway Management Permissions](#gateway-management-permissions "#gateway-management-permissions")
- [Gateway Access Permissions or Inbound Auth
  Configuration](#gateway-access-permissions "#gateway-access-permissions")
- [AgentCore Gateway service role permissions](#gateway-execution-permissions "#gateway-execution-permissions")
- [Best practices for Gateway
  permissions](#gateway-prerequisites-best-practices "#gateway-prerequisites-best-practices")

## Gateway Management Permissions

These permissions allow you to create and manage Gateways. You can create a gateway
specific policy (example name `BedrockAgentCoreGatewayFullAccess`) which could
look like:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "bedrock-agentcore:*Gateway*",
 "bedrock-agentcore:*WorkloadIdentity",
 "bedrock-agentcore:*CredentialProvider",
 "bedrock-agentcore:*Token*",
 "bedrock-agentcore:*Access*"
 ],
 "Resource": "arn:aws:bedrock-agentcore:*:*:*gateway*"
 }
 ]
}`

```

You may also need additional permissions for related services:

- `s3:GetObject` and `s3:PutObject` for storing and retrieving
  schemas when you configure targets based on S3
- `kms:Encrypt`, `kms:Decrypt`,
  `kms:GenerateDataKey*` for encryption operations
- Other service-specific permissions based on your Gateway's functionality or
  configuration

For more comprehensive permissions across all AgentCore services, consider using the
`BedrockAgentCoreFullAccess` managed policy, especially when working with
multiple AgentCore products.

If you prefer to follow the principle of least privilege, you can create a custom policy
that grants only specific permissions. Here's an example of a ReadOnly Gateway permission
policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "bedrock-agentcore:ListGateways",
 "bedrock-agentcore:GetGateway",
 "bedrock-agentcore:ListGatewayTargets",
 "bedrock-agentcore:GetGatewayTarget"
 ],
 "Resource": "arn:aws:bedrock-agentcore:*:*:*gateway*"
 }
 ]
}`

```

## Gateway Access Permissions or Inbound Auth

Configuration

Unlike other AWS services, which use standard AWS IAM mechanisms for access control,
Amazon Bedrock AgentCore Gateway uses JWT token-based authentication as specified in the
Model Context Protocol (MCP). These configurations have to be specified as a property of the
gateway.

You'll configure these permissions when [Creating
gateways](gateway-create.md "gateway-create.md") in the next section.

## AgentCore Gateway service role permissions

When creating a gateway, you need a service role that has permissions to assume an IAM role and to access AWS resources and external services on the IAM role's behalf. You can create the service role in the following ways:

- If you create a gateway in the AWS Management Console or through the AgentCore starter toolkit, you can choose to let AgentCore automatically create a service role for you with the necessary permissions. If you prefer this method, you can skip this prerequisite.
- If you prefer to create your own service role for greater customization, you'll need to configure the role with the permissions outlined in this topic. To learn how to create a service role and attach permissions to it, see [Create a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md").

The required permissions for a service role are in the following topics:

###### Topics

- [Trust permissions](#gateway-execution-permissions-trust "#gateway-execution-permissions-trust")
- [Outbound authorization permissions](#gateway-execution-permissions-outbound-auth "#gateway-execution-permissions-outbound-auth")
- [Permissions to access AWS resources](#gateway-execution-permissions-resources "#gateway-execution-permissions-resources")

### Trust permissions

A service role must have a [trust policy](../../../IAM/latest/UserGuide/id_roles.md#term_trust_policy "../../../IAM/latest/UserGuide/id_roles.md#term_trust_policy") attached that allows the AgentCore service to assume an IAM identity and carry out actions on its behalf.

The following is an example of a trust policy that you can use.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "GatewayAssumeRolePolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "bedrock-agentcore.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:bedrock-agentcore:`us-east-1`:`111122223333`:gateway/`gateway-name`-*"
 }
 }
 }
 ]
}`

```

###### Note

Because you won't know the gateway ARN before you create it, you can omit the `Condition` field when you first create the service role. After you create the gateway, add the `Condition` field back to the policy as a best security practice and do the following:

- Replace the `aws:SourceAccount` condition key value with the ID of the account that the gateway belongs to.
- Replace the `aws:SourceArn` condition key with the ARN of the gateway.

### Outbound authorization permissions

Depending on the type of outbound authorization you use for your gateway targets, you need to add permissions to the service role to allow it to invoke the target. These permissions allow the gateway service role to retrieve authorization credentials for invoking the target. You can do this in the process of [setting up outbound authorization](gateway-outbound-auth.md "gateway-outbound-auth.md").

### Permissions to access AWS resources

Depending on your gateway setup or the targets that you choose to add to the gateway, you might need to add permissions to the gateway service role to allow it to access AWS resources. The following topics cover some resources that your gateway service role might need access to:

If you attach a Lambda target to your gateway, you need to add permissions for the AgentCore Gateway service role to be able to invoke the function by doing the following:

- Attach an identity-based policy to the AgentCore Gateway service role that allows the `lambda:InvokeFunction` action on the Lambda function resource.
- (If the function is in a different account from the gateway service role) Attach a resource-based policy to the Lambda function that allows the gateway service role principal to perform the `lambda:InvokeFunction` action on the Lambda function resource.
  Select a topic to learn how to set up the permissions:

###### Topics

- [Attach an identity-based policy to the gateway service role](#gateway-lambda-identity-based-permissions "#gateway-lambda-identity-based-permissions")
- [(If function is in another account) Attach a resource-based policy to the Lambda function](#gateway-lambda-resource-based-permissions "#gateway-lambda-resource-based-permissions")

##### Attach an identity-based policy to the gateway service role

To allow the gateway service role to access a Lambda target, attach the following identity-based policy to your AgentCore Gateway service role by choosing the topic at [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") that pertains to your use case and following the steps..

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "AmazonBedrockAgentCoreGatewayLambdaProd",
        "Effect": "Allow",
        "Action": [
            "lambda:InvokeFunction"
        ],
        "Resource": [
            "arn:aws:lambda:`us-east-1`:`123456789012`:function:`FunctionName`"
        ]
    }]
}
```

Replace the ARN in the `Resource` field with the ARN of your Lambda function gateway target. If your gateway has multiple Lambda targets, you can add the ARN of each function to the `Resource` list.

##### (If function is in another account) Attach a resource-based policy to the Lambda function

If the Lambda function target is in a different account from the gateway service role, you need to attach a resource-based policy to allow the gateway service role to access it. The following is an example policy that you can use:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "LambdaAllowGatewayServiceRoleMyFunction",
            "Effect": "Allow",
            "Principal": {
              "AWS": "arn:aws:iam::`123456789012`:role/`MyGatewayExecutionRole`"
            },
            "Action": "lambda:InvokeFunction",
            "Resource":  "arn:aws:lambda:`us-east-1`:`123456789012`:function:`MyFunction`"
        }
     ]
}
```

Replace the values of the following fields:

- `AWS` – Use the ARN of your gateway service role.
- `Resource` – Use the ARN of your Lambda function.

To learn how to attach a resource-based policy to the Lambda function that allows your gateway service role to access the function, select one of the following methods::

Console

###### To attach a resource-based policy to your Lambda function in the AWS Management Console

1. Follow the steps in the **Console** tab at [Viewing resource-based IAM policies in Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md").
2. In the **Resource-based policy statements** section, choose **Add permissions**.
3. Select **AWS account** and fill out the following fields:
   - **Statement ID** – A unique identifier for the the statement providing permissions for the gateway service role to access the function.
   - **Principal** – Specify the ARN of your gateway service role.
   - **Action** – Select `lambda:InvokeFunction`.

CLI
To attach a resource-based policy to your Lambda function using the AWS CLI, follow the steps at [Granting Lambda function access to AWS services](../../../lambda/latest/dg/permissions-function-services.md "../../../lambda/latest/dg/permissions-function-services.md") and specify your gateway service role as the `principal`.

You can run the following code in a terminal to add permissions for your gateway service role to access the function in `us-east-1`:

```
aws lambda add-permission \
  --function-name "`MyFunction`" \
  --statement-id "GatewayInvoke" \
  --action "lambda:InvokeFunction" \
  --principal "arn:aws:iam::`123456789012`:role/`MyGatewayServiceRole`"
  --region `us-east-1`
```

If you plan to add a Smithy target, you need to add permissions for the gateway service role to access AWS services that your Smithy models refer to. To determine which permissions need to be attached to the service role, refer to that service's documentation.

You can add permissions to the service role by choosing the topic at [Adding and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") that pertains to your use case and following the steps.

For example, if your Smithy model target accesses a DynamoDB table, you can attach the following policy to allow the service role to perform DynamoDB operations on the table:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem",
 "dynamodb:Query",
 "dynamodb:Scan"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/*"
 }
 ]
}`

```

## Best practices for Gateway

permissions

**Follow the principle of least privilege**

- Grant only the permissions necessary for your Gateway to function
- Use specific resource ARNs rather than wildcards when possible
- Regularly review and audit permissions

**Separate roles by function**

- Use different roles for management and execution
- Create separate roles for different Gateways with different purposes

**Secure credential storage**

- Store API keys and OAuth credentials in AWS Secrets Manager
- Rotate credentials regularly

**Monitor and audit**

- Enable CloudTrail logging for Gateway operations
- Regularly review access patterns and permissions usage

**Use conditions in policies**

- Add conditions to limit when and how permissions can be used
- Consider using source IP restrictions for management operations
