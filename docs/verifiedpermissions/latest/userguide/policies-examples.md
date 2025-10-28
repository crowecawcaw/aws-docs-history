# Amazon Verified Permissions example policies

Some of the policy examples included here are basic Cedar policy examples and some are
Verified Permissions-specific. The basic ones link to the Cedar policy language Reference Guide and are included there.
For more information about Cedar policy syntax, see [Basic policy construction in
Cedar](https://docs.cedarpolicy.com/policies/syntax-policy.html "https://docs.cedarpolicy.com/policies/syntax-policy.html") in the Cedar policy language Reference Guide.

**Policy examples**

- [Allows access to individual entities](https://docs.cedarpolicy.com/policies/policy-examples.html#allow-acces-indivuals "https://docs.cedarpolicy.com/policies/policy-examples.html#allow-acces-indivuals")
- [Allows access to groups of entities](https://docs.cedarpolicy.com/policies/policy-examples.html#allow-acces-groups "https://docs.cedarpolicy.com/policies/policy-examples.html#allow-acces-groups")
- [Allows access for any entity](https://docs.cedarpolicy.com/policies/policy-examples.html#allow-any "https://docs.cedarpolicy.com/policies/policy-examples.html#allow-any")
- [Allows access for attributes of an entity (ABAC)](https://docs.cedarpolicy.com/policies/policy-examples.html#allow-abac "https://docs.cedarpolicy.com/policies/policy-examples.html#allow-abac")
- [Denies access](https://docs.cedarpolicy.com/policies/policy-examples.html#deny-access "https://docs.cedarpolicy.com/policies/policy-examples.html#deny-access")
- [Uses bracket notation to reference token
  attributes](#policies-examples-brackets "#policies-examples-brackets")
- [Uses dot notation to reference
  attributes](#policies-examples-dot "#policies-examples-dot")
- [Reflects Amazon Cognito ID token
  attributes](#policies-examples-cognito-id "#policies-examples-cognito-id")
- [Reflects OIDC ID token attributes](#policies-examples-oidc-id "#policies-examples-oidc-id")
- [Reflects Amazon Cognito access token
  attributes](#policies-examples-cognito-access "#policies-examples-cognito-access")
- [Reflects OIDC access token
  attributes](#policies-examples-oidc-access "#policies-examples-oidc-access")

## Uses bracket notation to reference token

attributes

This following example shows how you might create a policy that uses bracket notation
to reference token attributes.

For more information about using token attributes in policies in Verified Permissions, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

```
permit (
    principal in MyCorp::UserGroup::"us-west-2_EXAMPLE|MyUserGroup",
    action,
    resource
) when {
    principal["cognito:username"] == "alice" &&
    principal["custom:employmentStoreCode"] == "petstore-dallas" &&
    principal has email && principal.email == "alice@example.com" &&
    context["ip-address"] like "192.0.2.*"
};
```

## Uses dot notation to reference

attributes

This following example shows how you might create a policy that uses dot notation to
reference attributes.

For more information about using token attributes in policies in Verified Permissions, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

```
permit(principal, action, resource)
when {
    principal.cognito.username == "alice" &&
    principal.custom.employmentStoreCode == "petstore-dallas" &&
    principal.tenant == "x11app-tenant-1" &&
    principal has email && principal.email == "alice@example.com"
};
```

## Reflects Amazon Cognito ID token

attributes

This following example shows how you might create a policy references ID token
attributes from Amazon Cognito.

For more information about using token attributes in policies in Verified Permissions, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

```
permit (
    principal in MyCorp::UserGroup::"us-west-2_EXAMPLE|MyUserGroup",
    action,
    resource
) when {
    principal["cognito:username"] == "alice" &&
    principal["custom:employmentStoreCode"] == "petstore-dallas" &&
    principal.tenant == "x11app-tenant-1" &&
    principal has email && principal.email == "alice@example.com"
};
```

## Reflects OIDC ID token attributes

This following example shows how you might create a policy references ID token
attributes from an OIDC provider.

For more information about using token attributes in policies in Verified Permissions, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

```
permit (
    principal in MyCorp::UserGroup::"MyOIDCProvider|MyUserGroup",
    action,
    resource
) when {
    principal.email_verified == true && principal.email == "alice@example.com" &&
    principal.phone_number_verified == true && principal.phone_number like "+1206*"
};
```

## Reflects Amazon Cognito access token

attributes

This following example shows how you might create a policy references access token
attributes from Amazon Cognito.

For more information about using token attributes in policies in Verified Permissions, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

```
permit(principal, action in [MyApplication::Action::"Read", MyApplication::Action::"GetStoreInventory"], resource)
when {
    context.token.client_id == "52n97d5afhfiu1c4di1k5m8f60" &&
    context.token.scope.contains("MyAPI/mydata.write")
};
```

## Reflects OIDC access token

attributes

This following example shows how you might create a policy references access token
attributes from an OIDC provider.

For more information about using token attributes in policies in Verified Permissions, see [Mapping Amazon Cognito tokens to schema](cognito-map-token-to-schema.md "cognito-map-token-to-schema.md") and [Mapping OIDC tokens to schema](oidc-map-token-to-schema.md "oidc-map-token-to-schema.md").

```
permit(
    principal,
    action in [MyApplication::Action::"Read", MyApplication::Action::"GetStoreInventory"],
    resource
)
when {
    context.token.client_id == "52n97d5afhfiu1c4di1k5m8f60" &&
    context.token.scope.contains("MyAPI-read")
};
```
