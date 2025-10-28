# Unbox class

Unboxes (reformats) a string field in a `DynamicFrame`.

## Example

We recommend that you use the [DynamicFrame.unbox()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unbox "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unbox")
method to unbox a field in a `DynamicFrame`. To view a code example, see [Example: Use unbox to unbox a string field into a struct](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-unbox-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-unbox-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-Unbox-__call__ "#aws-glue-api-crawler-pyspark-transforms-Unbox-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-Unbox-apply "#aws-glue-api-crawler-pyspark-transforms-Unbox-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-Unbox-name "#aws-glue-api-crawler-pyspark-transforms-Unbox-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-Unbox-describeArgs "#aws-glue-api-crawler-pyspark-transforms-Unbox-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-Unbox-describeReturn "#aws-glue-api-crawler-pyspark-transforms-Unbox-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-Unbox-describeTransform "#aws-glue-api-crawler-pyspark-transforms-Unbox-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-Unbox-describeErrors "#aws-glue-api-crawler-pyspark-transforms-Unbox-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-Unbox-describe "#aws-glue-api-crawler-pyspark-transforms-Unbox-describe")

## \_\_call\_\_(frame, path,

format, transformation_ctx = "", info="", stageThreshold=0, totalThreshold=0,
\*\*options)

Unboxes a string field in a `DynamicFrame`.

- `frame` – The `DynamicFrame` in which to unbox a field.
  (required).
- `path` – The full path to the `StringNode` to unbox
  (required).
- `format` – A format specification (optional). This is used for an
  Amazon S3 or AWS Glue connection that supports multiple formats. For the formats
  that are supported, see [Data format options for inputs and outputs in
  AWS Glue for Spark](aws-glue-programming-etl-format.md "aws-glue-programming-etl-format.md").
- `transformation_ctx` – A unique string that is used to identify state
  information (optional).
- `info` – A string associated with errors in the transformation
  (optional).
- `stageThreshold` – The maximum number of errors that can occur in the
  transformation before it errors out (optional). The default is zero.
- `totalThreshold` – The maximum number of errors that can occur
  overall before processing errors out (optional). The default is zero.
- `separator` – A separator token (optional).
- `escaper` – An escape token (optional).
- `skipFirst` – `True` if the first line of data should be
  skipped, or `False` if it should not be skipped (optional).
- withSchema – A string that contains a schema for the data to be unboxed
  (optional). This should always be created using `StructType.json`.
- `withHeader` – `True` if the data being unpacked includes
  a header, or `False` if not (optional).

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
