# Promoting items in real-time recommendations

With all domain use cases and some custom recipes,
you can specify a promotion when you get real-time recommendations.

A _promotion_ defines additional business rules that apply to a configurable subset of recommended items. For example, you might have a streaming
app and want to promote your own shows and movies but also recommend relevant titles.
You could use a promotion to specify that a certain percentage of recommended items must come from the category _in-house_. The remaining recommended items
would continue to be relevant recommendations based on your recipe and any request filters.

To apply a promotion, you specify the following in your recommendation request:

- The percentage of recommended items to apply the promotion filter to.
- A filter that specifies the promotion criteria. For more information, see [Promotion filters](#promotion-filters "#promotion-filters").
  In the recommendation response, promoted items are positioned randomly relative to other recommended items, but in sorted order relative to other promoted items.
  Depending on your recipe, recommended
  items that aren't part of a promotion are sorted by relevance to the user, popularity, or similarity.
  If there aren't enough items that meet the promotion criteria, the result will contain as many promoted items as possible.

You can apply a promotion to recommendations with
the Amazon Personalize console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

###### Topics

- [Use cases and recipes that support promotions](#promotion-use-case-recipes "#promotion-use-case-recipes")
- [Promotion filters](#promotion-filters "#promotion-filters")
- [Promoting new items](#promoting-new-items "#promoting-new-items")
- [Promoting items (console)](#promoting-items-console "#promoting-items-console")
- [Promoting items (AWS CLI)](#promoting-items-cli "#promoting-items-cli")
- [Promoting items (AWS SDKs)](#promoting-items-sdk "#promoting-items-sdk")

## Use cases and recipes that support promotions

All use cases support promotions.
The following custom recipes support promotions:

- [User-Personalization-v2](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md")
  and [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") recipes
- [Similar-Items](native-recipe-similar-items.md "native-recipe-similar-items.md") and
  [SIMS](native-recipe-sims.md "native-recipe-sims.md")recipes
- [Trending-Now](native-recipe-trending-now.md "native-recipe-trending-now.md") and
  [Popularity-Count](native-recipe-popularity.md "native-recipe-popularity.md") recipes

## Promotion filters

When you apply a promotion to a recommendation request, you choose a filter that specifies the promotion criteria.
You can use an existing filter or create a new one. You create and manage filters for promotions as you would other filters
in Amazon Personalize. For information about creating and managing filters, see [Filtering results](filter.md "filter.md").

The only difference between a promotion filter and a filter that you choose outside the promotion (the
_request filter_) is how Amazon Personalize applies them. A promotion filter applies to only promoted items, while
a request filter applies to only the remaining recommended items. If you specify a request filter and promotion filter, and
want to apply both filters to promoted items, your promotion filter's expression must include both expressions. The way you
combine two expressions depends on the datasets you use. For more information on filter expressions, their rules, and how to
create them, see [Filter expressions](filter-expressions.md "filter-expressions.md").

**Filter expression examples**

The following expression includes only items from the category "in-house". You might use this expression if you want to promote your own content in your recommendations.

```
INCLUDE ItemID WHERE Items.OWNER IN ("in-house")
```

The following expression includes only items created more recently than a timestamp you specify. You might use this expression to promote new items in recommendations.

```
INCLUDE ItemID WHERE Items.CREATION_TIMESTAMP > $DATE
```

The following expression shows how you might apply a request filter to promoted items. It includes only available clothing items as promoted items.
In this scenario, the `Items.AVAILABLE IN ("True")` would also be used in the request filter expression, so that all recommendations are for items that are available.

```
INCLUDE ItemID WHERE Items.CATEGORY IN ("clothing") AND Items.AVAILABLE IN ("True")
```

For a more complete list of filter examples, see [Filter expression examples](filter-expression-examples.md "filter-expression-examples.md").

## Promoting new items

If you use the [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md "native-recipe-user-personalization-v2.md"),
Amazon Personalize recommends the most relevant items to users and more frequently recommends existing items
with interactions data. To make sure recommendations include some new items, you can apply a promotion to
recommendation requests that includes items based on creation timestamp.

If you don't already use a promotion, your filter expression can promote items created after a certain date:

```
INCLUDE ItemID WHERE Items.CREATION_TIMESTAMP > $DATE
```

If you already use a promotion, you create an expression that chains both the promotion and the new item condition statements:

```
INCLUDE ItemID WHERE Items.CATEGORY IN ("clothing") OR Items.CREATION_TIMESTAMP > $DATE
```

## Promoting items (console)

To promote certain items in recommendations with the Amazon Personalize console, create a filter, and then provide the promotion
details in the recommendation request. For information on other fields, see [Getting item recommendations (console)](getting-real-time-item-recommendations.md#get-real-time-recommendations-console "getting-real-time-item-recommendations.md#get-real-time-recommendations-console").

###### To promote items in recommendations

1. Open the Amazon Personalize console at [https://console.aws.amazon.com/personalize/home](https://console.aws.amazon.com/personalize/home "https://console.aws.amazon.com/personalize/home") and sign into your account.
2. Choose the dataset group that contains the campaign or recommender you are using.
3. If you haven't already, create a filter that specifies the promotion criteria. You create filters for promotions
   the same way that you create request filters.
   For information on creating and managing filters, see [Filtering results](filter.md "filter.md").
4. In the navigation pane, choose **Recommenders** or **Campaigns**.
5. Choose the target campaign or recommender.
6. For campaigns, under **Test campaign results**, enter your recommendation request details based on the recipe you used.
   For recommenders, choose **Test recommender** and enter your recommendation request details.
7. Optionally choose a filter for the request. This filter applies to only non-promoted items. For information on
   creating and managing filters, see [Filtering results](filter.md "filter.md").
8. If you use contextual metadata, provide data for each context. For each context, for the **Key** enter the metadata field. For the **Value**, enter the context data. For
   more information, see [Increasing recommendation relevance with contextual metadata](contextual-metadata.md "contextual-metadata.md").
9. For **Promotion** specify the following:
   - **Percent promoted items**: Enter the percentage of recommended items to apply the promotion to.
   - **Filter**: Choose a filter that specifies the promotion criteria. This filter applies to the
     promoted items instead of any request filter that you may have specified in step 7.
   - **Filter parameter**: If your promotion uses a filter with placeholder parameters, for each parameter, enter
     the value to set the filter criteria. To use multiple values for one parameter,
     separate each value with a comma.

10. Choose **Get recommendations**. A table containing the user’s top 25 recommended
    items displays. The **Promoted item** column indicates whether the item was included because of your
    promotion. Promoted items are positioned randomly relative to other recommended items, but in sorted order relative to
    other promoted items. Depending on your use case or recipe, recommended items that aren't part of a promotion are sorted
    by relevance to the user, popularity, or similarity. If there aren't enough items that meet the promotion criteria, the
    result will contain as many promoted items as possible.

## Promoting items (AWS CLI)

The following code shows how to promote items in recommendations with the AWS CLI and a custom campaign. To
promote items with a recommender, replace the `campaign-arn` parameter with a `recommender-arn`
and specify the Amazon Resource Name (ARN) for the recommender.
For the promotion fields, specify the following:

- name: Give the promotion a name. The recommendation response uses the name to identify promoted items.
- percent-promoted-items: The percentage of recommended items to apply the promotion to. In this example, 50% of items will be promoted items.
- filterArn: Specify the Amazon Resource Name (ARN) of the filter that defines the promotion criteria.
  For more information, see [Promotion filters](#promotion-filters "#promotion-filters").
- parameter names and values: If your filter expression has any parameters, provide the parameter names (case
  sensitive) and the values. For example, if your filter expression has a `$GENRE` parameter, provide GENRE as
  the key, and a genre or genres, such as _Comedy_, as the value. Separate multiple values with a
  comma. When you use the AWS CLI, for each value you must use the `/` character to escape both quotes and the
  `/` character. The following code example shows how to format the values.

The code shows how to use both a request filter and a promotion filter. A promotion filter applies to only promoted
items, while a request filter applies to only the remaining recommended items. For more information, see [Promotion filters](#promotion-filters "#promotion-filters").

For information about additional fields, see [Getting item recommendations (AWS SDKs)](getting-real-time-item-recommendations.md#get-item-rec-sdk "getting-real-time-item-recommendations.md#get-item-rec-sdk")
and [Getting a personalized ranking using contextual metadata](get-personalized-rankings-sdk.md#personalized-ranking-contextual-metadata-example "get-personalized-rankings-sdk.md#personalized-ranking-contextual-metadata-example").

```
aws personalize-runtime get-recommendations \
--campaign-arn `CampaignArn` \
--user-id `1` \
--num-results `10`  \
--filter-arn `RequestFilterArn` \
--filter-values '{
    "`RequestFilterParameterName`": "\"`value`\"",
    "`RequestFilterParameterName`": "\"`value1`\",\"`value2`\",\"`value3`\""
  }' \
--promotions "[{
  \"name\": \"`promotionName`\",
  \"percentPromotedItems\": `50`,
  \"filterArn\": \"`PromotionFilterARN`\",
  \"filterValues\": {\"`PromotionParameterName`\":\"\\\"`value1`, `value2`\\\"\"}
}]"
```

A list of recommended items displays. Promoted items are positioned randomly relative to other recommended items, but in sorted order relative to other promoted items.
Depending on your recipe, recommended
items that aren't part of a promotion are sorted by relevance to the user, popularity, or similarity. If there aren't enough items that meet the promotion criteria, the result will contain as many promoted items as possible.

```
{
  "itemList": [
      {
          "itemId1": "123",
          "score": .0117211,
          "promotionName": "promotionName"
      },
      {
         "itemId2": "456",
         "score": .0077976
      },
      {
         "itemId3": "789",
         "score": .0067171
      },
      .....
 ]
```

## Promoting items (AWS SDKs)

The following code shows how to promote items in recommendations with the SDK for Python (Boto3) and the SDK for Java 2.x and a custom
campaign. To
promote items with a recommender, replace the `campaignArn` parameter with `recommenderArn`
and specify the Amazon Resource Name (ARN) for the recommender.
For the promotion fields, specify the following:

- name: Specify the name of the promotion. The recommendation response includes the name to identify promoted items.
- percentPromotedItems: The percentage of recommended items to apply the promotion to.
- promotionFilterARN: The Amazon Resource Name (ARN) of the filter that defines the promotion criteria.
  For more information, see [Promotion filters](#promotion-filters "#promotion-filters").
- Any parameter names and values: If your filter expression has any parameters, for each parameter in your filter expression, provide the parameter name (case sensitive)
  and the values. For example, if your filter expression has a `$GENRE` parameter, provide `"GENRE"` as the key, and a genre or genres, such as "\"Comedy"\", as the value.
  Separate multiple values with a comma. For example, `"\"comedy\",\"drama\",\"horror"\"`.

The following code shows how to use both a request filter and a promotion filter. A promotion filter applies to only
promoted items, while a request filter applies to only the remaining recommended items. For more information, see [Promotion filters](#promotion-filters "#promotion-filters").

For information about additional fields, see [Getting item recommendations (AWS SDKs)](getting-real-time-item-recommendations.md#get-item-rec-sdk "getting-real-time-item-recommendations.md#get-item-rec-sdk")
and [Getting a personalized ranking using contextual metadata](get-personalized-rankings-sdk.md#personalized-ranking-contextual-metadata-example "get-personalized-rankings-sdk.md#personalized-ranking-contextual-metadata-example").

SDK for Python (Boto3)

```
import boto3

personalizeRt = boto3.client('personalize-runtime')

response = personalizeRt.get_recommendations(
  campaignArn = "`CampaignARN`",
  userId = '`1`',
  numResults = `10`,
  filterArn = '`RequestFilterARN`',
  filterValues = {
      "`RequestFilterParameterName`": "\"value1\"",
      "`RequestFilterParameterName`": "\"value1\",\"value2\",\"value3\""
      ....
  },
  promotions = [{
    "name" : "`promotionName`",
    "percentPromotedItems" : `50`,
    "filterArn": "`promotionFilterARN`",
    "filterValues": {
      "`PromotionParameterName`": "\"`Value1`\",\"`Value2`\""
      ...
    }
  }]
)

print("Recommended items")
for item in response['itemList']:
    print (item['itemId'])
    if ("promotionName" in item):
        print(item['promotionName'])
```

SDK for Java 2.x

```
public static void getRecommendationsWithPromotedItems(PersonalizeRuntimeClient personalizeRuntimeClient,
                                       String campaignArn,
                                       String userId,
                                       String requestFilterArn,
                                       String requestParameterName,
                                       String requestParameterValue1,
                                       String requestParameterValue2,
                                       String promotionName,
                                       int percentPromotedItems,
                                       String promotionFilterArn,
                                       String promotionParameterName,
                                       String promotionParameterValue1,
                                       String promotionParameterValue2) {

  try {

      Map<String, String> promotionFilterValues = new HashMap<>();

      promotionFilterValues.put(promotionParameterName, String.format("\"%1$s\",\"%2$s\"",
              promotionParameterValue1, promotionParameterValue2));

      Promotion newPromotion = Promotion.builder()
              .name(promotionName)
              .percentPromotedItems(percentPromotedItems)
              .filterArn(promotionFilterArn)
              .filterValues(promotionFilterValues)
              .build();

      List<Promotion> promotionList = new List<>();

      promotionList.add(newPromotion);

      Map<String, String> requestfilterValues = new HashMap<>();

      requestfilterValues.put(requestParameterName, String.format("\"%1$s\",\"%2$s\"",
              requestParameterValue1, requestParameterValue2));

      GetRecommendationsRequest recommendationsRequest = GetRecommendationsRequest.builder()
              .campaignArn(campaignArn)
              .numResults(20)
              .userId(userId)
              .filterArn(requestFilterArn)
              .fitlerValues(requestFilterValues)
              .promotions(promotionList)
              .build();

      GetRecommendationsResponse recommendationsResponse = personalizeRuntimeClient.getRecommendations(recommendationsRequest);
      List<PredictedItem> items = recommendationsResponse.itemList();

      for (PredictedItem item: items) {
          System.out.println("Item Id is : "+item.itemId());
          System.out.println("Item score is : "+item.score());
          System.out.println("Promotion name is : "+item.promotionName());
      }
  } catch (PersonalizeRuntimeException e) {
      System.err.println(e.awsErrorDetails().errorMessage());
      System.exit(1);
  }
}
```

SDK for JavaScript v3

```
// Get service clients and commands using ES6 syntax.
import { GetRecommendationsCommand, PersonalizeRuntimeClient } from
  "@aws-sdk/client-personalize-runtime";

// create personalizeRuntimeClient.
const personalizeRuntimeClient = new PersonalizeRuntimeClient({
  region: "REGION",
});

// set recommendation request param
export const getRecommendationsParam = {
  campaignArn: "CAMPAIGN_ARN",  /* required */
  userId: "USER_ID", /* required */
  numResults: 25, /* optional */
  filterArn: "FILTER_ARN", /* provide if you are applying a custom filter */
  filterValues: {
    "PARAM_NAME": "\"PARAM_VALUE\"" /* provide if your filter has a placeholder parameter */
  },
  promotions: [
    {
      name: "PROMOTION_NAME", /* specify the name of the promotion. The recommendation response includes the name to identify promoted items. */
      percentPromotedItems: 50, /* the percentage of recommended items to apply the promotion to. */
      filterArn:
        "PROMOTION_FILTER_ARN", /* the Amazon Resource Name (ARN) of the filter that defines the promotion criteria. */
      filterValues: {
        "PARAM_NAME": "\"PARAM_VALUE\"" /* provide if your promotion filter has a placeholder parameter */
      },
    },
  ],
};

export const run = async () => {
  try {
    const response = await personalizeRuntimeClient.send(new GetRecommendationsCommand(getRecommendationsParam));
    console.log("Success!", "\nItems are: ");
    response.itemList.forEach(element => console.log(element.itemId))
    return response; // For unit tests.
  } catch (err) {
    console.log("Error", err);
  }
};
run();


```

A list of recommended items displays. Promoted items are positioned randomly relative to other recommended items, but in sorted order relative to other promoted items.
Depending on your recipe, recommended
items that aren't part of a promotion are sorted by relevance to the user, popularity, or similarity. If there aren't enough items that meet the promotion criteria, the result will contain as many promoted items as possible.

```
{
  "itemList": [
      {
          "itemId1": "123",
          "score": .0117211,
          "promotionName": "promotionName"
      },
      {
         "itemId2": "456",
         "score": .0077976
      },
      {
         "itemId3": "789",
         "score": .0067171
      },
      .....
 ]
```
