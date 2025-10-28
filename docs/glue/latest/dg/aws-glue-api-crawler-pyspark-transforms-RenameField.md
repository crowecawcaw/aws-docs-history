# RenameField class

Renames a node within a `DynamicFrame`.

## Example

We recommend that you use the [DynamicFrame.rename_field()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-rename_field "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-rename_field")
method to rename a field in a `DynamicFrame`. To view a code example, see [Example: Use rename_field to rename fields in a DynamicFrame](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-rename_field-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-rename_field-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-RenameField-__call__ "#aws-glue-api-crawler-pyspark-transforms-RenameField-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-RenameField-apply "#aws-glue-api-crawler-pyspark-transforms-RenameField-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-RenameField-name "#aws-glue-api-crawler-pyspark-transforms-RenameField-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-RenameField-describeArgs "#aws-glue-api-crawler-pyspark-transforms-RenameField-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-RenameField-describeReturn "#aws-glue-api-crawler-pyspark-transforms-RenameField-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-RenameField-describeTransform "#aws-glue-api-crawler-pyspark-transforms-RenameField-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-RenameField-describeErrors "#aws-glue-api-crawler-pyspark-transforms-RenameField-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-RenameField-describe "#aws-glue-api-crawler-pyspark-transforms-RenameField-describe")

## \_\_call\_\_(frame,

old_name, new_name, transformation_ctx = "", info = "", stageThreshold = 0, totalThreshold = 0)

Renames a node within a `DynamicFrame`.

- `frame` – The `DynamicFrame` in which to rename a node
  (required).
- `old_name` – The full path to the node to rename (required).

If the old name has dots in it, RenameField will not work unless you place backticks
around it (````). For example, to replace `this.old.name`with
`thisNewName`, you would call RenameField as follows:

```
newDyF = RenameField(oldDyF, "`this.old.name`", "thisNewName")
```

- `new_name` – The new name, including full path (required).
- `transformation_ctx` – A unique string that is used to identify state
  information (optional).
- `info` – A string associated with errors in the transformation
  (optional).
- `stageThreshold` – The maximum number of errors that can occur in the
  transformation before it errors out (optional). The default is zero.
- `totalThreshold` – The maximum number of errors that can occur
  overall before processing errors out (optional). The default is zero.

## apply(cls, \*args, \*\*kwargs)

Inherited from `GlueTransform`
[apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply").

## name(cls)

Inherited from `GlueTransform`
[name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name").

## describeArgs(cls)

Inherited from `GlueTransform`
[describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs").

## describeReturn(cls)

Inherited from `GlueTransform`
[describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn").

## describeTransform(cls)

Inherited from `GlueTransform`
[describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform").

## describeErrors(cls)

Inherited from `GlueTransform`
[describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors").

## describe(cls)

Inherited from `GlueTransform`
[describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
