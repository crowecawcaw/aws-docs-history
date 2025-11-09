# AWS IoT TwinMaker knowledge graph additional

resources

This section provides basic examples of the PartiQL syntax used to write queries in the
knowledge graph, as well as links to PartiQL documentation that provide information on
the knowledge graph data model.

- [PartiQL graph data model documentation](https://partiql.org/gpml/graph_model.html "https://partiql.org/gpml/graph_model.html")
- [PartiQL graph query documentation](https://partiql.org/gpml/graph_query.html "https://partiql.org/gpml/graph_query.html")
  This set of examples shows basic queries with their responses. Use this as a reference to
  write your own queries.

**Basic queries**

- **Get all entities with a filter**

```
SELECT entity
FROM EntityGraph MATCH (entity)
WHERE entity.entityName = 'room_0'
```

This query returns all the entities in a workspace with the name
`room_0`.

`FROM` clause: `EntityGraph` is the
graph collection that contains all the entities and their
relationships in a workspace. This collection is automatically
created and managed by AWS IoT TwinMaker based on the entities in your
workspace.

`MATCH` clause: specifies a pattern that matches a
portion of the graph. In this case, the pattern `(entity)`
matches every node in the graph and is bound to the entity variable.
The `FROM` clause must be followed by the
`MATCH` clause.

`WHERE` clause: specifies a filter on the `entityName`
field of the node, where the value must match `room_0`.

`SELECT` clause: specifies the `entity` variable
so the whole entity node is returned.

**Response:**

```
{
  "columnDescriptions": [
    {
      "name": "entity",
      "type": "NODE"
    }
  ],
  "rows": [
    {
      "rowData": [
        {
          "arn": "arn:aws:iottwinmaker:us-east-1: 577476956029: workspace / SmartBuilding8292022 / entity / room_18f3ef90 - 7197 - 53 d1 - abab - db9c9ad02781 ",
          "creationDate": 1661811123914,
          "entityId": "room_18f3ef90-7197-53d1-abab-db9c9ad02781",
          "entityName": "room_0",
          "lastUpdateDate": 1661811125072,
          "workspaceId": "SmartBuilding8292022",
          "description": "",
          "components": [
            {
              "componentName": "RoomComponent",
              "componentTypeId": "com.example.query.construction.room",
              "properties": [
                {
                  "propertyName": "roomFunction",
                  "propertyValue": "meeting"
                },
                {
                  "propertyName": "roomNumber",
                  "propertyValue": 0
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

The `columnDescriptions` returns metadata about the
column, such as the name and type. The type returned is `NODE`.
This indicates that the whole node has been returned. Other values for
the type can be `EDGE` which would indicate a relationship or
`VALUE` which would indicate a scalar value such as an integer
or string.

The `rows` returns a list of rows. As only one entity
was matched, one `rowData` is returned which contains all
the fields in an entity.

###### Note

Unlike SQL where you can only return scalar values, you can
return an object (as JSON) using PartiQL.

Each node contains all the entity-level fields such as `entityId`,
`arn` and `components`, component-level fields such as
`componentName`, `componentTypeId` and `properties`
as well as property-level fields such as `propertyName` and
`propertyValue`, all as a nested JSON.

- **Get all relationships with a filter**:

```
SELECT relationship
FROM EntityGraph MATCH (e1)-[relationship]->(e2)
WHERE relationship.relationshipName = 'isLocationOf'
```

This query returns all the relationships in a workspace with
relationship name `isLocationOf`.

The `MATCH` clause: specifies a pattern that matches two
nodes (indicated by `()`) that are connected by a
directed edge (indicated by `-[]->`) and bound to a variable
called `relationship`.

The `WHERE` clause: specifies a filter on the
`relationshipName` field of the edge, where the value
is `isLocationOf`.

The `SELECT` clause: specifies the relationship
variable so the whole edge node is returned.

**Response**

```
{
    "columnDescriptions": [{
        "name": "relationship",
        "type": "EDGE"
    }],
    "rows": [{
        "rowData": [{
            "relationshipName": "isLocationOf",
            "sourceEntityId": "floor_83faea7a-ea3b-56b7-8e22-562f0cf90c5a",
            "targetEntityId": "building_4ec7f9e9-e67e-543f-9d1b- 235df7e3f6a8",
            "sourceComponentName": "FloorComponent",
            "sourceComponentTypeId": "com.example.query.construction.floor"
        }]
    },
        ... //rest of the rows are omitted
    ]
}
```

The type of the column in `columnDescriptions` is an
`EDGE`.

Each `rowData` represents an edge with fields like
`relationshipName`. This is the same as the relationship
property name defined on the entity. The `sourceEntityId`,
`sourceComponentName` and `sourceComponentTypeId`
give information about which entity and component the relationship property
was defined on. The `targetEntityId` specifies which entity this
relationship is pointing towards.

- **Get all entities with a specific relationship to a
  specific entity**

```
SELECT e2.entityName
      FROM EntityGraph MATCH (e1)-[r]->(e2)
      WHERE relationship.relationshipName = 'isLocationOf'
      AND e1.entityName = 'room_0'
```

This query returns all the entity names of all entities that have
an `isLocationOf` relationship with the `room_0`
entity.

The `MATCH` clause: specifies a pattern that matches any two nodes
(`e1`, `e2`) that have a directed edge
(`r`).

The `WHERE` clause: specifies a filter on the
relationship name and source entity’s name.

The `SELECT` clause: returns the `entityName`
field in the `e2` node.

**Response**

```
{
  "columnDescriptions": [
    {
       "name": "entityName",
       "type": "VALUE"
    }
  ],
   "rows": [
    {
       "rowData": [
         "floor_0"
      ]
    }
  ]
}
```

In the columnDescriptions, the type of the column is
`VALUE` since `entityName` is a string.

One entity, `floor_0`, is returned.

**MATCH**

The following patterns are supported in a `MATCH` clause:

- Match node 'b' pointing to node 'a':

```
FROM EntityGraph MATCH (a)-[rel]-(b)
```

- Match node 'a' pointing to node 'b':

```
FROM EntityGraph MATCH (a)-[]->(b)
```

There is no variable bound to a relationship assuming a filter
doesn’t need to be specified on the relationship.

- Match node 'a' pointing to node 'b' and node 'b' pointing to node
  'a':

```
FROM EntityGraph MATCH (a)-[rel]-(b)
```

This will return two matches: one from 'a' to 'b' and another from 'b'
to 'a', so the recommendation is to use directed edges wherever
possible.

- The relationship name is also a label of the property graph
  `EntityGraph`, so you can simply specify the relationship name
  following a colon (:) instead of specifying a filter on
  `rel.relationshipName` in the `WHERE` clause.

```
FROM EntityGraph MATCH (a)-[:isLocationOf]-(b)
```

- Chaining: patterns can be chained to match on multiple
  relationships.

```
FROM EntityGraph MATCH (a)-[rel1]->(b)-[rel2]-(c)
```

- Variable hop patterns can span multiple nodes and edges as
  well:

```
FROM EntityGraph MATCH (a)-[]->{1,5}(b)
```

This query matches any pattern with outgoing edges from node 'a'
within 1 to 5 hops. The allowed quantifiers are:

`{m,n}` - between m and n repetitions

`{m,}` - m or more repetitions.

**FROM**:

An entity node can contain nested data, such as components which themselves
contain further nested data such as properties. These can be accessed by
unnesting the result of the MATCH pattern.

```
SELECT e
FROM EntityGraph MATCH (e), e.components AS c, c.properties AS p
WHERE c.componentTypeId = 'com.example.query.construction.room',
AND p.propertyName = 'roomFunction'
AND p.propertyValue = 'meeting'
```

Access nested fields by dotting `.` into a variable. A comma
(,) is used to unnest (or join) entities with the components
inside and then the properties inside those components. `AS` is
used to bind a variable to the unnested variables so that they can be used
in the `WHERE` or `SELECT` clauses. This query returns
all entities that contains a property named `roomFunction` with
value `meeting` in a component with component type id
`com.example.query.construction.room`

To access multiple nested fields of a field such as multiple components in
an entity, use the comma notation to do a join.

```
SELECT e
FROM EntityGraph MATCH (e), e.components AS c1, e.components AS c2
```

**SELECT**:

- Return a node:

```
SELECT e
FROM EntityGraph MATCH (e)
```

- Return an edge:

```
SELECT r
FROM EntityGraph MATCH (e1)-[r]->(e2)
```

- Return a scalar value:

```
SELECT floor.entityName, room.description, p.propertyValue AS roomfunction
FROM EntityGraph MATCH (floor)-[:isLocationOf]-(room),
room.components AS c, c.properties AS p
```

Format the name of the output field by aliasing it using
`AS`. Here, instead of `propertyValue` as
column name in the response, `roomfunction` is
returned.

- Return aliases:

```
SELECT floor.entityName AS floorName, luminaire.entityName as luminaireName
FROM EntityGraph MATCH (floor)-[:isLocationOf]-(room)-[:hasPart]-
(lightingZone)-[:feed]-(luminaire)
WHERE floor.entityName = 'floor_0'
AND luminaire.entityName like 'lumin%'
```

Using aliases is highly recommended to be explicit, increase
readability, and avoid any ambiguities in your queries.

**WHERE**:

- The supported logical operators are `AND`,
  `NOT`, and `OR`.
- The supported comparison operators are `<`,
  `<=`, `>`, `=>`,`=`,
  and `!=`.
- Use the `IN` keyword if you want to specify multiple
  `OR` conditions on the same field.
- Filter on an entity, component or property field:

```
FROM EntityGraph MATCH (e), e.components AS c, c.properties AS p
WHERE e.entityName = 'room_0'
AND c.componentTypeId = 'com.example.query.construction.room',
AND p.propertyName = 'roomFunction'
AND NOT p.propertyValue = 'meeting'
OR p.propertyValue = 'office'
```

- Filter on the `configuration` property. Here
  `unit` is the key in the configuration map and
  `Celsius` is the value.

```
WHERE p.definition.configuration.unit = 'Celsius'
```

- Check if a map property contains a given key and value:

```
WHERE p.propertyValue.length = 20.0
```

- Check if a map property contains a given key:

```
WHERE NOT p.propertyValue.length IS MISSING
```

- Check if a list property contains a given value:

```
WHERE 10.0 IN p.propertyValue
```

- Use the `lower()` function for case insensitive
  comparisons. By default, all comparisons are case sensitive.

```
WHERE lower(p.propertyValue) = 'meeting'
```

**LIKE**:

Useful if you do not know the exact value for a field and can perform full
text search on the specified field. `%` represents zero or
more.

```
WHERE e.entityName LIKE '%room%'
```

- Infix search: `%room%`
- Prefix search: `room%`
- Suffix search: `%room`
- If you have '%' in your values, then put an escape character in the
  `LIKE` and specify the escape character with `ESCAPE`.

```
WHERE e.entityName LIKE 'room\%' ESCAPE '\'
```

**DISTINCT**:

```
SELECT DISTINCT c.componentTypeId
FROM EntityGraph MATCH (e), e.components AS c
```

- The `DISTINCT` keyword eliminates duplicates from the
  final result.

`DISTINCT` is not supported on complex data types.

**COUNT**

```
SELECT COUNT(e), COUNT(c.componentTypeId)
FROM EntityGraph MATCH (e), e.components AS c
```

- The `COUNT` keyword computes the number of items in a query result.
- `COUNT` is not supported on nested complex fields and graph pattern fields.
- `COUNT` aggregation is not supported with `DISTINCT` and nested queries.

For example, `COUNT(DISTINCT e.entityId)` is not supported.

**PATH**

The following pattern projections are supported in querying using path projection:

- Variable hop queries

```
SELECT p FROM EntityGraph MATCH p = (a)-[]->{1, 3}(b)
```

This query matches and projects nodes metadata of any patterns with outgoing edges from node _a_ within 1 to 3 hops.

- Fixed hop queries

```
SELECT p FROM EntityGraph MATCH p = (a)-[]->(b)<-[]-(c)
```

This query matches and projects metadata of entities and incoming edges to _b_.

- Undirected queries

```
SELECT p FROM EntityGraph MATCH p = (a)-[]-(b)-[]-(c)
```

This query matches and projects the metadata of nodes in 1 hop patterns connecting _a_ and _c_ via _b_.

```
{
    "columnDescriptions": [
        {
            "name": "path",
            "type": "PATH"
        }
    ],
    "rows": [
        {
            "rowData": [
                {
                    "path": [
                        {
                            "entityId": "a",
                            "entityName": "a"
                        },
                        {
                            "relationshipName": "a-to-b-relation",
                            "sourceEntityId": "a",
                            "targetEntityId": "b"
                        },
                        {
                            "entityId": "b",
                            "entityName": "b"
                        }
                    ]
                }
            ]
        },
        {
            "rowData": [
                {
                    "path": [
                        {
                            "entityId": "b",
                            "entityName": "b"
                        },
                        {
                            "relationshipName": "b-to-c-relation",
                            "sourceEntityId": "b",
                            "targetEntityId": "c"
                        },
                        {
                            "entityId": "c",
                            "entityName": "c"
                        }
                    ]
                }
            ]
        }
    ]
}
```

This `PATH` query response comprises of only metadata that identifies all the nodes and edges of each path/pattern between _a_ and _c_ via _b_.

**LIMIT** and **OFFSET**:

```
SELECT e.entityName
FROM EntityGraph MATCH (e)
WHERE e.entityName LIKE 'room_%'
LIMIT 10
OFFSET 5
```

`LIMIT` specifies the number of results to be returned in the
query, and `OFFSET` specifies the number of results to
skip.

**LIMIT** and **maxResults**:

The following example shows a query that returns 500 results in total, but only
displays 50 at a time per API call. This pattern can be used where you
need to limit the amount of displayed results, for example if you are only able to
display 50 results in a UI.

```
aws iottwinmaker execute-query \
--workspace-id exampleWorkspace \
--query-statement "SELECT e FROM EntityGraph MATCH (e) LIMIT 500"\
--max-results 50
```

- The `LIMIT` keyword affects the query and limits the resulting
  rows. If you need to control the number of results returned per API call
  without limiting the total number of returned results, use `LIMIT`.
- `max-results` is an optional parameter for
  the [ExecuteQuery
  API action](../apireference/API_ExecuteQuery.md "../apireference/API_ExecuteQuery.md"). `max-results` only applies to the API and
  how results are read within the bounds of the above query.

Using `max-results` in a query allows you to reduce the number
of displayed results without limiting the actual number of returned results.

The query below iterates through the next page of results. This query uses the
`ExecuteQuery` API call to return rows 51-100, where the next page of
results is specified by the `next-token`– in this case the token
is: `"H7kyGmvK376L"`.

```
aws iottwinmaker execute-query \
--workspace-id exampleWorkspace \
--query-statement "SELECT e FROM EntityGraph MATCH (e) LIMIT 500"\
--max-results 50
--next-token "H7kyGmvK376L"
```

- The `next-token` string specifies the next page of results.
  For more information, see the [ExecuteQuery](../apireference/API_ExecuteQuery.md#API_ExecuteQuery_RequestSyntax "../apireference/API_ExecuteQuery.md#API_ExecuteQuery_RequestSyntax") API action.

AWS IoT TwinMaker knowledge graph query has the following limits:

| Limit Name                                                                         | Quota      | Adjustable |
| ---------------------------------------------------------------------------------- | ---------- | ---------- |
| Query execution timeout                                                            | 10 seconds | No         |
| Maximum number of hops                                                             | 10         | Yes        |
| Maximum number of self `JOIN`s                                                     | 20         | Yes        |
| Maximum number of projected fields                                                 | 20         | Yes        |
| Maximum number of conditional expressions (`AND`,<br>`OR`, `NOT`)                  | 10         | Yes        |
| Maximum length of a `LIKE` expression pattern (including<br>wildcards and escapes) | 20         | Yes        |
| Maximum number of items that can be specified in an `IN` clause                    | 10         | Yes        |
| Maximum value for `OFFSET`                                                         | 3000       | Yes        |
| Maximum value for `LIMIT`                                                          | 3000       | Yes        |
| Maximum value for traversals (`OFFSET` + `LIMIT`)                                  | 3000       | Yes        |
