Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER IDENTITY PROVIDER

Alters an identity provider to assign new parameters and values. When you run this
command, all previously set parameter values are deleted before the new values are
assigned. Only a superuser can alter an identity provider.

## Syntax

```
ALTER IDENTITY PROVIDER *identity\_provider\_name*
[PARAMETERS *parameter\_string*]
[NAMESPACE *namespace*]
[IAM_ROLE *iam\_role*]
[AUTO_CREATE_ROLES
    [ TRUE [ { INCLUDE | EXCLUDE } GROUPS LIKE *filter\_pattern*] |
      FALSE
    ]
[DISABLE | ENABLE]
```

## Parameters

_identity_provider_name_

Name of the new identity provider. For more information about valid names,
see [Names and identifiers](r_names.md "r_names.md").

_parameter_string_

A string containing a properly formatted JSON object that contains
parameters and values required for the specific identity provider.

_namespace_

The organization namespace.

_iam_role_

The IAM role that provides permissions for the connection to IAM Identity Center. This
parameter is applicable only when the identity-provider type is AWSIDC.

_auto_create_roles_

Enables or disables the auto-create role feature.
If the value is TRUE, Amazon Redshift enables the
auto-create role feature.
If the value is FALSE, Amazon Redshift disables the
auto-create role feature.
If the value for this parameter isn't specified,
Amazon Redshift determines the value using the following logic:

- If `AUTO_CREATE_ROLES` is provided but the value isn't specified,
  the value is set to TRUE.
- If `AUTO_CREATE_ROLES` isn't provided and the identity provider is AWSIDC,
  the value is set to FALSE.
- If `AUTO_CREATE_ROLES` isn't provided and the identity provider is Azure,
  the value is set to TRUE.

To include groups, specify `INCLUDE`. The default is empty, which
means include all groups if `AUTO_CREATE_ROLES` is on.

To exclude groups, specify `EXCLUDE`. The default is empty, which
means do not exclude any groups if `AUTO_CREATE_ROLES` is
on.

_filter_pattern_

A valid UTF-8 character expression with a pattern to match group names. The
LIKE option performs a case-sensitive match that supports the following
pattern-matching metacharacters:

| Metacharacter | Description                                      |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `%`           | Matches any sequence of zero or more characters. |
| `_`           | Matches any single character.                    | If _filter_pattern_ does not contain metacharacters, then the pattern only represents the string itself; in that case LIKE acts the same as the equals operator. _filter_pattern_ supports the following characters: <br>• Uppercase and lowercase alphabetic characters (A-Z and a-z) <br>• Numerals (0-9) <br>• The following special characters: `_ % ^ * + ? { } , $` _DISABLE or ENABLE_ Turns an identity provider on or off. The default is ENABLE. ## Examples The following example alters an identity provider named _oauth_standard_. It applies specifically to when Microsoft Azure AD is the identity provider. `ALTER IDENTITY PROVIDER oauth_standard PARAMETERS '{"issuer":"https://sts.windows.net/2sdfdsf-d475-420d-b5ac-667adad7c702/", "client_id":"87f4aa26-78b7-410e-bf29-57b39929ef9a", "client_secret":"BUAH~ewrqewrqwerUUY^%tHe1oNZShoiU7", "audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift"] }'` The following sample shows how to set the identity-provider namespace. This can apply to Microsoft Azure AD, if it follows a statement like the previous sample, or to another identity provider. It can also apply to a case where you connect an existing Amazon Redshift provisioned cluster or Amazon Redshift Serverless workgroup to IAM Identity Center, if you have a connection set up through a managed application. `ALTER IDENTITY PROVIDER "my-redshift-idc-application" NAMESPACE 'MYCO';` The following sample sets the IAM role and works in the use case for configuring Redshift integration with IAM Identity Center. `ALTER IDENTITY PROVIDER "my-redshift-idc-application" IAM_ROLE 'arn:aws:iam::123456789012:role/myadministratorrole';` For more information about setting up a connection to IAM Identity Center from Redshift, see [Connect Redshift with IAM Identity Center to give users a single sign-on experience](../mgmt/redshift-iam-access-control-idp-connect.md "../mgmt/redshift-iam-access-control-idp-connect.md"). **Disabling an identity provider** The following sample statement shows how to disable an identity provider. When it's disabled, federated users from the identity provider can't login to the cluster until it's enabled again. `ALTER IDENTITY PROVIDER "redshift-idc-app" DISABLE;` |
