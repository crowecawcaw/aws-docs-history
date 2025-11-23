# .vectors.topK.byEmbedding algorithm

The `.vectors.topKByEmbedding` algorithm finds the `topK`
nearest neighbors of an embedding based on the distance of their vector embeddings.

## `.vectors.topK.byEmbedding`  syntax

```
CALL neptune.algo.vectors.topK.byEmbedding(
    {
        embedding: [*an embedding*] (required),
        topK: the number of result nodes to return (optional, default: 10),
        vertexFilter: a json structure that encodes vertex label or property filters (optional, default: empty),
        concurrency: the number of cores to use to run the algorithm (optional, default: 0)
    }
)
YIELD node, score
RETURN node, score
```

## `.vectors.topK.byEmbedding`  input

- **embedding**   _(required)_
  _type:_ float[] or double[].

The input embedding to use to compute the distance to the embeddings of the candidate target nodes.
The dimension of the embedding must match the declared dimension of the associated vector index.

The embedding may or may not exist in the database. If not, it can be any vector of the same dimension
as is declared in the associated vector index. Note that the input embedding must be static, aka, the input
embedding can't be the output of another query.

- **topK**   _(optional)_  
  _type:_ a positive integer;   _default:_ 10.

The number of result nodes to return.

- **vertexFilter**   _(optional)_  
  _type:_ a json string   _default:_ empty.

The vertexFilter is a json structure encoding filters to use on the vertex labels and properties during
computation. In it, there are two operation types: a joiner operation and a single operation. A joiner operation
includes andAll and orAll , which is an array of joiner and/or single operations. A single operation includes the
rest of the filters. A vertex filter can be used for either vertex labels or vertex properties or a combination of
both. Among the single operations, only equals and notEquals support vertex label filtering. The details of all the
operations are as follows:

    + *andAll:* Nodes are returned if their properties fulfill all the filter conditions inside this
     list. It is an array of joiner and/or single operations. It must contain minimum two items.




     Example: {andAll: [{equals:{property: “~label”, value: “Airport”}}, {greaterThan:{property: “runways”, value: 3}}]} →
     the Airport vertices that have more than 3 runways.
    + *orAll:* Nodes are returned if their properties fulfill all the filter conditions inside this list.
     It is an array of joiner and/or single operations. It must contain minimum two items.




     Example: {orAll: [{equals:{property: “dist”, value: 10}}, {notEquals:{property: “runways”, value: “2”}}]} → the vertices
     whose dist is equals to 10 or whose runways is not equal to 2.
    + *equals:* Nodes are returned if they contain a property whose name matches the property and whose value
     matches the value, or they have the vertex label whose label name matches the value.




     The property must be a string. It can either be a vertex property name or ~label.




     The value can be boolean, numeric or string if the property is a vertex property. The value can only be string if the
     property is ~label.




     Example for vertex property: {equals:{property: “dist”, value: 10}}




     Example for vertex label: {equals:{property: “~label”, value: “Person”}}
    + *notEquals:* Nodes are returned if they contain a property whose name matches the property and whose
     value doesn’t match the value , or they have the vertex label whose label name doesn’t match the value.




     The property must be a string. It can either be a vertex property name or ~label.




     The value can be boolean, numeric or string if the property is a vertex property. The value can only be string if the
     property is ~label.




     Example for vertex property: {notEquals:{property: “dist”, value: 10}}




     Example for vertex label: {notEquals:{property: “~label”, value: “Person”}}
    + *greaterThan:* Nodes are returned if they contain a property whose name matches the property and whose
     value is greater than the value. The value must be numeric.




     Example: {greaterThan:{property: “dist”, value: 10}}
    + *greaterThanOrEquals:* Nodes are returned if they contain a property whose name matches the property and
     whose value is greater than or equal to the value. The value must be numeric.
    + *lessThan:* Nodes are returned if they contain a property whose name matches the property and whose value
     is less than the value. The value must be numeric.




     Example: {lessThan:{property: “dist”, value: 10}}
    + *lessThanOrEquals:* Nodes are returned if they contain a property whose name matches the property and whose
     value is less than or equal to the value. The value must be numeric.




     Example: {lessThanOrEquals:{property: “dist”, value: 10}}
    + *in:* Nodes are returned if they contain a property whose name matches the property and whose value is in the
     specified value list, or they have the vertex label whose label name matches the values in the value list.




     The property must be a string. It can either be a vertex property name or ~label.




     The value list can be a mix list of booleans, numbers or strings if the property is a vertex property. The value can only be a
     list of strings if the property is ~label.




     Example for vertex property: {in:{property: “country”, value: [“US”, “UK”]}}




     Example for vertex label: {in:{property: “~label”, value: [“US”, “UK”]}}
    + *notIn:* Nodes are returned if they contain a property whose name matches the property and whose value is
     not in the specified value list, or they have the vertex label whose label name does not match the values in the value list.




     The property must be a string. It can either be a vertex property name or ~label.




     The value list can be a mix list of booleans, numbers or strings if the property is a vertex property. The value can only be
     a list of strings if the property is ~label.




     Example for vertex property: {in:{property: “country”, value: [“US”, “UK”]}}




     Example for vertex label: {in:{property: “~label”, value: [“US”, “UK”]}}
    + *startsWith:* Nodes are returned if they contain a property whose name matches the property and whose value
     starts with the value. The value must be a string.




     Example: {startsWith:{property: “country”, value “U”}}
    + *stringContains:* Nodes are returned if they contain a property whose name matches the property and whose value
     is one of the following:




     A string that contains the value as a substring. The following example would return data sources with an animal property that contains
     the substring at (for example cat).




     Example: {stringContains: { property: "animal", value: "at" }}

- **concurrency**   _(optional)_   –  
  _type:_ 0 or 1;   _default:_ 0.

Controls the number of concurrent threads used to run the algorithm.

If set to `0`, uses all available threads to complete execution of the individual algorithm
invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
of many algorithms concurrently.

## `.vectors.topK.byEmbedding`  outputs

For each node returned:

- **node**   –  
  A node whose embedding is at one of the `topK` nearest distances from
  the input embedding.
- **score**   –  
  The distance between the input embedding and the embedding of this node.

## `.vectors.topK.byEmbedding`  query example

```
CALL neptune.algo.vectors.topK.byEmbedding(
  {
    embedding: [0.1, 0.2, 0.3, ...],
    topK: 3,
    concurrency: 1
  }
)
YIELD node, score
RETURN node, score
```

###### Warning

Using `MATCH (n)` or `WITH` as the prefix of `CALL neptune.algo.vectors.topK.byEmbedding` is forbidden.
MATCH(n) can return a large number of nodes. Keep in mind that every node in (n) invokes a separate run of
.vectors.topK.byEmbedding. Too many inputs can therefore result in very long runtimes and many outputs.

## Sample  `.vectors.topKByEmbedding`  output

Here is an example of the output returned by .vectors.topK.byEmbedding when run against the sample Wikipedia dataset using
the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "CALL neptune.algo.vectors.topK.byEmbedding({ embedding: [*an embedding*], topK: 3 })
                       YIELD node, score
                       RETURN node, score"
  --language open_cypher \
  /tmp/out.txt
{
  "results": [
    {
      "node": {
        "~id": "0",
        "~entityType": "node",
        "~labels": [],
        "~properties": {
          "title": "24-hour clock",
          "views": 2450.62548828125,
          "wiki_id": 9985,
          "paragraph_id": 0,
          "url": "https://simple.wikipedia.org/wiki?curid=9985",
          "langs": 30,
          "text": "The 24-hour clock is a way of telling the time in which the day runs from midnight to midnight and is divided into 24 hours\\, numbered from 0 to 23. It does not use a.m. or p.m. This system is also referred to (only in the US and the English speaking parts of Canada) as military time or (only in the United Kingdom and now very rarely) as continental time. In some parts of the world\\, it is called railway time. Also\\, the international standard notation of time (ISO 8601) is based on this format."
        }
      },
      "score": 0.0
    },
    {
      "node": {
        "~id": "2",
        "~entityType": "node",
        "~labels": [],
        "~properties": {
          "title": "24-hour clock",
          "views": 2450.62548828125,
          "wiki_id": 9985,
          "paragraph_id": 2,
          "url": "https://simple.wikipedia.org/wiki?curid=9985",
          "langs": 30,
          "text": "However\\, the US military prefers not to say 24:00 - they do not like to have two names for the same thing\\, so they always say \"23:59\"\\, which is one minute before midnight."
        }
      },
      "score": 24.000200271606447
    },
    {
      "node": {
        "~id": "3",
        "~entityType": "node",
        "~labels": [],
        "~properties": {
          "title": "24-hour clock",
          "views": 2450.62548828125,
          "wiki_id": 9985,
          "paragraph_id": 3,
          "url": "https://simple.wikipedia.org/wiki?curid=9985",
          "langs": 30,
          "text": "24-hour clock time is used in computers\\, military\\, public safety\\, and transport. In many Asian\\, European and Latin American countries people use it to write the time. Many European people use it in speaking."
        }
      },
      "score": 25.013729095458986
    }
  ]
}
```
