

# Features by engine version in Amazon OpenSearch Service
<a name="features-by-version"></a>

Many OpenSearch Service features have a minimum OpenSearch version requirement or legacy Elasticsearch OSS version requirement. If you meet the minimum version for a feature, but the feature isn't available on your domain, update your domain's [service software](service-software.md).


<table>
<thead>
  <tr><th>Feature</th><th>Minimum required OpenSearch version</th><th>Minimum required Elasticsearch version</th></tr>
</thead>
<tbody>
  <tr><td>Multi-tier architecture </td><td>3.3</td><td>Not included</td></tr>
  <tr><td>Derived source</td><td>3.1</td><td>Not included</td></tr>
  <tr><td>Star-tree index</td><td>2.17</td><td>Not included</td></tr>
  <tr><td>Amazon Q support</td><td>2.17</td><td>Not included</td></tr>
  <tr><td>Custom plugins</td><td>2.15</td><td>Not included</td></tr>
  <tr><td>Concurrent segment search</td><td>2.13</td><td>Not included</td></tr>
  <tr><td>Natural language query generation</td><td>2.13</td><td>Not included</td></tr>
  <tr><td>Multimodal semantic search</td><td>2.11</td><td>Not included</td></tr>
  <tr><td>Direct-query data sources</td><td>2.11</td><td>Not included</td></tr>
  <tr><td>Machine learning connectors</td><td>2.9</td><td>Not included</td></tr>
  <tr><td>Semantic search</td><td>2.9</td><td>Not included</td></tr>
  <tr><td>Point in Time search</td><td>2.5</td><td>Not included</td></tr>
  <tr><td>Notifications</td><td>2.3</td><td>Not included</td></tr>
  <tr><td>ML Commons</td><td>1.3</td><td>Not included</td></tr>
  <tr><td>Cross-cluster replication</td><td>1.1</td><td>7.10</td></tr>
  <tr><td>Index transforms</td><td>1.0</td><td>Not included</td></tr>
  <tr><td>Dedicated coordinator node</td><td>1.0</td><td>6.8</td></tr>
  <tr><td>VPC support</td><td rowspan="7">1.0</td><td rowspan="7">1.0</td></tr>
  <tr><td>Require HTTPS for all traffic to the domain</td></tr>
  <tr><td>Multi-AZ support</td></tr>
  <tr><td>Dedicated master nodes</td></tr>
  <tr><td>Custom packages</td></tr>
  <tr><td>Custom endpoints</td></tr>
  <tr><td>Slow log publishing</td></tr>
  <tr><td>Error log publishing</td><td rowspan="4">1.0</td><td rowspan="4">5.1</td></tr>
  <tr><td>Encryption of data at rest</td></tr>
  <tr><td>Cognito authentication for OpenSearch Dashboards</td></tr>
  <tr><td>In-place upgrades</td></tr>
  <tr><td>Hourly automated snapshots</td><td>1.0</td><td>5.3</td></tr>
  <tr><td>Node-to-node encryption</td><td rowspan="3">1.0</td><td rowspan="3">6.0</td></tr>
  <tr><td>Java high-level REST client support</td></tr>
  <tr><td>HTTP request and response compression</td></tr>
  <tr><td>Alerting</td><td>1.0</td><td>6.2</td></tr>
  <tr><td>SQL</td><td>1.0</td><td>6.5</td></tr>
  <tr><td>Cross-cluster search</td><td rowspan="5">1.0</td><td rowspan="5">6.7</td></tr>
  <tr><td>Fine-grained access control</td></tr>
  <tr><td>SAML authentication for OpenSearch Dashboards</td></tr>
  <tr><td>Auto-Tune</td></tr>
  <tr><td>Remote reindex</td></tr>
  <tr><td>UltraWarm</td><td rowspan="2">1.0</td><td rowspan="2">6.8</td></tr>
  <tr><td>Index State Management</td></tr>
  <tr><td>k-NN by Euclidean distance</td><td>1.0</td><td>7.1</td></tr>
  <tr><td>Anomaly Detection</td><td>1.0</td><td>7.4</td></tr>
  <tr><td>k-NN by cosine similarity</td><td rowspan="2">1.0</td><td rowspan="2">7.7</td></tr>
  <tr><td>Learning to Rank</td></tr>
  <tr><td>Piped processing language</td><td rowspan="5">1.0</td><td rowspan="5">7.9</td></tr>
  <tr><td>OpenSearch Dashboards reports</td></tr>
  <tr><td>OpenSearch Dashboards Trace Analytics</td></tr>
  <tr><td>ARM-based Graviton instances</td></tr>
  <tr><td>Cold storage</td></tr>
  <tr><td>Hamming distance, L1 Norm distance, and Painless scripting for k-NN</td><td rowspan="2">1.0</td><td rowspan="2">7.10</td></tr>
  <tr><td>Asynchronous search</td></tr>
  <tr><td>Curator support</td><td>Not included</td><td>5.1</td></tr>
</tbody>
</table>


For information about plugins, which enable some of these features and additional functionality, see [Plugins by engine version in Amazon OpenSearch Service](supported-plugins.md). For information about the OpenSearch API for each version, see [Supported operations in Amazon OpenSearch Service](supported-operations.md).