# Send web notifications with Connect Customer outbound campaigns

You can use Connect Customer outbound campaigns to deliver personalized notifications to website visitors
through the Communications widget. Notifications are triggered by visitor activity that the web data
tracker captures into Customer Profiles, such as scrolling past a portion of the page, viewing a
product for an extended time, or adding an item to a cart. For an overview of how the web
data tracker and web notification work together, see [Web data tracker and web notification](customer-profiles-web-tracker-and-notification.md "customer-profiles-web-tracker-and-notification.md").

## How web notification works

1. An event trigger fires when visitor behavior matches a rule you configured
   in your outbound campaigns campaign.
2. The campaign passes the visitor context to the web notification service,
   which calls the Customer Profiles API to resolve dynamic placeholders such as first name
   and recommended products.
3. The service delivers the notification to the visitor's browser over
   WebSocket and displays it in the Communications widget. The service records
   interaction events for analytics.

## Prerequisites

- An Connect Customer instance with the Communications widget configured and data collection
  enabled. For more information, see [Capture website visitor activity with the web data tracker](chat-widget-data-tracker.md "chat-widget-data-tracker.md").
- Customer Profiles enabled on the instance. For more information, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md "enable-customer-profiles.md").
- Connect Customer outbound campaigns enabled on the instance. For more information, see [Enable outbound campaigns and Customer Profiles](enable-outbound-campaigns-customer-profiles.md "enable-outbound-campaigns-customer-profiles.md").
- Upgrade your existing outbound campaigns configuration to enable this channel. For
  more information, see [Set up Connect Customer outbound campaigns](enable-outbound-campaigns.md "enable-outbound-campaigns.md").

## Step 1: Enable web notification on your Communications widget

1. Sign in to the Connect Customer admin website.
2. In the navigation menu, choose **Channels**, then choose
   **Communications widgets**.
3. Create a new widget or open an existing one for editing.
4. Under the **Features** section, enable **Web
   notification**.
5. Add the website domains where the widget will be embedded to the allowed
   domains list.
6. Save the widget and copy the widget snippet code for embedding on your
   website.

## Step 2: Create a notification view

A view defines the visual layout and content of your notification. Use the
notification template to design what visitors see.

1. In the navigation menu, choose **UI Management**, then
   choose **Views**.
2. Choose **Create view** and select the
   **Notification** template.
3. Design the notification content:

   - **Title** – Supports
     personalization, for example `Hi {FirstName}!`.
   - **Message body** – Can include
     product recommendations from Customer Profiles.
   - **Action buttons** – For
     example, **Chat now** or **Learn
     more**.

4. Publish the view.

For more information about views, see [Views: UI templates to customize an agent's workspace in Connect Customer](view-resources-sg.md "view-resources-sg.md").

## Step 3: Add a web notification service integration and personalize your view

To personalize notification content with Customer Profiles data, add a web notification service
integration to your view. The integration connects the view to the Customer Profiles API so dynamic
placeholders are resolved at delivery time.

1. Open your view in the view editor.
2. Choose the **Integrations** tab.
3. Choose **Add integration**.
4. Set the **Integration name**, for example `WNS`.
   This name is how you reference profile attributes in your view content using
   the `$.#INTEGRATION_NAME` syntax.
5. Set **Integration type** to **Web notification
   service**.
6. Choose **Add integration** to save.

After adding the integration, use dynamic placeholders in the view to personalize
notifications with profile data. The following table shows the syntax patterns to use
in the title or message body of a notification view.

| **Data type**                 | **Syntax**                                                                 | **Example**                                  |
| ----------------------------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| Customer profile attribute    | `$.#INTEGRATION_NAME.Profile.<AttributeName>`                              | `$.#WNS.Profile.FirstName`                   |
| Recommendation (catalog item) | `$.#INTEGRATION_NAME.Recommendations[<Index>].CatalogItem.<AttributeName>` | `$.#WNS.Recommendations[0].CatalogItem.Name` |

**Example notification content**

Using an integration named `WNS`, a notification might look like the
following:

```
Title:   Hi $.#WNS.Profile.FirstName! Still thinking about this?
Message: We think you'll love $.#WNS.Recommendations[0].CatalogItem.Name.
         Click below to chat with an agent.
```

###### Tip

In the view editor, choose the **Reference** tab to see all
available Customer Profiles attributes and recommendation catalog fields you can use as
dynamic placeholders.

###### Note

When a notification is triggered, the web notification service calls the
`BatchGetProfile` and `GetProfileRecommendations` APIs in
Customer Profiles to fetch real-time profile data and resolve any dynamic placeholders before
delivering the notification to the visitor's browser.

## Step 4: Create the campaign

Web notifications are delivered through outbound campaigns. Create a campaign that links to
the widget you configured in Step 1 and the notification view you created in Step 2.
For a full walkthrough including screenshots, see [Create an outbound campaign using the admin website](how-to-create-campaigns.md "how-to-create-campaigns.md") and
[Create an outbound campaign using event triggers](how-to-create-campaigns-using-event-triggers.md "how-to-create-campaigns-using-event-triggers.md").

(Optional) Link a recommender to enable AI-driven product suggestions in the
notification. Recommenders are only available when you select the
**View** notification type and the selected view has a
**Web Notification Service** integration. For more information,
see [Predictive Insights (Preview)](customer-profiles-predictive-insights.md "customer-profiles-predictive-insights.md").

## Step 5: Initialize web notifications on your website

After embedding the Communications widget snippet on your website, initialize web
notifications by calling `Notification.init()` in your page
JavaScript. Call this method only after the visitor has granted appropriate consent
for personalized messaging.

```
await window.amazon_connect.Web.Notification.init();
```

## Measure performance

Track delivery, engagement, chat conversion, and dismissal in the Connect Customer analytics
dashboard under the outbound campaigns performance section.

## Limitations

For limitations that apply to web notification, see [Limitations](customer-profiles-web-tracker-and-notification.md#web-tracker-and-notification-limitations "customer-profiles-web-tracker-and-notification.md#web-tracker-and-notification-limitations").
