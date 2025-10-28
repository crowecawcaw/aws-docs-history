# SelectFields class

The `SelectFields` class creates a new `DynamicFrame` from an existing
`DynamicFrame`, and keeps only the fields that you specify.
`SelectFields` provides similar functionality to a SQL `SELECT`
statement.

## Example

We recommend that you use the [DynamicFrame.select_fields()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-select_fields "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-select_fields") method to select
fields from a `DynamicFrame`. To view a code example, see [Example: Use select_fields to create a new DynamicFrame with chosen fields](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-select_fields-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-select_fields-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-SelectFields-__call__ "#aws-glue-api-crawler-pyspark-transforms-SelectFields-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-SelectFields-apply "#aws-glue-api-crawler-pyspark-transforms-SelectFields-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-SelectFields-name "#aws-glue-api-crawler-pyspark-transforms-SelectFields-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeArgs "#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeReturn "#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeTransform "#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeErrors "#aws-glue-api-crawler-pyspark-transforms-SelectFields-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-SelectFields-describe "#aws-glue-api-crawler-pyspark-transforms-SelectFields-describe")

## \_\_call\_\_(frame, paths,

transformation_ctx = "", info = "", stageThreshold = 0, totalThreshold = 0)

Gets fields (nodes) in a `DynamicFrame`.

- `frame` – The `DynamicFrame` to select fields in
  (required).
- `paths` – A list of full paths to the fields to select (required).
- `transformation_ctx` – A unique string that is used to
  identify state information (optional).
- `info` – A string that is associated with errors in the transformation
  (optional).
- `stageThreshold` – The maximum number of errors that can occur in the
  transformation before it errors out (optional). The default is zero.
- `totalThreshold` – The maximum number of errors that can occur overall before
  processing errors out (optional). The default is zero.

Returns a new `DynamicFrame` that contains only the specified fields.

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
