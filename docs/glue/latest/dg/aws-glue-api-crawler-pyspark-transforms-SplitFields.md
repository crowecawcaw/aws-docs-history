# SplitFields class

Splits a `DynamicFrame` into two new ones, by specified fields.

## Example

We recommend that you use the [DynamicFrame.split_fields()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_fields "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_fields")
method to split fields in a `DynamicFrame`. To view a code example, see [Example: Use split_fields to split selected fields into a separate DynamicFrame](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-split_fields-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-split_fields-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-SplitFields-__call__ "#aws-glue-api-crawler-pyspark-transforms-SplitFields-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-SplitFields-apply "#aws-glue-api-crawler-pyspark-transforms-SplitFields-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-SplitFields-name "#aws-glue-api-crawler-pyspark-transforms-SplitFields-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeArgs "#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeReturn "#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeTransform "#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeErrors "#aws-glue-api-crawler-pyspark-transforms-SplitFields-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-SplitFields-describe "#aws-glue-api-crawler-pyspark-transforms-SplitFields-describe")

## \_\_call\_\_(frame,

paths, name1 = none, name2 = none, transformation_ctx = "", info = "", stageThreshold = 0,
totalThreshold = 0)

Splits one or more fields in a `DynamicFrame` off into a new
`DynamicFrame`, and creates another new `DynamicFrame` that contains
the fields that remain.

- `frame` – The source `DynamicFrame` to split into two new
  ones (required).
- `paths` – A list of full paths to the fields to be split
  (required).
- `name1` – The name to assign to the `DynamicFrame` that
  will contain the fields to be split off (optional). If no name is supplied, the name of
  the source frame is used with "1" appended.
- `name2` – The name to assign to the `DynamicFrame` that
  will contain the fields that remain after the specified fields are split off (optional).
  If no name is provided, the name of the source frame is used with "2" appended.
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
