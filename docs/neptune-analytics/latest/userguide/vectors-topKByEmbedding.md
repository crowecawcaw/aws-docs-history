# .vectors.topKByEmbedding algorithm (deprecated)

The `.vectors.topKByEmbedding` algorithm finds the `topK`
nearest neighbors of an embedding based on the distance of their vector embeddings.

## `.vectors.topKByEmbedding`  syntax

```
CALL neptune.algo.vectors.topKByEmbedding(
  [`an embedding (required`)],
  {
    topK: `the number of result nodes to return (optional, default: 10)`,
    concurrency: `the number of cores to use to run the algorithm (optional)`
  }
)
YIELD embedding, node, score
RETURN embedding, node, score
```

## `.vectors.topKByEmbedding`  input

- **an embedding**   _(required)_
  _type:_ a list of floating-point values.

The source input embedding to use to compute the distance to the embeddings of
the candidate target nodes. The dimension of the embedding must match the declared
dimension of the associated vector index.

The embedding may or may not exist in the database. If not, it can be any
vector of the same dimension as is declared in the associated vector index.

- **topK**   _(optional)_  
  _type:_ a positive integer;   _default:_ 10.

The number of result nodes to return.

- **concurrency**   _(optional)_   –  
  _type:_ 0 or 1;   _default:_ 0.

Controls the number of concurrent threads used to run the algorithm.

If set to `0`, uses all available threads to complete execution of the individual algorithm
invocation. If set to `1`, uses a single thread. This can be useful when requiring the invocation
of many algorithms concurrently.

## `.vectors.topKByEmbedding`  outputs

For each node returned:

- **embedding**   –  
  The input embedding.
- **node**   –  
  A node whose embedding is at one of the `topK` nearest distances from
  the input embedding.
- **score**   –  
  The distance between the input embedding and the embedding of this node.

## `.vectors.topKByEmbedding`  query example

You can provide the embedding explicitly in the query, although embeddings tend
to be very large:

```
CALL neptune.algo.vectors.topKByEmbedding(
  [0.1, 0.2, 0.3, `...`],
  {
    topK: 7,
    concurrency: 1
  }
)
YIELD embedding, node, score
RETURN embedding, node, score
```

Most often, you will by generating embeddings to pass to the
algorithm. For example:

```
MATCH ( n:airport {code: 'ANC'} )
CALL neptune.algo.vectors.get(n) YIELD embedding AS vector WITH vector
CALL neptune.algo.vectors.topKByEmbedding(
  vector,
  {
    topK: 10,
    concurrency: 1
  }
)
YIELD node, score
RETURN vector, node, score
```

###### Warning

In queries like the one above, be careful to limit `MATCH(n)`
so that it doesn't return a large number of nodes. Keep in mind that every node in `n`
invokes a separate run of both `.vectors.get` and `.vectors.topKByEmbedding`.
Too many inputs can therefore result in very long runtimes. Use `LIMIT` or
put conditions on the `MATCH` clause to restrict its output appropriately.

## Sample  `.vectors.topKByEmbedding`  output

Here is an example of the output returned by `.vectors.topKByEmbedding` when run against
the sample
Wikipedia dataset using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH ( n {`~id`: '0'} )
                       CALL neptune.algo.vectors.get(n) YIELD embedding AS vector
                       CALL neptune.algo.vectors.topKByEmbedding( vector, { topK: 3 })
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
