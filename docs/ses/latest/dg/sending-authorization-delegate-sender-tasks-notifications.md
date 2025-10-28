# Using delegate

sender notifications for Amazon SES sending authorization

As a delegate sender, you're sending emails on behalf of an identity that you don't own,
but are authorized to use; however, bounces and complaints still count toward
_your_ bounce and complaint metrics, not those of the identity
owner.

If the bounce or complaint rates for your account gets too high, your account is at risk
of being placed under review or have its ability to send email paused. For this reason, it's
important that you set up notifications and have a process in place to monitor them. You
also need to have a process in place for removing addresses that have bounced or complained
from your mailing lists.

Therefore, as a delegate sender, you can configure Amazon SES to send notifications when bounce
and complaint events occur for the emails you send on behalf of any identities that you
don't own, but have been authorized to use by the identity owner. You can also set up [event publishing](monitor-using-event-publishing.md "monitor-using-event-publishing.md") to publish bounce and
complaint notifications to Amazon SNS or Firehose.

###### Note

If you set up Amazon SES to send notifications by using Amazon SNS, you're charged standard
Amazon SNS rates for the notifications you receive. For more information, see the [Amazon SNS pricing page](https://aws.amazon.com/sns/pricing "https://aws.amazon.com/sns/pricing").

## Create a

new delegate sender notification

You can set up delegate sending notifications with either configuration sets using
[event publishing](event-destinations-manage.md "event-destinations-manage.md"), or with verified
identities [configured with your own
SNS topics](sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own "sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own").

Procedures are given below for setting up new delegate sending notifications using
either method:

- Event publishing through a configuration set
- Feedback notifications to SNS topics you own

###### To set up event publishing through a configuration set for your delegate sending

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. Follow the procedures in [Create event
   destinations](event-destinations-manage.md "event-destinations-manage.md").
3. After you've set up event publishing in your configuration set, specify the
   name of the configuration set when you send email as a delegate sender using the
   verified identity the identity owner authorized you to send from. See [Sending
   emails for the identity owner](sending-authorization-delegate-sender-tasks-email.md "sending-authorization-delegate-sender-tasks-email.md").

###### To set up feedback notifications to SNS topics you own for your delegate

sending

1. After you've decided which of your SNS topics you'd like to use for
   feedback notifications, follow the procedures [to find your SNS topic ARN](sending-authorization-delegate-sender-tasks-information.md#find-sns-topic-arn "sending-authorization-delegate-sender-tasks-information.md#find-sns-topic-arn") and copy the full ARN and share it
   with your identity owner.
2. Ask your identity owner to configure your SNS topics for feedback
   notifications on the shared identity he's authorized you to send from. (Your
   identity owner will need to follow the procedures given for [configuring SNS
   topics](sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own "sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own") in the authorization policy procedures.)
