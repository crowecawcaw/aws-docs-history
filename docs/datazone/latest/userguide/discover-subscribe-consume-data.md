# Amazon DataZone data discovery, subscription,

and consumption

In Amazon DataZone, once an asset is published to a domain, subscribers can discover and
request a subscription to this asset. The subscription process begins with a subscriber
searching for and browsing the catalog to find an asset they want. From the Amazon DataZone
portal, they choose to subscribe to the asset by submitting a subscription request that
includes justification and the reason for the request. The owner of the asset reviews the
request. They can either approve or reject the request.

After a subscription is granted, a fulfillment process starts to facilitate access to the
asset for the subscriber. There are two primary modes of asset access control and
fulfillment: those for Amazon DataZone-managed assets and those for assets that are not managed
by Amazon DataZone.

- **Managed assets** – Amazon DataZone can manage
  fulfillment and permissions for managed assets, such as AWS Glue tables and Amazon Redshift
  tables and views.
- **Unmanaged assets** – Amazon DataZone publishes
  standard events related to your actions (for example, approval given to a
  subscription request) to Amazon EventBridge. You can use these standard events to integrate
  with other AWS services or third-party solutions for custom integrations.

###### Topics

- [Search for and view assets in the Amazon DataZone
  catalog](search-for-data.md "search-for-data.md")
- [Request subscription to
  assets in Amazon DataZone](subscribe-to-data-assets-managed-by-datazone.md "subscribe-to-data-assets-managed-by-datazone.md")
- [Approve or reject a subscription
  request in Amazon DataZone](approve-reject-subscription-request.md "approve-reject-subscription-request.md")
- [Revoke an existing subscription in
  Amazon DataZone](revoke-subscription.md "revoke-subscription.md")
- [Cancel a subscription request in
  Amazon DataZone](cancel-subscription-request.md "cancel-subscription-request.md")
- [Unsubscribe from an asset in
  Amazon DataZone](unsubscribe-from-subscription.md "unsubscribe-from-subscription.md")
- [Using existing IAM roles to fulfill Amazon DataZone
  subscriptions](use-your-own-role.md "use-your-own-role.md")
- [Grant access to managed AWS Glue Data Catalog assets
  in Amazon DataZone](grant-access-to-glue-asset.md "grant-access-to-glue-asset.md")
- [Grant access to managed Amazon Redshift
  assets in Amazon DataZone](grant-access-to-redshift-asset.md "grant-access-to-redshift-asset.md")
- [Grant access for approved
  subscriptions to unmanaged assets in Amazon DataZone](grant-access-to-unmanaged-asset.md "grant-access-to-unmanaged-asset.md")
- [Query data in Amazon Athena or
  Amazon Redshift in Amazon DataZone](query-athena-with-deep-link-in-project.md "query-athena-with-deep-link-in-project.md")
- [Metadata enforcement rules for subscription
  requests](metadata-rules.md "metadata-rules.md")
- [Analyze Amazon DataZone subscribed data with external
  analytics applications via JDBC connection](query-with-jdbc.md "query-with-jdbc.md")
