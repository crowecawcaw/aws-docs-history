# Amazon Personalize Search Ranking plugin requirements

Before you start personalizing results from OpenSearch, note the following guidelines and requirements for the
Amazon Personalize Search Ranking plugin:

- You must use OpenSearch version 2.9.0 or later. If you use Amazon OpenSearch Service, your domain must use version
  2.9 or later.
- If you haven't already, complete the instructions in [Setting up permissions](aws-personalize-set-up-permissions.md "aws-personalize-set-up-permissions.md") to grant your users permission to access Amazon Personalize and give Amazon Personalize
  permission to access your resources in Amazon Personalize.
- You must be able to access your Amazon Personalize resources from your OpenSearch Service domain or open source OpenSearch cluster.
  - For information about granting access for an OpenSearch Service domain, see [Setting up Amazon OpenSearch Service permissions](opensearch-granting-access-managed.md "opensearch-granting-access-managed.md").
  - For information about granting access for an OpenSearch cluster, see [Setting up open source OpenSearch permissions](opensearch-granting-access.md "opensearch-granting-access.md").

- You can use only custom Amazon Personalize resources. If you created a Domain dataset group, you can still add custom
  resources.
- You can use only the custom recipes
  [Personalized-Ranking-v2 recipe](native-recipe-personalized-ranking-v2.md "native-recipe-personalized-ranking-v2.md") or
  [Personalized-Ranking recipe](native-recipe-search.md "native-recipe-search.md").
- You must create an Item interactions dataset in Amazon Personalize. Items and Users datasets are optional.
- You can't apply Amazon Personalize filters when you're using the Amazon Personalize Search Ranking plugin.
- By default, the plugin assumes that the `_id` for an indexed document in OpenSearch matches the itemId
  in your Amazon Personalize data. If your OpenSearch data uses a different field that corresponds with your Amazon Personalize itemIds, you
  must specify the name of the field when you configure the plugin.
- The userId that you use for a user making a query must match their userId in the data you import into
  Amazon Personalize.
- The plugin re-ranks only the top 500 search results from OpenSearch. The remaining items are not re-ranked and end
  up at the bottom of the list.
