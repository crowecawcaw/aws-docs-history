# Prerequisites for Amazon Q Business custom plugins

**Before you configure your Amazon Q custom plugin, you must
ensure you have the following:**

- A defined OpenAPI schema in JSON or YAML (maximum size is 1 MB). In order to
  maximize accuracy with Amazon Q Business custom plugin, follow the [best practices for configuring OpenAPI schema
  definitions](plugins-api-schema-best-practices.md "plugins-api-schema-best-practices.md") for custom plugins.
- If authentication is required to connect Amazon Q to your third-party
  application, create OAuth authentication credentials. You need to store these
  authentication credentials in a Secrets Manager secret to connect your third-party
  application to Amazon Q.
