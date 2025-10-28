Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up the identity

provider on Amazon Redshift

This section shows the steps to configure the identity provider and Amazon Redshift to establish
communication for native identity provider federation. You need an active account with your
identity provider. Prior to configuring Amazon Redshift, you register Redshift as an application with
your identity provider, granting administrator consent.

Complete the following steps in Amazon Redshift:

1. You run a SQL statement to register the identity provider, including descriptions of
   the Azure application metadata. To create the identity provider in Amazon Redshift, run the
   following command after replacing the parameter values _issuer_,
   _client_id_, _client_secret_, and
   _audience_. These parameters are specific to Microsoft Azure AD.
   Replace the identity provider name with a name of your choosing, and replace the
   namespace with a unique name to contain users and roles from your identity provider
   directory.

```
CREATE IDENTITY PROVIDER oauth_standard TYPE azure
NAMESPACE 'aad'
PARAMETERS '{
"issuer":"https://sts.windows.net/2sdfdsf-d475-420d-b5ac-667adad7c702/",
"client_id":"<client_id>",
"client_secret":"BUAH~ewrqewrqwerUUY^%tHe1oNZShoiU7",
"audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift"]
}'
```

The type `azure` indicates that the provider specifically facilitates
communication with Microsoft Azure AD. This is currently the only supported third-party
identity provider.

    * *issuer* - The issuer ID to trust when a token is received.
     The unique identifier for the *tenant\_id* is appended to the
     issuer.
    * *client\_id* - The unique, public identifier of the
     application registered with the identity provider. This can be referred to as the
     application ID.
    * *client\_secret* - A secret identifier, or password, known
     only to the identity provider and the registered application.
    * *audience* - The Application ID that is assigned to the
     application in Azure.

Instead of using a shared client secret, you can set parameters to specify a
certificate, a private key, and a private key password when you create the identity
provider.

```
CREATE IDENTITY PROVIDER example_idp TYPE azure
NAMESPACE 'example_aad'
PARAMETERS '{"issuer":"https://sts.windows.net/2sdfdsf-d475-420d-b5ac-667adad7c702/",
"client_id":"<client_id>",
"audience":["https://analysis.windows.net/powerbi/connector/AmazonRedshift"],
"client_x5t":"<certificate thumbprint>",
"client_pk_base64":"<private key in base64 encoding>",
"client_pk_password":"test_password"}';
```

The private key password, _client_pk_password_, is
optional. 2. Optional: Run SQL commands in Amazon Redshift to pre-create users and roles. This facilitates
granting permissions in advance. The role name in Amazon Redshift is like the following:
_<Namespace>:<GroupName on Azure AD>_. For example,
when you create a group in Microsoft Azure AD called `rsgroup` and a
namespace called `aad`, the role name is `aad:rsgroup`. The user
and role names in Amazon Redshift are defined from these user names and group memberships in the
identity provider namespace.

The mapping for roles and users includes verifying their `external_id`
value, to ensure it's up to date. The external ID maps to the identifier of the group or
user in the identity provider. For example, a role's external ID maps to the
corresponding Azure AD group ID. Similarly, each user's external ID maps to their ID in
the identity provider.

```
create role "aad:rsgroup";
```

3. Grant relevant permissions to roles per your requirements. For example:

```
GRANT SELECT on all tables in schema public to role "aad:rsgroup";
```

4. You can also grant permissions to a specific user.

```
GRANT SELECT on table foo to aad:alice@example.com
```

Note that a federated external user's role membership is available only in that
user's session. This has implications for creating database objects. When a federated
external user creates any view or stored procedure, for instance, the same user can't
delegate permission of those objects to other users and roles.
**An explanation of namespaces**

A namespace maps a user or role to a specific identity provider. For example, the prefix
for users created in AWS IAM is `iam:`. This prefix prevents user name
collisions and makes support for multiple identity stores possible. If a user
alice@example.com from the identity source registered with _aad_
namespace logs in, the user `aad:alice@example.com` is created in Redshift if it
doesn't already exist. Note that a user and role namespace has a different function than an
Amazon Redshift cluster namespace, which is a unique identifier associated with a cluster.
