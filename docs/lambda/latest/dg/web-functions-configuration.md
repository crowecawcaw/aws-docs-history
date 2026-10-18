

# Configuring Lambda Web Functions
<a name="web-functions-configuration"></a>

You configure most Web Function settings on a revision, which is an immutable snapshot of your application code and configuration. Because a revision is immutable, changing a revision setting means creating a new revision with the updated values. You set tags and the resource-based policy on the Web Function. Its revisions and endpoints inherit its tags, and the resource-based policy controls who can act on the Web Function, its revisions, and its endpoints. Endpoint settings apply to each endpoint, including authentication type, auto-deployment mode, revision weights, scaling, and throttling. You can change these without creating a new revision. The following topics describe the settings you can configure.

**Topics**
+ [Web Function deployment package](web-functions-configuration-deployment-package.md)
+ [Instruction set architecture](web-functions-configuration-architecture.md)
+ [Request timeout](web-functions-revisions-timeout.md)
+ [Environment variables](web-functions-revisions-env-vars.md)
+ [Tagging Web Functions](web-functions-configuration-tags.md)
+ [Using the metadata endpoint](web-functions-configuration-metadata-endpoint.md)