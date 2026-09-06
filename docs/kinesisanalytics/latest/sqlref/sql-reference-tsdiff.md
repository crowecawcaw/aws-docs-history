

# TSDIFF
<a name="sql-reference-tsdiff"></a>

Returns NULL if any of the arguments is null.

 Otherwise returns the difference between the two timestamps in milliseconds.

## Syntax
<a name="sql-reference-tsdiff-syntax"></a>

```
TSDIFF(startTime, endTime)
```

## Parameters
<a name="sql-reference-tsdiff-parameters"></a>

*startTime*

A Unix timestamp in the format milliseconds since '1970-01-01 00:00:00' UTC, expressed as a BIGINT.

*endTime*

A Unix timestamp in the format milliseconds since '1970-01-01 00:00:00' UTC, expressed as a BIGINT.