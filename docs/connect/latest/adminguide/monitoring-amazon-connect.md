

# Monitor live and recorded conversations using Connect Customer conversational analytics
<a name="monitoring-amazon-connect"></a>

Managers can monitor or listen-in to live conversations between agents and contacts. They can also review and download recordings of past interactions for both automated interactions (IVR) and agent interactions. 

Connect Customer provides two options to set up contact monitoring:
+ **Multi-party contacts**: Monitor live conversations that have up to six participants. There's no additional charge for this option.

  With this option, you can [barge](monitor-barge.md) into live conversations (voice and chats), and record chat transcripts.

  You enable this capability on the Connect Customer console by choosing **Enable Multi-Party Calls and Enhanced Monitoring for Voice** and **Enable Multi-Party Chats and Enhanced Monitoring for Chat**, as shown in the following image.   
![The Telephony and chat options page, the enhanced contact monitoring capabilities section.](http://docs.aws.amazon.com/connect/latest/adminguide/images/barge-voice-chat-enable.png)
+ **Three-party voice contacts**: Monitor conversations that have up to three participants. This is the default behavior. There's no additional charge for this option.

  You cannot barge into calls or chats.

  You enable this capability by adding a [Set recording and analytics behavior](set-recording-behavior.md) block to your flow.

How agents manage the conferencing experience is very different between these two options. Enhanced monitoring provides more functionality for the agents. See [Comparison of enhanced contact monitoring (multi-party) and three-party functionality in Connect Customer](three-party-multi-party-comparison.md).

**Important**  
New events are added to the agent event stream when you choose **Enhanced contact monitoring capabilities**.   
If you choose to start with the default three-party capability enabled by the [Set recording and analytics behavior](set-recording-behavior.md) block, and then later switch to **Enhanced contact monitoring capabilities**, know that new events will be added to the agent event stream. This will cause problems if you have customized your contact center based on the previous agent event stream.

**Topics**
+ [When, what, and where for contact recordings](about-recording-behavior.md)
+ [How to set up S3 Object Lock for immutable call recordings](s3-object-lock-call-recordings.md)
+ [Comparison of multi-party and three-party functionality](three-party-multi-party-comparison.md)
+ [Enable enhanced multi-party contact monitoring](monitor-conversations.md)
+ [Enable three-party call monitoring](enable-three-party-monitoring.md)
+ [Enable contact recording](set-up-recordings.md)
+ [Assign permissions](monitor-conversations-permissions.md)
+ [Monitor live conversations](monitor-conversations-howto.md)
+ [Barge live voice and chat conversations](monitor-barge.md)
+ [Review recorded conversations](review-recorded-conversations.md)
+ [Troubleshoot monitoring conversations](ts-monitoring-conversations.md)