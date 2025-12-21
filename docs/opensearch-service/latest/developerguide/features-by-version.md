# Features by engine version in Amazon OpenSearch Service

Many OpenSearch Service features have a minimum OpenSearch version requirement or legacy
Elasticsearch OSS version requirement. If you meet the minimum version for a feature,
but the feature isn't available on your domain, update your domain's [service software](service-software.md "service-software.md").

| Feature                                                                | Minimum required OpenSearch version | Minimum required Elasticsearch version |
| ---------------------------------------------------------------------- | ----------------------------------- | -------------------------------------- |
| Multi-tier architecture                                                | 3.3                                 | Not included                           |
| Derived source                                                         | 3.1                                 | Not included                           |
| Star-tree index                                                        | 2.17                                | Not included                           |
| Amazon Q support                                                       | 2.17                                | Not included                           |
| Custom plugins                                                         | 2.15                                | Not included                           |
| Concurrent segment search                                              | 2.13                                | Not included                           |
| Natural language query generation                                      | 2.13                                | Not included                           |
| Multimodal semantic search                                             | 2.11                                | Not included                           |
| Direct-query data sources                                              | 2.11                                | Not included                           |
| Machine learning connectors                                            | 2.9                                 | Not included                           |
| Semantic search                                                        | 2.9                                 | Not included                           |
| Point in Time search                                                   | 2.5                                 | Not included                           |
| Notifications                                                          | 2.3                                 | Not included                           |
| ML Commons                                                             | 1.3                                 | Not included                           |
| Cross-cluster replication                                              | 1.1                                 | 7.10                                   |
| Index transforms                                                       | 1.0                                 | Not included                           |
| Dedicated coordinator node                                             | 1.0                                 | 6.8                                    |
| VPC support                                                            | 1.0                                 | 1.0                                    |
| Require HTTPS for all traffic to the domain                            |
| Multi-AZ support                                                       |
| Dedicated master nodes                                                 |
| Custom packages                                                        |
| Custom endpoints                                                       |
| Slow log publishing                                                    |
| Error log publishing                                                   | 1.0                                 | 5.1                                    |
| Encryption of data at rest                                             |
| Cognito authentication for OpenSearch Dashboards                       |
| In-place upgrades                                                      |
| Hourly automated snapshots                                             | 1.0                                 | 5.3                                    |
| Node-to-node encryption                                                | 1.0                                 | 6.0                                    |
| Java high-level REST client support                                    |
| HTTP request and response compression                                  |
| Alerting                                                               | 1.0                                 | 6.2                                    |
| SQL                                                                    | 1.0                                 | 6.5                                    |
| Cross-cluster search                                                   | 1.0                                 | 6.7                                    |
| Fine-grained access control                                            |
| SAML authentication for OpenSearch Dashboards                          |
| Auto-Tune                                                              |
| Remote reindex                                                         |
| UltraWarm                                                              | 1.0                                 | 6.8                                    |
| Index State Management                                                 |
| k-NN by Euclidean distance                                             | 1.0                                 | 7.1                                    |
| Anomaly Detection                                                      | 1.0                                 | 7.4                                    |
| k-NN by cosine similarity                                              | 1.0                                 | 7.7                                    |
| Learning to Rank                                                       |
| Piped processing language                                              | 1.0                                 | 7.9                                    |
| OpenSearch Dashboards reports                                          |
| OpenSearch Dashboards Trace Analytics                                  |
| ARM-based Graviton instances                                           |
| Cold storage                                                           |
| Hamming distance, L1 Norm distance, and Painless scripting for<br>k-NN | 1.0                                 | 7.10                                   |
| Asynchronous search                                                    |
| Curator support                                                        | Not included                        | 5.1                                    |

For information about plugins, which enable some of these features and additional
functionality, see [Plugins by engine version in Amazon OpenSearch Service](supported-plugins.md "supported-plugins.md"). For information about the
OpenSearch API for each version, see [Supported operations in Amazon OpenSearch Service](supported-operations.md "supported-operations.md").
