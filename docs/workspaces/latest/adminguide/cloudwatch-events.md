# Monitor your WorkSpaces using Amazon EventBridge

You can use events from Amazon WorkSpaces to view, search, download, archive, analyze, and
respond to successful logins to your WorkSpaces. For example, you can use events for the
following purposes:

- Store or archive WorkSpaces login events as logs for future reference, analyze
  the logs to look for patterns, and take action based on those patterns.
- Use the WAN IP address to determine where users are logged in from, and then
  use policies to allow users access only to files or data from WorkSpaces that
  meet the access criteria found in the event type of `WorkSpaces
Access`.
- Analyze login data and perform automated actions using AWS Lambda.
- Use policy controls to block access to files and applications from
  unauthorized IP addresses.
- Find out the WorkSpaces client version used to connect to WorkSpaces.
  Amazon WorkSpaces emits these events on a best-effort basis. Events are delivered to EventBridge in
  near real time. With EventBridge, you can create rules that trigger programmatic actions in
  response to an event. For example, you can configure a rule that invokes an SNS topic to
  send an email notification or invokes a Lambda function to take some action. For more
  information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

## WorkSpaces Access events

WorkSpaces client applications send `WorkSpaces Access` events when a user
successfully logs in to a WorkSpace. All WorkSpaces clients send these events.

Events emitted for WorkSpaces using DCV require the WorkSpaces client
application version 4.0.1 or later.

Events are represented as JSON objects. The following is example data for a
`WorkSpaces Access` event.

```
{
    "version": "0",
    "id": "`64ca0eda-9751-dc55-c41a-1bd50b4fc9b7`",
    "detail-type": "WorkSpaces Access",
    "source": "aws.workspaces",
    "account": "`123456789012`",
    "time": "`2023-04-05T16:13:59Z`",
    "region": "`us-east-1`",
    "resources": [],
    "detail": {
        "clientIpAddress": "`192.0.2.3`",
        "actionType": "successfulLogin",
        "workspacesClientProductName": "`WorkSpacesWebClient`",
        "loginTime": "`2023-04-05T16:13:37.603Z`",
        "clientPlatform": "`Windows`",
        "directoryId": "domain/`d-123456789`",
        "clientVersion": "`5.7.0.3472`",
        "workspaceId": "`ws-xyskdga`"
    }
}
```

###### Event-specific fields

`clientIpAddress`

The WAN IP address of the client application. For PCoIP zero clients,
this is the IP address of the Teradici auth client.

`actionType`

This value is always `successfulLogin`.

`workspacesClientProductName`

The following values are case-sensitive.

- `WorkSpaces Desktop client` — Windows, macOS,
  and Linux clients
- `Amazon WorkSpaces Mobile client` — iOS
  client
- `WorkSpaces Mobile Client` — Android
  clients
- `WorkSpaces Chrome Client` — Chromebook
  client
- `WorkSpacesWebClient` — Web Access
  client
- `AmazonWorkSpacesThinClient` — Amazon WorkSpaces Thin
  Client device
- `Teradici PCoIP Zero Client, Teradici PCoIP Desktop
Client, or Dell Wyse PCoIP Client` — Zero
  Client

`loginTime`

The time at which the user logged in to the WorkSpace.

`clientPlatform`

- `Android`
- `Chrome`
- `iOS`
- `Linux`
- `OSX`
- `Windows`
- `Teradici PCoIP Zero Client and Tera2`
- `Web`

`directoryId`

The identifier of the directory for the WorkSpace. You must prepend
the directory identifier with `domain/`. For example,
`"domain/d-123456789"`.

`clientVersion`

The client version used to connect to WorkSpaces.

`workspaceId`

The identifier of the WorkSpace.

## Create a rule to handle WorkSpaces

events

Use the following procedure to create a rule to handle the WorkSpaces
events.

###### Prerequisite

To receive email notifications, create an Amazon Simple Notification Service topic.

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose **Create topic**.
4. For **Type**, choose
   **Standard**.
5. For **Name**, enter a name for your topic.
6. Choose **Create topic**.
7. Choose **Create subscription**.
8. For **Protocol**, choose
   **Email**.
9. For **Endpoint**, enter the email address that receives
   the notifications.
10. Choose **Create subscription**.
11. You'll receive an email message with the following subject line:
    AWS Notification - Subscription Confirmation. Follow
    the directions to confirm your subscription.

###### To create a rule to handle WorkSpaces events

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Choose **Create rule**.
3. For **Name**, enter a name for your rule.
4. For **Rule type**, choose **Rule with an event
   pattern**.
5. Choose **Next**.
6. For **Event pattern**, do the following:
   1. For **Event source**, choose
      **AWS services**.
   2. For **AWS service**, choose
      **WorkSpaces**.
   3. For **Event type**, choose **WorkSpaces
      Access**.
   4. By default, we send notifications for every event. If you prefer,
      you can create an event pattern that filters events for specific
      clients or workspaces.

7. Choose **Next**.
8. Specify a target as follows:
   1. For **Target types**, choose
      **AWS service**.
   2. For **Select a target**, choose **SNS
      topic**.
   3. For **Topic**, choose the SNS topic that you
      created for notifications.

9. Choose **Next**.
10. (Optional) Add tags to your rule.
11. Choose **Next**.
12. Choose **Create rule**.
