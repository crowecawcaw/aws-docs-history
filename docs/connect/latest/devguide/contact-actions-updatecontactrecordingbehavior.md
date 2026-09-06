

# UpdateContactRecordingBehavior
<a name="contact-actions-updatecontactrecordingbehavior"></a>

Sets contact recording behavior, including analysis behavior and which participants of the contact to record. 

## Parameter object
<a name="updatecontactrecordingbehavior-parameter"></a>

```
{
    "RecordingBehavior": { an object that holds the recording behavior
        "RecordedParticipants": [ ] a list of participants to record, chosen from "Agent" and "Customer". An empty list disables recording. Must be set statically.
        "ScreenRecordedParticipants": [ ] a list of participants for which to record their screen, can only include "Agent". Must be set statically.
        "IVRRecordingBehavior": Can be either "Enabled" or "Disabled". Must be set statically.
    },    
    "AnalyticsBehavior": { an object that holds the analytics behavior. Can only be set if the RecordedParticipants contains both Agent and Customer
        "Enabled": either "True" or "False". Must be set statically.
        "AnalyticsLanguage": Must be one of languages supported by Contact Lens post-call analysis. Must be set statically. Use the format xx-XX, for example, en-US for US English.
        "AnalyticsRedactionBehavior": either Enabled or Disabled. Defaults to Disabled if not set. Determines whether to redact sensitive data, such as personal information, in the Contact Lens output file and audio recording.
        "AnalyticsRedactionResults": either "RedactedAndOriginal" or "RedactedOnly". Can be set dynamically. Determines whether the customer gets both the redacted and the original transcripts and audio files, or just the redacted transcripts and audio files.
        "AnalyticsRedactionMaskMode": either "EntityType" or "PII".  Must be set statically.
        "AnalyticsRedactionEntities": ["BANK_ACCOUNT_NUMBER", "BANK_ROUTING", "CREDIT_DEBIT_NUMBER", "CREDIT_DEBIT_CVV", "CREDIT_DEBIT_EXPIRY", "INTERNATIONAL_BANK_ACCOUNT_NUMBER", "PIN", "SWIFT_CODE", "CA_HEALTH_NUMBER", "UK_NATIONAL_HEALTH_SERVICE_NUMBER", "CA_SOCIAL_INSURANCE_NUMBER", "SSN", "UK_NATIONAL_INSURANCE_NUMBER", "PASSPORT_NUMBER", "DRIVER_ID", "IN_AADHAAR", "NAME", "AGE", "EMAIL", "PHONE", "ADDRESS", "US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER", "UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER", "IN_PERMANENT_ACCOUNT_NUMBER", "IN_NREGA", "AWS_ACCESS_KEY", "AWS_SECRET_KEY", "IP_ADDRESS", "MAC_ADDRESS", "PASSWORD", "URL", "USERNAME", "LICENSE_PLATE", "VEHICLE_IDENTIFICATION_NUMBER", "IN_VOTER_NUMBER", "DATE_TIME", "AGENT_DISPLAY_NAME", "CUSTOMER_DISPLAY_NAME", "ATTACHMENT_NAME"],
        "ChannelConfiguration": {
          "Chat": {
            "AnalyticsModes": ["ContactLens"]  Can only be set to ContactLens
          },
         "Voice": {
            "AnalyticsModes": ["RealTime"]  Can be set to RealTime and PostContact
          } 
       },
        "SummaryConfiguration": {
            "SummaryModes": ["PostContact"] Optional parameter to enable post-contact summary. At present we only support "PostContact".
        },
         "SentimentConfiguration": {
            "Enabled": either "True" or "False". Must be set statically.
        }
    }
}
```

**Notes**
+ `AnalyticsRedactionMaskMode`: Optional, String. Allowed values:
  + `PII`: All PII data is replaced with `[PII]`. For example, Jane Doe is replaced with `[PII]`
  + `EntityType`: Each PII entity is replaced with its type. For example, Jane Doe is replaced with `[NAME]`.
  + If no value is provided, the default `PII` is used.
+ `AnalyticsRedactionEntities`: Optional, Array of strings. 
  + Valid values include: "BANK\_ACCOUNT\_NUMBER", "BANK\_ROUTING", "CREDIT\_DEBIT\_NUMBER", "CREDIT\_DEBIT\_CVV", "CREDIT\_DEBIT\_EXPIRY", "INTERNATIONAL\_BANK\_ACCOUNT\_NUMBER", "PIN", "SWIFT\_CODE", "CA\_HEALTH\_NUMBER", "UK\_NATIONAL\_HEALTH\_SERVICE\_NUMBER", "CA\_SOCIAL\_INSURANCE\_NUMBER", "SSN", "UK\_NATIONAL\_INSURANCE\_NUMBER", "PASSPORT\_NUMBER", "DRIVER\_ID", "IN\_AADHAAR", "NAME", "AGE", "EMAIL", "PHONE", "ADDRESS", "US\_INDIVIDUAL\_TAX\_IDENTIFICATION\_NUMBER", "UK\_UNIQUE\_TAXPAYER\_REFERENCE\_NUMBER", "IN\_PERMANENT\_ACCOUNT\_NUMBER", "IN\_NREGA", "AWS\_ACCESS\_KEY", "AWS\_SECRET\_KEY", "IP\_ADDRESS", "MAC\_ADDRESS", "PASSWORD", "URL", "USERNAME", "LICENSE\_PLATE", "VEHICLE\_IDENTIFICATION\_NUMBER", "IN\_VOTER\_NUMBER", "DATE\_TIME", "AGENT\_DISPLAY\_NAME", "CUSTOMER\_DISPLAY\_NAME", "ATTACHMENT\_NAME".
  + An empty array is not allowed. 
  + If `AnalyticsRedactionEntities` is not present, the default "redact all PII data" is used.

For more information on sensitive data redaction, see [Enable redaction of sensitive data](https://docs.aws.amazon.com/connect/latest/adminguide/enable-redaction.html) in the *Connect Customer Administrator's Guide*.

For a list of languages supported by Contact Lens post-call analysis, see [Contact Lens supported languages](https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages-contact-lens.html). For the 4-character language code to use, see [Supported languages](https://docs.aws.amazon.com/transcribe/latest/dg/supported-languages.html) in the *Amazon Transcribe Developer Guide*.

## Results and conditions
<a name="updatecontactrecordingbehavior-results"></a>

None.

## Errors
<a name="updatecontactrecordingbehavior-errors"></a>

None.

## Restrictions
<a name="updatecontactrecordingbehavior-restrictions"></a>

This is supported only in contact flows, transfer flows, outbound whispers, and customer queue flows. This is not supported in agent/customer whispers or hold flows. 

Analytics is only supported by the voice channel.

## Corresponding block in the UI
<a name="updatecontactrecordingbehavior-ui"></a>

[Set recording and analytics behavior](https://docs.aws.amazon.com/connect/latest/adminguide/set-recording-behavior.html) 