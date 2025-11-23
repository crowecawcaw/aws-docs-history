# Machine learning for Amazon OpenSearch Service

ML Commons is an OpenSearch plugin that provides a set of common machine learning (ML)
algorithms through transport and REST API calls. Those calls choose the right nodes and
resources for each ML request and monitors ML tasks to ensure uptime. This allows you to
leverage existing open-source ML algorithms and reduce the effort required to develop new ML
features. For more about the plugin, see [Machine
learning](https://opensearch.org/docs/latest/ml-commons-plugin/index/ "https://opensearch.org/docs/latest/ml-commons-plugin/index/") in the OpenSearch documentation. This chapter covers how to use the
plugin with Amazon OpenSearch Service.

###### Topics

- [Amazon OpenSearch Service ML connectors for
  AWS services](ml-amazon-connector.md "ml-amazon-connector.md")
- [Amazon OpenSearch Service ML connectors for third-party
  platforms](ml-external-connector.md "ml-external-connector.md")
- [Using CloudFormation to set up remote inference for semantic
  search](cfn-template.md "cfn-template.md")
- [Unsupported ML Commons settings](#sm "#sm")
- [OpenSearch Service flow framework templates](ml-workflow-framework.md "ml-workflow-framework.md")

## Unsupported ML Commons settings

Amazon OpenSearch Service doesn't support use of the following ML Commons settings:

- `plugins.ml_commons.allow_registering_model_via_url`
- `plugins.ml_commons.allow_registering_model_via_local_file`

###### Important

On _production clusters_, do not disable the
cluster setting `plugins.ml_commons.only_run_on_ml_node` (don't set it to
`false`). The option to disable this safeguard is for facilitating
development, but production clusters should be using the connectors. For more
information, see [Amazon OpenSearch Service ML connectors for
AWS services](ml-amazon-connector.md "ml-amazon-connector.md").

For more information on ML Commons settings, see [ML
Commons cluster settings](https://opensearch.org/docs/latest/ml-commons-plugin/cluster-settings/ "https://opensearch.org/docs/latest/ml-commons-plugin/cluster-settings/").
