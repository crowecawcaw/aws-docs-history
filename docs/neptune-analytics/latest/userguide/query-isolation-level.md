# Transaction isolation levels in Neptune Analytics

Neptune Analytics has some differences with isolation level supported by
[Neptune Database](../../../neptune/latest/userguide/transactions-neptune.md "../../../neptune/latest/userguide/transactions-neptune.md").

**Read-only query isolation in Neptune Analytics:** Neptune Analytics evaluates read-only queries under
snapshot isolation, just like Neptune Database.

**Mutation query isolation in Neptune Analytics:** Reads for mutation queries are normally executed under
snapshot isolation, unlike Neptune Database. This is less stricter isolation than Neptune Database as the conditions in the query for
proceeding to a write satisfied in a snapshot could have changed concurrently before the query commits.

For some specific steps, such as node/relationship deletion or conditional creation of new data using the MERGE step,
reads also look at the concurrent writes, to avoid inconsistencies. Below are some examples where concurrent execution
of queries one and two always lead to a consistent state. At most, one vertex gets created in example #1. The age is set
to 10 or 11 in example #2, not both. And in example #3, either the vertex is fully deleted or the age is set to 11
without any deletion or removal of other properties.

```
# EXAMPLE 1
Query 1: MERGE (m:Person {ssn: '123456789'})
Query 2: MERGE (n:Person {ssn: '123456789'})
```

```
# EXAMPLE 2
Query 1: MATCH (n {ssn : '123456789'}) SET n.age=10
Query 2: MATCH (n {ssn : '123456789'}) SET n.age=11
```

```
# EXAMPLE 3
Query 1: MATCH (n {ssn : '123456789'}) DETACH DELETE n
Query 2: MATCH (n {ssn : '123456789'}) SET n.age = 11
```

**Conflict detection:** Different from Neptune Database, conflicts are evaluated more precisely over
individual graph elements (properties or edges) rather than over a range of data. Queries one and two in example #4
would not conflict when run concurrently because they search and merge on different property values ('lname1' and 'lname2').
However, queries one and two in example #5 merge on different property-value sets, but they could still confict when
run concurrently because they share a property-value (firstName: 'fname').

```
# EXAMPLE 4
Query 1: MERGE (n {lastName: 'lname1'})
Query 2: MERGE (n {lastName: 'lname2'})
```

```
# EXAMPLE 5
Query 1: MERGE (n {firstName: 'fname', lastName: 'lname1'})
Query 2: MERGE (n {firstName: 'fname', lastName: 'lname2'})
```
