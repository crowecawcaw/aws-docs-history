# Creating an Amazon Q Business application using IAM Federation through Okta

As the first step toward creating a generative artificial intelligence (AI) assistant,
configure your external identity provider and connect it to AWS Identity and Access Management.

When you create an application environment, you can also choose to create an Amazon Q Business web experience, which your end users can use to chat with your
application. You can also add subscriptions for end users who log in to your Amazon Q Business web experience using Okta. Any user logging in to
your web experience is automatically provisioned with a subscription of a type that you
select for them.

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
  Okta as an example. Integrating Amazon Q Business with
  Okta requires that you switch between tasks on the Amazon Q Business console and the Okta admin console.

###### Topics

- [Prerequisites](#create-iam-app-okta-prereqs "#create-iam-app-okta-prereqs")
- [Step 1: Create and configure an Okta application](#create-iam-app-okta-1 "#create-iam-app-okta-1")
- [Step 2: Add an identity provider in IAM](#create-iam-app-okta-2 "#create-iam-app-okta-2")
- [Step 3: Connect IAM to Okta](#create-iam-app-okta-3 "#create-iam-app-okta-3")
- [Step 4: Create Amazon Q Business application](#create-iam-app-okta-saml-4 "#create-iam-app-okta-saml-4")

## Prerequisites

Before you start to integrate Amazon Q Business with Okta,
make sure that you have:

- Created an Okta account and added at least one user with a
  valid email address. For more information, see [Manage users](https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-people.htm "https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-people.htm") on the _Okta Help
  Center_.
- Created IAM policies containing the permissions outlined in [IAM role for an Amazon Q Business web
  experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md") to:

      + Allow an Amazon Q Business web experience to invoke the API
       operations required to integrate your application
      + (If you're creating a Amazon Q Business default web
       experience) Allow Amazon Q Business to access the resources it
       needs to create a web experience
      + (If you're using OIDC) Allow an Amazon Q Business web
       experience to invoke the API operations required to decrypt the
       Secrets Manager secret you created for your OIDC web experience

  You will need these roles to complete creating your Amazon Q Business IAM federated application.

###### Note

To create a new policy, follow the instructions in [Creating
IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the AWS Identity and Access Management User Guide.

- (Optional) Checked [how subscriptions work](tiers.md#managing-sub-tiers-iam "tiers.md#managing-sub-tiers-iam") for Amazon Q Business applications using IAM Federation.

## Step 1: Create and configure an Okta application

This procedure outlines how to create and configure an Okta
instance for an Amazon Q Business application using a built-in web experience
and a custom Amazon Q Business application client you develop using Amazon Q Business APIs.

###### Important

Amazon Q Business supports Microsoft Entra ID with SAML
2.0, but doesn't support OIDC for Google or Microsoft
Entra ID.

SAML
**To create an Okta instance**

1. Sign into Okta and go to the admin
   console.
2. In the left navigation pane, choose
   **Applications**, and then choose
   **Create App Integration**.
3. On the **Create a new app integration** page,
   choose **SAML 2.0** and then choose
   **Next**.
4. On the **Create SAML Integration** page, in
   **General Settings**, for **App
   name**, enter a name for the application and choose
   **Next**.
5. In **Configure SAML**, do the
   following:
   1. For **Single sign-on URL**, enter
      your web application endpoint.

   If you're creating a custom Amazon Q Business
   application, this value is the endpoint URL of your
   Amazon Q Business application with
   `/saml` added at the end. For example
   `http://localhost:8000/saml`.

   If you're creating an Amazon Q Business
   application generated web experience endpoint URL, this
   value be the Amazon Q Business generated web
   experience URL with `saml` added at the end.
   For example,
   `https://abcdefgh.qbusiness.us-east-1.on.aws/saml`.

   ###### Important

   If you're creating an Amazon Q Business
   application generated web experience endpoint URL, a
   web experience URL will be generated by Amazon Q Business after you finish creating an
   Amazon Q Business application. For now,
   enter a placeholder URL. For example:
   `http://sampleurl.com`.
   You will update this at the end of your Amazon Q Business application creation
   process. 2. Deselect the **Use this for Recipient URL and
   Destination URL** box. 3. Then, for the **Recipient URL**
   field, enter the following AWS endpoint:
   `https://signin.aws.amazon.com/saml`. 4. For **Destination URL**, enter your
   web application endpoint.

   If you're creating a custom Amazon Q Business
   application, this value is the endpoint URL of your
   Amazon Q Business application with
   `/saml` added at the end. For example
   `http://localhost:8000/saml`.

   If you're creating an Amazon Q Business
   application generated web experience endpoint URL, this
   value be the Amazon Q Business generated web
   experience URL with `saml` added at the end.
   For example,
   `https://abcdefgh.qbusiness.us-east-1.on.aws/saml`.

   If you're creating an Amazon Q Business
   application generated web experience endpoint URL, a web
   experience URL will be generated by Amazon Q Business after you finish creating an Amazon Q Business application. For now, enter a
   placeholder URL. For example:
   `http://sampleurl.com`. You
   will update this at the end of your Amazon Q Business application creation process. 5. For **Audience URI (SP Identity
   ID)**, enter the following AWS endpoint:
   `https://signin.aws.amazon.com/saml`. 6. For **Name ID format**, set to
   **Persistent**. 7. The, scroll down to the bottom of the page and select
   **Next**.

6. On the Create SAML Integration page, select the
   option that best fits your use case and then select
   **Finish**. You will be redirected to the
   application summary page.
7. On the application summary page, from the top navigation menu,
   select **Assignments**, and then select
   **Assign**. Then, complete the following
   steps:
   1. To assign users to your Okta app,
      choose between **Assign to People** and
      **Assign to Groups**.
   2. In the dialog box that opens up, locate the users or
      groups you want to assign to your application and then
      select **Assign**.
   3. Then, choose **Done**.

8. Next, you download the SAML payload and copy your
   **Sign on URL**.

You need to provide the SAML payload when you create an
identity provider in IAM.

If you choose to create a web experience from the Amazon Q Business console (Step 4 of this page), you input the
**Sign on URL** or **Single Sign-On
URL** (the URL where users sign in to access an
application integrated with an identity provider) as the
**Authentication URL**. The standard
authentication URL format for Okta is:
`https://<sub_domain>.okta.com/app/<app_name>/<app_id>/sso/saml`.

From the top navigation menu of your application home page,
select **Sign On**. Then, complete the
following steps:

    1. In the **Settings**, from the
     **SAML 2.0** section, from
     **Metadata details** section, to
     copy the metadata file XML file by choosing
     **Copy**. Then, save it in
     `.xml` format.


    ###### Note

    You can also navigate to the metadata URL and copy
     the network response payload and paste it in a file
     that you save in `.xml` format.


     For more information, see [Create SAML app integrations](https://help.okta.com/oie/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm "https://help.okta.com/oie/en-us/Content/Topics/Apps/Apps_App_Integration_Wizard_SAML.htm") on the
     *Okta Help
     Center* website.
    2. Then, from **Sign on URL**, select
     the **Copy** icon to copy the Sign on
     URL. Save it in a text editor of your choice.

OIDC
**To create an Okta instance**

1. Sign into Okta and go to the admin
   console.
2. In the left navigation pane, choose
   **Applications**, and then choose
   **Create App Integration**.
3. On the **Create a new app integration** page,
   do the following:
   - Choose **OIDC – OpenID
     Connect**.
   - Choose **Web application**.
   - Then, choose **Next**.

4. On the **New Web App Integration** page, do
   the following:
   - In **General Settings**, for
     **App name**, enter a name for the
     application.
   - In **Grant type**, for **Core
     grants**, ensure that
     **Authorization Code** is
     selected.
   - In **Sign-in-redirect URIs**, add a
     URL that Okta will send the
     authentication response and ID token for the user's sign
     in request.

   If you're using a custom application, the value of
   this URL will be
   `http://localhost:8080/authorization-code/callback`,
   where `http://localhost:8080` is your custom
   web experience endpoint URL.

   If you're creating an Amazon Q Business
   application generated web experience endpoint URL, this
   value will be the Amazon Q Business generated web
   experience URL with
   `/authorization-code/callback` added at
   the end. Amazon Q Business generates this web
   experience URL when you create a Amazon Q Business
   application using in Step 4. For now, enter a
   placeholder URL. For example:
   `http://sampleurl.com/authorization-code/callback`.
   You will update this after you finish creating a Amazon Q Business application by inputting your
   Amazon Q Business web experience URL with
   `/authorization-code/callback` added at
   the end. For example,
   `https://abcdefgh.qbusiness.us-east-1.on.aws/authorization-code/callback`.
   - In **Assignments**, select whether to
     assign the app integration to everyone in your org, only
     selected group(s), or skip assignment until after app
     creation.
   - Then, select **Save**.

5. From the application summary page, from
   **General**, do the following:
   - From **Client Credentials**, copy and
     save the **Client ID**. You will input
     this as the **Audience** when you
     create an identity provider in AWS Identity and Access Management in the next
     step.
   - From **CLIENT SECRETS**, copy and
     save the **Secret**. If you choose to
     use an Amazon Q Business default web experience,
     you will need to input this in an Secrets Manager secret when you
     configure **Web experience settings**
     in the Amazon Q Business console.

6. From the left navigation menu, select
   **Security**, and then select
   **API**.
7. Then, from **Authorization Servers**, do the
   following:
   - Copy the **Issuer URI**, for example
     `https://trial-`okta-instance-id`.okta.com/oauth2/default`.
     You will need to input this value as the
     **Provider URL** when you add your
     identity provider in IAM in Step 2.
   - Select **default**, and then select
     **Claims**.

8. In **Claims**, select **Add
   claim**, and then do the following:
   - For **Name**, add
     `https://aws.amazon.com/tags`.
   - For **Include in token type**, choose
     `ID token` and select
     **Always**.
   - For Okta, the
     **Value** will be the following:
     `{"principal_tags": {"Email": {user.email}
}}`. For other identity providers, use a valid
     JSON object in the following format:

   ```
   "principal_tags": {
       "Email": [email]
   }
   ```

   ###### Note

   To activate [Amazon Q Business
   response personalization](personalizing-chat-responses.md "personalizing-chat-responses.md") for your
   application, add the following optional tags:
   `{"principal_tags": {"Email": {user.email},
 "country": {user.city != null ? user.city :
 ""}}}`. Ensure that null values aren't
   passed via principal tags by using the operation
   `user.$attribute != null ? user.$attribute :
 ""`.
   - For **Include in**, choose `Any
scope`.
   - Select **Create**.

You are now ready to go to the AWS Identity and Access Management console and create an OIDC
identity provider instance.

###### Important

Amazon Q Business supports Microsoft Entra ID
with SAML 2.0, but doesn't support OIDC for Google or
Microsoft Entra ID.

You are now ready to move to the AWS Identity and Access Management console to create an identity provider
integration for your Okta instance.

## Step 2: Add an identity provider in IAM

In this step, you add configure AWS Identity and Access Management by creating an identity provider
integration for your Okta instance.

SAML
**To connect Okta to AWS Identity and Access Management**

1. Sign in to the AWS Identity and Access Management console.
2. In the left navigation menu, from **Access
   management**, select **Identity
   providers**.
3. From **Identity providers**, select
   **Add provider**.
4. In **Add an identity provider**, for
   **Configure provider** do the
   following:
   - For **Provider type** – Select
     **SAML**.
   - For **Provider name** – Add a
     name to identify your identity provider.
   - For **Metadata document** –
     Upload the `.xml` file you downloaded and
     saved from Okta in Step 1.
   - For **Add tags -
     _optional_** –
     Add tags to resources to help identify, organize, or
     search for the identity provider you're adding.
   - Select **Add provider**.

5. On the **Identity provider** summary page,
   from **Provider**, select the provider you just
   added do the following:
   - From **Summary** copy the
     **ARN** and save the value. You
     will need it when you add your trust policy and when you
     connect your AWS Identity and Access Management identity provider to your
     Okta instance. The format of the ARN
     is:
     `arn:aws:iam::`aws-account-id`:saml-provider/`assigned-iam-idp-name``.
   - Then, select **Assign role** to
     create an IAM role with the necessary permissions for
     your identity provider.

6. In **Assign role**, for **Role
   options** select **Create a new
   role**.
7. Then, on the **Selected trusted entity**
   page, do the following:
   - For **Trusted entity type** select
     **SAML 2.0 federation**.
   - In **SAML 2.0 federation**, from the
     **SAML 2.0-based provider**
     drop-down, select the identity provider you
     added.
   - For **Access to be allowed**, select
     **Allow programmatic access
     only**.
   - For **Attribute**, select
     **SAML:aud**.
   - For **Value**, enter the following:
     `https://signin.aws.amazon.com/saml`.
   - Select **Next**.

8. On the **Add permissions** page, for
   **Permissions policies** choose an IAM
   policy with the required permissions and then select
   **Next**.

For the policy permissions required, see [IAM role for an Amazon Q Business web experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md").

###### Note

To create a new policy, follow the instructions in [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the AWS Identity and Access Management User
Guide. 9. In the **Name, review, and create** page, add
a **Role name**, and optional role description
and tags to identify your IAM role. Then, select
**Create role**. 10. From the **Roles** page, select the IAM
role you just created. Then, from the role summary page, do the
following:

    * Copy the role **ARN** and save it.
     You will need this information to connect your AWS Identity and Access Management
     identity provider instance to Okta. The
     format of the ARN will be like this:
     `arn:aws:iam::111122223333:role/sample-role`.
    * In **Trust relationships**, select
     **Edit trust policy** and select
     **Add new statement** to add the
     following trust policy, replacing the value for
     `account_id` with your
     AWS account ID and
     `saml_provider` with the
     `assigned-iam-idp-name` you
     copied from your IAM identity provider ARN you
     copied:







    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Action": "sts:AssumeRoleWithSAML",
     "Sid": "SAMLAssumeRoleAccess",
     "Effect": "Allow",
     "Condition": {
     "StringEquals": {
     "SAML:aud": "https://signin.aws.amazon.com/saml"
     }
     },
     "Principal": {
     "Federated": "arn:aws:iam::111122223333:saml-provider/`saml-provider-name`"
     }
     },
     {
     "Action": "sts:TagSession",
     "Sid": "SAMLTagSessionAccess",
     "Effect": "Allow",
     "Condition": {
     "StringLike": {
     "aws:RequestTag/Email": "*"
     }
     },
     "Principal": {
     "Federated": "arn:aws:iam::111122223333:saml-provider/`saml-provider-name`"
     }
     }
     ]
    }`

    ```
    * Then, select **Update
     policy**.

You are now ready to return to Okta to complete the
process of establishing a trust relationship between AWS Identity and Access Management and
Okta.

OIDC
**To connect Okta to AWS Identity and Access Management**

1. Sign in to the AWS Identity and Access Management console.
2. In the left navigation menu, from **Access
   management**, select **Identity
   providers**.
3. From **Identity providers**, select
   **Add provider**.
4. In **Add an identity provider**, for
   **Configure provider** do the
   following:
   - For **Provider type** – Select
     **OpenID Connect**.
   - For **Provider URL** – Paste
     the **Input URI** you copied from the
     Okta console. For example,
     `trial-`okta-instance-id`.okta.com/oauth2/default`.
   - For **Audience** – Copy and
     paste the Client ID you copied from Okta
     from the Okta console.
   - For **Add tags -
     _optional_** –
     Add tags to resources to help identify, organize, or
     search for the identity provider you're adding.
   - Select **Add provider**.

5. On the **Identity provider** summary page,
   from **Provider**, select the provider you
   added do the following:
   - From **Summary** copy the
     **ARN** and save the value. You
     will need it when you add your trust policy and when you
     connect your AWS Identity and Access Management identity provider to your
     Okta instance. The format of the ARN
     is:
     `arn:aws:iam::`aws-account-id`:oidc-provider/`issuer``.
   - Then, select **Assign role** to
     create an IAM role with the necessary permissions for
     your identity provider.

6. In the **Assign role** dialog box that opens,
   for **Role options** select **Create a
   new role**.
7. Then, on the **Selected trusted entity**
   page, do the following:
   - For **Trusted entity type** select
     **Web identity**.
   - In **Web identity**, from the
     **Identity provider** drop-down,
     select the identity provider you added.
   - For **Audience**, select your Client
     ID.
   - Select **Next**.

8. On the **Add permissions** page, for
   **Permissions policies** choose an IAM
   policy to add, and then select **Next**. You
   can add an existing policy or update your policy you're creating
   to include required permissions. Your policy must contain the
   permissions outlined in [IAM role for an Amazon Q Business web experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md").

###### Note

To create a new policy, follow the instructions in [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the AWS Identity and Access Management User
Guide. 9. In the **Name, review, and create** page, add
a **Role name** add a role name, and optional
role description and tags to identify your IAM role. Then,
select **Create role**. 10. From the **Roles** page find and select the
IAM role you created. Then, from the role summary page, in
**Trust relationships**, select
**Edit trust policy** and select
**Add new statement** 11. Then, add the following statement to your existing trust
policy, replacing `account-id` with
your AWS account ID, `clientId` with
the OIDC client ID you copied, and
`iss` with the
`issuer` value from your IAM
identity provider ARN:

```


```

12. Then, select **Update policy**.

Now, move on to the Amazon Q Business console to create your
application.

## Step 3: Connect IAM to Okta

In this step, you complete configuring the trust relationship between AWS Identity and Access Management
and Okta.

SAML

1. Sign into Okta and go to the admin
   console.
2. In the left navigation pane, choose
   **Applications**, and then choose the
   Okta application you created.
3. In **General**, from **SAML
   Settings** choose **Edit**.
4. In **Edit SAML**, for **General
   Settings** choose **Next**.
5. In **Configure SAML**, scroll down to the
   **Attribute Statements** section, and add
   the following attributes:

**Attribute 1**

    * For the **Name** field, provide the
     following for the email attribute:
     `https://aws.amazon.com/SAML/Attributes/PrincipalTag:Email`.
    * For the **Name format** field, keep
     it set to **Unspecified**.
    * For the **Value** field, provide a
     mapping to the attribute by selecting
     `user.email` from the drop-down
     list.


    ###### Note

    You can add more attributes to enable [Amazon Q Business
     response personalization](personalizing-chat-responses.md "personalizing-chat-responses.md"). To do this,
     provide the following value for the
     **Name** field:
     `https://aws.amazon.com/SAML/Attributes/PrincipalTag:<attributeName>`.
     Keep the **Name format** field
     **Unspecified**. For
     **Value**, provide an attribute
     mapping by selecting a user attribute like
     `user.city` from the drop-down
     list.

**Attribute 2**

    * For the **Name** field, provide the
     following name for the role attribute:
     `https://aws.amazon.com/SAML/Attributes/Role` .
    * For the **Name format** field, keep
     it set to **Unspecified**.
    * For the **Value** field, add a
     mapping to the attribute in the following format using
     the values you copied from Step 2 of this section:
     `IAMroleArn,IAMidpArn`. For example:
     `arn:aws:iam::111122223333:role/sample-role,arn:aws:iam::111122223333:saml-provider/okta-idp`.

**Attribute 3**

    * Then, for the **Name** field, provide
     the following name for the role session name attribute:
     `https://aws.amazon.com/SAML/Attributes/RoleSessionName`.
    * For the **Name format** field, keep
     it set to **Unspecified**.
    * For the **Value** field, provide a
     mapping to the attribute by selecting
     `user.email` from the drop-down
     list.
    * Choose **Next**, and then choose
     **Finish**.

Now, move on to the Amazon Q Business console to create your
application.

OIDC
**This step isn't needed for
OIDC.**

## Step 4: Create Amazon Q Business application

To create an Amazon Q Business application environment, you can use either the
AWS Management Console or the Amazon Q Business API. When you create an application,
response generation from large language model (LLM) knowledge is enabled by
default.

If you're using an Amazon Q Business default web experience for your
application, you can choose to generate it in this step. If you're using this
generated URL as your web experience endpoint, you need to return to
Okta to update your identity provider instance with this
information.

You also add subscriptions for end users logging into your Amazon Q Business
web experience using Okta. Any user logging into your web experience
is automatically provisioned a subscription of the type you select.

###### Warning

User subscriptions are connected to the AWS account Amazon Q Business
applications are attached to. If the same user logs in to an Amazon Q Business application using multiple AWS accounts, they're charged
multiple times. [Create an Amazon Q Business application using
IAM Identity Center](create-application.md "create-application.md") for user management to avoid this issue.

For a consolidated view of your user subscriptions—including a list of
subscribed users, their subscription status, and applications, accounts, or services
a user can access through their subscriptions—see the [Amazon Q subscriptions page](https://console.aws.amazon.com/amazonq/subscriptions "https://console.aws.amazon.com/amazonq/subscriptions").
Subscriptions can only be viewed centrally and _not_ be created
or updated from the Amazon Q subscription management console.

For more information on user subscriptions for an IAM federated Amazon Q Business application, see [Subscriptions for applications using IAM
Federation](tiers.md#managing-sub-tiers-iam "tiers.md#managing-sub-tiers-iam").

As a prerequisite, make sure that you complete the [setting
up](setting-up.md "setting-up.md") tasks. If you're using the AWS CLI or the API, make sure that you
created the required [IAM roles](setting-up.md "setting-up.md").

The following tabs provide a procedure for creating your Amazon Q Business
application environment using the AWS Management Console and code examples for using the AWS CLI.

Console
**To create an application**

1. Sign in to the AWS Management Console and open the Amazon Q Business
   console.
2. On the **Create application** page, for
   **What kind of application do you want to
   create?**, enter the following information for your
   Amazon Q Business application:
   1. **Application name** – A name
      for your Amazon Q Business application environment for easy
      identification. This name is only visible in the
      AWS Management Console. The name can include hyphens (-), but not
      spaces, and can have a maximum of 1,000 alphanumeric
      characters. Amazon Q Business auto-generates an
      application name for you, unless you choose to enter a
      custom name.
   2. **Outcome** – Select
      **Web experience** to create a web
      experience for your application. Amazon Q Business
      creates a web experience by default when you create an
      application. If you don't want to create a web
      experience, deselect this option.

3. For **Access management method**, choose
   **AWS IAM Identity Provider**.

Then, for **Choose an identity provider
type**, choose between **Security Assertion
Markup Language (SAML)** and **OpenID
Connect (OIDC)**.

    1. For **SAML**, do the
     following:


    	1. For **Select Identity
    	 Provider**, choose the identity provider
    	 you've created in AWS Identity and Access Management to use with your
    	 Amazon Q Business application.
    	2. For **Authentication URL**,
    	 provide the authentication URL for
    	 Okta. Your authentication URL must
    	 be of the following format:
    	 `https://`<sub_domain>`.okta.com/app/`<app_name>`/`<app_id>`/sso/saml`.
    	 Enter the **Sign on URL** you
    	 copied in Step 1.


    	When end users navigate to the web experience
    	 URL they're redirected to this authentication URL
    	 where they provide their login ID and password.
    	 After successful authentication, they're
    	 redirected back to the web experience URL to begin
    	 chatting.
    2. For **OIDC**, do the
     following:


    	1. For **Select Identity
    	 Provider**, choose the identity provider
    	 you've created in AWS Identity and Access Management to use with your
    	 Amazon Q Business application.
    	2. For **ClientID for OIDC**,
    	 input the OIDC client ID you copied
    	 in Step 1.
    	3. For **AWS Secrets Manager**, choose to
    	 create a new Secrets Manager secret or add an existing one
    	 to allow Amazon Q Business to access your
    	 Okta instance. Your secret must
    	 contain the client secret you copied from your
    	 Okta instance.
    	4. In **Choose method to authorize
    	 Amazon Q Business web experience to use
    	 Secrets**, choose an existing IAM role to allow your Amazon Q Business web experience to access the
    	 AWS resources it needs to
    	 function.


    	For the policy permissions required, see
    	 [IAM role for an Amazon Q Business web experience using IAM
    	 Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md").


    	###### Note

    	To create a new policy, follow the
    	 instructions in [Creating IAM policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the AWS Identity and Access Management
    	 User Guide.

4. For **Default subscription settings**, for
   **Subscription tier**, choose between
   **Q Business Pro** and **Q Business
   Lite**. Any user logging in to your web experience
   will be assigned this subscription type by default.
5. For **Application details** – Amazon Q Business chooses the following configuration settings
   for your application by default:
   1. For **Application service access**
      – Amazon Q Business will create a new
      service-linked role for your application.
   2. **Encryption** – Amazon Q Business will create an AWS owned AWS KMS key
      to encrypt your data.
   3. For **Web experience service access**
      – If you've chosen to create a web experience,
      Amazon Q Business requires you select an
      existing role to allow end users to log in to a Amazon Q Business web experience.

6. (Optional) To customize **Application
   details**, expand the **Application details
   section**, and then do the following:
   1. In **Application service access**,
      for **Choose a method to authorize Amazon Q Business**, choose from the
      following options:
      1. **Create and use a new service-linked
         role (SLR)** – Create and use a
         new Amazon Q Business-managed IAM role to
         allow it to access the AWS
         resources it needs to create your
         application.
      2. **Create and use a new service role
         (SR)** – Create and use a new
         IAM role for Amazon Q Business to allow it to access the AWS
         resources it needs to create your
         application.
      3. **Use an existing service role
         (SR)/service-linked role (SLR)** –
         Use an existing service role or service-linked
         IAM role to allow Amazon Q Business to access the AWS
         resources it needs to create your
         application.

      ###### Note

      For more information about example service
      roles, see [IAM role for an Amazon Q Business application](create-application-iam-role.md "create-application-iam-role.md"). For
      information on service-linked roles, including to
      manage them, see [Using service-linked
      roles](../business-use-dg/using-service-linked-roles.md "../business-use-dg/using-service-linked-roles.md"). 4. **Service role name**
      – A name for the service (IAM) role you created for easy identification on
      the console.

   2. For **Encryption** – Amazon Q Business encrypts your data by default using
      AWS managed AWS KMS keys. To customize your
      encryption settings, select **Customize
      encryption settings (advanced)**. Then, you
      can choose to use an existing AWS KMS key or
      create a new one.
   3. In **Web experience service access**,
      enter the following information:
      1. For **Choose a method to authorize
         Amazon Q Business** – A
         service access role assumed by end users when they
         sign in to your web experience that grants them
         permission to start and manage conversations
         Amazon Q Business. You can only choose to
         use an existing role. For more information on how
         to create a role and permissions needed, see
         [Prerequisites for creating an
         IAM federated application](create-application-iam-okta.md#create-iam-app-okta-prereqs "create-application-iam-okta.md#create-iam-app-okta-prereqs").
      2. **Service role name**
         – A name for the service role you created
         for easy identification on the console.

7. To start creating your application, choose
   **Create**.

###### Note

If you're creating a web experience, you can also choose
to create your application and [view your web experience](customizing-web-experience-iam.md "customizing-web-experience-iam.md") by
selecting **Create and open web
experience**. 8. Once the application creation process completes, the web
experience settings section on your application summary page
will display your Amazon Q Business web experience URL.
Copy the URL to a file and then, depending on the authentication
type you've chosen, do the following:

    1. **If you're using SAML**
     – Add `/saml` at the end of the URL.
     Then, Return to the Okta console, edit
     your SAML application to update
     **Single sign-on URL** and
     **Destination URL** you added in
     Step 1 to your web experience URL. Remember to save your
     changes.
    2. **If you're using OIDC**
     – Add `/authorization-code/callback`
     at the end of the URL. Then, return to the
     Okta console to edit your
     OIDC application and update the
     **Sign-in-redirect URI** value you
     added in Step 1. Remember to save your changes.

AWS CLI
**To configure an Amazon Q Business
application**

```

aws qbusiness create-application \
--display-name application-name \
--iam-identity-provider-arn iam-identity-provider-arn \
--client-id-for-oidc client-id-for-oidc \
--identity-type identity-type\
--role-arn roleArn \
--description application-description \
--encryption-configuration kmsKeyId=<kms-key-id> \
--attachments-configuration attachmentsControlMode=ENABLED
```

You've finished configuring your Amazon Q Business application. Your
authenticated end users can now log in and chat with your web experience.
