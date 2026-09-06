

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# GeometryType
<a name="GeometryType-function"></a>

GeometryType returns the subtype of an input geometry as a string. 

## Syntax
<a name="GeometryType-function-syntax"></a>

```
GeometryType(geom)
```

## Arguments
<a name="GeometryType-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="GeometryType-function-return"></a>

`VARCHAR` representing the subtype of *geom*. 

If *geom* is null, then null is returned. 

The values returned are as follows.


| Returned string value for 2D, 3DZ, 4D geometries | Returned string value for 3DM geometries | Geometry subtype | 
| --- | --- | --- | 
| `POINT` | `POINTM` | Returned if *geom* is a `POINT` subtype  | 
| `LINESTRING` | `LINESTRINGM` | Returned if *geom* is a `LINESTRING` subtype  | 
| `POLYGON` | `POLYGONM` | Returned if *geom* is a `POLYGON` subtype  | 
| `MULTIPOINT` | `MULTIPOINTM` | Returned if *geom* is a `MULTIPOINT` subtype  | 
| `MULTILINESTRING` | `MULTILINESTRINGM` | Returned if *geom* is a `MULTILINESTRING` subtype  | 
| `MULTIPOLYGON` | `MULTIPOLYGONM` | Returned if *geom* is a `MULTIPOLYGON` subtype  | 
| `GEOMETRYCOLLECTION` | `GEOMETRYCOLLECTIONM` | Returned if *geom* is a `GEOMETRYCOLLECTION` subtype  | 

## Examples
<a name="GeometryType-function-examples"></a>

The following SQL converts a well-known text (WKT) representation of a polygon and returns the `GEOMETRY` subtype as a string.

```
SELECT GeometryType(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'));
```

```
geometrytype
-------------
 POLYGON
```