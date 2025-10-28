# Data inventory and publishing

This section describes the tasks and procedures to create an inventory of your data in
Amazon SageMaker Unified Studio and to publish your data in Amazon SageMaker Unified Studio.

To use Amazon SageMaker Unified Studio to catalog your data, you must first bring your data (assets) as
inventory of your project in Amazon SageMaker Unified Studio. Creating an inventory for a particular project makes
the assets discoverable only to that project’s members. Project inventory assets are not
available to all domain users in search or browse unless it is published to the
Amazon SageMaker Catalog. After creating a project inventory, data owners can curate their
inventory assets with the required business metadata by adding or updating business names
(asset and schema), descriptions (asset and schema), README, glossary terms (asset and
schema), and metadata forms.

The next step of using Amazon SageMaker Unified Studio to catalog your data is to make your project’s inventory
assets discoverable by the domain users. You can do this by publishing the inventory assets
to the Amazon SageMaker Unified Studio catalog. Only the latest version of the inventory asset can be published to
the catalog and only the latest published version is active in the discovery catalog. If an
inventory asset is updated after it's been published into the Amazon SageMaker Unified Studio catalog, you must
publish it again for the latest version to be in the discovery catalog.

For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md")

###### Topics

- [Configure
  Lake Formation permissions for Amazon SageMaker Unified Studio](lake-formation-permissions-for-amazon-sagemaker-unified-studio.md "lake-formation-permissions-for-amazon-sagemaker-unified-studio.md")
- [Create custom asset types in Amazon SageMaker Unified Studio](create-asset-types.md "create-asset-types.md")
- [Create an Amazon SageMaker Unified Studio data source for
  AWS Glue in the project catalog](data-source-glue.md "data-source-glue.md")
- [Create an Amazon SageMaker Unified Studio data source for
  Amazon Redshift in the project catalog](create-redshift-data-source.md "create-redshift-data-source.md")
- [Create an Amazon SageMaker Unified Studio data source for
  Amazon SageMaker AI in the project catalog](create-sagemaker-data-source.md "create-sagemaker-data-source.md")
- [Edit a data source in Amazon SageMaker Unified Studio](editing-a-data-source.md "editing-a-data-source.md")
- [Delete a data source in Amazon SageMaker Unified Studio](removing-a-data-source.md "removing-a-data-source.md")
- [Publish assets to the Amazon SageMaker Unified Studio catalog from the
  project inventory](publishing-data-asset.md "publishing-data-asset.md")
- [Share assets](share-assets.md "share-assets.md")
- [Manage inventory and curate assets in
  Amazon SageMaker Unified Studio](update-metadata.md "update-metadata.md")
- [Manually create an asset in
  Amazon SageMaker Unified Studio](create-data-asset-manually.md "create-data-asset-manually.md")
- [Unpublish an asset from the
  Amazon SageMaker Catalog](archive-data-asset.md "archive-data-asset.md")
- [Delete an Amazon SageMaker Unified Studio asset](delete-data-asset.md "delete-data-asset.md")
- [Manually start a data source run in
  Amazon SageMaker Unified Studio](manually-start-data-source-run.md "manually-start-data-source-run.md")
- [Asset revisions in Amazon SageMaker Unified Studio](asset-versioning.md "asset-versioning.md")
- [Data quality in Amazon SageMaker Unified Studio](data-quality.md "data-quality.md")
- [Using machine learning and generative AI in Amazon SageMaker Unified Studio](autodoc.md "autodoc.md")
- [Data lineage in Amazon SageMaker Unified Studio](datazone-data-lineage.md "datazone-data-lineage.md")
- [Analyze Amazon SageMaker Unified Studio data with external analytics
  applications via JDBC connection](query-with-jdbc.md "query-with-jdbc.md")
- [Metadata enforcement rules for
  publishing](metadata-rules-publishing.md "metadata-rules-publishing.md")
