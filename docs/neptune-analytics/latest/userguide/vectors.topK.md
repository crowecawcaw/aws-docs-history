# .vectors.topK.byNode algorithm

The `.vectors.topK.byNode` algorithm finds the `topK` nearest
neighbors of a node based on the distance of their vector embeddings from the node.

## `.vectors.topK.byNode`  syntax

```
CALL neptune.algo.vectors.topK.byNode(
  [`a list of one or more nodes (required`)],
  {
    topK: `the number of result nodes to return (optional, default: 10)`,
    concurrency: `the number of cores to use to run the algorithm (optional)`
  }
)
YIELD node, score
RETURN node, score
```

## `.vectors.topK.byNode`  input

- **a list of one or more source nodes**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`.

If the source-node list is empty then the query result is also empty.

- **topK**   _(optional)_  
  _type:_ a positive integer;   _default:_ 10.

The number of result nodes to return.

- **concurrency**   _(optional)_   –  
  _type:_ 0 or 1;   _default:_ 0.

Controls the number of concurrent threads used to run the algorithm.

If set to `0`, uses all available threads to complete execution of the individual algorithm
invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
of many algorithms concurrently.

## `.vectors.topK.byNode`  outputs

For each source node:

- **source**   –  
  The source node.
- **node**   –  
  A node whose embedding is at one of the `topK` nearest distances from
  the source node's embedding.
- **score**   –  
  The distance between the source node's embedding and the embedding of the close node.

## `.vectors.topK.byNode`  query example

```
MATCH ( n:airport {code: 'ANC'} )
CALL neptune.algo.vectors.topK.byNode(
  n,
  {
    topK: 10,
    concurrency: 1
  }
)
YIELD node, score
RETURN n, node, score
```

###### Warning

In queries like the one above, be careful to limit `MATCH(n)`
so that it doesn't return a large number of nodes. Keep in mind that every node in `n`
invokes a separate run of `.vectors.topK.byNode`.
Too many inputs can therefore result in very long runtimes. Use `LIMIT` or
put conditions on the `MATCH` clause to restrict its output appropriately.

## Sample  `.vectors.topK.byNode`  output

Here is an example of the output returned by `.vectors.topK.byNode` when run against
the sample
Wikipedia dataset using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH ( n {`~id`: '0'} )
                       CALL neptune.algo.vectors.topK.byNode(n, {topK: 3})
                       YIELD node, score
                       RETURN n, node, score" \
  --language open_cypher \
  /tmp/out.txt
{
  "results": [
    {
      "n": {
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
      "n": {
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
      "n": {
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
