

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_ZMin
<a name="ST_ZMin-function"></a>

ST\_ZMin returns the minimum `z` coordinate of an input geometry. 

## Syntax
<a name="ST_ZMin-function-syntax"></a>

```
ST_ZMin(geom)
```

## Arguments
<a name="ST_ZMin-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type. 

## Return type
<a name="ST_ZMin-function-return"></a>

`DOUBLE PRECISION` value of the minimum `z` coordinate. 

If *geom* is empty, then null is returned. 

If *geom* is null, then null is returned. 

If *geom* is a 2D or 3DM geometry, then null is returned. 

## Examples
<a name="ST_ZMin-function-examples"></a>

The following SQL returns the smallest `z` coordinate of a linestring in a 3DZ geometry. 

```
SELECT ST_ZMin(ST_GeomFromEWKT('LINESTRING Z (0 1 2, 3 4 5, 6 7 8)'));
```

```
st_zmin
-----------
  2
```

The following SQL returns the smallest `z` coordinate of a linestring in a 4D geometry. 

```
SELECT ST_ZMin(ST_GeomFromEWKT('LINESTRING ZM (0 1 2 3, 4 5 6 7, 8 9 10 11)'));
```

```
st_zmin
-----------
  2
```