**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Restoring chat messages

###### Note

You must be an Amazon Chime Enterprise account administrator to complete these
steps.

You can restore chat messages within 30 days of setting a chat retention period. When
you restore chat messages, you restore all the messages sent by all the users in your
Amazon Chime account.

Within that 30-day period, you can do either of the following to restore
messages:

- Use the Amazon Chime Console to turn off data retention.

—OR—

- Lengthen the retention period.
  After the 30-day grace period, all chat messages that fall under the retention period
  are permanently deleted. New chat messages are permanently deleted as soon as they pass
  the retention period.

For information about setting or changing a retention period, see [Turning on chat retention](turn-on-chat-retention.md "turn-on-chat-retention.md"), earlier
in this section.

Chat messages are also permanently deleted from Amazon Chime when you or an account member
perform either of the following actions:

- Delete an Amazon Chime chat room. For more information about deleting chat rooms, see
  [Deleting chat rooms](../ug/delete-chat-room.md "../ug/delete-chat-room.md"), in the _Amazon Chime User
  Guide_.
- End an Amazon Chime meeting in which chat messages are present.

###### Note

As needed, you can manually copy and save chat messages from a meeting,
but you must do so before the meeting ends. For more information, see [Using
in-meeting chat](../ug/meeting-chat.md "../ug/meeting-chat.md"), in the _Amazon Chime User
Guide_.
