# FlatMap class

Applies a transform to each `DynamicFrame` in a collection.
Results are not flattened into a single `DynamicFrame`, but preserved as a collection.

## Examples for FlatMap

The following example snippet demonstrates how to use the `ResolveChoice` transform on a collection of
dynamic frames when applied to a `FlatMap`. The data used for input is in the JSON located at the
placeholder Amazon S3 address `s3://bucket/path-for-data/sample.json` and contains the following data.

```
[{
    "firstname": "Arnav",
    "lastname": "Desai",
    "address": {
        "street": "6 Anyroad Avenue",
        "city": "London",
        "state": "England",
        "country": "UK"
    },
    "phone": 17235550101,
    "affiliations": [
        "General Anonymous Example Products",
        "Example Independent Research",
        "Government Department of Examples"
    ]
},
{
    "firstname": "Mary",
    "lastname": "Major",
    "address": {
        "street": "7821 Spot Place",
        "city": "Centerville",
        "state": "OK",
        "country": "US"
    },
    "phone": 19185550023,
    "affiliations": [
        "Example Dot Com",
        "Example Independent Research",
        "Example.io"
    ]
},
{
    "firstname": "Paulo",
    "lastname": "Santos",
    "address": {
        "street": "123 Maple Street",
        "city": "London",
        "state": "Ontario",
        "country": "CA"
    },
    "phone": 12175550181,
    "affiliations": [
        "General Anonymous Example Products",
        "Example Dot Com"
    ]
}]

```

###### Example Apply ResolveChoice to a DynamicFrameCollection and show output.

```
#Read DynamicFrame
datasource = glueContext.create_dynamic_frame_from_options("s3", connection_options = {"paths":["s3://bucket/path/to/file/mysamplejson.json"]}, format="json")
datasource.printSchema()
datasource.show()

## Split to create a DynamicFrameCollection
split_frame=datasource.split_fields(["firstname","lastname","address"],"personal_info","business_info")
split_frame.keys()
print("---")

## Use FlatMap to run ResolveChoice
kwargs = {"choice": "cast:string"}
flat = FlatMap.apply(split_frame, ResolveChoice, frame_name="frame", transformation_ctx='tcx', **kwargs)
flat.keys()

##Select one of the DynamicFrames
personal_info = flat.select("personal_info")
personal_info.printSchema()
personal_info.show()
print("---")

business_info = flat.select("business_info")
business_info.printSchema()
business_info.show()
```

###### Important

When calling `FlatMap.apply`, the `frame_name` parameter **must** be
`"frame"`. No other value is currently accepted.

```
root
|-- firstname: string
|-- lastname: string
|-- address: struct
|    |-- street: string
|    |-- city: string
|    |-- state: string
|    |-- country: string
|-- phone: long
|-- affiliations: array
|    |-- element: string
---
{
    "firstname": "Mary",
    "lastname": "Major",
    "address": {
        "street": "7821 Spot Place",
        "city": "Centerville",
        "state": "OK",
        "country": "US"
    },
    "phone": 19185550023,
    "affiliations": [
        "Example Dot Com",
        "Example Independent Research",
        "Example.io"
    ]
}

{
    "firstname": "Paulo",
    "lastname": "Santos",
    "address": {
        "street": "123 Maple Street",
        "city": "London",
        "state": "Ontario",
        "country": "CA"
    },
    "phone": 12175550181,
    "affiliations": [
        "General Anonymous Example Products",
        "Example Dot Com"
    ]
}
---
root
|-- firstname: string
|-- lastname: string
|-- address: struct
|    |-- street: string
|    |-- city: string
|    |-- state: string
|    |-- country: string

{
    "firstname": "Mary",
    "lastname": "Major",
    "address": {
        "street": "7821 Spot Place",
        "city": "Centerville",
        "state": "OK",
        "country": "US"
    }
}

{
    "firstname": "Paulo",
    "lastname": "Santos",
    "address": {
        "street": "123 Maple Street",
        "city": "London",
        "state": "Ontario",
        "country": "CA"
    }
}
---
root
|-- phone: long
|-- affiliations: array
|    |-- element: string

{
    "phone": 19185550023,
    "affiliations": [
        "Example Dot Com",
        "Example Independent Research",
        "Example.io"
    ]
}

{
    "phone": 12175550181,
    "affiliations": [
        "General Anonymous Example Products",
        "Example Dot Com"
    ]
}
```

## Methods

- [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-flat-map-__call__ "#aws-glue-api-crawler-pyspark-transforms-flat-map-__call__")
- [Apply](#aws-glue-api-crawler-pyspark-transforms-flat-map-apply "#aws-glue-api-crawler-pyspark-transforms-flat-map-apply")
- [Name](#aws-glue-api-crawler-pyspark-transforms-flat-map-name "#aws-glue-api-crawler-pyspark-transforms-flat-map-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-flat-map-describeArgs "#aws-glue-api-crawler-pyspark-transforms-flat-map-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-flat-map-describeReturn "#aws-glue-api-crawler-pyspark-transforms-flat-map-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-flat-map-describeTransform "#aws-glue-api-crawler-pyspark-transforms-flat-map-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-flat-map-describeErrors "#aws-glue-api-crawler-pyspark-transforms-flat-map-describeErrors")
- [Describe](#aws-glue-api-crawler-pyspark-transforms-flat-map-describe "#aws-glue-api-crawler-pyspark-transforms-flat-map-describe")

## \_\_call\_\_(dfc, BaseTransform, frame_name, transformation_ctx = "", \*\*base_kwargs)

Applies a transform to each `DynamicFrame` in a collection and flattens the
results.

- `dfc` – The `DynamicFrameCollection` over which to flatmap
  (required).
- `BaseTransform` – A transform derived from `GlueTransform` to
  apply to each member of the collection (required).
- `frame_name` – The argument name to pass the elements of the collection to
  (required).
- `transformation_ctx` – A unique string that
  is used to identify state information (optional).
- `base_kwargs` – Arguments to pass to the base
  transform (required).

Returns a new `DynamicFrameCollection` created by applying the transform to
each `DynamicFrame` in the source `DynamicFrameCollection`.

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
