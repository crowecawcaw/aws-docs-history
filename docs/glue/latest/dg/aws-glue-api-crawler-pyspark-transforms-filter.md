

# Filter class
<a name="aws-glue-api-crawler-pyspark-transforms-filter"></a>

Builds a new `DynamicFrame` that contains records from the input `DynamicFrame` that satisfy a specified predicate function.

## Example
<a name="aws-glue-api-crawler-pyspark-transforms-filter-example"></a>

We recommend that you use the [`DynamicFrame.filter()`](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-filter) method to filter records in a `DynamicFrame`. To view a code example, see [Example: Use filter to get a filtered selection of fields](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-filter-example).

## Methods
<a name="aws-glue-api-crawler-pyspark-transforms-filter-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-filter-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-filter-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-filter-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-filter-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-filter-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-filter-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-filter-describeErrors)
+ [describe](#aws-glue-api-crawler-pyspark-transforms-filter-describe)

## \_\_call\_\_(frame, f, transformation\_ctx="", info="", stageThreshold=0, totalThreshold=0))
<a name="aws-glue-api-crawler-pyspark-transforms-filter-__call__"></a>

Returns a new `DynamicFrame` that is built by selecting records from the input `DynamicFrame` that satisfy a specified predicate function.
+ `frame` – The source `DynamicFrame` to apply the specified filter function to (required).
+ `f` – The predicate function to apply to each `DynamicRecord` in the `DynamicFrame`. The function must take a `DynamicRecord` as its argument and return True if the `DynamicRecord` meets the filter requirements, or False if it doesn't (required).

  A `DynamicRecord` represents a logical record in a `DynamicFrame`. It's similar to a row in a Spark `DataFrame`, except that it is self-describing and can be used for data that doesn't conform to a fixed schema.
+ `transformation_ctx` – A unique string that is used to identify state information (optional).
+ `info` – A string that is associated with errors in the transformation (optional).
+ `stageThreshold` – The maximum number of errors that can occur in the transformation before it errors out (optional). The default is zero.
+ `totalThreshold` – The maximum number of errors that can occur overall before processing errors out (optional). The default is zero.

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-filter-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).