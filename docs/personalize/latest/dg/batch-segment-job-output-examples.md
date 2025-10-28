# Batch segment job output format examples

A batch segment job imports your batch input data from an Amazon S3 bucket, uses your solution version trained with a
USER_SEGMENTATION recipe to generate _user segments_, and exports the segments to an Amazon S3 bucket.

The following sections list JSON output examples for batch segment jobs by recipe.

###### Topics

- [Item-Affinity](#batch-segment-output-item-affinity "#batch-segment-output-item-affinity")
- [Item-Attribute-Affinity](#batch-segment-output-item-attribute-affinity "#batch-segment-output-item-attribute-affinity")

## Item-Affinity

The following example shows the format of the output JSON file for the Item-Affinity recipe.

```
{"input": {"itemId": "105"}, "output": {"recommendedUsers": ["106", "107", "49"]}}
{"input": {"itemId": "106"}, "output": {"recommendedUsers": ["105", "107", "49"]}}
{"input": {"itemId": "441"}, "output": {"recommendedUsers": ["2", "442", "435"]}}
...
```

## Item-Attribute-Affinity

The following example shows the format of the output JSON file for the Item-Attribute-Affinity recipe.

```
{"itemAttributes": "ITEMS.genres = \"Comedy\" AND ITEMS.genres = \"Action\"", "output": {"recommendedUsers": ["25", "78", "108"]}}
{"itemAttributes": "ITEMS.genres = \"Adventure\"", "output": {"recommendedUsers": ["87", "31", "129"]}}
{"itemAttributes": "ITEMS.genres = \"Horror\" AND ITEMS.genres = \"Action\"", "output": {"recommendedUsers": ["8", "442", "435"]}}
...
```
