# Setting up real-time notifications for AWS Partner Central and

AWS Marketplace events

The following topics explain how to set up real-time EventBridge
notifications for AWS Partner Central and AWS Marketplace events. You can set up notifications in Salesforce by configuring a connected app, or you can use AWS CloudFormation templates.

###### Topics

- [Configuring a Salesforce connected app](#configuring-salesforce-connected-app "#configuring-salesforce-connected-app")
- [Using an AWS CloudFormation stack to set up notifications](#configuring-aws-components "#configuring-aws-components")

## Configuring a Salesforce connected app

The following steps explain how to configure a connected app in Salesforce. You must
create a connected app in order to use OAuth authentication for destination connections. For
more information, refer to [Creating notification components manually](#manual-creation-of-aws-components "#manual-creation-of-aws-components"), later in this guide.

1. Sign in to your Salesforce organization as a system administrator.
2. From **Setup**, in the **Quick Find** box, enter `apps`, then select **App Manager**.
3. On the **Lightning Experience App Manager** page, choose **New Connected App**, choose **Create a Connected App**,
   then choose **Continue**.

The **New Connected App** page appears. 4. Do the following:

    1. In the **Connected App Name** box, enter a name for the app.
    2. In the **Contact Email** box, enter your email address.
    3. (Optional) Complete the remaining fields as described in
     [Configure Basic Connected App Settings](https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm "https://help.salesforce.com/s/articleView?id=sf.connected_app_create_basics.htm"),
     in the Salesforce documentation.

5. Select the **Enable OAuth Settings** checkbox, then
   do the following:
   1. Select the **Enable for Device Flow** checkbox. You can ignore the resulting callback URL.
   2. Under **Available OAuth Scopes**, select **Manage user data via
      APIs** and use the **Add** button to move the scope to the list of selected scopes.
   3. Select the following checkboxes:
      - **Require Proof Key for Code Exchange (PKCE) Extension for Supported Authorization Flows**
      - **Require Secret for Web Server Flow**
      - **Require Secret for Refresh Token Flow**
      - **Enable Client Credentials Flow**

   4. On the message that appears after you select **Enable Client Credentials Flow**, choose **OK**.
   5. Scroll to the bottom of the page and choose **Save**.

6. Choose **Continue**, then choose **Manage Consumer Details**.

The **Verify Your Identity** page appears, and the system sends a verification code to your contact email address. 7. Enter the verification code in the **Verification Code** box and
choose **Verify**.

The page for your connected app appears. 8. Under **Consumer Details**, choose the **Copy** buttons for the consumer key and customer secret. 9. From **Setup**, in the **Quick Find** box, enter **Apps**, select **Manage Connected Apps**,
then choose the connected app you just created. 10. Choose **Edit Policies**, then do the following:

    1. From the **Permitted Users** list, choose **All users may self authorize**.
    2. From the **IP Relaxation** list, choose **Enforce IP restrictions**.
    3. From the **Run As** list, select the *execution user*, the user to whom you assign the client credential flow.
     Salesforce requires the execution user to return access tokens on behalf of the user.
    4. Choose **Save**.

## Using an AWS CloudFormation stack to set up notifications

The following topics explain now to use AWS CloudFormation templates to set up real-time EventBridge notifications. The steps only apply to version 3.0 and later of the AWS Partner CRM connector.

For AWS Partner CRM connector version 3.0 and later, you can use an CloudFormation template to
configure the AWS Components for the Amazon EventBridge Integration, or you can create the components
manually. To use CloudFormation, download the templates from:

###### Topics

- [Finding your domain URL](#find-domain-url "#find-domain-url")
- [Using the CloudFormation stack](#downloading-templates "#downloading-templates")
- [Creating notification components manually](#manual-creation-of-aws-components "#manual-creation-of-aws-components")
- [Example rules](#example-rules "#example-rules")

### Finding your domain URL

The CloudFormation template uses your domain URL as one of its required parameters.

###### To find the URL

1. Sign in to Salesforce.
2. In the **Setup** section, in the **Quick Find** box, enter `my domain`.
3. In the left pane, under **Company Settings**, choose the **My Domain** link.
4. Copy the address in the **Current My Domain URL** box.

###### Note

You must use the https:// prefix when you enter the URL in the CloudFormation template.

### Using the CloudFormation stack

The steps in the following topics explain how to create and deploy a CloudFormation stack that sets up real-time notifications.

1. Download the following templates:

###### Note

You deploy each template separately, and you follow the same steps for both.

    * Partner Central API integration: [https://servicecatalogconnector.s3.amazonaws.com/APIDestinationCFT\_PCAPI.json](https://servicecatalogconnector.s3.amazonaws.com/APIDestinationCFT_PCAPI.json "https://servicecatalogconnector.s3.amazonaws.com/APIDestinationCFT_PCAPI.json")
    * (Optional) AWS Marketplace integration: [https://servicecatalogconnector.s3.amazonaws.com/APIDestinationCFT\_AWSMP.json](https://servicecatalogconnector.s3.amazonaws.com/APIDestinationCFT_AWSMP.json "https://servicecatalogconnector.s3.amazonaws.com/APIDestinationCFT_AWSMP.json")

2.  In the AWS Console, sign in to your AWS Marketplace seller account and ensure it runs in the **N. Virginia**. EventBridge only operates in that Region.
3.  Still in the console, search on `cloudformation`, then open the CloudFormation console.
4.  On the **Stacks** page, choose **Create stack**.
5.  Select the **Choose an existing template** and **Upload a template file** radio buttons.
6.  Select **Choose file** to open the downloaded template, then choose **Next**.
7.  On the **Specify stack details** page, enter the following:

        * **Stack name** – enter a name for the stack.
        * **Client ID** – Enter the consumer key you noted when creating the connected app.
        * **Client Secret** – Enter the consumer secret you noted when you created the connected app.
        * **Domain URL** – Use the following format: `https://`domain_URL`.`

    When finished, choose **Next**.

8.  On the **Configure stack options** page, scroll to the end, select the **I acknowledge that AWS CloudFormation might create IAM resources** checkbox, then choose **Next**.
9.  Choose **Submit**.

When deployed successfully, the templates create the API Destination, Connection, Event Rules, and Dead Letter Queue.

### Creating notification components manually

The following steps explain how to manually create the components for EventBridge notifications.

###### Topics

- [Create an Amazon EventBridge API destination and connection](#manual-destination-connection "#manual-destination-connection")
- [Creating an
  EventBridge Rule and connecting it to the API destination](#create-connect-ev-rule "#create-connect-ev-rule")
- [Creating change set events](#change-set-events "#change-set-events")
- [Creating Offer Released events](#offer-released-events "#offer-released-events")
- [Creating opportunity events](#opportunity-events "#opportunity-events")
- [Types of events](#types-of-events "#types-of-events")
- [Example event](#example-event "#example-event")

#### Create an Amazon EventBridge API destination and connection

To create an API destination and connection in EventBridge, create an API destination that uses a new connection. In this
case, the API destination is a REST API call to Salesforce to
publish an event back. The connection contains the
authentication information for the API call. The connection
accepts several authorization methods.

###### Prerequisites

To use OAuth authorization for the API destination connection, create a connected app
in Salesforce. To do so, follow the steps in [Configure a Connected App for the OAuth 2.0 Client Credentials Flow](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm "https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm"), in the
Salesforce documentation. You use the consumer key and secret from the connected app for
the API destination connection.

To create an API destination in the EventBridge console:

- Follow the steps in
  [Create
  an API destination](../../../eventbridge/latest/userguide/eb-api-destinations.md#eb-api-destination-create "../../../eventbridge/latest/userguide/eb-api-destinations.md#eb-api-destination-create") in the _Amazon EventBridge User Guide_.
- Set up the configurations that are specific to Salesforce.

In Salesforce, on the **My Domain** page, under
**Setup**, note your organizations domain name.
You use it to set up the API destination and connection in the EventBridge console. The following steps explain how.

###### To create the destination and connection

1. Open the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/"),
   and in the left navigation pane, choose **API destinations**.
2. Scroll down to the **API destinations** table and choose **Create API destination**.

The **Create API destination** page appears. 3. Enter the following information:

    1. A **Name** for the API destination. You can use up to 64 uppercase or lowercase letters, numbers,
     dots (.), dashes (-), or underscore (\_) characters.


    The name must be unique to your account in the current Region.
    2. (Optional) Enter a **Description** of the API destination.
    3. For **API destination endpoint**, use this URL:
     `https://`my-salesforce-domain-name`.my.salesforce.com/services/data/v58.0/sobjects/`event-api-name``.
    4. For **HTTP method**, select **POST**.

4.  Under **Connection configuration**, select **Create a new connection**, then do the following:
    1. Enter a name and optional description.
    2. For **Destination type**, choose **Other**.
    3. Choose **OAuth Client Credentials**.
    4. For **Authorization endpoint**, accept the prepopulated endpoint.

    —OR—

    if you use a production organization, replace the populated endpoint with this URL:

    `https://`my-salesforce-domain-name`.my.salesforce.com/services/oauth2/token` 5. For **HTTP method**, select **POST**. 6. For **Client ID**, enter the consumer key from the connected app in Salesforce. 7. For **Client secret**, enter the consumer secret from the connected app in Salesforce. 8. Add the following OAuth values:

        * **Parameter**: Body field
        * **Key**: grant\_type
        * **Value**: client\_credentials

5.  Choose **Create**.

###### Note

If your Salesforce organization uses multi-factor authentication
for API access, users must complete a second
authentication challenge to access the Salesforce APIs. For more
information, see
[Set
Multi-Factor Authentication Sign in Requirements for API
Access](https://help.salesforce.com/s/articleView?id=sf.security_require_2fa_api.htm&language=en_US&type=5 "https://help.salesforce.com/s/articleView?id=sf.security_require_2fa_api.htm&language=en_US&type=5") in the Salesforce documentation.

After you create the API destination, you can create a rule that uses the target as the destination.

#### Creating an

EventBridge Rule and connecting it to the API destination

EventBridge rules route events from the event bus to the API destination, which results in making a REST call to publish an event back to Salesforce.

For more information about EventBridge rules, see
[Creating
Amazon EventBridge rules that react to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.

#### Creating change set events

The following steps explain how to create change set events.

1. In [Amazon EventBridge](../../../marketplace/latest/userguide/seller-eventbridge.md#events-changesets "../../../marketplace/latest/userguide/seller-eventbridge.md#events-changesets"),
   choose **Rules**.
2. From the list, select the desired event bus.
3. In the **Rules** section,
   Choose **Create rule**.
4. Enter a name for the rule, then
   choose **Next**.
5. Under **Event pattern**, select **Custom patterns (JSON
   editor)** and enter the following filter. You can use any combination of detail types.

```
{
  "source": [
    "aws.marketplacecatalog"
  ],
  "detail-type": [
    "Change Set Succeeded",
    "Change Set Failed",
    "Change Set Cancelled"
  ]
}
```

For more information about event pattern matching, see
[Content
filtering in Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md "../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md") in the AWS
documentation. 6. Choose **Next**. 7. In **Select targets**, under
**Target 1**, select
**EventBridge API
destination**. 8. From the list, select the API destination that you just
created. 9. Expand **Additional
settings**. 10. Under **Configure Target
Input**, select **Input
Transformer** and **Configure
Input Transformer**. This ensures that only the
Salesforce event fields from the detail section of the
original event are sent.

The Input path must be: 

```
{
  "Name": "$.detail-type",
  "awsapn__Account_Number__c": "$.account",
  "awsapn__EntityId__c": "$.detail.ChangeSetId"
}
```

The template must be: 

```
{
  "Name": `Name`,
  "awsapn__Account_Number__c": `awsapn__Account_Number__c`,
  "awsapn__EntityId__c": `awsapn__EntityId__c`
}
```

11. Choose **Next**, then **Next**.
12. Review the rule, then choose **Create rule**.

###### Note

To troubleshoot an API destination, you can use the Amazon SQS console to add a dead letter queue to the target. The queue receives
messages that couldn't be delivered, plus the errors. From the Amazon SQS console, you can poll messages in the queue
for errors. For more information, refer to [Using
dead-letter queues to process undelivered events in EventBridge](../../../eventbridge/latest/userguide/eb-rule-dlq.md "../../../eventbridge/latest/userguide/eb-rule-dlq.md"), and
[Receiving
and deleting a message in Amazon SQS](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-receive-delete-message.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-receive-delete-message.md") in the
_Amazon SQS User Guide_.

#### Creating Offer Released events

The following steps explain how to create Offer Released events.

1. In the
   [Amazon EventBridge](../../../marketplace/latest/userguide/seller-eventbridge.md#events-changesets "../../../marketplace/latest/userguide/seller-eventbridge.md#events-changesets") console,
   Choose **Rules**.
2. Select the desired event bus from the list.
3. In the **Rules** section,
   Choose **Create rule**.
4. Enter a name for your rule, then
   choose **Next**.
5. Under **Event pattern**,
   select **Custom patterns (JSON
   editor)**, then enter the following filter: 

```
{
  "source": [
    "aws.marketplacecatalog"
  ],
  "detail-type": [
    "Offer Released"
  ]
}
```

For more information about event pattern matching, see
[Content
filtering in Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md "../../../eventbridge/latest/userguide/eb-event-patterns-content-based-filtering.md") in the
Amazon EventBridge User Guide. . 6. Choose **Next**. 7. In **Select targets**, under
**Target 1**, select
**EventBridge API
destination**, then open the list and select the
API destination that you just created. 8. Expand **Additional
settings**. 9. Under **Configure Target
Input** Select **Input
Transformer**, and select
**Configure Input
Tansformer**. This step prevents the top-level
Amazon event fields from being sent to Salesforce. Only the
part containing the Salesforce event fields from the detail
section of the original event are sent.

Use the following input path: 

```
{
   "Name":"$.detail-type",
   "awsapn__Account_Number__c":"$.account",
   "awsapn__EntityId__c":"$.detail.offer.id",
   "awsapn__Manufacturer_Account_Id__c":"$.detail.manufacturer.accountId",
   "awsapn__Product_Id__c":"$.detail.product.id",
   "awsapn__Seller_Account_Id__c":"$.detail.sellerOfRecord.accountId"
}
```

Use the following template: 

```
{
  "Name": `Name`,
  "awsapn__Account_Number__c": `awsapn__Account_Number__c`,
  "awsapn__EntityId__c": `awsapn__EntityId__c`,
  "awsapn__Seller_Account_Id__c": `awsapn__Seller_Account_Id__c`,
  "awsapn__Manufacturer_Account_Id__c": `awsapn__Manufacturer_Account_Id__c`,
  "awsapn__Product_Id__c": `awsapn__Product_Id__c`
}
```

10. Choose **Next** and then **Next**.
11. Review the rule, then choose **Create
    rule**.

###### Note

To help troubleshoot the
execution of the API destination, add an Amazon SQS dead
letter queue to the target. The queue receives the messages that
couldn't be delivered along with the errors. You can then poll
the messages to view the errors. For more information, see
[Event
retry policy and using dead-letter queues](../../../eventbridge/latest/userguide/eb-rule-dlq.md "../../../eventbridge/latest/userguide/eb-rule-dlq.md") and
[Receiving
and deleting messages (console)](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-receive-delete-message.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-receive-delete-message.md") in the AWS documentation.

#### Creating opportunity events

Opportunity events provide real-time notifications about changes
in the status or details of opportunities

You can also create and manage EventBridge rules
programmatically using the
[AWS SDKs](../selling-api/opportunity-events.md#aws-eventbridge "../selling-api/opportunity-events.md#aws-eventbridge").

#### Types of events

The following list describes the event types generated when partners work with opportunities.
The links take you to the API documentation for each event.

- [Opportunity Created:](../selling-api/selling-api-events.md#opportunity-created "../selling-api/selling-api-events.md#opportunity-created")
  – Triggered when a new opportunity is created.
- [Opportunity
  Updated](../selling-api/selling-api-events.md#opportunity-updated "../selling-api/selling-api-events.md#opportunity-updated") – Triggered when an opportunity is updated.
- [Engagement
  Invitation Created](../selling-api/selling-api-events.md#invitation-created "../selling-api/selling-api-events.md#invitation-created") – Triggered when an opportunity is created.
- [Engagement
  Invitation Accepted](../selling-api/selling-api-events.md#invitation-accepted "../selling-api/selling-api-events.md#invitation-accepted") – Triggered when a partner accepts an
  AWS Engagement Invitation, confirming their interest in
  collaborating with AWS on the opportunity.
- [Engagement
  Invitation Rejected](../selling-api/selling-api-events.md#invitation-rejected "../selling-api/selling-api-events.md#invitation-rejected") – Triggered when an opportunity is
  rejected.

#### Example event

```
{
    "version": "1",
    "id": ""`d1example-0c9c-4655-15bf-c5exampleb08`",
    "source": "aws.partnercentral-selling",
    "detail-type": "Opportunity Created",
    "time": ""`2023-10-28T13:31:05Z`",
    "region": ""`us-east-1`",
    "account": ""`123456789123`",
    "detail": { 
        "schemaVersion": "1",
        "catalog": "AWS",
        "opportunity": {
            "identifier": ""`O1234567`",
            "url": "`Partner Central Opportunity Page URL`"
        }
    }
}
```

### Example rules

The following table lists examples of the EventBridge rules that you can use with the events listed in the previous section.
Rules route events from the event bus to the API destination, which results in making a REST call to publish an event back to Salesforce.

| Event type                         | Example                                                                                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Opportunity Created**            | `<br>{<br>"source": ["aws.partnercentral-selling"],<br>"detail-type": ["Opportunity Created"],<br>"detail": {<br>"catalog": ["AWS"]<br>}<br>}<br>`            |
| **Opportunity Updated**            | `<br>{<br>"source": ["aws.partnercentral-selling"],<br>"detail-type": ["Opportunity Updated"],<br>"detail": {<br>"catalog": ["AWS"]<br>}<br>}<br>`            |
| **Engagement Invitation Created**  | `<br>{<br>"source": ["aws.partnercentral-selling"],<br>"detail-type": ["Engagement Invitation Created"],<br>"detail": {<br>"catalog": ["AWS"]<br>}<br>}<br>`  |
| **Engagement Invitation Accepted** | `<br>{<br>"source": ["aws.partnercentral-selling"],<br>"detail-type": ["Engagement Invitation Accepted"],<br>"detail": {<br>"catalog": ["AWS"]<br>}<br>}<br>` |
| **Engagement Invitation Rejected** | `<br>{<br>"source": ["aws.partnercentral-selling"],<br>"detail-type": ["Engagement Invitation Rejected"],<br>"detail": {<br>"catalog": ["AWS"]<br>}<br>}<br>` |
| **All events**                     | `<br>{<br>"source": ["aws.partnercentral-selling"],<br>"detail": {<br>"catalog": ["AWS"]<br>}<br>}<br>`                                                       |
