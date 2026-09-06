

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_NPoints
<a name="ST_NPoints-function"></a>

ST\_NPoints returns the number of nonempty points in an input geometry or geography. 

## Syntax
<a name="ST_NPoints-function-syntax"></a>

```
ST_NPoints(geo)
```

## Arguments
<a name="ST_NPoints-function-arguments"></a>

 *geo*   
A value of data type `GEOMETRY` or `GEOGRAPHY`, or an expression that evaluates to a `GEOMETRY` or `GEOGRAPHY` type.

## Return type
<a name="ST_NPoints-function-return"></a>

`INTEGER`

If *geo* is an empty point, then `0` is returned. 

If *geo* is null, then null is returned. 

## Examples
<a name="ST_NPoints-function-examples"></a>

The following SQL returns the number of points in a linestring. 

```
SELECT ST_NPoints(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```
st_npoints
-------------
 4
```

The following SQL returns the number of points in a linestring in a geography. 

```
SELECT ST_NPoints(ST_GeogFromText('LINESTRING(110 40, 2 3, -10 80, -7 9)'));
```

```
st_npoints
-------------
 4
```