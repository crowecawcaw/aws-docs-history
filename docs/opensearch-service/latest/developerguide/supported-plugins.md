# Plugins by engine version in Amazon OpenSearch Service

Amazon OpenSearch Service domains come prepackaged with plugins from the OpenSearch community. The
service automatically deploys and manages plugins for you, but it deploys different
plugins depending on the version of OpenSearch or legacy Elasticsearch OSS you choose for
your domain.

The following table lists plugins by OpenSearch version, as well as compatible versions
of legacy Elasticsearch OSS. It only includes plugins that you might interact
with—it’s not comprehensive. OpenSearch Service uses additional plugins to enable core service
functionality, such as the S3 Repository plugin for snapshots and the [OpenSearch
Performance Analyzer](https://opensearch.org/docs/latest/monitoring-plugins/pa/index/ "https://opensearch.org/docs/latest/monitoring-plugins/pa/index/") plugin for optimization and monitoring. For a complete
list of all plugins running on your domain, make the following request:

```
GET _cat/plugins?v
```

| Plugin                                                                                                                                                                               | Minimum required OpenSearch version | Minimum required Elasticsearch version |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | -------------------------------------- |
| [HanLP](https://github.com/KennFalcon/elasticsearch-analysis-hanlp "https://github.com/KennFalcon/elasticsearch-analysis-hanlp")                                                     | 2.11                                | Not supported                          |
| [Hebrew Analysis](https://github.com/hotstar/hebrew-analyzer/tree/feature/main-initial "https://github.com/hotstar/hebrew-analyzer/tree/feature/main-initial")                       | 2.11                                | Not supported                          |
| [Amazon Personalize<br>Search Ranking](../../../personalize/latest/dg/personalize-opensearch.md "../../../personalize/latest/dg/personalize-opensearch.md")                          | 2.9                                 | Not supported                          |
| [Neural Search](https://opensearch.org/docs/latest/search-plugins/neural-search/ "https://opensearch.org/docs/latest/search-plugins/neural-search/")                                 | 2.9                                 | Not supported                          |
| [Security Analytics](https://opensearch.org/docs/latest/security-analytics/index/ "https://opensearch.org/docs/latest/security-analytics/index/")                                    | 2.5                                 | Not supported                          |
| [OpenSearch notifications](https://opensearch.org/docs/latest/notifications-plugin/index/ "https://opensearch.org/docs/latest/notifications-plugin/index/")                          | 2.3                                 | Not supported                          |
| [ML Commons](https://opensearch.org/docs/latest/ml-commons-plugin/index/ "https://opensearch.org/docs/latest/ml-commons-plugin/index/")                                              | 1.3                                 | Not supported                          |
| [Sudachi Analysis](https://github.com/WorksApplications/elasticsearch-sudachi "https://github.com/WorksApplications/elasticsearch-sudachi") (recommended for Japanese)               | 1.3                                 | Not supported                          |
| [STConvert](https://github.com/aparo/opensearch-analysis-stconvert "https://github.com/aparo/opensearch-analysis-stconvert")                                                         | 1.3                                 | Not supported                          |
| [Pinyin Analysis](https://github.com/aparo/opensearch-analysis-pinyin "https://github.com/aparo/opensearch-analysis-pinyin")                                                         | 1.3                                 | Not supported                          |
| [Nori Analysis](https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-nori "https://github.com/opensearch-project/OpenSearch/tree/main/plugins/analysis-nori") | 1.3                                 | Not supported                          |
| [OpenSearch observability](observability.md "observability.md")                                                                                                                      | 1.2                                 | Not supported                          |
| [OpenSearch cross-cluster replication](replication.md "replication.md")                                                                                                              | 1.1                                 | 7.10                                   |
| [OpenSearch asynchronous search](asynchronous-search.md "asynchronous-search.md")                                                                                                    | 1.0                                 | 7.10                                   |
| [IK<br>(Chinese) Analysis](https://github.com/medcl/elasticsearch-analysis-ik "https://github.com/medcl/elasticsearch-analysis-ik")                                                  | 1.0                                 | 7.7                                    |
| [Vietnamese Analysis](https://github.com/duydo/elasticsearch-analysis-vietnamese "https://github.com/duydo/elasticsearch-analysis-vietnamese")                                       |
| [Thai analysis](https://github.com/tlefsad/elasticsearch-analysis-thaichub2 "https://github.com/tlefsad/elasticsearch-analysis-thaichub2")                                           |
| [Learning to Rank](learning-to-rank.md "learning-to-rank.md")                                                                                                                        |
| [OpenSearch anomaly detection](ad.md "ad.md")                                                                                                                                        | 1.0                                 | 7.4                                    |
| [OpenSearch k-NN](knn.md "knn.md")                                                                                                                                                   | 1.0                                 | 7.1                                    |
| [OpenSearch Index State Management](ism.md "ism.md")                                                                                                                                 | 1.0                                 | 6.8                                    |
| [OpenSearch security](fgac.md "fgac.md")                                                                                                                                             | 1.0                                 | 6.7                                    |
| [OpenSearch SQL](sql-support.md "sql-support.md")                                                                                                                                    | 1.0                                 | 6.5                                    |
| [OpenSearch alerting](alerting.md "alerting.md")                                                                                                                                     | 1.0                                 | 6.2                                    |
| Ukrainian Analysis                                                                                                                                                                   | 1.0                                 | 5.3                                    |
| Mapper Size                                                                                                                                                                          | 1.0                                 | 5.3                                    |
| Mapper Murmur3                                                                                                                                                                       | 1.0                                 | 5.1                                    |
| Ingest User Agent Processor                                                                                                                                                          | 1.0                                 | 5.1                                    |
| Ingest Attachment Processor                                                                                                                                                          | 1.0                                 | 5.1                                    |
| Stempel Polish Analysis                                                                                                                                                              | 1.0                                 | 5.1                                    |
| Smart Chinese Analysis                                                                                                                                                               | 1.0                                 | 5.1                                    |
| [Seunjeon Korean Analysis](https://bitbucket.org/eunjeon/seunjeon/src/master/elasticsearch/ "https://bitbucket.org/eunjeon/seunjeon/src/master/elasticsearch/")                      | 1.0                                 | 5.1                                    |
| Phonetic Analysis                                                                                                                                                                    | 1.0                                 | 2.3                                    |
| Japanese (kuromoji) Analysis                                                                                                                                                         | 1.0                                 | Included on all domains                |
| ICU Analysis                                                                                                                                                                         | 1.0                                 | Included on all domains                |

## Optional plugins

In addition to the default plugins that come pre-installed, Amazon OpenSearch Service supports
several optional language analyzer plugins. You can use the AWS Management Console and AWS CLI to
associate a plugin to a domain, disassociate a plugin from a domain, and list all
plugins. An optional plugin package is compatible with a specific OpenSearch version,
and can only be associated to domains with that version.

Note that for the [Sudachi
plugin](https://github.com/WorksApplications/elasticsearch-sudachi "https://github.com/WorksApplications/elasticsearch-sudachi"), when you reassociate a dictionary file, it doesn't immediately
reflect on the domain. The dictionary refreshes when the next blue/green deployment
runs on the domain as part of a configuration change or other update. Alternatively,
you can create a new package with the updated data, create a new index using this
new package, reindex the existing index to the new index, and then delete the old
index. If you prefer to use the reindexing approach, use an index alias so that
there's no disruption to your traffic.

Optional plugins use the `ZIP-PLUGIN` package type. For more
information about optional plugins, see [Importing and managing packages in Amazon OpenSearch Service](custom-packages.md "custom-packages.md").
