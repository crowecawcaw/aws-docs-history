# Amazon SNS SMS delivery monitoring with Amazon CloudWatch metrics

and logs

You can use Amazon CloudWatch and Amazon CloudWatch Logs to monitor your SMS message deliveries.

## Viewing Amazon CloudWatch metrics

Amazon SNS automatically collects metrics about your SMS message deliveries and pushes them
to Amazon CloudWatch. You can use CloudWatch to monitor these metrics and create alarms to alert you
when a metric crosses a threshold. For example, you can monitor CloudWatch metrics to learn
your SMS delivery rate and your month-to-date SMS charges.

For information about monitoring CloudWatch metrics, setting CloudWatch alarms, and the types of
metrics available, see [Monitoring Amazon SNS topics using
CloudWatch](sns-monitoring-using-cloudwatch.md "sns-monitoring-using-cloudwatch.md").

## Viewing CloudWatch Logs

You can collect information about successful and unsuccessful SMS message deliveries
by enabling Amazon SNS to write to Amazon CloudWatch Logs. For each SMS message that you send, Amazon SNS
writes a log that includes the message price, the success or failure status, the reason
for failure (if the message failed), the message dwell time, and other
information.

###### To enable and view CloudWatch Logs for your SMS messages

1.  Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2.  In the console menu, set the region selector to a [region that supports SMS
    messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md").
3.  On the navigation panel, choose **Text messaging
    (SMS)**.
4.  On the **Mobile text messaging (SMS)** page, in the
    **Text messaging preferences** section, choose
    **Edit**.
5.  On the next page, expand the **Delivery status logging**
    section.
6.  For **Success sample rate**, specify the percentage of
    successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. For
    example:

        * To write logs only for failed deliveries, set this value to 0.
        * To write logs for 10% of your successful deliveries, set it to
         10.

    If you don't specify a percentage, Amazon SNS writes logs for all successful
    deliveries.

7.  To provide the required permissions, do one of the following:
    - To create a new service role, choose **Create new service
      role** and then **Create new roles**. On
      the next page, choose **Allow** to give Amazon SNS write
      access to your account's resources.
    - To use an existing service role, choose **Use existing service
      role** and then paste the ARN name in the **IAM
      role for successful and failed deliveries** box.

    The service role you specify must allow write access to your account's
    resources. For more information on creating IAM roles, see [Creating a role for an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console") in the
    _IAM User Guide_.

8.  Choose **Save changes**.
9.  Back on the **Mobile text messaging (SMS)** page, go to the
    **Delivery status logs** section to view any available
    logs.

###### Note

Depending on the destination phone number's carrier, it can take up to 72
hours for delivery logs to appear in the Amazon SNS console.

## Example log for successful SMS

delivery

The delivery status log for a successful SMS delivery will resemble the following
example:

```
{
    "notification": {
        "messageId": "34d9b400-c6dd-5444-820d-fbeb0f1f54cf",
        "timestamp": "2016-06-28 00:40:34.558"
    },
    "delivery": {
        "phoneCarrier": "My Phone Carrier",
        "mnc": 270,
        "numberOfMessageParts": 1,
        "destination": "+1XXX5550100",
        "priceInUSD": 0.00645,
        "smsType": "Transactional",
        "mcc": 310,
        "providerResponse": "Message has been accepted by phone carrier",
        "dwellTimeMs": 599,
        "dwellTimeMsUntilDeviceAck": 1344
    },
    "status": "SUCCESS"
}
```

## Example log for failed SMS

delivery

The delivery status log for a failed SMS delivery will resemble the following
example:

```
{
    "notification": {
        "messageId": "1077257a-92f3-5ca3-bc97-6a915b310625",
        "timestamp": "2016-06-28 00:40:34.559"
    },
    "delivery": {
        "mnc": 0,
        "numberOfMessageParts": 1,
        "destination": "+1XXX5550100",
        "priceInUSD": 0.00645,
        "smsType": "Transactional",
        "mcc": 0,
        "providerResponse": "Unknown error attempting to reach phone",
        "dwellTimeMs": 1420,
        "dwellTimeMsUntilDeviceAck": 1692
    },
    "status": "FAILURE"
}
```

## SMS delivery failure reasons

The reason for a failure is provided with the `providerResponse` attribute.
SMS messages might fail to deliver for the following reasons:

- Blocked as spam by phone carrier
- Destination is on a blocked list
- Invalid phone number
- Message body is invalid
- Phone carrier has blocked this message
- Phone carrier is currently unreachable/unavailable
- Phone has blocked SMS
- Phone is on a blocked list
- Phone is currently unreachable/unavailable
- Phone number is opted out
- This delivery would exceed max price
- Unknown error attempting to reach phone
