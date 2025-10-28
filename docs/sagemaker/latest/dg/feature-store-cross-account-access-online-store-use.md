# Use online store shared

resources with access permissions

The resource owner account must grant permissions to resource consumer accounts to allow for
discoverability, read-only, write, or admin privileges with a shared resource. In the following
sections, we provide instructions on how to accept an invitation to access shared resources and
provide examples showing how to view and interact with shared feature groups.

**Accept an invitation to access shared resources using
AWS RAM**

As the resource consumer account, you will receive an invitation to join a resource share
once the resource owner account has granted permission. To accept the invitation to any shared
resources, open the [Shared with me:
Resource shares](https://console.aws.amazon.com/ram/home#SharedResourceShares "https://console.aws.amazon.com/ram/home#SharedResourceShares") page in the AWS RAM console to view and respond to invitations.
Invitations are not sent in these cases:

- If you are part of an organization in AWS Organizations and sharing in your organization is
  enabled, then principals in the organization automatically get access to the shared
  resources without invitations.
- If you share with the AWS account that owns the resource, then the principals in that
  account automatically get access to the shared resources without invitations.
  For more information about accepting and using a resource share in AWS RAM, see [Using shared AWS
  resources](../../../ram/latest/userguide/getting-started-shared.md "../../../ram/latest/userguide/getting-started-shared.md") in the AWS RAM User Guide.

## View shared

resources on the AWS RAM console

Granting any access permissions does not grant resource consumer accounts the
discoverability permission, so the resource consumer accounts with access permissions cannot
search and discover those feature groups. To allow for resource consumer accounts to search
and discover feature groups from the resource owner account, the resource owner account must
grant the discoverability permission to the resource consumer accounts, where all of the
feature groups within the resource owner account are discoverable by the resource consumer
accounts. For more information about granting the discoverability permission, see [Enabling cross account
discoverability](feature-store-cross-account-discoverability.md "feature-store-cross-account-discoverability.md").

To view the shared resources on the AWS RAM console, open the [Shared with me: Resource shares](https://console.aws.amazon.com/ram/home#SharedResourceShares "https://console.aws.amazon.com/ram/home#SharedResourceShares") page in the
AWS RAM console.

## Read

and write actions with a shared feature groups example

Once your resource consumer account is granted the appropriate permissions by the resource
owner account, you can perform actions on the shared resources using the Feature Store SDK. You can do
this by providing the resource ARN as the `FeatureGroupName`. To obtain the Feature
Group ARN, you can use the AWS SDK for Python (Boto3) [`DescribeFeatureGroup`](https://boto3.amazonaws.com/v1/documentation/api/1.26.98/reference/services/sagemaker/client/describe_feature_group.html#describe-feature-group "https://boto3.amazonaws.com/v1/documentation/api/1.26.98/reference/services/sagemaker/client/describe_feature_group.html#describe-feature-group") function or use the console UI. For information
about using the console UI to view feature group details, see [View feature group details
from the console](feature-store-use-with-studio.md#feature-store-view-feature-group-detail-studio "feature-store-use-with-studio.md#feature-store-view-feature-group-detail-studio").

The following examples use `PutRecord` and `GetRecord` with a shared
feature group entity. See the request and response syntax in the AWS SDK for Python (Boto3) documentation
for [`PutRecord`](https://boto3.amazonaws.com/v1/documentation/api/1.26.98/reference/services/firehose/client/put_record.html#put-record "https://boto3.amazonaws.com/v1/documentation/api/1.26.98/reference/services/firehose/client/put_record.html#put-record") and [`GetRecordAPIs`](https://boto3.amazonaws.com/v1/documentation/api/1.26.98/reference/services/sagemaker-featurestore-runtime/client/get_record.html#get-record "https://boto3.amazonaws.com/v1/documentation/api/1.26.98/reference/services/sagemaker-featurestore-runtime/client/get_record.html#get-record").

```
import boto3

sagemaker_featurestore_runtime = boto3.client('sagemaker-featurestore-runtime')

# Put record into feature group named 'test-fg' within the resource owner account ID 111122223333
featurestore_runtime.put_record(
    FeatureGroupName="arn:aws:sagemaker:us-east-1:111122223333:feature-group/test-fg",
    Record=[value.to_dict() for value in record] # You will need to define record prior to calling PutRecord
)
```

```
import boto3

sagemaker_featurestore_runtime = boto3.client('sagemaker-featurestore-runtime')

# Choose record identifier
record_identifier_value = str(2990130)

# Get record from feature group named 'test-fg' within the resource owner account ID 111122223333
featurestore_runtime.get_record(
    FeatureGroupName="arn:aws:sagemaker:us-east-1:111122223333:feature-group/test-fg",
    RecordIdentifierValueAsString=record_identifier_value
)
```

For more information about granting permissions to feature group entities, see [Share
your feature group entities](feature-store-cross-account-access-online-store-share-feature-group.md "feature-store-cross-account-access-online-store-share-feature-group.md").
