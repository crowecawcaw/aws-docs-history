Amazon Cloud Directory will no longer be open to new customers starting on November 7, 2025. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Arn Examples

The following examples are separated by ARN types and show how they can be constructed for
 each schema state (where applicable). A schema can exist in three states:


* *Development:* This is a mutable state of the schema. All new
 schemas are in the development state. Once the schema is finalized, it can be published. All
 development schemas are under the development sub root of the schema metadata
 container.
* *Published:* Published schemas are immutable and have a version
 associated with them. All published schemas are under the published sub root of the schema
 container.
* *Applied:* Applied schemas are mutable in a way that allows you to
 add new schema facets. However, existing schema facets cannot be changed. You can apply only
 published schemas to directories. You can't apply schemas at the node level, but only at the
 directory root level.

## Schema Arns




| State | Format or Example | Schema Arn |
| --- | --- | --- |
| Development | Format | `arn:aws:clouddirectory:us-west-2:`accountId`:schema/development/`SchemaName`` |
| Example | `arn:aws:clouddirectory:us-west-2:12345678910:schema/development/cognito` |
| Published | Format | `arn:aws:clouddirectory:us-west-2:`accountId`:`schema/published/`SchemaName``/`SchemaVersion`` |
| Example | `arn:aws:clouddirectory:us-west-2:12345678910:schema/published/cognito/1.0` | | Format | `arn:aws:clouddirectory:us-west-2:`accountId`:`schema/published/`SchemaName``/`SchemaVersion`/`SchemaMinorVersion`` |
| Example | `arn:aws:clouddirectory:us-west-2:12345678910:schema/published/cognito/1.0/XYZ` |
| Applied | Format | `arn:aws:clouddirectory:us-west-2:`accountId`:directory/`directoryId`/`SchemaName`/`SchemaVersion`` |
| Example | `arn:aws:clouddirectory:us-west-2:12345678910:directory/ARIqk1HD-UjdtmcIrJHEvPI/schema/cognito/1.0` | | Format | `arn:aws:clouddirectory:us-west-2:`accountId`:directory/`directoryId`/`SchemaName`/`SchemaVersion`/`SchemaMinorVersion`` |
| Example | `arn:aws:clouddirectory:us-west-2:12345678910:directory/ARIqk1HD-UjdtmcIrJHEvPI/schema/cognito/1.0/XYZ` | ## Directory Arns
| Arn Type | Format or example | Arn |
| --- | --- | --- |
| Directory Arn | Format | `arn:aws:clouddirectory:us-west-2:`Directory owner accountId`:directory/`directoryId`` |
| Example | `arn:aws:clouddirectory:us-west-2:12345678910:directory/ARIqk1HD-UjdtmcIrJHEvPI` |
