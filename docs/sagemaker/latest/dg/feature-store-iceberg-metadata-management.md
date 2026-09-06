

# Iceberg metadata management
<a name="feature-store-iceberg-metadata-management"></a>

When you create a feature group with the Iceberg table format, Amazon SageMaker Feature Store creates and manages the underlying Iceberg table on your behalf using default configuration values. You can configure Iceberg table properties at feature group creation, update properties on an existing feature group, and view the properties currently set on the table. These settings give you control over configuration parameters such as snapshot retention, metadata file management, and write behavior to manage the overall size and performance of your offline store table.

Only a subset of Iceberg table properties have been validated for compatibility with Feature Store. Configuring properties outside this supported set does not guarantee correct behavior. For the full list of supported properties, see [Allowed Iceberg properties](#feature-store-iceberg-allowed-properties).

**Prerequisite:** Your feature group must have an offline store using the Iceberg table format.

**Important**  
If non-allowed Iceberg properties are changed, Feature Store cannot guarantee continued compatibility and may lead to an inability to write to the offline store.

## IcebergProperties type
<a name="feature-store-iceberg-properties-type"></a>

The `IcebergProperties` type provides a validated wrapper for Iceberg property configurations, ensuring all keys belong to the allowed set and preventing duplicate entries.

```
class IcebergProperties(Base):
    """Configuration for Iceberg table properties in a Feature Group offline store."""
    properties: Optional[Dict[str, str]] = None
```

### Validating properties
<a name="feature-store-iceberg-validating-properties"></a>

Invalid and duplicate keys result in an error when passed to the create or update function. You can optionally validate keys using the `validate_property_keys()` method. This is helpful when adding or removing properties from an existing `IcebergProperties` object.

```
iceberg_properties = IcebergProperties(  # Validates on creation
    properties={
        "write.target-file-size-bytes": "268435456",
        "write.delete.mode": "merge-on-read",
    }
)

# Add non-allowed property
iceberg_properties.properties.update({"write.delete.isolation-level": "Snapshot"})

# Validate again — throws error because of non-allowed property
iceberg_properties.validate_property_keys()
```

## Create a feature group with Iceberg properties
<a name="feature-store-iceberg-create"></a>

The `FeatureGroupManager.create` function accepts an `iceberg_properties` parameter of type `IcebergProperties`. It creates a feature group and waits for creation to complete before updating the Iceberg properties on the underlying AWS Glue table.

Alternatively, you can create a `FeatureGroup`, call `create`, then pass the feature group object to the `FeatureGroupManager` class and call `update` to avoid blocking while the feature group finishes creating.

```
fg = FeatureGroupManager.create(
    # ...other parameters...
    offline_store_config=OfflineStoreConfig(
        s3_storage_config=S3StorageConfig(s3_uri="s3://my-bucket/features/"),
        table_format="Iceberg",  # Must use Iceberg table format
    ),
    iceberg_properties=IcebergProperties(
        properties={
            "write.target-file-size-bytes": "536870912",
            "history.expire.min-snapshots-to-keep": "3",
        }
    ),
)
```

## Update Iceberg properties on an existing feature group
<a name="feature-store-iceberg-update"></a>

The `update` function accepts an `iceberg_properties` parameter of type `IcebergProperties`. It takes an already-created feature group, retrieves the AWS Glue Data Catalog of the offline store, and sets the specified Iceberg properties.

```
fg = FeatureGroupManager.get(feature_group_name="my-feature-group")
fg.update(
    iceberg_properties=IcebergProperties(
        properties={
            "write.target-file-size-bytes": "268435456",
            "write.delete.mode": "merge-on-read",
        }
    ),
)
```

## View Iceberg properties on a feature group
<a name="feature-store-iceberg-get"></a>

The `FeatureGroupManager.get` function accepts an `include_iceberg_properties` parameter. When set to `True`, it retrieves the Iceberg properties that have been manually set and are part of the allowed list, and adds them to the `iceberg_properties` field in the returned object.

This only returns set properties that are part of the allowed list. To get all AWS Glue table properties, use the AWS Glue API directly. If an allowed Iceberg property does not appear, it has not been explicitly set and uses its default value.

```
fg = FeatureGroupManager.get(
    feature_group_name="my-feature-group",
    include_iceberg_properties=True,
)
print(fg.iceberg_properties.properties)
# e.g. {"write.target-file-size-bytes": "536870912"}
```

## Required permissions
<a name="feature-store-iceberg-permissions"></a>

Ensure both the [AmazonSageMakerFeatureStoreAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFeatureStoreAccess.html) and the [AmazonSageMakerFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSageMakerFullAccess.html) managed policies are attached to the IAM role you are using. Manage your policy based on your access pattern.

## Allowed Iceberg properties
<a name="feature-store-iceberg-allowed-properties"></a>

The following table lists the Iceberg table properties that have been validated for use with Feature Store. For more information about these properties, see [Table configuration](https://iceberg.apache.org/docs/latest/configuration/) in the Apache Iceberg documentation.


**Allowed Iceberg table properties**  

| Property | Default value | Description | 
| --- | --- | --- | 
| write.metadata.delete-after-commit.enabled | false | Controls whether to delete the oldest tracked version metadata files after each table commit. | 
| write.metadata.previous-versions-max | 100 | The max number of previous version metadata files to track. | 
| history.expire.max-snapshot-age-ms | 432000000 (5 days) | Default max age of snapshots to keep on the table and all of its branches while expiring snapshots. | 
| history.expire.min-snapshots-to-keep | 1 | Default min number of snapshots to keep on the table and all of its branches while expiring snapshots. | 
| history.expire.max-ref-age-ms | Long.MAX\_VALUE (forever) | For snapshot references except the main branch, default max age of snapshot references to keep while expiring snapshots. The main branch never expires. | 
| write.target-file-size-bytes | 536870912 (512 MB) | Controls the size of files generated to target about this many bytes. | 
| write.delete.target-file-size-bytes | 67108864 (64 MB) | Controls the size of delete files generated to target about this many bytes. | 
| write.delete.mode | copy-on-write | Mode used for delete commands: copy-on-write or merge-on-read (v2 and above). | 
| write.update.mode | copy-on-write | Mode used for update commands: copy-on-write or merge-on-read (v2 and above). | 
| write.delete.granularity | partition | Controls the granularity of generated delete files: partition or file. | 
| write.parquet.row-group-size-bytes | 134217728 (128 MB) | Parquet row group size. | 
| read.split.target-size | 134217728 (128 MB) | Target size when combining data input splits. | 
| read.split.metadata-target-size | 33554432 (32 MB) | Target size when combining metadata input splits. | 
| read.split.open-file-cost | 4194304 (4 MB) | The estimated cost to open a file, used as a minimum weight when combining splits. | 