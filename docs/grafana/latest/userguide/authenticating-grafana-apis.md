# Authenticate with tokens

To use a Grafana API with your Amazon Managed Grafana workspace, you must have a valid Grafana
_token_. The token provides authentication and authorization for
caller of the API. There are two ways to create tokens.

- **Service account** – A service account is
  used to run automated workloads in Grafana, such as provisioning, configuration,
  or report generation. You can create service account tokens for your service
  account. Service accounts are available in Grafana workspaces compatible with
  version 9.x, and are planned to replace API keys as the primary way to
  authenticate applications that interact with Grafana APIs.
- **API Key** – An API key (also called
  an API token) is a randomly generated string that external systems can use to
  interact with Grafana HTTP APIs. API keys are available in versions 8, 9, and
  10 of Grafana workspaces, however, GrafanaLabs has announced that they are
  deprecating them in a future release.

###### Topics

- [Use service accounts to authenticate with the
  Grafana HTTP APIs](service-accounts.md "service-accounts.md")
- [Use API keys to authenticate with Grafana HTTP
  APIs](using-api-keys.md "using-api-keys.md")
