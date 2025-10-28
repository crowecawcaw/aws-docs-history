# Manage inventory and curate assets in

Amazon DataZone

In order to use Amazon DataZone to catalog your data, you must first bring your data
(assets) as inventory of your project in Amazon DataZone. Creating inventory for a particular
project, makes the assets discoverable only to that project’s members.

Once the assets are created in project inventory, their metadata can be curated. For
example, you can edit the asset's name, description, or read me. Each edit to the asset
creates a new version of the asset. You can use the History tab on the asset's details
page to view all asset versions.

You can edit the **Read Me** section and add rich descriptions for
the asset. The **Read Me** section supports markdown, thus enabling you
to format your descriptions as required and describe key information about an asset to
consumers.

Glossary terms can be added at the asset level by filling out available forms.

To curate the schema, you can review the columns, add business names, descriptions,
and add glossary terms at column level.

If automated metadata generation is enabled when the data source is created, the
business names for assets and columns are available to review and accept or reject
individually or all at once.

You can also edit the subscription terms to specify if approval for the asset is
required or not.

Metadata forms in Amazon DataZone enable you to extend a data asset's metadata model by
adding custom-defined attributes (for example, sales region, sales year, and sales
quarter). The metadata forms that are attached to an asset type are applied to all
assets created from that asset type. You can also add additional metadata forms to
individual assets as part of the data source run or after it's created. For creating new
forms, see [Create a metadata form in Amazon DataZone](create-metadata-form.md "create-metadata-form.md").

To update the metadata of an asset, you must be the owner or the contributor of the
project to which the asset belongs.

###### To update the metadata of an asset

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project that contains the asset whose metadata you want to
   update.
3. Navigate to the **Data** tab for the project.
4. Choose **Inventory data** from the left navigation pane, then
   choose the name of the the asset whose metadata you want to update.
5. On the asset details page, under **Metadata forms**, choose
   **Edit** and edit the existing forms as needed. You can
   also attach additional metadata forms to the asset. For more information, see
   [Attach additional metadata forms to
   assets](#update-metadata-data-steward "#update-metadata-data-steward").
6. When you're done making updates, choose **Save form**.

When you save the form, Amazon DataZone generates a new inventory version of the
asset. To publish the updated version to the catalog, choose
**Re-publish asset**.

## Attach additional metadata forms to

assets

By default, metadata forms attached to a domain are attached to all assets
published to that domain. Data publishers can associate additional metadata forms to
individual assets in order to provide additional context.

###### To attach additional metadata forms to an asset

1. Navigate to the Amazon DataZone data portal URL and sign in using single
   sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone
   administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane
   and select the project that contains the asset whose metadata you want to
   add to.
3. Navigate to the **Data** tab for the project.
4. Choose **Inventory data** from the left navigation pane,
   then choose the name of the the asset whose metadata you want to add
   to.
5. On the asset details page, under **Metadata forms**,
   choose **Add forms**.
6. Select the form(s) to add to the asset, then choose **Add
   forms**.
7. Enter values for each of the metadata fields, then choose **Save
   form**.

When you save the form, Amazon DataZone generates a new inventory version of
the asset. To publish the updated version to the catalog, choose
**Re-publish asset**.

## Publish asset to the catalog after

curation in Amazon DataZone

Once satisfied with the asset curation, the data owner can publish an asset
version to the Amazon DataZone catalog and thus make it discoverable by all domain users.
The asset shows the inventory version and the published version. In the discovery
catalog, only the latest published version appears. If the metadata is updated after
publishing, then a new inventory version will be available for publishing to the
catalog.
