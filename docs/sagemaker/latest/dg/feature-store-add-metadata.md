

# Adding searchable metadata to your features
<a name="feature-store-add-metadata"></a>

In Amazon SageMaker Feature Store, you can search through all of your features. To make your features more discoverable, you can add metadata to them. You can add the following types of metadata:
+ Description – A searchable description of the feature.
+ Parameters – Searchable key-value pairs.

The description can have up to 255 characters. For parameters, you must specify a key-value pair in your search. You can add up to 25 parameters.

To update the metadata of a feature, you can use either the console or the [`UpdateFeatureMetadata`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureMetadata.html) operation.

## How to add searchable metadata to your features
<a name="feature-store-add-metadata-how-to"></a>

You can use the console or the Amazon SageMaker Feature Store API to add searchable metadata to your features. Instructions for using Feature Store through the console depend on whether you have enabled [Amazon SageMaker Studio](studio-updated.md) or [Amazon SageMaker Studio Classic](studio.md) as your default experience.

### Add searchable metadata to features if Studio is your default experience (console)
<a name="feature-store-add-metadata-how-to-with-studio-updated"></a>

1. Open the Studio console by following the instructions in [Launch Amazon SageMaker Studio](studio-updated-launch.md).

1. Choose **Data** in the left navigation pane, to expand the dropdown list.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your features, choose **My account**. To view shared features, choose **Cross account**.

1. To view your feature groups, under the **Feature Catalog** tab, choose **My account**.

1. Under the **Feature Catalog** tab, choose **Cross account** to view feature groups that others make discoverable to you. Under **Created by**, you can view the resource owner account ID of the feature group.

1. You can search for your feature in the **Search** dropdown list.
   + (Optional) To filter your search, choose the filter icon next to the **Search** dropdown list. You can use filters to specify parameters or date ranges in your search results. If you search for a parameter, specify both its key and value. To find your features more easily, you can specify time ranges or deselect columns that you don't want to query.
   + For shared resources, you can only edit feature group metadata or feature definitions if you have the proper access permission granted from the resource owner account. Having the discoverability permission alone doesn't allow you to edit metadata or feature definitions. For more information about granting access permissions, see[Enabling cross account access](feature-store-cross-account-access.md).

1. Choose your feature.

1. Choose **Edit metadata**.

1. In the **Description** field, add or update the description.

1. In the **Parameters** field under **Parameters**, specify a key-value pair for the parameter.

1. (Optional) Choose **Add new parameter** to add another parameter.

1. Choose **Save changes**.

1. Choose **Confirm**.

### Add searchable metadata to your features if Studio Classic is your default experience (console)
<a name="feature-store-add-metadata-how-to-with-studio-classic"></a>

1. Open the Studio Classic console by following the instructions in [Launch Amazon SageMaker Studio Classic Using the Amazon SageMaker AI Console](studio-launch.md#studio-launch-console).

1. In the left navigation pane, choose the **Home** icon (![Home icon.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/studio/icons/house.png)).

1. Choose **Data**.

1. From the dropdown list, choose **Feature Store**.

1. (Optional) To view your features, choose **My account**. To view shared features, choose **Cross account**.

1. To view your feature groups, under the **Feature Catalog** tab, choose **My account**.

1. Under the **Feature Catalog** tab, choose **Cross account** to view feature groups that other accounts made discoverable to you. Under **Created by**, you can view the resource owner account ID of the feature group.

1. You can search for your feature in the **Search** dropdown list.
   + (Optional) To filter your search, choose the filter icon next to the **Search** dropdown list. You can use filters to specify parameters or date ranges in your search results. If you search for a parameter, specify both its key and value. To find your features more easily, you can specify time ranges or deselect columns that you don't want to query.
   + For shared resources, you can only edit feature group metadata or feature definitions if you have the proper access permission granted from the resource owner account. Having the discoverability permission alone doesn't allow you to edit metadata or feature definitions. For more information about granting access permissions, see[Enabling cross account access](feature-store-cross-account-access.md).

1. Choose your feature.

1. Choose **Edit metadata**.

1. In the **Description** field, add or update the description.

1. In the **Parameters** field under **Parameters**, specify a key-value pair for the parameter.

1. (Optional) Choose **Add new parameter** to add another parameter.

1. Choose **Save changes**.

1. Choose **Confirm**.

### Add searchable metadata to your features using SDK for Python (Boto3)
<a name="feature-store-add-metadata-how-to-with-sdk"></a>

The code in this section uses the [`UpdateFeatureMetadata`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureMetadata.html) operation in the AWS SDK for Python (Boto3) to add searchable metadata to your features for different scenarios. For information about the other languages to submit a query, see [See Also](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_UpdateFeatureMetadata.html#API_Search_SeeAlso) in the *Amazon SageMaker API Reference*.

For more Feature Store examples and resources, see [Amazon SageMaker Feature Store resources](feature-store-resources.md).

------
#### [ Add a list of parameters to a feature ]

To add a list of parameters to a feature, specify values for the following fields:
+ `FeatureGroupName`
+ `Feature`
+ `Parameters`

The following example code uses the AWS SDK for Python (Boto3) to add two parameters.

```
sagemaker_client.update_feature_metadata(
    FeatureGroupName={{"feature_group_name"}},
    FeatureName={{"feature-name"}},
    ParameterAdditions=[
        {"Key": {{"example-key-0"}}, "Value": {{"example-value-0"}}},
        {"Key": {{"example-key-1"}}, "Value": {{"example-value-1"}}},
    ]
)
```

------
#### [ Add a description to a feature ]

To add a description to a feature, specify values for the following fields:
+ `FeatureGroupName`
+ `Feature`
+ `Description`

```
sagemaker_client.update_feature_metadata(
    FeatureGroupName={{"feature-group-name"}},
    FeatureName={{"feature-name"}},
    Description={{"description"}}
)
```

------
#### [ Remove parameters for a feature ]

To remove all parameters for a feature, do the following.

Specify values for the following fields:
+ `FeatureGroupName`
+ `Feature`

Specify the keys for the parameters that you're removing under `ParameterRemovals`.

```
sagemaker_client.update_feature_metadata(
    FeatureGroupName={{"feature_group_name"}},
    FeatureName={{"feature-name"}},
        ParameterRemovals=[
        {"Key": {{"example-key-0"}}},
        {"Key": {{"example-key-1"}}},
    ]
)
```

------
#### [ Remove the description for a feature ]

To remove the description for a feature, do the following.

Specify values for the following fields:
+ `FeatureGroupName`
+ `Feature`

Specify an empty string for `Description`.

```
sagemaker_client.update_feature_metadata(
    FeatureGroupName={{"feature-group-name"}},
    FeatureName={{"feature-name"}},
    Description=""
)
```

------

#### Example code
<a name="feature-store-add-metadata-python-sdk-example"></a>

After you've updated the metadata for a feature, you can use the [`DescribeFeatureMetadata`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureMetadata.html) operation to see the updates that you've made.

The following code goes through an example workflow using the AWS SDK for Python (Boto3). The example code does the following:

1. Sets up your SageMaker AI environment.

1. Creates a feature group.

1. Adds features to the group.

1. Adds metadata to the features.

For more Feature Store examples and resources, see [Amazon SageMaker Feature Store resources](feature-store-resources.md).

##### Step 1: Setup
<a name="feature-store-add-metadata-step-1"></a>

To start using Feature Store, create SageMaker AI, boto3 and Feature Store sessions. Then set up the S3 bucket you want to use for your features. This is your offline store. The following code uses the SageMaker AI default bucket and adds a custom prefix to it.

**Note**  
The role that you use must have the following managed policies attached to it: `AmazonS3FullAccess` and `AmazonSageMakerFeatureStoreAccess`.

```
# SageMaker Python SDK version 3.x is required
%pip install 'sagemaker>=2.0.0'
import sagemaker
import sys
```

```
import boto3
import pandas as pd
import numpy as np
import io
from sagemaker.core.helper.session_helper import Session
from sagemaker.core.helper.session_helper import get_execution_role
from botocore.exceptions import ClientError


prefix = 'sagemaker-featurestore-introduction'
role = get_execution_role()

sagemaker_session = Session()
region = sagemaker_session.boto_region_name
s3_bucket_name = sagemaker_session.default_bucket()
sagemaker_client = boto_session.client(service_name='sagemaker', region_name=region)
```

##### Step 2: Create a feature group and add features
<a name="feature-store-add-metadata-step-2"></a>

The following code is an example of creating a feature group with feature definitions.

```
feature_group_name = "test-for-feature-metadata"
feature_definitions = [
    {"FeatureName": "feature-1", "FeatureType": "String"},
    {"FeatureName": "feature-2", "FeatureType": "String"},
    {"FeatureName": "feature-3", "FeatureType": "String"},
    {"FeatureName": "feature-4", "FeatureType": "String"},
    {"FeatureName": "feature-5", "FeatureType": "String"}
]
try:
    sagemaker_client.create_feature_group(
        FeatureGroupName=feature_group_name,
        RecordIdentifierFeatureName="feature-1",
        EventTimeFeatureName="feature-2",
        FeatureDefinitions=feature_definitions,
        OnlineStoreConfig={"EnableOnlineStore": True}
    )
except ClientError as e:
    if e.response["Error"]["Code"] == "ResourceInUse":
        pass
    else:
        raise e
```

##### Step 3: Add metadata
<a name="feature-store-add-metadata-step-3"></a>

Before you add metadata, use the [`DescribeFeatureGroup`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html) operation to make sure that the status of the feature group is `Created`.

```
sagemaker_client.describe_feature_group(
        FeatureGroupName=feature_group_name
    )
```

Add a description to the feature.

```
sagemaker_client.update_feature_metadata(
    FeatureGroupName=feature_group_name,
    FeatureName="feature-1",
    Description="new description"
)
```

You can use the [`DescribeFeatureMetadata`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureMetadata.html) operation to see if you successfully updated the description for the feature group.

```
    sagemaker_client.describe_feature_metadata(
    FeatureGroupName=feature_group_name,
    FeatureName="feature-1"
)
```

You can also use it to add parameters to the feature group.

```
sagemaker_client.update_feature_metadata(
    FeatureGroupName=feature_group_name,
    FeatureName="feature-1",
    ParameterAdditions=[
        {"Key": "team", "Value": "featurestore"},
        {"Key": "org", "Value": "sagemaker"},
    ]
)
```

You can use the [`DescribeFeatureMetadata`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureMetadata.html) operation again to see if you have successfully added the parameters.

```
    sagemaker_client.describe_feature_metadata(
    FeatureGroupName=feature_group_name,
    FeatureName="feature-1"
)
```