# DynamicFrameCollection class

A `DynamicFrameCollection` is a dictionary of [DynamicFrame class](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md") objects, in which the
keys are the names of the `DynamicFrames` and the values are the
`DynamicFrame` objects.

## \_\_init\_\_

###### `__init__(dynamic_frames, glue_ctx)`

- `dynamic_frames` – A dictionary of [DynamicFrame class](aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md "aws-glue-api-crawler-pyspark-extensions-dynamic-frame.md") objects.
- `glue_ctx` – A [GlueContext class](aws-glue-api-crawler-pyspark-extensions-glue-context.md "aws-glue-api-crawler-pyspark-extensions-glue-context.md") object.

## Keys

`keys( )` – Returns a list of the keys in this collection, which
generally consists of the names of the corresponding `DynamicFrame` values.

## Values

`values(key)` – Returns a list of the `DynamicFrame` values in
this collection.

## Select

###### `select(key)`

Returns the `DynamicFrame` that corresponds to the specfied key (which is
generally the name of the `DynamicFrame`).

- `key` – A key in the `DynamicFrameCollection`, which
  usually represents the name of a `DynamicFrame`.

## Map

###### `map(callable, transformation_ctx="")`

Uses a passed-in function to create and return a new `DynamicFrameCollection`
based on the `DynamicFrames` in this collection.

- `callable` – A function that takes a `DynamicFrame` and
  the specified transformation context as parameters and returns a
  `DynamicFrame`.
- `transformation_ctx` – A transformation context to be used by the callable (optional).

## Flatmap

###### `flatmap(f, transformation_ctx="")`

Uses a passed-in function to create and return a new `DynamicFrameCollection`
based on the `DynamicFrames` in this collection.

- `f` – A function that takes a `DynamicFrame` as a
  parameter and returns a `DynamicFrame` or
  `DynamicFrameCollection`.
- `transformation_ctx` – A transformation context to be used by the function (optional).
