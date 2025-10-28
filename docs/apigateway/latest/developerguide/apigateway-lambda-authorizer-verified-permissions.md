# Control access based on an identity’s attributes with Verified Permissions

Use Amazon Verified Permissions to control access to your API Gateway API. When you use API Gateway with Verified Permissions, Verified Permissions creates a Lambda authorizer that uses fine-grained
authorization decisions to control access to your API. Verified Permissions
authorizes callers based on a policy store schema and policies using the Cedar policy
language to define fine-grained permissions for application users. For more information, see [Create a policy store with a connected API and identity provider](../../../verifiedpermissions/latest/userguide/getting-started-api-policy-store.md "../../../verifiedpermissions/latest/userguide/getting-started-api-policy-store.md") in
the _Amazon Verified Permissions User Guide_.

Verified Permissions supports Amazon Cognito user pools or OpenID Connect (OIDC) identity providers as identity sources. Verified Permissions
presumes that the principal has been previously identified and authenticated. Verified Permissions is only supported for Regional and edge-optimized REST APIs.

## Create a Lambda authorizer using Verified Permissions

Verified Permissions creates a Lambda authorizer to determine if a principal is allowed to perform an action on your API.
You create the Cedar policy that Verified Permissions uses to perform its authorization tasks.

The following is an example Cedar policy that allows access to invoke an API based on the Amazon Cognito user pool,
`us-east-1_ABC1234` for the `developer` group on the `GET /users` resource of an
API. Verified Permissions determines group membership by parsing the bearer token for the caller's identity.

```
permit(
  principal in MyAPI::UserGroup::"us-east-1_ABC1234|developer",
  action in [ MyAPI::Action::"get /users" ],
  resource
  );
```

Optionally, Verified Permissions can attach the authorizer to the methods
of your API. On production stages for your API, we recommend that you don't allow Verified Permissions to attach the authorizer for you.

The following list show how to configure Verified Permissions to attach or not to attach the Lambda authorizer to the method request of your API's methods.

**Attach the authorizer for you (AWS Management Console)**

When you choose **Create policy store** in the Verified Permissions console, on the **Deploy
app integration** page, choose **Now**.

**Don't attach the authorizer for you (AWS Management Console)**

When you choose **Create policy store** in the Verified Permissions console, on the **Deploy
app integration** page, choose **Later**.

Verified Permissions still creates a Lambda authorizer for you. The Lambda authorizer starts with `AVPAuthorizerLambda-`. For more instructions on how to attach
your authorizer on a method, see [Configure a method to use a Lambda authorizer (console)](configure-api-gateway-lambda-authorization.md#configure-api-gateway-lambda-authorization-method-console "configure-api-gateway-lambda-authorization.md#configure-api-gateway-lambda-authorization-method-console").

**Attach the authorizer for you (AWS CloudFormation)**

In the Verified Permissions-generated AWS CloudFormation template, in the `Conditions` section, set `"Ref":
 "shouldAttachAuthorizer"` to `true`.

**Don't attach the authorizer for you (AWS CloudFormation)**

In the Verified Permissions-generated AWS CloudFormation template, in the `Conditions` section, set `"Ref":
 "shouldAttachAuthorizer"` to `false`.

Verified Permissions still creates a Lambda authorizer for you. The Lambda authorizer starts with `AVPAuthorizerLambda-`. For more instructions on how to attach
your authorizer on a method, see [Configure a method to use a Lambda authorizer (AWS CLI)](configure-api-gateway-lambda-authorization.md#configure-api-gateway-lambda-authorization-method-cli "configure-api-gateway-lambda-authorization.md#configure-api-gateway-lambda-authorization-method-cli").

## Call a Lambda authorizer using Verified Permissions

You can call your Lambda authorizer by providing an identity or access token in the
`Authorization` header. For more information, see [Call an API with an API Gateway Lambda authorizer](call-api-with-api-gateway-lambda-authorization.md "call-api-with-api-gateway-lambda-authorization.md").

API Gateway caches the policy that your Lambda authorizer
returns for 120 seconds. You can modify the TTL in the API Gateway console or by using the
AWS CLI.
