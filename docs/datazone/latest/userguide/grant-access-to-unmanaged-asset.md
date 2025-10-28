# Grant access for approved

subscriptions to unmanaged assets in Amazon DataZone

In Amazon DataZone, subscription requests and approved or granted subscriptions for
**read** access to the assets are managed by asset owners.

Amazon DataZone enables users to publish any type of asset in the business data catalog.
For some of these assets, Amazon DataZone can can automatically manage access grants. These
assets are called **managed assets** and include Lake Formation-managed
AWS Glue Data Catalog tables and Amazon Redshift tables and views. All other assets to
which Amazon DataZone can't automatically grant subscriptions are called
**unmanaged**.

Amazon DataZone provides a path for you to manage access grants for your unmanaged assets.
When a subscription to an asset in the business data catalog is approved by the data
owner, Amazon DataZone publishes an event in Amazon EventBridge in the your account along
with all the necessary information in the payload that enables you to create the access
grants between the source and the target. When you receive this event, you can trigger a
custom handler which can use the information in the event to create necessary grants or
permissions. Once you have granted the access, you can report back and update the status
of the subscription in Amazon DataZone so that it can notify the user(s) who subscribed to
the asset that they can start consuming the asset. For more information, see [Amazon DataZone events and
notifications](working-with-events-and-notifications.md "working-with-events-and-notifications.md").
