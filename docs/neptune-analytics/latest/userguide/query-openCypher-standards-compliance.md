# Neptune Analytics OpenCypher specification compliance

Refer to the Neptune Database documentation found [here](../../../neptune/latest/userguide/feature-opencypher-compliance.md "../../../neptune/latest/userguide/feature-opencypher-compliance.md") for openCypher specification compliance,
with the exception that Neptune Analytics does not support custom edge IDs.

Amazon Neptune also supports several features beyond the scope of the OpenCypher specification. Refer to
[OpenCypher extensions in Amazon Neptune](../../../neptune/latest/userguide/access-graph-opencypher-extensions.md "../../../neptune/latest/userguide/access-graph-opencypher-extensions.md") for details.

### Vertex and edge IDs

**Custom IDs for vertices**

Neptune Analytics supports both querying and creating vertices with custom IDs. See [openCypher custom IDs](../../../neptune/latest/userguide/feature-opencypher-compliance.md#opencypher-compliance-custom-ids "../../../neptune/latest/userguide/feature-opencypher-compliance.md#opencypher-compliance-custom-ids") for more details.

**Custom IDs for edges**

Neptune Analytics does not support edge creation with custom edge IDs. Custom IDs are not permitted in CREATE or MERGE
clauses. Edges are assigned IDs by Neptune , using a reserved prefix `neptune_reserved_`.
Edges can be queried by the server assigned ids, just as in [Neptune Database](../../../neptune/latest/userguide/feature-opencypher-compliance.md#opencypher-compliance-custom-ids "../../../neptune/latest/userguide/feature-opencypher-compliance.md#opencypher-compliance-custom-ids").

```
# Supported
MATCH (n)-[r:knows {`~id`: 'neptune_reserved_1_123456789'}]->(m)
RETURN r

# Unsupported
CREATE (n:Person {name: 'John'})-[:knows {`~id`: 'john-knows->jim'}]->(m:Person {name: 'Jim'})

# Unsupported
MERGE (n)-[r:knows {`~id`: 'neptune_reserved_1_123456789'}]->(m)
RETURN r
```

Server assigned IDs are recycled. After an edge is deleted, a new edge created could get assigned the same ID.

###### Note

The edges could get assigned new IDs if the graph gets restructured and the older IDs would then become
invalid. If the edges are reassigned IDs, older IDs would match no other edges. It is not recommended to
store these IDs externally for long-term querying purposes.

### IRIs and language-tagged literals

Neptune Analytics supports values hat are of type IRI or languag-tagged literal. See
[Handling RDF values](using-rdf-data.md#rdf-handling "using-rdf-data.md#rdf-handling") for
more information.

### OpenCypher reduce() function

Reduce sequentially processes each list element by combining it with a running total or ‘accumulator.’ Starting
from an initial value, it updates the accumulator after each operation and uses that updated value in the next
iteration. Once all elements have been processed, it returns the final accumulated result.

###### A typical reduce() structure

`reduce(accumulator = initial , variable IN list | expression)`

###### Type specifications:

- initial: starting value for the accumulator - (LONG | FLOAT | STRING | LIST OF (STRING, LONG, FLOAT)).
- list: the input list - LIST OF T where T matches the initial type.
- variable : represents each element in the input list.
- expression : Only supports the `+` operator.
- return : The return will be the same type as the initial type.

###### Restrictions:

The reduce() expression currently only supports addition or concatenation (string or list). Both are
represented by the `+` operator. The expression should be a binary expression specified as
accumulator + any variable.

###### Examples

The following examples show the different supported input types:

```
Long Addition:
RETURN reduce(sum = 0, n IN [1, 2, 3] | sum + n)
{
  "results": [{
      "reduce(sum = 0, n IN [1, 2, 3] | sum + n)": 6
    }]
}
```

```
String Concatenation:
RETURN reduce(str = "", x IN ["A", "B", "C"] | str + x)
{
  "results": [{
      "reduce(str = "", x IN ["A", "B", "C"] | str + x)": "ABC"
    }]
}
```

```
List Combination:
RETURN reduce(lst = [], x IN [1, 2, 3] | lst + x)
{
  "results": [{
      "reduce(lst = [], x IN [1, 2, 3] | lst + x)": [1, 2, 3]
    }]
}
```

```
Float Addition:
RETURN reduce(total = 0.0, x IN [1.5, 2.5, 3.5] | total + x)
{
  "results": [{
      "reduce(total = 0.0, x IN [1.5, 2.5, 3.5] | total + x)": 7.5
    }]
}
```
