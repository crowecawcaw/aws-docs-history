# UnnestFrame class

Unnests a `DynamicFrame`, flattens nested objects to top-level elements, and
generates join keys for array objects.

## Example

We recommend that you use the [DynamicFrame.unnest()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unnest "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-unnest")
method to flatten nested structures in a `DynamicFrame`. To view a code example, see [Example: Use unnest to turn nested fields into
top-level fields](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-unnest-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-unnest-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-__call__ "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-apply "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-name "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeArgs "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeReturn "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeTransform "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeErrors "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describe "#aws-glue-api-crawler-pyspark-transforms-UnnestFrame-describe")

## \_\_call\_\_(frame,

transformation_ctx = "", info="", stageThreshold=0, totalThreshold=0)

Unnests a `DynamicFrame`, flattens nested objects to top-level elements, and
generates join keys for array objects.

- `frame` – The `DynamicFrame` to unnest (required).
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
