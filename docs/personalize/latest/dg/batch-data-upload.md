# Preparing input data for batch recommendations

A batch inference job imports your batch input JSON data
from an Amazon S3 bucket, uses your custom solution version to generate recommendations, and
then exports the item recommendations to an Amazon S3 bucket. Before you can get
batch recommendations, you must prepare and upload your JSON file to an Amazon S3
bucket. We recommend that you create an output folder in your Amazon S3 bucket or use a separate
output Amazon S3 bucket. You can then run multiple batch inference jobs using the same input data
location.

If you use a filter with placeholder parameters, such as `$GENRE`, you must provide the values for the parameters
in a `filterValues` object in your input JSON. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values").

###### To prepare and import data

1.  Format your batch input data depending on your recipe. You can't get batch recommendations with the Trending-Now recipe.

        * For USER\_PERSONALIZATION recipes and the Popularity-Count recipe, your input data is a JSON file with a list of userIds
        * For RELATED\_ITEMS recipes, your input data is a list of itemIds
        * For PERSONALIZED\_RANKING recipes, your input data is a list of userIds, each paired with a collection of
         itemIds

    Separate each row with a new line. For input data examples, see [Batch inference job input and output JSON examples](#batch-inference-job-json-examples "#batch-inference-job-json-examples").

2.  Upload your input JSON to an input folder in your Amazon S3 bucket.
    For more information, see [Uploading files and folders by using drag and drop](../../../AmazonS3/latest/user-guide/upload-objects.md "../../../AmazonS3/latest/user-guide/upload-objects.md") in the _Amazon Simple Storage Service User Guide_
3.  Create a separate location for your output data, either a folder or a different
    Amazon S3 bucket. By creating a separate location for the output JSON, you can run multiple
    batch inference jobs with the same input data location.
4.  Create a batch inference job. Amazon Personalize outputs the recommendations from your solution version to your output data location.

## Batch inference job input and output JSON examples

How you format your input data the recipe you use.
If you use a filter with placeholder parameters, such as `$GENRE`, you must provide the values for the parameters
in a `filterValues` object in your input JSON. For more information, see [Providing filter values in your input JSON](filter-batch.md#providing-filter-values "filter-batch.md#providing-filter-values").

The following sections list correctly formatted JSON input
and output examples for batch inference jobs. You can't get batch recommendations with the Trending-Now recipe.

###### Topics

- [USER_PERSONALIZATION recipes](#batch-input-user-personalization "#batch-input-user-personalization")
- [POPULAR_ITEMS recipes (Popularity-Count only)](#batch-input-popular-items "#batch-input-popular-items")
- [PERSONALIZED_RANKING recipes](#batch-input-ranking "#batch-input-ranking")
- [RELATED_ITEMS recipes](#batch-input-related-items "#batch-input-related-items")

### USER_PERSONALIZATION recipes

The following shows correctly formatted JSON input and output examples for the USER_PERSONALIZATION recipes. If you use User-Personalization-v2, each recommended item includes a list of reasons for why the item was included in
recommendations. This list can be empty. For information about possible reasons, see [Recommendation reasons with User-Personalization-v2](recommendations.md#recommendation-reasons "recommendations.md#recommendation-reasons").

Input
Separate each `userId` with a new line as follows.

```
{"userId": "4638"}
{"userId": "663"}
{"userId": "3384"}
...
```

Output

```
{"input":{"userId":"4638"},"output":{"recommendedItems":["63992","115149","110102","148626","148888","31685","102445","69526","92535","143355","62374","7451","56171","122882","66097","91542","142488","139385","40583","71530","39292","111360","34048","47099","135137"],"scores":[0.0152238,0.0069081,0.0068222,0.006394,0.0059746,0.0055851,0.0049357,0.0044644,0.0042968,0.004015,0.0038805,0.0037476,0.0036563,0.0036178,0.00341,0.0033467,0.0033258,0.0032454,0.0032076,0.0031996,0.0029558,0.0029021,0.0029007,0.0028837,0.0028316]},"error":null}
{"input":{"userId":"663"},"output":{"recommendedItems":["368","377","25","780","1610","648","1270","6","165","1196","1097","300","1183","608","104","474","736","293","141","2987","1265","2716","223","733","2028"],"scores":[0.0406197,0.0372557,0.0254077,0.0151975,0.014991,0.0127175,0.0124547,0.0116712,0.0091098,0.0085492,0.0079035,0.0078995,0.0075598,0.0074876,0.0072006,0.0071775,0.0068923,0.0066552,0.0066232,0.0062504,0.0062386,0.0061121,0.0060942,0.0060781,0.0059263]},"error":null}
{"input":{"userId":"3384"},"output":{"recommendedItems":["597","21","223","2144","208","2424","594","595","920","104","520","367","2081","39","1035","2054","160","1370","48","1092","158","2671","500","474","1907"],"scores":[0.0241061,0.0119394,0.0118012,0.010662,0.0086972,0.0079428,0.0073218,0.0071438,0.0069602,0.0056961,0.0055999,0.005577,0.0054387,0.0051787,0.0051412,0.0050493,0.0047126,0.0045393,0.0042159,0.0042098,0.004205,0.0042029,0.0040778,0.0038897,0.0038809]},"error":null}
...
```

### POPULAR_ITEMS recipes (Popularity-Count only)

The following shows correctly formatted JSON input and output examples for the Popularity-Count recipe. You can't
get batch recommendations with the Trending-Now recipe.

Input
Separate each `userId` with a new line as follows.

```
{"userId": "12"}
{"userId": "105"}
{"userId": "41"}
...
```

Output

```
{"input": {"userId": "12"}, "output": {"recommendedItems": ["105", "106", "441"]}}
{"input": {"userId": "105"}, "output": {"recommendedItems": ["105", "106", "441"]}}
{"input": {"userId": "41"}, "output": {"recommendedItems": ["105", "106", "441"]}}
...
```

### PERSONALIZED_RANKING recipes

The following shows correctly formatted JSON input and output examples for PERSONALIZED_RANKING recipes.

Input
Separate each `userId` and list of `itemIds` to be ranked with a new line as
follows.

```
{"userId": "891", "itemList": ["27", "886", "101"]}
{"userId": "445", "itemList": ["527", "55", "901"]}
{"userId": "71", "itemList": ["27", "351", "101"]}
...
```

Output

```
{"input":{"userId":"891","itemList":["27","886","101"]},"output":{"recommendedItems":["27","101","886"],"scores":[0.48421,0.28133,0.23446]}}
{"input":{"userId":"445","itemList":["527","55","901"]},"output":{"recommendedItems":["901","527","55"],"scores":[0.46972,0.31011,0.22017]}}
{"input":{"userId":"71","itemList":["29","351","199"]},"output":{"recommendedItems":["351","29","199"],"scores":[0.68937,0.24829,0.06232]}}
...
```

### RELATED_ITEMS recipes

The following shows correctly formatted JSON input and output examples for RELATED_ITEMS recipes.

Input
Separate each `itemId` with a new line as follows.

```
{"itemId": "105"}
{"itemId": "106"}
{"itemId": "441"}
...
```

Output

```
{"input": {"itemId": "105"}, "output": {"recommendedItems": ["106", "107", "49"]}}
{"input": {"itemId": "106"}, "output": {"recommendedItems": ["105", "107", "49"]}}
{"input": {"itemId": "441"}, "output": {"recommendedItems": ["2", "442", "435"]}}
...
```

The following shows correctly formatted JSON input and output examples for the Similar-Items recipe with themes.

Input
Separate each `itemId` with a new line as follows.

```
{"itemId": "40"}
{"itemId": "43"}
...
```

Output

```
{"input":{"itemId":"40"},"output":{"recommendedItems":["36","50","44","22","21","29","3","1","2","39"],"theme":"Movies with a strong female lead","itemsThemeRelevanceScores":[0.19994527,0.183059963,0.17478035,0.1618133,0.1574806,0.15468733,0.1499242,0.14353688,0.13531424,0.10291852]}}
{"input":{"itemId":"43"},"output":{"recommendedItems":["50","21","36","3","17","2","39","1","10","5"],"theme":"The best movies of 1995","itemsThemeRelevanceScores":[0.184988,0.1795761,0.11143453,0.0989443,0.08258403,0.07952615,0.07115086,0.0621634,-0.138913,-0.188913]}}
...

```
