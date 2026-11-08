

# How OpenSearch UI compares to OpenSearch Dashboards
<a name="application-vs-dashboards"></a>

OpenSearch UI and OpenSearch Dashboards are both analytics interfaces for Amazon OpenSearch Service, but they differ in where they run and what they can connect to. OpenSearch Dashboards runs on a single domain. OpenSearch UI is hosted in the AWS Cloud, connects to multiple data sources, remains available during cluster upgrades, and adds workspaces, single sign-on, and generative AI features.

## Feature comparison
<a name="application-vs-dashboards-comparison"></a>

The following table compares OpenSearch UI and OpenSearch Dashboards feature by feature.


| Feature | OpenSearch UI | OpenSearch Dashboards | 
| --- | --- | --- | 
| Hosting | Managed by AWS in the AWS Cloud | Runs on the domain | 
| Data sources | Multiple domains and collections, plus Amazon CloudWatch and Amazon Security Lake | A single domain | 
| Availability during upgrades | Remains available | Unavailable while the domain upgrades | 
| Workspaces | Team-based workspaces for each use case | A single shared space | 
| Single sign-on | AWS IAM Identity Center and SAML federation | SAML only, configured at the domain level | 
| Generative AI features | Amazon Q and natural language queries | Not available | 
| Cross-account and cross-Region access | Supported | Not supported | 
| Query languages | PPL, SQL, DQL, and Lucene | DQL and Lucene | 

## When to continue using OpenSearch Dashboards
<a name="application-vs-dashboards-when"></a>

OpenSearch Dashboards remains the right choice when you need direct access at the domain level, when you depend on custom plugins that OpenSearch UI does not yet support, or in AWS Regions where OpenSearch UI is not yet available. For the Regions where OpenSearch UI is available, see [OpenSearch UI endpoints and quotas](opensearch-ui-endpoints-quotas.md).

To move your existing saved objects, such as dashboards, visualizations, index patterns, and searches, from OpenSearch Dashboards to an OpenSearch UI workspace, see [Migrating saved objects from OpenSearch Dashboards to OpenSearch UI](application-migration.md).