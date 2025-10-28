# Spigot class

Writes sample records to a specified destination to help you verify the transformations
performed by your AWS Glue job.

## Example

We recommend that you use the [DynamicFrame.spigot()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-spigot "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-spigot")
method to write a subset of records from a `DynamicFrame` to a specified destination. To view a code example, see [Example: Use spigot to write sample fields from a DynamicFrame to Amazon S3](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-spigot-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-spigot-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-spigot-__call__ "#aws-glue-api-crawler-pyspark-transforms-spigot-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-spigot-apply "#aws-glue-api-crawler-pyspark-transforms-spigot-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-spigot-name "#aws-glue-api-crawler-pyspark-transforms-spigot-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-spigot-describeArgs "#aws-glue-api-crawler-pyspark-transforms-spigot-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-spigot-describeReturn "#aws-glue-api-crawler-pyspark-transforms-spigot-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-spigot-describeTransform "#aws-glue-api-crawler-pyspark-transforms-spigot-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-spigot-describeErrors "#aws-glue-api-crawler-pyspark-transforms-spigot-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-spigot-describe "#aws-glue-api-crawler-pyspark-transforms-spigot-describe")

## \_\_call\_\_(frame,

path, options, transformation_ctx = "")

Writes sample records to a specified destination during a transformation.

- `frame` – The `DynamicFrame` to spigot (required).
- `path` – The path of the destination to write to (required).
- `options` – JSON key-value pairs that specify options (optional). The
  `"topk"` option specifies that the first _k_
  records should be written. The `"prob"` option specifies the probability (as a
  decimal) of picking any given record. You use this in selecting records to write.
- `transformation_ctx` – A unique string that is used to identify state
  information (optional).

## apply(cls, \*args, \*\*kwargs)

Inherited from `GlueTransform`
[apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply")

## name(cls)

Inherited from `GlueTransform`
[name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name")

## describeArgs(cls)

Inherited from `GlueTransform`
[describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs")

## describeReturn(cls)

Inherited from `GlueTransform`
[describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn")

## describeTransform(cls)

Inherited from `GlueTransform`
[describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform")

## describeErrors(cls)

Inherited from `GlueTransform`
[describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors")

## describe(cls)

Inherited from `GlueTransform`
[describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe")
