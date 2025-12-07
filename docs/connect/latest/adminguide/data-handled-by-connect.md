# Data handled by Amazon Connect

Data held within Amazon Connect is segregated by the AWS account ID and the Amazon Connect instance
ID. This ensures that data can be accessed only by the authorized users of a specific
Amazon Connect instance.

Amazon Connect handles a variety of data related to the contact center, including but not
limited to the following categories.

- **Resources and configurations** – This includes
  queues, flows, users, routing profiles, and task templates.
- **Contact metadata** – This includes connection
  time, handle time, source number (ANI), destination number (DNIS), and user
  defined contact attributes.
- **Agent-related performance data** – This
  includes login time, status changes, and contacts handled.
- **Phone call audio streams** – When enabled,
  this also includes call recordings.
- **Chat transcripts** – Included only if enabled
  in flows.
- **Screen recordings** – Included only if enabled
  in flows.
- **Attachments** – Included only if enabled at the
  instance level.
- **Integration configuration** – Includes user
  defined name, description and metadata when creating integration with external
  applications.
- **Knowledge documents** – This includes documents
  used by agents to handle contacts.
- **Voiceprints** – When Amazon Connect Voice ID is enabled,
  a voiceprint is created from the customer's voice for future authentication.
  Similarly, a voiceprint is created while registering a fraudster in the
  Voice ID system for future fraud detection.
- **Speaker and Fraudster Audio** – When
  Amazon Connect Voice ID is enabled, the audio used for enrolling speakers and registering
  fraudsters is stored so that Voice ID can re-enroll and reregister them in
  future when there is a need to do so.
- **Forecasts, capacity plans, and schedules** –
  Included only if enabled and created.
  Amazon Connect stores the following Personally Identifiable Information (PII) data related to
  your customers:

- The customer's phone number: ANI for inbound calls, and DNIS for outbound
  calls or transfers.
- If you are using Amazon Connect Customer Profiles, all this data could potentially be
  PII. This data is always encrypted at rest using either a customer managed key or an
  AWS owned key. The Amazon Connect Customer Profiles data is segregated by the AWS
  account ID and the domain. Multiple Amazon Connect instances can share a single Customer
  Profiles domain.
- For outbound campaigns, Amazon Pinpoint passes customer phone numbers and relevant attributes to
  Amazon Connect. On the Amazon Connect side, these are always encrypted at rest using either a
  customer managed key or an AWS owned key. The outbound campaigns data is segregated by the Amazon Connect
  instance ID and are encrypted by instance-specific keys.

## External application data

Amazon AppIntegrations enables you to integrate with external applications. It stores
references to other AWS resources and client-service specified metadata. No data
is stored other than incidentally while being processed. When syncing data
periodically with an Amazon Connect service, data is encrypted using a customer managed key and stored
temporarily for one month.

## Phone call media

Amazon Connect is in the audio path for calls handled by the service. It is therefore
responsible for relaying the call’s media stream between participants. This can
include the audio between a customer and a flow / IVR, the audio between a customer
and an agent, or mixing the audio between multiple parties in a conference or during
a transfer. There are two types of phone calls:

- PSTN calls. This includes inbound customer calls, outbound calls placed by
  agents to customers, and calls to an agent’s physical phone, if this option
  has been enabled in the Contact Control Panel (CCP).
- Softphone calls placed to the agent’s browser.

PSTN calls are connected between Amazon Connect and various telecommunications carriers
using either private circuits maintained between Amazon Connect and our providers or existing
AWS internet connectivity. For PSTN calls routed over the public internet,
signaling is encrypted with TLS and the audio media is encrypted with SRTP.

Softphone calls are established to the agent’s browser with an encrypted WebSocket
connection using TLS. The audio media traffic to the browser is encrypted in transit
using DTLS-SRTP.

## Call recordings and screen

recordings

At the instance-level, by default the call recording and screen recording
capabilities are available when an Amazon S3 bucket is created for them. You determine
which contacts are recorded by specifying it in the flows. This allows for more
detailed control over which contacts are recorded.

Note the following behavior for call recordings:

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

Screen recording only records the agent's screen if the contact is enabled for
screen recording. Screen recording begins when the agent accepts a contact and ends
with the agent completes the after contact work. Screen recording supports the
voice, chat, and task channels.

###### Important

During a video call or screen sharing session, agents are able to see the
customer's video or screen share even when the customer is on hold. It is the customer's
responsibility to handle PII accordingly. If you want to change this behavior, you can build a
custom CCP and communication widget. For more information, see [Integrate in-app, web, video calling, and screen
sharing natively into your application](config-com-widget2.md "config-com-widget2.md").

You can limit access to the call and screen recordings based on user permissions.
Recordings can be searched and played back within the Amazon Connect admin website.

### Call recording and screen recording

storage

Call and screen recordings are stored in two phases:

- Recordings intermediately held within Amazon Connect during and after the
  contact, but before delivery.
- Recordings delivered to your Amazon S3 bucket.

The recordings that are stored in your Amazon S3 bucket are secured using a
KMS key that was configured when your instance was created.

At all times, you maintain full control over the security of call recordings
delivered to your Amazon S3 bucket.

### Access to call recordings and screen

recordings

You can search for and listen to call recordings or view screen recordings in
Amazon Connect. To determine which users can do this, assign them the appropriate
permissions in their security profile. If AWS CloudTrail is enabled, access to
specific recordings by Amazon Connect users is captured in CloudTrail.

The capabilities of Amazon S3, AWS KMS, and IAM put you in full control of who has
access to call recording data.

## Contact metadata

Amazon Connect stores metadata related to contacts that flow through the system and allows
authorized users to access this information. The Contact Search feature allows you
to search and view contact data, such as origination phone numbers or other
attributes set by the flow, that are associated with a contact for diagnostics or
reporting purposes.

Contact
data classified as PII that is stored by Amazon Connect is encrypted at rest using a key that
is time-limited and specific to the Amazon Connect instance. Specifically, the customer
origination phone number is cryptographically hashed with a key that is specific to
the instance to allow for use in contact search.
For
contact search, the encryption key is not time-sensitive.

The following data stored by Amazon Connect is treated as sensitive:

- Origination phone number
- Outbound phone number
- External numbers dialed by agents for transfers
- External numbers transferred to by a flow
- Contact name
- Contact description
- All contact attributes
- All contact references

## Contact Lens real-time

processing

Content processed by Contact Lens in real-time is encrypted at rest and in
transit. Data is encrypted with keys owned by Contact Lens.

Contact Lens persists data (transcript, category names, etc.) on the Amazon Connect
side for a short period of time. This is to ensure that the API serves data
continuously, for up to 24h after contact terminates.

## Voiceprints and Voice ID audio

recordings

When you enable Amazon Connect Voice ID, it computes voiceprints out of your customer's
speech for authenticating them in future, and stores the data. Similarly, when you
enable fraud detection, it stores the voiceprint for each fraudster registered in
Voice ID.

While enrolling a customer into Voice ID for authentication and fraud detection,
you must specify a `CustomerSpeakerId` for them. Since Voice ID stores
biometric information for each speaker, we strongly recommend that you use an
identifier that does not contain PII in the `CustomerSpeakerId` field.

## Speaker and Fraudster

Audio

When you enable Amazon Connect Voice ID, it stores a compacted version of the audio (called
utterances) that it aggregated while enrolling a speaker or registering a fraudster.
This audio is used in the future whenever the voiceprints for the speakers and
fraudsters need to be regenerated. The data is retained until the speaker/fraudster
is deleted. The original audio used for enrollment or evaluation is deleted after a
24 hour retention period.

The data is retained until the speaker/fraudster is deleted or opted out.

## Outbound campaigns

For outbound campaigns, Amazon Pinpoint passes customer phone numbers and relevant attributes to
Amazon Connect. On Amazon Connect, these are always encrypted at rest using either a customer managed key or an
AWS owned key. The outbound campaigns data is segregated by the Amazon Connect instance ID and are
encrypted by instance specific keys.

## Task templates

Any processing of task template resources in Amazon Connect is encrypted at rest and in
transit. Data is encrypted with an AWS KMS key.

## Forecasts, Capacity Plans, and

Schedules

When forecasts, capacity plans, and schedules are generated, they are always
encrypted at rest and in transit. Data is encrypted with an AWS KMS key.
