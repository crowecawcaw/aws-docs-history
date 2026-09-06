

# Web data tracker and web notification
<a name="customer-profiles-web-tracker-and-notification"></a>

Connect Customer offers two capabilities that work together with the Communications widget to help you understand website visitors and engage them with personalized messages:
+ **Web data tracker** – Captures how visitors interact with your website (click interactions, search queries, form completion) and associates that activity with their profile in Customer Profiles.
+ **Web notification** – Delivers personalized notifications to visitors directly in their browser through the Communications widget, with no need for them to start a conversation first.

## How it works
<a name="web-tracker-and-notification-how-it-works"></a>

1. The web data tracker captures visitor activity (click interactions, search queries, form completion) and associates it with the visitor's profile in Customer Profiles.

1. You define event trigger conditions in an outbound campaigns campaign, such as clicking certain buttons or entering specific search terms.

1. When the condition is met, a personalized notification is delivered to the visitor's browser through the Communications widget. The visitor can start a chat, follow a link, or dismiss the notification.

**Note**  
Notifications are delivered through the Communications widget. Visitors do not install a plugin, extension, or app.

## Prerequisites
<a name="web-tracker-and-notification-prereqs"></a>

Before you set up web data tracker and web notification, make sure that the following are in place on your Connect Customer instance:
+ The Communications widget is configured. For more information, see [Add a chat user interface to your website hosted by Connect Customer](add-chat-to-website.md).
+ Customer Profiles is enabled. For more information, see [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md).
+ Connect Customer outbound campaigns is enabled. For more information, see [Enable outbound campaigns and Customer Profiles](enable-outbound-campaigns-customer-profiles.md).

## What the web data tracker captures
<a name="web-tracker-what-is-captured"></a>

After you enable **Data collection**, you can begin emitting your own business events — such as "add to cart," "purchase," or any custom event types relevant to your use case. Note that this requires changes to your website.


| **Visitor activity** | **Capture mode** | **What is captured** | 
| --- | --- | --- | 
| Business events | Custom (API call) | Custom events such as Add to Cart, Purchase Completed, or View Product, configured using the `recordBusinessMetric` API. For more information, see [Capture website visitor activity with the web data tracker](chat-widget-data-tracker.md). | 

The **Advanced Data Collection** automatically captures common website interactions without additional coding:


| **Visitor activity** | **Capture mode** | **What is captured** | 
| --- | --- | --- | 
| Clicks | Automatic | Links and buttons clicked, including the element text and destination URL. | 
| Searches | Automatic | Search queries entered on your site through standard search input fields. | 
| Form submissions | Automatic | When forms are submitted. Form field values, passwords, and payment information are never captured. | 

## Common use cases
<a name="web-notification-use-cases"></a>

Common use cases include:
+ Recover abandoned carts.
+ Follow up on product interest.
+ Deliver personalized recommendations based on browsing history.
+ Offer proactive support when a visitor appears stuck.
+ Drive promotional engagement based on browsing behavior.

## Get started with web data tracker and web notification
<a name="web-tracker-and-notification-get-started"></a>

Setup is split across two areas of the admin console.
+ Configure web data tracking on your Communications widget and embed the widget on your website. For more information, see [Capture website visitor activity with the web data tracker](chat-widget-data-tracker.md).
+ Design the notification view, define event triggers in Customer Profiles, and create the campaign that delivers the notification. For more information, see [Send web notifications with Connect Customer outbound campaigns](outbound-campaigns-web-notification.md).

## Personalization options
<a name="web-notification-personalization"></a>

You can personalize notifications with profile data from Customer Profiles: visitor name and identity attributes, browsing history, AI-powered product recommendations, and any custom attributes you store in the profile. For recommendations, see [Predictive Insights (Preview)](customer-profiles-predictive-insights.md).

## Performance impact
<a name="web-tracker-performance-impact"></a>

The SDK loads asynchronously and does not block page rendering. The SDK batches and sends events in the background, typically within 1 to 5 seconds of capture, with sampling and deduplication to keep network usage low.

## Measuring success
<a name="web-notification-measuring-success"></a>

Track delivery rate, engagement rate, chat conversions, and dismissals in the Connect Customer analytics dashboard under the outbound campaigns performance section.

## Limitations
<a name="web-tracker-and-notification-limitations"></a>
+ Web notification requires an active WebSocket connection. The browser tab must be open and the widget must be loaded; closing the tab or putting the device to sleep ends the connection.
+ Concurrent active connections are subject to per-customer service quotas. Contact AWS Support to request a limit increase.
+ For single-page applications (SPAs), embed the widget snippet once at the application root. For multi-page applications (MPAs), include the snippet on every page where you want tracking or notifications.
+ Recommendation-based notifications require product catalog data to be ingested into Customer Profiles before the campaign runs. For more information, see [Predictive Insights (Preview)](customer-profiles-predictive-insights.md).
+ Each event trigger can be linked to at most one campaign.
+ Supported browsers: Google Chrome, Mozilla Firefox, and Safari.