# ErrorsAsDynamicFrame class

Returns a `DynamicFrame` that contains nested records for errors that occurred
while the source `DynamicFrame` was created.

## Example

We recommend that you use the [DynamicFrame.errorsAsDynamicFrame()](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsAsDynamicFrame "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#aws-glue-api-crawler-pyspark-extensions-dynamic-frame-errorsAsDynamicFrame") method to
retrieve and view error records. To view a code example, see [Example: Use errorsAsDynamicFrame to
view error records](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-errorsAsDynamicFrame-example "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md#pyspark-errorsAsDynamicFrame-example").

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-__call__ "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-apply "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-name "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeArgs "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeReturn "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeTransform "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeErrors "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describe "#aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame-describe")

## \_\_call\_\_(frame)

Returns a `DynamicFrame` that contains nested error records that relate to the
source `DynamicFrame`.

- `frame` – The source `DynamicFrame` (required).

## apply(cls, \*args, \*\*kwargs)

- `cls` – cls

## name(cls)

- `cls` – cls

## describeArgs(cls)

- `cls` – cls

## describeReturn(cls)

- `cls` – cls

## describeTransform(cls)

- `cls` – cls

## describeErrors(cls)

- `cls` – cls

## describe(cls)

- `cls` – cls
