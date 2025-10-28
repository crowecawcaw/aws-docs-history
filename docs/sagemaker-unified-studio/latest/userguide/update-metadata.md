# Manage inventory and curate assets in

Amazon SageMaker Unified Studio

In order to use Amazon SageMaker Unified Studio to catalog your data, you must first bring your data
(assets) as inventory of your project in Amazon SageMaker Unified Studio. Creating inventory for a particular
project makes the assets discoverable only to that project’s members.

After the assets are created in project inventory, their metadata can be curated. For
example, you can edit the asset's name, description, or README. Each edit to the asset
creates a new version of the asset. You can use the History tab on the asset's details
page to view all asset versions.

You can edit the **README** section and add rich descriptions for the
asset. The **README** section supports markdown, thus enabling you to
format your descriptions as required and describe key information about an asset to
consumers.

Glossary terms can be added at the asset level by filling out available forms.

To curate the schema, you can review the columns, add business names, descriptions,
and add glossary terms at column level.

If automated metadata generation is enabled when the data source is created, the
business names for assets and columns are available to review and accept or reject
individually or all at once.

You can also edit the subscription terms to specify if approval for the asset is
required or not.

Metadata forms in Amazon SageMaker Unified Studio enable you to extend a data asset's metadata model by
adding custom-defined attributes (for example, sales region, sales year, and sales
quarter). The metadata forms that are attached to an asset type are applied to all
assets created from that asset type. You can also add additional metadata forms to
individual assets as part of the data source run or after it's created. For creating new
forms, see [Create a metadata form in Amazon SageMaker Unified Studio](create-metadata-form.md "create-metadata-form.md").

To update the metadata of an asset, you must be the owner or the contributor of the
project to which the asset belongs.

###### To update the metadata of an asset

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project to which the asset belongs.
3. Under **Project catalog** in the left side navigation, choose
   **Assets**.
4. Make sure you are on the **Inventory** tab, then choose the
   name of the asset that you want to publish. You are then brought to the asset
   details page.
5. On the asset details page, under **Metadata forms**, choose
   **Edit values** to edit the existing forms as needed, or
   choose **Add metadata form** and enter values for each of the
   metadata fields to attach additional metadata forms to the asset.
6. When you're done making updates, choose **Save**.

When you save the form, Amazon SageMaker Unified Studio generates a new inventory version of the
asset. To publish the updated version to the catalog, choose
**Re-publish asset**.
By default, metadata forms attached to a domain are attached to all assets published
to that domain. Data publishers can associate additional metadata forms to individual
assets in order to provide additional context.

When you are satisfied with the asset curation, the data owner can publish an asset
version to the Amazon SageMaker Unified Studio catalog and thus make it discoverable by all domain users. The
asset in the project shows the inventory version and the published version. In the
discovery catalog, only the latest published version appears. If the metadata is updated
after publishing, then a new inventory version will be available for publishing to the
catalog.
