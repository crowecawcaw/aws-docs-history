# MapToCollection class

Applies a transform to each `DynamicFrame` in the specified
`DynamicFrameCollection`.

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-__call__ "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-__call__")
- [Apply](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-apply "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-apply")
- [Name](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-name "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeArgs "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeReturn "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeTransform "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeErrors "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describe "#aws-glue-api-crawler-pyspark-transforms-MapToCollection-describe")

## \_\_call\_\_(dfc, BaseTransform, frame_name, transformation_ctx = "", \*\*base_kwargs)

Applies a transform function to each `DynamicFrame` in the specified
`DynamicFrameCollection`.

- `dfc` – The `DynamicFrameCollection` over which to apply the
  transform function (required).
- `callable` – A callable transform function to apply to each member of the
  collection (required).
- `transformation_ctx` – A unique string that
  is used to identify state information (optional).

Returns a new `DynamicFrameCollection` created by applying the transform to
each `DynamicFrame` in the source `DynamicFrameCollection`.

## apply(cls, \*args, \*\*kwargs)

Inherited from `GlueTransform`
[apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply")

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
