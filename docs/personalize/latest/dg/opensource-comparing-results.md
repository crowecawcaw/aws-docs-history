# Comparing personalized OpenSearch results to results without personalization

To understand how results are re-ranked, you can run queries with the [Dev Tools console](https://opensearch.org/docs/latest/dashboards/dev-tools/run-queries "https://opensearch.org/docs/latest/dashboards/dev-tools/run-queries") in two separate
browser windows. Then you can compare results for queries with and without personalization.

###### To compare results with the Dev Tools console

1. Make sure OpenSearch Dashboards is installed. The quickstart bash script installs OpenSearch Dashboards. If you
   don't use the script or already have a cluster running, you must install OpenSearch Dashboards. For more information,
   see [Installing
   OpenSearch Dashboards](https://opensearch.org/docs/latest/install-and-configure/install-dashboards/index/ "https://opensearch.org/docs/latest/install-and-configure/install-dashboards/index/").
2. Launch OpenSearch Dashboards. Open `http://localhost:5601` from a browser and sign in to OpenSearch
   Dashboards. The default credentials are username 'admin' and password 'admin'.
3. Choose **Dev Tools** under the Management menu on the OpenSearch Dashboards home page.
4. Open a separate browser window and open the Dev Tools console again. You can use the URL from the previous
   window.
5. In one window, enter a query that doesn't use any re-ranking for personalization. In the other window, enter a
   curl command that uses a pipeline with the `personalized_search_ranking` response processor. If you paste a curl command directly
   into the console, the command is automatically converted into the format that the console uses. For a command example,
   see [Applying the Amazon Personalize Search Ranking plugin to queries in open source OpenSearch](opensource-apply-plugin.md "opensource-apply-plugin.md").
6. Run both queries and compare the results.
