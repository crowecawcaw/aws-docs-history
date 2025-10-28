# Custom plugins for Amazon Q Business

You can use the Amazon Q Business console or APIs to create custom plugins for your
Amazon Q application.

With custom plugins, you can choose to integrate Amazon Q with any third-party
application for a variety of different use cases. Once enabled, end users can use natural
language to query data (like available calendar slots, stock prices, vacation balance), and
take actions (like booking a meeting, submitting vacation time, updating a record).

To create a custom plugin, you need to perform the following steps:

- Configure authentication and network information to connect Amazon Q Business to your third-party application.
- Create or edit an OpenAPI schema outlining the different API operations you want
  to enable for your custom plugin in JSON or YAML format.

You can upload the OpenAPI schema file to Amazon S3 or you can paste it in the OpenAPI
text editor in the Amazon Q Business console, which will validate your schema.
You can configure up to 20 API operations per custom plugin.
Once your custom plugin is deployed, Amazon Q Business will dynamically determine
the appropriate APIs to call to accomplish an end user requested task. In order to maximize
plugin accuracy, review the [best practices for configuring OpenAPI schema definitions](plugins-api-schema-best-practices.md "plugins-api-schema-best-practices.md")
for custom plugins.

###### Note

Creating custom forms with array fields (fields with nested objects inside an array)
for custom plugins isn't supported on the console.

###### Topics

- [Prerequisites for Amazon Q Business custom plugins](custom-plugin-prereqs.md "custom-plugin-prereqs.md")
- [Service access roles for Amazon Q Business custom plugins](create-plugin-iam-role.md "create-plugin-iam-role.md")
- [Defining OpenAPI schemas for custom plugins](plugins-api-schema.md "plugins-api-schema.md")
- [Best practices for OpenAPI schema
  definition for custom plugins](plugins-api-schema-best-practices.md "plugins-api-schema-best-practices.md")
- [Creating an Amazon Q Business custom
  plugin](custom-plugin-create.md "custom-plugin-create.md")
- [Using an Amazon Q Business custom
  plugin](using-custom-plugin.md "using-custom-plugin.md")
