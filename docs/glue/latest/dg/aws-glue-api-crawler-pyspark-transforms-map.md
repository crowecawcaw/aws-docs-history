

# Map class
<a name="aws-glue-api-crawler-pyspark-transforms-map"></a>

Builds a new `DynamicFrame` by applying a function to all records in the input `DynamicFrame`.

## Example
<a name="aws-glue-api-crawler-pyspark-transforms-map-examples"></a>

We recommend that you use the [`DynamicFrame.map()`](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-map) method to apply a function to all records in a `DynamicFrame`. To view a code example, see [Example: Use map to apply a function to every record in a `DynamicFrame`](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-map-example).

## Methods
<a name="aws-glue-api-crawler-pyspark-transforms-map-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-map-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-map-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-map-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-map-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-map-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-map-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-map-describeErrors)
+ [Describe](#aws-glue-api-crawler-pyspark-transforms-map-describe)

## \_\_call\_\_(frame, f, transformation\_ctx="", info="", stageThreshold=0, totalThreshold=0)
<a name="aws-glue-api-crawler-pyspark-transforms-map-__call__"></a>

Returns a new `DynamicFrame` that results from applying the specified function to all `DynamicRecords` in the original `DynamicFrame`.
+ `frame` – The original `DynamicFrame` to apply the mapping function to (required).
+ `f` – The function to apply to all `DynamicRecords` in the `DynamicFrame`. The function must take a `DynamicRecord` as an argument and return a new `DynamicRecord` that is produced by the mapping (required).

  A `DynamicRecord` represents a logical record in a `DynamicFrame`. It's similar to a row in an Apache Spark `DataFrame`, except that it is self-describing and can be used for data that doesn't conform to a fixed schema.
+ `transformation_ctx` – A unique string that is used to identify state information (optional).
+ `info` – A string associated with errors in the transformation (optional).
+ `stageThreshold` – The maximum number of errors that can occur in the transformation before it errors out (optional). The default is zero.
+ `totalThreshold` – The maximum number of errors that can occur overall before processing errors out (optional). The default is zero.

Returns a new `DynamicFrame` that results from applying the specified function to all `DynamicRecords` in the original `DynamicFrame`.

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-map-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-map-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-map-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-map-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-map-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-map-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-map-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).