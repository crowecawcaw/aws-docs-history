# Creating custom responses to Amazon Inspector findings with Amazon EventBridge

Amazon Inspector creates an event in [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") for newly generated findings and aggregated findings.
Amazon Inspector also creates an event for any changes to the state of a finding.
This means Amazon Inspector creates a new event for a finding when you take actions like restarting a resource or changing tags associated with a resource.
When Amazon Inspector creates a new event for an updated finding, the finding `id` stays the same.

###### Note

If your account is an Amazon Inspector delegated administrator account, EventBridge publishes events to your account and the member account where the events originated.

When using EventBridge events with Amazon Inspector, you can automate tasks to help you respond to security issues your findings reveal.
To receive notifications about Amazon Inspector findings based on EventBridge events, you must create [an EventBridge rule](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") and specify a target for Amazon Inspector.
The EventBridge rule allows EventBridge to send notifications for Amazon Inspector findings, and the target specifies where to send the notifications.

Amazon Inspector emits events to the default event bus in the AWS Region where you are currently using Amazon Inspector.
This means you must configure event rules for each AWS Region where you activated Amazon Inspector and configured Amazon Inspector to receive EventBridge events.
Amazon Inspector emits events on a best-effort basis.

This section provides you with an example of an event schema and describes how to create an EventBridge rule.

## Event schema

The following is an example of the Amazon Inspector event format for an EC2 finding event. For example
schema of other finding types and event types, see [Amazon EventBridge event schema for Amazon Inspector events](eventbridge-integration.md "eventbridge-integration.md").

```

{
    "version": "0",
    "id": "66a7a279-5f92-971c-6d3e-c92da0950992",
    "detail-type": "Inspector2 Finding",
    "source": "aws.inspector2",
    "account": "111122223333",
    "time": "2023-01-19T22:46:15Z",
    "region": "us-east-1",
    "resources": ["i-0c2a343f1948d5205"],
    "detail": {
        "awsAccountId": "111122223333",
        "description": "\n It was discovered that the sound subsystem in the Linux kernel contained a\n race condition in some situations. A local attacker could use this to cause\n a denial of service (system crash).",
        "exploitAvailable": "YES",
        "exploitabilityDetails": {
            "lastKnownExploitAt": "Oct 24, 2022, 11:08:59 PM"
        },
        "findingArn": "arn:aws:inspector2:us-east-1:111122223333:finding/FINDING_ID",
        "firstObservedAt": "Jan 19, 2023, 10:46:15 PM",
        "fixAvailable": "YES",
        "lastObservedAt": "Jan 19, 2023, 10:46:15 PM",
        "packageVulnerabilityDetails": {
            "cvss": [{
                "baseScore": 4.7,
                "scoringVector": "CVSS:3.1/AV:L/AC:H/PR:L/UI:N/S:U/C:N/I:N/A:H",
                "source": "NVD",
                "version": "3.1"
            }],
            "referenceUrls": ["https://lore.kernel.org/all/CAFcO6XN7JDM4xSXGhtusQfS2mSBcx50VJKwQpCq=WeLt57aaZA@mail.gmail.com/", "https://ubuntu.com/security/notices/USN-5792-1", "https://ubuntu.com/security/notices/USN-5791-2", "https://ubuntu.com/security/notices/USN-5791-1", "https://ubuntu.com/security/notices/USN-5793-2", "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=8423f0b6d513b259fdab9c9bf4aaa6188d054c2d", "https://ubuntu.com/security/notices/USN-5793-1", "https://ubuntu.com/security/notices/USN-5792-2", "https://ubuntu.com/security/notices/USN-5791-3", "https://ubuntu.com/security/notices/USN-5793-4", "https://ubuntu.com/security/notices/USN-5793-3", "https://git.kernel.org/linus/8423f0b6d513b259fdab9c9bf4aaa6188d054c2d(6.0-rc5)", "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-3303"],
            "relatedVulnerabilities": [],
            "source": "UBUNTU_CVE",
            "sourceUrl": "https://people.canonical.com/~ubuntu-security/cve/2022/CVE-2022-3303.html",
            "vendorCreatedAt": "Sep 27, 2022, 11:15:00 PM",
            "vendorSeverity": "medium",
            "vulnerabilityId": "CVE-2022-3303",
            "vulnerablePackages": [{
                "arch": "X86_64",
                "epoch": 0,
                "fixedInVersion": "0:5.15.0.1027.31~20.04.16",
                "name": "linux-image-aws",
                "packageManager": "OS",
                "remediation": "apt update && apt install --only-upgrade linux-image-aws",
                "version": "5.15.0.1026.30~20.04.16"
            }]
        },
        "remediation": {
            "recommendation": {
                "text": "None Provided"
            }
        },
        "resources": [{
            "details": {
                "awsEc2Instance": {
                    "iamInstanceProfileArn": "arn:aws:iam::111122223333:instance-profile/AmazonSSMRoleForInstancesQuickSetup",
                    "imageId": "ami-0b7ff1a8d69f1bb35",
                    "ipV4Addresses": ["172.31.85.212", "44.203.45.27"],
                    "ipV6Addresses": [],
                    "launchedAt": "Jan 19, 2023, 7:53:14 PM",
                    "platform": "UBUNTU_20_04",
                    "subnetId": "subnet-8213f2a3",
                    "type": "t2.micro",
                    "vpcId": "vpc-ab6650d1"
                }
            },
            "id": "i-0c2a343f1948d5205",
            "partition": "aws",
            "region": "us-east-1",
            "type": "AWS_EC2_INSTANCE"
        }],
        "severity": "MEDIUM",
        "status": "ACTIVE",
        "title": "CVE-2022-3303 - linux-image-aws",
        "type": "PACKAGE_VULNERABILITY",
        "updatedAt": "Jan 19, 2023, 10:46:15 PM"
    }
}

```

## Creating an EventBridge rule to notify

you of Amazon Inspector findings

To increase the visibility of Amazon Inspector findings, you can use EventBridge to set up automated
finding alerts that are sent to a messaging hub. This topic shows you how to send alerts
for `CRITICAL` and `HIGH` severity findings to email, Slack, or
Amazon Chime. You'll learn how to set up an Amazon Simple Notification Service topic and then connect that topic to an
EventBridge event rule.

### Step 1. Set up an Amazon SNS

topic and endpoint

To set up automatic alerts, you must first set up a topic in Amazon Simple Notification Service and add an
endpoint. For more information, refer to the [SNS guide](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md").

This procedure establishes where you want to send Amazon Inspector findings data. The SNS
topic can be added to an EventBridge event rule during or after the creation of the event
rule.

Email setup

###### Creating an SNS topic

1. Sign in to the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. From the navigation pane, select **Topics**,
   and then select **Create Topic**.
3. In the **Create topic** section, select
   **Standard**. Next, enter a topic name,
   such as `Inspector_to_Email`. Other details
   are optional.
4. Choose **Create Topic**. This opens a new
   panel with details for your new topic.
5. In the **Subscriptions** section, select
   **Create Subscription**.
6. 1. From the **Protocol** menu, select
      **Email**.
   2. In the **Endpoint** field, enter the
      email address that you would like to receive
      notifications.

   ###### Note

   You will be required to confirm your subscription
   through your email client after creating the
   subscription. 3. Choose **Create
   subscription**.

7. Look for a subscription message in your inbox and choose
   **Confirm Subscription**.

Slack setup

###### Creating an SNS topic

1. Sign in to the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. From the navigation pane, select **Topics**,
   and then select **Create Topic**.
3. In the **Create topic** section, select
   **Standard**. Next, enter a topic name,
   such as `Inspector_to_Slack`. Other details
   are optional. Choose **Create topic** to
   complete endpoint creation.

###### Configuring an Amazon Q Developer in chat applications client

1. Navigate to the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. From the **Configured clients** pane, select
   **Configure new client**.
3. Choose **Slack**, and then choose
   **Configure** to confirm.

###### Note

When choosing Slack, you must confirm permissions for
Amazon Q Developer in chat applications to access your channel by selecting
**allow**. 4. Select **Configure new channel** to open the
configuration details pane.

    1. Enter a name for the channel.
    2. For **Slack channel**, choose the
     channel that you want to use.
    3. In Slack, copy the channel ID of the private channel
     by right-clicking on the channel name and selecting
     **Copy Link**.
    4. On the AWS Management Console, in the Amazon Q Developer in chat applications window, paste the
     channel ID that you copied from Slack into the
     **Private channel ID** field.
    5. In **Permissions**,
     choose to create an IAM role using a template if you
     do not already have a role.
    6. For **Policy** templates,
     choose **Notification
     permissions**. This is the IAM policy
     template for Amazon Q Developer in chat applications. This policy provides the necessary
     read and list permissions for CloudWatch alarms, events, and
     logs, and for Amazon SNS topics.
    7. For **Channel guardrail policies**,
     choose
     **AmazonInspector2ReadOnlyAccess**.
    8. Choose the Region in which you previously created your
     SNS topic, and then select the Amazon SNS topic you created
     to send notifications to the Slack channel.

5. Select **Configure**.

Amazon Chime setup

###### Creating an SNS topic

1. Sign in to the Amazon SNS console at [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. Select **Topics** from the navigation pane,
   and then select **Create Topic**.
3. In the **Create topic** section, select
   **Standard**. Next, enter a topic name,
   such as `Inspector_to_Chime`. Other details
   are optional. Choose **Create topic** to
   complete.

###### Configuring an Amazon Q Developer in chat applications client

1. Navigate to the Amazon Q Developer in chat applications console at [https://console.aws.amazon.com/chatbot/](https://console.aws.amazon.com/chatbot/ "https://console.aws.amazon.com/chatbot/").
2. From the **Configured clients** panel, select
   **Configure new client**.
3. Choose **Chime**, and then choose
   **Configure** to confirm.
4. From the **Configuration details** pane,
   enter a name for the channel.
5. In Amazon Chime, open the desired chat room.
   1. Choose the gear icon in the upper-right corner and
      choose **Manage webhooks and
      bots**.
   2. Select **Copy URL** to copy the
      webhook URL to your clipboard.

6. On the AWS Management Console, in the Amazon Q Developer in chat applications window, paste the URL you
   copied into the **Webhook URL** field.
7. In **Permissions**, choose to
   create an IAM role using a template if you do not already have
   a role.
8. For **Policy** templates, choose
   **Notification permissions**. This is the
   IAM policy template for Amazon Q Developer in chat applications. It provides the necessary read
   and list permissions for CloudWatch alarms, events, and logs, and for
   Amazon SNS topics.
9. Choose the Region in which you previously created your SNS
   topic, and then select the Amazon SNS topic you created to send
   notifications to the Amazon Chime room.
10. Select **Configure**.

### Step 2. Create

an EventBridge rule for Amazon Inspector findings

1. Sign in using your credentials.
2. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
3. Select **Rules** from the navigation pane, and then
   select **Create rule**.
4. Enter a name and optional description for your rule.
5. Select **Rule with an event pattern** and then
   **Next**.
6. In the **Event Pattern** pane, choose **Custom
   patterns (JSON editor)**.
7. Paste the following JSON into the editor.

```
{
  "source": ["aws.inspector2"],
  "detail-type": ["Inspector2 Finding"],
  "detail": {
    "severity": ["HIGH", "CRITICAL"],
    "status": ["ACTIVE"]
  }
}
```

###### Note

This pattern sends notifications for any active `CRITICAL`
or `HIGH` severity finding detected by Amazon Inspector.

Select **Next** when you are finished entering the event
pattern. 8. On the **Select targets** page, choose
**AWS service**. Then, for **Select target
type**, choose **SNS topic**. 9. For **Topic**, select the name of the SNS topic you
created in step 1. Then choose **Next**. 10. Add optional tags if needed and choose **Next**. 11. Review your rule and then choose **Create rule**.

## EventBridge for Amazon Inspector multi-account

environments

If you're an Amazon Inspector delegated administrator, EventBridge rules appear on your account based on
applicable findings from your member accounts. If you set up findings notifications
through EventBridge in your administrator account, as detailed in the preceding section, you'll
receive notifications about multiple accounts. In other words, you'll be notified of
findings and events generated by your member accounts in addition to those generated by
your own account.

You can use the `accountId` from the finding's JSON details to identify the
member account from which the Amazon Inspector finding originated.
