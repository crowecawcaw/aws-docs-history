# Authorization with Amazon Verified Permissions

[Amazon Verified Permissions](../../../verifiedpermissions/latest/userguide/what-is-avp.md "../../../verifiedpermissions/latest/userguide/what-is-avp.md") is an authorization service for the applications that you build. When you
add an Amazon Cognito user pool as an identity source, your app can pass user pool access or identity
(ID) tokens to Verified Permissions for an allow or deny decision. Verified Permissions considers your user's properties and
request context based on policies that you write in [Cedar Policy Language](https://docs.cedarpolicy.com/ "https://docs.cedarpolicy.com/"). The request context can include an identifier for the document, image,
or other resource they requested, and the action that your user wants to take on the
resource.

Your app can provide your user's identity or access tokens to Verified Permissions in [IsAuthorizedWithToken](../../../verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.md "../../../verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.md") or [BatchIsAuthorizedWithToken](../../../verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.md "../../../verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.md") API requests. These API operations accept your users as
a `Principal` and make authorization decisions for the `Action` on the
`Resource` that they want to access. Additional custom `Context` can
contribute to a detailed access decision.

When your app presents a token in an `IsAuthorizedWithToken` API request, Verified Permissions
performs the following validations.

1. Your user pool is a configured Verified Permissions [identity
   source](../../../verifiedpermissions/latest/userguide/identity-providers.md "../../../verifiedpermissions/latest/userguide/identity-providers.md") for the requested policy store.
2. The `client_id` or `aud` claim, in your access or identity token
   respectively, matches a user pool app client ID that you provided to Verified Permissions. To verify this
   claim, you must [configure client
   ID validation](../../../verifiedpermissions/latest/userguide/identity-sources_create.md "../../../verifiedpermissions/latest/userguide/identity-sources_create.md") in your Verified Permissions identity source.
3. Your token isn't expired.
4. The value of the `token_use` claim in your token matches the parameters
   that you passed to `IsAuthorizedWithToken`. The `token_use` claim
   must be `access` if you passed it to the `accessToken` parameter,
   and `id` if you passed it to the `identityToken` parameter.
5. The signature in your token comes from the published JSON web keys (JWKs) of your user
   pool. You can view your JWKs at `https://cognito-idp.*`Region`*.amazonaws.com/*`your user pool
   ID`*/.well-known/jwks.json`.

###### Revoked tokens and deleted users

Verified Permissions only validates the information it knows from your identity source and from the
expiration time of your user's token. Verified Permissions doesn't check for token revocation or user
existence. If you revoked your user's token or deleted your user's profile from your user
pool, Verified Permissions still considers the token valid until it expires.

###### Policy evaluation

Configure your user pool as an [identity source](../../../verifiedpermissions/latest/userguide/identity-providers.md "../../../verifiedpermissions/latest/userguide/identity-providers.md")
for your [policy
store](../../../verifiedpermissions/latest/userguide/terminology.md#term-policy-store "../../../verifiedpermissions/latest/userguide/terminology.md#term-policy-store"). Configure your app to submit your users' tokens in requests to Verified Permissions. For
each request, Verified Permissions compares the claims in the token to a policy. A Verified Permissions policy is like an
IAM policy in AWS. It declares a _principal_, _resource_, and _action_. Verified Permissions
responds to your request with `Allow` if it matches an allowed action and doesn't
match an explicit `Deny` action; otherwise, it responds with `Deny`.
For more information, see [Amazon Verified Permissions policies](../../../verifiedpermissions/latest/userguide/policies.md "../../../verifiedpermissions/latest/userguide/policies.md") in the
_Amazon Verified Permissions User Guide_.

###### Customizing tokens

To change, add, and remove the user claims that you want to present to Verified Permissions, customize
the content in your access and identity tokens with a [Pre token generation Lambda
trigger](user-pool-lambda-pre-token-generation.md "user-pool-lambda-pre-token-generation.md"). With a pre token generation trigger,
you can add and modify claims in your tokens. For example, you can query a database for
additional user attributes and encode them into your ID token.

###### Note

Because of the way that Verified Permissions processes claims, don't add claims named
`cognito`, `dev`, or `custom` in your pre token
generation function. When you present these reserved claim prefixes not in colon-delimited
format like `cognito:username` but as full claim names, your authorization
requests fail.

###### Additional resources

- [Mapping Amazon Cognito tokens to Verified Permissions schema](../../../verifiedpermissions/latest/userguide/identity-sources_map-token-to-schema.md "../../../verifiedpermissions/latest/userguide/identity-sources_map-token-to-schema.md")
- [Authorize API Gateway APIs using Amazon Verified Permissions and Amazon Cognito](https://aws.amazon.com/blogs/security/authorize-api-gateway-apis-using-amazon-verified-permissions-and-amazon-cognito/ "https://aws.amazon.com/blogs/security/authorize-api-gateway-apis-using-amazon-verified-permissions-and-amazon-cognito/")
- [Workshop: Authentication and authorization with Amazon Cognito and Verified Permissions](https://catalog.workshops.aws/app-auth "https://catalog.workshops.aws/app-auth")

## API authorization

with Verified Permissions

Your ID or access tokens can authorize requests to back-end Amazon API Gateway REST APIs with
Verified Permissions. You can create a [policy store](../../../verifiedpermissions/latest/userguide/policy-stores.md "../../../verifiedpermissions/latest/userguide/policy-stores.md") with
immediate links to your user pool and API. With the [Set up with API Gateway and
an identity source](../../../verifiedpermissions/latest/userguide/policy-stores_create.md "../../../verifiedpermissions/latest/userguide/policy-stores_create.md") starting option, Verified Permissions adds a user pool identity source to the
policy store, and a Lambda authorizer to the API. When your application passes a user pool
bearer token to the API, the Lambda authorizer invokes Verified Permissions. The authorizer passes the token
as a principal and the request path and method as an action.

The following diagram illustrates the authorization flow for an API Gateway API with Verified Permissions.
For a detailed breakdown, see [API-linked
policy stores](../../../verifiedpermissions/latest/userguide/policy-stores_api-userpool.md "../../../verifiedpermissions/latest/userguide/policy-stores_api-userpool.md") in the Amazon Verified Permissions User Guide.

![A diagram that illustrates the flow of API authorization with Amazon Verified Permissions. An application makes a request to an Amazon API Gateway API. The API invokes a Lambda authorizer. The authorizer makes an API request to Verified Permissions. Verified Permissions checks token validity and returns an authorization decision.](images/amazon-cognito-avp-use-case.png)

Verified Permissions structures API authorization around [user pool groups](cognito-user-pools-user-groups.md "cognito-user-pools-user-groups.md"). Because both ID and access tokens include a
`cognito:groups` claim, your policy store can manage role-based access control
(RBAC) for your APIs in a variety of application contexts.

### Choosing policy store settings

When you configure an identity source on a policy store, you must choose whether you
want to process access or ID tokens. This decision is significant to the way that your
policy engine operates. ID tokens contain user attributes. Access tokens contain user
access-control information: [OAuth scopes](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md"). Although both token types have group-membership information, we
generally recommend the access token for RBAC with a Verified Permissions policy store. The access token
adds to group membership with scopes that can contribute to the authorization decision.
The claims in an access token become [context](../../../verifiedpermissions/latest/userguide/context.md "../../../verifiedpermissions/latest/userguide/context.md") in the
authorization request.

You must also configure the user and group entity types when you configure a user pool
as an identity source. Entity types are principal, action, and resource identifiers that
you can reference in Verified Permissions policies. Entities in policy stores can have a _membership_ relationship, where one entity can be a member of a
_parent_ entity. With membership, you can reference
principal groups, action groups, and resource groups. In the case of user pool groups, the
user entity type that you specify must be a member of the group entity type. When you set
up an [API-linked
policy store](../../../verifiedpermissions/latest/userguide/policy-stores_api-userpool.md "../../../verifiedpermissions/latest/userguide/policy-stores_api-userpool.md") or follow **Guided setup** in the Verified Permissions console,
your policy store automatically has this parent-member relationship.

The ID token can combine RBAC with attribute-based access control (ABAC). After you
create an [API-linked
policy store](../../../verifiedpermissions/latest/userguide/policy-stores_api-userpool.md "../../../verifiedpermissions/latest/userguide/policy-stores_api-userpool.md"), you can enhance your policies with [user attributes](#amazon-cognito-authorization-with-avp-example-policy "#amazon-cognito-authorization-with-avp-example-policy")
_and_ group membership. The attribute claims in an ID
token become [principal
attributes](../../../verifiedpermissions/latest/userguide/policies_examples-abac.md "../../../verifiedpermissions/latest/userguide/policies_examples-abac.md") in the authorization request. Your policies can make authorization
decisions based on principal attributes.

You can also configure a policy store to accept tokens with an `aud` or
`client_id` claim that matches a list of acceptable app clients that you
provide.

### Example

policy for role-based API authorization

The following example policy was created by the setup of a Verified Permissions policy store for a
[PetStore](../../../apigateway/latest/developerguide/api-gateway-create-api-from-example.md "../../../apigateway/latest/developerguide/api-gateway-create-api-from-example.md") example REST API.

```
permit(
  principal in PetStore::UserGroup::"us-east-1_EXAMPLE|MyGroup",
  action in [ PetStore::Action::"get /pets", PetStore::Action::"get /pets/{petId}" ],
  resource
  );
```

Verified Permissions returns an `Allow` decision to the authorization request from your
application when:

1. Your application passed an ID or access token in an `Authorization`
   header as a bearer token.
2. Your application passed a token with a `cognito:groups` claim that
   contains the string `MyGroup`.
3. Your application made an `HTTP GET` request to, for example,
   `https://myapi.example.com/pets` or
   `https://myapi.example.com/pets/scrappy`.

## Example policy for an

Amazon Cognito user

Your user pool can also generate authorization requests to Verified Permissions in conditions other
than API requests. You can submit any access control decisions in your application to your
policy store. For example, you can supplement Amazon DynamoDB or Amazon S3 security with
attribute-based access control before any requests transit the network, reducing quota
use.

The following example uses the [Cedar Policy Language](https://docs.cedarpolicy.com/ "https://docs.cedarpolicy.com/") to permit Finance users who authenticate with one user pool app
client to read and write `example_image.png`. John, a user in your app, receives
an ID token from your app client and passes it in a GET request to a URL that requires
authorization, `https://example.com/images/example_image.png`. John's ID token
has an `aud` claim of your user pool app client ID
`1234567890example`. Your pre token generation Lambda function also inserted a new
claim `costCenter` with a value, for John, of `Finance1234`.

```
permit (
   principal,
   actions in [ExampleCorp::Action::"readFile", "writeFile"],
   resource == ExampleCorp::Photo::"example_image.png"
)
when {
   principal.aud == "1234567890example" &&
   principal.custom.costCenter like "Finance*"
};
```

The following request body results in an `Allow` response.

```
{
   "accesstoken": "`[John's ID token]`",
   "action": {
      "actionId": "readFile",
      "actionType": "Action"
   },
   "resource": {
      "entityId": "example_image.png",
      "entityType": "Photo"
   }
}
```

When you want to specify a principal in a Verified Permissions policy, use the following format:

```
permit (
   principal == [Namespace]::[Entity]::"[user pool ID]|[user sub]",
   action,
   resource
);
```

The following is an example principal for a user in a user pool with ID
`us-east-1_Example` with sub, or user ID,
`973db890-092c-49e4-a9d0-912a4c0a20c7`.

```
principal == `ExampleCorp`::`User`::"`us-east-1_Example`|`973db890-092c-49e4-a9d0-912a4c0a20c7`",
```

When you want to specify a user group in a Verified Permissions policy, use the following
format:

```
permit (
   principal in [Namespace]::[Group Entity]::"[Group name]",
   action,
   resource
);
```

###### Attribute-based access control

Authorization with Verified Permissions for your apps, and the [attributes for
access control](attributes-for-access-control.md "attributes-for-access-control.md") feature of Amazon Cognito identity pools for AWS credentials, are both
forms of attribute-based access control (ABAC). The following is a comparison of the
features of Verified Permissions and Amazon Cognito ABAC. In ABAC, a system examines the attributes of an entity and
makes an authorization decision from conditions that you define.

| Service                                                       | Process                                                                                                                                                                                                                                                       | Result                                                                                 |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Amazon Verified Permissions                                   | Returns an `Allow` or `Deny` decision from analysis of a user<br>pool JWT.                                                                                                                                                                                    | Access to application resources succeeds or fails based on Cedar policy<br>evaluation. |
| Amazon Cognito identity pools (attributes for access control) | Assigns [session tags](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md") to your user based on their attributes. IAM policy conditions<br>can check tags `Allow` or `Deny` user access to<br>AWS services. | A tagged session with temporary AWS credentials for an IAM role.                       |
