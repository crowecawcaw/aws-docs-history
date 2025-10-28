# Mapping Amazon Cognito tokens to

schema

You might find that you want to add an identity source to a policy store and map provider
claims, or tokens, to your policy store schema. You can automate this process, by using the [Guided
setup](policy-stores-create.md "policy-stores-create.md") to create your policy store with an identity source, or update your schema manually after the policy store is created.
Once you have mapped the tokens to the schema you can create policies that reference
them.

This section of the user guide has the following information:

- When you can automatically populate attributes to a policy store schema
- How to use Amazon Cognito token claims in your Verified Permissions policies
- How to manually build a schema for an identity source
  [API-linked policy stores](policy-stores-api-userpool.md "policy-stores-api-userpool.md") and policy stores with
  an identity source that were created through [Guided
  setup](policy-stores-create.md "policy-stores-create.md") don't require manual mapping of identity (ID) token attributes to schema.
  You can provide Verified Permissions with the attributes in your user pool and create a schema that is
  populated with user attributes. In ID token authorization, Verified Permissions maps claims to attributes
  of a principal entity. You might need to manually map Amazon Cognito tokens to your schema in the
  following conditions:

- You created an empty policy store or policy store from a sample.
- You want to extend your use of access tokens beyond role-based access control
  (RBAC).
- You create policy stores with the Verified Permissions REST API, an AWS SDK, or the AWS CDK.
  To use Amazon Cognito as an identity source in your Verified Permissions policy store,
  you must have provider attributes in your schema. The schema is fixed and must correspond to
  the entities that provider tokens create in [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md") or
  [BatchIsAuthorizedWithToken](../apireference/API_BatchIsAuthorizedWithToken.md "../apireference/API_BatchIsAuthorizedWithToken.md") API requests. If you created your policy store in a
  way that automatically populates your schema from provider information in an ID token,
  you're ready to write policies. If you create a policy store without a schema for your identity
  source, you must add provider attributes to the schema that match the entities created using
  API requests. Then you can write policies using attributes from the provider token.

For more information about using Amazon Cognito ID and access tokens for authenticated users in
Verified Permissions, see [Authorization with Amazon Verified Permissions](../../../cognito/latest/developerguide/amazon-cognito-authorization-with-avp.md "../../../cognito/latest/developerguide/amazon-cognito-authorization-with-avp.md") in the
_Amazon Cognito Developer Guide_.

###### Topics

- [Mapping ID tokens to schema](#cognito-map-id-token "#cognito-map-id-token")
- [Mapping access tokens](#cognito-map-access-token "#cognito-map-access-token")
- [Alternative notation for Amazon Cognito
  colon-delimited claims](#cognito-colon-claims "#cognito-colon-claims")
- [Things to know
  about schema mapping](#cognito-map-token-to-schema-things-to-know "#cognito-map-token-to-schema-things-to-know")

## Mapping ID tokens to schema

Verified Permissions processes ID token claims as the attributes of the user: their names and titles,
their group membership, their contact information. ID tokens are most useful in an
_attribute-based access control_ (ABAC)
authorization model. When you want Verified Permissions to analyze access to resources based on who's
making the request, choose ID tokens for your identity source.

Amazon Cognito ID tokens work with most [OIDC relying-party libraries](https://openid.net/developers/certified-openid-connect-implementations/ "https://openid.net/developers/certified-openid-connect-implementations/"). They extend the
features of OIDC with additional claims. Your application can authenticate the user
with Amazon Cognito user pools authentication API operations, or with the user pool hosted UI. For
more information, see [Using the API
and endpoints](../../../cognito/latest/developerguide/user-pools-API-operations.md "../../../cognito/latest/developerguide/user-pools-API-operations.md") in the _Amazon Cognito Developer
Guide_.

###### Useful claims in Amazon Cognito ID tokens

_`cognito:username` and `preferred_username`_

Variants of the user's username.

_`sub`_

The user's unique user identifier (UUID)

_Claims with a `custom:` prefix_

A prefix for custom user pool attributes like
`custom:employmentStoreCode`.

_Standard claims_

Standard OIDC claims like `email` and
`phone_number`. For more information, see [Standard claims](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims "https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims") in _OpenID Connect
Core 1.0 incorporating errata set 2_.

_`cognito:groups`_

A user's group memberships. In an authorization model based on
role-based access control (RBAC), this claim presents the roles that you
can evaluate in your policies.

_Transient claims_

Claims that aren't a property of the user, but are added at runtime by
a user pool [Pre token generation Lambda trigger](../../../cognito/latest/developerguide/user-pool-lambda-pre-token-generation.md "../../../cognito/latest/developerguide/user-pool-lambda-pre-token-generation.md"). Transient claims
resemble standard claims but are outside the standard, for example
`tenant` or `department`.

In policies that reference Amazon Cognito attributes that have a `:` separator,
reference the attributes in the format
`principal["`cognito:username`"]`. The
roles claim `cognito:groups` is an exception to this rule. Verified Permissions maps the
contents of this claim to parent entities of the user entity.

For more information about the structure of ID tokens from Amazon Cognito user pools, see [Using the ID token](../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.md "../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.md") in the _Amazon Cognito Developer
Guide_.

The following example ID token has each of the four types of attributes. It
includes the Amazon Cognito-specific claim `cognito:username`, the custom claim
`custom:employmentStoreCode`, the standard claim `email`,
and the transient claim `tenant`.

```
{
    "sub": "91eb4550-XXX",
    "cognito:groups": [
        "Store-Owner-Role",
        "Customer"
    ],
    "email_verified": true,
    "clearance": "confidential",
    "iss": "https://cognito-idp.us-east-2.amazonaws.com/us-east-2_EXAMPLE",
    "cognito:username": "alice",
    "custom:employmentStoreCode": "petstore-dallas",
    "origin_jti": "5b9f50a3-05da-454a-8b99-b79c2349de77",
    "aud": "1example23456789",
    "event_id": "0ed5ad5c-7182-4ecf-XXX",
    "token_use": "id",
    "auth_time": 1687885407,
    "department": "engineering",
    "exp": 1687889006,
    "iat": 1687885407,
    "tenant": "x11app-tenant-1",
    "jti": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111",
    "email": "alice@example.com"
}
```

When you create an identity source with your Amazon Cognito user pool, you specify the type
of principal entity that Verified Permissions generates in authorization requests with
`IsAuthorizedWithToken`. Your policies can then test attributes of
that principal as part of evaluating that request. Your schema defines the principal
type and attributes for an identity source, and then you can reference them in your
Cedar policies.

You also specify the type of group entity that you want to derive from the ID
token groups claim. In authorization requests, Verified Permissions maps each member of the groups
claim to that group entity type. In policies, you can reference that group entity as
the principal.

The following example shows how to reflect the attributes from the example
identity token in your Verified Permissions schema. For more information about editing your schema,
see [Editing policy store schemas](schema-edit.md "schema-edit.md"). If your
identity source configuration specifies the principal type `User`, then
you can include something similar to the following example to make those attributes
available to Cedar.

```
"User": {
   "shape": {
      "type": "Record",
      "attributes": {
         "cognito:username": {
            "type": "String",
            "required": false
         },
         "custom:employmentStoreCode": {
            "type": "String",
            "required": false
         },
         "email": {
            "type": "String"
         },
         "tenant": {
            "type": "String",
            "required": true
         }
      }
   }
}
```

For an example policy that will validate against this schema, see [Reflects Amazon Cognito ID token
attributes](policies-examples.md#policies-examples-cognito-id "policies-examples.md#policies-examples-cognito-id").

## Mapping access tokens

Verified Permissions processes access-token claims other than the groups claim as attributes of the
action, or _context attributes_. Along with group
membership, the access tokens from your IdP might contain information about API access.
Access tokens are useful in authorization models that use role-based access control
(RBAC). Authorization models that rely on access-token claims other than group
membership require additional effort in schema configuration.

Amazon Cognito access tokens have claims that can be used for authorization:

###### Useful claims in Amazon Cognito access tokens

_`client_id`_

The ID of the client application of an OIDC relying party. With the
client ID, Verified Permissions can verify that the authorization request comes from a
permitted client for the policy store. In machine-to-machine (M2M)
authorization, the requesting system authorizes a request with a client
secret and provides the client ID and scopes as evidence of
authorization.

_`scope`_

The [OAuth 2.0 scopes](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3 "https://datatracker.ietf.org/doc/html/rfc6749#section-3.3") that represent the access permissions of
the bearer of the token.

_`cognito:groups`_

A user's group memberships. In an authorization model based on
role-based access control (RBAC), this claim presents the roles that you
can evaluate in your policies.

_Transient claims_

Claims that aren't an access permission, but are added at runtime by a
user pool [Pre token generation Lambda trigger](../../../cognito/latest/developerguide/user-pool-lambda-pre-token-generation.md "../../../cognito/latest/developerguide/user-pool-lambda-pre-token-generation.md"). Transient claims
resemble standard claims but are outside the standard, for example
`tenant` or `department`. Customization of
access tokens adds cost to your AWS bill.

For more information about the structure of access tokens from Amazon Cognito user pools, see [Using the access token](../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.md "../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.md") in the _Amazon Cognito Developer
Guide_.

An Amazon Cognito access token is mapped to a context object when passed to Verified Permissions.
Attributes of the access token can be referenced using
`context.token.`attribute_name``. The
 following example access token includes both the `client_id`and
`scope` claims.

```
{
    "sub": "91eb4550-9091-708c-a7a6-9758ef8b6b1e",
    "cognito:groups": [
        "Store-Owner-Role",
        "Customer"
    ],
    "iss": "https://cognito-idp.us-east-2.amazonaws.com/us-east-2_EXAMPLE",
    "client_id": "1example23456789",
    "origin_jti": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN1111111",
    "event_id": "bda909cb-3e29-4bb8-83e3-ce6808f49011",
    "token_use": "access",
    "scope": "MyAPI/mydata.write",
    "auth_time": 1688092966,
    "exp": 1688096566,
    "iat": 1688092966,
    "jti": "a1b2c3d4-e5f6-a1b2-c3d4-TOKEN2222222",
    "username": "alice"
}
```

The following example shows how to reflect the attributes from the example access
token in your Verified Permissions schema. For more information about editing your schema, see
[Editing policy store schemas](schema-edit.md "schema-edit.md").

```
{
   "MyApplication": {
      "actions": {
         "Read": {
            "appliesTo": {
               "context": {
                  "type": "ReusedContext"
               },
               "resourceTypes": [
                  "Application"
               ],
               "principalTypes": [
                  "User"
               ]
            }
         }
      },
      ...
      ...
      "commonTypes": {
         "ReusedContext": {
            "attributes": {
               "token": {
                  "type": "Record",
                  "attributes": {
                     "scope": {
                        "type": "Set",
                        "element": {
                           "type": "String"
                        }
                     },
                     "client_id": {
                        "type": "String"
                     }
                  }
               }
            },
            "type": "Record"
         }
      }
   }
}
```

For an example policy that will validate against this schema, see [Reflects Amazon Cognito access token
attributes](policies-examples.md#policies-examples-cognito-access "policies-examples.md#policies-examples-cognito-access").

## Alternative notation for Amazon Cognito

colon-delimited claims

At the time that Verified Permissions launched, the recommended schema for Amazon Cognito token claims like
`cognito:groups` and `custom:store` converted these
colon-delimited strings to use the `.` character as a hierarchy delimiter.
This format is called _dot notation_. For example, a
reference to `cognito:groups` became `principal.cognito.groups` in
your policies. Although you can continue to use this format, we recommend that you build
your schema and policies with [bracket
notation](#cognito-map-token-to-schema-things-to-know "#cognito-map-token-to-schema-things-to-know"). In this format, a reference to `cognito:groups` becomes
`principal["cognito:groups"]` in your policies. Automatically-generated
schemas for user pool ID tokens from the Verified Permissions console use bracket notation.

You can continue to use dot notation in manually-built schema and policies for Amazon Cognito
identity sources. You can't use dot notation with `:` or any other
non-alphanumeric characters in schema or policies for any other type of OIDC IdP.

A schema for dot notation nests each instance of a `:` character as a child
of the `cognito` or `custom` initial phrase, as shown in the
following example:

```
"CognitoUser": {
   "shape": {
      "type": "Record",
      "attributes": {
         "cognito": {
            "type": "Record",
            "required": true,
            "attributes": {
               "username": {
                  "type": "String",
                  "required": true
               }
            }
         },
         "custom": {
            "type": "Record",
            "required": true,
            "attributes": {
               "employmentStoreCode": {
                  "type": "String",
                  "required": true
               }
            }
         },
         "email": {
            "type": "String"
         },
         "tenant": {
            "type": "String",
            "required": true
         }
      }
   }
}
```

For an example policy that will validate against this schema and use dot notation, see
[Uses dot notation to reference
attributes](policies-examples.md#policies-examples-dot "policies-examples.md#policies-examples-dot").

## Things to know

about schema mapping

###### Attribute mapping differs between token types

In access token authorization, Verified Permissions maps claims to [context](context.md "context.md"). In ID token authorization, Verified Permissions maps claims to principal
attributes. For policy stores that you create in the Verified Permissions console, only
**empty** and **sample** policy stores leave you
with no identity source and require you to populate your schema with user pool
attributes for ID token authorization. Access token authorization is based on
role-based access control (RBAC) with group-membership claims and doesn't
automatically map other claims to the policy store schema.

###### Identity source attributes aren't required

When you create an identity source in the Verified Permissions console, no attributes are marked
as required. This prevents missing claims from causing validation errors in
authorization requests. You can set attributes to required as needed, but they must
be present in all authorization requests.

###### RBAC doesn't require attributes in schema

Schemas for identity sources depend on the entity associations that you make when
you add your identity source. An identity source maps one claim to a user entity
type, and one claim to a group entity type. These entity mappings are the core of an
identity-source configuration. With this minimum information, you can write policies
that perform authorization actions for specific users and specific groups that users
might be members of, in a role-based access control (RBAC) model. The addition of
token claims to the schema extends the authorization scope of your policy store.
User attributes from ID tokens have information about users that can contribute to
attribute-based access control (ABAC) authorization. Context attributes from access
tokens have information like OAuth 2.0 scopes that can contribute additional
access-control information from your provider, but require additional schema
modifications.

The **Set up with API Gateway and an identity provider** and
**Guided setup** options in the Verified Permissions console assign ID token
claims to the schema. This isn't the case for access token claims. To add non-group
access-token claims to your schema, you must edit your schema in JSON mode and add
[commonTypes](https://docs.cedarpolicy.com/schema/json-schema.html#schema-commonTypes "https://docs.cedarpolicy.com/schema/json-schema.html#schema-commonTypes") attributes. For more information, see [Mapping access tokens](#cognito-map-access-token "#cognito-map-access-token").

###### Choose a token type

The way that your policy store works with your identity source depends on a key
decision in identity-source configuration: whether you will process ID or access
tokens. With an Amazon Cognito identity provider, you have the choice of token type when you
create an API-linked policy store. When you create an [API-linked policy store](policy-stores-api-userpool.md "policy-stores-api-userpool.md"), you must choose
whether you want to set up authorization for ID or access tokens. This information
affects the schema attributes that Verified Permissions applies to your policy store, and the syntax of the
Lambda authorizer for your API Gateway API.
Especially if you wish to benefit from the automatic mapping of ID token claims to
attributes in the Verified Permissions console, decide early about the token type that you want to
process before you create your identity source. Changing the token type requires
significant effort to refactor your policies and schema. The following topics
describe the use of ID and access tokens with policy stores.

###### Cedar parser requires brackets for some characters

Policies typically reference schema attributes in a format like
`principal.username`. In the case of most non-alphanumeric characters
like `:`, `.`, or `/` that might appear in token
claim names, Verified Permissions can't parse a condition value like
`principal.cognito:username` or `context.ip-address`. You
must instead format these conditions with bracket notation in the format
`principal["cognito:username"]` or
`context["ip-address"]`, respectively. The underscore character
`_` is a valid character in claim names, and the only
non-alphanumeric exception to this requirement.

A partial example schema for a principal attribute of this type looks like the
following:

```
"User": {
   "shape": {
      "type": "Record",
      "attributes": {
         "cognito:username": {
            "type": "String",
            "required": true
         },
         "custom:employmentStoreCode": {
            "type": "String",
            "required": true,
         },
         "email": {
            "type": "String",
            "required": false
         }
      }
   }
}
```

A partial example schema for a context attribute of this type looks like the
following:

```
"GetOrder": {
   "memberOf": [],
   "appliesTo": {
      "resourceTypes": [
         "Order"
      ],
      "context": {
         "type": "Record",
         "attributes": {
            "ip-address": {
               "required": false,
               "type": "String"
            }
		 }
	  },
      "principalTypes": [
         "User"
      ]
   }
}
```

For an example policy that will validate against this schema, see [Uses bracket notation to reference token
attributes](policies-examples.md#policies-examples-brackets "policies-examples.md#policies-examples-brackets").
