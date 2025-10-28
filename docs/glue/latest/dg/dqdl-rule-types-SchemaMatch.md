# SchemaMatch

Checks if the schema of the primary dataset matches the schema of a reference dataset. The schema check is done column by column. The schema of two columns match if the names are identical and the types are identical. The order of the columns does not matter.

**Syntax**

```
SchemaMatch `<REFERENCE_DATASET_ALIAS>` `<EXPRESSION>`
```

- **REFERENCE_DATASET_ALIAS** – The alias of the reference dataset against which to compare schemas.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: SchemaMatch**

The following example rule checks whether the schema of the primary dataset exactly matches the schema of a reference dataset.

```
SchemaMatch "reference" = 1.0
```
