

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Custom plugins FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-custom-plugins"></a>

Questions about running your own Python plugins from public and private repositories on the Amazon Timestream for InfluxDB 3 processing engine. For the complete guide, see [Use custom plugins with the processing engine](influxdb3-custom-plugins.md).

**What is a custom plugin?**  
 A custom plugin is a Python plugin that you write (rather than one of the InfluxData certified plugins) and run on the Timestream for InfluxDB 3 processing engine. You attach it to a trigger to transform data, send alerts, aggregate data, or expose a custom HTTP endpoint. 

**Which editions support custom plugins?**  
 Custom plugins run on both Timestream for InfluxDB 3 Core and Enterprise editions. Set the plugin repository parameters under `InfluxDBv3Core` or `InfluxDBv3Enterprise` in your parameter group to match your cluster's edition. 

**Do I need to enable custom plugins?**  
 Custom plugins must be enabled for your AWS account. You then enable them per cluster by creating a DB parameter group that sets `pluginRepositoryUrl` (and, for a private repository, `pluginRepositorySecretArn`) and applying it to the cluster with `create-db-cluster` or `update-db-cluster`. 

**What is the difference between a public and a private repository?**  
 Both are configured the same way – a `pluginRepositoryUrl` on the parameter group. For a private repository, you additionally store a read-only access token in a Secrets Manager secret named `InfluxDB-RepoToken-*` and reference its ARN as `pluginRepositorySecretArn`, so the engine can authenticate when it fetches your plugins. 

**How do I change the plugin repository for my cluster?**  
 The repository parameters are immutable on an existing parameter group. Create a new parameter group with the new `pluginRepositoryUrl` (and secret ARN, if private), then apply it to the cluster with `update-db-cluster --db-parameter-group-identifier`. Applying a parameter group runs a cluster maintenance action. 

**Can I use plugins from more than one repository on the same cluster – for example, the public InfluxData repository and my own repository?**  
 Yes. Set the `pluginRepositoryUrl` base to the raw-content host only (no owner or repository), and give each trigger the full owner/repository/branch/path in its `gh:` path. Note the security tradeoff: a host-only base lets the cluster load plugin code from any repository the host can serve, so use it only when you genuinely need multiple repositories. For the full configuration, examples, and security guidance, see [Use multiple plugin repositories](influxdb3-custom-plugins.md#influxdb3-custom-plugins-multiple-repos). 

**In which AWS Regions is this available?**  
 Custom plugins are available in all AWS Regions where Timestream for InfluxDB 3 is available unless noted otherwise. 

**Is there an additional charge for running custom plugins?**  
 There is no separate charge for the custom plugin feature. Plugin execution consumes the compute and memory of the cluster instances it runs on, so heavier plugins can affect the resources available for ingestion and queries. 

**How do I add Python package dependencies my plugin needs?**  
 You can use the Python standard library and the pre-installed, Amazon-vetted libraries (such as `numpy`, `pandas`, and `httpx`). The package manager is disabled, so you cannot install additional third-party packages. If a plugin imports a package that is not available, the trigger fails and the import error appears in `system.processing_engine_logs`. 

**How are my private repository credentials protected?**  
 You store a repository access token as a plain string in a Secrets Manager secret named `InfluxDB-RepoToken-*`, and Amazon Timestream for InfluxDB reads that secret with its service-linked role to fetch your plugins. Use a least-privileged, read-only token and rotate it by updating the secret value. To restrict access to only the service, attach the resource policies in [Restrict the secret and CMK to Timestream for InfluxDB (resource policies)](influxdb3-custom-plugins.md#influxdb3-custom-plugins-resource-policies). Never hard-code tokens or other secrets in plugin source. 

**What happens if my repository token expires or the repository becomes unreachable?**  
 If the token expires, the secret is deleted, or the repository cannot be reached, plugin retrieval fails the next time the engine loads plugins. Keep the token valid and update the secret when you rotate it. Check `system.processing_engine_logs` for retrieval errors. 

**Can I use custom plugins on a multi-node cluster?**  
 Yes. As with certified plugins, place plugins according to node roles: data write plugins on ingester nodes, HTTP request plugins on querier nodes, and scheduled plugins on any node with a scheduler. Keep plugin configuration identical across the relevant nodes. For details, see [Distributed deployment considerations](processing-engine.md#distributed-deployment-considerations). 

**My custom plugin is not running. How do I troubleshoot it?**  
 Query `system.processing_engine_logs` for the trigger name to see load and runtime errors, and confirm the trigger is enabled with `system.processing_engine_triggers`. Common causes are an incorrect `gh:` path, a missing Python dependency, or (for private repositories) a token that cannot read the repository. See [Troubleshoot custom plugins](influxdb3-custom-plugins.md#influxdb3-custom-plugins-troubleshooting). 