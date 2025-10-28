# Delivery of Insights events

Unlike other types of events that CloudTrail captures, Insights events are logged only when CloudTrail
detects changes in your account's API usage that differ significantly from the account's
typical usage patterns.

Where CloudTrail delivers events and how long it takes to receive Insights events differs between
trails and event data stores.

**Insights events delivery for trails**

If you've enabled Insights events on a trail and CloudTrail detects unusual activity, CloudTrail delivers
Insights events to the `/CloudTrail-Insight` folder in the chosen destination S3
bucket for your trail. After you enable CloudTrail Insights for the first time on a trail, CloudTrail may
take up to 36 hours to begin delivering Insights events, provided that unusual activity is
detected during that time.

If you turn off Insights events logging on a trail and then re-enable Insights events, or stop and
restart logging on a trail, it can take up to 36 hours for CloudTrail to restart delivery of
Insights events, provided that unusual activity is detected during that time.

**Insights events delivery for event data stores**

If you've enabled Insights events on a source event data store, CloudTrail delivers Insights events to the
destination event data store. After you enable CloudTrail Insights for the first time on the source
event data store, CloudTrail may take up to 7 days to begin delivering Insights events to the
destination event data store, provided that unusual activity is detected during that
time.

If you turn off Insights events logging on a source event data store and then re-enable Insights events,
or stop and restart event ingestion on a source event data store, it can take up to 7
days for CloudTrail to restart delivery of Insights events, provided that unusual activity is detected
during that time. Additional charges apply for ingesting Insights events in CloudTrail Lake. You will
be charged separately if you enable Insights for both trails and event data stores. For
information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").
