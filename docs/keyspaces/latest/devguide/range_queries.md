# Estimate the capacity consumption of range queries in Amazon Keyspaces

To look at the read capacity consumption of a range query, we use the following example table which is using on-demand capacity mode.

```
`pk1 | pk2 | pk3 | ck1 | ck2 | ck3 | value
-----+-----+-----+-----+-----+-----+-------
a | b | 1 | a | b | 50 | <any value that results in a row size larger than 4KB>
a | b | 1 | a | b | 60 | value_1
a | b | 1 | a | b | 70 | <any value that results in a row size larger than 4KB>`
```

Now run the following query on this table.

```
SELECT * FROM amazon_keyspaces.example_table_1 WHERE pk1='a' AND pk2='b' AND pk3=1 AND ck1='a' AND ck2='b' AND ck3 > 50 AND ck3 < 70;
```

You receive the following result set from the query and the read operation performed by Amazon Keyspaces consumes 2 RRUs in
`LOCAL_QUORUM` consistency mode.

```
`pk1 | pk2 | pk3 | ck1 | ck2 | ck3 | value
-----+-----+-----+-----+-----+-----+-------
a | b | 1 | a | b | 60 | value_1`
```

Amazon Keyspaces consumes 2 RRUs to evaluate the rows with the values `ck3=60` and `ck3=70` to process the query.
However, Amazon Keyspaces only returns the row where the `WHERE` condition specified in the query is true, which is the row with
value `ck3=60`. To evaluate the range specified
in the query, Amazon Keyspaces reads the row matching the upper bound of the range, in this case `ck3 = 70`,
but doesn’t return that row in the result. The read capacity consumption is based on the data read when processing the query, not
on the data returned.
