Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ST_GeogFromWKB

ST_GeogFromWKB constructs a geography object from a hexadecimal well-known binary (WKB) representation of an input geography.

## Syntax

```
ST_GeogFromWKB(*wkb\_string*)
```

## Arguments

_wkb_string_

A value of data type `VARCHAR` that is a hexadecimal WKB representation of a geography.

## Return type

`GEOGRAPHY`

If the SRID value is provided it is set to the provided value. If SRID is not provided, it is set to `4326`.

If _wkb_string_ is null, then null is returned.

If _wkb_string_ is not valid, then an error is returned.

## Examples

The following SQL constructs a geography from a hexadecimal WKB value.

```
SELECT ST_AsEWKT(ST_GeogFromWKB('01030000000100000005000000000000000000000000000000000000000000000000000000000000000000F03F000000000000F03F000000000000F03F000000000000F03F000000000000000000000000000000000000000000000000'));
```

```

 st_asewkt
------------------------------------------
 SRID=4326;POLYGON((0 0,0 1,1 1,1 0,0 0))

```
