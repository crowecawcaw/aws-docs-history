

# Track segment membership changes in Connect Customer
<a name="customer-segments-membership-events"></a>

You can subscribe a segment to receive notifications whenever the membership of the segment changes. A membership change occurs when a customer profile enters or exits the segment based on the segment criteria. This can happen because of a change in a profile, an associated object, or a calculated attribute. Membership changes are determined in two ways:
+ **Near real-time changes** — When membership changes because of a change to profile attributes, objects, or calculated attributes, Connect Customer Customer Profiles sends the event as a near real-time (`LIVE`) update.
+ **Time-based changes** — When membership changes because of a time-based aspect of the segment criteria, Customer Profiles evaluates membership on a schedule and compares it against the previous known state to determine changes (`SCHEDULE`).

Customer Profiles sends both types of notification to the Amazon Kinesis data stream that you configure for segment membership changes, using the IAM role that you provide.

**Note**  
To access the segmentation builder experience in the Connect Customer admin website, make sure that the appropriate security profile permissions are configured. For more information, see [Assign security profile permissions to manage customer segments](security-profile-customer-profile-segmentation.md).
Before you subscribe to membership events, you must enable segment membership streaming to set the destination Kinesis data stream for membership changes. For more information, see [Set up segment membership streaming](#customer-segments-membership-events-streaming).
You can create a subscription only after the segment is created. You can create a maximum of 10 segment subscriptions for each domain.

## Set up segment membership streaming
<a name="customer-segments-membership-events-streaming"></a>

Enabling segment membership streaming is a one-time setup that an administrator performs for the domain. It sets the destination Kinesis data stream that membership events are delivered to. Enabling the stream does not enable membership events by default — you must also subscribe individual segments to receive notifications, and the same Kinesis data stream is shared across all subscribed segments in the domain.

**To enable segment membership streaming for your domain**

1. Open the Connect Customer Customer Profiles console.

1. Choose the **Data export** tab, and then choose **Enable event streaming**.  
![The Data export tab with the Enable event streaming button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/enable-real-time-export-1.png)

1. Under **Segment membership changes**, choose **Enable data streaming**, and then select an existing Kinesis data stream from the drop-down menu, or choose **create a new Kinesis data stream** to open the Kinesis console and create the stream. For more information, see [Creating and managing streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html).  
![The Segment membership changes section showing the Enable data streaming options with a Kinesis data stream selected from the drop-down menu.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-enable-streaming.png)

1. For **Role name**, specify an IAM role that grants Customer Profiles permission to write to your Kinesis data stream, or choose **Create role in IAM** to create one.

1. Choose **Enable data streaming** to save your settings.

When you enable segment membership streaming, Customer Profiles assumes the role that you specify. Because of this, the IAM principal that enables streaming must have permission to pass that role to Customer Profiles. Grant the `iam:PassRole` action for the Kinesis role to the principal, scoped to the Customer Profiles service. The following is a sample statement to add to the principal's permissions.

```
{
    "Effect": "Allow",
    "Action": "iam:PassRole",
    "Resource": "arn:aws:iam::123456789012:role/my-segment-events-role",
    "Condition": {
        "StringEquals": {
            "iam:PassedToService": "profile.amazonaws.com"
        }
    }
}
```

The IAM role that you provide must trust the Customer Profiles service principal and grant permissions to write to the Kinesis data stream. The following is a sample trust policy for the Kinesis role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "profile.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

The following is a sample of the permissions to grant the Kinesis role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord",
                "kinesis:PutRecords",
                "kinesis:DescribeStream"
            ],
            "Resource": "arn:aws:kinesis:us-west-2:123456789012:stream/my-segment-events-stream"
        }
    ]
}
```

If your Kinesis data stream is encrypted with a customer managed AWS KMS key, the role also needs permission to use that key to write to the stream. Add the following statement, scoped to your AWS KMS key, to the role's permissions.

```
{
    "Effect": "Allow",
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-123456SAMPLE"
}
```

**To disable segment membership streaming for your domain**

1. Open the Connect Customer Customer Profiles console.

1. Choose the **Data export** tab, and then choose **Disable segment membership**.  
![The Event streams section showing the Disable profile changes and Disable segment membership buttons above the active stream details.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-disable-streaming.png)

## Key concepts
<a name="customer-segments-membership-events-concepts"></a>

The following terms are important for understanding segment membership events.

**Subscription**  
You enable a subscription on a segment to receive membership events that identify the change of state, along with a timestamp, for a given profile.

**Initial snapshot**  
Before evaluating membership changes, Customer Profiles creates an initial snapshot that preserves the current membership status for existing profiles. This snapshot is the source of truth that is used to determine membership changes. While Customer Profiles takes the snapshot, the subscription is in the `STARTING` state. After it completes, you begin to see results.

**SCHEDULE and LIVE events**  
The type of event that you receive depends on when and how Customer Profiles evaluated the membership.  
A `SCHEDULE` event is sent from a scheduled run. Scheduled runs occur every 24 hours by default when you subscribe through the API, and every hour by default from the Connect Customer admin website. You can configure the interval to a minimum of 1 hour and a maximum of 24 hours. Each scheduled run takes a fresh snapshot and compares the membership status of each profile against the previous snapshot. Scheduled runs are best-effort: the interval is a target cadence rather than a guaranteed run time, so a run might be delayed or skipped, for example if the previous scheduled run has not finished. Customer Profiles sends you a notification for any changes in membership.  
A `LIVE` event is sent in near real time, outside of the scheduled runs, when membership changes because of a change to a profile attribute, object, or calculated attribute. Customer Profiles evaluates the affected profile as the change occurs and sends a notification if its membership changed.

## Enable and view events
<a name="customer-segments-membership-events-enable"></a>

After a segment is created, you can enable the subscription from the Connect Customer admin website by choosing **Track membership changes**.

![The Segment membership changes section showing no membership changes tracked, with the Track membership changes button.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-track-changes.png)


After you enable tracking, Customer Profiles sends notifications to the Kinesis data stream associated with segment membership changes. If your administrator has not configured a stream, a message prompts you to enable segment membership streaming first.

![A message prompting you to enable segment membership streaming before subscribing to membership events.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-no-stream-warning.png)


After tracking is enabled, you see messages that provide detail about the initial snapshot.

![The Segment membership changes section with an information message that changes will appear after the initial snapshot completes.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-initial-snapshot.png)


### Viewing events
<a name="customer-segments-membership-events-view"></a>

Events are published to the Kinesis data stream in your account. After the initial snapshot completes, you can also view streaming events from the same section, and you can view membership event details on individual profiles. There might be a delay between when a membership change occurs and when it appears in the list of streaming events.

![The Segment membership changes table listing timestamps, profile IDs, and Joined membership statuses.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-view-events.png)


## Stop tracking changes
<a name="customer-segments-membership-events-stop"></a>

If you no longer want to receive notifications, choose **Stop tracking changes**.

![The Segment membership changes table with the Stop tracking changes button highlighted.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-stop-tracking.png)


## CloudWatch metrics
<a name="customer-segments-membership-events-metrics"></a>

You can view CloudWatch metrics for your segment membership events under your domain and segment. The following metrics are available.

`ProfilesJoined`  
The number of profiles that entered the segment.

`ProfilesLeft`  
The number of profiles that left the segment.

`NotificationsFailed`  
The number of notification events that failed.

`ScheduledRunsSucceeded`  
The number of scheduled runs that succeeded.

![The CloudWatch metrics browser filtered to customerProfiles, showing the ProfilesJoined metric by domain and segment.](http://docs.aws.amazon.com/connect/latest/adminguide/images/customer-segments-membership-events-cloudwatch-metrics.png)


## Segment membership changes payload
<a name="customer-segments-membership-events-payload"></a>

Customer Profiles sends this event to your Kinesis data stream each time a customer profile enters or exits a segment. The following is a sample segment membership event in JSON.

```
{
    "AccountId": "123456789012",
    "DomainName": "cp-domain-prod",
    "SegmentDefinitionName": "PeopleInSeattle",
    "SegmentType": "CLASSIC",
    "ProfileId": "0d25b61368c64fb786347d7e7314c6f1",
    "OperationType": "JOINED",
    "MembershipCalculatedAt": 1773967675,
    "PreviousMembershipChangedAt": 1773965432,
    "EventType": "LIVE"
}
```

The following list describes the fields in the segment membership event payload.

**AccountId**  
The AWS account receiving the event.

**DomainName**  
The name of the Customer Profiles domain where the segment is defined.

**SegmentDefinitionName**  
The name of the segment whose membership changed.

**SegmentType**  
The type of segment that the notification came from.  
+ `CLASSIC`: A segment built with audience groups and filters. For more information, see [Build customer segments in Connect Customer](customer-segments-building-segments.md).
+ `ENHANCED`: A segment defined with SQL.

**ProfileId**  
The unique identifier of the profile whose membership changed.

**OperationType**  
+ `JOINED`: The profile became a member of the segment.
+ `LEFT`: The profile is no longer a member of the segment.

**MembershipCalculatedAt**  
The time at which the membership was evaluated.

**PreviousMembershipChangedAt**  
The time at which the previous membership change was identified.

**EventType**  
+ `LIVE`: The membership was evaluated in near real-time.
+ `SCHEDULE`: The membership was evaluated during a scheduled run, and this notification reflects the membership at the time of that run.