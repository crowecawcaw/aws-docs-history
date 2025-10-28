# DatasetMatch

Checks if the data in the primary dataset matches the data in a reference dataset. The two datasets are joined using the provided
key column mappings. Additional column mappings can be provided should you wish to check for the equality of the data
in only those columns. Note that for **DataSetMatch** to work, your join keys should be unique and should not be
NULL (must be a primary key). If you don’t satisfy these conditions, you will get the error message,
“Provided key map not suitable for given data frames”. In cases where you can’t have joined keys that are unique, consider using other
ruletypes such as **AggregateMatch** to match on summary data.

**Syntax**

```
DatasetMatch `<REFERENCE_DATASET_ALIAS>` `<JOIN CONDITION WITH MAPPING>` `<OPTIONAL_MATCH_COLUMN_MAPPINGS>` `<EXPRESSION>`
```

- **REFERENCE_DATASET_ALIAS** – The alias of the reference dataset with which you compare data from the primary dataset.
- **KEY_COLUMN_MAPPINGS** – A comma-separated list of column names that form a key in the datasets. If the column names are not the same in both datasets, you must separated them with a `->`
- **OPTIONAL_MATCH_COLUMN_MAPPINGS** – You can supply this parameter if you want to check for matching data only in certain columns. It uses the same syntax as the key column mappings. If this parameter is not provided, we will match the data in all remaining columns. The remaining, non-key columns must have the same names in both datasets.
- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Match set datasets using ID column**

The following example rule checks that more than 90% of the primary dataset matches the reference dataset, using the "ID" column to join the two datasets. It compares all columns in this case.

```
DatasetMatch "reference" "ID" >= 0.9
```

**Example: Match set datasets using multiple key columns**

In the following example, the primary dataset and the reference dataset have different names for the key columns.
`ID_1` and `ID_2` together form a composite key in the primary dataset.
`ID_ref1` and `ID_ref2` together forms a composite key in the reference dataset.
In this scenario, you can use the special syntax to supply the column names.

```
DatasetMatch "reference" "ID_1->ID_ref1,ID_ref2->ID_ref2" >= 0.9
```

**Example: Match set datasets using multiple key columns and check that specific column matches**

This example builds on the previous example. We want to check that only the column containing the amounts match. This column is named `Amount1` in the primary dataset and `Amount2` in the reference dataset. You want an exact match.

```
DatasetMatch "reference" "ID_1->ID_ref1,ID_2->ID_ref2" "Amount1->Amount2" >= 0.9
```
