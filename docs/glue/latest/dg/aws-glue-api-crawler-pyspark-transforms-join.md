# Join class

Performs an equality join on two `DynamicFrames`.

## Example

We recommend that you use the [DynamicFrame.join()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-join "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-join") method to join
`DynamicFrames`. To view a code example, see [Example: Use join to combine DynamicFrames](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-join-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-join-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-join-__call__ "#aws-glue-api-crawler-pyspark-transforms-join-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-join-apply "#aws-glue-api-crawler-pyspark-transforms-join-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-join-name "#aws-glue-api-crawler-pyspark-transforms-join-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-join-describeArgs "#aws-glue-api-crawler-pyspark-transforms-join-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-join-describeReturn "#aws-glue-api-crawler-pyspark-transforms-join-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-join-describeTransform "#aws-glue-api-crawler-pyspark-transforms-join-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-join-describeErrors "#aws-glue-api-crawler-pyspark-transforms-join-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-join-describe "#aws-glue-api-crawler-pyspark-transforms-join-describe")

## \_\_call\_\_(frame1, frame2, keys1, keys2, transformation_ctx = "")

Performs an equality join on two `DynamicFrames`.

- `frame1` – The first `DynamicFrame` to join (required).
- `frame2` – The second `DynamicFrame` to join (required).
- `keys1` – The keys to join on for the first frame (required).
- `keys2` – The keys to join on for the second frame (required).
- `transformation_ctx` – A unique string that
  is used to identify state information (optional).

Returns a new `DynamicFrame` that is created by joining the two
`DynamicFrames`.

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
