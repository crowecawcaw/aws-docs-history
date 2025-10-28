# Personalizing results from open source Open Search with Amazon Personalize

To personalize results open source OpenSearch, you do the following:

1. **Set up Amazon Personalize** – If you haven't already, complete the steps in [Setting up Amazon Personalize](setup.md "setup.md") to set up your credentials and set up permissions for Amazon Personalize. You don't need to
   set up the AWS SDKs to personalize OpenSearch results.
2. **Complete the Amazon Personalize workflow** – Complete the Amazon Personalize workflow to import data, create
   a solution with the Personalized-Ranking-v2 or Personalized-Ranking recipe recipe, train a custom solution version, and deploy it in a campaign.
   You must create an Item interactions dataset. A Users dataset and an Items dataset
   are optional. For more information, see [Amazon Personalize workflow details](personalize-workflow.md "personalize-workflow.md").
3. **Set up permissions** – Set up permissions so you can access your Amazon Personalize resources
   from your OpenSearch cluster. For more information, see [Setting up permissions](opensearch-granting-access.md "opensearch-granting-access.md").
4. **Install the Amazon Personalize Search Ranking plugin** – The Amazon Personalize Search Ranking plugin handles communication with Amazon Personalize and
   re-ranking results.
   - If you already have an OpenSearch cluster running, you can manually install the plugin. For more information, see
     [Manually installing the plugin on an existing OpenSearch cluster](opensearch-manual-install.md "opensearch-manual-install.md").
   - If you haven't created an OpenSearch cluster, you can use a quickstart bash script to create one. For more
     information, see [Creating a new cluster and installing the plugin with a script](opensearch-install-with-script.md "opensearch-install-with-script.md").

5. **Configure the Amazon Personalize Search Ranking plugin** – To configure the plugin, you create search
   pipelines. _Search pipelines_ are sets of request and response processors. When you
   create a pipeline for the plugin, you specify your Amazon Personalize resources in a `personalized_search_ranking` response processor. You also
   configure how much weight the plugin gives the results from Amazon Personalize when it re-ranks results. For more information, see
   [Creating a pipeline](opensearch-plugin-pipeline-example.md "opensearch-plugin-pipeline-example.md").
6. **Apply the Amazon Personalize Search Ranking plugin to OpenSearch queries** –
   You can apply the Amazon Personalize Search Ranking plugin to all queries and responses for an OpenSearch index. You can also apply the plugin to
   individual OpenSearch queries and responses. For information about applying the plugin to queries in open source OpenSearch, see [Applying the plugin](opensource-apply-plugin.md "opensource-apply-plugin.md").
7. **Compare results** – The Amazon Personalize Search Ranking plugin re-ranks the search results in the OpenSearch
   query response. It considers both the ranking from Amazon Personalize and the ranking from OpenSearch. To understand how results are
   re-ranked, you can compare results from queries that use personalization and those that don't.
   For information about comparing results with open source OpenSearch, see [Comparing results](opensource-comparing-results.md "opensource-comparing-results.md").
8. **Monitor the Amazon Personalize Search Ranking plugin** – As you apply the Amazon Personalize Search Ranking plugin to search queries, you
   can monitor the plugin by getting metrics for your search pipelines. For information about monitoring the plugin on an open source OpenSearch cluster, see [Monitoring the plugin with open source OpenSearch](opensource-monitor.md "opensource-monitor.md"). For an excerpt of the pipeline metrics returned from OpenSearch, see [Pipeline metrics example](monitor-response.md "monitor-response.md").

###### Topics

- [Setting up open source OpenSearch permissions](opensearch-granting-access.md "opensearch-granting-access.md")
- [Manually installing the Amazon Personalize Search Ranking plugin on an existing OpenSearch cluster](opensearch-manual-install.md "opensearch-manual-install.md")
- [Creating a new cluster and installing the plugin with a script](opensearch-install-with-script.md "opensearch-install-with-script.md")
- [Creating a pipeline in open source OpenSearch](opensearch-plugin-pipeline-example.md "opensearch-plugin-pipeline-example.md")
- [Applying the Amazon Personalize Search Ranking plugin to queries in open source OpenSearch](opensource-apply-plugin.md "opensource-apply-plugin.md")
- [Comparing personalized OpenSearch results to results without personalization](opensource-comparing-results.md "opensource-comparing-results.md")
- [Monitoring the plugin with open source OpenSearch](opensource-monitor.md "opensource-monitor.md")
