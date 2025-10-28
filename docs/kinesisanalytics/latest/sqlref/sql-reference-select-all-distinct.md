# SELECT ALL and SELECT DISTINCT

If the ALL keyword is specified, the query does not eliminate duplicate rows. This is the
default behavior if neither ALL nor DISTINCT is specified.

If the DISTINCT keyword is specified, a query eliminates rows that are duplicates
according to the columns in the SELECT clause.

Note that for these purposes, the value NULL is considered equal to itself and not equal
to any other value. These are the same semantics as for GROUP BY and the IS NOT DISTINCT
FROM operator.

###### Streaming SELECT DISTINCT

SELECT DISTINCT can be used with streaming queries as long as there is a non-constant
monotonic expression in the SELECT clause. (The rationale for the non-constant monotonic
expression is the same as for
streaming
GROUP BY.) Amazon Kinesis Data Analytics emits rows for SELECT DISTINCT as soon as they are ready.

If ROWTIME is one of the columns in the SELECT clause, it is ignored for the purposes of
duplicate-elimination. Duplicates are eliminated on the basis of the other columns in the
SELECT clause.

For example:

```
SELECT STREAM DISTINCT ROWTIME, prodId, FLOOR(Orders.ROWTIME TO DAY)
FROM Orders

```

displays the set of unique products that are ordered in any given day.

If you are doing "GROUP BY floor(ROWTIME TO MINUTE)" and there are two rows in a given
minute -- say 22:49:10 and 22:49:15 -- then the summary of those rows is going to come out
timestamped 22:50:00. Why? Because that is the earliest time that row is complete.

**Note:** "GROUP BY ceil(ROWTIME TO MINUTE)" or "GROUP BY
floor(ROWTIME TO MINUTE) - INTERVAL '1' DAY" would give identical behavior.

It is not the value of the grouping expression that determines row completion, it's when
that expression changes value.

If you want the rowtimes of the output rows to be the time they are emitted, then in the
following example you would need to change from form 1 to use form 2 instead:

```
(Form 1)
   select distinct floor(s.rowtime to hour), a,b,c
   from s
(Form 2)
   select min(s.rowtime) as rowtime, floor(s.rowtime to hour), a, b, c
   from s
   group by floor(s.rowtime to hour), a, b, c

```
