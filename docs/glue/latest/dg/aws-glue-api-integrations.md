# Integration APIs in AWS Glue

## Data types

- [Integration structure](#aws-glue-api-integrations-Integration "#aws-glue-api-integrations-Integration")
- [IntegrationConfig structure](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig")
- [IntegrationPartition structure](#aws-glue-api-integrations-IntegrationPartition "#aws-glue-api-integrations-IntegrationPartition")
- [IntegrationError structure](#aws-glue-api-integrations-IntegrationError "#aws-glue-api-integrations-IntegrationError")
- [IntegrationFilter structure](#aws-glue-api-integrations-IntegrationFilter "#aws-glue-api-integrations-IntegrationFilter")
- [InboundIntegration structure](#aws-glue-api-integrations-InboundIntegration "#aws-glue-api-integrations-InboundIntegration")
- [SourceProcessingProperties structure](#aws-glue-api-integrations-SourceProcessingProperties "#aws-glue-api-integrations-SourceProcessingProperties")
- [TargetProcessingProperties structure](#aws-glue-api-integrations-TargetProcessingProperties "#aws-glue-api-integrations-TargetProcessingProperties")
- [SourceTableConfig structure](#aws-glue-api-integrations-SourceTableConfig "#aws-glue-api-integrations-SourceTableConfig")
- [TargetTableConfig structure](#aws-glue-api-integrations-TargetTableConfig "#aws-glue-api-integrations-TargetTableConfig")

## Integration structure

Describes a zero-ETL integration.

###### Fields

- `SourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN for the source of the integration.

- `TargetArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN for the target of the integration.

- `Description` – UTF-8 string, not more than 1000 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12 "aws-glue-api-common.md#regex_12").

A description for the integration.

- `IntegrationName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

A unique name for the integration.

- `IntegrationArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the integration.

- `KmsKeyId` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of a KMS key used for encrypting the channel.

- `AdditionalEncryptionContext` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

An optional set of non-secret key–value pairs that contains additional
contextual information for encryption. This can only be provided if `KMSKeyId`
is provided.

- `Tags` – An array of [Tag](aws-glue-api-common.md#aws-glue-api-common-Tag "aws-glue-api-common.md#aws-glue-api-common-Tag") objects.

Metadata assigned to the resource consisting of a list of key-value pairs.

- `Status` – _Required:_ UTF-8 string (valid values: `CREATING` | `ACTIVE` | `MODIFYING` | `FAILED` | `DELETING` | `SYNCING` | `NEEDS_ATTENTION`).

The possible statuses are:

    + CREATING: The integration is being created.
    + ACTIVE: The integration creation succeeds.
    + MODIFYING: The integration is being modified.
    + FAILED: The integration creation fails.
    + DELETING: The integration is deleted.
    + SYNCING: The integration is synchronizing.
    + NEEDS\_ATTENTION: The integration needs attention, such as synchronization.

- `CreateTime` – _Required:_ Timestamp.

The time that the integration was created, in UTC.

- `IntegrationConfig` – An [IntegrationConfig](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig") object.

Properties associated with the integration.

- `Errors` – An array of [IntegrationError](#aws-glue-api-integrations-IntegrationError "#aws-glue-api-integrations-IntegrationError") objects.

A list of errors associated with the integration.

- `DataFilter` – UTF-8 string, not less than 1 or more than 2048 bytes long.

Selects source tables for the integration using Maxwell filter syntax.

## IntegrationConfig structure

Properties associated with the integration.

###### Fields

- `RefreshInterval` – UTF-8 string, not less than 1 or more than 128 bytes long.

Specifies the frequency at which CDC (Change Data Capture) pulls or incremental
loads should occur. This parameter provides flexibility to align the refresh
rate with your specific data update patterns, system load considerations, and
performance optimization goals. Time increment can be set from 15 minutes to
8640 minutes (six days).

- `SourceProperties` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

A collection of key-value pairs that specify additional properties for
the integration source. These properties provide configuration options that
can be used to customize the behavior of the ODB source during data integration
operations.

- `ContinuousSync` – Boolean.

Enables continuous synchronization for on-demand data extractions
from SaaS applications to AWS data services like Amazon Redshift
and Amazon S3.

## IntegrationPartition structure

A structure that describes how data is partitioned on the target.

###### Fields

- `FieldName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The field name used to partition data on the target. Avoid using columns
that have unique values for each row (for example, 'LastModifiedTimestamp',
'SystemModTimeStamp') as the partition column. These columns are not suitable
for partitioning because they create a large number of small partitions, which
can lead to performance issues.

- `FunctionSpec` – UTF-8 string, not less than 1 or more than 128 bytes long.

Specifies the function used to partition data on the target. The accepted
values for this parameter are:

    + `identity` - Uses source values directly without transformation
    + `year` - Extracts the year from timestamp values (e.g., 2023)
    + `month` - Extracts the month from timestamp values (e.g.,
     2023-01)
    + `day` - Extracts the day from timestamp values (e.g., 2023-01-15)
    + `hour` - Extracts the hour from timestamp values (e.g., 2023-01-15-14)

- `ConversionSpec` – UTF-8 string, not less than 1 or more than 128 bytes long.

Specifies the timestamp format of the source data. Valid values are:

    + `epoch_sec` - Unix epoch timestamp in seconds
    + `epoch_milli` - Unix epoch timestamp in milliseconds
    + `iso` - ISO 8601 formatted timestamp

###### Note

Only specify `ConversionSpec` when using timestamp-based
partition functions (year, month, day, or hour). AWS Glue Zero-ETL
uses this parameter to correctly transform source data into timestamp format
before partitioning.

Do not use high-cardinality columns with the `identity`
partition function. High-cardinality columns include:

    + Primary keys
    + Timestamp fields (such as `LastModifiedTimestamp`, `CreatedDate`)
    + System-generated timestamps Using high-cardinality columns with identity partitioning creates

many small partitions, which can significantly degrade ingestion performance.

## IntegrationError structure

An error associated with a zero-ETL integration.

###### Fields

- `ErrorCode` – UTF-8 string, not less than 1 or more than 128 bytes long.

The code associated with this error.

- `ErrorMessage` – UTF-8 string, not less than 1 or more than 2048 bytes long.

A message describing the error.

## IntegrationFilter structure

A filter that can be used when invoking a `DescribeIntegrations`
request.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the filter.

- `Values` – An array of UTF-8 strings.

A list of filter values.

## InboundIntegration structure

A structure for an integration that writes data into a resource.

###### Fields

- `SourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the source resource for the integration.

- `TargetArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the target resource for the integration.

- `IntegrationArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the zero-ETL integration.

- `Status` – _Required:_ UTF-8 string (valid values: `CREATING` | `ACTIVE` | `MODIFYING` | `FAILED` | `DELETING` | `SYNCING` | `NEEDS_ATTENTION`).

The possible statuses are:

    + CREATING: The integration is being created.
    + ACTIVE: The integration creation succeeds.
    + MODIFYING: The integration is being modified.
    + FAILED: The integration creation fails.
    + DELETING: The integration is deleted.
    + SYNCING: The integration is synchronizing.
    + NEEDS\_ATTENTION: The integration needs attention, such as synchronization.

- `CreateTime` – _Required:_ Timestamp.

The time that the integration was created, in UTC.

- `IntegrationConfig` – An [IntegrationConfig](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig") object.

Properties associated with the integration.

- `Errors` – An array of [IntegrationError](#aws-glue-api-integrations-IntegrationError "#aws-glue-api-integrations-IntegrationError") objects.

A list of errors associated with the integration.

## SourceProcessingProperties structure

The resource properties associated with the integration source.

###### Fields

- `RoleArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The IAM role to access the AWS Glue connection.

## TargetProcessingProperties structure

The resource properties associated with the integration target.

###### Fields

- `RoleArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The IAM role to access the AWS Glue database.

- `KmsArn` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of the KMS key used for encryption.

- `ConnectionName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The AWS Glue network connection to configure the AWS Glue job running in the customer VPC.

- `EventBusArn` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of an Eventbridge event bus to receive the integration status notification.

## SourceTableConfig structure

Properties used by the source leg to process data from the source.

###### Fields

- `Fields` – An array of UTF-8 strings.

A list of fields used for column-level filtering. Currently unsupported.

- `FilterPredicate` – UTF-8 string, not less than 1 or more than 128 bytes long.

A condition clause used for row-level filtering. Currently unsupported.

- `PrimaryKey` – An array of UTF-8 strings.

Provide the primary key set for this table. Currently supported specifically
for SAP `EntityOf` entities upon request. Contact AWS Support to make this feature available.

- `RecordUpdateField` – UTF-8 string, not less than 1 or more than 128 bytes long.

Incremental pull timestamp-based field. Currently unsupported.

## TargetTableConfig structure

Properties used by the target leg to partition the data on the target.

###### Fields

- `UnnestSpec` – UTF-8 string (valid values: `TOPLEVEL` | `FULL` | `NOUNNEST`).

Specifies how nested objects are flattened to top-level elements. Valid
values are: "TOPLEVEL", "FULL", or "NOUNNEST".

- `PartitionSpec` – An array of [IntegrationPartition](#aws-glue-api-integrations-IntegrationPartition "#aws-glue-api-integrations-IntegrationPartition") objects.

Determines the file layout on the target.

- `TargetTableName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The optional name of a target table.

## Operations

- [CreateIntegration action (Python: create_integration)](#aws-glue-api-integrations-CreateIntegration "#aws-glue-api-integrations-CreateIntegration")
- [ModifyIntegration action (Python: modify_integration)](#aws-glue-api-integrations-ModifyIntegration "#aws-glue-api-integrations-ModifyIntegration")
- [DescribeIntegrations action (Python: describe_integrations)](#aws-glue-api-integrations-DescribeIntegrations "#aws-glue-api-integrations-DescribeIntegrations")
- [DeleteIntegration action (Python: delete_integration)](#aws-glue-api-integrations-DeleteIntegration "#aws-glue-api-integrations-DeleteIntegration")
- [DescribeInboundIntegrations action (Python: describe_inbound_integrations)](#aws-glue-api-integrations-DescribeInboundIntegrations "#aws-glue-api-integrations-DescribeInboundIntegrations")
- [CreateIntegrationTableProperties action (Python: create_integration_table_properties)](#aws-glue-api-integrations-CreateIntegrationTableProperties "#aws-glue-api-integrations-CreateIntegrationTableProperties")
- [UpdateIntegrationTableProperties action (Python: update_integration_table_properties)](#aws-glue-api-integrations-UpdateIntegrationTableProperties "#aws-glue-api-integrations-UpdateIntegrationTableProperties")
- [GetIntegrationTableProperties action (Python: get_integration_table_properties)](#aws-glue-api-integrations-GetIntegrationTableProperties "#aws-glue-api-integrations-GetIntegrationTableProperties")
- [DeleteIntegrationTableProperties action (Python: delete_integration_table_properties)](#aws-glue-api-integrations-DeleteIntegrationTableProperties "#aws-glue-api-integrations-DeleteIntegrationTableProperties")
- [CreateIntegrationResourceProperty action (Python: create_integration_resource_property)](#aws-glue-api-integrations-CreateIntegrationResourceProperty "#aws-glue-api-integrations-CreateIntegrationResourceProperty")
- [UpdateIntegrationResourceProperty action (Python: update_integration_resource_property)](#aws-glue-api-integrations-UpdateIntegrationResourceProperty "#aws-glue-api-integrations-UpdateIntegrationResourceProperty")
- [GetIntegrationResourceProperty action (Python: get_integration_resource_property)](#aws-glue-api-integrations-GetIntegrationResourceProperty "#aws-glue-api-integrations-GetIntegrationResourceProperty")
- [UntagResource action (Python: untag_resource)](#aws-glue-api-integrations-UntagResource "#aws-glue-api-integrations-UntagResource")
- [ListTagsForResource action (Python: list_tags_for_resource)](#aws-glue-api-integrations-ListTagsForResource "#aws-glue-api-integrations-ListTagsForResource")

## CreateIntegration action (Python: create_integration)

Creates a Zero-ETL integration in the caller's account between two resources
with Amazon Resource Names (ARNs): the `SourceArn` and `TargetArn`.

###### Request

- `IntegrationName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

A unique name for an integration in AWS Glue.

- `SourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the source resource for the integration.

- `TargetArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the target resource for the integration.

- `Description` – UTF-8 string, not more than 1000 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12 "aws-glue-api-common.md#regex_12").

A description of the integration.

- `DataFilter` – UTF-8 string, not less than 1 or more than 2048 bytes long.

Selects source tables for the integration using Maxwell filter syntax.

- `KmsKeyId` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of a KMS key used for encrypting the channel.

- `AdditionalEncryptionContext` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

An optional set of non-secret key–value pairs that contains additional
contextual information for encryption. This can only be provided if `KMSKeyId`
is provided.

- `Tags` – An array of [Tag](aws-glue-api-common.md#aws-glue-api-common-Tag "aws-glue-api-common.md#aws-glue-api-common-Tag") objects.

Metadata assigned to the resource consisting of a list of key-value pairs.

- `IntegrationConfig` – An [IntegrationConfig](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig") object.

The configuration settings.

###### Response

- `SourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the source resource for the integration.

- `TargetArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the target resource for the integration.

- `IntegrationName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

A unique name for an integration in AWS Glue.

- `Description` – UTF-8 string, not more than 1000 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12 "aws-glue-api-common.md#regex_12").

A description of the integration.

- `IntegrationArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the created integration.

- `KmsKeyId` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of a KMS key used for encrypting the channel.

- `AdditionalEncryptionContext` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

An optional set of non-secret key–value pairs that contains additional
contextual information for encryption.

- `Tags` – An array of [Tag](aws-glue-api-common.md#aws-glue-api-common-Tag "aws-glue-api-common.md#aws-glue-api-common-Tag") objects.

Metadata assigned to the resource consisting of a list of key-value pairs.

- `Status` – _Required:_ UTF-8 string (valid values: `CREATING` | `ACTIVE` | `MODIFYING` | `FAILED` | `DELETING` | `SYNCING` | `NEEDS_ATTENTION`).

The status of the integration being created.

The possible statuses are:

    + CREATING: The integration is being created.
    + ACTIVE: The integration creation succeeds.
    + MODIFYING: The integration is being modified.
    + FAILED: The integration creation fails.
    + DELETING: The integration is deleted.
    + SYNCING: The integration is synchronizing.
    + NEEDS\_ATTENTION: The integration needs attention, such as synchronization.

- `CreateTime` – _Required:_ Timestamp.

The time when the integration was created, in UTC.

- `Errors` – An array of [IntegrationError](#aws-glue-api-integrations-IntegrationError "#aws-glue-api-integrations-IntegrationError") objects.

A list of errors associated with the integration creation.

- `DataFilter` – UTF-8 string, not less than 1 or more than 2048 bytes long.

Selects source tables for the integration using Maxwell filter syntax.

- `IntegrationConfig` – An [IntegrationConfig](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig") object.

The configuration settings.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `ResourceNotFoundException`
- `InternalServerException`
- `IntegrationConflictOperationFault`
- `IntegrationQuotaExceededFault`
- `KMSKeyNotAccessibleFault`
- `EntityNotFoundException`
- `InternalServiceException`
- `ConflictException`
- `ResourceNumberLimitExceededException`
- `InvalidInputException`

## ModifyIntegration action (Python: modify_integration)

Modifies a Zero-ETL integration in the caller's account.

###### Request

- `IntegrationIdentifier` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the integration.

- `Description` – UTF-8 string, not more than 1000 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12 "aws-glue-api-common.md#regex_12").

A description of the integration.

- `DataFilter` – UTF-8 string, not less than 1 or more than 2048 bytes long.

Selects source tables for the integration using Maxwell filter syntax.

- `IntegrationConfig` – An [IntegrationConfig](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig") object.

The configuration settings for the integration. Currently, only the
RefreshInterval can be modified.

- `IntegrationName` – UTF-8 string, not less than 1 or more than 128 bytes long.

A unique name for an integration in AWS Glue.

###### Response

- `SourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the source for the integration.

- `TargetArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the target for the integration.

- `IntegrationName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

A unique name for an integration in AWS Glue.

- `Description` – UTF-8 string, not more than 1000 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12 "aws-glue-api-common.md#regex_12").

A description of the integration.

- `IntegrationArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the integration.

- `KmsKeyId` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of a KMS key used for encrypting the channel.

- `AdditionalEncryptionContext` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

An optional set of non-secret key–value pairs that contains additional
contextual information for encryption.

- `Tags` – An array of [Tag](aws-glue-api-common.md#aws-glue-api-common-Tag "aws-glue-api-common.md#aws-glue-api-common-Tag") objects.

Metadata assigned to the resource consisting of a list of key-value pairs.

- `Status` – _Required:_ UTF-8 string (valid values: `CREATING` | `ACTIVE` | `MODIFYING` | `FAILED` | `DELETING` | `SYNCING` | `NEEDS_ATTENTION`).

The status of the integration being modified.

The possible statuses are:

    + CREATING: The integration is being created.
    + ACTIVE: The integration creation succeeds.
    + MODIFYING: The integration is being modified.
    + FAILED: The integration creation fails.
    + DELETING: The integration is deleted.
    + SYNCING: The integration is synchronizing.
    + NEEDS\_ATTENTION: The integration needs attention, such as synchronization.

- `CreateTime` – _Required:_ Timestamp.

The time when the integration was created, in UTC.

- `Errors` – An array of [IntegrationError](#aws-glue-api-integrations-IntegrationError "#aws-glue-api-integrations-IntegrationError") objects.

A list of errors associated with the integration modification.

- `DataFilter` – UTF-8 string, not less than 1 or more than 2048 bytes long.

Selects source tables for the integration using Maxwell filter syntax.

- `IntegrationConfig` – An [IntegrationConfig](#aws-glue-api-integrations-IntegrationConfig "#aws-glue-api-integrations-IntegrationConfig") object.

The updated configuration settings for the integration.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `InternalServerException`
- `IntegrationNotFoundFault`
- `IntegrationConflictOperationFault`
- `InvalidIntegrationStateFault`
- `EntityNotFoundException`
- `InternalServiceException`
- `ConflictException`
- `InvalidStateException`
- `InvalidInputException`

## DescribeIntegrations action (Python: describe_integrations)

The API is used to retrieve a list of integrations.

###### Request

- `IntegrationIdentifier` – UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the integration.

- `Marker` – UTF-8 string, not less than 1 or more than 128 bytes long.

A value that indicates the starting point for the next set of response records
in a subsequent request.

- `MaxRecords` – Number (integer).

The total number of items to return in the output.

- `Filters` – An array of [IntegrationFilter](#aws-glue-api-integrations-IntegrationFilter "#aws-glue-api-integrations-IntegrationFilter") objects.

A list of key and values, to filter down the results. Supported keys are
"Status", "IntegrationName", and "SourceArn". IntegrationName is limited
to only one value.

###### Response

- `Integrations` – An array of [Integration](#aws-glue-api-integrations-Integration "#aws-glue-api-integrations-Integration") objects.

A list of zero-ETL integrations.

- `Marker` – UTF-8 string, not less than 1 or more than 128 bytes long.

A value that indicates the starting point for the next set of response records
in a subsequent request.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `InternalServerException`
- `IntegrationNotFoundFault`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## DeleteIntegration action (Python: delete_integration)

Deletes the specified Zero-ETL integration.

###### Request

- `IntegrationIdentifier` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the integration.

###### Response

- `SourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the source for the integration.

- `TargetArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The ARN of the target for the integration.

- `IntegrationName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

A unique name for an integration in AWS Glue.

- `Description` – UTF-8 string, not more than 1000 bytes long, matching the [Custom string pattern #12](aws-glue-api-common.md#regex_12 "aws-glue-api-common.md#regex_12").

A description of the integration.

- `IntegrationArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) for the integration.

- `KmsKeyId` – UTF-8 string, not less than 1 or more than 2048 bytes long.

The ARN of a KMS key used for encrypting the channel.

- `AdditionalEncryptionContext` – A map array of key-value pairs.

Each key is a UTF-8 string.

Each value is a UTF-8 string.

An optional set of non-secret key–value pairs that contains additional
contextual information for encryption.

- `Tags` – An array of [Tag](aws-glue-api-common.md#aws-glue-api-common-Tag "aws-glue-api-common.md#aws-glue-api-common-Tag") objects.

Metadata assigned to the resource consisting of a list of key-value pairs.

- `Status` – _Required:_ UTF-8 string (valid values: `CREATING` | `ACTIVE` | `MODIFYING` | `FAILED` | `DELETING` | `SYNCING` | `NEEDS_ATTENTION`).

The status of the integration being deleted.

The possible statuses are:

    + CREATING: The integration is being created.
    + ACTIVE: The integration creation succeeds.
    + MODIFYING: The integration is being modified.
    + FAILED: The integration creation fails.
    + DELETING: The integration is deleted.
    + SYNCING: The integration is synchronizing.
    + NEEDS\_ATTENTION: The integration needs attention, such as synchronization.

- `CreateTime` – _Required:_ Timestamp.

The time when the integration was created, in UTC.

- `Errors` – An array of [IntegrationError](#aws-glue-api-integrations-IntegrationError "#aws-glue-api-integrations-IntegrationError") objects.

A list of errors associated with the integration.

- `DataFilter` – UTF-8 string, not less than 1 or more than 2048 bytes long.

Selects source tables for the integration using Maxwell filter syntax.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `InternalServerException`
- `IntegrationNotFoundFault`
- `IntegrationConflictOperationFault`
- `InvalidIntegrationStateFault`
- `EntityNotFoundException`
- `InternalServiceException`
- `ConflictException`
- `InvalidStateException`
- `InvalidInputException`

## DescribeInboundIntegrations action (Python: describe_inbound_integrations)

Returns a list of inbound integrations for the specified integration.

###### Request

- `IntegrationArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) of the integration.

- `Marker` – UTF-8 string, not less than 1 or more than 128 bytes long.

A token to specify where to start paginating. This is the marker from a previously
truncated response.

- `MaxRecords` – Number (integer).

The total number of items to return in the output.

- `TargetArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) of the target resource in the integration.

###### Response

- `InboundIntegrations` – An array of [InboundIntegration](#aws-glue-api-integrations-InboundIntegration "#aws-glue-api-integrations-InboundIntegration") objects.

A list of inbound integrations.

- `Marker` – UTF-8 string, not less than 1 or more than 128 bytes long.

A value that indicates the starting point for the next set of response records
in a subsequent request.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `InternalServerException`
- `IntegrationNotFoundFault`
- `TargetResourceNotFound`
- `OperationNotSupportedException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## CreateIntegrationTableProperties action (Python: create_integration_table_properties)

This API is used to provide optional override properties for the the tables
that need to be replicated. These properties can include properties for filtering
and partitioning for the source and target tables. To set both source and target
properties the same API need to be invoked with the AWS Glue connection
ARN as `ResourceArn` with `SourceTableConfig`, and
the AWS Glue database ARN as `ResourceArn` with `TargetTableConfig`
respectively.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) of the target table for which to create integration
table properties. Currently, this API only supports creating integration table
properties for target tables, and the provided ARN should be the ARN of the target
table in the AWS Glue Data Catalog. Support for creating integration
table properties for source connections (using the connection ARN) is not yet
implemented and will be added in a future release.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the table to be replicated.

- `SourceTableConfig` – A [SourceTableConfig](#aws-glue-api-integrations-SourceTableConfig "#aws-glue-api-integrations-SourceTableConfig") object.

A structure for the source table configuration. See the `SourceTableConfig`
structure to see list of supported source properties.

- `TargetTableConfig` – A [TargetTableConfig](#aws-glue-api-integrations-TargetTableConfig "#aws-glue-api-integrations-TargetTableConfig") object.

A structure for the target table configuration.

###### Response

- _No Response parameters._

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `ResourceNotFoundException`
- `InternalServerException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## UpdateIntegrationTableProperties action (Python: update_integration_table_properties)

This API is used to provide optional override properties for the tables
that need to be replicated. These properties can include properties for filtering
and partitioning for the source and target tables. To set both source and target
properties the same API need to be invoked with the AWS Glue connection
ARN as `ResourceArn` with `SourceTableConfig`, and
the AWS Glue database ARN as `ResourceArn` with `TargetTableConfig`
respectively.

The override will be reflected across all the integrations using same
`ResourceArn` and source table.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the table to be replicated.

- `SourceTableConfig` – A [SourceTableConfig](#aws-glue-api-integrations-SourceTableConfig "#aws-glue-api-integrations-SourceTableConfig") object.

A structure for the source table configuration.

- `TargetTableConfig` – A [TargetTableConfig](#aws-glue-api-integrations-TargetTableConfig "#aws-glue-api-integrations-TargetTableConfig") object.

A structure for the target table configuration.

###### Response

- _No Response parameters._

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `ResourceNotFoundException`
- `InternalServerException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## GetIntegrationTableProperties action (Python: get_integration_table_properties)

This API is used to retrieve optional override properties for the tables
that need to be replicated. These properties can include properties for filtering
and partition for source and target tables.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) of the target table for which to retrieve
integration table properties. Currently, this API only supports retrieving
properties for target tables, and the provided ARN should be the ARN of the target
table in the AWS Glue Data Catalog. Support for retrieving integration
table properties for source connections (using the connection ARN) is not yet
implemented and will be added in a future release.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the table to be replicated.

###### Response

- `ResourceArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The Amazon Resource Name (ARN) of the target table for which to retrieve
integration table properties. Currently, this API only supports retrieving
properties for target tables, and the provided ARN should be the ARN of the target
table in the AWS Glue Data Catalog. Support for retrieving integration
table properties for source connections (using the connection ARN) is not yet
implemented and will be added in a future release.

- `TableName` – UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the table to be replicated.

- `SourceTableConfig` – A [SourceTableConfig](#aws-glue-api-integrations-SourceTableConfig "#aws-glue-api-integrations-SourceTableConfig") object.

A structure for the source table configuration.

- `TargetTableConfig` – A [TargetTableConfig](#aws-glue-api-integrations-TargetTableConfig "#aws-glue-api-integrations-TargetTableConfig") object.

A structure for the target table configuration.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `ResourceNotFoundException`
- `InternalServerException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## DeleteIntegrationTableProperties action (Python: delete_integration_table_properties)

Deletes the table properties that have been created for the tables that
need to be replicated.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `TableName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The name of the table to be replicated.

###### Response

- _No Response parameters._

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `ResourceNotFoundException`
- `InternalServerException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## CreateIntegrationResourceProperty action (Python: create_integration_resource_property)

This API can be used for setting up the `ResourceProperty`
of the AWS Glue connection (for the source) or AWS Glue
database ARN (for the target). These properties can include the role to access
the connection or database. To set both source and target properties the same
API needs to be invoked with the AWS Glue connection ARN as `ResourceArn`
with `SourceProcessingProperties` and the AWS Glue
database ARN as `ResourceArn` with `TargetProcessingProperties`
respectively.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `SourceProcessingProperties` – A [SourceProcessingProperties](#aws-glue-api-integrations-SourceProcessingProperties "#aws-glue-api-integrations-SourceProcessingProperties") object.

The resource properties associated with the integration source.

- `TargetProcessingProperties` – A [TargetProcessingProperties](#aws-glue-api-integrations-TargetProcessingProperties "#aws-glue-api-integrations-TargetProcessingProperties") object.

The resource properties associated with the integration target.

###### Response

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `SourceProcessingProperties` – A [SourceProcessingProperties](#aws-glue-api-integrations-SourceProcessingProperties "#aws-glue-api-integrations-SourceProcessingProperties") object.

The resource properties associated with the integration source.

- `TargetProcessingProperties` – A [TargetProcessingProperties](#aws-glue-api-integrations-TargetProcessingProperties "#aws-glue-api-integrations-TargetProcessingProperties") object.

The resource properties associated with the integration target.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `ConflictException`
- `InternalServerException`
- `ResourceNotFoundException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## UpdateIntegrationResourceProperty action (Python: update_integration_resource_property)

This API can be used for updating the `ResourceProperty`
of the AWS Glue connection (for the source) or AWS Glue
database ARN (for the target). These properties can include the role to access
the connection or database. Since the same resource can be used across multiple
integrations, updating resource properties will impact all the integrations
using it.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `SourceProcessingProperties` – A [SourceProcessingProperties](#aws-glue-api-integrations-SourceProcessingProperties "#aws-glue-api-integrations-SourceProcessingProperties") object.

The resource properties associated with the integration source.

- `TargetProcessingProperties` – A [TargetProcessingProperties](#aws-glue-api-integrations-TargetProcessingProperties "#aws-glue-api-integrations-TargetProcessingProperties") object.

The resource properties associated with the integration target.

###### Response

- `ResourceArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `SourceProcessingProperties` – A [SourceProcessingProperties](#aws-glue-api-integrations-SourceProcessingProperties "#aws-glue-api-integrations-SourceProcessingProperties") object.

The resource properties associated with the integration source.

- `TargetProcessingProperties` – A [TargetProcessingProperties](#aws-glue-api-integrations-TargetProcessingProperties "#aws-glue-api-integrations-TargetProcessingProperties") object.

The resource properties associated with the integration target.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `InternalServerException`
- `ResourceNotFoundException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## GetIntegrationResourceProperty action (Python: get_integration_resource_property)

This API is used for fetching the `ResourceProperty` of the
AWS Glue connection (for the source) or AWS Glue database
ARN (for the target)

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

###### Response

- `ResourceArn` – UTF-8 string, not less than 1 or more than 128 bytes long.

The connection ARN of the source, or the database ARN of the target.

- `SourceProcessingProperties` – A [SourceProcessingProperties](#aws-glue-api-integrations-SourceProcessingProperties "#aws-glue-api-integrations-SourceProcessingProperties") object.

The resource properties associated with the integration source.

- `TargetProcessingProperties` – A [TargetProcessingProperties](#aws-glue-api-integrations-TargetProcessingProperties "#aws-glue-api-integrations-TargetProcessingProperties") object.

The resource properties associated with the integration target.

###### Errors

- `ValidationException`
- `AccessDeniedException`
- `InternalServerException`
- `ResourceNotFoundException`
- `EntityNotFoundException`
- `InternalServiceException`
- `InvalidInputException`

## UntagResource action (Python: untag_resource)

Removes the specified tags from an integration resource.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) for the integration resource.

- `TagsToRemove` – _Required:_ An array of UTF-8 strings, not more than 50 strings.

A list of metadata tags to be removed from the resource.

###### Response

- _No Response parameters._

###### Errors

- `ResourceNotFoundException`

## ListTagsForResource action (Python: list_tags_for_resource)

Lists the metadata tags assigned to the specified resource.

###### Request

- `ResourceARN` – _Required:_ UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The resource ARN for the resource.

###### Response

- `Tags` – An array of [Tag](aws-glue-api-common.md#aws-glue-api-common-Tag "aws-glue-api-common.md#aws-glue-api-common-Tag") objects, not more than 10 structures.

A list of tags.

###### Errors

- `ResourceNotFoundException`

## Exceptions

- [ResourceNotFoundException structure](#aws-glue-api-integrations-ResourceNotFoundException "#aws-glue-api-integrations-ResourceNotFoundException")
- [InternalServerException structure](#aws-glue-api-integrations-InternalServerException "#aws-glue-api-integrations-InternalServerException")
- [IntegrationAlreadyExistsFault structure](#aws-glue-api-integrations-IntegrationAlreadyExistsFault "#aws-glue-api-integrations-IntegrationAlreadyExistsFault")
- [IntegrationConflictOperationFault structure](#aws-glue-api-integrations-IntegrationConflictOperationFault "#aws-glue-api-integrations-IntegrationConflictOperationFault")
- [IntegrationQuotaExceededFault structure](#aws-glue-api-integrations-IntegrationQuotaExceededFault "#aws-glue-api-integrations-IntegrationQuotaExceededFault")
- [KMSKeyNotAccessibleFault structure](#aws-glue-api-integrations-KMSKeyNotAccessibleFault "#aws-glue-api-integrations-KMSKeyNotAccessibleFault")
- [IntegrationNotFoundFault structure](#aws-glue-api-integrations-IntegrationNotFoundFault "#aws-glue-api-integrations-IntegrationNotFoundFault")
- [TargetResourceNotFound structure](#aws-glue-api-integrations-TargetResourceNotFound "#aws-glue-api-integrations-TargetResourceNotFound")
- [InvalidIntegrationStateFault structure](#aws-glue-api-integrations-InvalidIntegrationStateFault "#aws-glue-api-integrations-InvalidIntegrationStateFault")

## ResourceNotFoundException structure

The resource could not be found.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## InternalServerException structure

An internal server error occurred.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## IntegrationAlreadyExistsFault structure

The specified integration already exists.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## IntegrationConflictOperationFault structure

The requested operation conflicts with another operation.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## IntegrationQuotaExceededFault structure

The data processed through your integration exceeded your quota.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## KMSKeyNotAccessibleFault structure

The KMS key specified is not accessible.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## IntegrationNotFoundFault structure

The specified integration could not be found.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## TargetResourceNotFound structure

The target resource could not be found.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.

## InvalidIntegrationStateFault structure

The integration is in an invalid state.

###### Fields

- `Message` – UTF-8 string.

A message describing the problem.
