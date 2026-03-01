# Configuring the Amazon Q Business browser extension for use

After installation and authentication, your users can access Amazon Q
while browsing the web.

###### Note

- Amazon Q does not support users who authenticate using
  external SAML providers.
- The Safari browser is not supported.
- Amazon Q Business does not use user data for service improvement
  or for training its underlying large language models (LLMs). For more
  information, see [Amazon Q Business Service
  improvement](service-improvement.md "service-improvement.md").
- Upload your documents and have Amazon Q answer contextual
  questions about them.

###### Topics

- [Prerequisites for integrating the Amazon Q browser extension](#browser-extensions-prerequisites "#browser-extensions-prerequisites")
- [Integrating the browser extension with Amazon Q Business](#integrating-browser-extension "#integrating-browser-extension")
- [Activating and deploying the browser extension](#activating-deploying-extension "#activating-deploying-extension")

## Prerequisites for integrating the Amazon Q browser extension

As admins, before you can integrate the Amazon Q Business browser
extension, you must complete the following steps.

1. [Get started with Amazon Q Business](getting-started.md "getting-started.md")
2. [Create an IAM Identity Center-integrated
   application](create-application.md "create-application.md") or [Create an IAM federated
   application environment](create-application-iam.md "create-application-iam.md") and create your Amazon Q Business web
   experience.
3. To use this feature, do the following
   - Enable **Allow end users to send queries directly to
     the LLM** in your Admin controls and guardrails.
     For more information, see the [Response settings](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response") topic in
     [Admin controls and guardrails](guardrails.md "guardrails.md")
     and [`chatMode`](../api-reference/API_ChatSync.md#qbusiness-ChatSync-request-chatMode "../api-reference/API_ChatSync.md#qbusiness-ChatSync-request-chatMode") if you
     are configuring programmatically.
   - If you are using the IAM Identity Center or OpenID Connect
     (OIDC) provider in IAM, make sure your IAM role for an
     Amazon Q Business web experience using IAM Federation is up to date.
     For more information, see [IAM role for an Amazon Q Business
     web experience using IAM Federation](web-experience-iam-role-iam.md "web-experience-iam-role-iam.md").

## Integrating the browser extension with Amazon Q Business

To use the Amazon Q Business browser extension, you must allow it to
connect to your Amazon Q Business application environment and web experience. To do
this, admins can use the Amazon Q console, API, SDK, or AWS CLI.

###### Topics

- [Using the console](#integrating-browser-extensions-using-console "#integrating-browser-extensions-using-console")
- [Using the AWS API](#integrating-browser-extensions-browser-extensions-using-aws-api "#integrating-browser-extensions-browser-extensions-using-aws-api")

### Using the console

1. Sign in to the Amazon Q console.
2. Choose **Applications**, then select the name of
   your application environment from the list.
3. Choose **Integrations** under
   **Enhancements**.
4. Choose **Edit** in the **Browser
   extensions** section on the main page.
5. Choose the **Browser extensions** your want
   integrate with.

### Using the AWS API

Admin users can enable your browser extensions using the [`UpdateWebExperience`](../api-reference/API_UpdateWebExperience.md "../api-reference/API_UpdateWebExperience.md") and [`CreateWebExperience`](../api-reference/API_CreateWebExperience.md "../api-reference/API_CreateWebExperience.md")
operations.

## Activating and deploying the browser extension

After enabling the browser extension, complete these steps to activate and
deploy it:

1. Allow-list URLs. If you are using
   1. An OIDC provider like Okta: you must configure your identity
      provider (IdP) to support browser extension as follows. You will
      need to consult your provider on how to do this.
      1. Make sure you enable refresh grants
      2. Allow-list the following URLs with the IdP
         1. Mozilla based browsers —
            `https://ba6e8e6e4fa44c1057cf5f26fba9b2e788dfc34f.extensions.allizom.org`
         2. Chromium based browsers —
            `https://feihpdljijcgnokhfoibicengfiellbp.chromiumapp.org`

   2. IAM Identity Center, the above is not required and you can move
      to the next step of installing the browser extension for your
      users.

2. Install the browser extension for all users using the software
   deployment processes of your organization. The following is some
   information about policy settings from the browser vendors using mobile
   device management (MDM) software that may be helpful:
   1. Firefox policy settings: [https://mozilla.github.io/policy-templates/#extensionsettings](https://mozilla.github.io/policy-templates/#extensionsettings "https://mozilla.github.io/policy-templates/#extensionsettings")
   2. Chrome policy settings: [https://chromeenterprise.google/policies/#ExtensionSettings](https://chromeenterprise.google/policies/#ExtensionSettings "https://chromeenterprise.google/policies/#ExtensionSettings")
   3. Edge policy settings: [https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings](https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings "https://learn.microsoft.com/en-us/DeployEdge/microsoft-edge-policies#extensionsettings")
      and guide: [https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-manage-extensions-ref-guide")

3. Provide your selected users the browser store URL + Web experience URL
   so they can download and install the browser extension and connect to
   Amazon Q.
