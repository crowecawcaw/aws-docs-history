

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_IsCollection
<a name="ST_IsCollection-function"></a>

ST\_IsCollection returns true if the input geometry is one of the following subtypes: `GEOMETRYCOLLECTION`, `MULTIPOINT`, `MULTILINESTRING`, or `MULTIPOLYGON`. 

## Syntax
<a name="ST_IsCollection-function-syntax"></a>

```
ST_IsCollection(geom)
```

## Arguments
<a name="ST_IsCollection-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type. 

## Return type
<a name="ST_IsCollection-function-return"></a>

`BOOLEAN`

If *geom* is null, then null is returned. 

## Examples
<a name="ST_IsCollection-function-examples"></a>

The following SQL checks if the polygon is a collection. 

```
SELECT ST_IsCollection(ST_GeomFromText('POLYGON((0 2,1 1,0 -1,0 2))'));
```

```
st_iscollection
-----------
 false
```