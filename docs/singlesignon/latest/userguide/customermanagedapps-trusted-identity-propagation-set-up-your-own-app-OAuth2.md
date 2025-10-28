# Set up customer managed OAuth 2.0 applications for trusted identity

propagation

To set up a customer managed OAuth 2.0 application for trusted identity
propagation, you must first add it to IAM Identity Center. Use the following procedure to add
your application to IAM Identity Center.

###### Topics

- [Step 1: Select application type](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-select-app-type "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-select-app-type")
- [Step 2: Specify application details](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-app-details "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-app-details")
- [Step 3: Specify authentication settings](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-authentication-settings "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-authentication-settings")
- [Step 4: Specify application credentials](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-application-credentials "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-application-credentials")
- [Step 5: Review and configure](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-review-and-configure "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-review-and-configure")

## Step 1: Select application type

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Applications**.
3. Choose the **Customer managed** tab.
4. Choose **Add application**.
5. On the **Select application type** page, under
   **Setup preference**, choose **I have
   an application I want to set up**.
6. Under **Application type**, choose
   **OAuth 2.0**.
7. Choose **Next** to proceed to the next page,
   [Step 2: Specify application details](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-app-details "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-app-details").

## Step 2: Specify application details

1. On the **Specify application details** page,
   under **Application name and description**, enter a
   **Display name** for the application, such as
   `MyApp`. Then, enter a
   **Description**.
2. Under **User and group assignment method**,
   choose one of the following options:
   - **Require assignments** – Allow
     only IAM Identity Center users and groups who are assigned to this
     application to access the application.

   Application tile visibility –Only users who are
   assigned to the application directly or through a group
   assignment can view the application tile in the AWS access portal,
   provided that **Application visibility in
   AWS access portal** is set to
   **Visible**.
   - **Do not require assignments** –
     Allow all authorized IAM Identity Center users and groups to access this
     application.

   Application tile visibility – The application tile
   is visible to all users who sign in to the AWS access portal,
   unless **Application visibility in
   AWS access portal** is set to **Not
   visible**.

3. Under **AWS access portal**, enter the URL where users
   can access the application and specify whether the application tile
   will be visible or not visible in the AWS access portal. If you choose
   **Not visible**, not even assigned users can
   view the application tile.
4. Under **Tags (optional)**, choose **Add
   new tag**, and then specify values for
   **Key** and **Value
   (optional)**.

For information about tags, see [Tagging AWS IAM Identity Center resources](tagging.md "tagging.md"). 5. Choose **Next**, and proceed to the next page,
[Step 3: Specify authentication settings](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-authentication-settings "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-authentication-settings").

## Step 3: Specify authentication settings

To add a customer managed application that supports OAuth 2.0 to IAM Identity Center,
you must specify a trusted token issuer. A trusted token issuer is an OAuth
2.0 authorization server that creates signed tokens. These tokens authorize
applications that initiate requests (requesting applications) for access to
AWS managed applications (receiving applications).

1. On the **Specify authentication settings** page,
   under **Trusted token issuers**, do either of the
   following:
   - To use an existing trusted token issuer:

   Select the check box next to the name of the trusted token
   issuer that you want to use.
   - To add a new trusted token issuer:
     1. Choose **Create trusted token
        issuer**.
     2. A new browser tab opens. Follow steps 5 through 8
        in [How to add a trusted
        token issuer to the IAM Identity Center console](setuptrustedtokenissuer.md#how-to-add-trustedtokenissuer "setuptrustedtokenissuer.md#how-to-add-trustedtokenissuer").
     3. After you complete these steps, return to the
        browser window that you are using for your
        application setup and select the trusted token
        issuer that you just added.
     4. In the list of trusted token issuers, select the
        check box next to the name of the trusted token
        issuer that you just added.

     After you select a trusted token issuer, the
     **Configure selected trusted token
     issuers** section appears.

2. Under **Configure selected trusted token
   issuers**, enter the **Aud claim**.
   The **Aud claim** identifies the intended audience
   (recipients) for the token that is generated by the trusted token
   issuer. For more information, see [Aud claim](trusted-token-issuer-configuration-settings.md#trusted-token-issuer-aud-claim "trusted-token-issuer-configuration-settings.md#trusted-token-issuer-aud-claim").
3. To prevent your users from having to reauthenticate when they are
   using this application, select **Enable refresh token
   grant**. When selected, this option refreshes the
   access token for the session every 60 minutes, until the session
   expires or the user ends the session.
4. Choose **Next**, and proceed to the next page,
   [Step 4: Specify application credentials](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-application-credentials "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-specify-application-credentials").

## Step 4: Specify application credentials

Complete the steps in this procedure to specify the credentials that your
application uses to perform token exchange actions with trusted
applications. These credentials are used in a resource-based policy. The
policy requires that you specify a principal that has permissions to perform
the actions that are specified in the policy. **You must
specify a principal**, even if the trusted applications are in
the same AWS account.

###### Note

When you set permissions with policies, grant only the permissions
required to perform a task. You do this by defining the actions that can
be taken on specific resources under specific conditions, also known as
least-privilege permissions.

This policy requires the [`CreateTokenWithIAM`](../OIDCAPIReference/API_CreateTokenWithIAM.md "../OIDCAPIReference/API_CreateTokenWithIAM.md")
API action. For more information about this policy, and an example that you can adapt as required for your environment, see [Resource-based policy example for IAM Identity Center
IAM Identity Center](iam-auth-access-using-resource-based-policies.md "iam-auth-access-using-resource-based-policies.md").

1. On the **Specify application credentials** page,
   do either of the following:
   - To quickly specify one or more IAM roles:
     1. Choose **Enter one or more IAM
        roles**.
     2. Under **Enter IAM roles**,
        specify the Amazon Resource Name (ARN) of an
        existing IAM role. To specify the ARN, use the
        following syntax. The Region portion of the ARN is
        blank because IAM resources are global.

     ```
       arn:aws:iam::`account`:role/`role-name-with-path`
     ```

     For more information, see [Cross-account access using resource-based
     policies](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md#access_policies-cross-account-using-resource-based-policies "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md#access_policies-cross-account-using-resource-based-policies") and [IAM ARNs](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") in the _AWS Identity and Access Management
     User Guide_.

   - To manually edit the policy (required if you specify
     non-AWS credentials):
     1. Select **Edit the application
        policy**.
     2. Modify your policy by typing or pasting text in
        the JSON text box.
     3. Resolve any security warnings, errors, or general
        warnings generated during policy validation. For
        more information see [Validating IAM policies](../../../IAM/latest/UserGuide/access_policies_policy-validator.md "../../../IAM/latest/UserGuide/access_policies_policy-validator.md") in the
        _AWS Identity and Access Management User Guide_.

2. Choose **Next** and proceed to the next page,
   [Step 5: Review and configure](#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-review-and-configure "#customermanagedapps-trusted-identity-propagation-set-up-your-own-app-OAuth2-review-and-configure").

## Step 5: Review and configure

1. On the **Review and configure** page, review the
   choices that you made. To make changes, choose the configuration
   section that you want, choose **Edit**, and then
   make the required changes.
2. After you are finished, choose **Add
   application**.
3. The application that you added appears in the **Customer
   managed applications** list.
4. After you set up your customer managed application in IAM Identity Center, you
   must specify one or more AWS services, or trusted applications,
   for identity propagation. This enables users to sign in to your
   customer managed application and access data in the trusted
   application.

For more information, see [Specify trusted applications](trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.md "trustedidentitypropagation-using-customermanagedapps-specify-trusted-apps.md") .
