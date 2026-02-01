Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Setting up AWS IAM Identity Center

integration with Amazon Redshift

Your Amazon Redshift cluster administrator or Amazon Redshift Serverless administrator must perform several
steps to configure Redshift as an AWS IAM Identity Center enabled application. This makes it so
Redshift can discover and connect to AWS IAM Identity Center automatically to receive sign-in and user
directory services. After this, when your Redshift administrator creates a cluster or
workgroup, they can enable the new data warehouse to use AWS IAM Identity Center to manage database
access.

The point of enabling Redshift as an AWS IAM Identity Center managed application is so you can
control user and group permissions from within AWS IAM Identity Center, or from a third-party identity
provider that's integrated with it. When your database users sign in to a Redshift
database, for example an analyst or a data scientist, it checks their groups in AWS IAM Identity Center
and these match up with role names in Redshift. In this manner, a group that defines the
name for a Redshift database role can access a set of tables for sales analytics, for
example. The sections that follow show how to set this up.

## Prerequisites

These are the prerequisites for integrating AWS IAM Identity Center with Amazon Redshift:

- _Account configuration_ – You must configure AWS IAM Identity Center
  in your AWS organization's management account if you plan to have cross-account use
  cases, or if you use Redshift clusters in different accounts with the same AWS
  IAM Identity Center instance. This includes configuring your identity source. For more information,
  see [Getting Started](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md"), [workforce identities](../../../singlesignon/latest/userguide/identities.md "../../../singlesignon/latest/userguide/identities.md"), and [supported identity providers](../../../singlesignon/latest/userguide/supported-idps.md "../../../singlesignon/latest/userguide/supported-idps.md") in the
  _AWS IAM Identity Center User Guide_. You must ensure that you have created
  users or groups in AWS IAM Identity Center, or synchronized users and groups from your identity
  source before you can assign them to data in Redshift.

###### Note

You have an option to use an account instance of AWS IAM Identity Center, provided that
Redshift and AWS IAM Identity Center are in the same account. You can create this instance
using a widget when you create and configure a Redshift cluster or
workgroup.

- _Configuring a trusted token issuer_ – In some cases,
  you may need to use a trusted token issuer, which is an entity that can issue and
  verify trust tokens. Before you can do so, preliminary steps are required before the
  Redshift administrator who configures AWS IAM Identity Center integration can select the trusted
  token issuer and add the necessary attributes to complete the configuration. This can
  include configuring an external identity provider to serve as a trusted token issuer
  and adding its attributes in the AWS IAM Identity Center console. To complete these steps, see
  [Using applications with a trusted token issuer](../../../singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.md#setuptrustedtokenissuer "../../../singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.md#setuptrustedtokenissuer").

###### Note

Setting up a trusted token issuer isn't required for all external connections.
Connecting to your Redshift database with Amazon Redshift query editor v2 doesn't require trusted-token
issuer configuration. But it can apply for third-party applications such as
dashboards or custom applications that authenticate with your identity
provider.

- _Configuring an IAM role or roles_ – The sections that
  follow mention permissions that must be configured. You will have to add permissions
  per IAM best practices. Specific permissions are detailed in the procedures that
  follow.

For more information, see [Getting Started with AWS
IAM Identity Center](../../../singlesignon/latest/userguide/get-started-enable-identity-center.md "../../../singlesignon/latest/userguide/get-started-enable-identity-center.md").

## Configuring your identity

provider to work with AWS IAM Identity Center

The first step in controlling user and group identity management is to connect to
AWS IAM Identity Center and configure your identity provider. You can use AWS IAM Identity Center itself as your
identity provider, or you can connect a third-party identity store, such as Okta, for
instance. For more information about setting up the connection to and configuring your
identity provider, see [Connect to an external identity provider](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") in the _AWS IAM Identity Center user
guide_. Make sure at the end of this process that you have a small collection
of users and groups added to AWS IAM Identity Center, for test purposes.

### Administrative

Permissions

#### Permissions

required for Redshift/AWS IAM Identity Center application lifecycle management

You must create an IAM identity, which a Redshift administrator uses to
configure Redshift for use with AWS IAM Identity Center. Most commonly, you would create an IAM
role with permissions and assign it to other identities as required. It must have the
permissions listed to perform the following actions.

**Creating the Redshift/AWS IAM Identity Center
application**

- `sso:PutApplicationAssignmentConfiguration` – For
  security.
- `sso:CreateApplication` – Used to create an AWS IAM Identity Center
  application.
- `sso:PutApplicationAuthenticationMethod` – Grants Redshift
  authentication access.
- `sso:PutApplicationGrant` – Used to change the trusted token
  issuer information.
- `sso:PutApplicationAccessScope` – For Redshift AWS IAM Identity Center
  application setup. This includes for AWS Lake Formation and for [Amazon S3 Access
  Grants](../../../AmazonS3/latest/userguide/access-grants-get-started.md "../../../AmazonS3/latest/userguide/access-grants-get-started.md").
- `redshift:CreateRedshiftIdcApplication` – Used to create the
  Redshift AWS IAM Identity Center application.

**Describing the Redshift/AWS IAM Identity Center
application**

- `sso:GetApplicationGrant` – Used to list trusted token
  issuer information.
- `sso:ListApplicationAccessScopes` – For Redshift AWS
  IAM Identity Center application setup to list downstream integrations, such as for
  AWS Lake Formation and S3 Access Grants.
- `redshift:DescribeRedshiftIdcApplications` – Used to
  describe existing AWS IAM Identity Center applications.

**Changing the Redshift/AWS IAM Identity Center
application**

- `redshift:ModifyRedshiftIdcApplication` – Used to change an
  existing Redshift application.
- `sso:UpdateApplication` – Used to update an AWS IAM Identity Center
  application.
- `sso:GetApplicationGrant` – Gets the trust token issuer
  information.
- `sso:ListApplicationAccessScopes` – For Redshift AWS
  IAM Identity Center application setup.
- `sso:DeleteApplicationGrant` – Deletes the trust token
  issuer information.
- `sso:PutApplicationGrant` – Used to change the trusted token
  issuer information.
- `sso:PutApplicationAccessScope` – For Redshift AWS IAM Identity Center
  application setup. This includes for AWS Lake Formation and for [Amazon S3 Access
  Grants](../../../AmazonS3/latest/userguide/access-grants-get-started.md "../../../AmazonS3/latest/userguide/access-grants-get-started.md").
- `sso:DeleteApplicationAccessScope` – For deleting Redshift
  AWS IAM Identity Center application setup. This includes for AWS Lake Formation and
  for [Amazon S3 Access
  Grants](../../../AmazonS3/latest/userguide/access-grants-get-started.md "../../../AmazonS3/latest/userguide/access-grants-get-started.md").

**Deleting the Redshift/AWSIAM Identity Center
application**

- `sso:DeleteApplication` – Used to delete an AWS IAM Identity Center
  application.
- `redshift:DeleteRedshiftIdcApplication` – Gives the ability
  to delete an existing Redshift AWS IAM Identity Center application.

#### Permissions

required for Redshift/query editor v2 application lifecycle management

You must create an IAM identity, which a Redshift administrator uses to
configure Redshift for use with AWS IAM Identity Center. Most commonly, you would create an IAM
role with permissions and assign it to other identities as required. It must have the
permissions listed to perform the following actions.

**Creating the query editor v2 application**

- `redshift:CreateQev2IdcApplication` – Used to create the
  QEV2 application.
- `sso:CreateApplication` – Gives the ability to create an
  AWS IAM Identity Center application.
- `sso:PutApplicationAuthenticationMethod` – Grants Redshift
  authentication access.
- `sso:PutApplicationGrant` – Used to change the trusted token
  issuer information.
- `sso:PutApplicationAccessScope` – For Redshift AWS IAM Identity Center
  application setup. This includes query editor v2.
- `sso:PutApplicationAssignmentConfiguration` – For
  security.

**Describe the query editor v2 application**

- `redshift:DescribeQev2IdcApplications` – Used to describe
  the AWS IAM Identity Center QEV2 application.

**Change the query editor v2 application**

- `redshift:ModifyQev2IdcApplication` – Used to change the
  AWS IAM Identity Center QEV2 application.
- `sso:UpdateApplication` – Used to change the AWS IAM Identity Center
  QEV2 application.

**Delete the query editor v2 application**

- `redshift:DeleteQev2IdcApplication` – Used to delete the
  QEV2 application.
- `sso:DeleteApplication` – Used to delete the QEV2
  application.

###### Note

In the Amazon Redshift SDK, the following APIs aren’t available:

- CreateQev2IdcApplication
- DescribeQev2IdcApplications
- ModifyQev2IdcApplication
- DeleteQev2IdcApplication
  These actions are specific to performing AWS IAM Identity Center integration with Redshift
  QEV2 in the AWS console. For more information, see [Actions defined by Amazon Redshift](../../../service-authorization/latest/reference/list_amazonredshift.md#amazonredshift-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonredshift.md#amazonredshift-actions-as-permissions").

#### Permissions required for the database administrator to connect new resources in the

console

These permissions are required to connect new provisioned clusters or
Amazon Redshift Serverless workgroups during the creation process. If you have these
permissions, a selection appears in the console to choose to connect to the AWS
IAM Identity Center managed application for Redshift.

- `redshift:DescribeRedshiftIdcApplications`
- `sso:ListApplicationAccessScopes`
- `sso:GetApplicationAccessScope`
- `sso:GetApplicationGrant`

As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

## Setting up Redshift as an

AWS managed application with AWS IAM Identity Center

Before AWS IAM Identity Center can manage identities for an Amazon Redshift provisioned cluster or an
Amazon Redshift Serverless workgroup, the Redshift administrator must complete the steps to make
Redshift an AWS IAM Identity Center managed application:

1. Select **AWS IAM Identity Center integration** in the Amazon Redshift or Amazon Redshift Serverless
   console menu, and then select **Connect to AWS IAM Identity Center**. From
   there you step through a series of selections to populate the properties for AWS
   IAM Identity Center integration.
2. Choose a display name and a unique name for Redshift's AWS IAM Identity Center-managed
   application.
3. Specify the namespace for your organization. This is typically an abbreviated
   version of your organization's name. It's added as a prefix for your AWS
   IAM Identity Center-managed users and roles in the Redshift database.
4. Select an IAM role to use. This IAM role should be separate from others used
   for Redshift, and we recommend that it isn't used for other purposes. The specific
   policy permissions required are the following:
   - `sso:DescribeApplication` – Required to create an identity
     provider (IdP) entry in the catalog.
   - `sso:DescribeInstance` – Used to manually create IdP
     federated roles or users.

5. Configure client connections and trusted token issuers. Configuring trusted token
   issuers facilitates trusted identity propagation by setting up a relationship with an
   external identity provider. Identity propagation makes it possible for a user, for
   example, to sign into one application and access specific data in another application.
   This allows users to gather data from disparate locations more seamlessly. At this
   step, in the console, you set attributes for each trusted token issuer. The attributes
   include the name and the audience claim (or _aud claim_), which you
   might have to get from the tool's or service's configuration attributes. You might
   also need to supply the application name from the third-party tool's JSON Web Token
   (JWT).

###### Note

The `aud claim` required from each third-party tool or service can
vary, based on the token type, which can be an access token issued by an identity
provider, or another type, like an ID token. Each vendor can be different. When
you’re implementing trusted-identity propagation and integrating with Redshift,
it’s required to supply the correct _aud_ value for the token
type that the third-party tool sends to AWS. Check the recommendations of your
tool or service vendor.

For detailed information regarding trusted-identity propagation, see

[Trusted identity propagation overview](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md")
in the _AWS IAM Identity Center User Guide_.

After the Redshift administrator finishes the steps and saves the configuration, the
AWS IAM Identity Center properties appear in the Redshift console. You can also query the system view
[SVV_IDENTITY_PROVIDERS](../dg/r_SVV_IDENTITY_PROVIDERS.md "../dg/r_SVV_IDENTITY_PROVIDERS.md") to
verify the application's properties. These include the application name and the namespace.
You use the namespace as a prefix for Redshift database objects that are associated with
the application. Completing these tasks makes Redshift an AWS IAM Identity Center enabled
application. The properties in the console include the integration status. It says
**Enabled** when the integration is completed. After this process,
AWS IAM Identity Center integration can be enabled on each new cluster.

After configuration, you can include users and groups from AWS IAM Identity Center in Redshift by
choosing the **Users** or **Groups** tab and
choosing **Assign**.

## Enabling AWS IAM Identity Center

integration for a new Amazon Redshift cluster or Amazon Redshift Serverless workgroup

Your database administrator configures new Redshift resources to work in alignment
with AWS IAM Identity Center to make sign-in and data access easier. This is performed as part of the
steps to create a provisioned cluster or a Serverless workgroup. Anyone with permissions
to create Redshift resources can perform these AWS IAM Identity Center integration tasks.When you
create a provisioned cluster, you start by choosing **Create Cluster**
in the Amazon Redshift console. The steps that follow show how to enable AWS IAM Identity Center management for a
database. (It doesn't include all of the steps to create a cluster.)

1. Choose **Enable for <your cluster name>** in the section
   for **IAM Identity Center integration** in the create-cluster steps.
2. There's a step in the process when you enable integration. You do this by choosing
   **Enable IAM Identity Center integration** in the console.
3. For the new cluster or workgroup, create database roles in Redshift using SQL
   commands. The following is the command:

```
CREATE ROLE <idcnamespace:rolename>;
```

The namespace and role name are the following:

    * *IAM Identity Center namespace prefix* – This is the namespace you
     defined when you set up the connection between AWS IAM Identity Center and Redshift.
    * *Role name* – This Redshift database role must
     match the group name in AWS IAM Identity Center.

Redshift connects with AWS IAM Identity Center and fetches the information needed to create
and map the database role to the AWS IAM Identity Center group.

Note that when a new data warehouse is created, the IAM role specified for AWS
IAM Identity Center integration is automatically attached to the provisioned cluster or
Amazon Redshift Serverless workgroup. After you finish entering the required cluster metadata and
create the resource, you can check the status for AWS IAM Identity Center integration in the
properties. If your group names in AWS IAM Identity Center have spaces, it's required to use quotes in
SQL when you create the matching role.

After you enable the Redshift database and create roles, you are ready to connect to
the database with Amazon Redshift query editor v2 or Amazon Quick Suite. The details are explained
further in sections that follow.

### Setting up the

default `RedshiftIdcApplication` using the API

Setup is performed by your identity administrator. Using the API, you create and
populate a `RedshiftIdcApplication`, which represents the Redshift
application within AWS IAM Identity Center.

1. To start, you can create users and add them to groups in AWS IAM Identity Center. You do
   this in the AWS console for AWS IAM Identity Center.
2. Call `create-redshift-idc-application` to create an AWS IAM Identity Center
   application and make it compatible with Redshift usage. You create the application
   by populating the required values. The display name is the name to display on the
   AWS IAM Identity Center dashboard. The IAM role ARN is an ARN that has permissions to AWS
   IAM Identity Center and is also assumable by Redshift.

```
aws redshift create-redshift-idc-application
––idc-instance-arn 'arn:aws:sso:::instance/ssoins-1234a01a1b12345d'
––identity-namespace 'MYCO'
––idc-display-name 'TEST-NEW-APPLICATION'
––iam-role-arn 'arn:aws:redshift:us-east-1:012345678901:role/TestRedshiftRole'
––redshift-idc-application-name 'myredshiftidcapplication'
```

The following example shows a sample `RedshiftIdcApplication`
response that's returned from the call to
`create-redshift-idc-application`.

```
"RedshiftIdcApplication": {
                "IdcInstanceArn": "arn:aws:sso:::instance/ssoins-1234a01a1b12345d",
                "RedshiftIdcApplicationName": "test-application-1",
                "RedshiftIdcApplicationArn": "arn:aws:redshift:us-east-1:012345678901:redshiftidcapplication:12aaa111-3ab2-3ab1-8e90-b2d72aea588b",
                "IdentityNamespace": "MYCO",
                "IdcDisplayName": "Redshift-Idc-Application",
                "IamRoleArn": "arn:aws:redshift:us-east-1:012345678901:role/TestRedshiftRole",
                "IdcManagedApplicationArn": "arn:aws:sso::012345678901:application/ssoins-1234a01a1b12345d/apl-12345678910",
                "IdcOnboardStatus": "arn:aws:redshift:us-east-1:123461817589:redshiftidcapplication",
                "RedshiftIdcApplicationArn": "Completed",
                "AuthorizedTokenIssuerList": [
                       "TrustedTokenIssuerArn": ...,
                       "AuthorizedAudiencesList": [...]...
                ]}
```

3. You can use `create-application-assignment` to assign particular
   groups or individual users to the managed application in AWS IAM Identity Center. By doing this,
   you can specify groups to manage through AWS IAM Identity Center. If the database administrator
   creates database roles in Redshift, group names in AWS IAM Identity Center map to the role
   names in Redshift. The roles control permissions in the database. For more
   information, see [Assign user access
   to applications in the AWS IAM Identity Center console](../../../singlesignon/latest/userguide/assignuserstoapp.md "../../../singlesignon/latest/userguide/assignuserstoapp.md").
4. After you enable the application, call `create-cluster` and include
   the Redshift managed application ARN from AWS IAM Identity Center. Doing this associates the
   cluster with the managed application in AWS IAM Identity Center.

### Associating an

AWS IAM Identity Center application with an existing cluster or workgroup

If you have an existing cluster or workgroup that you would like to enable for AWS
IAM Identity Center integration, it is possible to do so, running SQL commands. You can also run SQL
commands to change settings for the integration. For more information, see [ALTER IDENTITY
PROVIDER](../dg/r_ALTER_IDENTITY_PROVIDER.md "../dg/r_ALTER_IDENTITY_PROVIDER.md").

It's also possible to drop an existing identity provider. The following example
shows how CASCADE deletes users and roles attached to the identity provider.

```
DROP IDENTITY PROVIDER
<provider_name> [ CASCADE ]
```

## Setting up user

permissions

An administrator configures permissions to various resources, based on users' identity
attributes and group memberships, within their identity provider or within AWS IAM Identity Center
directly.For example, the identity-provider administrator can add a database engineer to a
group appropriate to their role. This group name maps to a Redshift database role name.
The role provides or restricts access to specific tables or views in Redshift.
