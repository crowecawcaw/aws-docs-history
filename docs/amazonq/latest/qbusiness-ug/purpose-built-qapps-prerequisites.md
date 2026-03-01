# Prerequisites for Amazon Q Apps

Before using Amazon Q Apps, make sure that you do the following:

- **Set up your identity provider** – For
  web experience users to create and run their own Amazon Q Apps within a broader
  Amazon Q Business application environment, they must be recognized by either
  IAM Identity Center or AWS Identity and Access Management (IAM). These users can continue to authenticate either
  directly through IAM Identity Center, or through an existing enterprise identity provider
  connected to IAM Identity Center or IAM (like Okta, Microsoft Entra
  ID, and Ping Identity, among others). When users
  attempt to use an Amazon Q Business web experience, Amazon Q Apps authorizes
  their actions based on the user and group information it gathers from IAM Identity Center or
  IAM.

To set up IAM Identity Center, see [Enable single sign-on access to your AWS applications
(Application admin role)](../../../singlesignon/latest/userguide/use-case-app-admin.md "../../../singlesignon/latest/userguide/use-case-app-admin.md") in the _IAM Identity Center User
Guide_ . You need to complete this step before creating an Amazon Q Business application environment and using Amazon Q Apps. For a list of supported
enterprise identity providers and how to connect them to your IAM Identity Center instance,
see [Manage an external identity provider](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") in the
_IAM Identity Center User Guide_.

To set up AWS Identity and Access Management, see [Get
started with IAM](../../../IAM/latest/UserGuide/getting-started.md "../../../IAM/latest/UserGuide/getting-started.md") in the _AWS Identity and Access Management User Guide_.
You need to complete setting up and connecting an identity provider to an IAM
instance before creating an Amazon Q Business application environment and using
Amazon Q Apps. For a list of supported enterprise identity providers and how to
connect them to your IAM instance, see [Identity providers and federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md") in the _AWS Identity and Access Management User
Guide_. For an example of how to set up an Amazon Q Business
application environment with IAM federation using Okta as an example, see
[Configuring an Amazon Q Business application
using IAM Federation](create-application-iam.md "create-application-iam.md").

###### Important

As of July 1, 2024, Amazon Q Apps are available only to
[Amazon Q Business Pro users](tiers.md#managing-sub-tiers "tiers.md#managing-sub-tiers"). Amazon Q Business Lite users will no longer be able to
create, run, or view Q Apps. To access, Q Apps, Lite users must upgrade to Amazon Q Business Pro.

As of August 30, 2024, all Amazon Q Apps created by Lite
users who did not upgrade their account to Amazon Q Business Pro have been deleted.

- **Finish the Amazon Q Business setup**
  – Complete [setting up Amazon Q Business](../business-use-dg/setting-up.md "../business-use-dg/setting-up.md") and create an Amazon Q Business
  application environment integrated with either [IAM Identity Center](create-application.md "create-application.md") or [AWS Identity and Access Management](create-application-iam.md "create-application-iam.md"). Configuring the application environment is
  necessary so that you can allow users to manage their own Amazon Q Apps. Also,
  include a retriever and, optionally, a data source connector.
- **Create an IAM role** –
  Configure an AWS Identity and Access Management (IAM) access role
  (permissions policy) for the deployed web experience for your broader
  application environment, including permissions for Amazon Q Apps. The admin can use the
  Amazon Q Business console to create the required IAM
  role for users as part of the configuration steps. To view and modify the
  required IAM access role with set permissions and [optional permissions for web experience users to
  view and specify approved data sources](deploy-experience-iam-role.md#deploy-data-source-iam-permissions "deploy-experience-iam-role.md#deploy-data-source-iam-permissions") with Amazon Q Apps, see the
  [IAM role for web experience users](deploy-experience-iam-role.md "deploy-experience-iam-role.md").

###### Note

If you are using permissions for Amazon Q Apps created prior to July 10, 2024,
you must update your role with the new [Amazon Q Apps](deploy-q-apps-iam-permissions.md "deploy-q-apps-iam-permissions.md") permissions for your users
to have access to use the [permissions
to view and specify approved data sources](deploy-q-apps-iam-permissions.md#deploy-data-source-iam-permissions "deploy-q-apps-iam-permissions.md#deploy-data-source-iam-permissions") and other future features in Q Apps.

- **Quotas**
  _(formerly known as limits)_ — There are set maximum
  quotas for Amazon Q Apps. For information about these quotas, see [Quotas](quotas-regions.md#limits "quotas-regions.md#limits").
