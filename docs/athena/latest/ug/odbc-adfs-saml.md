# Configure federated access to Amazon Athena for Microsoft AD FS

users using an ODBC client

To set up federated access to Amazon Athena for Microsoft Active Directory Federation Services
(AD FS) users using an ODBC client, you first establish trust between AD FS and your AWS
account. With this trust in place, your AD users can [federate](../../../IAM/latest/UserGuide/id_roles_providers_saml.md#CreatingSAML-configuring-IdP "../../../IAM/latest/UserGuide/id_roles_providers_saml.md#CreatingSAML-configuring-IdP") into AWS using their AD credentials and assume permissions of an
[AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) role to access AWS
resources such as the Athena API.

To create this trust, you add AD FS as a SAML provider to your AWS account and create an
IAM role that federated users can assume. On the AD FS side, you add AWS as a relying
party and write SAML claim rules to send the right user attributes to AWS for
authorization (specifically, Athena and Amazon S3).

Configuring AD FS access to Athena involves the following major steps:

[1. Setting up
an IAM SAML provider and role](#odbc-adfs-saml-setting-up-an-iam-saml-provider-and-role "#odbc-adfs-saml-setting-up-an-iam-saml-provider-and-role")

[2. Configuring AD FS](#odbc-adfs-saml-configuring-ad-fs "#odbc-adfs-saml-configuring-ad-fs")

[3. Creating
Active Directory users and groups](#odbc-adfs-saml-creating-active-directory-users-and-groups "#odbc-adfs-saml-creating-active-directory-users-and-groups")

[4.
Configuring the AD FS ODBC connection to Athena](#odbc-adfs-saml-configuring-the-ad-fs-odbc-connection-to-athena "#odbc-adfs-saml-configuring-the-ad-fs-odbc-connection-to-athena")

## 1. Setting up

an IAM SAML provider and role

In this section, you add AD FS as a SAML provider to your AWS account and create an
IAM role that your federated users can assume.

###### To set up a SAML provider

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Identity providers**.
3. Choose **Add provider**.
4. For **Provider type**, choose
   **SAML**.

![Choose SAML.](images/odbc-adfs-saml-1.png) 5. For **Provider name**, enter
`adfs-saml-provider`. 6. In a browser, enter the following address to download the federation XML file
for your AD FS server. To perform this step, your browser must have access to
the AD FS server.

```
https://`adfs-server-name`/federationmetadata/2007-06/federationmetadata.xml
```

7. In the IAM console, for **Metadata document**, choose
   **Choose file**, and then upload the federation metadata
   file to AWS.
8. To finish, choose **Add provider**.

Next, you create the IAM role that your federated users can assume.

###### To create an IAM role for federated users

1. In the IAM console navigation pane, choose
   **Roles**.
2. Choose **Create role**.
3. For **Trusted entity type**, choose **SAML 2.0
   federation**.
4. For **SAML 2.0-based provider**, choose the
   **adfs-saml-provider** provider that you created.
5. Choose **Allow programmatic and AWS Management Console
   access**, and then choose **Next**.

![Choosing SAML as the trusted entity type.](images/odbc-adfs-saml-2.png) 6. On the **Add permissions** page, filter for the IAM
permissions policies that you require for this role, and then select the
corresponding check boxes. This tutorial attaches the
`AmazonAthenaFullAccess` and `AmazonS3FullAccess`
policies.

![Attaching the Athena full access policy to the role.](images/odbc-adfs-saml-3.png)

![Attaching the Amazon S3 full access policy to the role.](images/odbc-adfs-saml-4.png) 7. Choose **Next**. 8. On the **Name, review, and create** page, for **Role
name**, enter a name for the role. This tutorial uses the name
**adfs-data-access**.

In **Step 1: Select trusted entities**, the
**Principal** field should be automatically populated with
`"Federated:"
 "arn:aws:iam::`account_id`:saml-provider/adfs-saml-provider"`.
The `Condition` field should contain `"SAML:aud"` and
`"https://signin.aws.amazon.com/saml"`.

![Trusted entities JSON.](images/odbc-adfs-saml-5.png)

**Step 2: Add permissions** shows the policies that you have
attached to the role.

![List of policies attached to the role.](images/odbc-adfs-saml-6.png) 9. Choose **Create role**. A banner message confirms creation of
the role. 10. On the **Roles** page, choose the name of the role that you
just created. The summary page for the role shows the policies that have been
attached.

![Summary page for the role.](images/odbc-adfs-saml-7.png)

## 2. Configuring AD FS

Now you are ready to add AWS as a relying party and write SAML claim rules so that
you can send the right user attributes to AWS for authorization.

SAML-based federation has two participant parties: the IdP (Active Directory) and the
relying party (AWS), which is the service or application that uses authentication from
the IdP.

To configure AD FS, you first add a relying party trust, then you configure SAML claim
rules for the relying party. AD FS uses claim rules to form a SAML assertion that is
sent to a relying party. The SAML assertion states that the information about the AD
user is true, and that it has authenticated the user.

### Adding a relying party

trust

To add a relying party trust in AD FS, you use the AD FS server manager.

###### To add a relying party trust in AD FS

1. Sign in to the AD FS server.
2. On the **Start** menu, open **Server
   Manager**.
3. Choose **Tools**, and then choose **AD FS
   Management**.

![Choose Tools, AD FS Management.](images/odbc-adfs-saml-8.png) 4. In the navigation pane, under **Trust Relationships**,
choose **Relying Party Trusts**. 5. Under **Actions**, choose **Add Relying Party
Trust**.

![Choose Add Relying Party Trust.](images/odbc-adfs-saml-9.png) 6. On the **Add Relying Party Trust Wizard** page, choose
**Start**.

![Choose Start.](images/odbc-adfs-saml-10.png) 7. On the **Select Data Source** screen, select the option
**Import data about the relying party published online or on a
local network**. 8. For **Federation metadata address (host name or URL)**,
enter the URL `https://signin.aws.amazon.com/static/saml-metadata.xml` 9. Choose **Next.**

![Configuring the data source.](images/odbc-adfs-saml-11.png) 10. On the **Specify Display Name** page, for
**Display name**, enter a display name for your relying
party, and then choose **Next**.

![Enter a display name for the relying party.](images/odbc-adfs-saml-12.png) 11. On the **Configure Multi-factor Authentication Now**
page, this tutorial selects **I do not want to configure
multi-factor authentication for this relying party trust at this
time**.

For increased security, we recommend that you configure multi-factor
authentication to help protect your AWS resources. Because it uses a
sample dataset, this tutorial doesn't enable multi-factor
authentication.

![Configuring multi-factor authentication.](images/odbc-adfs-saml-13.png) 12. Choose **Next**. 13. On the **Choose Issuance Authorization Rules** page,
select **Permit all users to access this relying
party**.

This option allows all users in Active Directory to use AD FS with AWS
as a relying party. You should consider your security requirements and
adjust this configuration accordingly.

![Configuring user access to the relying party.](images/odbc-adfs-saml-14.png) 14. Choose **Next**. 15. On the **Ready to Add Trust** page, choose
**Next** to add the relying party trust to the AD FS
configuration database.

![Choose Next.](images/odbc-adfs-saml-15.png) 16. On the **Finish** page, choose
**Close**.

![Choose Close.](images/odbc-adfs-saml-16.png)

### Configuring SAML claim rules for the relying party

In this task, you create two sets of claim rules.

The first set, rules 1–4, contains AD FS claim rules that are required to
assume an IAM role based on AD group membership. These are the same rules that you
create if you want to establish federated access to the [AWS Management Console](http://aws.amazon.com/console "http://aws.amazon.com/console").

The second set, rules 5–6, are claim rules required for Athena access
control.

###### To create AD FS claim rules

1. In the AD FS Management console navigation pane, choose **Trust
   Relationships**, **Relying Party
   Trusts**.
2. Find the relying party that you created in the previous section.
3. Right-click the relying party and choose **Edit Claim
   Rules**, or choose **Edit Claim Rules** from
   the **Actions** menu.

![Choose Edit Claim Rules.](images/odbc-adfs-saml-17.png) 4. Choose **Add Rule.** 5. On the **Configure Rule** page of the Add Transform Claim
Rule Wizard, enter the following information to create claim rule 1, and
then choose **Finish**.

    * For **Claim Rule name**, enter
     `NameID`.
    * For **Rule template**, use **Transform an
     Incoming Claim**.
    * For **Incoming claim type**, choose
     **Windows account name**.
    * For **Outgoing claim type**, choose
     **Name ID**.
    * For **Outgoing name ID format**, choose
     **Persistent Identifier**.
    * Select **Pass through all claim values**.

![Create the first claim rule.](images/odbc-adfs-saml-18.png) 6. Choose **Add Rule**, and then enter the following
information to create claim rule 2, and then choose
**Finish**.

    * For **Claim rule name**, enter
     `RoleSessionName`.
    * For **Rule template**, use **Send LDAP
     Attribute as Claims**.
    * For **Attribute store**, choose **Active
     Directory**.
    * For **Mapping of LDAP attributes to outgoing claim
     types**, add the attribute
     `E-Mail-Addresses`. For the
     **Outgoing Claim Type**, enter `https://aws.amazon.com/SAML/Attributes/RoleSessionName`.

![Create the second claim rule.](images/odbc-adfs-saml-19.png) 7. Choose **Add Rule**, and then enter the following
information to create claim rule 3, and then choose
**Finish**.

    * For **Claim rule name**, enter `Get AD
     Groups`.
    * For **Rule template**, use **Send Claims
     Using a Custom Rule**.
    * For **Custom rule**, enter the following
     code:



    ```
    c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname",
     Issuer == "AD AUTHORITY"]=> add(store = "Active Directory", types = ("http://temp/variable"),
     query = ";tokenGroups;{0}", param = c.Value);

    ```


    ![Create the third claim rule.](images/odbc-adfs-saml-20.png)

8. Choose **Add Rule**. Enter the following information to
   create claim rule 4, and then choose **Finish**.
   - For **Claim rule name**, enter
     `Role`.
   - For **Rule template**, use **Send Claims
     Using a Custom Rule**.
   - For **Custom rule**, enter the following code
     with your account number and name of the SAML provider that you
     created earlier:

   ```
   c:[Type == "http://temp/variable", Value =~ "(?i)^aws-"]=> issue(Type = "https://aws.amazon.com/SAML/Attributes/Role",
   Value = RegExReplace(c.Value, "aws-", "arn:aws:iam::AWS_ACCOUNT_NUMBER:saml-provider/adfs-saml-provider,arn:aws:iam:: AWS_ACCOUNT_NUMBER:role/"));
   ```

![Create the fourth claim rule.](images/odbc-adfs-saml-21.png)

## 3. Creating

Active Directory users and groups

Now you are ready to create AD users that will access Athena, and AD groups to place
them in so that you can control levels of access by group. After you create AD groups
that categorize patterns of data access, you add your users to those groups.

###### To create AD users for access to Athena

1. On the Server Manager dashboard, choose **Tools**, and then
   choose **Active Directory Users and Computers**.

![Choose Tools, Active Directory Users and Computers.](images/odbc-adfs-saml-22.png) 2. In the navigation pane, choose **Users**. 3. On the **Active Directory Users and Computers** tool bar,
choose the **Create user** option.

![Choose Create user.](images/odbc-adfs-saml-23.png) 4. In the **New Object – User** dialog box, for
**First name**, **Last name**, and
**Full name**, enter a name. This tutorial uses
`Jane Doe`.

![Enter a user name.](images/odbc-adfs-saml-24.png) 5. Choose **Next**. 6. For **Password**, enter a password, and then retype to
confirm.

For simplicity, this tutorial deselects **User must change password at
next sign on**. In real-world scenarios, you should require newly
created users to change their password.

![Enter a password.](images/odbc-adfs-saml-25.png) 7. Choose **Next**. 8. Choose **Finish.**

![Choose Finish.](images/odbc-adfs-saml-26.png) 9. In **Active Directory Users and Computers**, choose the user
name. 10. In the **Properties** dialog box for the user, for
**E-mail**, enter an email address. This tutorial uses
`jane@example.com`.

![Enter an email address.](images/odbc-adfs-saml-27.png) 11. Choose **OK**.

### Create AD groups to represent data access patterns

You can create AD groups whose members assume the `adfs-data-access`
IAM role when they log in to AWS. The following example creates an AD group
called aws-adfs-data-access.

###### To create an AD group

1. On the Server Manager Dashboard, from the **Tools** menu,
   choose **Active Directory Users and Computers.**
2. On the tool bar, choose the **Create new group**
   option.

![Choose Create new group.](images/odbc-adfs-saml-28.png) 3. In the **New Object - Group** dialog box, enter the
following information:

    * For **Group name**, enter
     `aws-adfs-data-access`.
    * For **Group scope**, select
     **Global**.
    * For **Group type**, select
     **Security**.

![Creating a global security group in AD.](images/odbc-adfs-saml-29.png) 4. Choose **OK**.

### Add AD users to

appropriate groups

Now that you have created both an AD user and an AD group, you can add the user to
the group.

###### To add an AD user to an AD group

1. On the Server Manager Dashboard, on the **Tools** menu,
   choose **Active Directory Users and Computers**.
2. For **First name** and **Last name**,
   choose a user (for example, **Jane Doe**).
3. In the **Properties** dialog box for the user, on the
   **Member Of** tab, choose
   **Add**.

![Choose Add.](images/odbc-adfs-saml-30.png) 4. Add one or more AD FS groups according to your requirements. This tutorial
adds the **aws-adfs-data-access** group. 5. In the **Select Groups** dialog box, for **Enter
the object names to select**, enter the name of the AD FS group
that you created (for example, `aws-adfs-data-access`),
and then choose **Check Names**.

![Choose Check Names.](images/odbc-adfs-saml-31.png) 6. Choose **OK**.

In the **Properties** dialog box for the user, the name
of the AD group appears in the **Member of** list.

![AD group added to user properties.](images/odbc-adfs-saml-32.png) 7. Choose **Apply**, then choose
**OK**.

## 4.

Configuring the AD FS ODBC connection to Athena

After you have created your AD users and groups, you are ready to use the ODBC Data
Sources program in Windows to configure your Athena ODBC connection for AD FS.

###### To configure the AD FS ODBC connection to Athena

1. Install the ODBC driver for Athena. For download links, see [Connect to Amazon Athena with ODBC](connect-with-odbc.md "connect-with-odbc.md").
2. In Windows, choose **Start**, **ODBC Data
   Sources**.
3. In the **ODBC Data Source Administrator** program, choose
   **Add**.

![Choose Add to add an ODBC data source.](images/odbc-adfs-saml-33.png) 4. In the **Create New Data Source** dialog box, choose
**Simba Athena ODBC Driver**, and then choose
**Finish**.

![Choose Simba Athena ODBC Driver.](images/odbc-adfs-saml-34.png) 5. In the **Simba Athena ODBC Driver DSN Setup** dialog box,
enter the following values:

    * For **Data Source Name,** enter a name for your data
     source (for example,  `Athena-odbc-test`).
    * For **Description**, enter a description for your
     data source.
    * For **AWS Region**, enter the AWS Region that you
     are using (for example,  `us-west-1`).
    * For **S3 Output Location**, enter the Amazon S3 path where
     you want your output to be stored.

![Entering values for Simba Athena ODBC Driver DSN Setup.](images/odbc-adfs-saml-35.png) 6. Choose **Authentication Options**. 7. In the **Authentication Options** dialog box, specify the
following values:

    * For **Authentication Type**, choose
     **ADFS**.
    * For **User,** enter the user's email address (for
     example, `jane@example.com`).
    * For **Password**, enter the user's ADFS
     password.
    * For **IdP Host**, enter the AD FS server name (for
     example, `adfs.example.com`).
    * For **IdP Port**, use the default value
     **443**.
    * Select the **SSL Insecure** option.

![Configuring authentication options.](images/odbc-adfs-saml-37.png) 8. Choose **OK** to close **Authentication
Options**. 9. Choose **Test** to test the connection, or
**OK** to finish.
