# When, what, and where for contact recordings

in Amazon Connect

This topic explains when conversations are recorded, where recordings are stored, and
how to access them. It also provides best practices for managing recordings and
transcripts.

###### Contents

- [When is a conversation
  recorded?](#when-conversation-recorded "#when-conversation-recorded")
- [Where are recordings and transcripts
  stored?](#where-are-recordings-stored "#where-are-recordings-stored")
- [When are recordings
  available?](#when-are-recordings-available "#when-are-recordings-available")
- [Prevent agents from accessing
  recordings](#recording-prevent-access "#recording-prevent-access")
- [Headset requirements for listening
  to recordings](#recording-headset-requirements "#recording-headset-requirements")

## When is a conversation

recorded?

- The call recording feature has options for choosing whether to record the customer and system audio during IVR interactions
  or any combination of customer, agent, or both during agent interactions.
- There are a total of two possible recordings per contact: one for automated interactions (that is, IVR)
  and one for agent interactions. Enabling or disabling recording for automated interactions takes effect immediately.
  Conversely, modifying recording for agent interactions only takes effect after the agent joins the call.
- Agent audio is NOT transmitted to Amazon Connect when the agent is not on a call. On November 9, 2023, Amazon Connect deployed an optimization to
  improve agent productivity that pre-configures the microphone media stream of the agent's browser before the contact arrives.
  This reduces setup time for both incoming and outgoing calls. As a result, the microphone icon in the agent's browser appears to be on, even
  when the agent is not on a call.
- When a customer is on hold during agent interaction, the agent is still recorded.
- The transfer conversation between agents is recorded.
- When a call is transferred during a flow or IVR interaction (for example, by using the Transfer to phone number block)
  the recording continues to capture what the customer says and hears even after they are tranferred to an external voice system.
- Any transfers to external numbers during the agent interaction are not recorded after the agent leaves the
  call.
- If a participant mutes their own microphone, for example, to consult with a
  someone sitting next to them, their side-bar conversation is not recorded.

## Where are recordings and transcripts

stored?

Agents and contacts are stored on separate, stereo audio channels.

- For automated (IVR) interactions, the stereo file contains customer audio
  in the right channel and system prompts in the left channel.
- For agent interactions, the agent audio is stored in the right channel and
  customer (as well conferenced third parties) audio in the left
  channel.

Recordings are stored in the Amazon S3 bucket that are [created for your instance](amazon-connect-instances.md#get-started-data-storage "amazon-connect-instances.md#get-started-data-storage"). Any user or
application with the appropriate permissions can access the recordings in the Amazon S3
bucket.

Encryption is enabled by default for all call recordings using Amazon S3 server-side
encryption with KMS. The encryption is at the object level. The reports and
recording objects are encrypted; there's no encryption at the bucket level.

You shouldn't disable encryption.

###### Important

- For voice conversations to be stored in an Amazon S3 bucket, you need to
  enable recording in the flow block using the [Set recording and analytics
  behavior](set-recording-behavior.md "set-recording-behavior.md") block.
- For chat conversations, if there's an S3 bucket for storing chat
  transcripts, then all chats are recorded and stored there. If no bucket
  exists, then no chats are recorded. However, if you want to monitor chat
  conversations, you still need to add the [Set recording and analytics
  behavior](set-recording-behavior.md "set-recording-behavior.md") block to the
  flow.
- If a recording is moved from one S3 bucket to another for any reason,
  such as the retention period has expired, then the recording will no
  longer be accessible by Amazon Connect.

###### Tip

We recommend using the contact ID to search
for recordings.

Even though many call recordings for specific contact IDs may be named with
the contact ID prefix itself (for example, 123456-aaaa-bbbb-3223-2323234.wav),
there is no guarantee that the contact IDs and name of the contact recording
file _always_ match. By using **Contact ID**
for your search on the [Contact search](search-recordings.md "search-recordings.md")
page, you can find the correct recording by referring to the audio file on the
contact record.

## When are recordings

available?

When the recording for an agent interaction is enabled, the recording is placed in
your S3 bucket shortly after the contact is disconnected. When IVR recording is
enabled, the recording is placed in your S3 bucket shortly after the contact is
disconnected or once the call is answered by an agent. You can [review the recording](review-recorded-conversations.md "review-recorded-conversations.md") for both
agent interactions and automated interactions (IVR)..

###### Important

You can also access the recording from the customer's [contact record](sample-ctr.md "sample-ctr.md"). The recording is available in
the contact record, however, only after the contact has left the [After Contact Work (ACW) state](metrics-agent-status.md#agent-status-acw "metrics-agent-status.md#agent-status-acw"). The IVR
recording becomes available shortly after the call gets connected to the agent
or contact is disconnected.

###### Tip

Amazon Connect uses the Amazon S3
[PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") and [MultipartUpload](../../../AmazonS3/latest/API/API_MultipartUpload.md "../../../AmazonS3/latest/API/API_MultipartUpload.md")
APIs to upload the call recording to your S3 bucket. If you are using [S3 Event Notifications](../../../AmazonS3/latest/userguide/NotificationHowTo.md "../../../AmazonS3/latest/userguide/NotificationHowTo.md") when call recordings are uploaded
successfully to your bucket, make sure you enable the notification for
**All object create events**, or for both
_s3:ObjectCreated:Put_ and
_s3:ObjectCreated:CompleteMultipartUpload_ event types.

## Prevent agents from accessing

recordings

To prevent agents from accessing recordings outside of their agent hierarchy,
assign them the **Restrict contact access** security profile
permission. For more information, see [Assign permissions to review
past contact center conversations in Amazon Connect](assign-permissions-to-review-recordings.md "assign-permissions-to-review-recordings.md").

## Headset requirements for listening

to recordings

You need to use an output device (headset or other device) that supports stereo
output so you can hear both the agent and customer audio.

Agent and customer recordings are presented in two separate channels. With a full
headset, each side will play one channel. But for a one-ear headset, there isn't a
mechanism to mix two channels into one.
