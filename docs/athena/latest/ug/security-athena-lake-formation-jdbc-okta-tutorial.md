# Tutorial: Configure

federated access for Okta users to Athena using Lake Formation and JDBC

This tutorial shows you how to configure Okta, AWS Lake Formation, AWS Identity and Access Management permissions, and the
Athena JDBC driver to enable SAML-based federated use of Athena. Lake Formation provides fine-grained
access control over the data that is available in Athena to the SAML-based user. To set up
this configuration, the tutorial uses the Okta developer console, the AWS IAM and Lake Formation
consoles, and the SQL Workbench/J tool.

###### Prerequisites

This tutorial assumes that you have done the following:

- Created an Amazon Web Services account. To create an account, visit the [Amazon Web Services home page](https://aws.amazon.com/ "https://aws.amazon.com/").
- [Set up a query results
  location](query-results-specify-location.md "query-results-specify-location.md") for Athena in Amazon S3.
- [Registered an Amazon S3 data bucket
  location](../../../lake-formation/latest/dg/register-data-lake.md "../../../lake-formation/latest/dg/register-data-lake.md") with Lake Formation.
- Defined a [database](../../../glue/latest/dg/define-database.md "../../../glue/latest/dg/define-database.md") and
  [tables](../../../glue/latest/dg/tables-described.md "../../../glue/latest/dg/tables-described.md") on the [AWS Glue Data Catalog](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") that point to your
  data in Amazon S3.
  - If you have not yet defined a table, either [run a AWS Glue crawler](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") or [use Athena to
    define a database and one or more tables](work-with-data.md "work-with-data.md") for the data that you
    want to access.
  - This tutorial uses a table based on the [NYC taxi
    trips dataset](https://registry.opendata.aws/nyc-tlc-trip-records-pds/ "https://registry.opendata.aws/nyc-tlc-trip-records-pds/") available in the [Registry of open data on
    AWS](https://registry.opendata.aws/ "https://registry.opendata.aws/"). The tutorial uses the database name `tripdb`
    and the table name `nyctaxi`.

###### Tutorial Steps

- [Step 1: Create an Okta account](#security-athena-lake-formation-jdbc-okta-tutorial-step-1-create-an-okta-account "#security-athena-lake-formation-jdbc-okta-tutorial-step-1-create-an-okta-account")
- [Step 2: Add users and groups to Okta](#security-athena-lake-formation-jdbc-okta-tutorial-step-2-set-up-an-okta-application-for-saml-authentication "#security-athena-lake-formation-jdbc-okta-tutorial-step-2-set-up-an-okta-application-for-saml-authentication")
- [Step 3: Set up an Okta application for SAML authentication](#security-athena-lake-formation-jdbc-okta-tutorial-step-3-set-up-an-okta-application-for-saml-authentication "#security-athena-lake-formation-jdbc-okta-tutorial-step-3-set-up-an-okta-application-for-saml-authentication")
- [Step 4: Create an AWS SAML Identity Provider and Lake Formation access IAM
  role](#security-athena-lake-formation-jdbc-okta-tutorial-step-4-create-an-aws-saml-identity-provider-and-lake-formation-access-IAM-role "#security-athena-lake-formation-jdbc-okta-tutorial-step-4-create-an-aws-saml-identity-provider-and-lake-formation-access-IAM-role")
- [Step 5: Add the IAM role and SAML Identity Provider to the Okta
  application](#security-athena-lake-formation-jdbc-okta-tutorial-step-5-update-the-okta-application-with-the-aws-role-and-saml-identity-provider "#security-athena-lake-formation-jdbc-okta-tutorial-step-5-update-the-okta-application-with-the-aws-role-and-saml-identity-provider")
- [Step 6: Grant user and group permissions through AWS Lake Formation](#security-athena-lake-formation-jdbc-okta-tutorial-step-6-grant-permissions-through-aws-lake-formation "#security-athena-lake-formation-jdbc-okta-tutorial-step-6-grant-permissions-through-aws-lake-formation")
- [Step 7: Verify access through the Athena JDBC client](#security-athena-lake-formation-jdbc-okta-tutorial-step-7-verify-access-through-athena-jdbc-client "#security-athena-lake-formation-jdbc-okta-tutorial-step-7-verify-access-through-athena-jdbc-client")
- [Conclusion](#security-athena-lake-formation-jdbc-okta-tutorial-conclusion "#security-athena-lake-formation-jdbc-okta-tutorial-conclusion")
- [Related resources](#security-athena-lake-formation-jdbc-okta-tutorial-related-resources "#security-athena-lake-formation-jdbc-okta-tutorial-related-resources")

## Step 1: Create an Okta account

This tutorial uses Okta as a SAML-based identity provider. If you do not already have
an Okta account, you can create a free one. An Okta account is required so that you can
create an Okta application for SAML authentication.

###### To create an Okta account

1. To use Okta, navigate to the [Okta developer sign up page](https://developer.okta.com/signup/ "https://developer.okta.com/signup/") and create a free Okta trial account.
   The Developer Edition Service is free of charge up to the limits specified by
   Okta at [developer.okta.com/pricing](https://developer.okta.com/pricing "https://developer.okta.com/pricing").
2. When you receive the activation email, activate your account.

An Okta domain name will be assigned to you. Save the domain name for
reference. Later, you use the domain name
(`<okta-idp-domain>`) in the JDBC string that
connects to Athena.

## Step 2: Add users and groups to Okta

In this step, you use the Okta console to perform the following tasks:

- Create two Okta users.
- Create two Okta groups.
- Add one Okta user to each Okta group.

###### To add users to Okta

1. After you activate your Okta account, log in as administrative user to the
   assigned Okta domain.
2. In the left navigation pane, choose **Directory**, and then
   choose **People**.
3. Choose **Add Person** to add a new user who will access Athena
   through the JDBC driver.

![Choose Add Person.](images/security-athena-lake-formation-jdbc-okta-tutorial-3.png) 4. In the **Add Person** dialog box, enter the required
information.

    * Enter values for **First name** and **Last
     name**. This tutorial uses
     `athena-okta-user`.
    * Enter a **Username** and **Primary
     email**. This tutorial uses
     `athena-okta-user@anycompany.com`.
    * For **Password**, choose **Set by
     admin**, and then provide a password. This tutorial clears
     the option for **User must change password on first
     login**; your security requirements may vary.

![Adding a user to the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-4.png) 5. Choose **Save and Add Another**. 6. Enter the information for another user. This example adds the business analyst
user `athena-ba-user@anycompany.com`.

![Adding a user to the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-4a.png) 7. Choose **Save**.

In the following procedure, you provide access for two Okta groups through the Athena
JDBC driver by adding a "Business Analysts" group and a "Developer" group.

###### To add Okta groups

1. In the Okta navigation pane, choose **Directory**, and then
   choose **Groups**.
2. On the **Groups** page, choose **Add
   Group**.

![Choose Add Group.](images/security-athena-lake-formation-jdbc-okta-tutorial-4c.png) 3. In the **Add Group** dialog box, enter the required
information.

    * For **Name**, enter
     `lf-business-analyst`.
    * For **Group Description**, enter
     `Business Analysts`.

![Adding an Okta group.](images/security-athena-lake-formation-jdbc-okta-tutorial-4d.png) 4. Choose **Add Group**. 5. On the **Groups** page, choose **Add Group**
again. This time you will enter information for the Developer group. 6. Enter the required information.

    * For **Name**, enter
     `lf-developer`.
    * For **Group Description**, enter
     `Developers`.

7. Choose **Add Group**.

Now that you have two users and two groups, you are ready to add a user to each
group.

###### To add users to groups

1. On the **Groups** page, choose the
   **lf-developer** group that you just created. You will add
   one of the Okta users that you created as a developer to this group.

![Choose lf-developer.](images/security-athena-lake-formation-jdbc-okta-tutorial-4f.png) 2. Choose **Manage People**.

![Choose Manage People.](images/security-athena-lake-formation-jdbc-okta-tutorial-4g.png) 3. From the **Not Members** list, choose
**athena-okta-user**.

![Choose a user to add to the members list.](images/security-athena-lake-formation-jdbc-okta-tutorial-4h.png)

The entry for the user moves from the **Not Members** list on the left to the **Members** list
on the right.

![Okta user added to an Okta group.](images/security-athena-lake-formation-jdbc-okta-tutorial-4i.png) 4. Choose **Save**. 5. Choose **Back to Group**, or choose
**Directory**, and then choose
**Groups**. 6. Choose the **lf-business-analyst** group. 7. Choose **Manage People**. 8. Add the **athena-ba-user** to the
**Members** list of the
**lf-business-analyst** group, and then choose
**Save**. 9. Choose **Back to Group**, or choose
**Directory**, **Groups**.

The **Groups** page now shows that each group has one Okta
user.

![One user has been added to each Okta group in the Okta console.](images/security-athena-lake-formation-jdbc-okta-tutorial-4j.png)

## Step 3: Set up an Okta application for SAML authentication

In this step, you use the Okta developer console to perform the following
tasks:

- Add a SAML application for use with AWS.
- Assign the application to the Okta user.
- Assign the application to an Okta group.
- Download the resulting identity provider metadata for later use with
  AWS.

###### To add an application for SAML authentication

1. In the Okta navigation pane, choose **Applications**,
   **Applications** so that you can configure an Okta
   application for SAML authentication to Athena.
2. Click **Browse App Catalog**.
3. In the search box, enter `Redshift`.
4. Choose **Amazon Web Services Redshift**. The Okta application in this
   tutorial uses the existing SAML integration for Amazon Redshift.

![Choose Amazon Web Services Redshift.](images/security-athena-lake-formation-jdbc-okta-tutorial-7.png) 5. On the **Amazon Web Services Redshift** page, choose
**Add** to create a SAML-based application for Amazon
Redshift.

![Choose Add to create a SAML-based application.](images/security-athena-lake-formation-jdbc-okta-tutorial-8.png) 6. For **Application label**, enter
`Athena-LakeFormation-Okta`, and then choose
**Done**.

![Enter a name for the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-9.png)

Now that you have created an Okta application, you can assign it to the users and
groups that you created.

###### To assign the application to users and groups

1. On the **Applications** page, choose the
   **Athena-LakeFormation-Okta** application.
2. On the **Assignments** tab, choose
   **Assign**, **Assign to People**.

![Choose Assign, Assign to People.](images/security-athena-lake-formation-jdbc-okta-tutorial-10.png) 3. In the **Assign Athena-LakeFormation-Okta to People** dialog
box, find the **athena-okta-user** user that you created
previously. 4. Choose **Assign** to assign the user to the
application.

![Choose Assign.](images/security-athena-lake-formation-jdbc-okta-tutorial-11.png) 5. Choose **Save and Go Back**. 6. Choose **Done**. 7. On the **Assignments** tab for the
**Athena-LakeFormation-Okta** application, choose
**Assign**, **Assign to Groups**. 8. For **lf-business-analyst**, choose
**Assign** to assign the
**Athena-LakeFormation-Okta** application to the
**lf-business-analyst** group, and then choose
**Done**.

![Assigning an Okta application to an Okta user group.](images/security-athena-lake-formation-jdbc-okta-tutorial-12b.png)

The group appears in the list of groups for the application.

![The Okta application is assigned to the Okta group.](images/security-athena-lake-formation-jdbc-okta-tutorial-12c.png)

Now you are ready to download the identity provider application metadata for use with
AWS.

###### To download the application metadata

1. Choose the Okta application **Sign On** tab, and then
   right-click **Identity Provider metadata**.

![Right-click Identity Provider metadata.](images/security-athena-lake-formation-jdbc-okta-tutorial-13.png) 2. Choose **Save Link As** to save the identity provider
metadata, which is in XML format, to a file. Give it a name that you recognize
(for example, `Athena-LakeFormation-idp-metadata.xml`).

![Saving the identity provider metadata.](images/security-athena-lake-formation-jdbc-okta-tutorial-14.png)

## Step 4: Create an AWS SAML Identity Provider and Lake Formation access IAM

role

In this step, you use the AWS Identity and Access Management (IAM) console to
perform the following tasks:

- Create an identity provider for AWS.
- Create an IAM role for Lake Formation access.
- Add the AmazonAthenaFullAccess managed policy to the role.
- Add a policy for Lake Formation and AWS Glue to the role.
- Add a policy for Athena query results to the role.

###### To create an AWS SAML identity provider

1. Sign in to the **Amazon Web Services account**
   **console** as **Amazon Web Services account
   administrator** and navigate to the **IAM**
   console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).
2. In the navigation pane, choose **Identity providers**, and
   then click **Add provider**.
3. On the **Configure provider** screen, enter the following
   information:
   - For **Provider type**, choose
     **SAML**.
   - For **Provider name**, enter
     `AthenaLakeFormationOkta`.
   - For **Metadata document**, use the **Choose
     file** option to upload the identity provider (IdP)
     metadata XML file that you downloaded.

4. Choose **Add provider**.

Next, you create an IAM role for AWS Lake Formation access. You add two inline policies to the
role. One policy provides permissions to access Lake Formation and the AWS Glue APIs. The other
policy provides access to Athena and the Athena query results location in Amazon S3.

###### To create an IAM role for AWS Lake Formation access

1. In the IAM console navigation pane, choose **Roles**, and
   then choose **Create role**.
2. On the **Create role** page, perform the following
   steps:

![Configuring an IAM role to use SAML 2.0.](images/security-athena-lake-formation-jdbc-okta-tutorial-20.png)

    1. For **Select type of trusted entity**, choose
     **SAML 2.0 Federation.**
    2. For **SAML provider**, select
     **AthenaLakeFormationOkta**.
    3. For **SAML provider**, select the option
     **Allow programmatic and AWS Management Console access**.
    4. Choose **Next: Permissions**.

3. On the **Attach Permissions policies** page, for
   **Filter policies**, enter
   `Athena`.
4. Select the **AmazonAthenaFullAccess** managed policy, and then
   choose **Next: Tags**.

![Attaching the AmazonAthenaFullAccess managed policy to the IAM role.](images/security-athena-lake-formation-jdbc-okta-tutorial-21.png) 5. On the **Add tags** page, choose **Next:
Review**. 6. On the **Review** page, for **Role name**,
enter a name for the role (for example,
`Athena-LakeFormation-OktaRole`), and then choose
**Create role**.

![Enter a name for the IAM role.](images/security-athena-lake-formation-jdbc-okta-tutorial-22.png)

Next, you add inline policies that allow access to Lake Formation, AWS Glue APIs, and Athena query
results in Amazon S3.

Whenever you use IAM policies, make sure that you follow IAM best practices. For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

###### To add an inline policy to the role for Lake Formation and AWS Glue

1. From the list of roles in the IAM console, choose the newly created
   `Athena-LakeFormation-OktaRole`.
2. On the **Summary** page for the role, on the
   **Permissions** tab, choose **Add inline
   policy**.
3. On the **Create policy** page, choose
   **JSON**.
4. Add an inline policy like the following that provides access to Lake Formation and the
   AWS Glue APIs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "lakeformation:GetDataAccess",
 "glue:GetTable",
 "glue:GetTables",
 "glue:GetDatabase",
 "glue:GetDatabases",
 "glue:CreateDatabase",
 "glue:GetUserDefinedFunction",
 "glue:GetUserDefinedFunctions"
 ],
 "Resource": "*"
 }
}`

```

5. Choose **Review policy**.
6. For **Name**, enter a name for the policy (for example,
   `LakeFormationGlueInlinePolicy`).
7. Choose **Create policy**.

###### To add an inline policy to the role for the Athena query results location

1. On the **Summary** page for the
   `Athena-LakeFormation-OktaRole` role, on the
   **Permissions** tab, choose **Add inline
   policy**.
2. On the **Create policy** page, choose
   **JSON**.
3. Add an inline policy like the following that allows the role access to the
   Athena query results location. Replace the
   `<athena-query-results-bucket>` placeholders
   in the example with the name of your Amazon S3 bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AthenaQueryResultsPermissionsForS3",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket",
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`<athena-query-results-bucket>`",
 "arn:aws:s3:::`<athena-query-results-bucket>`/*"
 ]
 }
 ]
}`

```

4. Choose **Review policy**.
5. For **Name**, enter a name for the policy (for example,
   `AthenaQueryResultsInlinePolicy`).
6. Choose **Create policy**.

Next, you copy the ARN of the Lake Formation access role and the ARN of the SAML provider that
you created. These are required when you configure the Okta SAML application in the next
section of the tutorial.

###### To copy the role ARN and SAML identity provider ARN

1. In the IAM console, on the **Summary** page for the
   `Athena-LakeFormation-OktaRole` role, choose the **Copy to
   clipboard** icon next to **Role ARN**. The ARN has
   the following format:

```
arn:aws:iam::`<account-id>`:role/Athena-LakeFormation-OktaRole
```

2. Save the full ARN securely for later reference.
3. In the IAM console navigation pane, choose **Identity
   providers**.
4. Choose the **AthenaLakeFormationOkta** provider.
5. On the **Summary** page, choose the **Copy to
   clipboard** icon next to **Provider ARN**. The ARN
   should look like the following:

```
arn:aws:iam::`<account-id>`:saml-provider/AthenaLakeFormationOkta
```

6. Save the full ARN securely for later reference.

## Step 5: Add the IAM role and SAML Identity Provider to the Okta

application

In this step, you return to the Okta developer console and perform the following
tasks:

- Add user and group Lake Formation URL attributes to the Okta application.
- Add the ARN for the identity provider and the ARN for the IAM role to the
  Okta application.
- Copy the Okta application ID. The Okta application ID is required in the JDBC
  profile that connects to Athena.

###### To add user and group Lake Formation URL attributes to the Okta application

1. Sign into the Okta developer console.
2. Choose the **Applications** tab, and then choose the
   `Athena-LakeFormation-Okta` application.
3. Choose on the **Sign On** tab for the application, and then
   choose **Edit**.

![Edit the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-24.png) 4. Choose **Attributes (optional)** to expand it.

![Adding a user Lake Formation URL attribute to the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-25.png) 5. For **Attribute Statements (optional)**, add the following
attribute:

    * For **Name**, enter
     `https://lakeformation.amazon.com/SAML/Attributes/Username`.
    * For **Value**, enter
     `user.login`

6. Under **Group Attribute Statements (optional)**, add the
   following attribute:
   - For **Name**, enter
     `https://lakeformation.amazon.com/SAML/Attributes/Groups`.
   - For **Name format**, enter
     `Basic`
   - For **Filter**, choose **Matches
     regex**, and then enter `.*` in the
     filter box.

![Adding a group Lake Formation URL attribute to the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-25a.png) 7. Scroll down to the **Advanced Sign-On Settings** section,
where you will add the identity provider and IAM Role ARNs to the Okta
application.

###### To add the ARNs for the identity provider and IAM role to the Okta

application

1. For **Idp ARN and Role ARN**, enter the AWS identity
   provider ARN and role ARN as comma separated values in the format
   `<saml-arn>`,`<role-arn>`.
   The combined string should look like the following:

```
arn:aws:iam::`<account-id>`:saml-provider/AthenaLakeFormationOkta,arn:aws:iam::`<account-id>`:role/Athena-LakeFormation-OktaRole
```

![Entering the identity provider ARN and IAM role ARN in the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-26.png) 2. Choose **Save**.

Next, you copy the Okta application ID. You will require this later for the JDBC
string that connects to Athena.

###### To find and copy the Okta application ID

1. Choose the **General** tab of the Okta application.

![Choose the General tab of the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-27.png) 2. Scroll down to the **App Embed Link** section. 3. From **Embed Link**, copy and securely save the Okta
application ID portion of the URL. The Okta application ID is the part of the
URL after `amazon_aws_redshift/` but before the next forward slash.
For example, if the URL contains `amazon_aws_redshift/aaa/bbb`, the
application ID is `aaa`.

![Copy the ID of the Okta application.](images/security-athena-lake-formation-jdbc-okta-tutorial-28.png)

###### Note

The embed link cannot be used to log directly into the Athena console to view
databases. The Lake Formation permissions for SAML users and groups are recognized only when
you use the JDBC or ODBC driver to submit queries to Athena. To view the databases,
you can use the SQL Workbench/J tool, which uses the JDBC driver to connect to
Athena. The SQL Workbench/J tool is covered in [Step 7: Verify access through the Athena JDBC client](#security-athena-lake-formation-jdbc-okta-tutorial-step-7-verify-access-through-athena-jdbc-client "#security-athena-lake-formation-jdbc-okta-tutorial-step-7-verify-access-through-athena-jdbc-client").

## Step 6: Grant user and group permissions through AWS Lake Formation

In this step, you use the Lake Formation console to grant permissions on a table to the SAML
user and group. You perform the following tasks:

- Specify the ARN of the Okta SAML user and associated user permissions on the
  table.
- Specify the ARN of the Okta SAML group and associated group permissions on the
  table.
- Verify the permissions that you granted.

###### To grant permissions in Lake Formation for the Okta user

1. Sign in as data lake administrator to the AWS Management Console.
2. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
3. From the navigation pane, choose **Tables**, and then select
   the table that you want to grant permissions for. This tutorial uses the
   `nyctaxi` table from the `tripdb` database.

![Choose the table that you want to grant permissions for.](images/security-athena-lake-formation-jdbc-okta-tutorial-29.png) 4. From **Actions**, choose **Grant**.

![Choose Grant.](images/security-athena-lake-formation-jdbc-okta-tutorial-30.png) 5. In the **Grant permissions** dialog, enter the following
information:

    1. Under **SAML and Amazon Quick Suite users and groups**, enter
     the Okta SAML user ARN in the following format:



    ```
    arn:aws:iam::`<account-id>`:saml-provider/AthenaLakeFormationOkta:user/`<athena-okta-user>`@`<anycompany.com>`
    ```
    2. For **Columns**, for **Choose filter
     type**, and optionally choose **Include
     columns** or **Exclude columns**.
    3. Use the **Choose one or more columns** dropdown under
     the filter to specify the columns that you want to include or exclude
     for or from the user.
    4. For **Table permissions**, choose
     **Select**. This tutorial grants only the
     `SELECT` permission; your requirements may vary.



    ![Granting table and column-level permissions to an Okta user.](images/security-athena-lake-formation-jdbc-okta-tutorial-31.png)

6. Choose **Grant**.

Now you perform similar steps for the Okta group.

###### To grant permissions in Lake Formation for the Okta group

1. On the **Tables** page of the Lake Formation console, make sure that
   the **nyctaxi** table is still selected.
2. From **Actions**, choose **Grant**.
3. In the **Grant permissions** dialog, enter the following
   information:
   1. Under **SAML and Amazon Quick Suite users and groups**, enter
      the Okta SAML group ARN in the following format:

   ```
   arn:aws:iam::`<account-id>`:saml-provider/AthenaLakeFormationOkta:group/lf-business-analyst
   ```

   2. For **Columns**, **Choose filter
      type**, choose **Include columns**.
   3. For **Choose one or more columns**, choose the first
      three columns of the table.
   4. For **Table permissions**, choose the specific access
      permissions to grant. This tutorial grants only the `SELECT`
      permission; your requirements may vary.

   ![Granting table permissions to an Okta group.](images/security-athena-lake-formation-jdbc-okta-tutorial-31b.png)

4. Choose **Grant**.
5. To verify the permissions that you granted, choose
   **Actions**, **View permissions**.

![Choose View permissions to verify the permissions that were granted.](images/security-athena-lake-formation-jdbc-okta-tutorial-32.png)

The **Data permissions** page for the `nyctaxi`
table shows the permissions for **athena-okta-user** and the
**lf-business-analyst** group.

![Viewing the permissions that were granted to the Okta user and group.](images/security-athena-lake-formation-jdbc-okta-tutorial-33.png)

## Step 7: Verify access through the Athena JDBC client

Now you are ready to use a JDBC client to perform a test connection to Athena as the
Okta SAML user.

In this section, you perform the following tasks:

- Prepare the test client – Download the Athena JDBC driver, install SQL
  Workbench, and add the driver to Workbench. This tutorial uses SQL Workbench to
  access Athena through Okta authentication and to verify Lake Formation permissions.
- In SQL Workbench:
  - Create a connection for the Athena Okta user.
  - Run test queries as the Athena Okta user.
  - Create and test a connection for the business analyst user.

- In the Okta console, add the business analyst user to the developer
  group.
- In the Lake Formation console, configure table permissions for the developer
  group.
- In SQL Workbench, run test queries as the business analyst user and verify how
  the change in permissions affects the results.

###### To prepare the test client

1. Download and extract the Lake Formation compatible Athena JDBC driver (2.0.14 or later
   version) from [Connect to Amazon Athena with JDBC](connect-with-jdbc.md "connect-with-jdbc.md").
2. Download and install the free [SQL Workbench/J](https://www.sql-workbench.eu/index.html "https://www.sql-workbench.eu/index.html") SQL
   query tool, available under a modified Apache 2.0 license.
3. In SQL Workbench, choose **File**, and then choose
   **Manage Drivers**.

![Choose Manage Drivers.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-1.png) 4. In the **Manage Drivers** dialog box, perform the following
steps:

    1. Choose the new driver icon.
    2. For **Name**, enter
     `Athena`.
    3. For **Library**, browse to and choose the Simba Athena
     JDBC `.jar` file that you just downloaded.
    4. Choose **OK**.



    ![Adding the Athena JDBC driver to SQL Workbench.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-2.png)

You are now ready to create and test a connection for the Athena Okta user.

###### To create a connection for the Okta user

1. Choose **File**, **Connect window**.

![Choose Connect window.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-3.png) 2. In the **Connection profile** dialog box, create a connection
by entering the following information:

    * In the name box, enter
     `Athena_Okta_User_Connection`.
    * For **Driver**, choose the Simba Athena JDBC
     Driver.
    * For **URL**, do one of the following:




    	+ To use a connection URL, enter a single-line connection
    	 string. The following example adds line breaks for
    	 readability.



    	```
    	jdbc:awsathena://AwsRegion=`region-id`;
    	S3OutputLocation=s3://amzn-s3-demo-bucket/athena_results;
    	AwsCredentialsProviderClass=com.simba.athena.iamsupport.plugin.OktaCredentialsProvider;
    	user=`athena-okta-user`@`anycompany.com`;
    	password=`password`;
    	idp_host=`okta-idp-domain`;
    	App_ID=`okta-app-id`;
    	SSL_Insecure=true;
    	LakeFormationEnabled=true;
    	```
    	+ To use an AWS profile-based URL, perform the following
    	 steps:




    		1. Configure an [AWS profile](../../../cli/latest/userguide/cli-configure-profiles.md "../../../cli/latest/userguide/cli-configure-profiles.md") that has an AWS credentials
    		 file like the following example.



    		```
    		[`athena_lf_dev`]
    		plugin_name=com.simba.athena.iamsupport.plugin.OktaCredentialsProvider
    		idp_host=`okta-idp-domain`app_id=`okta-app-id`
    		uid=`athena-okta-user`@`anycompany.com`pwd=`password`
    		```
    		2. For **URL**, enter a single-line
    		 connection string like the following example. The
    		 example adds line breaks for readability.



    		```
    		jdbc:awsathena://AwsRegion=`region-id`;
    		S3OutputLocation=s3://amzn-s3-demo-bucket/athena_results;
    		profile=`athena_lf_dev`;
    		SSL_Insecure=true;
    		LakeFormationEnabled=true;
    		```
    Note that these examples are basic representations of the URL needed
     to connect to Athena. For the full list of parameters supported in the
     URL, refer to the [JDBC documentation](connect-with-jdbc.md "connect-with-jdbc.md").

The following image shows a SQL Workbench connection profile that uses a
connection URL.

![A connection profile in SQL Workbench.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-4.png)

Now that you have established a connection for the Okta user, you can test it by
retrieving some data.

###### To test the connection for the Okta user

1. Choose **Test**, and then verify that the connection
   succeeds.
2. From the SQL Workbench **Statement** window, run the
   following SQL `DESCRIBE` command. Verify that all columns are
   displayed.

```
DESCRIBE "tripdb"."nyctaxi"
```

![All columns displayed.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-5.png) 3. From the SQL Workbench **Statement** window, run the
following SQL `SELECT` command. Verify that all columns are
displayed.

```
SELECT * FROM tripdb.nyctaxi LIMIT 5
```

![Verify that all columns are displayed.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-6.png)

Next, you verify that the **athena-ba-user**, as a member of the
**lf-business-analyst** group, has access to only the first three
columns of the table that you specified earlier in Lake Formation.

###### To verify access for the **athena-ba-user**

1. In SQL Workbench, in the **Connection profile** dialog box,
   create another connection profile.
   - For the connection profile name, enter `Athena_Okta_Group_Connection`.
   - For **Driver**, choose the Simba Athena JDBC
     driver.
   - For **URL**, do one of the following:
     - To use a connection URL, enter a single-line connection
       string. The following example adds line breaks for
       readability.

     ```
     jdbc:awsathena://AwsRegion=`region-id`;
     S3OutputLocation=s3://amzn-s3-demo-bucket/athena_results;
     AwsCredentialsProviderClass=com.simba.athena.iamsupport.plugin.OktaCredentialsProvider;
     user=`athena-ba-user`@`anycompany.com`;
     password=`password`;
     idp_host=`okta-idp-domain`;
     App_ID=`okta-application-id`;
     SSL_Insecure=true;
     LakeFormationEnabled=true;
     ```

     - To use an AWS profile-based URL, perform the following
       steps:
       1. Configure an AWS profile that has a credentials file
          like the following example.

       ```
       [`athena_lf_ba`]
       plugin_name=com.simba.athena.iamsupport.plugin.OktaCredentialsProvider
       idp_host=`okta-idp-domain`
       app_id=`okta-application-id`
       uid=`athena-ba-user`@`anycompany.com`pwd=`password`
       ```

       2. For **URL**, enter a single-line
          connection string like the following. The example adds
          line breaks for readability.

       ```
       jdbc:awsathena://AwsRegion=`region-id`;
       S3OutputLocation=s3://amzn-s3-demo-bucket/athena_results;
       profile=`athena_lf_ba`;
       SSL_Insecure=true;
       LakeFormationEnabled=true;
       ```

2. Choose **Test** to confirm that the connection is
   successful.
3. From the **SQL Statement** window, run the same
   `DESCRIBE` and `SELECT` SQL commands that you did
   before and examine the results.

Because **athena-ba-user** is a member of the
**lf-business-analyst** group, only the first three columns
that you specified in the Lake Formation console are returned.

![Only the first three columns are returned.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-7.png)

![Data from the first three columns.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-8.png)

Next, you return to the Okta console to add the `athena-ba-user` to the
`lf-developer` Okta group.

###### To add the athena-ba-user to the lf-developer group

1. Sign in to the Okta console as an administrative user of the assigned Okta
   domain.
2. Choose **Directory**, and then choose
   **Groups**.
3. On the Groups page, choose the **lf-developer** group.

![Choose the lf-developer group.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-9.png) 4. Choose **Manage People**. 5. From the **Not Members** list, choose the
**athena-ba-user** to add it to the **lf-developer
group**. 6. Choose **Save**.

Now you return to the Lake Formation console to configure table permissions for the
**lf-developer** group.

###### To configure table permissions for the lf-developer-group

1. Log into the Lake Formation console as Data Lake administrator.
2. In the navigation pane, choose **Tables**.
3. Select the **nyctaxi** table.
4. Choose **Actions**, **Grant**.
5. In the **Grant Permissions** dialog, enter the following
   information:
   - For **SAML and Amazon Quick Suite users and groups**, enter the
     Okta SAML lf-developer group ARN in the following format:
   - For **Columns**, **Choose filter
     type**, choose **Include columns**.
   - Choose the **trip_type** column.
   - For **Table permissions**, choose
     **SELECT**.

6. Choose **Grant**.

Now you can use SQL Workbench to verify the change in permissions for the
**lf-developer** group. The change should be reflected in the data
available to **athena-ba-user**, who is now a member of the
**lf-developer** group.

###### To verify the change in permissions for athena-ba-user

1. Close the SQL Workbench program, and then re-open it.
2. Connect to the profile for **athena-ba-user**.
3. From the **Statement** window, issue the same SQL statements
   that you ran previously:

This time, the **trip_type** column is displayed.

![The fourth column is available for query.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-10.png)

Because **athena-ba-user** is now a member of both the
**lf-developer** and
**lf-business-analyst** groups, the combination of Lake Formation
permissions for those groups determines the columns that are returned.

![The fourth column in the data results.](images/security-athena-lake-formation-jdbc-okta-tutorial-verify-access-11.png)

## Conclusion

In this tutorial you configured Athena integration with AWS Lake Formation using Okta as the SAML
provider. You used Lake Formation and IAM to control the resources that are available to the
SAML user in your data lake AWS Glue Data Catalog.

## Related resources

For related information, see the following resources.

- [Connect to Amazon Athena with JDBC](connect-with-jdbc.md "connect-with-jdbc.md")
- [Enable federated access to the Athena API](access-federation-saml.md "access-federation-saml.md")
- [AWS Lake Formation Developer Guide](../../../lake-formation/latest/dg.md "../../../lake-formation/latest/dg.md")
- [Granting and
  revoking Data Catalog permissions](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md") in the
  _AWS Lake Formation Developer Guide_.
- [Identity providers and
  federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md") in the _IAM User Guide_.
- [Creating IAM
  SAML identity providers](../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md "../../../IAM/latest/UserGuide/id_roles_providers_create_saml.md") in the
  _IAM User Guide_.
- [Enabling federation to AWS using Windows Active Directory, ADFS, and SAML
  2.0](https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/ "https://aws.amazon.com/blogs/security/enabling-federation-to-aws-using-windows-active-directory-adfs-and-saml-2-0/") on the _AWS Security Blog_.
