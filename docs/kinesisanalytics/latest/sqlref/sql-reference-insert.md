# INSERT

INSERT is used to insert rows into a stream. It can also be used in a pump to insert the
output of one stream into another.

## Syntax

```
 <insert statement> :=
   INSERT [ EXPEDITED ]
   INTO  <table-name > [ ( insert-column-specification ) ]
   <  query  >
 <insert-column-specification> := < simple-identifier-list >
 <simple-identifier-list> :=
    <simple-identifier> [ , < simple-identifier-list > ]
```

For a discussion of VALUES, see [SELECT statement](sql-reference-select.md "sql-reference-select.md").

## Pump Stream Insert

INSERT may also be specified as part of a [CREATE PUMP](sql-reference-create-pump.md "sql-reference-create-pump.md") statement.

```
 CREATE PUMP "HighBidsPump" AS INSERT INTO "highBids" ( "ticker", "shares", "price")
 SELECT  "ticker", "shares", "price"
 FROM SALES.bids
 WHERE "shares"*"price">100000

```

Here the results to be inserted into the "highBids" stream should come from a
UNION ALL expression that
evaluates to a stream. This will create a continuously running stream insert. Rowtimes of the
rows inserted will be inherited from the rowtimes of the rows output from the select or UNION
ALL. Again rows may be initially dropped if other inserters, ahead of this inserter, have
inserted rows with rowtimes later than those initially prepared by this inserter, since the
latter would then be out of time order. See the topic [CREATE PUMP](sql-reference-create-pump.md "sql-reference-create-pump.md") in this
guide.
