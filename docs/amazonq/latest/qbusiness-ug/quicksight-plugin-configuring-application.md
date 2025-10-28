# Configuring an Amazon Q Business

application to use the plugin

You configure an Amazon Q Business application to get insights from Quick Suite answers in
different ways depending on whether you have a Quick Suite account.

- If you don't have a Quick Suite account, you can create one in the Amazon Q Business
  console, and then authorize Amazon Q Business to communicate with Quick Suite.
- If you already have a Quick Suite account, you use the Amazon Q Business console or
  APIs to authorize Amazon Q Business to communicate with Amazon Quick Suite.
  After you configure your application, you create Quick Suite datasets, and create and
  share Quick Suite topics. Users can also get insights from Quick Suite dashboards.

- You can create datasets from new or existing data sources in Amazon Quick Suite. You can
  use a variety of database data sources to provide data to Amazon Quick Suite. For more
  information, see [Creating
  datasets](../../../quicksight/latest/user/creating-data-sets.md "../../../quicksight/latest/user/creating-data-sets.md").
- Quick Suite _topics_ are collections of one or more datasets
  that represent a subject area that your business users can ask questions about.
  For more information, see [Working with Amazon Quick Suite
  Q topics](../../../quicksight/latest/user/quicksight-q-topics.md "../../../quicksight/latest/user/quicksight-q-topics.md").
- A Quick Suite _dashboard_ is a read-only snapshot of an
  analysis that you can share with other Amazon Quick Suite users for reporting purposes.
  For more information, see [Sharing and
  subscribing to data in Amazon Quick Suite](../../../quicksight/latest/user/working-with-dashboards.md "../../../quicksight/latest/user/working-with-dashboards.md").

###### Topics

- [Creating a new Amazon Quick Suite
  account in the Amazon Q Business console](#quicksight-plugin-creating-new-qs-account "#quicksight-plugin-creating-new-qs-account")
- [Linking an existing
  Quick Suite account](#quicksight-plugin-linking-existing-account "#quicksight-plugin-linking-existing-account")

## Creating a new Amazon Quick Suite

account in the Amazon Q Business console

If you don't have an existing Quick Suite account, you can use the Amazon Q Business
console to create one and link the two accounts. Then you configure your Quick Suite
resources to start getting insights.

###### To link a new Quick Suite account

1. Log in to the Amazon Q Business console.
2. In **Applications**, choose the name of your application
   from the list of applications.
3. In the navigation pane, choose **Amazon Quick Suite**.
4. Choose **Create Quick Suite Account**.
5. Give your new account a name, and specify the email address to use for
   account notifications.
6. Optionally, specify an email for product updates.
7. In **Assign Quick Suite Admin Pro role**, choose the IAM Identity Center
   groups to assign the Quick Suite Admin Pro role, and choose
   **Next**.
8. In **Service access**, create a new service role or use
   an existing one. This role authorizes Amazon Q Business to communicate with
   Amazon Quick Suite. For more information, see [Service access role](quicksight-plugin.md#quicksight-plugin-service-access-role "quicksight-plugin.md#quicksight-plugin-service-access-role").
9. Choose **Authorize**.
10. Choose **Go to Quick Suite** to go to your Quick Suite
    account. There you create datasets, create and share Quick Suite topics, and
    optionally create, publish, and share dashboards. After you configure these
    resources, end users start getting insights with Quick Suite answers.

## Linking an existing

Quick Suite account

If you have an existing Quick Suite account that uses AWS IAM Identity Center for authentication,
you can authorize Amazon Q Business to communicate with Amazon Quick Suite in the console or with
the Amazon Q Business API. Then end users can start getting insights from new and existing
Quick Suite topics and dashboards.

If you have an existing Quick Suite account that uses AWS IAM Identity Center for
authentication, you can start getting insights after you authorize
Amazon Q Business to communicate with Amazon Quick Suite. To authorize Amazon Q Business, you
use the Amazon Q Business console to assign IAM Identity Center groups the Admin Pro role.
Then you specify a service role that grants Amazon Q Business access.

###### To link an existing Quick Suite account

1. Log in to the Amazon Q Business console.
2. Choose your application.
3. In the navigation pane, choose
   **Amazon Quick Suite**.
4. Choose **Authorize Quick Suite answers**.
5. In **Assign Quick Suite Admin Pro role**, choose
   the IAM Identity Center groups to assign the Admin Pro role. The Quick Suite Admin
   Pro role includes additional costs. For more information, see
   Amazon Quick Suite pricing.
6. In **Service access**, create a new service role
   or use an existing one. This role authorizes Amazon Q Business to
   communicate with Amazon Quick Suite. For more information, see [Service access role](quicksight-plugin.md#quicksight-plugin-service-access-role "quicksight-plugin.md#quicksight-plugin-service-access-role").
7. Choose **Authorize**. After you authorize the
   connection, end users start getting insights from existing Quick Suite
   resources.
8. To get insights from additional structured data resources, choose
   **Go to Quick Suite** to go to your Quick Suite
   account. There you can create additional datasets, topics, and
   dashboards.
   To authorize Amazon Q Business with the API, you first use IAM Identity Center to assign
   groups the Admin Pro role. Also, if your Quick Suite account was created
   before November 25, 2024 and uses IdC authentication, use the [UpdateApplicationWithTokenExchangeGrant](../../../quicksight/latest/APIReference/API_UpdateApplicationWithTokenExchangeGrant.md "../../../quicksight/latest/APIReference/API_UpdateApplicationWithTokenExchangeGrant.md") API to update your
   subscription to allow integration with Amazon Q Business Then you use the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation to create a Quick Suite plugin for an
   Amazon Q Business application.

The following code shows how to create a Quick Suite plugin. For
`idcApplicationArn`, specify the Amazon Resource Name
(ARN) of your application in IAM Identity Center. For `roleArn`, specify
an AWS Identity and Access Management (IAM) role that authorizes Amazon Q Business to communicate with
Amazon Quick Suite. For more information about this role, see [Service access role](quicksight-plugin.md#quicksight-plugin-service-access-role "quicksight-plugin.md#quicksight-plugin-service-access-role").

```
aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type QUICKSIGHT \
--auth-configuration idcAuthConfiguration="{idcApplicationArn=arn:aws:sso::<account-id>:application/<application-id>,roleArn=arn:aws:iam::<account-id>:role/AmazonQServiceRole}"
```
