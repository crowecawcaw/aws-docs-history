

# Plugins by engine version in Amazon OpenSearch Service
<a name="supported-plugins"></a>

Amazon OpenSearch Service domains come prepackaged with plugins from the OpenSearch community. The service automatically deploys and manages plugins for you, but it deploys different plugins depending on the version of OpenSearch or legacy Elasticsearch OSS you choose for your domain.

The following table lists plugins by OpenSearch version, as well as compatible versions of legacy Elasticsearch OSS. This table isn't exhaustive; it lists only the plugins that you're most likely to interact with directly. OpenSearch Service uses additional plugins to enable core service functionality, such as the S3 Repository plugin for snapshots and the [OpenSearch Performance Analyzer](https://opensearch.org/docs/latest/monitoring-plugins/pa/index/) plugin for optimization and monitoring. For a complete list of all plugins running on your domain, make the following request:

```
GET _cat/plugins?v
```



<table>
<thead>
  <tr><th>Plugin</th><th>Minimum required OpenSearch version</th><th>Minimum required Elasticsearch version</th></tr>
</thead>
<tbody>
  <tr><td><a href="https://github.com/KennFalcon/elasticsearch-analysis-hanlp">HanLP</a></td><td>2.11</td><td>Not supported</td></tr>
  <tr><td><a href="https://github.com/hotstar/hebrew-analyzer/tree/feature/main-initial">Hebrew Analysis</a></td><td>2.11</td><td>Not supported</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/personalize/latest/dg/personalize-opensearch.html">Amazon Personalize Search Ranking</a></td><td>2.9</td><td>Not supported</td></tr>
  <tr><td><a href="https://opensearch.org/docs/latest/search-plugins/neural-search/">Neural Search</a></td><td>2.9</td><td>Not supported</td></tr>
  <tr><td><a href="https://opensearch.org/docs/latest/security-analytics/index/">Security Analytics</a></td><td>2.5</td><td>Not supported</td></tr>
  <tr><td><a href="https://opensearch.org/docs/latest/notifications-plugin/index/">OpenSearch notifications</a></td><td>2.3</td><td>Not supported</td></tr>
  <tr><td><a href="https://opensearch.org/docs/latest/ml-commons-plugin/index/">ML Commons</a></td><td>1.3</td><td>Not supported</td></tr>
  <tr><td><a href="https://github.com/WorksApplications/elasticsearch-sudachi">Sudachi Analysis</a> (recommended for Japanese)</td><td>1.3</td><td>Not supported</td></tr>
  <tr><td><a href="https://github.com/aparo/opensearch-analysis-stconvert">STConvert</a></td><td>1.3</td><td>Not supported</td></tr>
  <tr><td><a href="https://github.com/aparo/opensearch-analysis-pinyin">Pinyin Analysis</a></td><td>1.3</td><td>Not supported</td></tr>
  <tr><td><a href="https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-nori">Nori Analysis</a></td><td>1.3</td><td>Not supported</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/observability.html">OpenSearch observability</a></td><td>1.2</td><td>Not supported</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/replication.html">OpenSearch cross-cluster replication</a></td><td>1.1</td><td>7.10</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/asynchronous-search.html">OpenSearch asynchronous search</a></td><td>1.0</td><td>7.10</td></tr>
  <tr><td><a href="https://github.com/medcl/elasticsearch-analysis-ik">IK (Chinese) Analysis</a></td><td rowspan="4">1.0</td><td rowspan="4">7.7</td></tr>
  <tr><td><a href="https://github.com/duydo/elasticsearch-analysis-vietnamese">Vietnamese Analysis</a></td></tr>
  <tr><td><a href="https://github.com/tlefsad/elasticsearch-analysis-thaichub2">Thai analysis</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/learning-to-rank.html">Learning to Rank</a></td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ad.html">OpenSearch anomaly detection</a></td><td>1.0</td><td>7.4</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/knn.html">OpenSearch k-NN</a></td><td>1.0</td><td>7.1</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ism.html">OpenSearch Index State Management</a></td><td>1.0</td><td>6.8</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html">OpenSearch security</a></td><td>1.0</td><td>6.7</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/sql-support.html">OpenSearch SQL</a></td><td>1.0</td><td>6.5</td></tr>
  <tr><td><a href="https://docs.aws.amazon.com/opensearch-service/latest/developerguide/alerting.html">OpenSearch alerting</a></td><td>1.0</td><td>6.2</td></tr>
  <tr><td>Ukrainian Analysis</td><td>1.0</td><td>5.3</td></tr>
  <tr><td>Mapper Size</td><td>1.0</td><td>5.3</td></tr>
  <tr><td>Mapper Murmur3</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Ingest User Agent Processor</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Ingest Attachment Processor</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Stempel Polish Analysis</td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Smart Chinese Analysis</td><td>1.0</td><td>5.1</td></tr>
  <tr><td><a href="https://bitbucket.org/eunjeon/seunjeon/src/master/elasticsearch/">Seunjeon Korean Analysis</a></td><td>1.0</td><td>5.1</td></tr>
  <tr><td>Phonetic Analysis</td><td>1.0</td><td>2.3</td></tr>
  <tr><td><a href="https://opensearch.org/docs/latest/analyzers/supported-analyzers/language-analyzers/">Japanese (kuromoji) Analysis</a></td><td>1.0</td><td>Included on all domains</td></tr>
  <tr><td>ICU Analysis</td><td>1.0</td><td>Included on all domains</td></tr>
</tbody>
</table>


## Optional plugins
<a name="plugins-optional"></a>

In addition to the default plugins that come pre-installed, Amazon OpenSearch Service supports several optional language analyzer plugins. You can use the AWS Management Console and AWS CLI to associate a plugin to a domain, disassociate a plugin from a domain, and list all plugins. An optional plugin package is compatible with a specific OpenSearch version, and can only be associated to domains with that version. 

Note that for the [Sudachi plugin](https://github.com/WorksApplications/elasticsearch-sudachi), when you reassociate a dictionary file, it doesn't immediately reflect on the domain. The dictionary refreshes when the next blue/green deployment runs on the domain as part of a configuration change or other update. Alternatively, you can create a new package with the updated data, create a new index using this new package, reindex the existing index to the new index, and then delete the old index. If you prefer to use the reindexing approach, use an index alias so that there's no disruption to your traffic.

Optional plugins use the `ZIP-PLUGIN` package type. For more information about optional plugins, see [Importing and managing packages in Amazon OpenSearch Service](custom-packages.md).