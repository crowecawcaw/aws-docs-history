Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Automatically creating

Amazon Redshift roles for identity providers

This feature allows you to automatically create roles in Redshift based on group
membership from your Identity Provider (IdP). Auto-creating roles supports the Azure Active
Directory with the native IdP integration.

There are several benefits to auto-creating roles. When you auto-create a role,
Redshift creates the role with group membership in your IdP, so you can avoid tedious
manual role creation and maintenance. You also have the option to filter which groups are
mapped to Redshift roles.

## How it works

When you, as an IdP user, log into Redshift, the following sequence of events happen:

1. Redshift retrieves your group memberships from the IdP.
2. Redshift automatically creates roles mapping to those groups, with the role format
   ``idp_namespace`:`rolename``.
3. Redshift grants you permissions with the mapped roles.

Upon each user login, each group that's not present in catalog but that the user is
part of, is auto-created. You can optionally set include and exclude filters to control
which IdP groups have Redshift roles created.

## Configuring auto-create roles

Use the `CREATE IDENTITY PROVIDER` and `ALTER IDENTITY PROVIDER`
commands to enable and configure automatic role creation.

```
-- Create a new IdP with auto role creation enabled
CREATE IDENTITY PROVIDER <`idp_name`> TYPE azure
  NAMESPACE '<`namespace`>'
  APPLICATION_ARN '`app_arn`'
  IAM_ROLE '`role_arn`'
  AUTO_CREATE_ROLES TRUE;

-- Enable on existing IdP
ALTER IDENTITY PROVIDER <`idp_name`>
  AUTO_CREATE_ROLES TRUE;

-- Disable
ALTER IDENTITY PROVIDER <`idp_name`>
  AUTO_CREATE_ROLES FALSE;
```

## Filtering groups

You can optionally filter which IdP groups are mapped to Redshift roles using
`INCLUDE` and `EXCLUDE` patterns. When patterns conflict,
`EXCLUDE` takes precedence over `INCLUDE`.

```
-- Only create roles for groups with 'dev'
CREATE IDENTITY PROVIDER <`idp_name`> TYPE azure
  ...
  AUTO_CREATE_ROLES TRUE
  INCLUDE GROUPS LIKE '%dev%';

-- Exclude 'test' groups
ALTER IDENTITY PROVIDER <`idp_name`>
  AUTO_CREATE_ROLES TRUE
  EXCLUDE GROUPS LIKE '%test%';
```

## Examples

The following example shows how to turn on auto-create roles with no filtering.

```
CREATE IDENTITY PROVIDER prod_idc TYPE azure ...
  AUTO_CREATE_ROLES TRUE;
```

The following example includes development groups and excludes test groups.

```
ALTER IDENTITY PROVIDER prod_idc
  AUTO_CREATE_ROLES TRUE
  INCLUDE GROUPS LIKE '%dev%'
  EXCLUDE GROUPS LIKE '%test%';
```

## Best practices

Consider the following best practives when you enable auto-create for roles:

- Use `INCLUDE` and `EXCLUDE` filters to control which groups
  get roles.
- Periodically audit roles and clean up unused ones.
- Leverage Redshift role hierarchies to simplify permission management.
