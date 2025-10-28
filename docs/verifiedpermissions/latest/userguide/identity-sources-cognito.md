# Working with Amazon Cognito identity sources

Verified Permissions works closely with Amazon Cognito user pools. Amazon Cognito JWTs have a predictable structure. Verified Permissions
recognizes this structure and draws maximum benefit from the information that it
contains. For example, you can implement a role-based access control (RBAC)
authorization model with either ID tokens or access tokens.

A new Amazon Cognito user pools identity source requires the following information:

- The AWS Region.
- The user pool ID.
- The principal entity type that you want to associate with your identity
  source, for example `MyCorp::User`.
- The principal group entity type that you want to associate with your identity
  source, for example `MyCorp::UserGroup`.
- The client IDs from your user pool that you want to authorize to make requests
  to your policy store.
  Because Verified Permissions only works with Amazon Cognito user pools in the same AWS account, you can't specify an
  identity source in another account. Verified Permissions sets the _entity
  prefix_—the identity-source identifier that you must reference in
  policies that act on user pool principals—to the ID of your user pool, for
  example `us-west-2_EXAMPLE`. In this case, you would reference a user in that
  user pool with ID `a1b2c3d4-5678-90ab-cdef-EXAMPLE22222` as
  `us-west-2_EXAMPLE|a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`

User pool token _claims_ can contain attributes, scopes, groups,
client IDs, and custom data. [Amazon Cognito JWTs](../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.md "../../../cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.md") have the ability to include a variety of information that can
contribute to authorization decisions in Verified Permissions. These include:

1. Username and group claims with a `cognito:` prefix
2. [Custom user attributes](../../../cognito/latest/developerguide/user-pool-settings-attributes.md#user-pool-settings-custom-attributes "../../../cognito/latest/developerguide/user-pool-settings-attributes.md#user-pool-settings-custom-attributes") with a `custom: prefix`
3. Custom claims added at runtime
4. OIDC standard claims like `sub` and `email`
   We cover these claims in detail, and how to manage them in Verified Permissions policies, in [Mapping Amazon Cognito tokens to
   schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md").

###### Important

Although you can revoke Amazon Cognito tokens before they expire, JWTs are considered to be
stateless resources that are self-contained with a signature and validity. Services
that conform with [the
JSON Web Token RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 "https://datatracker.ietf.org/doc/html/rfc7519") are expected to validate tokens remotely and
aren't required to validate them with the issuer. This means that it is possible for
Verified Permissions to grant access based on a token that was revoked or issued for a user that
was later deleted. To mitigate this risk, we recommend that you create your tokens
with the shortest possible validity duration and revoke refresh tokens when you want
to remove authorization to continue a user's session. For more information, see
[Ending user sessions with token
revocation](../../../cognito/latest/developerguide/token-revocation.md "../../../cognito/latest/developerguide/token-revocation.md")

This following example shows how you might create a policy that references some of the Amazon Cognito user pools claims associated with a
principal.

```
permit(
     principal,
     action,
     resource == ExampleCo::Photo::"VacationPhoto94.jpg"
)
when {
     principal["cognito:username"]) == "alice" &&
     principal["custom:department"]) == "Finance"
};
```

This following example shows how you might create a policy that references a principal that's a user in a Cognito user pool.
Note that the principal ID takes the form of
`"<userpool-id>|<sub>"`.

```
permit(
     principal == ExampleCo::User::"us-east-1_example|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
     action,
     resource == ExampleCo::Photo::"VacationPhoto94.jpg"
);
```

Cedar policies for user pool identity sources in Verified Permissions use a special syntax for
claim names that contain characters other than alphanumeric and underscore
(`_`). This includes user pool prefix claims that contain a
`:` character, like `cognito:username` and
`custom:department`. To write a policy condition that references the
`cognito:username` or `custom:department` claim, write them as
`principal["cognito:username"]` and
`principal["custom:department"]`, respectively.

###### Note

If a token contains a claim with a `cognito:` or `custom:`
prefix and a claim name with the literal value `cognito` or
`custom`, an authorization request with [IsAuthorizedWithToken](../apireference/API_IsAuthorizedWithToken.md "../apireference/API_IsAuthorizedWithToken.md")
will fail with a `ValidationException`.

For more information about mapping claims, see [Mapping Amazon Cognito tokens to
schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md"). For more information about authorization
for Amazon Cognito users, see [Authorization with
Amazon Verified Permissions](../../../cognito/latest/developerguide/amazon-cognito-authorization-with-avp.md "../../../cognito/latest/developerguide/amazon-cognito-authorization-with-avp.md") in the _Amazon Cognito Developer Guide_.

###### Topics

- [Creating Amazon Verified Permissions Amazon Cognito identity sources](cognito-create.md "cognito-create.md")
- [Editing Amazon Verified Permissions Amazon Cognito identity sources](cognito-edit.md "cognito-edit.md")
- [Mapping Amazon Cognito tokens to
  schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md")
- [Client and audience validation for Amazon Cognito](cognito-validation.md "cognito-validation.md")
