

# Using the AWS Quick Sight Embedding SDK to enable shareable links to embedded dashboard views

AWS Quick Sight developers can use the AWS Quick Sight Embedding SDK (version 2.8.0 and higher) to allow readers of embedded dashboards to receive and distribute shareable links to their view of an embedded dashboard. Developers can use dashboard or console embedding to generate a shareable link to their application page with AWS Quick Sight's reference encapsulated using the AWS Quick Sight Embedding SDK. AWS Quick Sight Readers can then send this shareable link to their peers. When their peer accesses the shared link, they are taken to the page on the application that contains the embedded AWS Quick Sight dashboard. Developers can also generate and save shareable links of dashboard views that can be used as a bookmarks for anonymous readers of AWS Quick Sight when using anonymous embedding.

**Prerequisites**

Before you get started, make sure that you are using the AWS Quick Sight Embedding SDK version 2.8.0 or higher

**Topics**
+ [Enabling the `SharedView` feature configuration for AWS Quick Sight embedded analytics](embedded-view-sharing-set-up.md)
+ [Creating a shared view with the AWS Quick Sight `createSharedView` API](embedded-view-sharing-sdk-create.md)
+ [Consuming a shared AWS Quick Sight view](embedded-view-sharing-sdk-consume.md)