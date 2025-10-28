Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Defining database roles to

grant to federated users in Amazon Redshift Serverless

When you're part of an organization, you have a collection of associated roles. For
instance, you have roles for your job function, like _programmer_ and
_manager_. Your roles determine which applications and data you
have access to. Most organizations use an identity provider, such as Microsoft Active
Directory, to assign roles to users and groups. The use of roles to control resource
access has grown, because organizations don't have to do as much management of
individual users.

Recently, role-based access control was introduced in Amazon Redshift Serverless. Using
database roles, you can secure access to data and objects, like schemas or tables, for
example. Or you can use roles to define a set of elevated permissions, such as for a
system monitor or database administrator. But after you grant resource permissions to
database roles, there is an additional step, which is to connect a user's roles from the
organization to the database roles. You can assign each user to their database roles
upon initial sign in by running SQL statements, but it's a lot of effort. An easier way
is to define the database roles to grant and pass them to Amazon Redshift Serverless. This has
the advantage of simplifying the initial sign-in process.

You can pass roles to Amazon Redshift Serverless using `GetCredentials`. When a user
signs in for the first time to an Amazon Redshift Serverless database, an associated database
user is created and mapped to the matching database roles. This topic details the
mechanism for passing roles to Amazon Redshift Serverless.

Passing database roles has a couple primary use cases:

- When a user signs in through a third-party identity provider, typically with
  federation configured, and passes the roles by means of a session tag.
- When a user signs in through IAM sign-in credentials, and their roles are
  passed by means of a tag key and value.
  For more information about role-based access control, see [Role-based access control (RBAC)](../dg/t_Roles.md "../dg/t_Roles.md").

## Defining

database roles

Before you can pass roles to Amazon Redshift Serverless, you must configure database roles in
your database and grant them appropriate permissions on database resources. For
instance, in a simple scenario, you can create a database role named
_sales_ and grant it access to query tables with sales data. For
more information about how to create database roles and grant permissions, see [CREATE ROLE](../dg/r_CREATE_ROLE.md "../dg/r_CREATE_ROLE.md") and [GRANT](../dg/r_GRANT.md "../dg/r_GRANT.md").

## Use cases for

defining database roles to grant to federated users

These sections outline a couple use cases where passing database roles to
Amazon Redshift Serverless can simplify access to database resources.

### Signing

in using an identity provider

The first use case assumes that your organization has user identities in an
identity and access management service. This service can be cloud based, for
example JumpCloud or Okta, or on-premises, such as Microsoft Active Directory.
The goal is to automatically map a user's roles from the identity provider to
your database roles when they sign in to a client like Query editor V2, for
instance, or with a JDBC client.
To set this up, you must complete a couple of configuration tasks. These include
the following:

1. Configure federated integration with your identity provider (IdP)
   using a trust relationship. This is a prerequisite. When you set this
   up, the identity provider is responsible for authenticating the user via
   a SAML assertion and providing sign-in credentials. For more
   information, see [Integrating third party SAML solution providers with AWS](../../../IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.md "../../../IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.md").
   You can also find more information at [Federate access to Amazon Redshift query editor V2 with Active Directory
   Federation Services (AD FS)](https://aws.amazon.com/blogs//big-data/federate-access-to-amazon-redshift-query-editor-v2-with-active-directory-federation-services-ad-fs-part-3/ "https://aws.amazon.com/blogs//big-data/federate-access-to-amazon-redshift-query-editor-v2-with-active-directory-federation-services-ad-fs-part-3/") or [Federate single sign-on access to Amazon Redshift query editor v2 with
   Okta](https://aws.amazon.com/blogs//big-data/federate-single-sign-on-access-to-amazon-redshift-query-editor-v2-with-okta/ "https://aws.amazon.com/blogs//big-data/federate-single-sign-on-access-to-amazon-redshift-query-editor-v2-with-okta/").
2. The user must have the following policy permissions:
   - `GetCredentials` – Provides credentials for
     temporary authorization to log in to Amazon Redshift Serverless.
   - `sts:AssumeRoleWithSAML` – Provides a
     mechanism for tying an enterprise identity store or directory to
     role-based AWS access.
   - `sts:TagSession` – Permission to the
     tag-session action, on the identity provider principal.
     In this case, `AssumeRoleWithSAML` returns a set of
     security credentials for users who have been authenticated via a SAML
     authenticated response. This operation provides a mechanism for tying an
     identity store or directory to role-based AWS access without
     user-specific credentials. For users with permission to
     `AssumeRoleWithSAML`, the identity provider is
     responsible for managing the SAML assertion that is used to pass the
     role information.

As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md"). 3. You configure the tag `RedshiftDbRoles` with the
colon-separated role values, in the format
_role1:role2_. For example,
`manager:engineer`. These can be retrieved from a
session-tag implementation configured in your identity provider. The
SAML authentication request passes the roles programmatically. For more
information about passing session tags, see [Passing session tags in
AWS STS](../../../IAM/latest/UserGuide/id_session-tags.md "../../../IAM/latest/UserGuide/id_session-tags.md").

In a case where you pass a role name that doesn't exist in the
database, it's ignored.

In this use case, when a user signs in using a federated identity, their roles
are passed in the authorization request through the session tag key and value.
Subsequently, following authorization, `GetCredentials` passes the
roles to the database. Upon a successful connection, the database roles are
mapped and the user can perform database tasks corresponding with their role.
The essential part of the operation is that the `RedshiftDbRoles`
session tag is assigned the roles in the initial authorization request. For more
information about passing session tags, see [Passing session tags using AssumeRoleWithSAML](../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_adding-assume-role-saml "../../../IAM/latest/UserGuide/id_session-tags.md#id_session-tags_adding-assume-role-saml").

### Signing in

using IAM credentials

In the second use case, roles can be passed for a user and they can access a
database client application through IAM credentials.

1. The user who signs in in this case must be assigned policy permissions
   for the following actions:
   - `tag:GetResources` – Returns tagged
     resources associated with specified tags.
   - `tag:GetTagKeys` – Returns tag keys
     currently in use.

   As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
   needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

2. Allow permissions are also required to access the database service,
   such as Amazon Redshift Serverless.
3. For this use case, configure the tag values for your roles in
   AWS Identity and Access Management. You can choose to **edit tags** and create
   a tag key called _RedshiftDbRoles_ with an
   accompanying tag value string that contains the roles. For example,
   _manager:engineer_.

When a user logs in, their role is added to the authorization request and
passed to the database. It is mapped to an existing database role.

## Additional

resources

As mentioned in the use cases, you can configure the trust relationship between
your IdP and AWS. For more information, see [Configuring your SAML 2.0 IdP with relying party trust and adding
claims](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.md "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.md").
