Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# ST\_GeogFromText

ST\_GeogFromText constructs a geography object from a well-known text (WKT) or extended well-known text (EWKT) representation of an input geography.

## Syntax

```
ST_GeogFromText(*wkt\_string*)
```

## Arguments

_wkt\_string_

A value of data type `VARCHAR` that is a WKT or EWKT representation of a geography.

## Return type

`GEOGRAPHY`

If the SRID value is set to the provided value in the input. If SRID is not provided, it is set to `4326`.

If _wkt\_string_ is null, then null is returned.

If _wkt\_string_ is not valid, then an error is returned.

## Examples

The following SQL constructs a polygon from a geography object with an SRID value.

```
SELECT ST_AsEWKT(ST_GeogFromText('SRID=4324;POLYGON((0 0,0 1,1 1,10 10,1 0,0 0))'));
```

```

  st_asewkt
------------------------------------------------
 SRID=4324;POLYGON((0 0,0 1,1 1,10 10,1 0,0 0))

```

The following SQL constructs a polygon from a geography object. The SRID value is set to `4326`.

```
SELECT ST_AsEWKT(ST_GeogFromText('POLYGON((0 0,0 1,1 1,10 10,1 0,0 0))'));
```

```

 st_asewkt
------------------------------------------------
 SRID=4326;POLYGON((0 0,0 1,1 1,10 10,1 0,0 0))

```
