# Asset revisions in Amazon DataZone

Amazon DataZone increments the revision of an asset when you edit its business or technical
metadata. These edits include modifying the asset name, description, glossary terms,
columns names, metadata forms, and metadata form field values. These changes can result
from manual edits, data source job run, or API operations. Amazon DataZone automatically
generates a new asset revision any time you make an edit to the asset.

After you update an asset and a new revision is generated, you must publish the new
revision to the catalog for it to be updated and available to subscribers. For more
information, see [Publish assets to the Amazon DataZone catalog from
the project inventory](publishing-data-asset.md "publishing-data-asset.md"). You can only publish the most
recent version of an asset to the catalog.

###### To view past revisions of an asset

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project that contains the asset.
3. Navigate to the **Data** tab for the project, then locate and
   choose the asset. This opens the asset details page.
4. Navigate to the **History** tab, which displays a list of
   past revisions of the asset.
