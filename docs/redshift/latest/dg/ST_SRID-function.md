

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# ST\_SRID
<a name="ST_SRID-function"></a>

ST\_SRID returns the spatial reference system identifier (SRID) of an input geometry. For more information about an SRID, see [Querying spatial data in Amazon Redshift](geospatial-overview.md).

## Syntax
<a name="ST_SRID-function-syntax"></a>

```
ST_SRID(geom)
```

## Arguments
<a name="ST_SRID-function-arguments"></a>

 *geom*   
A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type. 

## Return type
<a name="ST_SRID-function-return"></a>

`INTEGER` representing the SRID value of *geom*. 

If *geom* is null, then null is returned. 

## Examples
<a name="ST_SRID-function-examples"></a>

The following SQL returns an SRID value of a linestring that is set to SRID `4326`.

```
SELECT ST_SRID(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)',4326));
```

```
st_srid
-------------
 4326
```

The following SQL returns an SRID value of a linestring that is not set when constructed. This results in `0` for the SRID value.

```
SELECT ST_SRID(ST_GeomFromText('LINESTRING(77.29 29.07,77.42 29.26,77.27 29.31,77.29 29.07)'));
```

```
st_srid
-------------
 0
```