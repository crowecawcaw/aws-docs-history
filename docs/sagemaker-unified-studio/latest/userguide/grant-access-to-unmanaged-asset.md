# Grant access for approved subscriptions to

unmanaged assets in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables users to publish any type of asset in the Amazon SageMaker Catalog. For some of
these assets, Amazon SageMaker Unified Studio can can automatically manage access grants. These assets are called
**managed assets** and include Lake Formation-managed AWS Glue Data
Catalog tables and Amazon Redshift tables and views. All other assets to which Amazon SageMaker Unified Studio can't
automatically grant subscriptions are called **unmanaged**.

Amazon SageMaker Unified Studio provides a path for you to manage access grants for your unmanaged assets. When
a subscription to an asset in the Amazon SageMaker Catalog is approved by the data owner, Amazon SageMaker Unified Studio
publishes an event in Amazon EventBridge in your account along with all the necessary
information in the payload that enables you to create the access grants between the source and
the target. When you receive this event, you can trigger a custom handler which can use the
information in the event to create necessary grants or permissions. After you have granted the
access, you can report back and update the status of the subscription in Amazon SageMaker Unified Studio so that it
can notify the user(s) who subscribed to the asset that they can start consuming the asset.
