

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SupportsBBox
<a name="SupportsBBox-function"></a>

SupportsBBox returns true if the input geometry supports encoding with a precomputed bounding box. For more information about support for bounding boxes, see [Bounding box](spatial-terminology.md#spatial-terminology-bounding-box).

## Syntax
<a name="SupportsBBox-function-syntax"></a>

```
SupportsBBox(geom)
```

## Arguments
<a name="SupportsBBox-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type
<a name="SupportsBBox-function-return"></a>

`BOOLEAN`

If *geom* is null, then null is returned.

## Examples
<a name="SupportsBBox-function-examples"></a>

The following SQL returns true because the input point geometry supports being encoded with a bounding box. 

```
SELECT SupportsBBox(AddBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```
supportsbbox
--------------
t
```

The following SQL returns false because the input point geometry doesn't support being encoded with a bounding box. 

```
SELECT SupportsBBox(DropBBox(ST_GeomFromText('POLYGON((0 0,1 0,0 1,0 0))')));
```

```
supportsbbox
--------------
f
```