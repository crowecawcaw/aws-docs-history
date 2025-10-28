# openCypher extensions in Amazon Neptune

Amazon Neptune supports the openCypher specification reference version 9. Please refer to
[openCypher specification compliance in Amazon Neptune](feature-opencypher-compliance.md "feature-opencypher-compliance.md")
in Amazon Neptune for details. Additionally, Amazon Neptune supports the features listed here. Unless specific
versions are mentioned, the features are available in Neptune Database and Neptune Analytics.

## The Neptune-specific `join()` function

Available in Neptune Database and Neptune Analytics.

Neptune implements a `join()` function that is not present in the
openCypher specification. It creates a string literal from a list of string literals
and a string delimiter. It takes two arguments:

- The first argument is a list of string literals.
- The second argument is the delimiter string, which can consist of
  zero, one, or more than one characters.

Example:

```
join(["abc", "def", "ghi"], ", ")    // Returns "abc, def, ghi"
```

## The Neptune-specific `removeKeyFromMap()` function

Available in Neptune Database and Neptune Analytics.

Neptune implements a `removeKeyFromMap()` function that is not present
in the openCypher specification. It removes a specified key from a map and returns
the resulting new map.

The function takes two arguments:

- The first argument is the map from which to remove the key.
- The second argument is the key to remove from the map.

The `removeKeyFromMap()` function is particularly useful in situations
where you want to set values for a node or relationship by unwinding a list of maps.
For example:

```
UNWIND [{`~id`: 'id1', name: 'john'}, {`~id`: 'id2', name: 'jim'}] as val
CREATE (n {`~id`: val.`~id`})
SET n = removeKeyFromMap(val, '~id')
```

## Custom ID values for node and

relationship properties

Available in Neptune Database 1.2.0.2 and up, and Neptune Analytics.

Starting in [engine release 1.2.0.2](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
Neptune has extended the openCypher specification so that you can now specify the
`id` values for nodes and relationships in
`CREATE`, `MERGE`, and `MATCH` clauses. This lets
you assign user-friendly strings instead of system-generated UUIDs to identify nodes
and relationships.

In Neptune Analytics, custom id values are not available for edges.

###### Warning

This extension to the openCypher specification is backward incompatible,
because `~id` is now considered a reserved property name. If you are
already using `~id` as a property in your data and queries, you will
need to migrate the existing property to a new property key and remove the old
one. See [What to do if you're currently using ~id as a property](#opencypher-compliance-custom-ids-migrating "#opencypher-compliance-custom-ids-migrating").

Here is an example showing how to create nodes and relationships that have
custom IDS:

```
CREATE (n {`~id`: 'fromNode', name: 'john'})
  -[:knows {`~id`: 'john-knows->jim', since: 2020}]
  ->(m {`~id`: 'toNode', name: 'jim'})
```

If you try to create a custom ID that is already in use, Neptune throws a
`DuplicateDataException` error.

Here is an example of using a custom ID in a `MATCH` clause:

```
MATCH (n {`~id`: 'id1'})
RETURN n
```

Here is an example of using custom IDs in a `MERGE` clause:

```
MATCH (n {name: 'john'}), (m {name: 'jim'})
MERGE (n)-[r {`~id`: 'john->jim'}]->(m)
RETURN r
```

### What to do if you're currently using `~id` as a property

With [engine release 1.2.0.2](engine-releases-1.2.0.md "engine-releases-1.2.0.md"), the
`~id` key in openCypher clauses is now treated as `id` instead of
as a property. This means that if you have a property named `~id`, accessing
it becomes impossible.

If you're using an `~id` property, what you have to do before upgrading
to engine release `1.2.0.2` or above is first to migrate the existing
`~id` property to a new property key, and then remove the `~id`
property. For example, the query below:

- Creates a new property named 'newId' for all nodes,
- copies over the value of the '~id' property into the 'newId' property,
- and removes the '~id' property from the data

```
MATCH (n)
WHERE exists(n.`~id`)
SET n.newId = n.`~id`
REMOVE n.`~id`
```

The same thing needs to be done for any relationships in the data that have
an `~id` property.

You will also have to change any queries you're using that reference an
`~id` property. For example, this query:

```
MATCH (n)
WHERE n.`~id` = 'some-value'
RETURN n
```

...would change to this:

```
MATCH (n)
WHERE n.newId = 'some-value'
RETURN n
```

## CALL subquery support in Neptune

Available in Neptune Database 1.4.1.0 and up, and Neptune Analytics.

Amazon Neptune supports `CALL` subqueries. A `CALL` subquery is a part of the main query that runs in an
isolated scope for each input to the `CALL` subquery.

For example, suppose a graph contains data about persons, their friends, and cities they lived in. We can retrieve the
two largest cities where each friend of someone lived in by using a `CALL` subquery:

```
MATCH (person:Person)-[:knows]->(friend)
CALL {
  WITH friend
  MATCH (friend)-[:lived_in]->(city)
  RETURN city
  ORDER BY city.population DESC
  LIMIT 2
}
RETURN person, friend, city
```

In this example, the query part inside `CALL { ... }` is executed for each `friend` that is matched
by the preceding MATCH clause. When the inner query is executed the `ORDER` and `LIMIT` clauses
are local to the cities where a specific friend lived in, so we obtain (at most) two cities per friend.

All query clauses are available inside `CALL` subqueries. This includes nested `CALL` subqueries as
well. Some restrictions for the first `WITH` clause and the emitted variables exist and are explained below.

### Scope of variables inside CALL subquery

The variables from the clauses before the `CALL` subquery that are used inside it must be imported by the
initial `WITH` clause. Unlike regular `WITH` clauses it can only contain a list of variables
but doesn't allow aliasing and can't be used together with `DISTINCT`, `ORDER BY`,
`WHERE`, `SKIP`, or `LIMIT`.

### Variables returned from CALL subquery

The variables that are emitted from the `CALL` subquery are specified with the final `RETURN`
clause. Note that the emitted variables cannot overlap with variables before the `CALL` subquery.

### Limitations

As of now, updates inside of a `CALL` subquery are not supported.

## Neptune openCypher functions

Available in Neptune Database 1.4.1.0 and up, and Neptune Analytics.

**textIndexOf**

`textIndexOf(text :: STRING, lookup :: STRING, from = 0 :: INTEGER?, to = -1 :: INTEGER?) :: (INTEGER?)`

Returns the index of the first occurrence of `lookup` in the range of `text` starting at offset
`from` (inclusive), through offset `to` (exclusive). If `to` is -1, the range continues
to the end of `text`. Indexing is zero-based, and is expressed in Unicode scalar values (non-surrogate code
points).

```
RETURN textIndexOf('Amazon Neptune', 'e')
{
  "results": [{
      "textIndexOf('Amazon Neptune', 'e')": 8
    }]
}
```

**collToSet**

`collToSet(values :: LIST OF ANY?) :: (LIST? OF ANY?)`

Returns a new list containing only the unique elements from the original list. The order of the original list is
**maintained** (e.g `[1, 6, 5, 1, 5]` returns `[1, 6, 5]`).

```
RETURN collToSet([1, 6, 5, 1, 1, 5])
{
  "results": [{
      "collToSet([1, 6, 5, 1, 1, 5])": [1, 6, 5]
    }]
}
```

**collSubtract**

`collSubtract(first :: LIST OF ANY?, second :: LIST OF ANY?) :: (LIST? OF ANY?)`

Returns a new list containing all the unique elements of `first` excluding elements from `second`.

```
RETURN collSubtract([2, 5, 1, 0], [1, 5])
{
  "results": [{
      "collSubtract([2, 5, 1, 0], [1, 5])": [0, 2]
    }]
}
```

**collIntersection**

`collIntersection(first :: LIST? OF ANY?, second :: LIST? OF ANY?) :: (LIST? OF ANY?)`

Returns a new list containing all the unique elements of the intersection of `first` and `second`.

```
RETURN collIntersection([2, 5, 1, 0], [1, 5])
{
  "results": [{
      "collIntersection([2, 5, 1, 0], [1, 5])": [1, 5]
    }]
}
```

## Sorting functions

The following sections define functions to sort collections. These functions take (in some cases optional) `config`
map arguments, or a list of multiple such maps, that define the sort key and/or the sort direction:

```
{ key: STRING, order: STRING }
```

Here `key` is either a map or node property whose value is to be used for sorting. `order` is
either "`asc`" or "`desc`" (case insensitive) to specify an ascending or descending sort,
respectively. By default, sorting will be performed in ascending order.

**collSort**

`collSort(coll :: LIST OF ANY, config :: MAP?) :: (LIST? OF ANY?)`

Returns a new sorted list containing the elements from the `coll` input list.

```
RETURN collSort([5, 3, 1], {order: 'asc'})
{
  "results": [{
      "collSort([5, 3, 1])": [1, 3, 5]
    }]
}
```

**collSortMaps**

`collSortMaps(coll :: LIST OF MAP, config :: MAP) :: (LIST? OF ANY?)`

Returns a list of maps sorted by the value of the specified `key` property.

```
RETURN collSortMaps([{name: 'Alice', age: 25}, {name: 'Bob', age: 35}, {name: 'Charlie', age: 18}], {key: 'age', order: 'desc'})
{
  "results": [{
      "x": [{
          "age": 35,
          "name": "Bob"
        }, {
          "age": 25,
          "name": "Alice"
        }, {
          "age": 18,
          "name": "Charlie"
        }]
    }]
}
```

**collSortMulti**

```
collSortMulti(coll :: LIST OF MAP?,
configs = [] :: LIST OF MAP,
limit = -1 :: INTEGER?,
skip = 0 :: INTEGER?) :: (LIST? OF ANY?)
```

Returns a list of maps sorted by the value of the specified `key` properties, optionally applying limit and skip.

```
RETURN collSortMulti([{name: 'Alice', age: 25}, {name: 'Bob', age: 35}, {name: 'Charlie', age: 18}], [{key: 'age', order: 'desc'}, {key:'name'}]) as x
{
  "results": [{
      "x": [{
          "age": 35,
          "name": "Bob"
        }, {
          "age": 25,
          "name": "Alice"
        }, {
          "age": 18,
          "name": "Charlie"
        }]
    }]
}
```

**collSortNodes**

`collSortNodes(coll :: LIST OF NODE, config :: MAP) :: (LIST? OF NODE?)`

Returns a sorted version of the `coll` input list, sorting the node elements by the values of
their respective `key` properties.

```
create (n:person {name: 'Alice', age: 23}), (m:person {name: 'Eve', age: 21}), (o:person {name:'Bob', age:25})
{"results":[]}

match (n:person) with collect(n) as people return collSortNodes(people, {key: 'name', order: 'desc'})
{
  "results": [{
      "collSortNodes(people, 'name')": [{
          "~id": "e599240a-8c23-4337-8aa8-f603c8fb5488",
          "~entityType": "node",
          "~labels": ["person"],
          "~properties": {
            "age": 21,
            "name": "Eve"
          }
        }, {
          "~id": "8a6ef785-59e3-4a0b-a0ff-389655a9c4e6",
          "~entityType": "node",
          "~labels": ["person"],
          "~properties": {
            "age": 25,
            "name": "Bob"
          }
        }, {
          "~id": "466bc826-f47f-452c-8a27-6b7bdf7ae9b4",
          "~entityType": "node",
          "~labels": ["person"],
          "~properties": {
            "age": 23,
            "name": "Alice"
          }
        }]
    }]
}

match (n:person) with collect(n) as people return collSortNodes(people, {key: 'age'})
{
  "results": [{
      "collSortNodes(people, '^age')": [{
          "~id": "e599240a-8c23-4337-8aa8-f603c8fb5488",
          "~entityType": "node",
          "~labels": ["person"],
          "~properties": {
            "age": 21,
            "name": "Eve"
          }
        }, {
          "~id": "466bc826-f47f-452c-8a27-6b7bdf7ae9b4",
          "~entityType": "node",
          "~labels": ["person"],
          "~properties": {
            "age": 23,
            "name": "Alice"
          }
        }, {
          "~id": "8a6ef785-59e3-4a0b-a0ff-389655a9c4e6",
          "~entityType": "node",
          "~labels": ["person"],
          "~properties": {
            "age": 25,
            "name": "Bob"
          }
        }]
    }]
}
```

## Temporal functions

Temporal functions are available from Neptune version
[1.4.5.0](../../../releases/release-1.4.5.0.md "../../../releases/release-1.4.5.0.md") and up.

### day

`day(temporal :: (datetime | date)) :: (LONG)`

Returns the `day` of the month from a `datetime` or `date` value.
For `datetime`: values are normalized to UTC based on input before extracting the day. For
`date`: day is extracted based on the timezone.

The `datetime` input is available in both Neptune Database and Neptune Analytics:

```
RETURN day(datetime('2021-06-03T01:48:14Z'))
{
  "results": [{
      "day(datetime('2021-06-03T01:48:14Z'))": 3
    }]
}
```

Here, the `datetime` is normalized to UTC, so +08:00 shifts back to June 2.

```
RETURN day(datetime('2021-06-03T00:00:00+08:00'))
{
  "results": [{
      "day(datetime('2021-06-03T00:00:00+08:00'))": 2
    }]
}
```

The `date` input is available only in Neptune Analytics:

```
RETURN day(date('2021-06-03Z'))
{
  "results": [{
      "day(date('2021-06-03Z'))": 3
    }]
}
```

The `date` preserves timezone, keeping June 3.

```
RETURN day(date('2021-06-03+08:00'))
{
  "results": [{
      "day(date('2021-06-03+08:00'))": 3
    }]
}

```

### month

`month(temporal :: (datetime | date)) :: (LONG)`

Returns the month from a `datetime` or `date` value (1-12). For `datetime`:
values are normalized to UTC based on input before extracting the month. For `date`: month is extracted
based on the timezone.

The `datetime` input is available in both Neptune Database and Neptune Analytics:

```
RETURN month(datetime('2021-06-03T01:48:14Z'))
{
  "results": [{
      "month(datetime('2021-06-03T01:48:14Z'))": 6
    }]
}
```

Here, the `datetime` is normalized to UTC, so +08:00 shifts back to May 31.

```

RETURN month(datetime('2021-06-01T00:00:00+08:00'))
{
  "results": [{
      "month(datetime('2021-06-01T00:00:00+08:00'))": 5
    }]
}

```

The `date` input is available only in Neptune Analytics:

```
RETURN month(date('2021-06-03Z'))
{
  "results": [{
      "month(date('2021-06-03Z'))": 6
    }]
}
```

The `date` preserves timezone, keeping June 1.

```
RETURN month(date('2021-06-01+08:00'))
{
  "results": [{
      "month(date('2021-06-01+08:00'))": 6
    }]
}
```

### year

`year(temporal :: (datetime | date)) :: (LONG)`

Returns the year from a `datetime` or `date` value. For `datetime`:
the values are normalized to UTC based on input before extracting the year. For `date`: the year
is extracted based on the timezone.

The `datetime` input is available in both Neptune Database and Neptune Analytics:

```

RETURN year(datetime('2021-06-03T01:48:14Z'))
{
  "results": [{
      "year(datetime('2021-06-03T01:48:14Z'))": 2021
    }]
}
```

Here, the `datetime` is normalized to UTC, so +08:00 shifts back to December 31, 2020.

```
RETURN year(datetime('2021-01-01T00:00:00+08:00'))
{
  "results": [{
      "year(datetime('2021-01-01T00:00:00+08:00'))": 2020
    }]
}
```

The `date` input is available only in Neptune Analytics:

```
RETURN year(date('2021-06-03Z'))
{
  "results": [{
      "year(date('2021-06-03Z'))": 2021
    }]
}
```

The `date` preserves timezone, keeping June 2021.

```
RETURN year(date('2021-01-01+08:00'))
{
  "results": [{
      "year(date('2021-01-01+08:00'))": 2021
    }]
}
```

### Neptune openCypher functions

Available in Neptune Database 1.4.6.0 and up, and Neptune Analytics.

#### reduce()

Reduce sequentially processes each list element by combining it with a running total or ‘accumulator.’
Starting with an initial value, it updates the accumulator after each operation and uses that updated value
in the next iteration.

`for i in (0, ..., n) acc = acc X list[I], where X denotes any binary operator`

Once all elements have been processed, it returns the final accumulated result.

A typical reduce() structure would be -
`reduce(accumulator = initial , variable IN list | expression)`

###### Type specifications:

`- initial: starting value for the accumulator :: (Long | FLOAT | STRING | LIST? OF (STRING, LONG, FLOAT))

- list: the input list :: LIST OF T where T matches initial type
- variable :: represents each element in the input list
- expression :: Only supports '+' and '\*' operator
- return :: Same type as initial`

###### Restrictions:

Currently, the `reduce()` expression only supports :

- Numeric Multiplication
- Numeric Addition
- String Concatenation
- List Concatenation

They are represented by the `+` or `*` operator. The expression should be a binary expression
as specified below -
`expression pattern: accumulator + any variable or accumulator * any variable`

###### Overflow handling:

Neptune detects numeric overflow during the `reduce()` evaluation and responds differently based
on the data type:

```
LONG (signed 64‑bit)
--------------------
• Valid range: –9 223 372 036 854 775 808 … 9 223 372 036 854 775 807
• If any intermediate or final value falls outside this range,
  Neptune aborts the query with long overflow error message.

FLOAT (IEEE‑754 double)
-----------------------
• Largest finite value ≈ 1.79 × 10^308
• Larger results overflow to INF
  Once `INF` is produced, it propagates through the remainder
  of the reduction.
```

###### Examples:

See the following examples for the reduce() function.

```

1. Long Addition:
RETURN reduce(sum = 0, n IN [1, 2, 3] | sum + n)
{
  "results": [{
      "reduce(sum = 0, n IN [1, 2, 3] | sum + n)": 6
    }]
}

2. String Concatenation:
RETURN reduce(str = "", x IN ["A", "B", "C"] | str + x)
{
  "results": [{
      "reduce(str = "", x IN ["A", "B", "C"] | str + x)": "ABC"
    }]
}

3. List Combination:
RETURN reduce(lst = [], x IN [1, 2, 3] | lst + x)
{
  "results": [{
      "reduce(lst = [], x IN [1, 2, 3] | lst + x)": [1, 2, 3]
    }]
}

4. Float Addition:
RETURN reduce(total = 0.0, x IN [1.5, 2.5, 3.5] | total + x)
{
  "results": [{
      "reduce(total = 0.0, x IN [1.5, 2.5, 3.5] | total + x)": 7.5
    }]
}

5. Long Multiplication:
RETURN reduce(product = 1, n IN [1, 2, 3] | product * n)
{
  "results": [{
      "reduce(product = 0, n IN [1, 2, 3] | product * n)": 6
    }]
}

6. Float Multiplication:
RETURN reduce(product = 1.0, n IN [1.5, 2.5, 3.5] | product * n)
{
  "results": [{
      "reduce(product = 1.0, n IN [1.5, 2.5, 3.5] | product * n)": 13.125
    }]
}

7. Long Overflow (Exception):
RETURN reduce(s = 9223372036854775807, x IN [2, 3] | s * x) AS result
{
"results": [{
    "reduce(s = 9223372036854775807, x IN [2, 3] | s * x) AS result": long overflow
    }]
}

8. Float Overflow:
RETURN reduce(s = 9.0e307, x IN [8.0e307, 1.0e307] | s + x) AS result
{
"results": [{
    "reduce(s = 9.0e307, x IN [8.0e307, 1.0e307] | s + x) AS result": INF
    }]
}

```
