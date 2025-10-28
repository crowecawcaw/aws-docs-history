# Troubleshooting API-linked policy stores

Use the information here to help you diagnose and fix common issues when you build
Amazon Verified Permissions API-linked policy stores.

###### Topics

- [I updated my policy but the authorization decision didn't change](#policy-stores-api-userpool-considerations-troubleshooting-update-didnt-change "#policy-stores-api-userpool-considerations-troubleshooting-update-didnt-change")
- [I attached the Lambda authorizer to my API but it's not generating authorization
  requests](#policy-stores-api-userpool-considerations-troubleshooting-attached-not-deployed "#policy-stores-api-userpool-considerations-troubleshooting-attached-not-deployed")
- [I received an unexpected authorization decision and want to review the
  authorization logic](#policy-stores-api-userpool-considerations-troubleshooting-review-code "#policy-stores-api-userpool-considerations-troubleshooting-review-code")
- [I
  want to find logs from my Lambda authorizer](#policy-stores-api-userpool-considerations-troubleshooting-find-logs "#policy-stores-api-userpool-considerations-troubleshooting-find-logs")
- [My Lambda authorizer doesn't exist](#policy-stores-api-userpool-considerations-troubleshooting-didnt-deploy "#policy-stores-api-userpool-considerations-troubleshooting-didnt-deploy")
- [My API is in a private VPC and can't invoke the authorizer](#policy-stores-api-userpool-considerations-troubleshooting-in-a-vpc "#policy-stores-api-userpool-considerations-troubleshooting-in-a-vpc")
- [I
  want to process additional user attributes in my authorization model](#policy-stores-api-userpool-considerations-troubleshooting-fgac "#policy-stores-api-userpool-considerations-troubleshooting-fgac")
- [I want to add new actions, action context attributes, or resource
  attributes](#policy-stores-api-userpool-considerations-troubleshooting-action-resource-attributes "#policy-stores-api-userpool-considerations-troubleshooting-action-resource-attributes")

## I updated my policy but the authorization decision didn't change

By default, Verified Permissions configures the Lambda authorizer to cache authorization decisions
for 120 seconds. Try again after two minutes, or disable cache on your authorizer.
For more information, see [Enabling API
caching to enhance responsiveness](../../../apigateway/latest/developerguide/api-gateway-caching.md "../../../apigateway/latest/developerguide/api-gateway-caching.md") in the _Amazon API Gateway Developer Guide_.

## I attached the Lambda authorizer to my API but it's not generating authorization

requests

To begin processing requests, you must deploy the API stage that you attached your
authorizer to. For more information, see [Deploying a REST
API](../../../apigateway/latest/developerguide/how-to-deploy-api.md "../../../apigateway/latest/developerguide/how-to-deploy-api.md") in the _Amazon API Gateway Developer
Guide_.

## I received an unexpected authorization decision and want to review the

authorization logic

The API-linked policy store process creates a Lambda function for your authorizer. Verified Permissions
automatically builds the logic of your authorization decisions into the authorizer
function. You can go back after you create your policy store to review and update the logic
in the function.

To locate your Lambda function from the AWS CloudFormation console, choose the
**Check deployment** button on the
**Overview** page of your new policy store.

You can also locate your function in the AWS Lambda console. Navigate to the
console in the AWS Region of your policy store and search for a function name with a
prefix of `AVPAuthorizerLambda`. If you have create more than one
API-linked policy store, use the **Last modified** time of your functions
to correlate them with policy store creation.

## I

want to find logs from my Lambda authorizer

Lambda functions collect metrics and log their invocation results in Amazon CloudWatch. To
review your logs, [locate your function](#policy-stores-api-userpool-considerations-troubleshooting-review-code "#policy-stores-api-userpool-considerations-troubleshooting-review-code") in the Lambda console and choose the
**Monitor** tab. Select **View CloudWatch logs** and
review the entries in the log group.

For more information about Lambda function logs, see [Using Amazon CloudWatch Logs with
AWS Lambda](../../../lambda/latest/dg/monitoring-cloudwatchlogs.md "../../../lambda/latest/dg/monitoring-cloudwatchlogs.md") in the _AWS Lambda Developer
Guide_.

## My Lambda authorizer doesn't exist

After you complete setup of an API-linked policy store, you must attach the Lambda
authorizer to your API. If you can't locate your authorizer in the API Gateway console,
the additional resources for your policy store might have failed or not deployed yet.
API-linked policy stores deploy these resources in an AWS CloudFormation stack.

Verified Permissions displays a link with the label **Check deployment** at the
end of the creation process. If you already navigated away from this screen, go to
the CloudFormation console and search recent stacks for a name that's prefixed with
`AVPAuthorizer-<policy store ID>`. CloudFormation provides valuable
troubleshooting information in the output of a stack deployment.

For help troubleshooting CloudFormation stacks, see [Troubleshooting
CloudFormation](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md") in the _AWS CloudFormation User
Guide_.

## My API is in a private VPC and can't invoke the authorizer

Verified Permissions doesn't support access to Lambda authorizers through VPC endpoints. You must
open a network path between your API and the Lambda function that serves as your
authorizer.

## I

want to process additional user attributes in my authorization model

The API-linked policy store process derives Verified Permissions policies from the groups claim in users'
tokens. To update your authorization model to consider additional user attributes,
integrate those attributes in your policies.

You can map many claims in ID and access tokens from Amazon Cognito user pools to Verified Permissions policy
statements. For example, most users have an `email` claim in their ID
token. For more information about adding claims from your identity source to
policies, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

## I want to add new actions, action context attributes, or resource

attributes

An API-linked policy store and the Lambda authorizer that it creates are a point-in-time
resource. They reflect the state of your API at the time of creation. The policy store
schema doesn't assign any context attributes to actions, nor any attributes or
parents to the default `Application` resource.

When you add actions—paths and methods—to your API, you must update
your policy store to be aware of the new actions. You must also update your Lambda authorizer
to process authorization requests for the new actions. You can [start again with a new policy store](policy-stores-create.md "policy-stores-create.md") or you can
update your existing policy store.

To update your existing policy store, [locate your function](#policy-stores-api-userpool-considerations-troubleshooting-review-code "#policy-stores-api-userpool-considerations-troubleshooting-review-code"). Examine the logic in the automatically-generated
function and update it to process the new actions, attributes, or context. Then
[edit your schema](schema-edit.md "schema-edit.md") to include the new
actions and attributes.
