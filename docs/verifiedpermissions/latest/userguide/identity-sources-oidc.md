# Working with OIDC identity sources

You can also configure any compliant OpenID Connect (OIDC) IdP as the identity source
of a policy store. OIDC providers are similar to Amazon Cognito user pools: they produce JWTs as the product of
authentication. To add an OIDC provider, you must provide an issuer URL

A new OIDC identity source requires the following information:

- The issuer URL. Verified Permissions must be able to discover a
  `.well-known/openid-configuration` endpoint at this URL.
- CNAME records that don't include wild cards. For example,
  `a.example.com` can't be mapped to `*.example.net`.
  Conversely, `*.example.com` can't be mapped to
  `a.example.net`.
- The token type that you want to use in authorization requests. In this case,
  you chose **Identity token**.
- The user entity type that you want to associate with your identity source, for
  example `MyCorp::User`.
- The group entity type that you want to associate with your identity source,
  for example `MyCorp::UserGroup`.
- An example ID token, or a definition of the claims in the ID token.
- The prefix that you want to apply to user and group entity IDs. In the CLI and
  API, you can choose this prefix. In policy stores that you create with the
  **Set up with API Gateway and an identity provider** or
  **Guided setup** option, Verified Permissions assigns a prefix of the
  issuer name minus `https://`, for example
  `MyCorp::User::"auth.example.com|a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`.
  For more information about using API operations to authorize requests from OIDC
  sources, see [Available API operations for authorization](authorization.md#authorization-operations "authorization.md#authorization-operations").

This following example shows how you might create a policy that permits access to year-end reports for employees in the
accounting department, have a confidential classification, and aren't in a satellite
office. Verified Permissions derives these attributes from the claims in the principal's ID
token.

Note that when referencing a group in the principal, you must use the `in` operator for the policy to be evaluated correctly.

```
permit(
     principal in MyCorp::UserGroup::"MyOIDCProvider|Accounting",
     action,
     resource in MyCorp::Folder::"YearEnd2024"
) when {
     principal.jobClassification == "Confidential" &&
     !(principal.location like "SatelliteOffice*")
};
```

###### Topics

- [Creating Amazon Verified Permissions OIDC identity sources](oidc-create.md "oidc-create.md")
- [Editing Amazon Verified Permissions OIDC identity sources](oidc-edit.md "oidc-edit.md")
- [Mapping OIDC tokens to
  schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md")
- [Client and audience validation for OIDC providers](oidc-validation.md "oidc-validation.md")
