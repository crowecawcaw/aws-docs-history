# Schema registry

The Schema registry API describes the data types and API related to working
with schemas in AWS Glue.

## Data types

- [RegistryId structure](#aws-glue-api-schema-registry-api-RegistryId "#aws-glue-api-schema-registry-api-RegistryId")
- [RegistryListItem structure](#aws-glue-api-schema-registry-api-RegistryListItem "#aws-glue-api-schema-registry-api-RegistryListItem")
- [MetadataInfo structure](#aws-glue-api-schema-registry-api-MetadataInfo "#aws-glue-api-schema-registry-api-MetadataInfo")
- [OtherMetadataValueListItem structure](#aws-glue-api-schema-registry-api-OtherMetadataValueListItem "#aws-glue-api-schema-registry-api-OtherMetadataValueListItem")
- [SchemaListItem structure](#aws-glue-api-schema-registry-api-SchemaListItem "#aws-glue-api-schema-registry-api-SchemaListItem")
- [SchemaVersionListItem structure](#aws-glue-api-schema-registry-api-SchemaVersionListItem "#aws-glue-api-schema-registry-api-SchemaVersionListItem")
- [MetadataKeyValuePair structure](#aws-glue-api-schema-registry-api-MetadataKeyValuePair "#aws-glue-api-schema-registry-api-MetadataKeyValuePair")
- [SchemaVersionErrorItem structure](#aws-glue-api-schema-registry-api-SchemaVersionErrorItem "#aws-glue-api-schema-registry-api-SchemaVersionErrorItem")
- [ErrorDetails structure](#aws-glue-api-schema-registry-api-ErrorDetails "#aws-glue-api-schema-registry-api-ErrorDetails")
- [SchemaVersionNumber structure](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber")
- [SchemaId structure](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId")

## RegistryId structure

A wrapper structure that may contain the registry name and Amazon Resource
Name (ARN).

###### Fields

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

Name of the registry. Used only for lookup. One of `RegistryArn`
or `RegistryName` has to be provided.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

Arn of the registry to be updated. One of `RegistryArn` or
`RegistryName` has to be provided.

## RegistryListItem structure

A structure containing the details for a registry.

###### Fields

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the registry.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the registry.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `DELETING`).

The status of the registry.

- `CreatedTime` – UTF-8 string.

The data the registry was created.

- `UpdatedTime` – UTF-8 string.

The date the registry was updated.

## MetadataInfo structure

A structure containing metadata information for a schema version.

###### Fields

- `MetadataValue` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

The metadata key's corresponding value.

- `CreatedTime` – UTF-8 string.

The time at which the entry was created.

- `OtherMetadataValueList` – An array of [OtherMetadataValueListItem](#aws-glue-api-schema-registry-api-OtherMetadataValueListItem "#aws-glue-api-schema-registry-api-OtherMetadataValueListItem") objects.

Other metadata belonging to the same metadata key.

## OtherMetadataValueListItem structure

A structure containing other metadata for a schema version belonging
to the same metadata key.

###### Fields

- `MetadataValue` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

The metadata key's corresponding value for the other metadata belonging
to the same metadata key.

- `CreatedTime` – UTF-8 string.

The time at which the entry was created.

## SchemaListItem structure

An object that contains minimal details for a schema.

###### Fields

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

the name of the registry where the schema resides.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema.

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) for the schema.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description for the schema.

- `SchemaStatus` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `DELETING`).

The status of the schema.

- `CreatedTime` – UTF-8 string.

The date and time that a schema was created.

- `UpdatedTime` – UTF-8 string.

The date and time that a schema was updated.

## SchemaVersionListItem structure

An object containing the details about a schema version.

###### Fields

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique identifier of the schema version.

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `FAILURE` | `DELETING`).

The status of the schema version.

- `CreatedTime` – UTF-8 string.

The date and time the schema version was created.

## MetadataKeyValuePair structure

A structure containing a key value pair for metadata.

###### Fields

- `MetadataKey` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

A metadata key.

- `MetadataValue` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

A metadata key's corresponding value.

## SchemaVersionErrorItem structure

An object that contains the error details for an operation on a schema version.

###### Fields

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

- `ErrorDetails` – An [ErrorDetails](#aws-glue-api-schema-registry-api-ErrorDetails "#aws-glue-api-schema-registry-api-ErrorDetails") object.

The details of the error for the schema version.

## ErrorDetails structure

An object containing error details.

###### Fields

- `ErrorCode` – UTF-8 string.

The error code for an error.

- `ErrorMessage` – UTF-8 string.

The error message for an error.

## SchemaVersionNumber structure

A structure containing the schema version information.

###### Fields

- `LatestVersion` – Boolean.

The latest version available for the schema.

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

## SchemaId structure

The unique ID of the schema in the AWS Glue schema registry.

###### Fields

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema. One of `SchemaArn`
or `SchemaName` has to be provided.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema. One of `SchemaArn` or `SchemaName`
has to be provided.

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema registry that contains the schema.

## Operations

- [CreateRegistry action (Python: create_registry)](#aws-glue-api-schema-registry-api-CreateRegistry "#aws-glue-api-schema-registry-api-CreateRegistry")
- [CreateSchema action (Python: create_schema)](#aws-glue-api-schema-registry-api-CreateSchema "#aws-glue-api-schema-registry-api-CreateSchema")
- [GetSchema action (Python: get_schema)](#aws-glue-api-schema-registry-api-GetSchema "#aws-glue-api-schema-registry-api-GetSchema")
- [ListSchemaVersions action (Python: list_schema_versions)](#aws-glue-api-schema-registry-api-ListSchemaVersions "#aws-glue-api-schema-registry-api-ListSchemaVersions")
- [GetSchemaVersion action (Python: get_schema_version)](#aws-glue-api-schema-registry-api-GetSchemaVersion "#aws-glue-api-schema-registry-api-GetSchemaVersion")
- [GetSchemaVersionsDiff action (Python: get_schema_versions_diff)](#aws-glue-api-schema-registry-api-GetSchemaVersionsDiff "#aws-glue-api-schema-registry-api-GetSchemaVersionsDiff")
- [ListRegistries action (Python: list_registries)](#aws-glue-api-schema-registry-api-ListRegistries "#aws-glue-api-schema-registry-api-ListRegistries")
- [ListSchemas action (Python: list_schemas)](#aws-glue-api-schema-registry-api-ListSchemas "#aws-glue-api-schema-registry-api-ListSchemas")
- [RegisterSchemaVersion action (Python: register_schema_version)](#aws-glue-api-schema-registry-api-RegisterSchemaVersion "#aws-glue-api-schema-registry-api-RegisterSchemaVersion")
- [UpdateSchema action (Python: update_schema)](#aws-glue-api-schema-registry-api-UpdateSchema "#aws-glue-api-schema-registry-api-UpdateSchema")
- [CheckSchemaVersionValidity action (Python: check_schema_version_validity)](#aws-glue-api-schema-registry-api-CheckSchemaVersionValidity "#aws-glue-api-schema-registry-api-CheckSchemaVersionValidity")
- [UpdateRegistry action (Python: update_registry)](#aws-glue-api-schema-registry-api-UpdateRegistry "#aws-glue-api-schema-registry-api-UpdateRegistry")
- [GetSchemaByDefinition action (Python: get_schema_by_definition)](#aws-glue-api-schema-registry-api-GetSchemaByDefinition "#aws-glue-api-schema-registry-api-GetSchemaByDefinition")
- [GetRegistry action (Python: get_registry)](#aws-glue-api-schema-registry-api-GetRegistry "#aws-glue-api-schema-registry-api-GetRegistry")
- [PutSchemaVersionMetadata action (Python: put_schema_version_metadata)](#aws-glue-api-schema-registry-api-PutSchemaVersionMetadata "#aws-glue-api-schema-registry-api-PutSchemaVersionMetadata")
- [QuerySchemaVersionMetadata action (Python: query_schema_version_metadata)](#aws-glue-api-schema-registry-api-QuerySchemaVersionMetadata "#aws-glue-api-schema-registry-api-QuerySchemaVersionMetadata")
- [RemoveSchemaVersionMetadata action (Python: remove_schema_version_metadata)](#aws-glue-api-schema-registry-api-RemoveSchemaVersionMetadata "#aws-glue-api-schema-registry-api-RemoveSchemaVersionMetadata")
- [DeleteRegistry action (Python: delete_registry)](#aws-glue-api-schema-registry-api-DeleteRegistry "#aws-glue-api-schema-registry-api-DeleteRegistry")
- [DeleteSchema action (Python: delete_schema)](#aws-glue-api-schema-registry-api-DeleteSchema "#aws-glue-api-schema-registry-api-DeleteSchema")
- [DeleteSchemaVersions action (Python: delete_schema_versions)](#aws-glue-api-schema-registry-api-DeleteSchemaVersions "#aws-glue-api-schema-registry-api-DeleteSchemaVersions")

## CreateRegistry action (Python: create_registry)

Creates a new registry which may be used to hold a collection of schemas.

###### Request

- `RegistryName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

Name of the registry to be created of max length of 255, and may only contain
letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the registry. If description is not provided, there will
not be any default value for this.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

AWS tags that contain a key value pair and may be searched
by console, command line, or API.

###### Response

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the newly created registry.

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the registry.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags for the registry.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `AlreadyExistsException`
- `ResourceNumberLimitExceededException`
- `ConcurrentModificationException`
- `ThrottlingException`
- `InternalServiceException`

## CreateSchema action (Python: create_schema)

Creates a new schema set and registers the schema definition. Returns
an error if the schema set already exists without actually registering the version.

When the schema set is created, a version checkpoint will be set to the first
version. Compatibility mode "DISABLED" restricts any additional schema versions
from being added after the first schema version. For all other compatibility
modes, validation of compatibility settings will be applied only from the second
version onwards when the `RegisterSchemaVersion` API is used.

When this API is called without a `RegistryId`, this will
create an entry for a "default-registry" in the registry database tables, if
it is not already present.

###### Request

- `RegistryId` – A [RegistryId](#aws-glue-api-schema-registry-api-RegistryId "#aws-glue-api-schema-registry-api-RegistryId") object.

This is a wrapper shape to contain the registry identity fields. If this
is not provided, the default registry will be used. The ARN format for the same
will be: `arn:aws:glue:us-east-2:<customer id>:registry/default-registry:random-5-letter-id`.

- `SchemaName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

Name of the schema to be created of max length of 255, and may only contain
letters, numbers, hyphen, underscore, dollar sign, or hash mark. No whitespace.

- `DataFormat` – _Required:_ UTF-8 string (valid values: `AVRO` | `JSON` | `PROTOBUF`).

The data format of the schema definition. Currently `AVRO`,
`JSON` and `PROTOBUF` are supported.

- `Compatibility` – UTF-8 string (valid values: `NONE` | `DISABLED` | `BACKWARD` | `BACKWARD_ALL` | `FORWARD` | `FORWARD_ALL` | `FULL` | `FULL_ALL`).

The compatibility mode of the schema. The possible values are:

    + *NONE*: No compatibility mode applies. You can
     use this choice in development scenarios or if you do not know the compatibility
     mode that you want to apply to schemas. Any new version added will be accepted without
     undergoing a compatibility check.
    + *DISABLED*: This compatibility choice prevents
     versioning for a particular schema. You can use this choice to prevent future
     versioning of a schema.
    + *BACKWARD*: This compatibility choice is recommended
     as it allows data receivers to read both the current and one previous schema version.
     This means that for instance, a new schema version cannot drop data fields or change
     the type of these fields, so they can't be read by readers using the previous version.
    + *BACKWARD\_ALL*: This compatibility choice allows
     data receivers to read both the current and all previous schema versions. You
     can use this choice when you need to delete fields or add optional fields, and check
     compatibility against all previous schema versions.
    + *FORWARD*: This compatibility choice allows data
     receivers to read both the current and one next schema version, but not necessarily
     later versions. You can use this choice when you need to add fields or delete optional
     fields, but only check compatibility against the last schema version.
    + *FORWARD\_ALL*: This compatibility choice allows
     data receivers to read written by producers of any new registered schema. You
     can use this choice when you need to add fields or delete optional fields, and check
     compatibility against all previous schema versions.
    + *FULL*: This compatibility choice allows data
     receivers to read data written by producers using the previous or next version
     of the schema, but not necessarily earlier or later versions. You can use this
     choice when you need to add or remove optional fields, but only check compatibility
     against the last schema version.
    + *FULL\_ALL*: This compatibility choice allows
     data receivers to read data written by producers using all previous schema versions.
     You can use this choice when you need to add or remove optional fields, and check
     compatibility against all previous schema versions.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

An optional description of the schema. If description is not provided,
there will not be any automatic default value for this.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

AWS tags that contain a key value pair and may be searched
by console, command line, or API. If specified, follows the AWS tags-on-create pattern.

- `SchemaDefinition` – UTF-8 string, not less than 1 or more than 170000 bytes long, matching the [Custom string pattern #13](aws-glue-api-common.md#regex_13 "aws-glue-api-common.md#regex_13").

The schema definition using the `DataFormat` setting for
`SchemaName`.

###### Response

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the registry.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema.

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the schema if specified when created.

- `DataFormat` – UTF-8 string (valid values: `AVRO` | `JSON` | `PROTOBUF`).

The data format of the schema definition. Currently `AVRO`,
`JSON` and `PROTOBUF` are supported.

- `Compatibility` – UTF-8 string (valid values: `NONE` | `DISABLED` | `BACKWARD` | `BACKWARD_ALL` | `FORWARD` | `FORWARD_ALL` | `FULL` | `FULL_ALL`).

The schema compatibility mode.

- `SchemaCheckpoint` – Number (long), not less than 1 or more than 100000.

The version number of the checkpoint (the last time the compatibility
mode was changed).

- `LatestSchemaVersion` – Number (long), not less than 1 or more than 100000.

The latest version of the schema associated with the returned schema definition.

- `NextSchemaVersion` – Number (long), not less than 1 or more than 100000.

The next version of the schema associated with the returned schema definition.

- `SchemaStatus` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `DELETING`).

The status of the schema.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags for the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique identifier of the first schema version.

- `SchemaVersionStatus` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `FAILURE` | `DELETING`).

The status of the first schema version created.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `AlreadyExistsException`
- `ResourceNumberLimitExceededException`
- `ConcurrentModificationException`
- `ThrottlingException`
- `InternalServiceException`

## GetSchema action (Python: get_schema)

Describes the specified schema in detail.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either
     `SchemaArn` or `SchemaName` and `RegistryName`
     has to be provided.
    + SchemaId$SchemaName: The name of the schema. Either `SchemaArn`
     or `SchemaName` and `RegistryName` has to be provided.

###### Response

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the registry.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema.

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of schema if specified when created

- `DataFormat` – UTF-8 string (valid values: `AVRO` | `JSON` | `PROTOBUF`).

The data format of the schema definition. Currently `AVRO`,
`JSON` and `PROTOBUF` are supported.

- `Compatibility` – UTF-8 string (valid values: `NONE` | `DISABLED` | `BACKWARD` | `BACKWARD_ALL` | `FORWARD` | `FORWARD_ALL` | `FULL` | `FULL_ALL`).

The compatibility mode of the schema.

- `SchemaCheckpoint` – Number (long), not less than 1 or more than 100000.

The version number of the checkpoint (the last time the compatibility
mode was changed).

- `LatestSchemaVersion` – Number (long), not less than 1 or more than 100000.

The latest version of the schema associated with the returned schema definition.

- `NextSchemaVersion` – Number (long), not less than 1 or more than 100000.

The next version of the schema associated with the returned schema definition.

- `SchemaStatus` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `DELETING`).

The status of the schema.

- `CreatedTime` – UTF-8 string.

The date and time the schema was created.

- `UpdatedTime` – UTF-8 string.

The date and time the schema was updated.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ThrottlingException`
- `InternalServiceException`

## ListSchemaVersions action (Python: list_schema_versions)

Returns a list of schema versions that you have created, with minimal information.
Schema versions in Deleted status will not be included in the results. Empty results
will be returned if there are no schema versions available.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either
     `SchemaArn` or `SchemaName` and `RegistryName`
     has to be provided.
    + SchemaId$SchemaName: The name of the schema. Either `SchemaArn`
     or `SchemaName` and `RegistryName` has to be provided.

- `MaxResults` – Number (integer), not less than 1 or more than 100.

Maximum number of results required per page. If the value is not supplied,
this will be defaulted to 25 per page.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `Schemas` – An array of [SchemaVersionListItem](#aws-glue-api-schema-registry-api-SchemaVersionListItem "#aws-glue-api-schema-registry-api-SchemaVersionListItem") objects.

An array of `SchemaVersionList` objects containing details
of each schema version.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ThrottlingException`
- `InternalServiceException`

## GetSchemaVersion action (Python: get_schema_version)

Get the specified schema by its unique ID assigned when a version of the
schema is created or registered. Schema versions in Deleted status will not be
included in the results.

###### Request

- `SchemaId` – A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either
     `SchemaArn` or `SchemaName` and `RegistryName`
     has to be provided.
    + SchemaId$SchemaName: The name of the schema. Either `SchemaArn`
     or `SchemaName` and `RegistryName` has to be provided.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The `SchemaVersionId` of the schema version. This field
is required for fetching by schema ID. Either this or the `SchemaId`
wrapper has to be provided.

- `SchemaVersionNumber` – A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

The version number of the schema.

###### Response

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The `SchemaVersionId` of the schema version.

- `SchemaDefinition` – UTF-8 string, not less than 1 or more than 170000 bytes long, matching the [Custom string pattern #13](aws-glue-api-common.md#regex_13 "aws-glue-api-common.md#regex_13").

The schema definition for the schema ID.

- `DataFormat` – UTF-8 string (valid values: `AVRO` | `JSON` | `PROTOBUF`).

The data format of the schema definition. Currently `AVRO`,
`JSON` and `PROTOBUF` are supported.

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `FAILURE` | `DELETING`).

The status of the schema version.

- `CreatedTime` – UTF-8 string.

The date and time the schema version was created.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ThrottlingException`
- `InternalServiceException`

## GetSchemaVersionsDiff action (Python: get_schema_versions_diff)

Fetches the schema version difference in the specified difference type
between two stored schema versions in the Schema Registry.

This API allows you to compare two schema versions between two schema definitions
under the same schema.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One
     of `SchemaArn` or `SchemaName` has to be provided.
    + SchemaId$SchemaName: The name of the schema. One of `SchemaArn`
     or `SchemaName` has to be provided.

- `FirstSchemaVersionNumber` – _Required:_ A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

The first of the two schema versions to be compared.

- `SecondSchemaVersionNumber` – _Required:_ A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

The second of the two schema versions to be compared.

- `SchemaDiffType` – _Required:_ UTF-8 string (valid values: `SYNTAX_DIFF`).

Refers to `SYNTAX_DIFF`, which is the currently supported
diff type.

###### Response

- `Diff` – UTF-8 string, not less than 1 or more than 340000 bytes long, matching the [Custom string pattern #13](aws-glue-api-common.md#regex_13 "aws-glue-api-common.md#regex_13").

The difference between schemas as a string in JsonPatch format.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `AccessDeniedException`
- `ThrottlingException`
- `InternalServiceException`

## ListRegistries action (Python: list_registries)

Returns a list of registries that you have created, with minimal registry
information. Registries in the `Deleting` status will not be included
in the results. Empty results will be returned if there are no registries available.

###### Request

- `MaxResults` – Number (integer), not less than 1 or more than 100.

Maximum number of results required per page. If the value is not supplied,
this will be defaulted to 25 per page.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `Registries` – An array of [RegistryListItem](#aws-glue-api-schema-registry-api-RegistryListItem "#aws-glue-api-schema-registry-api-RegistryListItem") objects.

An array of `RegistryDetailedListItem` objects containing
minimal details of each registry.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `ThrottlingException`
- `InternalServiceException`

## ListSchemas action (Python: list_schemas)

Returns a list of schemas with minimal details. Schemas in Deleting status
will not be included in the results. Empty results will be returned if there are
no schemas available.

When the `RegistryId` is not provided, all the schemas across
registries will be part of the API response.

###### Request

- `RegistryId` – A [RegistryId](#aws-glue-api-schema-registry-api-RegistryId "#aws-glue-api-schema-registry-api-RegistryId") object.

A wrapper structure that may contain the registry name and Amazon Resource
Name (ARN).

- `MaxResults` – Number (integer), not less than 1 or more than 100.

Maximum number of results required per page. If the value is not supplied,
this will be defaulted to 25 per page.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `Schemas` – An array of [SchemaListItem](#aws-glue-api-schema-registry-api-SchemaListItem "#aws-glue-api-schema-registry-api-SchemaListItem") objects.

An array of `SchemaListItem` objects containing details
of each schema.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ThrottlingException`
- `InternalServiceException`

## RegisterSchemaVersion action (Python: register_schema_version)

Adds a new version to the existing schema. Returns an error if new version
of schema does not meet the compatibility requirements of the schema set. This
API will not create a new schema set and will return a 404 error if the schema set
is not already present in the Schema Registry.

If this is the first schema definition to be registered in the Schema Registry,
this API will store the schema version and return immediately. Otherwise, this
call has the potential to run longer than other operations due to compatibility
modes. You can call the `GetSchemaVersion` API with the `SchemaVersionId`
to check compatibility modes.

If the same schema definition is already stored in Schema Registry as a
version, the schema ID of the existing schema is returned to the caller.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. Either
     `SchemaArn` or `SchemaName` and `RegistryName`
     has to be provided.
    + SchemaId$SchemaName: The name of the schema. Either `SchemaArn`
     or `SchemaName` and `RegistryName` has to be provided.

- `SchemaDefinition` – _Required:_ UTF-8 string, not less than 1 or more than 170000 bytes long, matching the [Custom string pattern #13](aws-glue-api-common.md#regex_13 "aws-glue-api-common.md#regex_13").

The schema definition using the `DataFormat` setting for
the `SchemaName`.

###### Response

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique ID that represents the version of this schema.

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version of this schema (for sync flow only, in case this is the first
version).

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `FAILURE` | `DELETING`).

The status of the schema version.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ResourceNumberLimitExceededException`
- `ThrottlingException`
- `ConcurrentModificationException`
- `InternalServiceException`

## UpdateSchema action (Python: update_schema)

Updates the description, compatibility setting, or version checkpoint
for a schema set.

For updating the compatibility setting, the call will not validate compatibility
for the entire set of schema versions with the new compatibility setting. If the
value for `Compatibility` is provided, the `VersionNumber`
(a checkpoint) is also required. The API will validate the checkpoint version
number for consistency.

If the value for the `VersionNumber` (checkpoint) is provided,
`Compatibility` is optional and this can be used to set/reset a checkpoint
for the schema.

This update will happen only if the schema is in the AVAILABLE state.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One
     of `SchemaArn` or `SchemaName` has to be provided.
    + SchemaId$SchemaName: The name of the schema. One of `SchemaArn`
     or `SchemaName` has to be provided.

- `SchemaVersionNumber` – A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

Version number required for check pointing. One of `VersionNumber`
or `Compatibility` has to be provided.

- `Compatibility` – UTF-8 string (valid values: `NONE` | `DISABLED` | `BACKWARD` | `BACKWARD_ALL` | `FORWARD` | `FORWARD_ALL` | `FULL` | `FULL_ALL`).

The new compatibility setting for the schema.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The new description for the schema.

###### Response

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema.

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry that contains the schema.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ConcurrentModificationException`
- `ThrottlingException`
- `InternalServiceException`

## CheckSchemaVersionValidity action (Python: check_schema_version_validity)

Validates the supplied schema. This call has no side effects, it simply
validates using the supplied schema using `DataFormat` as the format.
Since it does not take a schema set name, no compatibility checks are performed.

###### Request

- `DataFormat` – _Required:_ UTF-8 string (valid values: `AVRO` | `JSON` | `PROTOBUF`).

The data format of the schema definition. Currently `AVRO`,
`JSON` and `PROTOBUF` are supported.

- `SchemaDefinition` – _Required:_ UTF-8 string, not less than 1 or more than 170000 bytes long, matching the [Custom string pattern #13](aws-glue-api-common.md#regex_13 "aws-glue-api-common.md#regex_13").

The definition of the schema that has to be validated.

###### Response

- `Valid` – Boolean.

Return true, if the schema is valid and false otherwise.

- `Error` – UTF-8 string, not less than 1 or more than 5000 bytes long.

A validation failure error message.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `ThrottlingException`
- `InternalServiceException`

## UpdateRegistry action (Python: update_registry)

Updates an existing registry which is used to hold a collection of schemas.
The updated properties relate to the registry, and do not modify any of the schemas
within the registry.

###### Request

- `RegistryId` – _Required:_ A [RegistryId](#aws-glue-api-schema-registry-api-RegistryId "#aws-glue-api-schema-registry-api-RegistryId") object.

This is a wrapper structure that may contain the registry name and Amazon
Resource Name (ARN).

- `Description` – _Required:_ Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the registry. If description is not provided, this field
will not be updated.

###### Response

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the updated registry.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource name (ARN) of the updated registry.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ConcurrentModificationException`
- `ThrottlingException`
- `InternalServiceException`

## GetSchemaByDefinition action (Python: get_schema_by_definition)

Retrieves a schema by the `SchemaDefinition`. The schema
definition is sent to the Schema Registry, canonicalized, and hashed. If the
hash is matched within the scope of the `SchemaName` or ARN (or the
default registry, if none is supplied), that schema's metadata is returned.
Otherwise, a 404 or NotFound error is returned. Schema versions in `Deleted`
statuses will not be included in the results.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure to contain schema identity fields. The structure
contains:

    + SchemaId$SchemaArn: The Amazon Resource Name (ARN) of the schema. One
     of `SchemaArn` or `SchemaName` has to be provided.
    + SchemaId$SchemaName: The name of the schema. One of `SchemaArn`
     or `SchemaName` has to be provided.

- `SchemaDefinition` – _Required:_ UTF-8 string, not less than 1 or more than 170000 bytes long, matching the [Custom string pattern #13](aws-glue-api-common.md#regex_13 "aws-glue-api-common.md#regex_13").

The definition of the schema for which schema details are required.

###### Response

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The schema ID of the schema version.

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `DataFormat` – UTF-8 string (valid values: `AVRO` | `JSON` | `PROTOBUF`).

The data format of the schema definition. Currently `AVRO`,
`JSON` and `PROTOBUF` are supported.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `FAILURE` | `DELETING`).

The status of the schema version.

- `CreatedTime` – UTF-8 string.

The date and time the schema was created.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ThrottlingException`
- `InternalServiceException`

## GetRegistry action (Python: get_registry)

Describes the specified registry in detail.

###### Request

- `RegistryId` – _Required:_ A [RegistryId](#aws-glue-api-schema-registry-api-RegistryId "#aws-glue-api-schema-registry-api-RegistryId") object.

This is a wrapper structure that may contain the registry name and Amazon
Resource Name (ARN).

###### Response

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the registry.

- `Description` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

A description of the registry.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `DELETING`).

The status of the registry.

- `CreatedTime` – UTF-8 string.

The date and time the registry was created.

- `UpdatedTime` – UTF-8 string.

The date and time the registry was updated.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `EntityNotFoundException`
- `ThrottlingException`
- `InternalServiceException`

## PutSchemaVersionMetadata action (Python: put_schema_version_metadata)

Puts the metadata key value pair for a specified schema version ID. A maximum
of 10 key value pairs will be allowed per schema version. They can be added over
one or more calls.

###### Request

- `SchemaId` – A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

The unique ID for the schema.

- `SchemaVersionNumber` – A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

The version number of the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique version ID of the schema version.

- `MetadataKeyValue` – _Required:_ A [MetadataKeyValuePair](#aws-glue-api-schema-registry-api-MetadataKeyValuePair "#aws-glue-api-schema-registry-api-MetadataKeyValuePair") object.

The metadata key's corresponding value.

###### Response

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) for the schema.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name for the schema.

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name for the registry.

- `LatestVersion` – Boolean.

The latest version of the schema.

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique version ID of the schema version.

- `MetadataKey` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

The metadata key.

- `MetadataValue` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

The value of the metadata key.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `AlreadyExistsException`
- `EntityNotFoundException`
- `ThrottlingException`
- `ResourceNumberLimitExceededException`

## QuerySchemaVersionMetadata action (Python: query_schema_version_metadata)

Queries for the schema version metadata information.

###### Request

- `SchemaId` – A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

A wrapper structure that may contain the schema name and Amazon Resource
Name (ARN).

- `SchemaVersionNumber` – A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

The version number of the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique version ID of the schema version.

- `MetadataList` – An array of [MetadataKeyValuePair](#aws-glue-api-schema-registry-api-MetadataKeyValuePair "#aws-glue-api-schema-registry-api-MetadataKeyValuePair") objects.

Search key-value pairs for metadata, if they are not provided all the metadata
information will be fetched.

- `MaxResults` – Number (integer), not less than 1 or more than 50.

Maximum number of results required per page. If the value is not supplied,
this will be defaulted to 25 per page.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation call.

###### Response

- `MetadataInfoMap` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

Each value is a A [MetadataInfo](#aws-glue-api-schema-registry-api-MetadataInfo "#aws-glue-api-schema-registry-api-MetadataInfo") object.

A map of a metadata key and associated values.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique version ID of the schema version.

- `NextToken` – UTF-8 string.

A continuation token for paginating the returned list of tokens, returned
if the current segment of the list is not the last.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `ThrottlingException`
- `EntityNotFoundException`

## RemoveSchemaVersionMetadata action (Python: remove_schema_version_metadata)

Removes a key value pair from the schema version metadata for the specified
schema version ID.

###### Request

- `SchemaId` – A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

A wrapper structure that may contain the schema name and Amazon Resource
Name (ARN).

- `SchemaVersionNumber` – A [SchemaVersionNumber](#aws-glue-api-schema-registry-api-SchemaVersionNumber "#aws-glue-api-schema-registry-api-SchemaVersionNumber") object.

The version number of the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The unique version ID of the schema version.

- `MetadataKeyValue` – _Required:_ A [MetadataKeyValuePair](#aws-glue-api-schema-registry-api-MetadataKeyValuePair "#aws-glue-api-schema-registry-api-MetadataKeyValuePair") object.

The value of the metadata key.

###### Response

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema.

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry.

- `LatestVersion` – Boolean.

The latest version of the schema.

- `VersionNumber` – Number (long), not less than 1 or more than 100000.

The version number of the schema.

- `SchemaVersionId` – UTF-8 string, not less than 36 or more than 36 bytes long, matching the [Custom string pattern #45](aws-glue-api-common.md#regex_45 "aws-glue-api-common.md#regex_45").

The version ID for the schema version.

- `MetadataKey` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

The metadata key.

- `MetadataValue` – UTF-8 string, not less than 1 or more than 256 bytes long, matching the [Custom string pattern #14](aws-glue-api-common.md#regex_14 "aws-glue-api-common.md#regex_14").

The value of the metadata key.

###### Errors

- `InvalidInputException`
- `AccessDeniedException`
- `ThrottlingException`
- `EntityNotFoundException`

## DeleteRegistry action (Python: delete_registry)

Delete the entire registry including schema and all of its versions. To
get the status of the delete operation, you can call the `GetRegistry`
API after the asynchronous call. Deleting a registry will deactivate all online
operations for the registry such as the `UpdateRegistry`, `CreateSchema`,
`UpdateSchema`, and `RegisterSchemaVersion` APIs.

###### Request

- `RegistryId` – _Required:_ A [RegistryId](#aws-glue-api-schema-registry-api-RegistryId "#aws-glue-api-schema-registry-api-RegistryId") object.

This is a wrapper structure that may contain the registry name and Amazon
Resource Name (ARN).

###### Response

- `RegistryName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the registry being deleted.

- `RegistryArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the registry being deleted.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `DELETING`).

The status of the registry. A successful operation will return the `Deleting`
status.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `AccessDeniedException`
- `ThrottlingException`
- `ConcurrentModificationException`

## DeleteSchema action (Python: delete_schema)

Deletes the entire schema set, including the schema set and all of its versions.
To get the status of the delete operation, you can call `GetSchema`
API after the asynchronous call. Deleting a registry will deactivate all online
operations for the schema, such as the `GetSchemaByDefinition`,
and `RegisterSchemaVersion` APIs.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure that may contain the schema name and Amazon
Resource Name (ARN).

###### Response

- `SchemaArn` – UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the schema being deleted.

- `SchemaName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Custom string pattern #46](aws-glue-api-common.md#regex_46 "aws-glue-api-common.md#regex_46").

The name of the schema being deleted.

- `Status` – UTF-8 string (valid values: `AVAILABLE` | `PENDING` | `DELETING`).

The status of the schema.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `AccessDeniedException`
- `ThrottlingException`
- `ConcurrentModificationException`

## DeleteSchemaVersions action (Python: delete_schema_versions)

Remove versions from the specified schema. A version number or range may
be supplied. If the compatibility mode forbids deleting of a version that is necessary,
such as BACKWARDS_FULL, an error is returned. Calling the `GetSchemaVersions`
API after this call will list the status of the deleted versions.

When the range of version numbers contain check pointed version, the API
will return a 409 conflict and will not proceed with the deletion. You have to remove
the checkpoint first using the `DeleteSchemaCheckpoint` API before
using this API.

You cannot use the `DeleteSchemaVersions` API to delete
the first schema version in the schema set. The first schema version can only be
deleted by the `DeleteSchema` API. This operation will also delete
the attached `SchemaVersionMetadata` under the schema versions.
Hard deletes will be enforced on the database.

If the compatibility mode forbids deleting of a version that is necessary,
such as BACKWARDS_FULL, an error is returned.

###### Request

- `SchemaId` – _Required:_ A [SchemaId](#aws-glue-api-schema-registry-api-SchemaId "#aws-glue-api-schema-registry-api-SchemaId") object.

This is a wrapper structure that may contain the schema name and Amazon
Resource Name (ARN).

- `Versions` – _Required:_ UTF-8 string, not less than 1 or more than 100000 bytes long, matching the [Custom string pattern #15](aws-glue-api-common.md#regex_15 "aws-glue-api-common.md#regex_15").

A version range may be supplied which may be of the format:

    + a single version number, 5
    + a range, 5-8 : deletes versions 5, 6, 7, 8

###### Response

- `SchemaVersionErrors` – An array of [SchemaVersionErrorItem](#aws-glue-api-schema-registry-api-SchemaVersionErrorItem "#aws-glue-api-schema-registry-api-SchemaVersionErrorItem") objects.

A list of `SchemaVersionErrorItem` objects, each containing
an error and schema version.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `AccessDeniedException`
- `ThrottlingException`
- `ConcurrentModificationException`
