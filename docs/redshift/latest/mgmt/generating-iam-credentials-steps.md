Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating temporary IAM

credentials

In this section, you can find how to configure your system to generate temporary
IAM-based database user credentials and log in to your database using the new
credentials.

At a high level, the process flows as follows:

1. [Step 1: Create an
   IAM role for IAM single sign-on access](#generating-iam-credentials-sso-role "#generating-iam-credentials-sso-role")

(Optional) You can authenticate users for access to an Amazon Redshift database by
integrating IAM authentication and a third-party identity provider (IdP). 2. [Step 2: Configure SAML
assertions for your IdP](#configuring-saml-assertions "#configuring-saml-assertions")

(Optional) To use IAM authentication using an IdP, you need to define a claim
rule in your IdP application that maps users or groups in your organization to
the IAM role. Optionally, you can include attribute elements to set
`GetClusterCredentials` parameters. 3. [Step 3:
Create an IAM role with permissions to call GetClusterCredentials](#generating-iam-credentials-role-permissions "#generating-iam-credentials-role-permissions")

Your SQL client application assumes the user when it calls the
`GetClusterCredentials` operation. If you created an IAM role for
identity provider access, you can add the necessary permission to that
role. 4. [Step 4:
Create a database user and database groups](#generating-iam-credentials-user-and-groups "#generating-iam-credentials-user-and-groups")

(Optional) By default, `GetClusterCredentials` returns credentials
create a new user if the user name doesn't exist. You can also choose to
specify user groups that users join at logon. By default, database users join
the PUBLIC group. 5. [Step
5: Configure a JDBC or ODBC connection to use IAM credentials](#generating-iam-credentials-configure-jdbc-odbc "#generating-iam-credentials-configure-jdbc-odbc")

To connect to your Amazon Redshift database, you configure your SQL client to use an Amazon Redshift
JDBC or ODBC driver.

## Step 1: Create an

IAM role for IAM single sign-on access

If you don't use an identity provider for single sign-on access, you can skip
this step.

If you already manage user identities outside of AWS, you can authenticate users
for access to an Amazon Redshift database by integrating IAM authentication and a third-party
SAML-2.0 identity provider (IdP).

For more information, see [Identity Providers and Federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md") in the _IAM User Guide_.

Before you can use Amazon Redshift IdP authentication, create an AWS SAML identity
provider. You create an IdP in the IAM console to inform AWS about the IdP and its
configuration. Doing this establishes trust between your AWS account and the IdP.
For steps to create a role, see [Creating a Role for SAML 2.0 Federation (Console)](../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md") in the
_IAM User Guide_.

## Step 2: Configure SAML

assertions for your IdP

After you create the IAM role, you define a claim rule in your IdP application to
map users or groups in your organization to the IAM role. For more information, see
[Configuring SAML Assertions for the Authentication Response](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md") in the
_IAM User Guide_.

If you choose to use the optional `GetClusterCredentials` parameters
`DbUser`, `AutoCreate`, and `DbGroups`, you
have two options. You can set the values for the parameters with your JDBC or ODBC
connection, or you can set the values by adding SAML attribute elements to your IdP.
For more information about the `DbUser`, `AutoCreate`, and
`DbGroups` parameters, see [Step
5: Configure a JDBC or ODBC connection to use IAM credentials](#generating-iam-credentials-configure-jdbc-odbc "#generating-iam-credentials-configure-jdbc-odbc").

###### Note

If you use an IAM policy variable `${redshift:DbUser}`, as
described in [Resource
policies for GetClusterCredentials](redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources "redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources")
the value for `DbUser` is replaced with the value retrieved by the
API operation's request context. The Amazon Redshift drivers use the value for the
`DbUser` variable provided by the connection URL, rather than the
value supplied as a SAML attribute.

To help secure this configuration, we recommend that you use a condition in an
IAM policy to validate the `DbUser` value by using
`RoleSessionName`. You can find examples of how to set a
condition using an IAM policy in [Example policy for using
GetClusterCredentials](redshift-iam-access-control-identity-based.md#redshift-policy-examples-getclustercredentials "redshift-iam-access-control-identity-based.md#redshift-policy-examples-getclustercredentials").

To configure your IdP to set the `DbUser`, `AutoCreate`, and
`DbGroups` parameters, include the following `Attribute`
elements:

- An `Attribute` element with the `Name` attribute set
  to "https://redshift.amazon.com/SAML/Attributes/DbUser"

Set the `AttributeValue` element to the name of a user that
will connect to the Amazon Redshift database.

The value in the `AttributeValue` element must be lowercase,
begin with a letter, contain only alphanumeric characters, underscore ('\_'),
plus sign ('+'), dot ('.'), at ('@'), or hyphen ('-'), and be fewer than 128
characters. Typically, the user name is a user ID (for example, bobsmith) or
an email address (for example bobsmith@example.com). The value can't
include a space (for example, a user's display name such as Bob
Smith).

```
<Attribute Name="https://redshift.amazon.com/SAML/Attributes/DbUser">
    <AttributeValue>user-name</AttributeValue>
</Attribute>
```

- An Attribute element with the Name attribute set to
  "https://redshift.amazon.com/SAML/Attributes/AutoCreate"

Set the AttributeValue element to true to create a new database user if
one doesn't exist. Set the AttributeValue to false to specify that the
database user must exist in the Amazon Redshift database.

```
<Attribute Name="https://redshift.amazon.com/SAML/Attributes/AutoCreate">
    <AttributeValue>true</AttributeValue>
</Attribute>
```

- An `Attribute` element with the `Name` attribute set
  to set to "https://redshift.amazon.com/SAML/Attributes/DbGroups"

This element contains one or more `AttributeValue` elements.
Set each `AttributeValue` element to a database group name that
the `DbUser` joins for the duration of the session when
connecting to the Amazon Redshift database.

```
<Attribute Name="https://redshift.amazon.com/SAML/Attributes/DbGroups">
    <AttributeValue>group1</AttributeValue>
    <AttributeValue>group2</AttributeValue>
    <AttributeValue>group3</AttributeValue>
</Attribute>
```

## Step 3:

Create an IAM role with permissions to call GetClusterCredentials

Your SQL client needs authorization to call the `GetClusterCredentials`
operation on your behalf. To provide that authorization, you create a user or role
and attach a policy that grants the necessary permissions.

###### To create an IAM role with permissions to call GetClusterCredentials

1. Using the IAM service, create a user or role. You can also use an existing
   user or role. For example, if you created an IAM role for identity provider
   access, you can attach the necessary IAM policies to that role.
2. Attach a permission policy with permission to call the
   `redshift:GetClusterCredentials` operation. Depending on
   which optional parameters you specify, you can also allow or restrict
   additional actions and resources in your policy:
   - To permit your SQL client to retrieve cluster ID, AWS Region,
     and port, include permission to call the
     `redshift:DescribeClusters` operation with the
     Redshift cluster resource.
   - If you use the `AutoCreate` option, include permission
     to call `redshift:CreateClusterUser` with the
     `dbuser` resource. The following Amazon Resource Name
     (ARN) specifies the Amazon Redshift `dbuser`. Replace
     `region`,
     `account-id`, and
     `cluster-name` with
     the values for your AWS Region, account, and cluster. For
     `dbuser-name`, specify
     the user name to use to log in to the cluster database.

   ```
   arn:aws:redshift:`region`:`account-id`:dbuser:`cluster-name`/`dbuser-name`

   ```

   - (Optional) Add an ARN that specifies the Amazon Redshift `dbname`
     resource in the following format. Replace
     `region`,
     `account-id`, and
     `cluster-name` with
     the values for your AWS Region, account, and cluster. For
     `database-name`,
     specify the name of a database that the user will log in to.

   ```
   arn:aws:redshift:`region`:`account-id`:dbname:`cluster-name`/`database-name`

   ```

   - If you use the `DbGroups` option, include permission to
     call the `redshift:JoinGroup` operation with the Amazon Redshift
     `dbgroup` resource in the following format. Replace
     `region`,
     `account-id`, and
     `cluster-name` with
     the values for your AWS Region, account, and cluster. For
     `dbgroup-name`,
     specify the name of a user group that the user joins at
     login.

   ```
   arn:aws:redshift:`region`:`account-id`:dbgroup:`cluster-name`/`dbgroup-name`
   ```

For more information and examples, see [Resource
policies for GetClusterCredentials](redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources "redshift-iam-access-control-identity-based.md#redshift-policy-resources.getclustercredentials-resources").

The following example shows a policy that allows the IAM role to call the
`GetClusterCredentials` operation. Specifying the Amazon Redshift
`dbuser` resource grants the role access to the database user name
`temp_creds_user` on the cluster named
`examplecluster`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "redshift:GetClusterCredentials",
 "Resource": "arn:aws:redshift:us-west-2:123456789012:dbuser:examplecluster/temp_creds_user"
 }
}`

```

You can use a wildcard (\*) to replace all, or a portion of, the cluster name, user
name, and database group names. The following example allows any user name beginning
with `temp_` with any cluster in the specified account.

###### Important

The statement in the following example specifies a wildcard character (\*) as
part of the value for the resource so that the policy permits any resource that
begins with the specified characters. Using a wildcard character in your IAM
policies might be overly permissive. As a best practice, we recommend using the
most restrictive policy feasible for your business application.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": "redshift:GetClusterCredentials",
 "Resource": "arn:aws:redshift:us-west-2:123456789012:dbuser:*/temp_*"
 }
}`

```

The following example shows a policy that allows the IAM role to call the
`GetClusterCredentials` operation with the option to automatically
create a new user and specify groups the user joins at login. The `"Resource":
 "*"` clause grants the role access to any resource, including clusters,
database users, or user groups.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "redshift:GetClusterCredentials",
 "redshift:CreateClusterUser",
 "redshift:JoinGroup"
 ],
 "Resource": "*"
 }
}`

```

For more information, see [Amazon
Redshift ARN syntax](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-redshift "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-redshift").

## Step 4:

Create a database user and database groups

Optionally, you can create a database user that you use to log in to the cluster
database. If you create temporary user credentials for an existing user, you can
disable the user's password to force the user to log on with the temporary
password. Alternatively, you can use the `GetClusterCredentials`
Autocreate option to automatically create a new database user.

You can create database user groups with the permissions you want the IAM database
user to join at login. When you call the `GetClusterCredentials`
operation, you can specify a list of user group names that the new user joins at
login. These group memberships are valid only for sessions created using credentials
generated with the given request.

###### To create a database user and database groups

1. Log in to your Amazon Redshift database and create a database user using [CREATE USER](../dg/r_CREATE_USER.md "../dg/r_CREATE_USER.md") or alter an
   existing user using [ALTER
   USER](../dg/r_ALTER_USER.md "../dg/r_ALTER_USER.md").
2. Optionally, specify the PASSWORD DISABLE option to prevent the user from
   using a password. When a user's password is disabled, the user can log
   on only using temporary credentials. If the password is not disabled, the
   user can log on either with the password or using temporary credentials. You
   can't disable the password for a superuser.

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

| Which user needs programmatic access?                     | To                                                                                                              | By                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Workforce identity (Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions for the interface that you want to use. <br>• For the AWS CLI, see [Configuring the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_. <br>• For AWS SDKs, tools, and AWS APIs, see [IAM Identity Center authentication](../../../sdkref/latest/guide/access-sso.md "../../../sdkref/latest/guide/access-sso.md") in the _AWS SDKs and Tools Reference Guide_.                                                                                                                                                                                                                        |
| IAM                                                       | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs.                  | Following the instructions in [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the _IAM User Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IAM                                                       | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use. <br>• For the AWS CLI, see [Authenticating using IAM user credentials](../../../cli/latest/userguide/cli-authentication-user.md "../../../cli/latest/userguide/cli-authentication-user.md") in the _AWS Command Line Interface User Guide_. <br>• For AWS SDKs and tools, see [Authenticate using long-term credentials](../../../sdkref/latest/guide/access-iam-users.md "../../../sdkref/latest/guide/access-iam-users.md") in the _AWS SDKs and Tools Reference Guide_. <br>• For AWS APIs, see [Managing access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md") in the _IAM User Guide_. | The following example creates a user with password disabled. `create user temp_creds_user password disable;` The following example disables the password for an existing user. `alter user temp_creds_user password disable;` 3. Create database user groups using [CREATE GROUP](../dg/r_CREATE_GROUP.md "../dg/r_CREATE_GROUP.md"). 4. Use the [GRANT](../dg/r_GRANT.md "../dg/r_GRANT.md") command to define access privileges for the groups. ## Step 5: Configure a JDBC or ODBC connection to use IAM credentials You can configure your SQL client with an Amazon Redshift JDBC or ODBC driver. This driver manages the process of creating database user credentials and establishing a connection between your SQL client and your Amazon Redshift database. If you use an identity provider for authentication, specify the name of a credential provider plugin. The Amazon Redshift JDBC and ODBC drivers include plugins for the following SAML-based identity providers: <br>• Active Directory Federation Services (AD FS) <br>• PingOne <br>• Okta <br>• Microsoft Azure AD For the steps to set up Microsoft Azure AD as an identity provider, see [Setting up JDBC or ODBC single sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md"). ###### To configure a JDBC connection to use IAM credentials 1. Download the latest Amazon Redshift JDBC driver from the [Configuring a connection for JDBC driver version 2.x for Amazon Redshift](jdbc20-install.md "jdbc20-install.md") page. 2. Create a JDBC URL with the IAM credentials options in one of the following formats. To use IAM authentication, add `iam:` to the Amazon Redshift JDBC URL following `jdbc:redshift:` as shown in the following example. `jdbc:redshift:iam://` Add `cluster-name`, `region`, and `account-id`. The JDBC driver uses your IAM account information and cluster name to retrieve the cluster ID and AWS Region. To do so, your user or role must have permission to call the `redshift:DescribeClusters` operation with the specified cluster. If your user or role doesn't have permission to call the `redshift:DescribeClusters` operation, include the cluster ID, AWS Region, and port as shown in the following example. The port number is optional. `jdbc:redshift:iam://examplecluster.abc123xyz789.us-west-2.redshift.amazonaws.com:5439/dev` 3. Add JDBC options to provide IAM credentials. You use different combinations of JDBC options to provide IAM credentials. For details, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). The following URL specifies AccessKeyID and SecretAccessKey for a user. `jdbc:redshift:iam://examplecluster:us-west-2/dev?AccessKeyID=AKIAIOSFODNN7EXAMPLE&SecretAccessKey=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` The following example specifies a named profile that contains the IAM credentials. `jdbc:redshift:iam://examplecluster:us-west-2/dev?Profile=user2` 4. Add JDBC options that the JDBC driver uses to call the `GetClusterCredentials` API operation. Don't include these options if you call the `GetClusterCredentials` API operation programmatically. The following example includes the JDBC `GetClusterCredentials` options. `jdbc:redshift:iam://examplecluster:us-west-2/dev?plugin_name=com.amazon.redshift.plugin.AzureCredentialsProvider&UID=user&PWD=password&idp_tenant=my_tenant&client_secret=my_secret&client_id=my_id` ###### To configure an ODBC connection to use IAM credentials In the following procedure, you can find steps only to configure IAM authentication. For steps to use standard authentication, using a database user name and password, see [Configuring a connection for ODBC driver version 2.x for Amazon Redshift](odbc20-install.md "odbc20-install.md"). 1. Install and configure the latest Amazon Redshift OBDC driver for your operating system. For more information, see [Configuring a connection for ODBC driver version 2.x for Amazon Redshift](odbc20-install.md "odbc20-install.md") page. ###### Important The Amazon Redshift ODBC driver must be version 1.3.6.1000 or later. 2. Follow the steps for your operating system to configure connection settings. 3. On Microsoft Windows operating systems, access the Amazon Redshift ODBC Driver DSN Setup window. 1. Under **Connection Settings**, enter the following information: <br>• **Data Source Name** <br>• **Server** (optional) <br>• **Port** (optional) <br>• **Database** If your user or role has permission to call the `redshift:DescribeClusters` operation, only **Data Source Name** and **Database** are required. Amazon Redshift uses **ClusterId** and **Region** to get the server and port by calling the `DescribeCluster` operation. If your user or role doesn't have permission to call the `redshift:DescribeClusters` operation, specify **Server** and **Port**. 2. Under **Authentication**, choose a value for **Auth Type**. For each authentication type, enter values as listed following: AWS Profile Enter the following information: <br>• **ClusterID** <br>• **Region** <br>• **Profile name** Enter the name of a profile in an AWS config file that contains values for the ODBC connection options. For more information, see [Using a configuration profile](options-for-providing-iam-credentials.md#using-configuration-profile "options-for-providing-iam-credentials.md#using-configuration-profile"). (Optional) Provide details for options that the ODBC driver uses to call the `GetClusterCredentials` API operation: <br>• **DbUser** <br>• **User AutoCreate** <br>• **DbGroups** For more information, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). IAM Credentials Enter the following information: <br>• **ClusterID** <br>• **Region** <br>• **AccessKeyID** and **SecretAccessKey** The access key ID and secret access key for the IAM role or user configured for IAM database authentication. <br>• **SessionToken** **SessionToken** is required for an IAM role with temporary credentials. For more information, see [Temporary Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md"). Provide details for options that the ODBC driver uses to call the `GetClusterCredentials` API operation: <br>• **DbUser** (required) <br>• **User AutoCreate** (optional) <br>• **DbGroups** (optional) For more information, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). Identity Provider: AD FS For Windows Integrated Authentication with AD FS, leave **User** and **Password** empty. Provide IdP details: <br>• **IdP Host** The name of the corporate identity provider host. This name should not include any slashes ( / ). <br>• **IdP Port** (optional) The port used by identity provider. The default is 443. <br>• **Preferred Role** An Amazon Resource Name (ARN) for the IAM role from the multi-valued `AttributeValue` elements for the `Role` attribute in the SAML assertion. To find the appropriate value for the preferred role, work with your IdP administrator. For more information, see [Step 2: Configure SAML assertions for your IdP](#configuring-saml-assertions "#configuring-saml-assertions"). (Optional) Provide details for options that the ODBC driver uses to call the `GetClusterCredentials` API operation: <br>• **DbUser** <br>• **User AutoCreate** <br>• **DbGroups** For more information, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). Identity Provider: PingFederate For **User** and **Password**, enter your IdP user name and password. Provide IdP details: <br>• **IdP Host** The name of the corporate identity provider host. This name should not include any slashes ( / ). <br>• **IdP Port** (optional) The port used by identity provider. The default is 443. <br>• **Preferred Role** An Amazon Resource Name (ARN) for the IAM role from the multi-valued `AttributeValue` elements for the `Role` attribute in the SAML assertion. To find the appropriate value for the preferred role, work with your IdP administrator. For more information, see [Step 2: Configure SAML assertions for your IdP](#configuring-saml-assertions "#configuring-saml-assertions"). (Optional) Provide details for options that the ODBC driver uses to call the `GetClusterCredentials` API operation: <br>• **DbUser** <br>• **User AutoCreate** <br>• **DbGroups** For more information, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). Identity Provider: Okta For **User** and **Password**, enter your IdP user name and password. Provide IdP details: <br>• **IdP Host** The name of the corporate identity provider host. This name should not include any slashes ( / ). <br>• **IdP Port** This value is not used by Okta. <br>• **Preferred Role** An Amazon Resource Name (ARN) for the IAM role from the `AttributeValue` elements for the `Role` attribute in the SAML assertion. To find the appropriate value for the preferred role, work with your IdP administrator. For more information, see [Step 2: Configure SAML assertions for your IdP](#configuring-saml-assertions "#configuring-saml-assertions"). <br>• **Okta App ID** An ID for an Okta application. The value for App ID follows "amazon_aws" in the Okta application embed link. Work with your IdP administrator to get this value. (Optional) Provide details for options that the ODBC driver uses to call the `GetClusterCredentials` API operation: <br>• **DbUser** <br>• **User AutoCreate** <br>• **DbGroups** For more information, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). Identity Provider: Azure AD For **User** and **Password**, enter your IdP user name and password. For **Cluster ID** and **Region**, enter the cluster ID and AWS Region of your Amazon Redshift cluster. For **Database**, enter the database that you created for your Amazon Redshift cluster. Provide IdP details: <br>• **IdP Tenant** The tenant used for Azure AD. <br>• **Azure Client Secret** The client secret of the Amazon Redshift enterprise app in Azure. <br>• **Azure Client ID** The client ID (application ID) of the Amazon Redshift enterprise app in Azure. (Optional) Provide details for options that the ODBC driver uses to call the `GetClusterCredentials` API operation: <br>• **DbUser** <br>• **User AutoCreate** <br>• **DbGroups** For more information, see [JDBC and ODBC options for creating database user credentials](options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials "options-for-providing-iam-credentials.md#jdbc-and-odbc-options-for-database-credentials"). |
