# Transform data with AWS Glue managed transforms

AWS Glue Studio provides two types of transforms:

- **AWS Glue-native transforms** - available to all users and are managed by AWS Glue.
- **Custom visual transforms** - allows you to upload your own transforms to use in AWS Glue Studio

## AWS Glue managed data transform nodes

AWS Glue Studio provides a set of built-in transforms that you can use to process your data. Your
data passes from one node in the job diagram to another in a data structure called a
`DynamicFrame`, which is an extension to an Apache Spark SQL
`DataFrame`.

In the pre-populated diagram for a job, between the data source and data target nodes is
the **Change Schema** transform node. You can configure this transform node
to modify your data, or you can use additional transforms.

The following built-in transforms are available with AWS Glue Studio:

- **[ChangeSchema](transforms-configure-applymapping.md "transforms-configure-applymapping.md")**: Map data property keys in the data source to data
  property keys in the data target. You can rename keys, modify the data types for keys, and
  choose which keys to drop from the dataset.
- **[SelectFields](transforms-configure-select-fields.md "transforms-configure-select-fields.md")**: Choose the data property keys that you want to
  keep.
- **[DropFields](transforms-configure-drop-fields.md "transforms-configure-drop-fields.md")**: Choose the data property keys that you want to
  drop.
- **[RenameField](transforms-configure-rename-field.md "transforms-configure-rename-field.md")**: Rename a single data property key.
- **[Spigot](transforms-configure-spigot.md "transforms-configure-spigot.md")**:
  Write samples of the data to an Amazon S3 bucket.
- **[Join](transforms-configure-join.md "transforms-configure-join.md")**: Join two
  datasets into one dataset using a comparison phrase on the specified data property keys.
  You can use inner, outer, left, right, left semi, and left anti joins.
- **[Union](transforms-configure-union.md "transforms-configure-union.md")**: Combine rows
  from more than one data source that have the same schema.
- **[SplitFields](transforms-configure-split-fields.md "transforms-configure-split-fields.md")**: Split data property keys into two
  `DynamicFrames`. Output is a collection of `DynamicFrames`: one
  with selected data property keys, and one with the remaining data property keys.
- **[SelectFromCollection](transforms-selectfromcollection-overview.md "transforms-selectfromcollection-overview.md")**: Choose one `DynamicFrame` from a
  collection of `DynamicFrames`. The output is the selected
  `DynamicFrame`.
- **[FillMissingValues](transforms-configure-fmv.md "transforms-configure-fmv.md")**: Locate records in the dataset that have missing
  values and add a new field with a suggested value that is determined by imputation
- **[Filter](transforms-filter.md "transforms-filter.md")**: Split a
  dataset into two, based on a filter condition.
- **[Drop Null Fields](transforms-dropnull-fields.md "transforms-dropnull-fields.md")**:
  Removes columns from the dataset if all values in the column are ‘null’.
- **[Drop Duplicates](transforms-drop-duplicates.md "transforms-drop-duplicates.md")**:
  Removes rows from your data source by choosing to match entire rows or specify keys.
- **[SQL](transforms-sql.md "transforms-sql.md")**: Enter SparkSQL code
  into a text entry field to use a SQL query to transform the data. The output is a single
  `DynamicFrame`.
- **[Aggregate](transforms-aggregate-fields.md "transforms-aggregate-fields.md")**:
  Performs a calculation (such as average, sum, min, max) on selected fields and rows, and
  creates a new field with the newly calculated value(s).
- **[Flatten](transforms-flatten.md "transforms-flatten.md")**:
  Extract fields inside structs into top level fields.
- **[UUID](transforms-uuid.md "transforms-uuid.md")**:
  Add a column with a Universally Unique Identifier for each row.
- **[Identifier](transforms-identifier.md "transforms-identifier.md")**:
  Add a column with a numeric identifier for each row.
- **[To timestamp](transforms-to-timestamp.md "transforms-to-timestamp.md")**:
  Convert a column to timestamp type.
- **[Format timestamp](transforms-format-timestamp.md "transforms-format-timestamp.md")**:
  Convert a timestamp column to a formatted string.
- **[Conditional Router transform](transforms-conditional-router.md "transforms-conditional-router.md")**:
  Apply multiple conditions to incoming data. Each row of the incoming data is evaluated by a group filter condition and
  processed into its corresponding group.
- **[Concatenate Columns transform](transforms-concatenate-columns.md "transforms-concatenate-columns.md")**:
  Build a new string column using the values of other columns with an optional spacer.
- **[Split String transform](transforms-split-string.md "transforms-split-string.md")**:
  Break up a string into an array of tokens using a regular expression to define how the split is done.
- **[Array To Columns transform](transforms-array-to-columns.md "transforms-array-to-columns.md")**:
  Extract some or all the elements of a column of type array into new columns.
- **[Add Current Timestamp transform](transforms-add-current-timestamp.md "transforms-add-current-timestamp.md")**:
  Mark the rows with the time on which the data was processed. This is useful for auditing purposes or to track latency in the
  data pipeline.
- **[Pivot Rows to Columns transform](transforms-pivot-rows-to-columns.md "transforms-pivot-rows-to-columns.md")**:
  Aggregate a numeric column by rotating unique values on selected columns which become new columns.
  If multiple columns are selected, the values are concatenated to name the new columns.
- **[Unpivot Columns To Rows transform](transforms-unpivot-columns-to-rows.md "transforms-unpivot-columns-to-rows.md")**:
  Convert columns into values of new columns generating a row for each unique value.
- **[Autobalance Processing transform](transforms-autobalance-processing.md "transforms-autobalance-processing.md")**:
  Redistribute the data better among the workers. This is useful where the data is unbalanced or as it comes from the source doesn’t
  allow enough parallel processing on it.
- **[Derived Column transform](transforms-derived-column.md "transforms-derived-column.md")**:
  Define a new column based on a math formula or SQL expression in which you can use other columns in the data, as well as constants and
  literals.
- **[Lookup transform](transforms-lookup.md "transforms-lookup.md")**:
  Add columns from a defined catalog table when the keys match the defined lookup columns in the data.
- **[Explode Array or Map Into Rows transform](transforms-explode-array.md "transforms-explode-array.md")**:
  Extract values from a nested structure into individual rows that are easier to manipulate.
- **[Record matching transform](transforms-record-matching.md "transforms-record-matching.md")**:
  Invoke an existing Record Matching machine learning data classification transform.
- **[Remove null rows transform](transforms-remove-null-rows.md "transforms-remove-null-rows.md")**:
  Remove from the dataset rows that have all columns as null, or empty.
- **[Parse JSON column transform](transforms-parse-json-column.md "transforms-parse-json-column.md")**:
  Parse a string column containing JSON data and convert it to a struct or an array column, depending if the JSON is an object or an array, respectively.
- **[Extract JSON path transform](transforms-extract-json-path.md "transforms-extract-json-path.md")**:
  Extract new columns from a JSON string column.
- **[Extract string fragments from a regular expression](transforms-regex-extractor.md "transforms-regex-extractor.md")**:
  Extract string fragments using a regular expression and create new column out of it, or multiple columns if using regex groups.
- **[Custom transform](transforms-custom.md "transforms-custom.md")**:
  Enter code into a text entry field to use custom transforms. The output is a collection of
  `DynamicFrames`.
