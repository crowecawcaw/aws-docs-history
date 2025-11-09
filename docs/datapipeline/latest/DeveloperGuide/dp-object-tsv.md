AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# TSV Data Format

A comma-delimited data format where the column separator is a tab character and
the record separator is a newline character.

## Example

The following is an example of this object type.

```
{
  "id" : "MyOutputDataType",
  "type" : "TSV",
  "column" : [
    "Name STRING",
    "Score INT",
    "DateOfBirth TIMESTAMP"
  ]
}
```

## Syntax

| Optional Fields | Description                                                                                                                                                                                                                                                        | Slot Type                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| column          | Column name and data type for the data described by this data node. For example `"Name<br>STRING"` denotes a column named `Name` with fields of<br>data type `STRING`. Separate multiple column name and data type<br>pairs with commas (as shown in the example). | String                                                           |
| columnSeparator | The character that separates fields in one column from fields in the next column. Defaults to '\t'.                                                                                                                                                                | String                                                           |
| escapeChar      | A character, for example "\", that instructs the parser to ignore the next character.                                                                                                                                                                              | String                                                           |
| parent          | Parent of the current object from which slots are inherited.                                                                                                                                                                                                       | Reference Object, for example, "parent":{"ref":"myBaseObjectId"} |
| recordSeparator | The character that separates records. Defaults to '\n'.                                                                                                                                                                                                            | String                                                           |

| Runtime Fields | Description                                        | Slot Type |
| -------------- | -------------------------------------------------- | --------- |
| @version       | Pipeline version that the object was created with. | String    |

| System Fields | Description                                                                                                                                    | Slot Type |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| @error        | Error describing the ill-formed object.                                                                                                        | String    |
| @pipelineId   | ID of the pipeline to which this object belongs.                                                                                               | String    |
| @sphere       | The sphere of an object denotes its place in the lifecycle: Component Objects give rise to<br>Instance Objects, which execute Attempt Objects. | String    |
