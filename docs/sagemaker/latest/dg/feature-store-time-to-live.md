# Time to live (TTL) duration for records

Amazon SageMaker Feature Store provides the option for records to be hard deleted from the online store after a
time duration is reached, with time to live (TTL) duration (`TtlDuration`). The record
will expire after the record’s `EventTime` plus the `TtlDuration` is
reached, or `ExpiresAt` = `EventTime` + `TtlDuration`. The
`TtlDuration` can be applied at a feature group level, where all records within the
feature group will have the `TtlDuration` by default, or at an individual record level.
If `TtlDuration` is unspecified, the default value is `null` and the record
will remain in the online store until it is overwritten.

A record deleted using `TtlDuration` is hard deleted, or completely removed from
the online store, and the deleted record is added to the offline store. For more information on
hard delete and deletion modes, see [`DeleteRecord`](../APIReference/API_feature_store_DeleteRecord.md "../APIReference/API_feature_store_DeleteRecord.md") in the Amazon SageMaker API Reference guide. When a record is hard
deleted it immediately becomes inaccessible using Feature Store APIs.

###### Important

TTL typically deletes expired items within a few days. Depending on the size and activity
level of a table, the actual delete operation of an expired item can vary. Because TTL is meant
to be a background process, the nature of the capacity used to expire and delete items via TTL is
variable (but free of charge). For more information on how items are deleted from a DynamoDB table,
see [How it works: DynamoDB Time to Live (TTL)](../../../amazondynamodb/latest/developerguide/howitworks-ttl.md "../../../amazondynamodb/latest/developerguide/howitworks-ttl.md").

`TtlDuration` must be a dictionary containing a `Unit` and a
`Value`, where the `Unit` must be a string with values "Seconds",
"Minutes", "Hours", "Days", or "Weeks" and `Value` must be an integer greater than or
equal to 1. `TtlDuration` can be applied while using the
`CreateFeatureGroup`, `UpdateFeatureGroup`, and `PutRecord`
APIs. See the request and response syntax in the SDK for Python (Boto3) documentation for [`CreateFeatureGroup`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_feature_group.html#SageMaker.Client.create_feature_group "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_feature_group.html#SageMaker.Client.create_feature_group"), [`UpdateFeatureGroup`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_feature_group.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/update_feature_group.html"), and [`PutRecord`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/put_record.html# "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/put_record.html#") APIs.

- When `TtlDuration` is applied at a feature group level (using the
  `CreateFeatureGroup` or `UpdateFeatureGroup` APIs), the applied
  `TtlDuration` becomes the default `TtlDuration` for all records that are
  added to the feature group _from the point in time that the API is
  called_. When applying `TtlDuration` with the
  `UpdateFeatureGroup` API, this will _not_ become
  the default `TtlDuration` for records that were created _before_ the API is called.

To remove the default `TtlDuration` from an existing feature group, use the
`UpdateFeatureGroup` API and set the `TtlDuration`
`Unit` and `Value` to `null`.

- When `TtlDuration` is applied at a record level (for example, using
  `PutRecord` API), the `TtlDuration` duration applies to that record and
  is used instead of the feature group level default `TtlDuration`.
- When `TtlDuration` is applied on a feature group level it may take a few minutes
  for `TtlDuration` to come into effect.
- If `TtlDuration` is used when there is no online store, you will receive a
  `Validation Exception (400)` error.
  The following example code shows how to apply `TtlDuration` while updating a
  feature group, such that the records added to the feature group _after
  running the API_ will by default expire four weeks after their event times.

```
import boto3

sagemaker_client = boto3.client("sagemaker")
feature_group_name = '`<YOUR_FEATURE_GROUP_NAME>`'

sagemaker_client.update_feature_group(
    FeatureGroupName=feature_group_name,
    OnlineStoreConfig={
        TtlDuration:{
            Unit: "Weeks",
            Value: 4
        }
    }
)
```

You can use the `DescribeFeatureGroup` API to view the default
`TtlDuration`.

To view the expiration times, `ExpiresAt` (in UTC time ISO-8601 format), while
using the `GetRecord` or `BatchGetRecord` APIs you must set
`ExpirationTimeResponse` to `ENABLED`. See the request and response syntax
in the SDK for Python (Boto3) documentation for [`DescribeFeatureGroup`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_feature_group.html#describe-feature-group "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_feature_group.html#describe-feature-group"), [`GetRecord`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/get_record.html#get-record "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/get_record.html#get-record"), and [`BatchGetRecord`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/batch_get_record.html#batch-get-record "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker-featurestore-runtime/client/batch_get_record.html#batch-get-record") APIs.
