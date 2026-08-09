# Information extraction

Information extraction uses generative AI to extract information from voice and chat
contacts. That information could be verbatim — such as preferred name, invoice number, or
reservation ID; or it could be derived – such as reason for contact, resolution provided, or
next steps promised. The extracted information is associated with the contact as structured
data.

###### Note

Information extraction is not available in [Amazon
Connect Customer Basic](enable-nextgeneration-amazonconnect.md "enable-nextgeneration-amazonconnect.md") instances.

Extracted information is available in the following locations:

- **Contact Control Panel (CCP)** — During
  after-call work.
- **Contact details page** — After the contact
  ends.
- **Contact search** — You can filter and search
  contacts based on extracted information.
- **S3 files** — Extracted data is included in the
  conversational analytics output files stored in Amazon S3.
- **API** — Via
  [ListRealtimeContactAnalysisSegments](../APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.md "../APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.md") (voice) and [ListRealtimeContactAnalysisSegmentsV2](../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md "../APIReference/API_ListRealtimeContactAnalysisSegmentsV2.md") (chat).
- **Amazon Kinesis** — Extracted information events are
  delivered to your Kinesis data stream in real time.
- **Rule actions** — Extracted information can be
  injected as variables into other rule actions, such as sending emails, creating
  tasks, creating cases, or sending notifications.

## How it works

Information extraction uses a large language model (LLM) to extract information from
contacts — either verbatim information mentioned in the conversation, or derived
information inferred from the conversation. You define what to extract by creating extraction
definitions (Step 1), and when to extract by configuring rules (Step 2). When a rule
fires, the LLM processes the contact content and returns the extracted
information.

###### Note

If a single extraction definition matches multiple times within a contact, all
matches are returned as a list of results. For example, if you create an extraction
definition for "Flight Number" and the conversation is about a round-trip, all flight numbers mentioned
are returned: "XX123, YY567".

## Prerequisites

Before you configure information extraction, verify the following:

- **Contact with conversational analytics** — Your
  flow must include a [Set recording and analytics
  behavior](set-recording-behavior.md "set-recording-behavior.md") block with conversational
  analytics enabled.
- **Security profile permissions** — Information
  extraction requires explicit permissions configured in the Security Profiles
  under [Analytics and Optimization](security-profile-list.md#analytics-list "security-profile-list.md#analytics-list"):

For users that manage information extraction definitions:

    + **Conversational analytics** = View
    + **Information extraction - definitions** = All
    + **Rules** = All
    + **Rules - Generative AI** = All

For users to view information extracted for a contact:

    + **Conversational analytics** = View
    + **Information extraction - results** = View

###### Important

Information extraction operates on the raw contact content, before redaction is
applied. This means you can extract sensitive data, wholly or in part. For example,
you can redact the credit card number from a call recording and transcript while using information extraction to extract
the last 6 digits of the credit card number.

## Known limitations

- Maximum information extraction definitions per instance: 100
- Maximum information extractions per contact: 20
- Maximum extracted information length: 3000 characters

## Pricing

Information extraction is included at no additional cost for voice and chat
contacts.

###### Contents

- [Configure voice and chat
  information extraction](information-extraction-configure.md "information-extraction-configure.md")
- [View extracted
  information](information-extraction-view.md "information-extraction-view.md")
- [Programmatic access to
  extracted information](information-extraction-programmatic.md "information-extraction-programmatic.md")
