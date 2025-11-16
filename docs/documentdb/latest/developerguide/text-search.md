# Performing text search with Amazon DocumentDB

Amazon DocumentDB's native full text search feature (Text Index v1) allows you to perform text search on large textual data sets using special purpose text indexes.
This section describes the functionalities of the text index feature and provides steps on how to create and use text indexes in Amazon DocumentDB.
Text search limitations are also listed.

###### Topics

- [Supported functionalities](#text-search-capabilities "#text-search-capabilities")
- [Using Amazon DocumentDB text index](#using-text-search "#using-text-search")
- [Differences with MongoDB](#text-index-mongo-diff "#text-index-mongo-diff")
- [Best practices and guidelines](#text-search-best-practice "#text-search-best-practice")
- [Text Index V2](#text-index-v2 "#text-index-v2")
- [Limitations](#text-search-limitations "#text-search-limitations")

## Supported functionalities

Amazon DocumentDB text search supports the following MongoDB API compatible functionalities:

- Create text indexes on a single field.
- Create compound text indexes that include more than one text field.
- Perform single word or multi-word searches.
- Control search results using weights.
- Sort search results by score.
- Use text index in aggregation pipeline.
- Search for exact phrase.

## Using Amazon DocumentDB text index

To create a text index on a field containing string data, specify the string “text” as shown below:

Single field index:

```
db.test.createIndex({"comments": "text"})
```

This index supports text search queries in the "comments" string field in the specified collection.

Create a compound text index on more than one string field:

```
db.test.createIndex({"comments": "text", "title":"text"})
```

This index supports text search queries in the "comments" and "title" string fields in the specified collection.
You can specify up to 30 fields when creating a compound text index.
Once created, your text search queries will query all the indexed fields.

###### Note

Only one text index is allowed on each collection.

### Listing a text index on an Amazon DocumentDB collection

You can use `getIndexes()` on your collection to identify and describe indexes, including text indexes, as shown in the example below:

```
rs0:PRIMARY> db.test.getIndexes()
[
   {
      "v" : 4,
      "key" : {
         "_id" : 1
      },
      "name" : "_id_",
      "ns" : "test.test"
   },
   {
      "v" : 1,
      "key" : {
         "_fts" : "text",
         "_ftsx" : 1
      },
      "name" : "contents_text",
      "ns" : "test.test",
      "default_language" : "english",
      "weights" : {
         "comments" : 1
      },
      "textIndexVersion" : 1
   }
]
```

Once you have created an index, start inserting data into your Amazon DocumentDB collection.

```
db.test.insertMany([{"_id": 1, "star_rating": 4, "comments": "apple is red"},
                    {"_id": 2, "star_rating": 5, "comments": "pie is delicious"},
                    {"_id": 3, "star_rating": 3, "comments": "apples, oranges - healthy fruit"},
                    {"_id": 4, "star_rating": 2, "comments": "bake the apple pie in the oven"},
                    {"_id": 5, "star_rating": 5, "comments": "interesting couch"},
                    {"_id": 6, "star_rating": 5, "comments": "interested in couch for sale, year 2022"}])
```

### Running text search queries

**Run a single-word text search query**

You will need to use `$text` and `$search` operators to perform text searches.
The following example returns all documents where your text indexed field contain the string “apple” or “apple” in other formats such as “apples”:

```
db.test.find({$text: {$search: "apple"}})
```

Output:

The output of this command looks something like this:

```
{ "_id" : 1, "star_rating" : 4, "comments" : "apple is red" }
{ "_id" : 3, "star_rating" : 3, "comments" : "apples, oranges - healthy fruit" }
{ "_id" : 4, "star_rating" : 2, "comments" : "bake the apple pie in the oven" }
```

**Run a multi-word text search**

You can also perform multi-word text searches on your Amazon DocumentDB data.
The command below returns documents with a text indexed field containing “apple” or “pie”:

```
db.test.find({$text: {$search: "apple pie"}})
```

Output:

The output of this command looks something like this:

```
{ "_id" : 1, "star_rating" : 4, "comments" : "apple is red" }
{ "_id" : 2, "star_rating" : 5, "comments" : "pie is delicious" }
{ "_id" : 3, "star_rating" : 3, "comments" : "apples, oranges - healthy fruit" }
{ "_id" : 4, "star_rating" : 2, "comments" : "bake the apple pie in the oven" }
```

**Run a multi-word phrase text search**

For a multi-word phrase search, use this example:

```
db.test.find({$text: {$search: "\"apple pie\""}})
```

Output:

The command above returns documents with text indexed field containing the exact phrase “apple pie”.
The output of this command looks something like this:

```
{ "_id" : 4, "star_rating" : 2, "comments" : "bake the apple pie in the oven" }
```

**Run a text search with filters**

You can also combine text search with other query operators to filter results based on additional criteria:

```
db.test.find({$and: [{star_rating: 5}, {$text: {$search: "interest"}}]})
```

Output:

The command above returns documents with a text indexed field containing any form of “interest” and a “star_rating” equal to 5.
The output of this command looks something like this:

```
{ "_id" : 5, "star_rating" : 5, "comments" : "interesting couch" }
{ "_id" : 6, "star_rating" : 5, "comments" : "interested in couch for sale, year 2022" }
```

**Limit the number of documents returned in a text search**

You can choose to restrict the number of documents returned by using `limit`:

```
db.test.find({$and: [{star_rating: 5}, {$text: {$search: "couch"}}]}).limit(1)
```

Output:

The command above returns one result that satisfies the filter:

```
{ "_id" : 5, "star_rating" : 5, "comments" : "interesting couch" }
```

**Sort results by text score**

The following example sorts the text search results by text score:

```
db.test.find({$text: {$search: "apple"}}, {score: {$meta: "textScore"}}).sort({score: {$meta: "textScore"}})
```

Output:

The command above returns documents with a text indexed field containing “apple”, or “apple” in it's other formats like “apples”, and sorts the result based on how relevant the document is related to the search term.
The output of this command looks something like this:

```
{ "_id" : 1, "star_rating" : 4, "comments" : "apple is red", "score" : 0.6079270860936958 }
{ "_id" : 3, "star_rating" : 3, "comments" : "apples, oranges - healthy fruit", "score" : 0.6079270860936958 }
{ "_id" : 4, "star_rating" : 2, "comments" : "bake the apple pie in the oven", "score" : 0.6079270860936958 }
```

`$text` and `$search` are also supported for `aggregate`, `count`, `findAndModify`, `update`, and `delete` commands.

### Aggregation operators

**Aggregation pipeline using `$match`**

```
db.test.aggregate(
   [{ $match: { $text: { $search: "apple pie" } } }]
)
```

Output:

The command above returns the following results:

```
{ "_id" : 1, "star_rating" : 4, "comments" : "apple is red" }
{ "_id" : 3, "star_rating" : 3, "comments" : "apple - a healthy fruit" }
{ "_id" : 4, "star_rating" : 2, "comments" : "bake the apple pie in the oven" }
{ "_id" : 2, "star_rating" : 5, "comments" : "pie is delicious" }
```

**A combination of other aggregation operators**

```
db.test.aggregate(
   [
      { $match: { $text: { $search: "apple pie" } } },
      { $sort: { score: { $meta: "textScore" } } },
      { $project: { score: { $meta: "textScore" } } }
   ]
)
```

Output:

The command above returns the following results:

```
{ "_id" : 4, "score" : 0.6079270860936958 }
{ "_id" : 1, "score" : 0.3039635430468479 }
{ "_id" : 2, "score" : 0.3039635430468479 }
{ "_id" : 3, "score" : 0.3039635430468479 }
```

### Specify multiple fields when creating a text index

You can assign weights to up to three fields in your compound text index.
The default weight assigned to a field in a text index is one (1).
Weight is an optional parameter and must be in the range from 1 to 100000.

```
db.test.createIndex(
   {
     "firstname": "text",
     "lastname": "text",
     ...
   },
   {
     weights: {
       "firstname": 5,
       "lastname":10,
       ...
     },
     name: "name_text_index"
   }
 )
```

## Differences with MongoDB

Amazon DocumentDB’s text index feature uses inverted index with a term-frequency algorithm.
Text indexes are sparse by default.
Due to differences in parsing logic, tokenization delimiters, and others, the same result set as MongoDB may not be returned for the same dataset or query shape.

The following additional differences between Amazon DocumentDB text index and MongoDB exist:

- Compound indexes using non-text indexes are not supported.
- Amazon DocumentDB text indexes are case insensitive.
- Only English language is supported with text index.
- Text indexing of array (or multi-key) fields is not supported.
  For example, creating a text index on “a“ with the document {“a”:[“apple”, “pie”]} will fail.
- Wildcard text indexing is not supported.
- Unique text indexes are not supported.
- Excluding a term is not supported.

## Best practices and guidelines

- For optimal performance on text search queries involving sorting by text scores, we recommended that you create the text index before loading data.
- Text indexes require additional storage for an optimized internal copy of the indexed data.
  This has additional cost implications.

## Text Index V2

Amazon DocumentDB 8.0 introduces a new version of text index (V2) that changes underlying text search parser to bring more compatibility with the MongoDB.

In addition to the functionalities provided by the V1 text indexes, V2 text indexes also provide the following support:

- The planner moves $match stages earlier in the pipeline when possible, reducing the number of documents processed by subsequent stages.

```

rs0:PRIMARY> db.coll.createIndex({ "a": "text" });
rs0:PRIMARY> db.coll.find()
{ "_id" : 1, "a" : "jane.doe_1234@company.com" }
{ "_id" : 2, "a" : "janedoe@company.com" }
{ "_id" : 3, "a" : "/home/user/company/thesis.pdf" }
{ "_id" : 4, "a" : "/home/user/path/jane.pdf" }
{ "_id" : 5, "a" : "http://www.company.com/path" }
{ "_id" : 6, "a" : "https://company.com/path/../home" }

//Sample queries
rs0:PRIMARY> db.coll.find({ $text: { $search: "jane" } });
rs0:PRIMARY> db.coll.find({ $text: { $search: "doe_1234" } });
rs0:PRIMARY> db.coll.find({ $text: { $search: "http" } });

// Text Index V1 results
None

// Text Index V2 results
{ "_id" : 1, "a" : "jane.doe_1234@company.com" }
{ "_id" : 4, "a" : "/home/user/path/jane.pdf" }
{ "_id" : 5, "a" : "http://www.company.com/path" }

```

## Limitations

Text search has the following limitations in Amazon DocumentDB:

- Text indexes store lexemes and their position information.
  The combined size of all lexemes and their position information, within a single document, is limited to 1MB.
