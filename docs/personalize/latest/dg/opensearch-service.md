# Personalizing results from Amazon OpenSearch Service with Amazon Personalize

To personalize OpenSearch results from Amazon OpenSearch Service, you do the following:

1. **Set up Amazon Personalize** – If you haven't already, complete the steps in [Setting up Amazon Personalize](setup.md "setup.md") to set up your credentials and set up permissions for Amazon Personalize. You don't need to
   set up the AWS SDKs to personalize OpenSearch results.
2. **Complete the Amazon Personalize workflow** – Complete the Amazon Personalize workflow to import data, create
   a solution with the Personalized-Ranking-v2 or Personalized-Ranking recipe, train a custom solution version, and deploy it in a campaign.
   You must create an Item interactions dataset. A Users dataset and an Items dataset
   are optional. For more information, see [Amazon Personalize workflow details](personalize-workflow.md "personalize-workflow.md").
3. **Set up permissions** – Set up permissions so you can access your Amazon Personalize resources
   from your OpenSearch Service domain. For more information, see [Setting up permissions](opensearch-granting-access-managed.md "opensearch-granting-access-managed.md").
4. **Install the Amazon Personalize Search Ranking plugin** – This plugin handles communication with Amazon Personalize and
   re-ranking results. For information about installing the plugin on an OpenSearch Service domain, see [Installing the plugin](open-search-install-managed.md "open-search-install-managed.md").
5. **Configure the Amazon Personalize Search Ranking plugin** – To configure the plugin, you create search
   pipelines. _Search pipelines_ are sets of request and response processors. When you
   create a pipeline for the plugin, you specify your Amazon Personalize resources in a `personalized_search_ranking` response processor. You also
   configure how much weight the plugin gives the results from Amazon Personalize when it re-ranks results. For more information, see
   [Creating a pipeline](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md").
6. **Apply the Amazon Personalize Search Ranking plugin to OpenSearch queries** – After you configure a search
   pipeline with a `personalized_search_ranking` response processor, you're ready to apply the Amazon Personalize Search Ranking plugin to your OpenSearch queries
   and view the re-ranked results. For information about applying the plugin to OpenSearch Service queries, see [Applying the plugin](managed-apply-plugin.md "managed-apply-plugin.md").
7. **Compare results** – The Amazon Personalize Search Ranking plugin re-ranks the search results in the OpenSearch
   query response. It considers both the ranking from Amazon Personalize and the ranking from OpenSearch. To understand how results are
   re-ranked, you can compare results from queries that use personalization and those that don't.
   For information about comparing results with OpenSearch Service, see [Comparing results](managed-comparing-results.md "managed-comparing-results.md").
8. **Monitor the Amazon Personalize Search Ranking plugin** – As you apply the Amazon Personalize Search Ranking plugin to search queries, you
   can monitor the plugin by getting metrics for your search pipelines.
   For information about monitoring the plugin with OpenSearch Service, see [Monitoring the plugin](managed-monitor.md "managed-monitor.md").

###### Topics

- [Setting up Amazon OpenSearch Service permissions](opensearch-granting-access-managed.md "opensearch-granting-access-managed.md")
- [Installing the Amazon Personalize Search Ranking plugin on an OpenSearch Service domain](open-search-install-managed.md "open-search-install-managed.md")
- [Creating a pipeline in Amazon OpenSearch Service](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md")
- [Applying the plugin to Amazon OpenSearch Service queries](managed-apply-plugin.md "managed-apply-plugin.md")
- [Comparing personalized Amazon OpenSearch Service results to results without personalization](managed-comparing-results.md "managed-comparing-results.md")
- [Monitoring the plugin with Amazon OpenSearch Service](managed-monitor.md "managed-monitor.md")
