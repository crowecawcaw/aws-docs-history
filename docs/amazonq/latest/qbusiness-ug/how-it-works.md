# How Amazon Q Business works

With Amazon Q Business, you can build an interactive chat application environment for your
organization’s end users, using a combination of your enterprise data and large language
model knowledge, or enterprise data only. The following sections outline how Amazon Q works.

###### Topics

- [Admin workflow](#admin-flow "#admin-flow")
- [User workflow](#user-flow "#user-flow")
- [Amazon Q Business workflow](#app-flow "#app-flow")

## Admin workflow

Amazon Q Business uses AWS IAM Identity Center to connect to your workforce users. [Identity Federation through IAM](../../../IAM/latest/UserGuide/id_roles_providers.md#id_roles_providers_iam "../../../IAM/latest/UserGuide/id_roles_providers.md#id_roles_providers_iam") is also supported,
with the limitations described below. If you're an admin user configuring an Amazon Q Business application, your application creation process depends on whether
you're using IAM Identity Center or AWS Identity and Access Management for end user access management.

**If IAM Identity Center is already enabled** in your organization,
Amazon Q Business will automatically identify it and allow you to connect to
it. IAM Identity Center will enable you to manage access based on the users and groups in your
corporate directory. It will provide you with accurate billing for the subscriptions of
your users and will ensure that your configuration can support the future growth of your
Amazon Q Business use cases.

**If IAM Identity Center is not yet enabled**, we strongly recommend
that you work with your AWS Administrator to [enable an organization instance of IAM Identity Center](idc-setup.md#idc-org-account-setup "idc-setup.md#idc-org-account-setup"). This will
give your AWS Administrator the most control over the configuration. It will ensure
accurate billing for the subscriptions of your users. It will also give you the most
flexibility to grow Amazon Q Business use cases, spanning multiple AWS accounts,
users, and integrations with other AWS applications. If your AWS Administrator
cannot enable an organization instance of IAM Identity Center, you can [enable an account instance of IAM Identity Center](idc-setup.md#idc-account-instance-setup "idc-setup.md#idc-account-instance-setup") by yourself through
the Amazon Q Business console. Your deployment of Amazon Q Business, and its
integration with other AWS applications, will be limited to the AWS Region and AWS
account where the IAM Identity Center account instance is enabled.

###### Note

If you have Amazon Q Business deployments with account instances of IAM Identity Center in
multiple AWS accounts, you will be billed separately for user subscriptions per
AWS account. For more information, see [Understanding user subscriptions](tiers.md#managing-sub-tiers "tiers.md#managing-sub-tiers").

**If you cannot use any IAM Identity Center option**, you can still set
up Amazon Q Business using IAM Federation through OIDC (preferred) or SAML. This
approach will give your users access to Amazon Q Business capabilities, but will
limit your ability to scale Amazon Q Business use cases via integration with other
AWS applications.

###### Note

If you have Amazon Q Business deployments with IAM federation to multiple
AWS accounts, you will be billed separately for user subscriptions per AWS
account. For more information, see [Understanding user subscriptions](tiers.md#managing-sub-tiers "tiers.md#managing-sub-tiers").

The following section outlines the admin workflow for creating applications with IAM Identity Center
and Identity Federation through IAM.

###### Topics

- [Admin workflow for apps using AWS IAM Identity Center](#admin-flow-idc "#admin-flow-idc")
- [Admin workflow for apps using Identity Federation through IAM](#admin-flow-iam "#admin-flow-iam")

### Admin workflow for apps using AWS IAM Identity Center

Amazon Q Business supports managing end user access to applications using
AWS IAM Identity Center. When you use AWS IAM Identity Center to manage users, you sync user identities into
IAM Identity Center and connect your Amazon Q Business to IAM Identity Center to manage user
access.

As an admin user using IAM Identity Center for user management—including integrating an
external identity provider to manage user access through IAM Identity Center—you create and
configure an Amazon Q Business application environment by completing the following
steps:

1. [Enabling an IAM Identity Center instance](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") and [connecting the identity source](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md") for your Amazon Q Business
   application environment in IAM Identity Center. Amazon Q Business supports both organization and account
   level IAM Identity Center instances.
2. [Connecting an IAM Identity Center instance](idc-setup.md "idc-setup.md") for your
   Amazon Q Business application environment with users and groups
   added.
3. [Creating a fully-configured Amazon Q Business
   application](create-application.md "create-application.md") that powers your web experience, connected to
   IAM Identity Center.

If you use the console to create an application environment, Amazon Q Business
automatically creates a web experience for you, unless you choose not to. If
you use the API, you have to create a web experience for your
application environment.

###### Note

When you create an application, you can optionally add groups and
users who will be able to access the Amazon Q Business web
experience, and then provision the user subscriptions. Or, you can add
groups and users when you update your application. An Amazon Q
application environment will be created even if you don't add users to it, but an
application environment needs to have a subscribed user to work.

###### Important

Only an admin can create and upgrade user subscriptions. 4. (Optional) [Enhancing the web experience](../business-use-dg/enhancements.md "../business-use-dg/enhancements.md") by adding data
sources to it, configuring admin-level controls, tuning chat relevance,
plugins, and chat features (including Amazon Q Apps) for end users. For more
information, see [Enhancing an Amazon Q Business
application environment](../business-use-dg/enhancements.md "../business-use-dg/enhancements.md") and [Amazon Q Business features](../business-use-dg/features.md "../business-use-dg/features.md"). 5. (Optional) [Customizing your web experience](customizing-web-experience.md "customizing-web-experience.md") to test how
it looks for your end users. In this step, you add a title and subtitle for
your web experience, a welcome message, and [quick prompts](quick-prompts.md "quick-prompts.md") for your end users. You can't
chat with—or test—the application environment in customize mode. 6. Then, share the web experience URL generated by Amazon Q Business
with the end users you've subscribed so that they can log in and begin
chatting.

###### Note

When you create an application, response generation from large
language model (LLM) knowledge is enabled by default.

### Admin workflow for apps using Identity Federation through IAM

Amazon Q Business supports managing end user access to applications using
[Identity Federation through IAM](../../../IAM/latest/UserGuide/id_roles_providers.md#id_roles_providers_iam "../../../IAM/latest/UserGuide/id_roles_providers.md#id_roles_providers_iam"). When you use
IAM Identity Federation to manage users, your application derives user identities
directly from your identity provider. As an admin, you create and configure a
Amazon Q Business application environment using IAM Identity Federation by
completing the following steps:

1. Configuring your external identity provider and connecting it to an
   AWS Identity and Access Management identity provider instance.
2. [Creating a fully-configured Amazon Q Business
   application](create-application-iam.md "create-application-iam.md") that powers your web experience, connected to your
   identity provider through IAM. You also add subscriptions for end users by
   adding subscriptions when you create an application.
3. (Optional) [Enhancing the web experience](../business-use-dg/enhancements.md "../business-use-dg/enhancements.md") by adding a
   data source, configuring admin-level controls, tuning chat relevance,
   plugins, and chat features (including Amazon Q Apps) for end users. For more
   information, see [Enhancing an Amazon Q Business
   application environment](../business-use-dg/enhancements.md "../business-use-dg/enhancements.md") and [Amazon Q Business features](../business-use-dg/features.md "../business-use-dg/features.md").
4. Optionally, [customizing your web experience](customizing-web-experience-iam.md "customizing-web-experience-iam.md") to test how
   it looks for your end users. In this step, you add a title and subtitle for
   your web experience, a welcome message, and [quick prompts](quick-prompts.md "quick-prompts.md") for your end users. You can't
   chat with—or test—the application environment in customize mode.
5. Then, sharing either your own custom web application URL or the web
   experience URL generated by Amazon Q Business with the end users
   you've subscribed so that they can log in and begin chatting.

###### Note

When you create an application, response generation from large
language model (LLM) knowledge is enabled by default.

## User workflow

If you're an end user using your organization's Amazon Q Business web
experience, you perform the following steps:

1.  Navigate to your organization's Amazon Q Business web experience URL,
    and sign in with your credentials.
2.  Start chatting and ask questions of your organization's Amazon Q Business web experience. You can, for example choose from the following
    options:

        * **Ask questions** – Ask a
         question. Amazon Q Business generates and returns answers based on
         the enterprise data that the end user has access to. Continue the
         conversation by asking follow-up questions.
        * **Verify response sources** – Each
         Amazon Q Business answer cites the source documents used to
         generate it.
        * **See conversation history** –
         Amazon Q Business retains conversation history for 30 days so
         that they can search through questions and answers. You can view
         conversation history from the left navigation pane.
        * **Summarize content** – Amazon Q Business can summarize email message threads.
        * **Create outlines and drafts** –
         Use Amazon Q Business to create outlines and templates for
         documents.
        * **Perform plugin actions** – If
         you've configured [Plugins](plugins.md "plugins.md"), ask Amazon Q Business to
         perform actions on your behalf, like creating a ticket in a supported
         third party app.
        * **Test guardrails and chat controls**
         – If you've configured [Guardrails and chat controls](guardrails.md "guardrails.md"), check how
         Amazon Q Business responds to queries and special
         topics.
        * Additionally, you can ask Amazon Q Business to complete [any supported follow-up tasks](plugins.md "plugins.md")—like [creating task-focused Amazon Q
         Apps](purpose-built-qapps.md "purpose-built-qapps.md")—that your admin has enabled for your
         application environment.

    For a list of web experience capabilities, see [Using an Amazon Q web experience](using-web-experience.md "using-web-experience.md").

3.  Sometimes your question requires information that's beyond the scope of your
    enterprise data. Then, Amazon Q Business responds that it couldn't find an
    answer in your documents, unless your admin has allowed Amazon Q Business
    to [generate responses using model knowledge](guardrails.md "guardrails.md").

Amazon Q Business stores conversation history for 30 days and maintains
conversation context after a conversation ends. Conversations can be resumed from where
you left off within this 30-day period.

## Amazon Q Business workflow

In response to an end user query during a web experience chat, Amazon Q Business
does the following:

1. Uses the retriever chosen by the admin to select and retrieve documents that
   are relevant to the query, following authorization and access control.
2. Generates a response to the user query using either a combination of retrieved
   enterprise data and model knowledge, or only enterprise data, depending on admin
   configuration.
3. Returns the generated response to the end user. Amazon Q Business
   assigns a unique message ID to each answer for tracking purposes.
