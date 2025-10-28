# Asset revisions in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio increments the revision of an asset when you edit its business or technical
metadata. These edits include modifying the asset name, description, glossary terms,
column names, metadata forms, and metadata form field values. These changes can result
from manual edits, data source job runs, or API operations. Amazon SageMaker Unified Studio automatically
generates a new asset revision any time you make an edit to the asset.

After you update an asset and a new revision is generated, you must publish the new
revision to the catalog for it to be updated and available to subscribers. For more
information, see [Publish assets to the Amazon SageMaker Unified Studio catalog from the
project inventory](publishing-data-asset.md "publishing-data-asset.md"). You can only publish the most
recent version of an asset to the catalog.

###### To view past revisions of an asset

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project to which the asset belongs.
3. Under **Project catalog** in the left side navigation, choose
   **Assets**.
4. On the **Inventory** tab, choose the name of the asset that
   you want to unpublish. This opens the asset details page.
5. Navigate to the **History** tab, which displays a list of
   past revisions of the asset.
