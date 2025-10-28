# EVERY

```
EVERY ( <boolean_expression> )
```

EVERY returns true if the supplied boolean_expression is true in all of the selected rows.
Returns false if the supplied boolean_expression is false in any of the selected rows.

###### Example

The following SQL snippet returns 'true' if the price for every ticker in the stream of
trades is below 1. Returns 'false' if any price is 1 or greater.

```
 SELECT STREAM EVERY (price < 1) FROM trades
  GROUP BY (FLOOR trades.rowtime to hour)
```
