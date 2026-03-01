# Configuring an Amazon Q Business application to use the plugin

You configure an Amazon Q Business application to get insights from Quick answers in
different ways depending on whether you have a Quick account.

- If you don't have a Quick account, you can create one in the Amazon Q Business
  console, and then authorize Amazon Q Business to communicate with Quick.
- If you already have a Quick account, you use the Amazon Q Business console or
  APIs to authorize Amazon Q Business to communicate with Amazon Quick.
  After you configure your application, you create Quick datasets, and create and
  share Quick topics. Users can also get insights from Quick dashboards.

- You can create datasets from new or existing data sources in Amazon Quick. You can
  use a variety of database data sources to provide data to Amazon Quick. For more
  information, see [Creating
  datasets](../../../quicksight/latest/user/creating-data-sets.md "../../../quicksight/latest/user/creating-data-sets.md").
- Quick _topics_ are collections of one or more datasets
  that represent a subject area that your business users can ask questions about.
  For more information, see [Working with Amazon Quick
  Q topics](../../../quicksight/latest/user/quicksight-q-topics.md "../../../quicksight/latest/user/quicksight-q-topics.md").
- A Quick _dashboard_ is a read-only snapshot of an
  analysis that you can share with other Amazon Quick users for reporting purposes.
  For more information, see [Sharing and
  subscribing to data in Amazon Quick](../../../quicksight/latest/user/working-with-dashboards.md "../../../quicksight/latest/user/working-with-dashboards.md").

###### Topics

- [Creating a new Amazon Quick account in the Amazon Q Business console](#quicksight-plugin-creating-new-qs-account "#quicksight-plugin-creating-new-qs-account")
- [Linking an existing Quick account](#quicksight-plugin-linking-existing-account "#quicksight-plugin-linking-existing-account")

## Creating a new Amazon Quick account in the Amazon Q Business console

If you don't have an existing Quick account, you can use the Amazon Q Business
console to create one and link the two accounts. Then you configure your Quick
resources to start getting insights.

###### To link a new Quick account

1. Log in to the Amazon Q Business console.
2. In **Applications**, choose the name of your application
   from the list of applications.
3. In the navigation pane, choose **Amazon Quick**.
4. Choose **Create Quick Account**.
5. Give your new account a name, and specify the email address to use for
   account notifications.
6. Optionally, specify an email for product updates.
7. In **Assign Quick Admin Pro role**, choose the IAM Identity Center
   groups to assign the Quick Admin Pro role, and choose
   **Next**.
8. In **Service access**, create a new service role or use
   an existing one. This role authorizes Amazon Q Business to communicate with
   Amazon Quick. For more information, see [Service access role](quicksight-plugin.md#quicksight-plugin-service-access-role "quicksight-plugin.md#quicksight-plugin-service-access-role").
9. Choose **Authorize**.
10. Choose **Go to Quick** to go to your Quick
    account. There you create datasets, create and share Quick topics, and
    optionally create, publish, and share dashboards. After you configure these
    resources, end users start getting insights with Quick answers.

## Linking an existing Quick account

If you have an existing Quick account that uses AWS IAM Identity Center for authentication,
you can authorize Amazon Q Business to communicate with Amazon Quick in the console or with
the Amazon Q Business API. Then end users can start getting insights from new and existing
Quick topics and dashboards.

If you have an existing Quick account that uses AWS IAM Identity Center for
authentication, you can start getting insights after you authorize
Amazon Q Business to communicate with Amazon Quick. To authorize Amazon Q Business, you
use the Amazon Q Business console to assign IAM Identity Center groups the Admin Pro role.
Then you specify a service role that grants Amazon Q Business access.

###### To link an existing Quick account

1. Log in to the Amazon Q Business console.
2. Choose your application.
3. In the navigation pane, choose
   **Amazon Quick**.
4. Choose **Authorize Quick answers**.
5. In **Assign Quick Admin Pro role**, choose
   the IAM Identity Center groups to assign the Admin Pro role. The Quick Admin
   Pro role includes additional costs. For more information, see
   Amazon Quick pricing.
6. In **Service access**, create a new service role
   or use an existing one. This role authorizes Amazon Q Business to
   communicate with Amazon Quick. For more information, see [Service access role](quicksight-plugin.md#quicksight-plugin-service-access-role "quicksight-plugin.md#quicksight-plugin-service-access-role").
7. Choose **Authorize**. After you authorize the
   connection, end users start getting insights from existing Quick
   resources.
8. To get insights from additional structured data resources, choose
   **Go to Quick** to go to your Quick
   account. There you can create additional datasets, topics, and
   dashboards.
   To authorize Amazon Q Business with the API, you first use IAM Identity Center to assign
   groups the Admin Pro role. Also, if your Quick account was created
   before November 25, 2024 and uses IdC authentication, use the [UpdateApplicationWithTokenExchangeGrant](../../../quicksight/latest/APIReference/API_UpdateApplicationWithTokenExchangeGrant.md "../../../quicksight/latest/APIReference/API_UpdateApplicationWithTokenExchangeGrant.md") API to update your
   subscription to allow integration with Amazon Q Business Then you use the [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md") API operation to create a Quick plugin for an
   Amazon Q Business application.

The following code shows how to create a Quick plugin. For
`idcApplicationArn`, specify the Amazon Resource Name
(ARN) of your application in IAM Identity Center. For `roleArn`, specify
an AWS Identity and Access Management (IAM) role that authorizes Amazon Q Business to communicate with
Amazon Quick. For more information about this role, see [Service access role](quicksight-plugin.md#quicksight-plugin-service-access-role "quicksight-plugin.md#quicksight-plugin-service-access-role").

```
aws qbusiness create-plugin \
--application-id `application-id` \
--display-name `display-name` \
--type QUICKSIGHT \
--auth-configuration idcAuthConfiguration="{idcApplicationArn=arn:aws:sso::<account-id>:application/<application-id>,roleArn=arn:aws:iam::<account-id>:role/AmazonQServiceRole}"
```
