# Installing the Amazon Personalize Search Ranking plugin on an OpenSearch Service domain

After you complete the Amazon Personalize workflow and meet the requirements listed in [Plugin requirements](plugin-requirements.md "plugin-requirements.md"), you're ready to install the plugin
on your domain.

To use the plugin, you associate the `Amazon_Personalize_Search_Ranking_Plugin` plugin with your domain. The plugin is
pre-installed, and you don't have to import it from Amazon S3. You associate the plugin the same way that you associate an
OpenSearch Service package. For information about associating an OpenSearch Service package, see [Custom packages for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/custom-packages.md#custom-packages-assoc "../../../opensearch-service/latest/developerguide/custom-packages.md#custom-packages-assoc").

After you associate the plugin with your domain, you're ready to configure the plugin. You
configure it by creating a search pipeline and specifying a `personalized_search_ranking` response processor. For more information, see
[Creating a pipeline](managed-opensearch-plugin-pipeline-example.md "managed-opensearch-plugin-pipeline-example.md").

## Additional information about Amazon OpenSearch Service domains

The following resources provide additional information about using Amazon OpenSearch Service domain.

- For a concise tutorial for configuring a test domain, see [Step 1: Create an Amazon OpenSearch
  Service domain](../../../opensearch-service/latest/developerguide/gsg.md#gsgcreate-domain "../../../opensearch-service/latest/developerguide/gsg.md#gsgcreate-domain") in the "Getting started" section of the _Amazon OpenSearch Service Developer Guide_.
- For more detailed steps about configuring OpenSearch Service domains, see [Creating and managing Amazon OpenSearch Service
  domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md").
- For a concise tutorial for uploading a small amount of test data to OpenSearch Service, see [Step 2: Upload data to Amazon OpenSearch Service for
  indexing](../../../opensearch-service/latest/developerguide/gsg.md#gsgupload-data "../../../opensearch-service/latest/developerguide/gsg.md#gsgupload-data") in the "Getting started" section of the _Amazon OpenSearch Service Developer Guide_.
- For complete information about ingesting data, see [Indexing data in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/indexing.md "../../../opensearch-service/latest/developerguide/indexing.md") in the
  _Amazon OpenSearch Service Developer Guide_.
