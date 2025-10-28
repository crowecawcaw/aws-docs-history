# ReferentialIntegrity

Checks to what extent the values of a set of columns in the primary dataset are a subset of the values of a set of columns in a reference dataset.

**Syntax**

```
ReferentialIntegrity `<PRIMARY_COLS>` `<REFERENCE_DATASET_COLS>` `<EXPRESSION>`
```

- **PRIMARY_COLS** – A comma-separated list of column names in the primary dataset.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **REFERENCE_DATASET_COLS** – This parameter contains two parts separated by a period. The first part is the alias of the reference dataset. The second part is the comma-separated list of column names in the reference dataset enclosed in braces.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Check the referential integrity of a zip code column**

The following example rule checks that more than 90% of the values in the `zipcode` column in the primary dataset, are present in the `zipcode` column in the `reference` dataset.

```
ReferentialIntegrity "zipcode" "reference.zipcode" >= 0.9
```

**Example: Check the referential integrity of the city and state columns**

In the following example, columns containing city and state information exist in the primary dataset and the reference dataset. The names of the columns are different in both datasets. The rule checks if the set of values of the columns in the primary dataset is exactly equal to the set of values of the columns in the reference dataset.

```
ReferentialIntegrity "city,state" "reference.{ref_city,ref_state}" = 1.0
```

**Sample dynamic rules**

- `ReferentialIntegrity "city,state" "reference.{ref_city,ref_state}" > avg(last(10))`
- `ReferentialIntegrity "city,state" "reference.{ref_city,ref_state}" between min(last(10)) - 1 and max(last(10)) + 1`
