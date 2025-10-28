# Data discovery, subscription, and consumption

In Amazon SageMaker Unified Studio, after an asset is published to a domain, subscribers can discover and request
a subscription to this asset. The subscription process begins with a subscriber searching for
and browsing the catalog to find an asset they want. In the Amazon SageMaker Catalog, they subscribe to
the asset by submitting a subscription request that includes justification and the reason for
the request. The owner of the asset reviews the request. They can either approve or reject the
request.

After a subscription is granted, a fulfillment process starts to facilitate access to the
asset for the subscriber. There are two primary modes of asset access control and fulfillment:
those for Amazon SageMaker Unified Studio managed assets and those for assets that are not managed by
Amazon SageMaker Unified Studio.

- **Managed assets** – Amazon SageMaker Unified Studio can manage
  fulfillment and permissions for managed assets, such as AWS Glue tables and Amazon Redshift tables and
  views.
- **Unmanaged assets** – Amazon SageMaker Unified Studio publishes standard
  events related to your actions (for example, approval given to a subscription request to
  Amazon EventBridge). You can use these standard events to integrate with other AWS services or
  third-party solutions for custom integrations.

###### Topics

- [Search
  for and view assets in the Amazon SageMaker Unified Studio catalog](search-for-data.md "search-for-data.md")
- [Request subscription to assets in
  Amazon SageMaker Unified Studio](subscribe-to-data-assets-managed.md "subscribe-to-data-assets-managed.md")
- [Approve or reject a subscription request
  in Amazon SageMaker Unified Studio](approve-reject-subscription-request.md "approve-reject-subscription-request.md")
- [Revoke an existing subscription in Amazon SageMaker Unified Studio](revoke-subscription.md "revoke-subscription.md")
- [Cancel a subscription request in
  Amazon SageMaker Unified Studio](cancel-subscription-request.md "cancel-subscription-request.md")
- [Unsubscribe from an asset in Amazon SageMaker Unified Studio](unsubscribe-from-subscription.md "unsubscribe-from-subscription.md")
- [Grant access to managed AWS Glue Data Catalog assets in
  Amazon SageMaker Unified Studio](grant-access-to-glue-asset.md "grant-access-to-glue-asset.md")
- [Grant access to managed Amazon Redshift assets in
  Amazon SageMaker Unified Studio](grant-access-to-redshift-asset.md "grant-access-to-redshift-asset.md")
- [Grant access for approved subscriptions to
  unmanaged assets in Amazon SageMaker Unified Studio](grant-access-to-unmanaged-asset.md "grant-access-to-unmanaged-asset.md")
- [Metadata enforcement rules for subscription
  requests](metadata-rules-subscription.md "metadata-rules-subscription.md")
