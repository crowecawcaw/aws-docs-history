# Manually installing the Amazon Personalize Search Ranking plugin on an existing OpenSearch cluster

If you already have an OpenSearch cluster, you can manually install the plugin on your cluster directly from the
OpenSearch GitHub repository.

###### To manually install the plugin

1. Use the following command to start your OpenSearch cluster:

```
bin/opensearch
```

2. If you haven't already, upload your catalog data to your OpenSearch cluster. When you upload your data, you
   create an OpenSearch index and define your field mappings. Then you upload your data to that index. For an example,
   see [Create an index and field mappings using sample data](https://opensearch.org/docs/latest/quickstart/#create-an-index-and-field-mappings-using-sample-data "https://opensearch.org/docs/latest/quickstart/#create-an-index-and-field-mappings-using-sample-data").
3. Use the following command to install the plugin:

```
bin/opensearch-plugin install https://github.com/opensearch-project/search-processor/releases/download/2.9.0/opensearch-search-processor-2.9.0.0.zip
```

For more information about installing plugins, see [Installing plugins](https://opensearch.org/docs/latest/install-and-configure/plugins/ "https://opensearch.org/docs/latest/install-and-configure/plugins/").
After you install the Amazon Personalize Search Ranking plugin, you're ready to configure it. You configure the plugin by creating a search
pipeline and specifying a `personalized_search_ranking` response processor. For more information, see [Creating a pipeline](opensearch-plugin-pipeline-example.md "opensearch-plugin-pipeline-example.md").
