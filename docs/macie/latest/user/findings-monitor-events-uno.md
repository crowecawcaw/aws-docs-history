# Monitoring Macie findings with AWS User Notifications

AWS User Notifications is a service that acts as a central location for your AWS notifications on the
AWS Management Console. This includes notifications such as Amazon CloudWatch alarms, AWS Support cases, and
communications from other AWS services. With User Notifications, you can configure custom rules and
delivery channels for receiving notifications about certain types of Amazon EventBridge events. The
delivery channels include email, Amazon Q Developer in chat applications, and push notifications in the AWS Console Mobile Application. You can
also review notifications on the AWS User Notifications console. To learn more about User Notifications, see the [AWS User Notifications User
Guide](../../../notifications/latest/userguide/what-is-service.md "../../../notifications/latest/userguide/what-is-service.md").

Amazon Macie integrates with AWS User Notifications, which means you can configure User Notifications to notify you of
events that Macie publishes to EventBridge for policy and sensitive data findings. If a finding event
matches criteria that you specify, User Notifications generates a notification. The notification includes key
details of the associated finding, such as the finding's type and severity, and the name of the
affected resource. User Notifications can also send the notification to one or more delivery channels that
you specify. You can tailor your choice of delivery channels to align with your security and
compliance workflows.

For example, you might configure User Notifications to generate notifications for specific types of new,
high-severity findings. You might also specify Amazon Q Developer in chat applications as a delivery channel for those
notifications. User Notifications then detects EventBridge events for the findings, generates notifications that
include data from the findings, and sends the notifications to Amazon Q Developer in chat applications. Amazon Q Developer in chat applications might then
route the notifications to a Slack channel or an Amazon Chime chat room to notify your incident
response team.

###### Topics

- [Working with
  AWS User Notifications](#findings-monitor-events-uno-overview "#findings-monitor-events-uno-overview")
- [Enabling and configuring
  notifications for findings](#findings-monitor-events-uno-configure "#findings-monitor-events-uno-configure")
- [Mapping notification fields
  to finding fields](#findings-monitor-events-uno-schema "#findings-monitor-events-uno-schema")
- [Changing notification
  settings for findings](#findings-monitor-events-uno-change "#findings-monitor-events-uno-change")
- [Disabling notifications for
  findings](#findings-monitor-events-uno-disable "#findings-monitor-events-uno-disable")

## Working with AWS User Notifications

With AWS User Notifications, you create rules to specify the types of Amazon EventBridge events that you want to
monitor and receive notifications for. A rule defines criteria that an EventBridge event must match
in order to generate a notification. You can also choose one or more delivery channels for a
rule. Delivery channels specify where you want to receive notifications for events that match
a rule's criteria.

If User Notifications detects an EventBridge event that matches a rule's criteria, it performs the following
general tasks:

1. Extracts a subset of data from the event.
2. Generates a notification that contains the extracted data.
3. Sends the notification to delivery channels that you specify for that type of
   event.

The design and structure of the notification is optimized for each delivery channel that
it's sent to.

To control the frequency or number of notifications that you receive, you can configure
aggregation settings for a rule. If you enable these settings, User Notifications combines data for
multiple events into a single notification. You can choose to send aggregated event
notifications quickly and frequently, which you might want to do for high-severity finding
events. Or send them less frequently to receive fewer notifications, which you might want to
do for low-severity finding events. If you combine event data, you can drill down to review
the details of each aggregated event by using the AWS User Notifications console. From there, you can also
navigate to each associated finding on the Amazon Macie console.

## Enabling and configuring AWS User Notifications for

Macie findings

To enable AWS User Notifications to generate notifications for Amazon Macie findings, create a
notification configuration for Macie in User Notifications. A _notification
configuration_ specifies the criteria for a rule. It also specifies delivery
channels and other settings for monitoring and sending notifications about Amazon EventBridge events
that match the rule's criteria. For detailed information about creating a notification
configuration, see [Getting started with
AWS User Notifications](../../../notifications/latest/userguide/getting-started.md "../../../notifications/latest/userguide/getting-started.md") in the _AWS User Notifications User Guide_.

To create a notification configuration for Macie findings, choose the following options
for the event rule:

- For **AWS service name**, choose **Macie**.
- For **Event type**, choose **Macie Finding**.
- For **Regions**, select each AWS Region in which you use Macie and
  want to be notified of findings.

With this configuration, User Notifications monitors EventBridge events for your AWS account and generates
notifications for all Macie finding events in the Regions that you selected. The events match
the following criteria:

- `source` equals `aws.macie`
- `detail-type` equals `Macie Finding`

The underlying JSON pattern for the event rule is:

```
{
    "source": ["aws.macie"],
    "detail-type": ["Macie Finding"]
}
```

To refine the rule and generate notifications only for a subset of findings, you can
customize the JSON pattern for the rule. To do this, specify additional criteria that derive
from the [Amazon EventBridge event schema for Macie
findings](findings-publish-event-schemas.md "findings-publish-event-schemas.md").

If you create a rule that uses a custom JSON pattern, you can create multiple notification
configurations for Macie findings. You can then tailor the delivery channels and other
settings for each configuration to align with your security and compliance workflows for
specific types of findings.

For example, you might create one rule that notifies you if Macie generates or updates a
_Policy:IAMUser/S3BucketPublic_ finding. In
this case, the pattern for the rule might be:

```
{
    "source": ["aws.macie"],
    "detail-type": ["Macie Finding"],
    "detail": {
        "type": ["Policy:IAMUser/S3BucketPublic"]
    }
}
```

And you might create another rule that notifies you if Macie generates a sensitive data
finding for an S3 bucket that's publicly accessible. In this case, the pattern for the rule
might be:

```
{
    "source": ["aws.macie"],
    "detail-type": ["Macie Finding"],
    "detail": {
        "type": [ { "prefix": "SensitiveData" } ],
        "resourcesAffected": {
            "effectivePermission": ["PUBLIC"]
        }
    }
}
```

If you create multiple notification configurations for Macie findings, it's a good idea to
ensure that the rule for each configuration is unique. Otherwise, you might receive duplicate
notifications for individual findings.

To learn more about customizing event patterns for rules, see [Using customized JSON event
patterns](../../../notifications/latest/userguide/common-usecases.md "../../../notifications/latest/userguide/common-usecases.md") in the _AWS User Notifications User Guide_.

## Mapping AWS User Notifications fields to Macie finding

fields

When AWS User Notifications generates a notification for an Amazon Macie finding, it populates the
notification with data from a subset of fields in the corresponding Amazon EventBridge event. These
fields provide key details of the associated finding, such as the finding's type and severity,
and the name of the affected resource.

If you review a notification on the AWS User Notifications console, the notification includes all the
data for this subset of fields. It also provides a link to the associated finding on the
Amazon Macie console. If you review a notification in other delivery channels, it might contain
data for only some of the fields. This is because User Notifications tailors the design and structure of
its notifications to work with each type of delivery channel that it supports.

The following table lists the fields that might be included in a notification for a
finding. In the table, the **Notification field** column describes (in
_italics_) or indicates the name of a field in a
notification. The **Finding event field** column uses dot notation to
indicate the name of the corresponding JSON field in an EventBridge event for a finding. The
**Description** column describes the data that's stored in the
field.

| Notification field          | Finding event field                                                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _Message headline_          | `detail.type`                                                                                                                                      | The finding's type. For example: `Policy:IAMUser/S3BucketPublic` or `SensitiveData:S3Object/Financial`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| _Summary_                   | `detail.title`                                                                                                                                     | The brief description of the finding. For example: `The S3 object contains financial information.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| _Description_               | `detail.description`                                                                                                                               | The full description of the finding. For example: `The S3 object contains financial information such as bank account numbers or credit card numbers.`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Severity                    | `detail.severity.description`                                                                                                                      | The qualitative representation of the finding's severity: `Low`, `Medium`, or `High`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Finding ID                  | `detail.id`                                                                                                                                        | The unique identifier for the finding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Created                     | `detail.createdAt`                                                                                                                                 | The date and time when Macie created the finding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Updated                     | `detail.updatedAt`                                                                                                                                 | The date and time when Macie most recently updated the finding. For sensitive data findings, this value is the same as the value for the _Created_ (`detail.createdAt`) field. All sensitive data findings are considered new (unique).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Affected S3 bucket          | `detail.resourcesAffected.s3Bucket.arn`                                                                                                            | The Amazon Resource Name (ARN) of the affected S3 bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Affected S3 object          | `detail.resourcesAffected.s3Object.path`                                                                                                           | The name (_key_) of the affected S3 object, including the name of the bucket that stores the object and, if applicable, the object's prefix. This field isn't included in notifications for policy findings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| _Sensitive data detections_ | `detail.classificationDetails.result.sensitiveData.detections...` And/Or `detail.classificationDetails.result.customDataIdentifiers.detections...` | This is a concatenation of multiple fields in an event for a sensitive data finding. This field isn't included in notifications for policy findings. If a managed data identifier detected the sensitive data, this field specifies the category, type, and number (`count`) of occurrences of the sensitive data that was detected. For example: `PERSONAL_INFORMATION: USA_SOCIAL_SECURITY_NUMBER 100 occurrences`. If a custom data identifier detected the sensitive data, this field specifies the name of the custom data identifier and the number (`count`) of occurrences of the sensitive data that was detected. For example: `Employee ID 20 occurrences`. If a finding reports multiple types of sensitive data, the notification includes data for up to four types. The data is populated first by any applicable custom data identifiers and then by any applicable managed data identifiers. | ## Changing AWS User Notifications settings for Macie findings You can change your AWS User Notifications settings for Amazon Macie findings at any time. To do this, edit the notification configuration in User Notifications. To learn how, see [Managing notification configurations](../../../notifications/latest/userguide/managing-notifications.md "../../../notifications/latest/userguide/managing-notifications.md") in the _AWS User Notifications User Guide_. If you have multiple notification configurations for Macie findings, changing the settings for one configuration doesn't affect the settings for your other configurations. You can edit all or only some of your configurations. ## Disabling AWS User Notifications for Macie findings To stop generating and receiving notifications from AWS User Notifications for Amazon Macie findings, delete the notification configuration in User Notifications. To learn how, see [Managing notification configurations](../../../notifications/latest/userguide/managing-notifications.md "../../../notifications/latest/userguide/managing-notifications.md") in the _AWS User Notifications User Guide_. If you have multiple notification configurations for Macie findings, deletion of one configuration doesn't affect your other configurations. You can delete all or only some of your configurations. |
