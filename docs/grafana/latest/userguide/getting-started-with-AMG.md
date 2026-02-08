# Learn how to create and use Amazon Managed Grafana

resources

This tutorial helps you get started with Amazon Managed Grafana. Create your first
workspace, and then connect to the Grafana console in that workspace.

A _workspace_ is a logical Grafana server. You can have as many as five
workspaces in each Region in your account.

###### Note

If you do not have an AWS account, start by learning how to
[Set up AWS to use
Amazon Managed Grafana](Amazon-Managed-Grafana-setting-up.md "Amazon-Managed-Grafana-setting-up.md").

###### Topics

- [User
  authentication](#AMG-getting-started-workspace-authentication "#AMG-getting-started-workspace-authentication")
- [Necessary
  permissions](#AMG-getting-started-workspace-permissions "#AMG-getting-started-workspace-permissions")
- [Create your first
  workspace](#AMG-getting-started-workspace-create "#AMG-getting-started-workspace-create")
- [Set up AWS to use Amazon Managed Grafana](Amazon-Managed-Grafana-setting-up.md "Amazon-Managed-Grafana-setting-up.md")

## User

authentication

For user authentication within your workspaces, Amazon Managed Grafana supports the following
options:

- User credentials stored in identity providers (IdPs), with authentication by
  Security Assertion Markup Language 2.0 (SAML 2.0)
- AWS IAM Identity Center

**SAML**

If you use SAML, your users must already be created in an identity provider. Amazon Managed Grafana
supports identity providers that support SAML 2.0. For more information, see [Use SAML with your Amazon Managed Grafana
workspace](authentication-in-AMG-SAML.md "authentication-in-AMG-SAML.md").

**AWS IAM Identity Center**

When you create a workspace and choose to use AWS IAM Identity Center for authentication, Amazon Managed Grafana
activates IAM Identity Center in your account if you are not already using it. For more information
about IAM Identity Center, see [What is AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md").

To use IAM Identity Center with Amazon Managed Grafana, you must also have AWS Organizations activated in your account. If
you don't have it activated already, Amazon Managed Grafana activates it when it activates IAM Identity Center. If
Amazon Managed Grafana enables Organizations, it also creates an organization for you. For more information
about Organizations, see [What is
AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md").

###### Note

To create a workspace in an account that is already a member of an AWS
organization, IAM Identity Center must be enabled in the management account of the organization.
If you enabled IAM Identity Center in the management account before November 25, 2019, you must
also enable IAM Identity Center-integrated applications in the management account. For more
information, see [IAM Identity Center-integrated
applications](../../../singlesignon/latest/userguide/awsapps.md "../../../singlesignon/latest/userguide/awsapps.md").

## Necessary

permissions

To create a workspace that uses an IdP and SAML for authorization, you must be signed
on to an IAM principal that has the
**AWSGrafanaAccountAdministrator** policy attached.

To create your first workspace that uses AWS IAM Identity Center for authorization, you must be
signed on to an IAM principal that has at least the following policies
attached:

- **AWSGrafanaAccountAdministrator**
- **AWSSSOMemberAccountAdministrator**
- **AWSSSODirectoryAdministrator**

For more information, see [Create and manage Amazon Managed Grafana workspaces and users in a single standalone
account using IAM Identity Center](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-workspace-standalone "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-create-workspace-standalone").

## Create your first

workspace

Use the following steps to create your first workspace.

###### To create a workspace in Amazon Managed Grafana

1. Open the Amazon Managed Grafana console at [https://console.aws.amazon.com/grafana/](https://console.aws.amazon.com/grafana/home/ "https://console.aws.amazon.com/grafana/home/").
2. Choose **Create workspace**.
3. For **Workspace name**, enter a name for the
   workspace.

Optionally, enter a description for the workspace. 4. Choose **Next**. 5. For **Authentication access**, select **AWS IAM Identity Center** , **Security Assertion Markup Language (SAML)**, or
both.

    * **AWS IAM Identity Center**— If you select IAM Identity Center
     and you have not already enabled IAM Identity Center in your account, you are prompted
     to enable it by creating your first IAM Identity Center user. IAM Identity Center handles user
     management for access to Amazon Managed Grafana workspaces.


    To enable IAM Identity Center, follow these steps:
    1. Choose **Create user**.
    2. Enter an email address, first name, and last name for the user, and
     choose **Create user**. For this tutorial, use the name
     and email address of the account that you want to use to try out
     Amazon Managed Grafana. An email message is sent, prompting you to create a password
     for this account for IAM Identity Center.###### Important

The user that you create does not automatically have access to your
Amazon Managed Grafana workspace. You provide the user with access to the workspace in
the workspace details page in a later step.

    * **SAML**— If you select
     **SAML**, you complete the SAML setup after the
     workspace is created.

6. Choose **Next**.
7. For this first workspace, confirm that **Service managed** is
   selected for **Permission type**. This selection enables
   Amazon Managed Grafana to automatically provision the permissions you need for the AWS data
   sources that you choose to use for this workspace.
8. For this tutorial, choose **Current account**.
9. (Optional) Select the data sources that you want to query in this workspace.
   For this getting started tutorial, you do not need to select any data sources.
   However, if you plan to use this workspace with any of the listed data sources,
   select them here.

Selecting data sources enables Amazon Managed Grafana to create AWS Identity and Access Management (IAM) policies
for each of the data sources so that Amazon Managed Grafana has permission to read their
data. This does not completely set up these services as data sources for the
Grafana workspace. You can do that within the Grafana workspace console. 10. (Optional) If you want Grafana alerts from this workspace to be sent to an
Amazon Simple Notification Service (Amazon SNS) notification channel, select **Amazon SNS**.
This enables Amazon Managed Grafana to create an IAM policy to publish to the Amazon SNS topics
in your account with `TopicName` values that start with
`grafana`. This does not completely set up Amazon SNS as a
notification channel for the workspace. You can do that within the Grafana
console in the workspace. 11. (Optional) By default, Amazon Managed Grafana automatically provides you with encryption at rest and does this using AWS-owned encryption keys. But you have the option to use a customer managed key that you create, own, and manage as an alternative. For more information, see [Encryption at rest](AMG-encryption-at-rest.md "AMG-encryption-at-rest.md"). 12. Choose **Next**. 13. Confirm the workspace details, and choose **Create
workspace**.

The workspace details page appears.

Initially, the **Status** is
**CREATING**.

###### Important

Wait until the status is **ACTIVE** before doing either
of the following:

    * Completing the SAML setup, if you are using SAML.
    * Assigning your IAM Identity Center users access to the workspace, if you are
     using IAM Identity Center.You might need to refresh your browser to see the current status.

14. If you are using IAM Identity Center, do the following:
    1.  In the **Authentication** tab, choose
        **Assign new user or group**.
    2.  Select the check box next to the user that you want to grant workspace
        access to, and choose **Assign user**.
    3.  Select the check box next to the user, and choose **Make
        admin** action from the Actions dropdown list.

    ###### Important

    Assign at least one user as `Admin` for each workspace,
    in order to sign in to the Grafana workspace console to manage the
    workspace.

15. If you are using SAML, do the following:
    1.  In the **Authentication** tab, under
        **Security Assertion Markup Language (SAML)**,
        choose **Complete setup**.
    2.  For **Import method**, do one of the
        following:
        - Choose **URL** and enter the URL of the IdP
          metadata.
        - Choose **Upload or copy/paste**. If you are
          uploading the metadata, choose **Choose file**
          and select the metadata file. Or, if you are using copy and
          paste, copy the metadata into **Import the
          metadata**.

    3.  For **Assertion attribute role**, enter the name of
        the SAML assertion attribute from which to extract role
        information.
    4.  For **Admin role values**, either enter the user
        roles from your IdP who should all be granted the `Admin`
        role in the Amazon Managed Grafana workspace, or select **I want to opt-out
        of assigning admins to my workspace.**

    ###### Note

    If you choose **I want to opt-out of assigning admins to
    my workspace.**, you won't be able to use the Grafana
    workspace console to administer the workspace, including tasks such
    as managing data sources, users, and dashboard permissions. You can
    make administrative changes to the workspace only by using Grafana
    APIs. 5. (Optional) To enter additional SAML settings, choose
    **Additional settings** and do one or more the
    following. All of these fields are optional.

        * For **Assertion attribute name**, specify the
         name of the attribute within the SAML assertion to use for the
         user full "friendly" names for SAML users.
        * For **Assertion attribute login**, specify
         the name of the attribute within the SAML assertion to use for
         the user sign-in names for SAML users.
        * For **Assertion attribute email**, specify
         the name of the attribute within the SAML assertion to use for
         the user email names for SAML users.
        * For **Login validity duration (in minutes)**,
         specify how long a SAML user's sign-in is valid before the user
         must sign in again.
        * For **Assertion attribute organization**,
         specify the name of the attribute within the SAML assertion to
         use for the "friendly" name for user organizations.
        * For **Assertion attribute groups**, specify
         the name of the attribute within the SAML assertion to use for
         the "friendly" name for user groups.
        * For **Allowed organizations**, you can limit
         user access to only the users who are members of certain
         organizations in the IdP. Enter one or more organizations to
         allow, separating them with commas.
        * For **Editor role values**, enter the user
         roles from your IdP who should all be granted the
         `Editor` role in the Amazon Managed Grafana workspace. Enter
         one or more roles, separated by commas.

    ###### Note

    Any users that are not specifically assigned an Admin or Editor
    role are assigned as Viewers. 6. Choose **Save SAML configuration**.

16. In the workspace details page, choose the URL displayed under
    **Grafana workspace URL**.
17. Choosing the workspace URL takes you to the landing page for the Grafana
    workspace console. Do one of the following:
    - Choose **Sign in with SAML**, and enter the name and
      password.
    - Choose **Sign in with AWS IAM Identity Center**, and enter the
      email address and password of the user that you created earlier in this
      procedure. These credentials only work if you have responded to the
      email from Amazon Managed Grafana that prompted you to create a password for
      IAM Identity Center.

    You are now in your Grafana workspace, or logical Grafana server. You
    can start adding data sources to query, visualize, and analyze data. For
    more information, see [Use your Grafana
    workspace](AMG-working-with-Grafana-workspace.md "AMG-working-with-Grafana-workspace.md").
