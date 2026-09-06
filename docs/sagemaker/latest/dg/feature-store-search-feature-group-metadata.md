

# Find feature groups in your Feature Store
<a name="feature-store-search-feature-group-metadata"></a>

With Amazon SageMaker Feature Store, you can search for the feature groups using either the console or the [Search](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) operation. You can use the search functionality to find features and feature groups that are relevant to the models that you're creating. You can use the search functionality to quickly find the feature groups that are relevant to your use case.

**Note**  
The feature groups that you're searching for must be within your AWS Region and AWS account, or shared with and made discoverable to your AWS account. For more information about how to share the feature group catalog and grant discoverability, see [Share your feature group catalog](feature-store-cross-account-discoverability-share-feature-group-catalog.md).

The following table shows the searchable fields and whether you can use the console to search for a specific field.

You can search for features using either Amazon SageMaker Studio Classic or the [`Search`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) operation in the SageMaker API. The following table lists all of the searchable metadata and whether you can search for it in the console. Tags are searchable for your own feature groups but are not searchable for feature groups made discoverable to you.



| Searchable metadata | API field name | Searchable in the console? | Searchable with cross account? | 
| --- | --- | --- | --- | 
| All Tags | AllTags | Yes | No | 
| Creation Failure Reason | FailureReason | No | No | 
| Creation Status | [FeatureGroupStatus](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureGroup.html) | Yes | Yes | 
| Creation time | CreationTime | Yes | Yes | 
| Description | Description | Yes | Yes | 
| Event Time Feature Name | EventTimeFeatureName | No | No | 
| Feature Definitions | [FeatureDefinitions](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureDefinition.html) | No | No | 
| Feature Group ARN | [FeatureGroupARN](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureGroup.html) | No | No | 
| Feature Group Name | [FeatureGroupName](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_FeatureGroup.html) | Yes | Yes | 
| Offline Store Configuration | [OfflineStoreConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreConfig.html) | No | No | 
| Offline Store Status | [OfflineStoreStatus](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_OfflineStoreStatus.html) | Yes | Yes | 
| Last Update Status | [LastUpdateStatus](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LastUpdateStatus.html) | No | No | 
| Record Identfier Feature Name | RecordIdentifierFeatureName | Yes | Yes | 
| Tags | Tags.key | Yes | No | 

## How to find feature groups
<a name="feature-store-search-feature-group-metadata-how-to"></a>

You can use the console or the Amazon SageMaker Feature Store API to find your feature groups. The instructions for using Feature Store through the console depends on if you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### Find feature groups if Studio is your default experience (console)
<a name="feature-store-search-feature-group-metadata-how-to-using-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** in the left navigation pane to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Under the **Feature Group Catalog** tab, choose **My account** to view your feature groups.

1. Under the **Feature Group Catalog** tab, choose **Cross account** to view feature groups that others made discoverable to you. Under **Created by**, you can view the resource owner account ID.

1. You can search for your feature groups in the **Search** dropdown list:
   + (Optional) To filter your search, choose the filter icon next to the **Search** dropdown list. You can use filters to specify parameters or date ranges in your search results. If you search for a parameter, specify both its key and value. To find your feature groups, you can specify time ranges, clear (deselect) columns that you don't want to query, choose stores to search, or search by status.
   + For shared resources, you can only edit feature group metadata or feature definitions if you have the proper access permission granted from the resource owner account. The discoverability permission alone won't allow you to edit metadata or feature definitions. For more information about granting access permissions, see [Enabling cross account access](feature-store-cross-account-access.md).

### Find feature groups if Studio Classic is your default experience (console)
<a name="feature-store-search-feature-group-metadata-how-to-with-studio-classic"></a>

Use the latest version of Amazon SageMaker Studio Classic to get the most recent version of the search functionality if you are accessing Feature Store through the Studio Classic application. For information about updating Studio Classic, see [Shut Down and Update Amazon SageMaker Studio Classic](studio-tasks-update-studio.md).

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic](studio-launch.md).

1. Choose the **Home** icon (![Black square icon representing a placeholder or empty image.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)) in the left navigation pane.

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your feature groups, choose **My account**. To view shared feature groups, choose **Cross account**.

1. Under the **Feature Group Catalog** tab, choose **My account** to view your feature groups.

1. Under the **Feature Group Catalog** tab, choose **Cross account** to view feature groups that others made discoverable to you. Under **Created by**, you can view the resource owner account ID.

1. You can search for your feature groups in the **Search** dropdown list:
   + (Optional) To filter your search, choose the filter icon next to the **Search** dropdown list. You can use filters to specify parameters or date ranges in your search results. If you search for a parameter, specify both its key and value. To find your feature groups more easily, you can specify time ranges, clear (deselect) columns that you don't want to query, choose stores to search, or search by status.
   + For shared resources, you can only edit feature group metadata or feature definitions if you have the proper access permission granted from the resource owner account. The discoverability permission alone won't allow you to edit metadata or feature definitions. For more information about granting access permissions, see [Enabling cross account access](feature-store-cross-account-access.md).

### Find feature groups using SDK for Python (Boto3)
<a name="feature-store-search-feature-group-metadata-how-to-with-sdk"></a>

The code in this section uses the [`Search`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html) operation in the AWS SDK for Python (Boto3) to run the search query to find feature groups. For information about the other languages to submit a query, see [See Also](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Search.html#API_Search_SeeAlso) in the *Amazon SageMaker API Reference*.

For more Feature Store examples and resources, see [Amazon SageMaker Feature Store resources](feature-store-resources.md).

The following code shows different example search queries using the API:

```
# Return all feature groups
sagemaker_client.search(
    Resource="FeatureGroups",
)  

# Search for feature groups that are shared with your account
sagemaker_session.search(
    resource="FeatureGroup",
    search_expression={
        "Filters": [
            {
                "Name": "FeatureGroupName",
                "Value": "MyFeatureGroup",
                "Operator": "Contains",
            }
        ],
        "Operator": "And",
    },
    sort_by="Name",
    sort_order="Ascending",
    next_token="token",
    max_results=50,
    CrossAccountFilterOption="SameAccount"
)

# Search for all feature groups with a name that contains the "ver" substring
sagemaker_client.search(
    Resource="FeatureGroups",
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

# Search for all feature groups that have the EXACT name "airport"
sagemaker_client.search(
    Resource="FeatureGroups",
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

# Search for all feature groups that contains the name "ver"
# AND have a record identifier feature name that contains "wha"
# AND have a tag (key or value) that contains "hea"
sagemaker_client.search(
    Resource="FeatureGroups",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
            {
                'Name': 'RecordIdentifierFeatureName',
                'Operator': 'Contains',
                'Value': 'wha'
            },
            {
                'Name': 'AllTags', 
                'Operator': 'Contains',
                'Value': 'hea'
            },
        ]
    }
)  

# Search for all feature groups with substring "ver" in its name
# OR feature groups that have a record identifier feature name that contains "wha"
# OR feature groups that have a tag (key or value) that contains "hea"
sagemaker_client.search(
    Resource="FeatureGroups",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
            {
                'Name': 'RecordIdentifierFeatureName',
                'Operator': 'Contains',
                'Value': 'wha'
            },
            {
                'Name': 'AllTags', 
                'Operator': 'Contains',
                'Value': 'hea'
            },
        ],
        'Operator': 'Or' # note that this is explicitly set to "Or"- the default is "And"
    }
)              


# Search for all feature groups with substring "ver" in its name
# OR feature groups that have a record identifier feature name that contains "wha"
# OR tags with the value 'Sage' for the 'org' key
sagemaker_client.search(
    Resource="FeatureGroups",
    SearchExpression={
        'Filters': [
            {
                'Name': 'FeatureGroupName',
                'Operator': 'Contains',
                'Value': 'ver'
            },
            {
                'Name': 'RecordIdentifierFeatureName',
                'Operator': 'Contains',
                'Value': 'wha'
            },
            {
                'Name': 'Tags.org', 
                'Operator': 'Contains',
                'Value': 'Sage'
            },
        ],
        'Operator': 'Or' # note that this is explicitly set to "Or"- the default is "And"
    }
)

# Search for all offline only feature groups
sagemaker_client.search(
    Resource="FeatureGroups",
    SearchExpression={
        'Filters': [
            {
                'Name': 'OnlineStoreConfig.EnableOnlineStore',
                'Operator': 'NotEquals',
                'Value': 'true'
            },
            {
                'Name': 'OfflineStoreConfig.S3StorageConfig.S3Uri',
                'Operator': 'Exists'
            }
        ]
    }
)

# Search for all online only feature groups
sagemaker_client.search(
    Resource="FeatureGroups",
    SearchExpression={
        'Filters': [
            {
                'Name': 'OnlineStoreConfig.EnableOnlineStore',
                'Operator': 'Equals',
                'Value': 'true'
            },
            {
                'Name': 'OfflineStoreConfig.S3StorageConfig.S3Uri',
                'Operator': 'NotExists'
            }
        ]
    }
)

# Search for all feature groups that are BOTH online and offline
sagemaker_client.search(
    Resource="FeatureGroups",
    SearchExpression={
        'Filters': [
            {
                'Name': 'OnlineStoreConfig.EnableOnlineStore',
                'Operator': 'Equals',
                'Value': 'true'
            },
            {
                'Name': 'OfflineStoreConfig.S3StorageConfig.S3Uri',
                'Operator': 'Exists'
            }
        ]
    }
)
```

You can also use python SDK of AWS RAM APIs to create resource share. The API signature is given below. To use python SDK of AWS RAM API, you need attach AWS RAM full access managed policy with execution Role.

```
response = client.create_resource_share(
    name='string',
    resourceArns=[
        'string',
    ],
    principals=[
        'string',
    ],
    tags=[
        {
            'key': 'string',
            'value': 'string'
        },
    ],
    allowExternalPrincipals=True|False,
    clientToken='string',
    permissionArns=[
        'string',
    ]
)
```