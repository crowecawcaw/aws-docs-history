# Configuring an Amazon Q Business application

using AWS IAM Identity Center

As the first step towards creating a generative artificial intelligence (AI) assistant,
you configure an application environment, and grant end user access to users to interact with an
application environment using AWS IAM Identity Center for user management. Then you provision subscriptions for
your IAM Identity Center users and groups.

Your authorized users interact with your application environment through the web experience. You
share the endpoint URL of your web experience with your users, who open the URL and are
authenticated before they can start chatting. The endpoint URL can be found in your web
experience settings when selecting your application environment in the console.

This section guides you through the process of creating and configuring an Amazon Q Business application environment. To create an application environment, you can use the Amazon Q Business console, the AWS Command Line Interface (AWS CLI), and Amazon Q Business API
operations.

As a prerequisite, make sure that you complete the [setting
up](setting-up.md "setting-up.md") tasks and go through the [configuring an
IAM Identity Center instance](idc-setup.md "idc-setup.md") section. If you're using the AWS CLI or the API, make sure that
you've created the required [IAM roles](setting-up.md "setting-up.md").

After you finish creating your application environment, you can customize and preview the web
experience that it will power.

###### Note

Response generation from large language model (LLM) knowledge is enabled by default
for your application.

###### Topics

- [Configuring an IAM Identity Center instance for an Amazon Q Business
  application](idc-setup.md "idc-setup.md")
- [Creating an Amazon Q Business application environment](create-app.md "create-app.md")
- [Migrating an Amazon Q Business direct SAML 2.0
  application to IAM Identity Center](migrate-application.md "migrate-application.md")
- [Making authenticated Amazon Q Business API calls using IAM Identity Center](making-sigv4-authenticated-api-calls.md "making-sigv4-authenticated-api-calls.md")
- [Managing Amazon Q Business application
  resources](managing-resources.md "managing-resources.md")
