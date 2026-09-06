

# Find features in your feature groups
<a name="feature-store-search-metadata"></a>

With Amazon SageMaker Feature Store, you can search for the features that you created in your feature groups. You can search through all of your features without needing to select a feature group first. The search functionality helps find the features that are relevant to your use case.

**Note**  
The feature groups where you're searching for features must be within your AWS Region and AWS account. For shared feature groups, the feature groups must be made discoverable to your AWS account. For more instructions on how to share the feature group catalog and grant discoverability, see [Share your feature group catalog](feature-store-cross-account-discoverability-share-feature-group-catalog.md).

If you're on a team, and teammates are looking for features to use in their models, they can search through the features in all of the feature groups.

You can add searchable parameters and descriptions to make your features more discoverable. For more information, see [Adding searchable metadata to your features](feature-store-add-metadata.md).

You can search for features using either the console or by using the [`Search`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) API operation in SageMaker AI. The following table lists all of the searchable metadata and whether you can search for it in the console or with the API.



| Searchable metadata | API field name | Searchable in the console? | 
| --- | --- | --- | 
| All Parameters | AllParameters | Yes | 
| Creation time | CreationTime | Yes | 
| Description | Description | Yes | 
| Feature group name | FeatureGroupName | No | 
| Feature name | FeatureName | Yes | 
| Feature type | FeatureType | No | 
| Last modified time | LastModifiedTime | No | 
| Parameters | Parameters.{{key}} | Yes | 

## How to search for your features
<a name="feature-store-search-metadata-how-to"></a>

The instructions for using Feature Store through the console depends on whether you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience. Choose one of the following instructions based on your use case.

### Search for features if Studio is your default experience (console)
<a name="feature-store-search-metadata-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** in the left navigation pane to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your features, choose **My account**. To view shared features, choose **Cross account**.

1. Under the **Feature Catalog** tab, choose **My account** to view your feature groups.

1. Under the **Feature Catalog** tab, choose **Cross account** to view feature groups that others made discoverable to you. Under **Created by**, you can view the resource owner account ID.

1. You can search for your feature in the **Search** dropdown list:
   + (Optional) To filter your search, choose the filter icon next to the **Search** dropdown list. You can use filters to specify parameters or date ranges in your search results. If you search for a parameter, specify both its key and value. To find your features, specify time ranges, or clear (deselect) columns that you don't want to query.
   + For shared resources, you can only edit feature group metadata or feature definitions if you have the proper access permission granted from the resource owner account. The discoverability permission alone won't allow you to edit metadata or feature definitions. For more information about granting access permissions, see[Enabling cross account access](feature-store-cross-account-access.md).

### Search for features if Studio Classic is your default experience (console)
<a name="feature-store-search-metadata-how-to-with-studio-classic"></a>

Use the latest version of Amazon SageMaker Studio Classic so that you have the most recent version of the search functionality. For information about updating Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md).

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your features, choose **My account**. To view shared features, choose **Cross account**.

1. Under the **Feature Catalog** tab, choose **My account** to view your feature groups.

1. Under the **Feature Catalog** tab, choose **Cross account** to view feature groups that others made discoverable to you. Under **Created by**, you can view the resource owner account ID.

1. You can search for your feature in the **Search** dropdown list:
   + (Optional) To filter your search, choose the filter icon next to the **Search** dropdown list. You can use filters to specify parameters or date ranges in your search results. If you search for a parameter, specify both its key and value. To find your features, specify time ranges, or clear (deselect) columns that you don't want to query.
   + For shared resources, you can only edit feature group metadata or feature definitions if you have the proper access permission granted from the resource owner account. The discoverability permission alone won't allow you to edit metadata or feature definitions. For more information about granting access permissions, see[Enabling cross account access](feature-store-cross-account-access.md).

### Search for your features using SDK for Python (Boto3)
<a name="feature-store-search-metadata-how-to-with-sdk"></a>

The code in this section uses the [`Search`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) operation in the AWS SDK for Python (Boto3) to run the search query to find features in your feature groups. For information about the other languages to submit a query, see [See Also](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html#API_Search_SeeAlso) in the *Amazon SageMaker API Reference*.

For more Feature Store examples and resources, see [Amazon SageMaker Feature Store resources](feature-store-resources.md).

The following code shows different example search queries using the API:

```
# Return all features in your feature groups
sagemaker_client.search(
    Resource="FeatureMetadata",
)  

# Search for all features that belong to a feature group that contain the "ver" substring
sagemaker_client.search(
    Resource="FeatureMetadata",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
        ]
    }
)

# Search for all features that belong to a feature group that have the EXACT name "airport"
sagemaker_client.search(
    Resource="FeatureMetadata",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Equals',
                'Value': 'airport'
            },
        ]
    }
)

# Search for all features that belong to a feature group that contains the name "ver"
AND have a name that contains "wha"
AND have a parameter (key or value) that contains "hea"

sagemaker_client.search(
    Resource="FeatureMetadata",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
            {
                'Name': 'FeatureName',
                'Operator': 'Contains',
                'Value': 'wha'
            },
            {
                'Name': 'AllParameters', 
                'Operator': 'Contains',
                'Value': 'hea'
            },
        ]
    }
)  

# Search for all features that belong to a feature group with substring "ver" in its name
OR features that have a name that contain "wha"
OR features that have a parameter (key or value) that contains "hea"

sagemaker_client.search(
    Resource="FeatureMetadata",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
            {
                'Name': 'FeatureName',
                'Operator': 'Contains',
                'Value': 'wha'
            },
            {
                'Name': 'AllParameters', 
                'Operator': 'Contains',
                'Value': 'hea'
            },
        ],
        'Operator': 'Or' # note that this is explicitly set to "Or"- the default is "And"
    }
)              


# Search for all features that belong to a feature group with substring "ver" in its name
OR features that have a name that contain "wha"
OR parameters with the value 'Sage' for the 'org' key

sagemaker_client.search(
    Resource="FeatureMetadata",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
            {
                'Name': 'FeatureName',
                'Operator': 'Contains',
                'Value': 'wha'
            },
            {
                'Name': 'Parameters.org', 
                'Operator': 'Contains',
                'Value': 'Sage'
            },
        ],
        'Operator': 'Or' # note that this is explicitly set to "Or"- the default is "And"
    }
)
```