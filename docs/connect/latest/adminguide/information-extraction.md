

# Information extraction
<a name="information-extraction"></a>

Information extraction uses generative AI to extract information from conversations. That information could be verbatim — such as preferred name, invoice number, or reservation ID. Alternatively, it could be derived – such as reason for contact, resolution provided, or next steps promised. Information can be extracted from chat contacts or voice contacts with human agents. The extracted information is associated with the contact as structured data.

**Note**  
Information extraction is only available in [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html) instances.

Extracted information is available in the following locations:
+ **Contact Control Panel (CCP)** — During after-call work.
+ **Contact details page** — After the contact ends.
+ **Contact search** — Extracted information is displayed in the contact search results table.
+ **S3 files** — Extracted data is included in the conversational analytics output files stored in Amazon S3.
+ **API** — Via [ListRealtimeContactAnalysisSegments](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-contact-lens_ListRealtimeContactAnalysisSegments.html) (voice) and [ListRealtimeContactAnalysisSegmentsV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListRealtimeContactAnalysisSegmentsV2.html) (chat).
+ **Amazon Kinesis** — Extracted information events are delivered to your Kinesis data stream in real time.
+ **Rule actions** — Extracted information can be injected as variables into other rule actions, such as sending emails, creating tasks, creating cases, or sending notifications.

## How it works
<a name="information-extraction-how-it-works"></a>

Information extraction uses a large language model (LLM) to extract information from contacts — either verbatim information mentioned in the conversation, or derived information inferred from the conversation. You define what to extract by creating extraction definitions (Step 1), and when to extract by configuring rules (Step 2). When a rule fires, the LLM processes the contact content and returns the extracted information.

**Note**  
If a single extraction definition matches multiple times within a contact, all matches are returned as a list of results. For example, if you create an extraction definition for "Flight Number" and the conversation is about a round-trip, all flight numbers mentioned are returned: "XX123, YY567".

## Prerequisites
<a name="information-extraction-prerequisites"></a>

Before you configure information extraction, verify the following:
+ **Contact with conversational analytics** — Your flow must include a [Set recording and analytics behavior](set-recording-behavior.md) block with conversational analytics enabled.
+ **Security profile permissions** — Information extraction requires explicit permissions configured in the Security Profiles under [**Analytics and Optimization**](security-profile-list.md#analytics-list):

  For users that manage information extraction definitions:
  + **Conversational analytics** = View
  + **Information extraction - definitions** = All
  + **Rules** = All
  + **Rules - Generative AI** = All

  For users to view information extracted for a contact:
  + **Conversational analytics** = View
  + **Information extraction - results** = View

**Important**  
Information extraction operates on the raw contact content, before redaction is applied. This means you can extract sensitive data, wholly or in part. For example, you can redact the credit card number from a call recording and transcript while using information extraction to extract the last 6 digits of the credit card number.

## Known limitations
<a name="information-extraction-limitations"></a>
+ Maximum information extraction definitions per instance: 100
+ Maximum information extractions per contact with after-call work analytics rules: 20
+ Maximum information extractions per contact with post-contact analytics rules: 20

## Pricing
<a name="information-extraction-pricing"></a>

Information extraction is available in Amazon Connect Customer at no additional cost for voice and chat contacts.