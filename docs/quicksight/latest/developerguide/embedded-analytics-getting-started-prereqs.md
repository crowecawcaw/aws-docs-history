

# Prerequisites
<a name="embedded-analytics-getting-started-prereqs"></a>

Before you get started, familiarize yourself with the list of technologies Quick Sight uses to create an embedding experience. Check that the technologies listed below are compatible with your application:
+ Embedding utilizes [Iframes](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) to display your content and [MessageChannels](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel) to communicate.
+ If you’re developing a JavaScript-based front-end application, we ecommend you use the [Embedding Quick Sight data dashboards for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-dashboards-for-authenticated-users.html) in your application to leverage performance, customization, and interactivity capabilities offered through the SDK for your embedded content.
+ A backend service that is compatible with one of the languages supported in the [AWS SDK](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html).
+ Many web applications use [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) to add security on what can be loaded within the application. Ensure you have ability to allowlist Quick Sight domains in your CSP.
+ Make sure you are using one of our [supported browsers](https://docs.aws.amazon.com/quicksight/latest/user/supported-browsers.html).

After you confirm that your application is compatible with Quick Sight embedding, complete the steps listed in [Getting started with Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/getting-started.html). 