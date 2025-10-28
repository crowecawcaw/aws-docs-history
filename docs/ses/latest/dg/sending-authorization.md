# Using sending authorization with Amazon SES

You can configure Amazon SES to authorize other users to send emails from the identities that
you own (domains or email addresses) using their own Amazon SES accounts. With the
_sending authorization_ feature, you can maintain control over your
identities so that you can change or revoke permissions at any time. For example, if you're
a business owner, you can use sending authorization to enable a third party (such as an
email marketing company) to send email from a domain you own.

This chapter covers the specifics of sending authorization which replaces the legacy
cross-account notifications feature. You should first understand the basics of identity
based authorization using authorization policies as explained in [Using identity authorization in
Amazon SES](identity-authorization-policies.md "identity-authorization-policies.md") which covers important topics such as
the anatomy of an authorization policy and how to manage your polices.

## Cross-account

notifications legacy support

Feedback notifications for bounces, complaints, and deliveries associated with email
sent from a delegate sender that's been authorized by an identity owner to send from one
of his verified identities, have traditionally been configured using cross-account
notifications where the delegate sender would
associate a topic with an identity they didn't own (that’s the cross-account). However,
cross-account notifications have been replaced by using configuration sets and verified
identities in association with delegate sending where the delegate sender has been
authorized by the identity owner to use one of their verified identities to send email
from. This new method allows the flexibility to configure bounce, complaint, delivery,
and other event notifications by the following two constructs depending if you're the
delegate sender or the owner of the verified identity:

- Configuration sets – The delegate sender
  can set up event publishing in his own configuration set that he can specify
  when sending email from a verified identity he doesn't own, but has been
  authorized to send from by the identity owner through an authorization policy.
  Event publishing allows bounce, complaint, delivery, and other event
  notifications to be published to Amazon CloudWatch, Amazon Data Firehose, Amazon Pinpoint, and Amazon SNS. See
  [Create event
  destinations](event-destinations-manage.md "event-destinations-manage.md").
- Verified identities – Besides having the
  identity owner authorize the delegate sender to use one of his verified
  identities to send email from, he can also, at the request of the delegate
  sender, configure feedback notifications on the shared identity to use
  SNS topics owned by the delegate sender. Only the delegate sender will
  get these notifications because they own the SNS topic. See Step 14 for
  how to [configure an "SNS
  topic you don't own"](sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own "sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own") in the authorization policy procedures.

###### Note

For compatibility, cross-account notifications are being supported for legacy
cross-account notifications currently being used in your account. This support is
limited to being able to modify and use any current cross-accounts you created in
the Amazon SES classic console; however, you can no longer create
_new_ cross-account notifications. To create new ones in the
Amazon SES new console, use the new methods of delegate sending either with configuration
sets using [event publishing](event-destinations-manage.md "event-destinations-manage.md"), or
with verified identities [configured
with your own SNS topics](sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own "sending-authorization-identity-owner-tasks-policy.md#configure-sns-topic-you-dont-own").

###### Topics

- [Overview of Amazon SES sending
  authorization](sending-authorization-overview.md "sending-authorization-overview.md")
- [Identity owner tasks for Amazon SES
  sending authorization](sending-authorization-identity-owner-tasks.md "sending-authorization-identity-owner-tasks.md")
- [Delegate sender tasks for
  Amazon SES sending authorization](sending-authorization-delegate-sender-tasks.md "sending-authorization-delegate-sender-tasks.md")
