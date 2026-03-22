# Legacy DynamoDB conditional parameters

This document provides an overview of legacy conditional parameters in DynamoDB and recommends
using the new expression parameters instead. It covers details on parameters like AttributesToGet,
AttributeUpdates, ConditionalOperator, Expected, KeyConditions, QueryFilter, and ScanFilter, and
provides examples of how to use the new expression parameters as replacements.

###### Important

We recommend that you use the new expression parameters instead of these legacy parameters whenever possible.
For more information, see [Using expressions in DynamoDB](Expressions.md "Expressions.md").

Additionally, DynamoDB does not allow mixing legacy conditional parameters and expression parameters in
a single call. For example, calling the `Query` operation with
`AttributesToGet` and `ConditionExpression` will result in an
error.

The following table shows the DynamoDB API operations that still support these legacy
parameters, and which expression parameter to use instead. This table can be helpful if you
are considering updating your applications so that they use expression parameters
instead.

| If you use this API operation... | With these legacy parameters... | Use this expression parameter instead |
| -------------------------------- | ------------------------------- | ------------------------------------- |
| `BatchGetItem`                   | `AttributesToGet`               | `ProjectionExpression`                |
| `DeleteItem`                     | `Expected`                      | `ConditionExpression`                 |
| `GetItem`                        | `AttributesToGet`               | `ProjectionExpression`                |
| `PutItem`                        | `Expected`                      | `ConditionExpression`                 |
| `Query`                          | `AttributesToGet`               | `ProjectionExpression`                |
| `KeyConditions`                  | `KeyConditionExpression`        |
| `QueryFilter`                    | `FilterExpression`              |
| `Scan`                           | `AttributesToGet`               | `ProjectionExpression`                |
| `ScanFilter`                     | `FilterExpression`              |
| `UpdateItem`                     | `AttributeUpdates`              | `UpdateExpression`                    |
| `Expected`                       | `ConditionExpression`           |

The following sections provide more information about legacy conditional
parameters.

###### Topics

- [AttributesToGet (legacy)](LegacyConditionalParameters.AttributesToGet.md "LegacyConditionalParameters.AttributesToGet.md")
- [AttributeUpdates (legacy)](LegacyConditionalParameters.AttributeUpdates.md "LegacyConditionalParameters.AttributeUpdates.md")
- [ConditionalOperator (legacy)](LegacyConditionalParameters.ConditionalOperator.md "LegacyConditionalParameters.ConditionalOperator.md")
- [Expected (legacy)](LegacyConditionalParameters.Expected.md "LegacyConditionalParameters.Expected.md")
- [KeyConditions (legacy)](LegacyConditionalParameters.KeyConditions.md "LegacyConditionalParameters.KeyConditions.md")
- [QueryFilter (legacy)](LegacyConditionalParameters.QueryFilter.md "LegacyConditionalParameters.QueryFilter.md")
- [ScanFilter (legacy)](LegacyConditionalParameters.ScanFilter.md "LegacyConditionalParameters.ScanFilter.md")
- [Writing conditions with legacy parameters](LegacyConditionalParameters.Conditions.md "LegacyConditionalParameters.Conditions.md")
