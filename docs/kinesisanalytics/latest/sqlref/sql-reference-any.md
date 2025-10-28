# ANY

```
ANY ( <boolean_expression> )
```

ANY returns true if the supplied boolean_expression is true in any of the selected rows.
Returns false if the supplied boolean_expression is true in none of the selected rows.

###### Example

The following SQL snippet returns 'true' if the price for any ticker in the stream of
trades is below 1. Returns 'false' if every price in the stream is 1 or greater.

```
 SELECT STREAM ANY (price < 1) FROM trades
  GROUP BY (FLOOR trades.rowtime to hour)

```
