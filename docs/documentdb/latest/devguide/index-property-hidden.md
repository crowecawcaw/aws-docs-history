# Index property: hidden

Amazon DocumentDB supports the `hidden` index property beginning with Amazon DocumentDB 8.0.1.

Hidden indexes are not visible to the query planner and cannot be used to support a query. By hiding an index from the planner, you can evaluate the potential impact of dropping the index without actually dropping it. If the impact is negative, you can unhide the index instead of having to recreate a dropped index.

The `hidden` property is supported on all index types, including single field, compound, multikey, text, geospatial, and vector indexes.

## Behavior

Apart from being hidden from the planner, hidden indexes are fully maintained and enforced. For example:

- If a hidden index is a unique index, the index still applies its unique constraint to documents.
- If a hidden index is a TTL index, the index still expires documents.
- Hidden indexes are included in `listIndexes` and `db.collection.getIndexes()` results.
- Hidden indexes are updated on write operations to the collection and continue to consume disk space and memory. As a result, they are included in statistics operations such as `db.collection.stats()` and `$indexStats`.
- Hiding an unhidden index, or unhiding a hidden index, resets its `$indexStats`. Hiding an already hidden index, or unhiding an already unhidden index, does not reset `$indexStats`.

## Restrictions

- You cannot hide the `_id` index.
- You cannot use `cursor.hint()` to force the use of a hidden index.
- `$merge` fails if the required unique index on the `on` fields is hidden. Make the index visible before running `$merge`.

## Examples

### Create a hidden index

To create an index in the hidden state, use the `db.collection.createIndex()` method and set the `hidden` option to `true` in the index definition.

For example, the following operation creates a hidden ascending index on the `productId` field:

```
db.collection.createIndex(
  { "productId": 1 },
  { "name": "productId_1", "hidden": true }
)
```

To verify, run `db.collection.getIndexes()` or `listIndexes` on the collection. A hidden index includes `"hidden": true` in its definition.

```
db.collection.getIndexes()
[
  {
    "v": 4,
    "key": { "_id": 1 },
    "name": "_id_"
  },
  {
    "v": 4,
    "key": { "productId": 1 },
    "name": "productId_1",
    "hidden": true
  }
]
```

The index option `hidden` is only returned if the value is `true`.

### Hide an existing index

Use the `collMod` command to hide an existing index. Identify the index either by its `name` or by its `keyPattern`, and set `hidden` to `true`.

The following example hides an index by name.

```
db.runCommand({
  collMod: "collection",
  index: {
    name: "productId_1", // Specify the index name
    hidden: true
  }
})
```

You can also identify the index by its key pattern.

```
db.runCommand({
  collMod: "collection",
  index: {
    keyPattern: { productId: 1 }, // Specify the index key specification document
    hidden: true
  }
})
```

### Unhide an existing index

To make a hidden index visible again, use the `collMod` command with `hidden` set to `false`.

```
db.runCommand({
  collMod: "collection",
  index: { name: "productId_1", hidden: false }
})
```

Because indexes are fully maintained while hidden, the index is immediately available for use once unhidden.
