

# Installing the Amazon Personalize Search Ranking plugin on an OpenSearch Service domain
<a name="open-search-install-managed"></a>

After you complete the Amazon Personalize workflow and meet the requirements listed in [Plugin requirements](plugin-requirements.md), you're ready to install the plugin on your domain.

 To use the plugin, you associate the `Amazon_Personalize_Search_Ranking_Plugin` plugin with your domain. The plugin is pre-installed, and you don't have to import it from Amazon S3. You associate the plugin the same way that you associate an OpenSearch Service package. For information about associating an OpenSearch Service package, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html#custom-packages-assoc). 

After you associate the plugin with your domain, you're ready to configure the plugin. You configure it by creating a search pipeline and specifying a `personalized_search_ranking` response processor. For more information, see [Creating a pipeline](managed-opensearch-plugin-pipeline-example.md).

## Additional information about Amazon OpenSearch Service domains
<a name="opensearch-service-additional-information"></a>

The following resources provide additional information about using Amazon OpenSearch Service domain. 
+ For a concise tutorial for configuring a test domain, see [Step 1: Create an Amazon OpenSearch Service domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html#gsgcreate-domain) in the "Getting started" section of the *Amazon OpenSearch Service Developer Guide*.
+ For more detailed steps about configuring OpenSearch Service domains, see [Creating and managing Amazon OpenSearch Service domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/createupdatedomains.html).
+ For a concise tutorial for uploading a small amount of test data to OpenSearch Service, see [Step 2: Upload data to Amazon OpenSearch Service for indexing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gsg.html#gsgupload-data) in the "Getting started" section of the *Amazon OpenSearch Service Developer Guide*.
+ For complete information about ingesting data, see [Indexing data in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/indexing.html) in the *Amazon OpenSearch Service Developer Guide*.