# Creating an Amazon Q Business

application using IAM federation through Microsoft Entra ID

As the first step toward creating a generative artificial intelligence (AI) assistant,
configure your external identity provider and connect it to AWS Identity and Access Management.

When you create an application environment, you can also choose to create an Amazon Q Business web experience, which your end users can use to chat with your
application. You can add subscriptions for end users who log in to your Amazon Q Business web experience using Microsoft Entra ID. Any user
logging in to your web experience is automatically provisioned with a subscription of a
type that you select for them.

###### Note

As of Oct 31, 2024, once you have created a new Amazon Q Business
application environment, the default web experience will allow users to interact directly with the
LLM to get answers from its general knowledge or uploaded file content, even if the Admin has not yet connected any enterprise data sources.

For existing application environments, the _Allow direct access to LLM_
setting will remain as previously configured. For new application environments, the
_Allow direct access to LLM_ setting will be enabled by default,
though Admins can still disable this if desired.

To learn more about identity federation using AWS Identity and Access Management, see the following
topics:

- [Identity federation
  in AWS](https://aws.amazon.com/identity/federation/ "https://aws.amazon.com/identity/federation/") on the _AWS website_.
- [Providing access to externally authenticated users
  (identity federation)](../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_federated-users.md") in the _IAM User
  Guide_.
  The following steps show how to integrate Amazon Q Business with
  Microsoft Entra ID. Integrating Amazon Q Business with
  Microsoft Entra ID requires that you switch between tasks on the
  Amazon Q Business console and the Microsoft Entra ID admin
  portal.

###### Topics

- [Prerequisites](#create-iam-app-entraid-prereqs "#create-iam-app-entraid-prereqs")
- [Step 1: Create and configure a
  Microsoft Entra ID application](#create-iam-app-entraid-1 "#create-iam-app-entraid-1")
- [Step 2: Create an IAM identity
  provider](#create-iam-app-entraid-2 "#create-iam-app-entraid-2")
- [Step 3: Update your Microsoft
  Entra ID application with the IAM role ARN](#create-iam-app-entraid-3 "#create-iam-app-entraid-3")
- [Step 4: Create an Amazon Q Business
  application](#create-iam-app-entraid-4 "#create-iam-app-entraid-4")
- [Step 5: Update your Microsoft
  Entra ID application with the web experience URL](#create-iam-app-entraid-5 "#create-iam-app-entraid-5")
- [Troubleshooting Microsoft
  Entra ID integration](#create-iam-app-entraid-troubleshooting "#create-iam-app-entraid-troubleshooting")

## Prerequisites

Before you start to integrate Amazon Q Business with Microsoft Entra
ID, make sure that you have:

- Created a Microsoft Entra ID account and added at least one
  user with a valid email address. For more information, see [Add
  users in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/add-users "https://learn.microsoft.com/en-us/entra/fundamentals/add-users") on the
  _Microsoft Learn website_.
- Appropriate permissions in Microsoft Entra ID to create and
  configure enterprise applications. Review the [Microsoft Entra ID built-in roles
  documentation](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference "https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference") to ensure you have the required permissions.
  Typically, you need the `Application Administrator` or
  `Cloud Application Administrator` role.
- Created IAM policies containing the permissions outlined in [IAM role for an Amazon Q Business web
  experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md") to:

      + Allow an Amazon Q Business web experience to invoke the API
       operations required to integrate your application
      + **(If you're creating a Amazon Q Business default web experience)** Allow Amazon Q Business to access the resources it needs to create a web
       experience

  You will need these roles to complete creating your Amazon Q Business IAM federated application.

###### Note

To create a new policy, follow the instructions in [Creating
IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the AWS Identity and Access Management User Guide.

- (Optional) Checked [how subscriptions work](tiers.md#managing-sub-tiers-iam "tiers.md#managing-sub-tiers-iam") for Amazon Q Business applications using IAM Federation.

## Step 1: Create and configure a

Microsoft Entra ID application

This procedure outlines how to create and configure a Microsoft Entra
ID instance for an Amazon Q Business application using a built-in
web experience and a custom Amazon Q Business application client you develop
using Amazon Q Business APIs.

###### Important

Amazon Q Business supports Microsoft Entra ID with SAML
2.0 only. OIDC is not supported for Microsoft Entra ID.

###### To create a Microsoft Entra ID instance

1. Sign into the Microsoft Entra admin center in your
   Microsoft Azure Portal.
2. In the left navigation pane, choose **Enterprise
   apps**.
3. From **All applications**, choose **+ New
   application** from the top navigation pane.
4. On the **Browse Microsoft Entra gallery** page, choose
   **Amazon Web Services (AWS)**, and then select
   **AWS Single-Account Access**.
5. Then, in the **AWS Single-Account Access** menu that
   opens, in **Name**, add a name for your application. For
   example: `QBusinessSAMLProvider`. Then, select
   **Create**.
6. When the application is ready, on the **Overview** page
   of your application, from **Getting Started** choose
   **Single sign-on**.
7. On the **Single sign-on** page, for **Select a
   single sign-on method**, select
   **SAML**.

Selecting SAML configures the application to use Security Assertion Markup
Language (SAML) 2.0 for authentication, which is the protocol required for
IAM federation with AWS services like Amazon Q Business. 8. On the **Set up Single Sign-On with SAML** page, for
**Basic SAML Configuration**, choose
**Edit**, and then configure the following
settings:

    * For **Identifier (Entity ID)**, enter your web
     application endpoint.


    If you're creating an Amazon Q Business application
     generated web experience endpoint URL, this value be the Amazon Q Business generated web experience URL with
     `saml` added at the end. For example,
     `https://abcdefgh.qbusiness.us-east-1.on.aws/saml`.
     The web experience URL will be generated by Amazon Q Business
     after you finish creating an Amazon Q Business application.
     For now, enter a placeholder URL. For example:
     `https://sampleurl.com`. You will
     update this at the end of your Amazon Q Business application
     creation process.
    * For **Reply URL (Assertion Consumer Service
     URL)** – Enter your web application
     endpoint.


    If you're creating an Amazon Q Business application
     generated web experience endpoint URL, this value be the Amazon Q Business generated web experience URL with
     `saml` added at the end. For example,
     `https://abcdefgh.qbusiness.us-east-1.on.aws/saml`.
     The web experience URL will be generated by Amazon Q Business
     after you finish creating an Amazon Q Business application.
     For now, enter a placeholder URL. For example:
     `https://sampleurl.com`. You will
     update this at the end of your Amazon Q Business application
     creation process.
    * Select **Save**.

9. In the **SAML Certificates** section, download the
   **Federation Metadata XML** file. You will need this
   file when you create an identity provider in IAM.

The **Federation Metadata XML** file contains all the
necessary SAML metadata that IAM needs to establish trust with your
Microsoft Entra ID application, including certificate
information, entity IDs, and endpoint URLs. This file will be uploaded to
IAM when creating the identity provider in the next step.

You're now ready to move on to configuring AWS Identity and Access Management on the AWS Management Console.

## Step 2: Create an IAM identity

provider

After you create and configure your Microsoft Entra ID application,
create an IAM identity provider.

**To connect Microsoft Entra ID to AWS Identity and Access Management**

1. Sign in to the AWS Management Console and open the AWS Identity and Access Management.
2. In the navigation pane, choose **Identity providers**,
   and then choose **Add provider**.
3. For **Configure provider**, do the following:
   1. For **Provider type**, choose
      **SAML**.
   2. For **Provider name**, enter a name for your
      identity provider (for example,
      `EntraIDProvider`).
   3. For **Metadata document**, choose
      **Choose file** and upload the
      **Federation Metadata XML** file that you
      downloaded from Microsoft Entra ID.
   4. Choose **Add provider**.

4. On the **Identity provider** summary page, from
   **Provider**, select the provider you just added do the
   following:
   - From **Summary** copy the
     **ARN** and save the value. You will need it
     when you add your IAM trust policy and when you connect your
     AWS Identity and Access Management identity provider to your Microsoft Entra
     ID instance. The format of the ARN is:
     `arn:aws:iam::`aws-account-id`:saml-provider/`assigned-iam-idp-name``.
   - Then, select **Assign role** to create an IAM
     role with the necessary permissions for your identity
     provider.

5. In **Assign role**, for **Role options**
   select **Create a new role**.
6. Then, on the **Selected trusted entity** page, do the
   following:
   - For **Trusted entity type** select
     **Custom trust policy**.
   - In **Custom trust policy**, add the following
     trust policy, replacing the value for `AWS IAM
Identity Provider ARN` with the identity provider
     ARN you copied in the previous step:

   ```


   ```

   ###### Note

   Leave the `SAML:aud` field as
   `https://sampleurl.com` for now.
   You'll come back to update it with your Amazon Q web experience
   URL as part of Step 5 of this tutorial.

   Select **Next**.

7. On the **Add permissions** page, for
   **Permissions policies** choose an IAM policy with
   the required permissions and then select **Next**.

For the policy permissions required, see [IAM role for an Amazon Q Business web
experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md"). Optionally, select
**AdministratorAccess**.

###### Note

To create a new policy, follow the instructions in [Creating
IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the AWS Identity and Access Management User Guide. 8. In the **Name, review, and create** page, add a
**Role name**, and optional role description and tags
to identify your IAM role. Then, select **Create
role**. 9. From the **Roles** page, select the IAM role you just
created. Then, from the role summary page, do the following:

    * Copy the role **ARN** and save it. You will need
     this information to connect your AWS Identity and Access Management identity provider
     instance to Microsoft Entra ID. The format of the ARN
     will be like this:
     `arn:aws:iam::111122223333:role/sample-role`.

You are now ready to return to Microsoft Entra ID to complete the
process of establishing a trust relationship between AWS Identity and Access Management and Microsoft
Entra ID.

## Step 3: Update your Microsoft

Entra ID application with the IAM role ARN

In this step, you complete configuring the trust relationship between AWS Identity and Access Management
and Microsoft Entra ID.

**To update your Microsoft Entra ID
application**

1. Return to the Microsoft Azure Portal and navigate to the
   application you created.
2. In the left navigation pane, choose **Single sign-on**,
   then choose **Manage**. Then, choose **Single
   sign-on**.
3. In **Single sign-on** section, choose
   **Attributes & Claims**, and select
   **Edit**.
4. From **Required claim**, select **Unique User
   Identifier (Name ID)**.
5. In **Manage claim**, do the following:
   - For **Name identifier format**, choose
     **Persistent**.
   - For **Source attribute**, choose
     **user.objectid**.
   - Select **Save**.

6. Then, from **Attributes & Claims** select
   **Add new claim**, and in **Manage
   claim**, do the following:
   - For **Name** – Type
     **PrincipalTag:Email**.
   - For **Namespace**, type
     **https://aws.amazon.com/SAML/Attributes**.
   - Leave **Source** value as
     **Attribute**.
   - For **Source attribute**, choose
     **user.mail**.
   - Select **Save**.

7. Then, from your application menu, choose **Manage** and
   then select **Security**.
8. From **Security**, select
   **Permissions**.
9. In **Permissions**, choose **Application
   registration**.
10. From **Application registration** from the left
    navigation menu, select **App roles**, and then select
    **Create app role**. In the **Create app
    role** dialog box that opens, and do the following:
    - For **Display name**, add a name for your
      role.
    - For **Allowed member types**, choose
      **Both (Users/Groups + Applications)**.
    - For the **Value** field, add a mapping to the
      attribute in the following format using the values you copied from
      Step 2 of this section: `IAMroleArn,IAMidpArn`. For
      example:
      `arn:aws:iam::111122223333:role/sample-role,arn:aws:iam::111122223333:saml-provider/entra-idp`.
    - For **Description**, add a description for your
      app role.
    - Select **Apply**.

11. Then, in the left navigation pane of your application, choose
    **Users and groups**, and do the following
    steps.
    1. Choose **+ Add user/group** and select the users
       or groups you want to assign to your application, and then choose
       **Select**.
    2. Choose **Assign**.

12. Refresh your page. Then, from the left navigation pane of your
    application, choose **Manage**. Then, select **API
    Permissions**, and **Add a
    permission**.
13. In **Add a permission**. Then, on the **Request
    API permissions** section, do the following:
    1. Choose **APIs my organization uses** and select
       and open the Entra ID application you created.
    2. For **What type pf permissions does your application
       require?** – Choose **Application
       permissions**.
    3. In **Permissions** – Choose the app role
       permissions you created in the last step.
    4. Select **Add permissions**.

14. Then, from **Manage**, select
    **Properties** and copy and save the **User
    access URL** value for your application.

You will need this value to create your Amazon Q application.

Your Entra ID setup is complete. You're now ready to begin creating
your Amazon Q Business application.

## Step 4: Create an Amazon Q Business

application

After you configure Microsoft Entra ID and IAM, create an Amazon Q Business application.

**To create an Amazon Q Business
application**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. In the navigation pane, choose **Applications**, and then
   choose **Create application**.
3. On the **Create application** page, for **What
   kind of application do you want to create?**, enter the
   following information for your Amazon Q Business application:
   1. **Application name** – A name for your
      Amazon Q Business application environment for easy identification.
      This name is only visible in the AWS Management Console. The name can include
      hyphens (-), but not spaces, and can have a maximum of 1,000
      alphanumeric characters. Amazon Q Business auto-generates an
      application name for you, unless you choose to enter a custom
      name.
   2. For **User access**, choose
      **Authenticated access**.
   3. For **Outcome**, choose **Web
      experience**.

4. For **Access management method**, choose **AWS
   IAM Identity Provider**.

Then, for **Choose an identity provider type**, choose
**Security Assertion Markup Language (SAML)**.

For **SAML**, do the following:

    1. For **Select Identity Provider**, choose the
     identity provider you've created in AWS Identity and Access Management to use with your
     Amazon Q Business application.
    2. For **Authentication URL**, provide the
     authentication URL for Entra ID. Your authentication
     URL must be of the following format:
     `https://myapps.microsoft.com/signin/`app_name`/`user_access_url_suffix``.


    For the `user_access_url_suffix`, copy the value of
     everything after `https://myapps.microsoft.com/signin/`
     from the **User access URL** you copied and saved
     in the last step.


    When end users navigate to the web experience URL they're
     redirected to this authentication URL where they provide their login
     ID and password. After successful authentication, they're redirected
     back to the web experience URL to begin chatting.

5. For **Default subscription settings**, for
   **Subscription tier**, choose between **Q
   Business Pro** and **Q Business Lite**. Any
   user logging in to your web experience will be assigned this subscription
   type by default.
6. For **Application details** – Amazon Q Business chooses the following configuration settings for your
   application by default:
   1. For **Application service access** –
      Amazon Q Business will create a new service-linked role
      for your application.
   2. **Encryption** – Amazon Q Business
      will create an AWS owned AWS KMS key to encrypt your data.
   3. For **Web experience service access** – If
      you've chosen to create a web experience, Amazon Q Business
      requires you select an existing role to allow end users to log in to
      a Amazon Q Business web experience.

7. (Optional) To customize **Application details**, expand
   the **Application details section**, and then do the
   following:
   1. In **Application service access**, for
      **Choose a method to authorize Amazon Q Business**, choose from the following options:
      1. **Create and use a new service-linked role
         (SLR)** – Create and use a new Amazon Q Business-managed IAM role to allow it to access
         the AWS resources it needs to create your
         application.
      2. **Create and use a new service role
         (SR)** – Create and use a new IAM role for Amazon Q Business to allow it
         to access the AWS resources it needs to
         create your application.

      For **Service role name** – A name
      for the service (IAM) role you created for
      easy identification on the console. 3. **Use an existing service role (SR)/service-linked
      role (SLR)** – Use an existing service
      role or service-linked IAM role to allow
      Amazon Q Business to access the AWS
      resources it needs to create your application.

      ###### Note

      For more information about example service roles, see
      [IAM role for an Amazon Q Business application](create-application-iam-role.md "create-application-iam-role.md"). For
      information on service-linked roles, including to manage
      them, see [Using service-linked
      roles](../business-use-dg/using-service-linked-roles.md "../business-use-dg/using-service-linked-roles.md").

   2. For **Encryption** – Amazon Q Business encrypts your data by default using AWS managed AWS KMS keys. To customize your encryption settings, select
      **Customize encryption settings (advanced)**.
      Then, you can choose to use an existing AWS KMS key or
      create a new one.
   3. In **Web experience service access**, enter the
      following information:
      1. For **Choose a method to authorize Amazon Q Business** – A service access
         role assumed by end users when they sign in to your web
         experience that grants them permission to start and manage
         conversations Amazon Q Business. Choose the IAM role
         you created in Step 2.

8. To start creating your application, choose
   **Create**.

###### Note

If you're creating a web experience, you can also choose to create
your application and [view your web experience](customizing-web-experience-iam.md "customizing-web-experience-iam.md") by selecting
**Create and open web experience**. 9. Once the application creation process completes, the web experience
settings section on your application summary page will display your Amazon Q Business web experience URL. Copy the URL to a file and add
`/saml` at the end of the web experience URL. 10. Then, open IAM on the AWS Management Console, and do the following:

    1. From the left navigation menu, for **Access
     management**, choose **Roles**, and
     then choose the IAM role you created in Step 2 of this tutorial.
    2. From the role summary page, select **Trust
     relationships**, and then select **Edit trust
     policy**.
    3. Replace the placeholder
     ``{{https://sampleurl.com}}``
     with the Amazon Q web application URL you copied in the previous
     step.
    4. Select **Update policy**.

You've finished configuring your Amazon Q Business application. You're now
ready to return to Entra ID to make the final changes needed to
successfully launch your web experience application.

## Step 5: Update your Microsoft

Entra ID application with the web experience URL

After you create your Amazon Q Business application and web experience,
update your Microsoft Entra ID application with the web experience
URL.

Return to the Entra ID console, edit the Basic SAML
Configuration of your Entra ID application to update the
**Identifier (Entity ID)** and **Reply URL (Assertion
Consumer Service URL)** you added in Step 1 to your web experience URL.
Remember to save your changes.

**To update your Microsoft Entra ID
application**

1. Return to the Microsoft Entra admin center and navigate to
   your application.
2. In the left navigation pane, choose **Single
   sign-on**.
3. In the **Basic SAML Configuration** section, choose
   **Edit**.
4. Update the following fields with your Amazon Q Business web
   experience URL:
   1. For **Identifier (Entity ID)**,replace
      `https://sampleurl.com` with your web
      experience URL with the `/saml` suffix added. For
      example:
      `https://abcdefgh.qbusiness.us-east-1.on.aws/saml`.
   2. For **Reply URL (Assertion Consumer Service
      URL)**, replace
      `https://sampleurl.com` with your web
      experience URL with `/saml` added at the end. For
      example:
      `https://abcdefgh.qbusiness.us-east-1.on.aws/saml`.

5. Choose **Save**.

You've finished configuring your Amazon Q Business for chat. Your authenticated end users
can now log in and chat with your web experience.

## Troubleshooting Microsoft

Entra ID integration

If you encounter issues with your Microsoft Entra ID integration,
check the following:

**SAML assertion validation errors**

If you receive errors about invalid SAML assertions, verify
that:

- The **Identifier (Entity ID)** is set to
  `https://signin.aws.amazon.com/saml`.
- The **Reply URL** ends with
  `/saml` and matches your web experience URL
  exactly.
- All three required SAML attributes are correctly configured:
  `Role`, `RoleSessionName`, and
  `PrincipalTag:Email`.

**Access denied errors**

If users receive access denied errors when trying to access the
Amazon Q Business web experience, check that:

- The IAM role ARN and identity provider ARN in the
  `Role` attribute are correct and separated by a
  comma.
- The IAM role has the necessary permissions for Amazon Q Business web experience access.
- The trust relationship in the IAM role is correctly configured
  to trust the SAML identity provider.

**User not provisioned errors**

If users receive errors about not being provisioned in Amazon Q Business, verify that:

- The `PrincipalTag:Email` attribute is correctly
  configured to use `user.mail`.
- The user has a valid email address in Microsoft Entra
  ID.
- The default subscription tier is correctly set in the Amazon Q Business application.

**Testing SAML configuration**

To test your SAML configuration:

1. In the Microsoft Entra admin center, navigate
   to your application.
2. Choose **Single sign-on**, then scroll down
   to **Test single sign-on with <application
   name>**.
3. Choose **Test** to sign in as the current
   user, or choose **Test as another user** to
   sign in as a different user.
4. If the test is successful, you'll be redirected to your
   Amazon Q Business web experience.

For SAML assertion validation errors, access denied errors, and user not
provisioned errors, you'll need to check the Microsoft Entra ID
configuration in the admin portal as described in the Console tab.

For more information about SAML federation with Microsoft Entra ID,
see [Set up SAML-based single sign-on](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso "https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/add-application-portal-setup-sso") in the Microsoft Entra
documentation.
