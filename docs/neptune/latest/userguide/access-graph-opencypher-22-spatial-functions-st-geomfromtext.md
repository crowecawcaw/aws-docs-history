

# ST\_GeomFromText
<a name="access-graph-opencypher-22-spatial-functions-st-geomfromtext"></a>

ST\_GeomFromText constructs a geometry object from a well-known text (WKT) representation of an input geometry.

**Syntax**

```
ST_GeomFromText(wkt_string)
```

**Arguments**
+ `wkt_string` - A value of data type STRING that is a WKT representation of a geometry.

**Return type**

GEOMETRY

If wkt\_string is null, then null is returned.

If wkt\_string is not valid, then a BadRequestException is returned.

**Examples**

```
RETURN ST_GeomFromText('POLYGON((0 0,0 1,1 1,1 0,0 0))')             
POLYGON((0 0,0 1,1 1,1 0,0 0))
```