# Creating a new cluster and installing the plugin with a script

If you haven't created an OpenSearch cluster, you can use a quickstart bash script to create one. This script sets
up an OpenSearch cluster in a Docker container, sets up credentials using your default AWS profile, and installs the
Amazon Personalize Search Ranking plugin.

For information about manually creating an OpenSearch cluster, see the [Quickstart](https://opensearch.org/docs/quickstart "https://opensearch.org/docs/quickstart") instructions in the OpenSearch documentation.

###### To install the plugin with a quickstart bash script

1. Before you run the script, download and install [Docker
   Desktop](https://docs.docker.com/get-docker/ "https://docs.docker.com/get-docker/") for your operating system.
2. Download the [quick start bash script](https://github.com/opensearch-project/search-processor/blob/main/helpers/personalized_search_ranking_quickstart.sh "https://github.com/opensearch-project/search-processor/blob/main/helpers/personalized_search_ranking_quickstart.sh") from GitHub.
3. In your working directory, run the script with the following command.

```
sh personalized_search_ranking_quickstart.sh
```

With this command, the script uses the credentials in your default AWS profile. To provide an alternate
profile, use the `--profile` argument.

```
sh personalized_search_ranking_quickstart.sh --profile `profile-name`
```

After you run the script, you can find more information about the script in the README file that's located in
the unique directory created by the script. This directory stores the Dockerfile and docker-compose.yml files that
the script uses. For example: `../opensearch-personalize-intelligent-ranking-docker.1234/README`. 4. Upload your catalog data to your OpenSearch cluster. When you upload your data, you create an OpenSearch index
and define your field mappings. Then you upload your data to that index. For an example, see [Create
an index and field mappings using sample data](https://opensearch.org/docs/latest/quickstart/#create-an-index-and-field-mappings-using-sample-data "https://opensearch.org/docs/latest/quickstart/#create-an-index-and-field-mappings-using-sample-data").
After you set up OpenSearch and install the Amazon Personalize Search Ranking plugin, you're ready to configure it. You configure the plugin
by creating a search pipeline and specifying a `personalized_search_ranking` response processor. For more information, see [Creating a pipeline](opensearch-plugin-pipeline-example.md "opensearch-plugin-pipeline-example.md").
