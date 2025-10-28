Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# AD FS

This tutorial shows you how you can use AD FS as an identity provider (IdP) to
access your Amazon Redshift cluster.

## Step 1: Set up AD FS

and your AWS account to trust each other

The following procedure describes how to set up a trust relationship.

1. Create or use an existing Amazon Redshift cluster for your AD FS users to
   connect to. To configure the connection, certain properties of this
   cluster are needed, such as the cluster identifier. For more
   information, see [Creating a Cluster](create-cluster.md "create-cluster.md").
2. Set up AD FS to control Amazon Redshift access on the Microsoft Management
   Console:
   1. Choose **ADFS 2.0**, and then choose
      **Add Relying Party Trust**. On the
      **Add Relying Party Trust Wizard**
      page, choose **Start**.
   2. On the **Select Data Source** page,
      choose **Import data about the relying party
      published online or on a local
      network**.
   3. For **Federation metadata address (host name or
      URL)**, enter
      `https://signin.aws.amazon.com/saml-metadata.xml`.
      The metadata XML file is a standard SAML metadata document
      that describes AWS as a relying party.
   4. On the **Specify Display Name** page,
      enter a value for **Display name**.
   5. On the **Choose Issuance Authorization
      Rules** page, choose an issuance authorization
      rule to either permit or deny all users to access this
      relying party.
   6. On the **Ready to Add Trust** page,
      review your settings.
   7. On the **Finish** page, choose
      **Open the Edit Claim Rules dialog for this
      relying party trust when the wizard
      closes**.
   8. On the context (right-click) menu, choose
      **Relying Party Trusts**.
   9. For your relying party, open the context (right-click)
      menu and choose **Edit Claim Rules**. On
      the **Edit Claim Rules** page, choose
      **Add Rule**.
   10. For **Claim rule template**, choose
       **Transform an Incoming Claim**, and
       then on the **Edit Rule – NameId** page, do
       the following:
       - For **Claim rule name**,
         enter **NameId**.
       - For **Incoming claim name**,
         choose **Windows Account
         Name**.
       - For **Outgoing claim name**,
         choose **Name ID**.
       - For **Outgoing name ID format**,
         choose **Persistent
         Identifier**.
       - Choose **Pass through all claim
         values**.

   11. On the **Edit Claim Rules** page, choose
       **Add Rule**. On the **Select
       Rule Template** page, for **Claim rule
       template**, choose **Send LDAP
       Attributes as Claims**.
   12. On the **Configure Rule** page, do the
       following:
       - For **Claim rule name**, enter
         **RoleSessionName**.
       - For **Attribute store**, choose
         **Active Directory**.
       - For **LDAP Attribute**, choose
         **Email Addresses**.
       - For **Outgoing Claim Type**,
         choose
         **https://aws.amazon.com/SAML/Attributes/RoleSessionName**.

   13. On the **Edit Claim Rules** page, choose
       **Add Rule**. On the **Select
       Rule Template** page, for **Claim rule
       template**, choose **Send Claims Using
       a Custom Rule**.
   14. On the **Edit Rule – Get AD Groups**
       page, for **Claim rule name**, enter
       **Get AD Groups**.
   15. For **Custom rule**, enter the
       following.

   ```
   c:[Type ==
                                       "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname",
                                       Issuer == "AD AUTHORITY"] => add(store = "Active Directory",
                                       types = ("http://temp/variable"), query = ";tokenGroups;{0}",
                                       param = c.Value);
   ```

   16. On the **Edit Claim Rules** page, choose
       **Add Rule**. On the **Select
       Rule Template** page, for **Claim rule
       template**, choose **Send Claims Using
       a Custom Rule**.
   17. On the **Edit Rule – Roles** page, for
       **Claim rule name**, type
       **Roles**.
   18. For **Custom rule,** enter the
       following.

   ```
   c:[Type == "http://temp/variable", Value =~ "(?i)^AWS-"] => issue(Type = "https://aws.amazon.com/SAML/Attributes/Role", Value = RegExReplace(c.Value, "AWS-", "arn:aws:iam::123456789012:saml-provider/ADFS,arn:aws:iam::123456789012:role/ADFS-"));
   ```

   Note the ARNs of the SAML provider and role to assume. In
   this example,
   `arn:aws:iam:123456789012:saml-provider/ADFS`
   is the ARN of the SAML provider and
   `arn:aws:iam:123456789012:role/ADFS-` is the
   ARN of the role.

3. Make sure that you have downloaded the
   `federationmetadata.xml` file. Check that the
   document contents do not have invalid characters. This is the
   metadata file you use when configuring the trust relationship with
   AWS.
4. Create an IAM SAML identity provider on the IAM console. The
   metadata document. that you provide is the federation metadata XML
   file that you saved when you set up Azure Enterprise Application.
   For detailed steps, see [Creating and Managing an IAM Identity Provider
   (Console)](../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console "../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md#idp-manage-identityprovider-console") in the _IAM User Guide_.
5. Create an IAM role for SAML 2.0 federation on the IAM console. For
   detailed steps, see [Creating a Role for SAML](../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create "../../../IAM/latest/UserGuide/id_roles_create_for-idp_saml.md#idp_saml_Create") in the
   _IAM User Guide_.
6. Create an IAM policy that you can attach to the IAM role that you
   created for SAML 2.0 federation on the IAM console. For detailed
   steps, see [Creating IAM Policies (Console)](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-start") in the
   _IAM User Guide_. For an Azure AD example,
   see [Setting up JDBC or ODBC single
   sign-on authentication](setup-azure-ad-identity-provider.md "setup-azure-ad-identity-provider.md").

## Step 2: Set up JDBC or

ODBC for authentication to AD FS

JDBC
The following procedure describes how to set up a JDBC
relationship to AD FS.

- Configure your database client to connect to your
  cluster through JDBC using AD FS single sign-on.

You can use any client that uses a JDBC driver to
connect using AD FS single sign-on or use a language
like Java to connect using a script. For installation
and configuration information, see [Configuring a connection for JDBC driver version 2.x for
Amazon Redshift](jdbc20-install.md "jdbc20-install.md").

For example, you can use SQLWorkbench/J as the client.
When you configure SQLWorkbench/J, the URL of your
database uses the following format.

```
jdbc:redshift:iam://`cluster-identifier`:`us-west-1`/`dev`
```

If you use SQLWorkbench/J as the client, take the
following steps:

    1. Start SQL Workbench/J. In the **Select
     Connection Profile** page, add a
     **Profile Group**, for example
     `ADFS`.
    2. For **Connection Profile**,
     enter your connection profile name, for example
     `ADFS`.
    3. Choose **Manage Drivers**,
     and choose **Amazon Redshift**.
     Choose the **Open Folder** icon
     next to **Library**, then choose
     the appropriate JDBC .jar file.
    4. On the **Select Connection
     Profile** page, add information to the
     connection profile as follows:




    	+ For **User**, enter your AD
    	 FS user name. This is the user name of the account
    	 that you are using for single sign-on that has
    	 permission to the cluster that you are trying to
    	 authenticate using.
    	+ For **Password**, enter
    	 your AD FS password.
    	+ For **Drivers**, choose
    	 **Amazon Redshift
    	 (com.amazon.redshift.jdbc.Driver)**.
    	+ For **URL**, enter
    	 `jdbc:redshift:iam://`your-cluster-identifier`:`your-cluster-region`/`your-database-name``.
    5. Choose **Extended
     Properties**. For
     **plugin\_name**, enter
     `com.amazon.redshift.plugin.AdfsCredentialsProvider`.
     This value specifies to the driver to use AD FS
     single sign-on as the authentication method.

ODBC

###### To set up ODBC for authentication to AD FS

- Configure your database client to connect to your
  cluster through ODBC using AD FS single sign-on.

Amazon Redshift provides ODBC drivers for Linux, Windows, and
macOS operating systems. Before you install an ODBC
driver, determine whether your SQL client tool is 32-bit
or 64-bit. Install the ODBC driver that matches the
requirements of your SQL client tool.

On Windows, in the **Amazon Redshift ODBC
Driver DSN Setup** page, under
**Connection Settings**, enter the
following information:

    + For **Data Source Name**,
     enter
     ``your-DSN``.
     This specifies the data source name used as the
     ODBC profile name.
    + For **Auth type**, choose
     **Identity Provider: SAML**. This
     is the authentication method that the ODBC driver
     uses to authenticate using AD FS single
     sign-on.
    + For **Cluster ID**, enter
     ``your-cluster-identifier``.
    + For **Region**, enter
     ``your-cluster-region``.
    + For **Database**, enter
     ``your-database-name``.
    + For **User**, enter
     ``your-adfs-username``.
     This is the user name for the AD FS account that
     you are using for single sign-on that has
     permission to the cluster that you're trying to
     authenticate using. Use this only for
     **Auth type** is
     **Identity Provider:
     SAML**.
    + For **Password**, enter
     ``your-adfs-password``.
     Use this only for **Auth type**
     is **Identity Provider: SAML**.

On macOS and Linux, edit the `odbc.ini`
file as follows:

###### Note

All entries are case-insensitive.

    + For **clusterid**, enter
     ``your-cluster-identifier``.
     This is the name of the created Amazon Redshift
     cluster.
    + For **region**, enter
     ``your-cluster-region``.
     This is the AWS Region of the created Amazon Redshift
     cluster.
    + For **database**, enter
     ``your-database-name``.
     This is the name of the database that you're
     trying to access on the Amazon Redshift cluster.
    + For **locale**, enter
     `en-us`. This is the language
     that error messages display in.
    + For **iam**, enter
     `1`. This value specifies to
     the driver to authenticate using IAM
     credentials.
    + For **plugin\_name**, do one
     of the following:




    	- For AD FS single sign-on with MFA
    	 configuration, enter
    	 `BrowserSAML`. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate to AD FS.
    	- For AD FS single sign-on configuration,
    	 enter `ADFS`. This is the
    	 authentication method that the ODBC driver uses to
    	 authenticate using Azure AD single sign-on.
    + For **uid**, enter
     ``your-adfs-username``.
     This is the user name of the Microsoft Azure
     account that you are using for single sign-on that
     has permission to the cluster you are trying to
     authenticate against. Use this only for
     **plugin\_name** is
     **ADFS**.
    + For **pwd**, enter
     ``your-adfs-password``.
     Use this only for **plugin\_name**
     is **ADFS**.

On macOS and Linux, also edit the profile settings to
add the following exports.

```
export ODBCINI=/opt/amazon/redshift/Setup/odbc.ini
```

```
export ODBCINSTINI=/opt/amazon/redshift/Setup/odbcinst.ini
```
