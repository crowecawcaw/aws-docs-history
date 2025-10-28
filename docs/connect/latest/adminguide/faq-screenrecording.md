# Frequently asked questions about Amazon Connect screen

recording capabilities

This topic provides frequently asked questions about using Amazon Connect screen recording
capabilities.

###### Contents

- [General specifications](#faq-sr-general "#faq-sr-general")
- [Configuration](#faq-sr-configuration "#faq-sr-configuration")
- [Performance](#faq-sr-performance "#faq-sr-performance")

## General specifications

- **What is the file format of screen
  recordings?**

The screen recording files are saved in MP4 format.

- **Which Amazon Connect channels are
  supported?**

You can generate screen recordings for voice, chat, and task
contacts.

- **Do you capture the entire screen?**

Yes, the Amazon Connect Client Service records all the open applications on the agent's monitor,
up to three monitors.

- **Does screen recording support concurrent user
  sessions on Windows using Virtual Desktop Infrastructure (VDI)
  environments?**

Yes, screen recording supports concurrent user sessions on Windows when
using Amazon Connect Client Application version 2.0.0 or later.

- **Where are the screen recording files stored in my
  AWS account?**

The screen recordings are delivered to your Amazon S3 bucket and encrypted
using the KMS key you specify. This is similar to how call recordings are
stored and encrypted.

- **How can I be notified when there is a latest version
  of the client application?**
  - For Windows, to be notified when there is an update to the
    Amazon Connect Client Application, we recommend subscribing to the RSS feed of this
    administrator guide. Choose the **RSS** link that
    appears under the title of this page (it's next to the PDF
    link).
  - For ChromeOS, Isolated Web App and Chrome Extension are hosted and
    managed by Amazon Connect. They are automatically updated as newer
    versions are published.

- **Can I opt only for screen recording and not for call
  recording?**

Yes, you can enable screen recording without call recording for a voice
call.

- **How do I find the Amazon S3 location of the screen
  recording?**

You can find the screen recording location in the [RecordingsInfo](ctr-data-model.md#ctr-RecordingsInfo "ctr-data-model.md#ctr-RecordingsInfo")
section of the contact record. See the **Location**
field.

- **How do I enable screen recording for a percentage of
  my contacts?**

You can use the [Distribute by
percentage](distribute-by-percentage.md "distribute-by-percentage.md") block in the flow to
enable a percentage of contacts for screen recording.

- **Is screen recording PCI compliant?**

Amazon Connect, including the screen recording capability, is compliant with the
Payment Card Industry Data Security Standard (PCI DSS). However, you are
responsible for determining whether your specific implementation meets your
compliance requirements.

###### Important

During a video call or screen sharing session, agents are able to see the
customer's video or screen share even when the customer is on hold. It is the customer's
responsibility to handle PII accordingly. If you want to change this behavior, you can build a
custom CCP and communication widget. For more information, see [Integrate in-app, web, video calling, and screen
sharing natively into your application](config-com-widget2.md "config-com-widget2.md").

- **Does screen recording work with custom CCP and agent
  desktops?**

Screen recording is designed to work with custom CCP and agent workspace
built with the [Amazon Connect
Streams JS library](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams"). We recommend testing your custom solution
before deploying screen recording in production.

- **Can I use screen recording anywhere in the
  world?**

Screen recording is available in AWS GovCloud (US) and all AWS commercial
Regions where Amazon Connect is available. However, your use of screen recording may
be subject to compliance with privacy and other laws. Please consult your
compliance team before enabling this capability for your agents.

To use screen recording in AWS GovCloud (US-West) requires client version
2.0.3 or later.

- **Are agents alerted when screen recording is enabled
  for a contact?**

By default Amazon Connect doesn't provide a notification feature. However, you can
use the [Amazon Connect Streams JS library](https://github.com/amazon-connect/amazon-connect-streams/blob/master/cheat-sheet.md "https://github.com/amazon-connect/amazon-connect-streams/blob/master/cheat-sheet.md") to create a notice or other visual
indicator on an agent's desktop to signal that screen recording is in
use.

- **What happens if an agent closes the browser during a
  contact, or immediately after a contact ends?**

If the browser is closed at the beginning of contact before any screen
capture data can be uploaded to Amazon Connect, the final screen recording may not be
published. If the browser is closed immediately after a contact ends but
before the final screen capture data can be uploaded, the screen recording
is published when the agent next logs in to CCP.

- **Does screen recording STOP when an agent places a
  customer on hold?**

No, the screen recording continues recording when an agent places a
customer on hold.

- **Is screen recording supported when Agents are logged
  into multiple CCP instances?**

No, screen recording is not supported when Agents are logged into multiple
CCP instances simultaneously either in the same or different browsers. You
might see inconsistent behavior with screen recordings in these
cases.

## Configuration

- **Can I opt only for screen recording and not for call
  recording?**

Yes, you can enable screen recording without call recording for a voice
call. To do so, disable voice recording in the [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md") block while keeping the
screen recording enabled.

- **How do I find the Amazon S3 location of the screen
  recording?**

You can find the screen recording location in the [RecordingsInfo](ctr-data-model.md#ctr-RecordingsInfo "ctr-data-model.md#ctr-RecordingsInfo")
section of the contact record. See the **Location**
field.

- **How do I enable screen recording for a percentage of
  my contacts?**

You can use the [Distribute by
percentage](distribute-by-percentage.md "distribute-by-percentage.md") block in the flow to
enable a percentage of contacts for screen recording.

- **What is the average size of a screen recording file
  per minute in S3?**

The average size of screen recording is 1.5MB/minute. This size can vary
depending on factors like video encoding etc.

- **What is the frame rate for screen recording and is
  this configurable?**

The screen is recorded at 5 frames per second and this is not
configurable.

- **What codec is used for screen
  recording?**

Screen recording uses OpenH264 codec.

- **Is there a way to choose which audio (redacted or
  unredacted) gets used for screen recording?**

No, today only the unredacted audio gets used for screen recording.

- **Is there a service limit for screen
  recording?**

No, there is no service limit or quota for screen recording
service.

- **Is there a maximum duration for screen
  recording?**

No, the screen recording solution imposes no maximum duration for a
recording.

- **How many agent monitors can be
  recorded?**

Screen recording can record up to 3 screens/monitors.

- **Can I configure my call/screen recording storage S3
  bucket to enable bucket level encryption with a KMS key that is
  different from the KMS key used as part of instance data storage
  configuration?**

No, the same key should be used at bucket level and also as part of
instance data storage configuration.

## Performance

- **What are the bandwidth requirements for screen
  recording?**

We recommend 500kbps per concurrent contact with screen recording enabled.

- **Why do I see higher CPU usage after installing
  screen recording client application on my windows
  machine?**

Screen recording in general is a CPU intensive application and hence CPU
utilization increase is expected. We recommend ensuring you provide
sufficient resources as documented in [System requirements](sr-system-req.md#sr-requirements "sr-system-req.md#sr-requirements") to avoid any resource contention
issues.
