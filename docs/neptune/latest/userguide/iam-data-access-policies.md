# Creating custom IAM policy statements to access data in Amazon Neptune

Neptune data-access policy statements use [data-access
actions](iam-dp-actions.md "iam-dp-actions.md"), [resources](iam-data-resources.md "iam-data-resources.md"), and [condition keys](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys"), all of which are preceded by
a `neptune-db:` prefix.

###### Topics

- [Using query actions in Neptune data-access
  policy statements](#iam-data-query-actions "#iam-data-query-actions")
- [IAM actions for data access in Amazon Neptune](iam-dp-actions.md "iam-dp-actions.md")
- [IAM resource types for accessing data in Amazon Neptune](iam-data-resources.md "iam-data-resources.md")
- [IAM condition keys for accessing data in Amazon Neptune](iam-data-condition-keys.md "iam-data-condition-keys.md")
- [Creating IAM data-access policies in Amazon Neptune](iam-data-access-examples.md "iam-data-access-examples.md")

## Using query actions in Neptune data-access

policy statements

There are three Neptune query actions that can be used in data-access policy
statements, namely `ReadDataViaQuery`, `WriteDataViaQuery`,
and `DeleteDataViaQuery`. A particular query may need permissions to
perform more than one of these actions, and it may not always be obvious what
combination of these actions must be permitted in order to run a query.

Before running a query, Neptune determines the permissions needed to run each
step of the query, and combines these into the full set of permissions that the query
requires. Note that this full set of permissions includes all actions that the query
_might_ perform, which is not necessarily the set of actions
that the query actually will perform when it runs over your data.

This means that to permit a given query to run, you must provide permissions
for every action that the query could possibly perform, whether or not it actually
performs them.

Here are some sample Gremlin queries where this is explained in more detail:

- ```
  g.V().count()
  ```

````

`g.V()` and `count()` only require
 read access, so the query as a whole only requires `ReadDataViaQuery`
 access.
* ```
g.addV()
````

`addV()` needs to check whether a vertex with a given ID exists
or not before inserting a new one. This means that it requires both
`ReadDataViaQuery` and `WriteDataViaQuery` access.

- ```
  g.V('1').as('a').out('created').addE('createdBy').to('a')
  ```

````

`g.V('1').as('a')` and `out('created')` only require
 read access, but `addE().from('a')` requires both read and write access
 because `addE()` needs to read the `from` and `to`
 vertices and check whether an edge with the same ID already exists before adding
 a new one. The query as a whole therefore needs both `ReadDataViaQuery`
 and `WriteDataViaQuery` access.
* ```
g.V().drop()
````

`g.V()` only requires read access. `drop()` needs
both read and delete access because it needs to read a vertex or edge before
deleting it, so the query as a whole requires both `ReadDataViaQuery`
and `DeleteDataViaQuery` access.

- ```
  g.V('1').property(single, 'key1', 'value1')
  ```

````

`g.V('1')` only requires read access, but `property(single, 'key1',
 'value1')` requires read, write, and delete access. Here, the
 `property()` step inserts the key and value if they do not already
 exist in the vertex, but if they do already exist, it deletes the existing
 property value and inserts a new value in its place. Therefore, the query
 as a whole requires `ReadDataViaQuery`, `WriteDataViaQuery`,
 and `DeleteDataViaQuery` access.


Any query that contains a `property()` step will need
 `ReadDataViaQuery`, `WriteDataViaQuery`, and
 `DeleteDataViaQuery` permissions.

Here are some openCypher examples:



* ```
MATCH (n)
RETURN n
````

This query reads all nodes in the database and returns them,
which only requires `ReadDataViaQuery` access.

- ```
  MATCH (n:Person)
  SET n.dept = 'AWS'
  ```

````

This query requires `ReadDataViaQuery`, `WriteDataViaQuery`,
 and `DeleteDataViaQuery` access. It reads all nodes with
 the label 'Person' and either adds a new property with the key `dept`
 and value `AWS` to them, or if the `dept` property already
 exists, it deletes the old value and inserts `AWS` instead. Also, if
 the value to be set is `null`, `SET` deletes the property
 altogether.


 Because the `SET` clause may in some cases need to delete an
 existing value, it **always** needs
 `DeleteDataViaQuery` permissions as well as `ReadDataViaQuery`
 and `WriteDataViaQuery` permissions.
* ```
MATCH (n:Person)
DETACH DELETE n
````

This query needs `ReadDataViaQuery` and
`DeleteDataViaQuery` permissions. It finds all the nodes with
The label `Person` and deletes them along with the edges connected
to those nodes and any associated labels and properties.

- ```
  MERGE (n:Person {name: 'John'})-[:knows]->(:Person {name: 'Peter'})
  RETURN n
  ```

```

This query needs `ReadDataViaQuery`
 and `WriteDataViaQuery` permissions. The `MERGE` clause
 either matches a specified pattern or creates it. Since, a write can occur if the
 pattern is not matched, write permissions are needed as well as read permissions.
```
