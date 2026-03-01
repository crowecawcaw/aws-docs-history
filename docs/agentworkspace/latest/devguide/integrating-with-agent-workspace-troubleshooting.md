# Troubleshoot application setup in Amazon Connect Agent Workspace

You can use the [Amazon Connect SDK's](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK")
`AppConfig` object to retrieve data about your applications’s setup in the Amazon Connect
agent workspace, including its permissions. This will allow you to inspect its
state and determine which permissions were assigned to your app. Accessing its `permissions` property will return a list of strings, each representing a
permissions that grants access to a set of events and requests. Performing an action,
whether subscribing to an event or making a request, will fail if your app does not have
the corresponding permission that grants the action. You may have to ask your account
admin to assign the permissions required for your app to function. To review the full
list of permissions assignable to apps, please see the admin guide.

## Events

If your app uses the [Amazon Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK")
to subscribe to an event that it does not have permission for, the agent workspace
will throw an error with a message formatted like below.

```

App attempted to subscribe to topic without permission - Topic {"key":
<event_name>,"namespace":"aws.connect.contact"}`

```

## Requests

If your app uses the [Amazon Connect SDK](https://github.com/amazon-connect/AmazonConnectSDK "https://github.com/amazon-connect/AmazonConnectSDK")
to make a request that it does not have permission for, the agent workspace will
throw an error with a message formatted like below.

```

App does not have permission for this request

```
