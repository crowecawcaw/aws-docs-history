# Example conversational analytics output files for an email analyzed by conversational analytics

This section shows an example schema for an email contact that has been
analyzed by conversational analytics. The example shows
matched categories and a contact chain summary.

Note the following about email analytics output files:

- The `Channel` field is set to `EMAIL`.
- The `Version` field uses the `EMAIL` prefix
  (for example, `EMAIL-2026-01-01`).
- Email output files do not include sentiment scores, sentiment shift,
  loudness, or non-talk time data.
- The `Categories` section includes an
  `EventSource` field set to
  `OnEmailAnalysisAvailable`.
- Contact summaries use `ContactChainSummary` instead of
  `PostContactSummary`, because email analytics summarizes
  the full email thread (contact chain).
- The `CustomerMetadata.InputFiles` section references the
  email message and plain text files stored in Amazon S3.

## Example email analytics output file

The following example shows the output for an email contact with
categorization, redaction, and contact chain summary enabled.

```
{
  "Version": "EMAIL-2026-01-01",
  "AccountId": "123456789012",
  "Channel": "EMAIL",
  "Configuration": {
    "ChannelConfiguration": {
      "AnalyticsModes": [
        "ContactLens"
      ]
    },
    "LanguageLocale": "en-US",
    "RedactionConfiguration": {
      "Behavior": "Enable",
      "Policy": "RedactedAndOriginal",
      "Entities": [],
      "MaskMode": "EntityType"
    },
    "SummaryConfiguration": {
      "SummaryModes": [
        "ContactChain"
      ]
    }
  },
  "CustomerMetadata": {
    "ContactId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "InstanceId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "InputFiles": {
      "EmailMessageS3URI": "connect/your-instance/EmailMessages/2026/01/15/a1b2c3d4_message.json",
      "EmailMessagePlainTextS3URI": "connect/your-instance/EmailMessages/2026/01/15/a1b2c3d4_plain_text.json"
    }
  },
  "Categories": {
    "MatchedCategories": [
      "refund-request",
      "shipping-issue"
    ],
    "MatchedDetails": {
      "refund-request": {
        "PointsOfInterest": [
          {
            "Contacts": [
              {
                "ContactId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
              }
            ]
          }
        ],
        "EventSource": "OnEmailAnalysisAvailable"
      },
      "shipping-issue": {
        "PointsOfInterest": [],
        "EventSource": "OnEmailAnalysisAvailable"
      }
    }
  },
  "ConversationCharacteristics": {
    "ContactSummary": {
      "ContactChainSummary": {
        "Content": "The customer reported that their order arrived damaged and requested a full refund including shipping costs. The agent confirmed the refund would be processed within 3-5 business days and offered a replacement unit."
      }
    }
  },
  "JobDetails": {}
}
```
