# .vectors.remove algorithm

The `.vectors.remove` algorithm is used to remove the embedding from
a node.

## `.vectors.remove`  syntax

```
CALL neptune.algo.vectors.remove(
  [`a list of one or more nodes`]
)
YIELD node, success
RETURN node, success
```

## `.vectors.remove`  input

- **a target node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`.

The node(s) from which you want to remove the embedding. If an empty list is
supplied, the result will be empty.

## `.vectors.remove`  outputs

The following outputs are returned for each target node, and if the node has an
embedding, the embedding is removed:

- **node**   –  
  The target node.
- **success**   –  
  A Boolean value: `true` indicates that the removal succeded for the
  node, and `false` indicates that it failed.

## `.vectors.remove`  query examples

```
CALL neptune.algo.vectors.remove( ["person933"] )
YIELD node, success
RETURN node, success
```

```
MATCH (n: Student)
CALL neptune.algo.vectors.remove(n)
YIELD status
RETURN n, success
```

## Sample  `.vectors.remove`  output

Here is an example of the output returned by `.vectors.remove` when run against
the sample
Wikipedia dataset using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (n {`~id`: '1'})
                       CALL neptune.algo.vectors.remove(n)
                       YIELD node, success
                       RETURN node, success" \
  --language open_cypher \
  /tmp/out.txt
{
  "results": [
    {
      "node": {
        "~id": "1",
        "~entityType": "node",
        "~labels": [],
        "~properties": {
          "title": "24-hour clock",
          "views": 2450.62548828125,
          "wiki_id": 9985,
          "paragraph_id": 1,
          "url": "https://simple.wikipedia.org/wiki?curid=9985",
          "langs": 30,
          "text": "A time in the 24-hour clock is written in the form hours:minutes (for example\\, 01:23)\\, or hours:minutes:seconds (01:23:45). Numbers under 10 have a zero in front (called a leading zero); e.g. 09:07. Under the 24-hour clock system\\, the day begins at midnight\\, 00:00\\, and the last minute of the day begins at 23:59 and ends at 24:00\\, which is identical to 00:00 of the following day. 12:00 can only be mid-day. Midnight is called 24:00 and is used to mean the end of the day and 00:00 is used to mean the beginning of the day. For example\\, you would say \"Tuesday at 24:00\" and \"Wednesday at 00:00\" to mean exactly the same time."
        }
      },
      "success": true
    }
  ]
}
```
