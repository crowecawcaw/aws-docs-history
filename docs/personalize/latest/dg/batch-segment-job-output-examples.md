

# Batch segment job output format examples
<a name="batch-segment-job-output-examples"></a>

A batch segment job imports your batch input data from an Amazon S3 bucket, uses your solution version trained with a USER\_SEGMENTATION recipe to generate *user segments*, and exports the segments to an Amazon S3 bucket.

The following sections list JSON output examples for batch segment jobs by recipe.

**Topics**
+ [Item-Affinity](#batch-segment-output-item-affinity)
+ [Item-Attribute-Affinity](#batch-segment-output-item-attribute-affinity)

## Item-Affinity
<a name="batch-segment-output-item-affinity"></a>

 The following example shows the format of the output JSON file for the Item-Affinity recipe. 

```
{"input": {"itemId": "105"}, "output": {"recommendedUsers": ["106", "107", "49"]}}
{"input": {"itemId": "106"}, "output": {"recommendedUsers": ["105", "107", "49"]}}
{"input": {"itemId": "441"}, "output": {"recommendedUsers": ["2", "442", "435"]}}
...
```

## Item-Attribute-Affinity
<a name="batch-segment-output-item-attribute-affinity"></a>

 The following example shows the format of the output JSON file for the Item-Attribute-Affinity recipe. 

```
{"itemAttributes": "ITEMS.genres = \"Comedy\" AND ITEMS.genres = \"Action\"", "output": {"recommendedUsers": ["25", "78", "108"]}}
{"itemAttributes": "ITEMS.genres = \"Adventure\"", "output": {"recommendedUsers": ["87", "31", "129"]}}
{"itemAttributes": "ITEMS.genres = \"Horror\" AND ITEMS.genres = \"Action\"", "output": {"recommendedUsers": ["8", "442", "435"]}}
...
```