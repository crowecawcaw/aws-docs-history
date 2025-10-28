# SplitRows class

Creates a `DynamicFrameCollection` that contains two `DynamicFrames`.
One `DynamicFrame` contains only the specified rows to be split, and the other
contains all remaining rows.

## Example

We recommend that you use the [DynamicFrame.split_rows()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_rows "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-split_rows")
method to split rows in a `DynamicFrame`. To view a code example, see [Example: Use split_rows to split rows in a
DynamicFrame](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-split_rows-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-split_rows-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-SplitRows-__call__ "#aws-glue-api-crawler-pyspark-transforms-SplitRows-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-SplitRows-apply "#aws-glue-api-crawler-pyspark-transforms-SplitRows-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-SplitRows-name "#aws-glue-api-crawler-pyspark-transforms-SplitRows-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeArgs "#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeReturn "#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeTransform "#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeErrors "#aws-glue-api-crawler-pyspark-transforms-SplitRows-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-SplitRows-describe "#aws-glue-api-crawler-pyspark-transforms-SplitRows-describe")

## \_\_call\_\_(frame,

comparison_dict, name1="frame1", name2="frame2", transformation_ctx = "", info = none,
stageThreshold = 0, totalThreshold = 0)

Splits one or more rows in a `DynamicFrame` off into a new
`DynamicFrame`.

- `frame` – The source `DynamicFrame` to split into two new
  ones (required).
- `comparison_dict` – A dictionary where the key is the full path to a
  column, and the value is another dictionary for mapping comparators to values that the
  column values are compared to. For example, `{"age": {">": 10, "<": 20}}`
  splits rows where the value of "age" is between 10 and 20, exclusive, from rows where
  "age" is outside that range (required).
- `name1` – The name to assign to the `DynamicFrame` that
  will contain the rows to be split off (optional).
- `name2` – The name to assign to the `DynamicFrame` that
  will contain the rows that remain after the specified rows are split off
  (optional).
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
