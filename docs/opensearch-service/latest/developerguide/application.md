# Using OpenSearch UI in Amazon OpenSearch Service

OpenSearch UI (user interface) is a modernized operational analytics experience for
Amazon OpenSearch Service that provides a unified view for you to interact with data across multiple sources.
Unlike OpenSearch Dashboards, which works with only the one domain or collection that hosts it,
OpenSearch UI is hosted in the AWS Cloud. This makes it possible for OpenSearch UI to
achieve high availability and stay functional during cluster upgrades, and to natively
connect with multiple data sources. For information about OpenSearch Dashboards, see [Using OpenSearch Dashboards with Amazon OpenSearch Service](dashboards.md "dashboards.md").

The following are key features of OpenSearch UI:

- **Multiple data source support** –
  OpenSearch UI can connect with multiple data sources to create a comprehensive
  view. This includes OpenSearch domains and serverless collections, as well as
  integrated AWS data sources such as Amazon CloudWatch, Amazon Security Lake, and Amazon Simple Storage Service
  (Amazon S3).
- **Zero downtime during upgrades** –
  OpenSearch UI is hosted in the AWS Cloud. This means that OpenSearch remains
  operational and can retrieve data from clusters during upgrade processes.
- **Workspaces** – Curated spaces for team
  collaborations for various workflows, such as Observability, Security Analytics and
  Search. You can define the privacy settings and manage permissions for collaborators
  in your workspace.
- **Single sign-on** – OpenSearch UI works
  with AWS IAM Identity Center and SAML through AWS Identity and Access Management (IAM) federatation to integrate with
  your identity providers to create a single sign-on experience for your end
  users.
- **GenAI-powered analytics** – OpenSearch UI
  supports natural language query generation to help generate the right queries for
  your analysis. OpenSearch UI also works with Amazon Q Developer to provide the Amazon Q chat
  and help generate visualizations, alert summary, insights, and recommended anomaly
  detectors.
- **Multiple query language support** –
  OpenSearch UI supports Piped Processing Language (PPL), SQL, Lucene, and
  Dashboards Query Language (DQL).
- **Cross-Region and cross-account support** –
  OpenSearch UI can utilize the cross-cluster search feature to connect with
  OpenSearch domains in different accounts and different Regions for aggregated
  analysis and visualizations.
  To get started and create your first OpenSearch UI, follow the instructions in [Getting started with the OpenSearch user interface in Amazon OpenSearch Service](application-getting-started.md "application-getting-started.md").

###### Note

**Required IAM permissions:** To access the
OpenSearch UI application, users must have the following IAM permissions:
`es:getApplication`, `es:DescribeApplication`, and
`es:ListApplications`. Without these permissions, users will receive
access denied errors when attempting to access the OpenSearch UI.

For information about the latest features released for OpenSearch UI, see [Amazon OpenSearch Service user interface release history](application-release-history.md "application-release-history.md").

###### Topics

- [Amazon OpenSearch Service user interface release history](application-release-history.md "application-release-history.md")
- [Getting started with the OpenSearch user interface in Amazon OpenSearch Service](application-getting-started.md "application-getting-started.md")
- [Agentic AI in Amazon OpenSearch Service](application-ai-assistant.md "application-ai-assistant.md")
- [Encrypting OpenSearch UI application metadata with customer managed keys](application-encryption-cmk.md "application-encryption-cmk.md")
- [Enabling SAML federation with AWS Identity and Access Management](application-enable-SAML-identity-federation.md "application-enable-SAML-identity-federation.md")
- [Managing data source associations and Virtual Private Cloud access permissions](application-data-sources-and-vpc.md "application-data-sources-and-vpc.md")
- [Using Amazon OpenSearch Service workspaces](application-workspaces.md "application-workspaces.md")
- [Configuring settings and preferences in OpenSearch UI](application-settings.md "application-settings.md")
- [Cross-Region and cross-account data access](application-cross-region-cross-account.md "application-cross-region-cross-account.md")
- [Managing access to the OpenSearch UI from a VPC endpoint](application-access-ui-from-vpc-endpoint.md "application-access-ui-from-vpc-endpoint.md")
- [Restricting network access to OpenSearch UI applications](application-network-access.md "application-network-access.md")
- [Migrating saved objects from OpenSearch Dashboards to OpenSearch UI](application-migration.md "application-migration.md")
- [Monitoring OpenSearch UI with Amazon CloudWatch](application-monitoring.md "application-monitoring.md")
- [Setting up a friendly URL for OpenSearch UI applications (self-service)](application-custom-domain.md "application-custom-domain.md")
- [OpenSearch UI endpoints and quotas](opensearch-ui-endpoints-quotas.md "opensearch-ui-endpoints-quotas.md")
