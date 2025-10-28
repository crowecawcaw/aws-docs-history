# Batch recommendations with themes from Content Generator

###### Important

When you get batch recommendations with themes, you incur additional costs. For more information, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/ "https://aws.amazon.com/personalize/pricing/").

If you use the [Similar-Items
recipe](native-recipe-similar-items.md "native-recipe-similar-items.md"), Amazon Personalize Content Generator can add descriptive themes to batch recommendations.
_Content Generator_ is a generative artificial intelligence (generative AI) capability managed by
Amazon Personalize.

When you get batch recommendations with themes, Amazon Personalize Content Generator adds a descriptive theme for each set of
similar items. The theme is based on the item description and item name data in your Items dataset. Amazon Personalize includes the themes
in the output of the batch inference job. You can use the themes to make the text in your application or marketing messages
more compelling.

For example, if you get related items
recommendations for a breakfast food item, Amazon Personalize might generate a theme like _Rise and shine_ or _Morning essentials_.
You might use the theme to replace a generic carousel title, like _Frequently bought together_. Or you
might incorporate the theme in a promotional email or marketing campaign for new menu options.

AWS doesn't monitor themes from Content Generator. To confirm the theme quality, you can use the scores
produced for each recommended item. For more information, see [Ranking and scoring for batch recommendations with themes](#themed-batch-rec-scoring "#themed-batch-rec-scoring").

###### Topics

- [Supported regions](#themes-regions "#themes-regions")
- [Guidelines and requirements](#themed-batch-requirements "#themed-batch-requirements")
- [Ranking and scoring for batch recommendations with themes](#themed-batch-rec-scoring "#themed-batch-rec-scoring")
- [Generating batch recommendations with themes](#getting-themed-batch-rec "#getting-themed-batch-rec")

## Supported regions

Amazon Personalize Content Generator is only available in the following AWS Regions:

- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Tokyo)

## Guidelines and requirements

The following are guidelines and requirements for generating recommendations with themes:

- Your input file can have up to 100 items. For information about input data for batch
  recommendations, see [Preparing input data for batch recommendations](batch-data-upload.md "batch-data-upload.md").
- Your solution must use the [Similar-Items
  recipe](native-recipe-similar-items.md "native-recipe-similar-items.md").
- You must have an Items dataset with the following data. This data can help generate more relevant themes.
  - It must have a textual field, such as a DESCRIPTION field. For information about textual data, see [Unstructured text metadata](items-datasets.md#text-data "items-datasets.md#text-data").
  - It must have a string column with item name data, such as a TITLE field.
    If your Items dataset doesn't have this data, you can add it.
    For information about updating existing data, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

## Ranking and scoring for batch recommendations with themes

When you get batch recommendations with themes, Amazon Personalize ranks each set of items based
on how relevant the theme is for each item. Each item includes a score in a rough range of
-0.1 and 0.6. The higher the score, the more closely related the item is to the theme. You
might use the scores to set a threshold to show only items that are strongly related to the
theme.

For example, Amazon Personalize might return a theme of `For your sweet tooth`, and the related items and their
scores might be: hard candy (score 0.19884521), chocolate (score .17664525), apple (score .08994528), popsicle (score
.14294521), sweet potato (score .07794527), and carrot (score .04994523). In your application, you might add a rule to
include only items with a score of `.10` or greater, eliminating the fruits and vegetables.

The following example shows the format of the output of a batch inference job that generates movie recommendations with themes.

```
{"input":{"itemId":"40"},"output":{"recommendedItems":["36","50","44","22","21","29","3","1","2","39"],"theme":"Movies with a strong female lead","itemsThemeRelevanceScores":[0.19994527,0.183059963,0.17478035,0.1618133,0.1574806,0.15468733,0.1499242,0.14353688,0.13531424,0.10291852]}}
{"input":{"itemId":"43"},"output":{"recommendedItems":["50","21","36","3","17","2","39","1","10","5"],"theme":"The best movies of 1995","itemsThemeRelevanceScores":[0.184988,0.1795761,0.11143453,0.0989443,0.08258403,0.07952615,0.07115086,0.0621634,-0.138913,-0.188913]}}
...

```

## Generating batch recommendations with themes

To generate batch recommendations with themes, you complete the batch workflow as described in [Batch workflow](getting-batch-recommendations.md#batch-worfklow-steps "getting-batch-recommendations.md#batch-worfklow-steps"). You prepare your input data in the same way you
would for a `RELATED_ITEMS` recipe. For an example, see [RELATED_ITEMS recipes](batch-data-upload.md#batch-input-related-items "batch-data-upload.md#batch-input-related-items").

When you create the batch inference job, you enable theme generation and specify the item title column of your Items
dataset.

- For information about using the Amazon Personalize console to create a batch inference job that generates themes, see [Creating a batch inference
  job](creating-batch-inference-job.md "creating-batch-inference-job.md").
- For a code sample that shows how to use the SDK for Python (Boto3) to create a batch inference job
  that generates themes, see [Creating a batch inference job that generates themes](creating-batch-inference-job.md#batch-sdk-themes "creating-batch-inference-job.md#batch-sdk-themes").
