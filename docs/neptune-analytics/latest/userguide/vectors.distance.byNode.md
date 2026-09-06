

# The  `.vectors.distance.byNode`  algorithm
<a name="vectors.distance.byNode"></a>

The `.vectors.distance.byNode` algorithm computes the distance between two nodes based on their embeddings. The default distance is the squared L2 norm.

## `.vectors.distance.byNode`  syntax
<a name="vectors.distance.byNode-syntax"></a>

```
MATCH( n {`~id`: "{{the ID of the source node(s)}}"} )
MATCH( m {`~id`: "{{the ID of the target node(s)}}"} )
CALL neptune.algo.vectors.distance.byNode(n, m,
   {
       metric: The distance computation metric (optional)
   }
)
YIELD distance
RETURN n, m, distance
```

## `.vectors.distance.byNode`  inputs
<a name="vectors.distance.byNode-inputs"></a>
+ **a source node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

  The result of a `MATCH` statement from which you want to get the source for the distance computations.
+ **target node list**   *(required)*   –   *type:* `Node[]` or `NodeId[]`;   *default: none*.

  The result of a `MATCH` statement from which you want to get the targets of the distance computations.
+  **metric**   *(optional)*   –   *type:* `string`   *default: L2Squared*. 

   The distance metric to use for distance computation. 
  +  Must be one of [L2Squared, L2, CosineSimilarity, CosineDistance, DotProduct]. 
  +  Case-insensitive. 
  +  The descriptions for the metrics, where x and y are vectors, x\_i and y\_i are the components of x and y vectors, θ is the angle between the x and y vectors, \|\|x\|\| denotes the magnitude (length, l2-norm, norm2) of vector x, ∑ denotes summation: 
    +  L2-Squared: Squared Euclidean distance between two vectors:   
![L2-Squared: Squared Euclidean distance between two vectors.](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/images/vectors-distance/L2Squared.png)

       For more information on L2-Squared, see [ https://en.wikipedia.org/wiki/Euclidean\_distance\#Squared\_Euclidean\_distance](https://en.wikipedia.org/wiki/Euclidean_distance#Squared_Euclidean_distance). 
    +  L2: Euclidean distance (L2 norm) between two vectors:   
![L2: Euclidean distance (L2 norm) between two vectors.](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/images/vectors-distance/L2.png)

       For more information on L2, see [ https://en.wikipedia.org/wiki/Euclidean\_distance](https://en.wikipedia.org/wiki/Euclidean_distance). 
    +  Dot Product: Inner dot product of two vectors:   
![Dot Product: Inner dot product of two vectors.](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/images/vectors-distance/dot1.png)

       For more information on Dot Product, see [ https://en.wikipedia.org/wiki/Dot\_product](https://en.wikipedia.org/wiki/Dot_product). 
    +  Cosine Similarity: Measures the cosine of the angle between two vectors (higher value means more similar):   
![Cosine Similarity: Measures the cosine of the angle between two vectors (higher value means more similar).](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/images/vectors-distance/cossimi4.png)

       Range: [-1, 1] 

       For more information on Cosine Similarity, see [ https://en.wikipedia.org/wiki/Cosine\_similarity](https://en.wikipedia.org/wiki/Cosine_similarity). 
    +  Cosine Distance: Opposite of cosine similarity (lower value means more similar):   
![Cosine Distance: Opposite of cosine similarity (lower value means more similar).](http://docs.aws.amazon.com/neptune-analytics/latest/userguide/images/vectors-distance/cosdist1.png)

       Range: [0, 2] 

       For more information on Cosine Distance, see [ https://en.wikipedia.org/wiki/Cosine\_similarity\#Cosine\_distance](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance). 

**Warning**  
Be careful to limit `MATCH(n)` and `MATCH(m)` so that they don't return a large number of nodes. Keep in mind that every pair of `n` and `m` in the join result invokes `.vectors.distance.byNode` once. Too many inputs can therefore result in very long runtimes. Use `LIMIT` or put conditions on the `MATCH` clause to restrict its output appropriately.

## `.vectors.distance.byNode`  outputs
<a name="vectors.distance.byNode-outputs"></a>

For every pair of source node and target node:
+ **source**   –   The source node.
+ **target**   –   The target node.
+ **distance**   –   The distance between source and target nodes.

## `.vectors.distance.byNode`  query examples
<a name="vectors.distance.byNode-query-example"></a>

```
MATCH ( n {`~id`: "106"} )
MATCH ( m {`~id`: "110" } )
CALL neptune.algo.vectors.distance.byNode( n, m )
YIELD distance
RETURN n, m, distance
```

```
MATCH ( n {`~id`: "106"} )
MATCH ( m {`~id`: "110"} )
CALL neptune.algo.vectors.distance.byNode( n, m, {metric: "CosineSimilarity"} )
YIELD distance
RETURN n, m, distance
```

## Sample  `.vectors.distance.byNode`  output
<a name="vectors.distance.byNode-sample-output"></a>

Here is an example of the output returned by `.vectors.distance.byNode` when run against a sample Wikipedia dataset using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "MATCH (n{`~id`: '0'})
                       MATCH (m{`~id`: '1'})
                       CALL neptune.algo.vectors.distance.byNode(n, m)
                       YIELD distance
                       RETURN n, m, distance" \
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
      "m": {
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
      "distance": 27.762847900390626
    }
  ]
}
```