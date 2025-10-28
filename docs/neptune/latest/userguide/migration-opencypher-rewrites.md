# Rewriting Cypher queries to run in openCypher on Neptune

The openCypher language is a declarative query language for property graphs that
was originally developed by Neo4j, then open-sourced in 2015, and contributed to the
[openCypher project](https://www.opencypher.org/ "https://www.opencypher.org/") under an Apache 2
open-source license. At AWS, we believe that open source is good for everyone and
we are committed to bringing the value of open source to our customers, and the
operational excellence of AWS to open source communities.

OpenCypher syntax is documented in the [Cypher
Query Language Reference, Version 9](https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf "https://s3.amazonaws.com/artifacts.opencypher.org/openCypher9.pdf").

Because openCypher contains a subset of the syntax and features of the Cypher
query language, some migration scenarios require either rewriting queries in
openCypher-compliant forms or examining alternative methods to achieve the
desired functionality.

This section contains recommendations for handling common differences, but they
are by no means exhaustive. You should test any application using these rewrites
thoroughly to ensure that the results are what you expect.

## Rewriting `None`,

`All`, and `Any` predicate functions

These functions are not part of the openCypher specification. Comparable results
can be achieved in openCypher using List Comprehension.

For example, find all the paths that go from node `Start` to node
`End`, but no journey is allowed to pass through a node with a class
property of `D`:

```
# Neo4J Cypher code
match p=(a:Start)-[:HOP*1..]->(z:End)
where none(node IN nodes(p) where node.class ='D')
return p

# Neptune openCypher code
match p=(a:Start)-[:HOP*1..]->(z:End)
where size([node IN nodes(p) where node.class = 'D']) = 0
return p
```

List comprehension can achieve these results as follows:

```
all  => size(list_comprehension(list)) = size(list)
any  => size(list_comprehension(list)) >= 1
none => size(list_comprehension(list)) = 0
```

## Rewriting the Cypher

`reduce()` function in openCypher

The `reduce()` function is not part of the openCypher specification.
It is often used to create an aggregation of data from elements within a list.
In many cases, you can use a combination of List Comprehension and the
`UNWIND` clause to achieve similar results.

For example, the following Cypher query finds all airports on paths having one
to three stops between Anchorage (ANC) and Austin (AUS), and returns the total
distance of each path:

```
MATCH p=(a:airport {code: 'ANC'})-[r:route*1..3]->(z:airport {code: 'AUS'})
RETURN p, reduce(totalDist=0, r in relationships(p) | totalDist + r.dist) AS totalDist
ORDER BY totalDist LIMIT 5
```

You can write the same query in openCypher for Neptune as follows:

```
MATCH p=(a:airport {code: 'ANC'})-[r:route*1..3]->(z:airport {code: 'AUS'})
UNWIND [i in relationships(p) | i.dist] AS di
RETURN p, sum(di) AS totalDist
ORDER BY totalDist
LIMIT 5
```

## Rewriting the Cypher FOREACH

clause in openCypher

The FOREACH clause is not part of the openCypher specification. It is often used
to update data in the middle of a query, often from aggregations or elements within
a path.

As a path example, find all airports on a path with no more than two
stops between Anchorage (ANC) and Austin (AUS) and set a property of
visited on each of them:

```
# Neo4J Example
MATCH p=(:airport {code: 'ANC'})-[*1..2]->({code: 'AUS'})
FOREACH (n IN nodes(p) | SET n.visited = true)

# Neptune openCypher
MATCH p=(:airport {code: 'ANC'})-[*1..2]->({code: 'AUS'})
WITH nodes(p) as airports
UNWIND airports as a
SET a.visited=true
```

Another example is:

```
# Neo4J Example
MATCH p=(start)-[*]->(finish)
WHERE start.name = 'A' AND finish.name = 'D'
FOREACH (n IN nodes(p) | SET n.marked = true)

# Neptune openCypher
MATCH p=(start)-[*]->(finish)
WHERE start.name = 'A' AND finish.name = 'D'
UNWIND nodes(p) AS n
SET n.marked = true
```

## Rewriting Neo4j APOC procedures

in Neptune

The examples below use openCypher to replace some of the most commonly used
[APOC
procedures](https://neo4j.com/blog/intro-user-defined-procedures-apoc/ "https://neo4j.com/blog/intro-user-defined-procedures-apoc/"). These examples are for reference only, and are intended to
provide some suggestions about how to handle common scenarios. In practice,
each application is different, and you'll have to come up with your own
strategies for providing all the functionality you need.

### Rewriting `apoc.export` procedures

Neptune provides an array of options for both full graph and query-based exports
in various output formats such as CSV and JSON, using the [neptune-export](https://github.com/aws/neptune-export "https://github.com/aws/neptune-export") utility
(see [Exporting data from a Neptune DB cluster](neptune-data-export.md "neptune-data-export.md")).

### Rewriting `apoc.schema` procedures

Neptune does not have explicitly defined schema, indices, or constraints, so many
`apoc.schema` procedures are no longer required. Examples are:

- `apoc.schema.assert`
- `apoc.schema.node.constraintExists`
- `apoc.schema.node.indexExists`,
- `apoc.schema.relationship.constraintExists`
- `apoc.schema.relationship.indexExists`
- `apoc.schema.nodes`
- `apoc.schema.relationships`

Neptune openCypher does support retrieving similar values to those that the procedures
do, as shown below, but can run into performance issues on larger graphs as doing so requires
scanning a large portion of the graph to return the answer.

```
# openCypher replacement for apoc.schema.properties.distinct
MATCH (n:airport)
RETURN DISTINCT n.runways
```

```
# openCypher replacement for apoc.schema.properties.distinctCount
MATCH (n:airport)
RETURN DISTINCT n.runways, count(n.runways)
```

### Alternatives to `apoc.do` procedures

These procedures are used to provide conditional query execution that is easy to
implement using other openCypher clauses. In Neptune there are at least two ways
to achieve similar behavior:

- One way is to combine openCypher's List Comprehension
  capabilities with the `UNWIND` clause.
- Another way is to use the choose() and coalesce() steps in Gremlin.

Examples of these approaches are shown below.

#### Alternatives to apoc.do.when

```
# Neo4J Example
MATCH (n:airport {region: 'US-AK'})
CALL apoc.do.when(
 n.runways>=3,
 'SET n.is_large_airport=true RETURN n',
 'SET n.is_large_airport=false RETURN n',
 {n:n}
) YIELD value
WITH collect(value.n) as airports
RETURN size([a in airports where a.is_large_airport]) as large_airport_count,
size([a in airports where NOT a.is_large_airport]) as small_airport_count


# Neptune openCypher
MATCH (n:airport {region: 'US-AK'})
WITH n.region as region, collect(n) as airports
WITH [a IN airports where a.runways >= 3] as large_airports,
[a IN airports where a.runways < 3] as small_airports, airports
UNWIND large_airports as la
SET la.is_large_airport=true
WITH DISTINCT small_airports, airports
UNWIND small_airports as la
    SET la.small_airports=true
WITH DISTINCT airports
RETURN size([a in airports where a.is_large_airport]) as large_airport_count,
size([a in airports where NOT a.is_large_airport]) as small_airport_count

#Neptune Gremlin using choose()
g.V().
  has('airport', 'region', 'US-AK').
  choose(
    values('runways').is(lt(3)),
    property(single, 'is_large_airport', false),
    property(single, 'is_large_airport', true)).
  fold().
  project('large_airport_count', 'small_airport_count').
    by(unfold().has('is_large_airport', true).count()).
    by(unfold().has('is_large_airport', false).count())

 #Neptune Gremlin using coalesce()
g.V().
  has('airport', 'region', 'US-AK').
  coalesce(
    where(values('runways').is(lt(3))).
    property(single, 'is_large_airport', false),
    property(single, 'is_large_airport', true)).
  fold().
  project('large_airport_count', 'small_airport_count').
    by(unfold().has('is_large_airport', true).count()).
    by(unfold().has('is_large_airport', false).count())
```

#### Alternatives to apoc.do.case

```
# Neo4J Example
MATCH (n:airport {region: 'US-AK'})
CALL apoc.case([
 n.runways=1, 'RETURN "Has one runway" as b',
 n.runways=2, 'RETURN "Has two runways" as b'
 ],
 'RETURN "Has more than 2 runways" as b'
) YIELD value
RETURN {type: value.b,airport: n}

# Neptune openCypher
MATCH (n:airport {region: 'US-AK'})
WITH n.region as region, collect(n) as airports
WITH [a IN airports where a.runways =1] as single_runway,
[a IN airports where a.runways =2] as double_runway,
[a IN airports where a.runways >2] as many_runway
UNWIND single_runway as sr
    WITH {type: "Has one runway",airport: sr} as res, double_runway, many_runway
WITH DISTINCT double_runway as double_runway, collect(res) as res, many_runway
UNWIND double_runway as dr
    WITH {type: "Has two runways",airport: dr} as two_runways, res, many_runway
WITH collect(two_runways)+res as res, many_runway
UNWIND many_runway as mr
    WITH {type: "Has more than 2 runways",airport: mr} as res2, res, many_runway
WITH collect(res2)+res as res
UNWIND res as r
RETURN r

#Neptune Gremlin using choose()
g.V().
  has('airport', 'region', 'US-AK').
  project('type', 'airport').
    by(
      choose(values('runways')).
        option(1, constant("Has one runway")).
        option(2, constant("Has two runways")).
        option(none, constant("Has more than 2 runways"))).
    by(elementMap())

 #Neptune Gremlin using coalesce()
 g.V().
  has('airport', 'region', 'US-AK').
  project('type', 'airport').
    by(
      coalesce(
        has('runways', 1).constant("Has one runway"),
        has('runways', 2).constant("Has two runways"),
        constant("Has more than 2 runways"))).
    by(elementMap())
```

## Alternatives to List-based properties

Neptune does not currently support storing List-based properties. However, similar
results can be obtained by storing list values as a comma separated string and then using
the `join()` and `split()` functions to construct and deconstruct
the list property.

For example, if we wanted to save a list of tags as a property, we could use
the example rewrite which shows how to retrieve a comma separated property and
then use the `split()` and `join()` functions with List
Comprehension to achieve comparable results:

```
# Neo4j Example (In this example, tags is a durable list of string.
MATCH (person:person {name: "TeeMan"})
WITH person, [tag in person.tags WHERE NOT (tag IN ['test1', 'test2', 'test3'])] AS newTags
SET person.tags = newTags
RETURN person

# Neptune openCypher
MATCH (person:person {name: "TeeMan"})
WITH person, [tag in split(person.tags, ',') WHERE NOT (tag IN ['test1', 'test2', 'test3'])] AS newTags
SET person.tags = join(newTags,',')
RETURN person
```

## Rewriting CALL subqueries

Neptune `CALL` subqueries do not support the syntax `CALL (friend) { ... }` for importing
variables into the subquery scope (`friend`, in this example). Please use the `WITH` clause
inside the subquery for the same, e.g., `CALL { WITH friend ... }`.

Optional `CALL` subqueries are not supported at this moment.

## Other differences between Neptune openCypher and Cypher

- Neptune only supports TCP connections for the Bolt protocol. WebSockets
  connections for Bolt are not supported.
- Neptune openCypher removes whitespace as defined by Unicode
  in the `trim()`, `ltrim()` and `rtrim()`
  functions.
- In Neptune openCypher, `tostring(`double`)`
  does not automatically switch to E notation for large values of the double.
