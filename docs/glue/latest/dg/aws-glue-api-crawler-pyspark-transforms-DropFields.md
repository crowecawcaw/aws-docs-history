# DropFields class

Drops fields within a `DynamicFrame`.

## Example

We recommend that you use the [DynamicFrame.drop_fields()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-drop_fields "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-drop_fields") method to drop
fields from a `DynamicFrame`. To view a code example, see [Example: Use drop_fields to remove fields from a DynamicFrame](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-drop_fields-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-drop_fields-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-DropFields-__call__ "#aws-glue-api-crawler-pyspark-transforms-DropFields-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-DropFields-apply "#aws-glue-api-crawler-pyspark-transforms-DropFields-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-DropFields-name "#aws-glue-api-crawler-pyspark-transforms-DropFields-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-DropFields-describeArgs "#aws-glue-api-crawler-pyspark-transforms-DropFields-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-DropFields-describeReturn "#aws-glue-api-crawler-pyspark-transforms-DropFields-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-DropFields-describeTransform "#aws-glue-api-crawler-pyspark-transforms-DropFields-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-DropFields-describeErrors "#aws-glue-api-crawler-pyspark-transforms-DropFields-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-DropFields-describe "#aws-glue-api-crawler-pyspark-transforms-DropFields-describe")

## \_\_call\_\_(frame, paths, transformation_ctx = "",

info = "", stageThreshold = 0, totalThreshold = 0)

Drops nodes within a `DynamicFrame`.

- `frame` – The `DynamicFrame` to drop the nodes in
  (required).
- `paths` – A list of full paths to the nodes to drop (required).
- `transformation_ctx` – A unique string that is used to identify state
  information (optional).
- `info` – A string associated with errors in the transformation (optional).
- `stageThreshold` – The maximum number of errors that can occur in the
  transformation before it errors out (optional). The default is zero.
- `totalThreshold` – The maximum number of errors that can occur overall before
  processing errors out (optional). The default is zero.

Returns a new `DynamicFrame` without the specified fields.

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
