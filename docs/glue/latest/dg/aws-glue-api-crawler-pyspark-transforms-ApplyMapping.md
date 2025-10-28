# ApplyMapping class

Applies a mapping in a `DynamicFrame`.

## Example

We recommend that you use the [DynamicFrame.apply_mapping()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-apply_mapping "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-apply_mapping")
method to apply a mapping in a `DynamicFrame`. To view a code example, see [Example: Use apply_mapping to rename fields and change field types](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-apply_mapping-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-apply_mapping-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-__call__ "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-apply "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-name "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeArgs "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeReturn "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeTransform "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeErrors "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describe "#aws-glue-api-crawler-pyspark-transforms-ApplyMapping-describe")

## \_\_call\_\_(frame, mappings, transformation_ctx = "",

info = "", stageThreshold = 0, totalThreshold = 0)

Applies a declarative mapping to a specified `DynamicFrame`.

- `frame` – The `DynamicFrame` to apply the mapping to
  (required).
- `mappings` – A list of mapping tuples (required). Each consists of:
  (source column, source type, target column, target type).

If the source column has a dot "`.`" in the name, you must place
back-ticks "````" around it. For example, to map `this.old.name` (string) to`thisNewName`, you would use the following tuple:

```
("`this.old.name`", "string", "thisNewName", "string")
```

- `transformation_ctx` – A unique string that is used to identify state
  information (optional).
- `info` – A string that is associated with errors in the
  transformation (optional).
- `stageThreshold` – The maximum number of errors that can occur in the
  transformation before it errors out (optional). The default is zero.
- `totalThreshold` – The maximum number of errors that can occur
  overall before processing errors out (optional). The default is zero.

Returns only the fields of the `DynamicFrame` that are specified in the
"mapping" tuples.

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
