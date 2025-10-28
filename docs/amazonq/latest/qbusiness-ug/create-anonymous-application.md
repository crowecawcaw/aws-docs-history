# Creating an Amazon Q Business

application environment for anonymous access

Amazon Q Business application environments support anonymous access, enabling unauthenticated
user interactions with the Amazon Q generative AI assistant. You can also make
selected enterprise data accessible to users without requiring credentials, such as website
visitors seeking product information or support. This can be integrated through:

- Embedding the web experience URL in an iframe for quick deployment
- Using the `Chat`, `ChatSync`, and `PutFeedback`
  APIs to build custom interfaces
  Billing for anonymous access application environments is based on usage. For more information, see
  [Amazon Q Business
  pricing](https://aws.amazon.com/q/business/pricing/ "https://aws.amazon.com/q/business/pricing/").

###### Important

**Limitations of anonymous application environments**

- You can create your anonymous application environment using Amazon Q Business
  Console, API, SDK, and AWS CLI. You can only use the application environment with the chat
  APIs. The following are the only chat APIs that support anonymous access
  application environments.
  - `Chat`
  - `ChatSync`
  - `PutFeedback`

- The web experience is only available for preview and testing purposes unless
  used within the context of an Amazon Q embedded implementation. For
  more information, see [Amazon Q embedded](embed-amazon-q-business.md "embed-amazon-q-business.md").
- The GetDocumentContent API is not available for anonymous applications, consistent with other APIs such as GetMedia that require authentication.
- Chat history is not available for anonymous application environments
- Anonymous users and authenticated users are not supported on the same
  application environments
- Topic rules using users and groups are not supported for anonymous
  application environments
- Plugins are not supported for anonymous application environments
- Amazon Q Apps are not supported for anonymous application environments
- Attachments are not supported for anonymous application environments
- Admin controls and guardrails are read-only for anonymous application environments,
  except for [blocked words](guardrails-global-controls.md#guardrails-global-blocked "guardrails-global-controls.md#guardrails-global-blocked").
- Amazon Q Business integrations are not supported for anonymous
  application environments
- The Amazon Q Quick Suite integration is not supported for anonymous
  application environments
- You must only ingest publicly available data sources without access control
  lists (ACLs). Examples of public data sources include:

      + any data from the Amazon Q Business Web Crawler
      + S3 data without Amazon Q Business ACLs

  All other Amazon Q Business functionality and features remain unchanged.

###### Topics

- [Creating an a Amazon Q Business
  application environment for anonymous access](#create-anonymous-app "#create-anonymous-app")
- [Making
  authenticated Amazon Q Business API calls for application environment supporting
  anonymous access](making-sigv4-authenticated-api-calls-anonymous-applications.md "making-sigv4-authenticated-api-calls-anonymous-applications.md")
- [Managing resources for Amazon Q Business application environments that support anonymous access](managing-anonymous-app-resources.md "managing-anonymous-app-resources.md")

## Creating an a Amazon Q Business

application environment for anonymous access

You can create an Amazon Q Business application environment that can be accessed
anonymously using the Amazon Q Business Console, API, SDK, and AWS CLI. As a
prerequisite, you must complete the [setting up](setting-up.md "setting-up.md") tasks. If
you're using the AWS CLI or the API, you must create the required [IAM
roles](setting-up.md "setting-up.md").

The following tabs provide a procedure for creating your Amazon Q Business
application environment with anonymous access using the Amazon Q Business console; and an
example using the AWS CLI.

Console
**To create an anonymous access
application environment**

1. Sign in to the Amazon Q Business console.
2. On the **Create application environment** page, for
   **What kind of application environment do you want to
   create?**, enter the following information for your
   Amazon Q Business application environment:
   1. **Application name** – A name for
      your Amazon Q Business application environment for easy
      identification. This name is only visible in the AWS Management Console.
      The name can include hyphens (-), but not spaces, and can
      have a maximum of 1,000 alphanumeric characters. Amazon Q Business auto-generates an application environment name for
      you, unless you choose to enter a custom name.
   2. **User Access** – Choose
      **Anonymous access**, users can then
      access this application environment without authentication.

   ###### Note

   The web experience is only available for preview and
   testing purposes _unless_ used within
   the context of an Amazon Q embedded
   implementation. For more information, see [Amazon Q embedded](embed-amazon-q-business.md "embed-amazon-q-business.md"). If you want
   this capability, choose **Web
   experience**

3. For application environments with **Anonymous access**, you
   will be billed using usage based billing. For more information, see
   [Amazon Q Business pricing](https://aws.amazon.com/q/business/pricing/ "https://aws.amazon.com/q/business/pricing/").
4. For **Application details** – Amazon Q Business chooses the following configuration settings for
   your application environment by default:
   1. For **Application service access**
      – Amazon Q Business will create a new
      service-linked role for your application environment.
   2. **Encryption** – Amazon Q Business will create an AWS owned AWS KMS key to
      encrypt your data.

5. (Optional) To customize **Application details**,
   expand the **Application details section**, and
   then do the following:
   1. In **Application service access**, for
      **Choose a method to authorize Amazon Q Business**, choose from the
      following options:
      1. **Create and use a new service-linked role
         (SLR)** – Create and use a new
         Amazon Q Business-managed IAM role to
         allow it to access the AWS resources
         it needs to create your application environment.
      2. **Create and use a new service role
         (SR)** – Create and use a new
         IAM role for Amazon Q Business to allow it to access the AWS
         resources it needs to create your
         application environment.
      3. **Use an existing service role
         (SR)/service-linked role (SLR)** –
         Use an existing service role or service-linked
         IAM role to allow Amazon Q Business to access the AWS
         resources it needs to create your
         application environment.

      ###### Note

      For more information about example service
      roles, see [IAM role for an Amazon Q Business application](create-application-iam-role.md "create-application-iam-role.md"). For
      information on service-linked roles, including to
      manage them, see [Using service-linked
      roles](../business-use-dg/using-service-linked-roles.md "../business-use-dg/using-service-linked-roles.md"). 4. **Service role name** – A
      name for the service (IAM) role you
      created for easy identification on the
      console.

   2. For **Encryption** – Amazon Q Business encrypts your data by default using
      AWS managed AWS KMS keys. To customize your
      encryption settings, select **Customize encryption
      settings (advanced)**. Then, you can choose to
      use an existing AWS KMS key or create a new
      one.

6. For **Web experience service settings**, consider
   the following.
   1. **If you will use the web experience feature,
      choose a method to authorize Amazon Q Business** – A service access role assumed by
      your web experience that grants permission to have
      conversations anonymously. You can choose to use an existing
      role or create a new role.
   2. **Service role name** – A name for
      the service role you created for easy identification on the
      console.

7. To start creating your application environment, choose
   **Create**.

AWS CLI
**To configure an Amazon Q Business
application environment for anonymous access**

```

aws qbusiness create-application \
--region `your-region`
--display-name `application-name` \
--identity-type ANONYMOUS \
--role-arn `your-role-arn` \
--description `application-description` \
--encryption-configuration `kmsKeyId=<kms-key-id>` \

```

###### Note

The web experience is only available for preview and testing purposes
_unless_ used within the context of an Amazon Q embedded implementation. For more information, see
[Amazon Q embedded](embed-amazon-q-business.md "embed-amazon-q-business.md").

**To create an Amazon Q Business web
experience**

If you use the web experience, you must add the web experience permissions
and trust [IAM
policies](anonymous-application-iam-policies.md "anonymous-application-iam-policies.md") here.

```

aws qbusiness create-web-experience \
--application-id `the-application-id-from-the-previous-step` \
--role-arn `iam-role-created` \
--region `your-region` \

```
