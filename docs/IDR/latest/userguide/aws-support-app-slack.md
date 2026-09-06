

# Manage Incident Detection and Response support cases with the AWS Support App in Slack
<a name="aws-support-app-slack"></a>

With the [AWS Support App in Slack](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html), you can manage your Support cases in Slack, receive notifications about new [alarm initiated incidents](https://docs.aws.amazon.com/IDR/latest/userguide/incidents-idr.html) on your AWS Incident Detection and Response workload, and create [Incident Response Requests](https://docs.aws.amazon.com/IDR/latest/userguide/inbound-incident-idr.html).

To configure the AWS Support App in Slack, follow the instructions provided in the [*Support User Guide*](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html). 

**Important**  
To receive notifications in Slack for all alarm initiated incidents on your workload, you must configure the AWS Support App in Slack for all your workload’s accounts that are onboarded to AWS Incident Detection and Response. Support cases are created in the account that the workload alarm originated in.
Multiple high-severity support cases can be opened on your behalf during an incident to engage Support resolvers. You receive notifications in Slack for all support cases that are opened during an incident that match your [notification configuration for the Slack channel](https://docs.aws.amazon.com/awssupport/latest/user/add-your-slack-channel.html).
Notifications that you receive through the AWS Support App in Slack don't replace your workload’s initial and escalation contacts that are engaged via email or phone call by AWS Incident Detection and Response during an incident.

**Topics**
+ [Alarm-initiated incident notifications in Slack](#aws-support-app-slack-alarm-initiated)
+ [Create an Incident Response Request in Slack](#aws-support-app-slack-create-ir)

## Alarm-initiated incident notifications in Slack
<a name="aws-support-app-slack-alarm-initiated"></a>

After you configure the AWS Support App in Slack in your Slack channel, you receive notifications about alarm initiated incidents on your AWS Incident Detection and Response monitored workload.

The following example shows how notifications for alarm initiated incidents appear in Slack.

**Example notification**

When your alarm initiated incident is acknowledged by AWS Incident Detection and Response, a notification similar to the following generates in Slack:

![Acknowledgement notification in Slack](http://docs.aws.amazon.com/IDR/latest/userguide/images/slack-app-acknowledgement.png)


To view the full correspondence added by AWS Incident Detection and Response, choose** See details**.

![Acknowledgement notification in Slack correspondence](http://docs.aws.amazon.com/IDR/latest/userguide/images/slack-app-acknowledgement-correspondence.png)


Further updates from AWS Incident Detection and Response appear in the case’s thread. 

![View further details in the case thread](http://docs.aws.amazon.com/IDR/latest/userguide/images/slack-app-further-updates.png)


Choose **See details** to view the full correspondence added by AWS Incident Detection and Response.

![See the full correspondence](http://docs.aws.amazon.com/IDR/latest/userguide/images/slack-app-details.png)


## Create an Incident Response Request in Slack
<a name="aws-support-app-slack-create-ir"></a>

For instructions on how to create an Incident Response Request through the AWS Support App in Slack, see [Request an Incident Response](inbound-incident-idr.md).