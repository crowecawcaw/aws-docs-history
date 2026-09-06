

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# AddBBox
<a name="AddBBox-function"></a>

AddBBox returns a copy of the input geometry that supports encoding with a precomputed bounding box. For more information about support for bounding boxes, see [Bounding box](spatial-terminology.md#spatial-terminology-bounding-box).

## Syntax
<a name="AddBBox-function-syntax"></a>

```
AddBBox(geom)
```

## Arguments
<a name="AddBBox-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="AddBBox-function-return"></a>

`GEOMETRY`

If *geom* is null, then null is returned.

## Examples
<a name="AddBBox-function-examples"></a>

The following SQL returns a copy of an input polygon geometry that supports being encoded with a bounding box. 

```
SELECT ST_AsText(AddBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```
 st_astext
----------
 POLYGON((0 0,1 0,0 1,0 0))
```