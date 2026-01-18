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

## Set up cross-Region and cross-account subscriptions

Cross-Region subscriptions allow data consumers to subscribe to and access data assets published in a different AWS Region than their consuming project. Cross-account subscriptions enable access to data assets owned by a different AWS account. You can subscribe to data across Regions or accounts.

Cross-Region and cross-account subscriptions support AWS Glue tables and views, as well as Amazon Redshift tables and views across all standard (non-opt-in) AWS Regions. For AWS Glue assets, cross-Region access is achieved through resource links created in the target Region while the original table remains in the source Region. For Amazon Redshift assets, cross-Region and cross-account access uses Redshift's native datashare functionality. Cross-account Redshift scenarios require AWS RAM authorization on both the producer and consumer sides.

### Prerequisites

Before enabling cross-Region or cross-account subscriptions, you must have an existing domain with permissions to manage blueprints and projects. The appropriate blueprints must be enabled in both source and target Regions—LakeHouseDatabase for Glue assets or RedshiftServerless for Redshift assets. In Amazon SageMaker Unified Studio domains, the Tooling blueprint must also be enabled in the target Region.

### Enable cross-Region and cross-account subscriptions

To enable cross-Region or cross-account subscriptions, first enable the required blueprints in the target Region through the Blueprints page in your domain. Next, create a project profile configured for the target Region, then create a new project using that profile. Subscriptions to this project automatically fulfill to the target Region and account.

### Considerations

Cross-Region subscriptions are not supported in opt-in Regions. Blueprints must be enabled in both source and target Regions before creating subscriptions. In Amazon SageMaker Unified Studio domains, you cannot add new environments to existing projects through the console—to subscribe to assets in a new Region, you must create a new project with a project profile configured for that Region. For cross-account Redshift data sharing, AWS RAM authorization is required on both producer and consumer sides. Cross-account Glue access requires appropriate Lake Formation permissions to be configured between accounts.
