# Tuning Your Queries Using Composite Attributes

Careful implementation of attributes can increase the efficiency of query
operations in terms of duration and complexity. SimpleDB indexes attributes
individually. In some cases, a query contains predicates on more than one attribute,
and the combined selectivity of the predicates is significantly higher than the
selectivity of each individual predicate. When this happens, the query retrieves a
lot of data, and then removes most of the data to generate the result, which can
degrade performance. If you find your queries using this pattern, you can implement
composite attributes to improve your queries' performance.

The following example retrieves many books and many book prices before returning
the requested result of books priced under nine dollars.

```
select * from myDomain where Type = 'Book' and Price < '9'
```

A composite attribute provides a more efficient way to handle this query. Assuming
the attribute `Type` is a fixed four character string, a new composite
attribute of `TypePrice` allows you to write a single predicate
query.

```
select * from myDomain where TypePrice > 'Book' and TypePrice < 'Book9'
```

Performance for a multi-predicate query can also degrade if it uses an `order
 by` clause and the sorted attribute is constrained by a non-selective
predicate. A typical example uses `not null`. For example, a table
contains user names, billing timestamps, and a variety of other attributes. You want
to get the latest 100 billing times for a user. A typical approach for this query
leverages the index on the `user_id` attribute, retrieving all the
records with the user's ID value, filtering the ones with correct values for the
billing time, and then sorting the records and filtering out the top 100. The
following example retrieves the latest 100 billing times for a user.

```
select * from myDomain where user_id = '1234' and bill_time is not null order by bill_time limit 100
```

However, if the predicate on `user_id` is not selective (i.e. many
items exist in the domain for the `user_id` value `1234`),
then the SimpleDB query processor could avoid dynamically sorting a very large
number of records and scan the index on `bill_time`, instead. For this
execution strategy, SimpleDB discards all the records not belonging to
`user_id` value `1234`.

A composite attribute provides a more efficient way to handle this query, too.
You can combine the `user_id` and `bill_time` values into a
composite value, and then query for items with that value. The way you combine must
depend on your data. In our example, bill_time may be a single string or may be
missing, and the `user_id` attribute is a single four character string.
We combine them by concatenating their texts; but if bill_time is missing, the
missing data propagates and the concatenation is also missing. The following query
would efficiently seek the billing times for a user by querying only that composite
attribute.

```
select * from myDomain where user_id_bill_time like '1234%' order by user_id_bill_time limit 100
```

If `user_id` is a variable length field (not a fixed number of
characters for the value), consider using a separator when combining it with
`bill_time` in the `user_id_bill_time` composite
attribute. For example, the following attribute assignment uses the vertical bar
separator character (`|`) for a `user_id` that is six
characters long: `user_id_bill_time = 123456|1305914378`. The following
select example only gets the attributes with `user_id =1234` in the
composite attribute, and does not get the attributes for the six character
`user_id`.

```
select * from myDomain where user_id_bill_time like '1234|%' order by user_id_bill_time limit 100
```

The composite attribute technique is described further in the "Query performance
optimization" section at [Building
for Performance and Reliability with Amazon SimpleDB](http://aws.amazon.com/articles/1394 "http://aws.amazon.com/articles/1394").
