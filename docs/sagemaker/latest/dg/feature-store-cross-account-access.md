# Enabling cross account access

The access permissions are read-only, read-write, and admin permissions. The permission name,
description, and list of specific APIs available for each permission are listed in the
following:

- Read-only permission (`AWSRAMPermissionSageMakerFeatureGroupReadOnly`): The read
  privilege allows resource consumer accounts to read records in the shared feature groups and
  view details and metadata.
  - `DescribeFeatureGroup`: Retrieves details about a feature group and its
    configuration
  - `DescribeFeatureMetadata`: Shows the metadata for a feature within a feature
    group
  - `BatchGetRecord`: Retrieves a batch of records from a feature group
  - `GetRecord`: Retrieves a record from a feature group

- Read-write permission (`AWSRAMPermissionSagemakerFeatureGroupReadWrite`): The
  read-write privilege allows resource consumer accounts to write records to, and delete records
  from, the shared feature groups, in addition to read permissions.
  - `PutRecord`: Writes a record to a feature group
  - `DeleteRecord`: Removes a record from a feature group
  - APIs listed in `AWSRAMPermissionSageMakerFeatureGroupReadOnly`

- Admin permission (`AWSRAMPermissionSagemakerFeatureGroupAdmin`): The admin
  privilege allows the resource consumer accounts to update the description and parameters of
  features within the shared feature groups, update the configuration of the shared feature
  groups, in addition to read-write permissions.

      + `DescribeFeatureMetadata`: Shows the metadata for a feature within a feature
       group
      + `UpdateFeatureGroup`: Updates a feature group configuration
      + `UpdateFeatureMetadata`: Updates description and parameters of a feature in
       the feature group
      + APIs listed in `AWSRAMPermissionSagemakerFeatureGroupReadWrite`

  In the following topics you can learn how to share online store and offline feature
  groups—there are differences between the two when it comes to sharing.

###### Topics

- [Share online feature groups with
  AWS Resource Access Manager](feature-store-cross-account-access-online-store.md "feature-store-cross-account-access-online-store.md")
- [Cross account offline store
  access](feature-store-cross-account-access-offline-store.md "feature-store-cross-account-access-offline-store.md")
