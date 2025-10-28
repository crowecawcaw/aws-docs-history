# Resilience in Amazon DataZone

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between zones without interruption. Availability Zones are more highly available,
fault tolerant, and scalable than traditional single or multiple data center
infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon DataZone offers several features to help
support your data resiliency and backup needs.

###### Topics

- [Data source
  resilience](#disaster-recovery-resiliency-data-source "#disaster-recovery-resiliency-data-source")
- [Asset resilience](#disaster-recovery-resiliency-asset "#disaster-recovery-resiliency-asset")
- [Asset type and metadata
  form resilience](#disaster-recovery-resiliency-asset-type-form "#disaster-recovery-resiliency-asset-type-form")
- [Glossary resilience](#disaster-recovery-resiliency-glossary "#disaster-recovery-resiliency-glossary")
- [Global search
  resilience](#disaster-recovery-resiliency-global-search "#disaster-recovery-resiliency-global-search")
- [Subscription
  resilience](#disaster-recovery-resiliency-subscription "#disaster-recovery-resiliency-subscription")
- [Environment
  resilience](#disaster-recovery-resiliency-environment "#disaster-recovery-resiliency-environment")
- [Environment
  blueprint resilience](#disaster-recovery-resiliency-environment-blueprint "#disaster-recovery-resiliency-environment-blueprint")
- [Project resilience](#disaster-recovery-resiliency-project "#disaster-recovery-resiliency-project")
- [RAM resilience](#disaster-recovery-resiliency-ram "#disaster-recovery-resiliency-ram")
- [User profile
  management resilience](#disaster-recovery-resiliency-user-profile-management "#disaster-recovery-resiliency-user-profile-management")
- [Domain resilience](#disaster-recovery-resiliency-domain "#disaster-recovery-resiliency-domain")

## Data source

resilience

During an Amazon DataZone availability event, `DataSource` jobs will
periodically retry for up to 24 hours. If a job fails due to a misconfiguration, a
`DataSourceRunFailed` event will be emitted. If the Amazon DataZone domain is
configured with a KMS key, and the AmazonDataZoneDomainExecutionRole loses access to
this key during a job run, the run will end in the `INACCESSIBLE` state.
Once KMS access is restored, the job should be manually updated to trigger the
transition back to a useable state.

## Asset resilience

In Amazon DataZone, assets are versioned. If a version of an asset needs to be rolled back,
you can create a new version using content of the last stable version. An asset version
can be published. A published version of an asset cannot be edited, except by publishing
a new version. A published asset (aka listing) can be subscribed to. To prevent new
subscriptions to an asset, it can be unpublished. Un-publishing an asset does not have
an effect on the existing subscriptions. Deleting an asset will delete all unpublished
versions of the asset. Published versions of the asset must be deleted separately. A
published version of an asset can be deleted only if there are no subscriptions.

## Asset type and metadata

form resilience

In Amazon DataZone, asset types and metadata form types are versioned. An asset type cannot
be deleted if it is in use by an asset. A metadata form type cannot be deleted if it is
in use by an asset type or an asset. If you don’t want specific metadata-form-type to be
used for curation, you can disable them which doesn’t affect the ones it’s already
attached to.

## Glossary resilience

In Amazon DataZone, glossaries and glossary terms cannot be deleted if they are in use. If
you don’t want specific glossary or glossary-term to be used for curation, you can
disable them which doesn’t affect the ones it’s already attached to.

## Global search

resilience

In Amazon DataZone, published assets (aka listings) can be discovered through global
search. Publishing of an asset can be rolled back by unpublishing the asset.
Unpublishing an asset does not affect existing subscriptions. A published asset can be
rolled back to a particular version of the asset by republishing that version. This will
not effect existing subscriptions.

## Subscription

resilience

In Amazon DataZone, subscriptionGrant fulfillment will attempt two retires before failing.
If it fails, it must be manually deleted to retry. If Amazon DataZone cannot revoke
permissions for a subscription, deleting the subscription may fail. The underlying error
should be addressed, or the `retainPermissions` flag can be used in the
`DeleteSubscriptionGrant` API operation to force deletion of the grant
from Amazon DataZone without revoking the permissions.

If the Amazon DataZone domain is configured with a KMS key, and the
`AmazonDataZoneDomainExecutionRole` loses access to this key during the
`SubscriptionGrant` workflow, the grant is marked
`INACCESSIBLE`. Once KMS access is restored, the
`INACCESSIBLE` grants must be deleted and recreate.

## Environment

resilience

If the Amazon DataZone domain is configured with a KMS key, and the
`AmazonDataZoneDomainExecutionRole` loses access to this key during the
environment workflow, the environment will be marked `INACCESSIBLE`. Once KMS
access is restored, the `INACCESSIBLE` environment must be deleted and
recreated. Environment creation will attempt two retires before failing. If it fails, it
must be manually deleted to retry. If the environment workflow fails, the environment
will enter a failed state. At this point, it can only be deleted and recreated.

## Environment

blueprint resilience

In Amazon DataZone, an environment blueprint cannot be deleted if there are any underlying
environment profiles.

## Project resilience

In Amazon DataZone, a project cannot be deleted if there are any contained
environments.

## RAM resilience

For RAM resilience information, see [https://docs.aws.amazon.com/ram/latest/userguide/security-disaster-recovery-resiliency.html](../../../ram/latest/userguide/security-disaster-recovery-resiliency.md "../../../ram/latest/userguide/security-disaster-recovery-resiliency.md").

## User profile

management resilience

For user profile resilience information, see [AWS Identity Center](../../../singlesignon/latest/userguide/resiliency-regional-behavior.md "../../../singlesignon/latest/userguide/resiliency-regional-behavior.md").

## Domain resilience

In Amazon DataZone, a domain cannot be deleted if it contains projects or data
sources.
