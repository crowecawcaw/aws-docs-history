Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE IDENTITY PROVIDER

Defines a new identity provider. Only a superuser can create an identity
provider.

## Syntax

```
CREATE IDENTITY PROVIDER *identity\_provider\_name* TYPE *type\_name*
NAMESPACE *namespace\_name*
[PARAMETERS *parameter\_string*]
[APPLICATION_ARN *arn*]
[IAM_ROLE *iam\_role*]
[AUTO_CREATE_ROLES
    [ TRUE [ { INCLUDE | EXCLUDE } GROUPS LIKE *filter\_pattern*] |
      FALSE
    ]
  ];
```

## Parameters

_identity_provider_name_

Name of the new identity provider. For more information about valid names,
see [Names and identifiers](r_names.md "r_names.md").

_type_name_

The identity provider to interface with. Azure and AWSIDC are currently the only
supported identity providers.

_namespace_name_

The namespace. This is a unique, shorthand identifier for the identity
provider directory.

_parameter_string_

A string containing a properly formatted JSON object that contains
parameters and values required for the identity provider.

_arn_

The Amazon resource name (ARN) for an IAM Identity Center managed application. This
parameter is applicable only when the identity-provider type is AWSIDC.

_iam_role_

The IAM role that provides permissions to make the connection to IAM Identity Center.
This parameter is applicable only when the identity-provider type is
AWSIDC.

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

| Metacharacter | Description                                         |
| ------------- | --------------------------------------------------- |
| `%`           | Matches any sequence of zero or more<br>characters. |
| `_`           | Matches any single character.                       |

If _filter_pattern_ does not contain metacharacters, then
the pattern only represents the string itself; in that case LIKE acts the same
as the equals operator.

_filter_pattern_ supports the following characters:

- Uppercase and lowercase alphabetic characters (A-Z and a-z)
- Numerals (0-9)
- The following special characters:

```
_ % ^ * + ? { } , $
```

## Examples

The following example creates an identity provider named
_oauth_standard_, with a TYPE _azure_, to
establish communication with Microsoft Azure Active Directory (AD).

```
CREATE IDENTITY PROVIDER oauth_standard TYPE azure
NAMESPACE 'aad'
PARAMETERS '{"issuer":"https://sts.windows.net/2sdfdsf-d475-420d-b5ac-667adad7c702/",
"client_id":"87f4aa26-78b7-410e-bf29-57b39929ef9a",
"client_secret":"BUAH~ewrqewrqwerUUY^%tHe1oNZShoiU7",
"audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift"]
}'
```

You can connect an IAM Identity Center managed application with an existing provisioned cluster or
Amazon Redshift Serverless workgroup. This gives you the ability to manage access to a Redshift
database through IAM Identity Center. To do so, run a SQL command like the following sample. You have
to be a database administrator.

```
CREATE IDENTITY PROVIDER "redshift-idc-app" TYPE AWSIDC
NAMESPACE 'awsidc'
APPLICATION_ARN 'arn:aws:sso::123456789012:application/ssoins-12345f67fe123d4/apl-a0b0a12dc123b1a4'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyRedshiftRole';
```

The application ARN in this case identifies the managed application to connect to.
You can find it by running `SELECT * FROM SVV_IDENTITY_PROVIDERS;`.

For more information about using CREATE IDENTITY PROVIDER, including additional
examples, see [Native identity provider (IdP) federation for Amazon Redshift](../mgmt/redshift-iam-access-control-native-idp.md "../mgmt/redshift-iam-access-control-native-idp.md"). For more information
about setting up a connection to IAM Identity Center from Redshift, see [Connect Redshift
with IAM Identity Center to give users a single sign-on experience](../mgmt/redshift-iam-access-control-idp-connect.md "../mgmt/redshift-iam-access-control-idp-connect.md").
