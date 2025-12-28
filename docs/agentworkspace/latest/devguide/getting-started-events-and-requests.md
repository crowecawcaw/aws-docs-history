# Events and requests in Amazon Connect

Agent Workspace

App developers can easily create applications that seamlessly integrate into the
agent workspace experience in the Amazon Connect agent workspace with the event and
request functionality natively supported by [Amazon Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK").
You can build an app by leveraging the [Amazon
Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK") to subscribe to agent/contact events (invoking a particular
handler when the event occurs) and make requests to quickly retrieve agent/contact
data.

This is the main module needed to integrate your app into the agent workspace and
get exposure to its agent/contact data and make your app responsive throughout the
contact-handling lifecycle.

- **Event**

Refers to an asynchronous subscription-publication model, where the [Amazon Connect
SDK's](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK") client allows the 3P app to subscribe a callback to-be-invoked
when a specific event occurs, such as an agent changing their state from _Available_ to _Offline_. It then performs an
application-defined action using the event context when said event fires. If
and when an event fires is dependent on the event type. For more
information, see the [API
Reference](api-reference-3P-apps-events-and-requests.md "api-reference-3P-apps-events-and-requests.md").

- **Request**

Refers to a request-reply model, where the [Amazon Connect
SDK's](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK") client allows the 3P app to make requests on demand to
retrieve data about the current contact or the logged-in agent.

**Install from NPM**

Install the contact package from NPM by installing **@amazon-connect/contact**.

```

% npm install --save @amazon-connect/contact

```
