# Preparing input data for user segments

Batch segment jobs use a solution version to make user segments based on data that you
provide in an input JSON file. Before you can get user segments, you must prepare and upload your JSON file to an Amazon S3
bucket. We recommend that you create an output folder in your Amazon S3 bucket or use a separate
output Amazon S3 bucket. You can then run multiple batch inference jobs using the same input data
location.

If you use a filter with placeholder parameters, such as `$GENRE`, you must provide the values for the parameters
in a `filterValues` object in your input JSON. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values").

###### To prepare and import data

1. Format your batch input data depending on the recipe your solution uses. Separate input data element with a new
   line. Your input data is either a list of itemIds (Item-Affinity) or item attributes (Item-Attribute-Affinity).
   - For item attributes, input data can include logical expressions with the `AND` operator to get users
     for multiple items or attributes per query. For more information, see [Specifying item attributes for the Item-Attribute-Affinity recipe](#specifying-item-attributes "#specifying-item-attributes").
   - For item attributes, use the `\` character to escape any special characters and single or double quotes in your input data.
   - For input data examples for both recipes, see [Batch segment job input and output JSON examples](#batch-segment-job-json-examples "#batch-segment-job-json-examples").

2. Upload your input JSON to an input folder in your Amazon S3 bucket. For more information, see [Uploading files and folders by using drag
   and drop](../../../AmazonS3/latest/user-guide/upload-objects.md "../../../AmazonS3/latest/user-guide/upload-objects.md") in the _Amazon Simple Storage Service User Guide_
3. Create a separate location for your output data, either a folder or a different
   Amazon S3 bucket. By creating a separate location for the output JSON, you can run multiple
   batch segment jobs with the same input data location.

After you have prepared your input data and uploaded it to an Amazon S3 bucket, you are ready to generate user segments with a batch segment job.
For more information, see [Getting user segments with a batch segment job](creating-batch-seg-job.md "creating-batch-seg-job.md").

###### Topics

- [Specifying item attributes for the Item-Attribute-Affinity recipe](#specifying-item-attributes "#specifying-item-attributes")
- [Batch segment job input and output JSON examples](#batch-segment-job-json-examples "#batch-segment-job-json-examples")

## Specifying item attributes for the Item-Attribute-Affinity recipe

If you use the Item-Attribute-Affinity recipe, your input data is a list of item attributes.
You can mix different columns of metadata. For example one row might be a numerical column and
the next might be a categorical column. You can't use unstructured textual item metadata as an item attribute.

Your input item metadata can include logical expressions with the
`AND` operator to get a user segment for multiple attributes. For example, a line of your input data might be
`{"itemAttributes": "ITEMS.genres = \"Comedy\" AND ITEMS.genres = \"Action\""}` or `{"itemAttributes":
 "ITEMS.genres = "\Comedy\" AND ITEMS.audience = "\teen\""}`.

When you combine two attributes with the
`AND` operator, you create a user segment with users who are more likely to interact with items that have
both attributes based on the users interactions history. Unlike filter expressions (which use the `IN` operator
for string equality), batch segment input expressions support only the `=` symbol for equality for string
matching.

## Batch segment job input and output JSON examples

For a batch segment job, your input data must be either a list of itemIds (Item-Affinity recipe) or item
attributes (Item-Attribute-Affinity). Each line of input data is a separate inference query. Each user segment is sorted
in descending order based on the probability that each user will interact with items in your inventory.

If you use a filter with placeholder parameters, such as `$GENRE`, you must provide the values for the
parameters in a `filterValues` object in your input JSON. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values").

The following are correctly formatted JSON input and output examples for batch segment jobs organized by
recipe.

**Item-Affinity**

Input
Your input data can have a maximum of 500 items. Separate each `itemId` with a
new line as follows.

```
{"itemId": "105"}
{"itemId": "106"}
{"itemId": "441"}
...
```

Output

```
{"input": {"itemId": "105"}, "output": {"recommendedUsers": ["106", "107", "49"]}}
{"input": {"itemId": "106"}, "output": {"recommendedUsers": ["105", "107", "49"]}}
{"input": {"itemId": "441"}, "output": {"recommendedUsers": ["2", "442", "435"]}}
...
```

**Item-Attribute-Affinity**

Input
Your input data can have a maximum of 10 queries, where each query is one or
more non-textual item attributes. Separate each attribute or attribute expression with a new line as follows.

```
{"itemAttributes": "ITEMS.genres = \"Comedy\" AND ITEMS.genres = \"Action\""}
{"itemAttributes": "ITEMS.genres = \"Comedy\""}
{"itemAttributes": "ITEMS.genres = \"Horror\" AND ITEMS.genres = \"Action\""}
...
```

Output

```
{"itemAttributes": "ITEMS.genres = \"Comedy\" AND ITEMS.genres = \"Action\"", "output": {"recommendedUsers": ["25", "78", "108"]}}
{"itemAttributes": "ITEMS.genres = \"Adventure\"", "output": {"recommendedUsers": ["87", "31", "129"]}}
{"itemAttributes": "ITEMS.genres = \"Horror\" AND ITEMS.genres = \"Action\"", "output": {"recommendedUsers": ["8", "442", "435"]}}
...
```
