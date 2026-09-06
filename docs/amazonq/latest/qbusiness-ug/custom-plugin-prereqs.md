

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Prerequisites for Amazon Q Business custom plugins
<a name="custom-plugin-prereqs"></a>

**Before you configure your Amazon Q custom plugin, you must ensure you have the following:**
+ A defined OpenAPI schema in JSON or YAML (maximum size is 1 MB). In order to maximize accuracy with Amazon Q Business custom plugin, follow the [best practices for configuring OpenAPI schema definitions](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins-api-schema-best-practices.html) for custom plugins.
+ If authentication is required to connect Amazon Q to your third-party application, create OAuth authentication credentials. You need to store these authentication credentials in a Secrets Manager secret to connect your third-party application to Amazon Q.