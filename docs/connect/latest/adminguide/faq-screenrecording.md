# Frequently asked questions about Connect Customer screen recording capabilities

This topic provides frequently asked questions about using Connect Customer screen recording
capabilities.

###### Contents

- [Screen recording FAQ](#faq-screen-recording-questions "#faq-screen-recording-questions")
- [Rule-based redaction FAQ](#faq-sr-rule-based-redaction "#faq-sr-rule-based-redaction")

## Screen recording FAQ

### General specifications

- **What is the file format of screen
  recordings?**

The screen recording files are saved in MP4 format.

- **Which Connect Customer channels are
  supported?**

You can generate screen recordings for voice, chat, and task
contacts. Screen recording is not supported for email contacts.

- **Does screen recording support concurrent user
  sessions on Windows using Virtual Desktop Infrastructure (VDI)
  environments?**

Yes, screen recording supports concurrent user sessions on Windows when
using Connect Customer Client Application version 2.0.0 or later.

- **Where are the screen recording files stored in my
  AWS account?**

The screen recordings are delivered to your Amazon S3 bucket and encrypted
using the KMS key you specify. This is similar to how call recordings are
stored and encrypted.

- **How can I be notified when there is a latest version
  of the client application?**

  - For Windows, to be notified when there is an update to the
    Connect Customer Client Application, we recommend subscribing to the RSS feed of this
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

Connect Customer, including the screen recording capability, is compliant with the
Payment Card Industry Data Security Standard (PCI DSS). However, you are
responsible for determining whether your specific implementation meets your
compliance requirements.

###### Important

During a video call or screen sharing session, agents are able to see the
customer's video or screen share even when the customer is on hold. It is the customer's
responsibility to handle PII accordingly. If you want to change this behavior, you can build a
custom CCP and communication widget. For more information, see [Integrate in-app, web, video calling, and screen sharing natively into your application](config-com-widget2.md "config-com-widget2.md").

- **Does screen recording work with custom CCP and agent
  desktops?**

Screen recording is designed to work with custom CCP and agent workspace
built with the [Connect Customer
Streams JS library](https://github.com/amazon-connect/amazon-connect-streams "https://github.com/amazon-connect/amazon-connect-streams"). We recommend testing your custom solution
before deploying screen recording in production.

- **Can I use screen recording anywhere in the
  world?**

Screen recording is available in AWS GovCloud (US) and all AWS commercial
Regions where Connect Customer is available. However, your use of screen recording might
be subject to compliance with privacy and other laws. Please consult your
compliance team before enabling this capability for your agents.

To use screen recording in AWS GovCloud (US-West) requires client version
2.0.3 or later.

- **Are agents alerted when screen recording is enabled
  for a contact?**

By default Connect Customer doesn't provide a notification feature. However, you can
use the [Connect Customer Streams JS library](https://github.com/amazon-connect/amazon-connect-streams/blob/master/cheat-sheet.md "https://github.com/amazon-connect/amazon-connect-streams/blob/master/cheat-sheet.md") to create a notice or other visual
indicator on an agent's desktop to signal that screen recording is in
use.

- **What happens if an agent closes the browser during a
  contact, or immediately after a contact ends?**

If the browser is closed at the beginning of contact before any screen
capture data can be uploaded to Connect Customer, the final screen recording might not be
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

### Configuration

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
depending on factors like video encoding.

- **What is the frame rate for screen recording and is
  this configurable?**

The screen is recorded at 5 frames per second and this is not
configurable.

- **What codec is used for screen
  recording?**

Screen recording uses OpenH264 codec.

- **Is there a way to choose which audio (redacted or
  unredacted) gets used for screen recording?**

By default, the screen recording uses unredacted audio.

To preserve screen content and use redacted call audio, enable screen
recording and [rule-based
redaction](configure-rule-based-redaction.md "configure-rule-based-redaction.md") in the contact flow. Select
**Denylist** and leave the URL and window title rule
lists empty. Enable conversational analytics call recording redaction for the contact.

The resulting redacted screen recording preserves screen content and
contains redacted audio. Without conversational analytics call recording redaction, the redacted
screen recording has no audio.

Grant the **Screen recording (redacted) - Access**
permission to anyone who needs access to the redacted recording. Remove the
**Screen recording - Access** permission from anyone who
must not access the original recording.

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

- **Where are screen recordings
  stored?**

Screen recordings are delivered to your Amazon S3 bucket under your configured
prefix:

```
s3://`your-bucket`/`your-prefix`/`year`/`month`/`day`/`contact-id`_`UTC-timestamp`.mp4
```

Here, `your-prefix` is the Amazon S3 prefix configured
for your instance. The console default is
`connect/`your-instance-alias`/ScreenRecordings`,
and the prefix is configurable.

### Performance

- **What are the bandwidth requirements for screen
  recording?**

We recommend 500 Kbps bandwidth for screen recording, regardless of the
number of concurrent contacts. The system requirements specify 600 Kbps total
network bandwidth to account for additional agent workstation traffic.

- **Why do I see higher CPU usage after installing
  screen recording client application on my windows
  machine?**

Screen recording in general is a CPU intensive application and hence CPU
use increase is expected. We recommend making sure you provide
sufficient resources as documented in [System requirements](sr-system-req.md#sr-requirements "sr-system-req.md#sr-requirements") to avoid any resource contention
issues.

## Rule-based redaction FAQ

### General specifications

- **Do I need to replace my existing screen recording
  setup to use rule-based redaction?**

No. [Rule-based redaction
for screen recordings](rule-based-redaction-screen-recording.md "rule-based-redaction-screen-recording.md") is an
extension of Connect Customer agent screen recording. You enable it on a per-contact
basis through a contact flow.

- **Is there an additional charge for rule-based
  redaction?**

Rule-based redaction is included with Connect Customer agent screen recording at no
additional charge. Standard recording and storage rates apply.

- **Does rule-based redaction affect storage
  costs?**

Connect Customer stores both the unredacted and redacted recordings in your Amazon S3
bucket. You pay standard Amazon S3 storage rates for both files. If you do not need
to retain the unredacted originals, you can use an Amazon S3 lifecycle policy to
expire them on a shorter schedule than the redacted versions.

- **Does rule-based redaction apply to call
  recordings?**

Rule-based redaction applies only to agent screen recordings. It does not
redact audio. When rule-based redaction is enabled for a contact, Connect Customer
stitches the redacted video with the redacted call recording if conversational analytics call
recording redaction is also enabled for the contact, and with no audio
otherwise. To redact audio from call recordings, see [Use
sensitive data redaction with conversational analytics](sensitive-data-redaction.md "sensitive-data-redaction.md").

- **Does rule-based redaction use artificial
  intelligence or machine learning?**

No. Rule-based redaction is purely pattern matching. It evaluates each
browser page URL and application window title against the rules you
configure, and does not use artificial intelligence, machine learning, or
generative AI.

- **Can I redact only part of a page, such as a single
  form field?**

No. Rule-based redaction masks entire browser or application windows that
match a rule. Field-level redaction is not supported.

- **Does rule-based redaction work in Citrix or other
  virtual desktop environments?**

Yes, provided that the Connect Customer Client Application and the Connect Customer browser extension are installed
in the virtual desktop session. Performance depends on the virtual desktop
configuration.

- **What happens if an agent opens a matching URL in a
  private browsing window or an unsupported browser?**

Private browsing windows are reported by the Connect Customer browser extension the
same as regular windows and are redacted according to your URL rules. Browsers
other than Google Chrome, Microsoft Edge, and Mozilla Firefox do not report
URLs to the Connect Customer Client Application, so URL rules cannot match pages in those browsers. To
cover those cases, add window title rules that match on the browser's window
title, or use group policy to restrict agents to Chrome, Edge, or Firefox
during recorded contacts.

- **How does redaction behave with multiple browser
  windows or tabs, or when a matching page is left open in the
  background?**

Redaction follows what is visible on screen, not which window the agent is
actively using:

    + Each browser window is evaluated independently. A matching window
     is masked; non-matching windows remain visible.
    + For multiple tabs in the same window, redaction follows the visible
     tab. If the visible tab matches a rule, the whole window is masked. If
     a matching page is open but is not the visible tab, that window is not
     masked.
    + A matching window stays masked whenever it is visible, even if the
     agent is working in another window beside it. Only the visible portion
     is masked — if the matching window is covered, minimized, or on an
     inactive tab, there is nothing on screen to mask.
    + On the first contact after an agent begins their session, if a
     matching page was opened before the extension observed it, that window
     might briefly not be masked at the start of the recording. Redaction
     applies as soon as the agent selects any tab in the window, and
     subsequent contacts are unaffected.

- **Does rule-based redaction pause or stop the recording
  when a matching window is detected?**

No. The agent's screen is captured continuously throughout the contact.
Matching windows are masked only in the final redacted recording that is
produced after the contact ends; the capture itself is never paused.

- **Can I preview a redacted recording before the contact
  ends?**

No. Redaction is applied when the recording is assembled after the contact
ends.

- **Are agents notified when they visit a page that
  matches a redaction rule?**

No. Agents are not notified when a page or window matches a redaction rule.
Connect Customer does not provide a built-in notification for rule matches.

- **What browser information can the Connect Customer browser
  extension access?**

The extension only reads the URL of each browser page and the title of the
visible tab. It cannot access other browser data such as cookies, page
content, or browsing history. These URLs and window titles are the only
information used to match your redaction rules.

- **What APIs does rule-based redaction consume, and how
  are they authenticated?**

Rule-based redaction introduces no new public APIs, and the browser
extension consumes none. The extension communicates locally with the Connect Customer Client Application
on the agent's workstation using the browser's native messaging channel; the
extension is signed and scoped to the Connect Customer native messaging host. Redaction
reuses the existing screen recording upload path, so it inherits that path's
authentication and authorization — no additional credentials or permissions
are required.

- **What happens if the Connect Customer browser extension fails or
  is not running?**

Because redaction is applied after the contact ends, the extension does no
real-time video processing during the contact — it only reports page URLs and
window titles — so it is unlikely to affect the responsiveness of the agent's
desktop. The possible failure cases are:

    + If the extension is not installed or not running, URLs are not
     reported, so URL rules cannot match and browser pages that should be
     redacted by URL might appear in the recording. Window title rules do not
     depend on the extension and continue to work.
    + The extension does not connect to Connect Customer directly; it communicates
     with the Connect Customer Client Application on the agent's workstation. If the Connect Customer Client Application is not
     running, screen recording does not function at all — not only
     redaction.
    + If the extension fails to report a matching URL during a contact,
     that page is not masked in the final output, and the unredacted
     recording still contains the full capture.

For troubleshooting, see [Download log files for the screen
recording app](troubleshoot-sr.md "troubleshoot-sr.md").

### Configuration

- **Does rule-based redaction require conversational
  analytics?**

No. The URL and window-title matching that drives rule-based redaction is
independent of conversational analytics and works without it enabled. However, audio in the
_redacted_ recording does depend on it: when rule-based
redaction is enabled for a contact, the redacted screen recording is stitched
with the redacted call recording only if conversational analytics call recording redaction is
also enabled for that contact — otherwise the redacted recording has no
audio. The unredacted screen recording always uses the unredacted
audio.

- **Can I change the redaction rule during an active
  contact?**

No. The redaction configuration is fixed for the duration of a
contact.

- **Where are redacted recordings stored?**

Redacted recordings are stored in the same Amazon S3 bucket as the unredacted
recordings, as a sibling of the unredacted file. The redacted key is rooted
at the parent of your configured prefix, under a fixed
`Analysis/ScreenRecordings/Redacted/` path.

```
s3://`your-bucket`/`your-prefix-parent`/Analysis/ScreenRecordings/Redacted/`year`/`month`/`day`/`contact-id`_screen_recording_redacted_`UTC-timestamp`.mp4
```

In this path, `your-prefix-parent` is your
configured screen recordings prefix with its last segment removed. For
example, with the console default prefix
`connect/`your-instance-alias`/ScreenRecordings`,
redacted recordings are stored under
`connect/`your-instance-alias`/Analysis/ScreenRecordings/Redacted/`.

- **How can I audit whether a specific contact was
  recorded with redaction enabled?**

The flow that applied the redaction configuration is captured in the contact
record. For information about accessing contact records, see [Contact records data
model](ctr-data-model.md "ctr-data-model.md").

- **Can I use rule-based redaction with the
  SuspendContactRecording and ResumeContactRecording
  APIs?**

Yes. You can use the [SuspendContactRecording](../APIReference/API_SuspendContactRecording.md "../APIReference/API_SuspendContactRecording.md") and [ResumeContactRecording](../APIReference/API_ResumeContactRecording.md "../APIReference/API_ResumeContactRecording.md") APIs for screen recording in conjunction
with rule-based redaction.

### Performance

- **Does enabling rule-based redaction delay when a
  recording is available?**

Your unredacted screen recording is unaffected — it is captured, delivered,
and available on the same timeline as before. Redaction runs as a separate
post-processing step, so the redacted recording becomes available after both
the redacted screen recording and the redacted call recording have finished
processing.

- **How much CPU and memory does the browser extension
  add?**

The browser extension is lightweight — it only reports page URLs and window
titles to the Connect Customer Client Application — and adds roughly 1% additional CPU and memory usage
on top of the existing screen recording baseline. The most resource-intensive
component remains the screen capture process in the Connect Customer Client Application. Follow the
minimum system requirements in [System requirements](sr-system-req.md#sr-requirements "sr-system-req.md#sr-requirements").
