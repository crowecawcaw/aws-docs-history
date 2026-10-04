

# Connected Services portal and subscription plane
<a name="connected-services-portal"></a>

The Connected Services portal exposes CMS’s existing data model — signal catalog, vehicle models, ECUs, decoder manifests, data-collection campaigns, and simulation — as a subscriber-facing surface, alongside a subscription plane that streams data products to authorized third-party consumers. The three stacks below are all opt-in.

## ConnectedServicesUiStack (`DEPLOY_CONNECTED_SERVICES_UI=true`)
<a name="connected-services-ui-stack"></a>

Deploys a standalone React SPA on its own CloudFront distribution and subdomain (`cms-{stage}-connected-services-ui`). The portal reads six surfaces directly from CMS’s deployed `data_processing_api.py` — signal catalog, vehicle models, ECUs, decoder manifests, data-collection campaigns, and simulation. It owns no data-model storage; every surface is read directly from the source-of-truth API, so nothing is duplicated between CMS and the portal.

## SubscriptionsStack (`DEPLOY_SUBSCRIPTIONS=true`)
<a name="subscriptions-stack"></a>

Deploys the subscription plane in `services/connectors/subscriptions/`. The plane manages subscriber identities and enrollment lifecycle, tracks vehicle-scoped access permissions (subscription scope), streams records from data products to authorized subscribers, and enforces subscriber-scoped quotas. A dedicated `subscriber` Cognito group grants access to the subscriber-facing REST routes; admin routes (`POST /admin/subscribers`, `POST /admin/subscriptions/vehicles/{vin}/available`) require the `connected-services` group.

The bundled `products.json` catalog seeds the four data products shipped today: `telemetry-hifi-v1`, `meridian-telemetry-v1`, `diagnostics-v1`, and `charging-sessions-v1`. Subscriptions live in the `cms-{stage}-storage-subscriptions-{region}-{account}` DynamoDB table with a GSI on `consumer_id` for "my subscriptions" ordering by creation time; vehicle availability lives in `cms-{stage}-storage-vehicle-availability-{region}-{account}`.

## Subscription ownership authorization
<a name="cs-subscription-authorization"></a>

Subscription ownership is derived from the row’s `consumer_id` field, which is written from the caller’s Cognito `sub` claim at create time and is immutable thereafter. Every subsequent read or write on a subscription re-reads the row and compares `row.consumer_id == claims["sub"]`; a mismatch returns HTTP 403. A JWT `custom:subscriptionIds` claim was previously considered as an ownership signal but was found to have no writer path; it is retired and does not participate in authorization.

## ConnectedServicesConsumerStack (`DEPLOY_CONNECTED_SERVICES_CONSUMER=true`)
<a name="connected-services-consumer-stack"></a>

Deploys a CMS-side feed-cache DynamoDB table (`cms-{stage}-storage-cs-feed-cache-{region}-{account}`) that supports the Fleet Manager portal’s own consumption of the subscription plane. CMS runs a single machine subscriber account in the producer’s Cognito pool with one subscription to `telemetry-hifi-v1`; the enrollment path an operator triggers from Vehicle Detail is the same `POST /subscriptions/{id}/scope` call an external subscriber makes, so the demo exercises the real contract rather than a CMS-privileged shortcut. See [Third-party data delivery](third-party-data-delivery.md) for the delivery-pattern framing and the Connected Services subscription plane’s role within it.

 **Partial in this release.** The feed-cache table is deployed and the read-through proxy routes are wired, but nothing currently reads or writes the cache — the CMS-side proxy calls the producer live on every request. The authorization contract holds either way; freshness/TTL is deferred.