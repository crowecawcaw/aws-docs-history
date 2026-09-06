# The  `.vectors.distanceByEmbedding`  algorithm (deprecated)

The `.vectors.distanceByEmbedding` algorithm computes the distance between an embedding vector and the
embedding of an input node. The default distance is the squared L2 norm of the input (source) embedding vector and
the embedding vector of the (target) input node.

## `.vectors.distanceByEmbedding`  syntax

```
WITH [*an embedding*] as embedding
MATCH( n {`~id`: "the ID of the target node(s)"} )
CALL neptune.algo.vectors.distanceByEmbedding(embedding, n,
   {
       metric: The distance computation metric (optional)
   }
)
YIELD distance
RETURN embedding, n, distance
```

## `.vectors.distanceByEmbedding`  inputs

- **a source embedding list**   _(required)_   –  
  _type:_ `float[]` or `double[]`;.

The mebedding vector from which you want to use as the source for the distance computations.

- **a target node list**   _(required)_   –  
  _type:_ `Node[]` or `NodeId[]`;   _default: none_.

The result of a `MATCH` statement from which you want to source
distance computations.

- **metric**   _(optional)_   –  
  _type:_ `string`   _default: L2Squared_.

The distance metric to use for distance computation.

    + Must be one of [L2Squared, L2, CosineSimilarity, CosineDistance, DotProduct].
    + Case-insensitive.
    + The descriptions for the metrics, where x and y are vectors, x\_i and y\_i are the components of x and y vectors,
     θ is the angle between the x and y vectors, ||x|| denotes the magnitude (length, l2-norm, norm2) of vector x,
     ∑ denotes summation:





    	- L2-Squared: Squared Euclidean distance between two vectors:




    	![L2-Squared: Squared Euclidean distance between two vectors.](images/vectors-distance/L2Squared.png)


    	 For more information on L2-Squared, see
    	 [https://en.wikipedia.org/wiki/Euclidean\_distance#Squared\_Euclidean\_distance](https://en.wikipedia.org/wiki/Euclidean_distance#Squared_Euclidean_distance "https://en.wikipedia.org/wiki/Euclidean_distance#Squared_Euclidean_distance").
    	- L2: Euclidean distance (L2 norm) between two vectors:




    	![L2: Euclidean distance (L2 norm) between two vectors.](images/vectors-distance/L2.png)


    	 For more information on L2, see
    	 [https://en.wikipedia.org/wiki/Euclidean\_distance](https://en.wikipedia.org/wiki/Euclidean_distance "https://en.wikipedia.org/wiki/Euclidean_distance").
    	- Dot Product: Inner dot product of two vectors:




    	![Dot Product: Inner dot product of two vectors.](images/vectors-distance/dot1.png)


    	 For more information on Dot Product, see
    	 [https://en.wikipedia.org/wiki/Dot\_product](https://en.wikipedia.org/wiki/Dot_product "https://en.wikipedia.org/wiki/Dot_product").
    	- Cosine Similarity: Measures the cosine of the angle between two vectors (higher value means more similar):




    	![Cosine Similarity: Measures the cosine of the angle between two vectors (higher value means more similar).](images/vectors-distance/cossimi4.png)


    	 Range: [-1, 1]




    	 For more information on Cosine Similarity, see
    	 [https://en.wikipedia.org/wiki/Cosine\_similarity](https://en.wikipedia.org/wiki/Cosine_similarity "https://en.wikipedia.org/wiki/Cosine_similarity").
    	- Cosine Distance: Opposite of cosine similarity (lower value means more similar):




    	![Cosine Distance: Opposite of cosine similarity (lower value means more similar).](images/vectors-distance/cosdist1.png)


    	 Range: [0, 2]




    	 For more information on Cosine Distance, see
    	 [https://en.wikipedia.org/wiki/Cosine\_similarity#Cosine\_distance](https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance "https://en.wikipedia.org/wiki/Cosine_similarity#Cosine_distance").

## `.vectors.distanceByEmbedding`  outputs

For every pair of source node and target node:

- **embedding**   –  
  The input source embedding vector.
- **target**   –  
  The target node.
- **distance**   –  
  The distance between the source embedding and the target node.

## `.vectors.distanceByEmbedding`  query examples

```
WITH [1.1, 1.2, 1.3, 1.4] as embedding
MATCH (n)
WHERE id(n)="v1"
CALL neptune.algo.vectors.distanceByEmbedding(embedding, n)
YIELD distance
RETURN embedding, n, distance
```

```
WITH [1.1, 1.2, 1.3, 1.4] as embedding
MATCH (n)
WHERE id(n)="v1"
CALL neptune.algo.vectors.distanceByEmbedding(embedding, n, {metric: "CosineSimilarity" })
YIELD distance
return embedding, n, distance
```

```
UNWIND [ {id: "933", embedding: [1,2,3,4]},
         {id: "934", embedding: [-1,-2,-3,-4]} ] as entry
MATCH (n:person) WHERE id(n)=entry.id WITH n, entry.embedding as embedding
CALL neptune.algo.vectors.distanceByEmbedding(embedding, n)
YIELD distance
RETURN embedding, n, distance
```

## Sample  `.vectors.distanceByEmbedding`  output

Here is an example of the output returned by `.vectors.distanceByEmbedding` when run against
a sample Wikipedia dataset using the following query:

```
aws neptune-graph execute-query \
  --graph-identifier ${graphIdentifier} \
  --query-string "***embedding part***
                       MATCH (n{`~id`: '1'})
                       CALL neptune.algo.vectors.distanceByEmbedding(embedding, n)
                       YIELD distance
                       RETURN embedding, n, distance" \
  --language open_cypher \
  /tmp/out.txt

{
  "results": [
    {
      "embedding": [***embedding***],
      "n": {
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
