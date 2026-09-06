

# Estimate traffic requirements for CDN and MediaTailor integrations
<a name="estimate-traffic"></a>

To accurately size your content delivery network (CDN) integration with AWS Elemental MediaTailor:

1. Calculate your expected viewer concurrency using historical data or similar events. Plan for additional capacity beyond your baseline to handle unexpected spikes. For current scaling recommendations, consult with your AWS account team. You can also see [Quotas in AWS Elemental MediaTailor](quotas.md).

1. Identify peak traffic patterns and potential spikes in your content schedule. Consider factors like:
   + Live sports events or season premieres
   + Marketing campaigns or promotional events
   + Time zone differences for global audiences
   + Holiday or seasonal viewing patterns

1. Determine your bandwidth requirements by multiplying viewer counts by stream bitrates. Work with your CDN provider to calculate appropriate capacity. Base this calculation on your specific content bitrates and expected audience size. Add overhead for ad segments and manifest requests as your provider recommends.

1. Work with your CDN provider to ensure sufficient edge capacity in your target regions.

Ensure your ad insertion capacity meets viewer demand by taking these specific actions:

1. Check your current ad insertion requests quota in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/mediatailor/quotas). Review the current service limits to understand how many concurrent viewers your configuration can support.

1. For high-traffic events, request an increased quota through the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/mediatailor/quotas).

1. If you expect more than 500,000 concurrent viewers, then contact [AWS Support](https://aws.amazon.com/premiumsupport/) at least 2 weeks before your event. This allows AWS to ensure sufficient capacity for your ad personalization needs.

For more information about implementing capacity planning in your workflow, see [Using prefetch scheduling](https://docs.aws.amazon.com/mediatailor/latest/ug/prefetch.html) to optimize ad delivery for high-traffic events.