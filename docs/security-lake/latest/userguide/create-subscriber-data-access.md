# Creating a subscriber with data

access in Security Lake

Choose one of the following access methods to create a subscriber with access to data
in the current AWS Region.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. By using the AWS Region selector in the upper-right corner of
   the page, select the Region where you want to create the
   subscriber.
3. In the navigation pane, choose
   **Subscribers**.
4. On the **Subscribers** page, choose
   **Create subscriber**.
5. For **Subscriber details**, enter
   **Subscriber name** and an optional
   **Description**.

The **Region** is auto-populated as your
currently selected AWS Region and can't be modified. 6. For **Log and event sources**, choose which
sources the subscriber is authorized to consume. 7. For **Data access method**, choose
**S3** to set up data access for the
subscriber. 8. For **Subscriber credentials**, provide the
subscriber's AWS account ID and [external ID](prereqs-creating-subscriber.md#subscriber-external-id "prereqs-creating-subscriber.md#subscriber-external-id"). 9. (Optional) For **Notification details**, if you
want Security Lake to create an Amazon SQS queue that the subscriber can poll
for object notifications, select **SQS queue**. If
you want Security Lake to send notifications through EventBridge to an HTTPS
endpoint, select **Subscription endpoint**.

If you select **Subscription endpoint**, also do
the following:

    1. Enter the **Subscription endpoint**.
     Examples of valid endpoint formats include
     `http://example.com`. Optionally,
     you can also provide an **HTTPS key name**
     and **HTTPS key value**.
    2. For **Service Access**, create a new
     IAM role or use an existing IAM role that gives EventBridge
     permission to invoke API destinations and send object
     notifications to the correct endpoints.


    For information about creating a new IAM role, see
     [Create IAM role to invoke EventBridge API
     destinations](prereqs-creating-subscriber.md#iam-role-subscriber "prereqs-creating-subscriber.md#iam-role-subscriber").

10. (Optional) For **Tags**, enter as many as 50 tags
    to assign to the subscriber.

A _tag_ is a label that you can
define and assign to certain types of AWS resources. Each tag
consists of a required tag key and an optional tag value. Tags can
help you identify, categorize, and manage resources in different
ways. To learn more, see [Tagging Security Lake resources](tagging-resources.md "tagging-resources.md"). 11. Choose **Create**.

API
To create a subscriber with data access programmatically, use the [CreateSubscriber](../APIReference/API_CreateSubscriber.md "../APIReference/API_CreateSubscriber.md") operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run
the [create-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber.html") command.

In your
request, use these parameters to specify the following settings for
the subscriber:

- For `sources`, specify each source that you want the
  subscriber to access.
- For `subscriberIdentity`, specify the AWS account ID
  and external ID that the subscriber will use to access source
  data.
- For `subscriber-name`, specify the name of the subscriber.
- For `accessTypes`, specify `S3`.

**Example 1**

The following example creates a subscriber with access to data in the
current AWS Region for the specified subscriber identity for an AWS
source.

```
`$` `aws securitylake create-subscriber \
--subscriber-identity {"accountID": `1293456789123`,"externalId": `123456789012`} \
--sources [{"awsLogSource": {"sourceName": `VPC_FLOW`, "sourceVersion": `2.0`}}] \
--subscriber-name `subscriber name` \
--access-types `S3``
```

**Example 2**

The following example creates a subscriber with access to data in the
current AWS Region for the specified subscriber identity for a custom
source.

```
`$` `aws securitylake create-subscriber \
--subscriber-identity {"accountID": `1293456789123`,"externalId": `123456789012`} \
--sources [{"customLogSource": {"sourceName": `custom-source-name`, "sourceVersion": `2.0`}}] \
--subscriber-name `subscriber name`
--access-types `S3``
```

The preceding examples are formatted for Linux, macOS, or Unix, and they use the
backslash (\) line-continuation character to improve readability.

(Optional) After you create a subscriber, use the [CreateSubscriberNotification](../APIReference/API_CreateSubscriberNotification.md "../APIReference/API_CreateSubscriberNotification.md") operation to specify how to notify
the subscriber when new data is written to the data lake for the sources
that you want the subscriber to access. If you're using the AWS Command Line Interface (AWS CLI), run
the [create-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber-notification.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-subscriber-notification.html") command.

- To override the default notification
  method (HTTPS endpoint) and create an Amazon SQS queue, specify values for the
  `sqsNotificationConfiguration` parameters.
- If you prefer notification with an HTTPS endpoint, specify values for the
  `httpsNotificationConfiguration` parameters.
- For the `targetRoleArn` field, specify the ARN of the IAM role that
  you created to invoke EventBridge API destinations.

```
`$` `aws securitylake create-subscriber-notification \
--subscriber-id "`12345ab8-1a34-1c34-1bd4-12345ab9012`" \
--configuration httpsNotificationConfiguration={"targetRoleArn"="`arn:aws:iam::XXX:role/service-role/RoleName`", "endpoint"="`https://account-management.$3.$2.securitylake.aws.dev/v1/datalake`"}`
```

To get the `subscriberID`, use the [ListSubscribers](../APIReference/API_ListSubscribers.md "../APIReference/API_ListSubscribers.md") operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run
the [list-subscriber](../../../cli/latest/reference/securitylake/list-subscribers.md "../../../cli/latest/reference/securitylake/list-subscribers.md") command.

```
`$` `aws securitylake list-subscribers`
```

To subsequently change the notification method (Amazon SQS queue or HTTPS endpoint) for the
subscriber, use the [UpdateSubscriberNotification](../APIReference/API_UpdateSubscriberNotification.md "../APIReference/API_UpdateSubscriberNotification.md") operation or, if you're using the AWS CLI, run
the [update-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber-notification.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber-notification.html") command. You can also change the
notification method by using the Security Lake console: select the subscriber on the
**Subscribers** page, and then choose
**Edit**.

## Sample object notification message

The following example shows the event notification in JSON structure format for the
`CreateSubscriberNotification` operation.

```
{
  "source": "aws.s3",
  "time": "2021-11-12T00:00:00Z",
  "account": "123456789012",
  "region": "ca-central-1",
  "resources": [
    "arn:aws:s3:::amzn-s3-demo-bucket"
  ],
  "detail": {
    "bucket": {
      "name": "amzn-s3-demo-bucket"
    },
    "object": {
      "key": "example-key",
      "size": 5,
      "etag": "b57f9512698f4b09e608f4f2a65852e5"
    },
    "request-id": "N4N7GDK58NMKJ12R",
    "requester": "securitylake.amazonaws.com"
  }
}
```
