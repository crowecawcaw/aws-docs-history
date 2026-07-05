Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_NRings

ST\_NRings returns the number of rings in an input geometry.

## Syntax

```
ST_NRings(*geom*)
```

## Arguments

_geom_

A value of data type `GEOMETRY` or an expression that evaluates to a `GEOMETRY` type.

## Return type

`INTEGER`

If _geom_ is null, then null is returned.

The values returned are as follows.

| Returned value                        | Geometry subtype                                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| 0                                     | Returned if *geom<br>• is a `POINT`, `LINESTRING`,<br>`MULTIPOINT`, or `MULTILINESTRING` subtype |
| The number of rings.                  | Returned if *geom<br>• is a `POLYGON` or `MULTIPOLYGON`<br>subtype                               |
| The number of rings in all components | Returned if *geom<br>• is a `GEOMETRYCOLLECTION` subtype                                         |

## Examples

The following SQL returns the number of rings in a multipolygon.

```
SELECT ST_NRings(ST_GeomFromText('MULTIPOLYGON(((0 0,10 0,0 10,0 0)),((0 0,-10 0,0 -10,0 0)))'));
```

```

 st_nrings
-------------
 2

```
