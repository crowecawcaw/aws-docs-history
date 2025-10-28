# Mapping OIDC tokens to

schema

You might find that you want to add an identity source to a policy store and map provider
claims, or tokens, to your policy store schema. You can automate this process, by using the [Guided
setup](policy-stores-create.md "policy-stores-create.md") to create your policy store with an identity source, or update your schema manually after the policy store is created.
Once you have mapped the tokens to the schema you can create policies that reference
them.

This section of the user guide has the following information:

- When you can automatically populate attributes to a policy store schema
- How to manually build a schema for an identity source
  [API-linked policy stores](policy-stores-api-userpool.md "policy-stores-api-userpool.md") and policy stores with
  an identity source that were created through [Guided
  setup](policy-stores-create.md "policy-stores-create.md") don't require manual mapping of identity (ID) token attributes to schema.
  You can provide Verified Permissions with the attributes in your user pool and create a schema that is
  populated with user attributes. In ID token authorization, Verified Permissions maps claims to attributes
  of a principal entity.

To use an OIDC identity provider (IdP) as an identity source in your Verified Permissions policy store,
you must have provider attributes in your schema. The schema is fixed and must correspond to
the entities that provider tokens create in [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md") or
[BatchIsAuthorizedWithToken](../apireference/API_BatchIsAuthorizedWithToken.md "../apireference/API_BatchIsAuthorizedWithToken.md") API requests. If you created your policy store in a
way that automatically populates your schema from provider information in an ID token,
you're ready to write policies. If you create a policy store without a schema for your identity
source, you must add provider attributes to the schema that match the entities created using
API requests. Then you can write policies using attributes from the provider token.

###### Topics

- [Mapping ID tokens to schema](#oidc-map-id-token "#oidc-map-id-token")
- [Mapping access tokens](#oidc-map-access-token "#oidc-map-access-token")
- [Things to know
  about schema mapping](#oidc-map-token-to-schema-things-to-know "#oidc-map-token-to-schema-things-to-know")

## Mapping ID tokens to schema

Verified Permissions processes ID token claims as the attributes of the user: their names and titles,
their group membership, their contact information. ID tokens are most useful in an
_attribute-based access control_ (ABAC)
authorization model. When you want Verified Permissions to analyze access to resources based on who's
making the request, choose ID tokens for your identity source.

Working with ID tokens from an OIDC provider is much the same as working with
Amazon Cognito ID tokens. The difference is in the claims. Your IdP might present [standard OIDC attributes](https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims "https://openid.net/specs/openid-connect-core-1_0.html#StandardClaims"), or have a custom schema. When you create a
new policy store in the Verified Permissions console, you can add an OIDC identity source with an example
ID token, or you can manually map token claims to user attributes. Because Verified Permissions
isn't aware of the attribute schema of your IdP, you must provide this
information.

For more information, see [Creating Verified Permissions policy stores](policy-stores-create.md "policy-stores-create.md").

The following is an example schema for a policy store with an OIDC identity source.

```
"User": {
   "shape": {
      "type": "Record",
      "attributes": {
         "email": {
            "type": "String"
         },
         "email_verified": {
            "type": "Boolean"
         },
         "name": {
            "type": "String",
            "required": true
         },
         "phone_number": {
            "type": "String"
         },
         "phone_number_verified": {
            "type": "Boolean"
         }
      }
   }
}
```

For an example policy that will validate against this schema, see [Reflects OIDC ID token attributes](policies-examples.md#policies-examples-oidc-id "policies-examples.md#policies-examples-oidc-id").

## Mapping access tokens

Verified Permissions processes access-token claims other than the groups claim as attributes of the
action, or _context attributes_. Along with group
membership, the access tokens from your IdP might contain information about API access.
Access tokens are useful in authorization models that use role-based access control
(RBAC). Authorization models that rely on access-token claims other than group
membership require additional effort in schema configuration.

Most access tokens from external OIDC providers align closely with Amazon Cognito access
tokens. An OIDC access token is mapped to a context object when passed to Verified Permissions.
Attributes of the access token can be referenced using
`context.token.`attribute_name``. The
following example OIDC access token includes example base claims.

```
{
    "sub": "91eb4550-9091-708c-a7a6-9758ef8b6b1e",
    "groups": [
        "Store-Owner-Role",
        "Customer"
    ],
    "iss": "https://auth.example.com",
    "client_id": "1example23456789",
    "aud": "https://myapplication.example.com"
    "scope": "MyAPI-Read",
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

For an example policy that will validate against this schema, see [Reflects OIDC access token
attributes](policies-examples.md#policies-examples-oidc-access "policies-examples.md#policies-examples-oidc-access").

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
[commonTypes](https://docs.cedarpolicy.com/schema/json-schema.html#schema-commonTypes "https://docs.cedarpolicy.com/schema/json-schema.html#schema-commonTypes") attributes. For more information, see [Mapping access tokens](#oidc-map-access-token "#oidc-map-access-token").

###### OIDC groups claim supports multiple formats

When you add an OIDC provider, you can choose the name of the groups claim in ID
or access tokens that you want to map to a user’s group membership in your policy
store. Verified permissions recognizes groups claims in the following
formats:

1. String without spaces: `"groups": "MyGroup"`
2. Space-delimited list: `"groups": "MyGroup1 MyGroup2 MyGroup3"`.
   Each string is a group.
3. JSON (comma-delimited) list: `"groups": ["MyGroup1", "MyGroup2",
"MyGroup3"]`

###### Note

Verified Permissions interprets each string in a space-separated groups claim as a
separate group. To interpret a group name with a space character as a single group,
replace or remove the space in the claim. For example, format a group named `My
 Group` as `MyGroup`.

###### Choose a token type

The way that your policy store works with your identity source depends on a key
decision in identity-source configuration: whether you will process ID or access
tokens. With an OIDC provider, you must choose a token
type when you add the identity source. You can choose ID or access token, and your
choice excludes the unchosen token type from being processed in your policy store.
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
