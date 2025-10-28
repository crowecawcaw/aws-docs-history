# Operations

The Amazon EventBridge Schemas REST API includes the following operations.

- [CreateDiscoverer](v1-discoverers.md#CreateDiscoverer "v1-discoverers.md#CreateDiscoverer")

Creates a discoverer.

Due to no name being passed in the CreateDiscoverer API call there is no resource to DENY against when the customer adds a resource ARN of an existing discoverer in their IAM policies.

- [CreateRegistry](v1-registries-name-registryname.md#CreateRegistry "v1-registries-name-registryname.md#CreateRegistry")

Creates a registry.

- [CreateSchema](v1-registries-name-registryname-schemas-name-schemaname.md#CreateSchema "v1-registries-name-registryname-schemas-name-schemaname.md#CreateSchema")

Creates a schema definition.

###### Note

Inactive schemas will be deleted after two years.

- [DeleteDiscoverer](v1-discoverers-id-discovererid.md#DeleteDiscoverer "v1-discoverers-id-discovererid.md#DeleteDiscoverer")

Deletes a discoverer.

- [DeleteRegistry](v1-registries-name-registryname.md#DeleteRegistry "v1-registries-name-registryname.md#DeleteRegistry")

Deletes a Registry.

- [DeleteResourcePolicy](v1-policy.md#DeleteResourcePolicy "v1-policy.md#DeleteResourcePolicy")

Delete the resource-based policy attached to the specified registry.

- [DeleteSchema](v1-registries-name-registryname-schemas-name-schemaname.md#DeleteSchema "v1-registries-name-registryname-schemas-name-schemaname.md#DeleteSchema")

Delete a schema definition.

- [DeleteSchemaVersion](v1-registries-name-registryname-schemas-name-schemaname-version-schemaversion.md#DeleteSchemaVersion "v1-registries-name-registryname-schemas-name-schemaname-version-schemaversion.md#DeleteSchemaVersion")

Delete the schema version definition

- [DescribeCodeBinding](v1-registries-name-registryname-schemas-name-schemaname-language-language.md#DescribeCodeBinding "v1-registries-name-registryname-schemas-name-schemaname-language-language.md#DescribeCodeBinding")

Describe the code binding URI.

- [DescribeDiscoverer](v1-discoverers-id-discovererid.md#DescribeDiscoverer "v1-discoverers-id-discovererid.md#DescribeDiscoverer")

Describes the discoverer.

- [DescribeRegistry](v1-registries-name-registryname.md#DescribeRegistry "v1-registries-name-registryname.md#DescribeRegistry")

Describes the registry.

- [DescribeSchema](v1-registries-name-registryname-schemas-name-schemaname.md#DescribeSchema "v1-registries-name-registryname-schemas-name-schemaname.md#DescribeSchema")

Retrieve the schema definition.

- [ExportSchema](v1-registries-name-registryname-schemas-name-schemaname-export.md#ExportSchema "v1-registries-name-registryname-schemas-name-schemaname-export.md#ExportSchema")

Exports a schema.

- [GetCodeBindingSource](v1-registries-name-registryname-schemas-name-schemaname-language-language-source.md#GetCodeBindingSource "v1-registries-name-registryname-schemas-name-schemaname-language-language-source.md#GetCodeBindingSource")

Get the code binding source URI.

- [GetDiscoveredSchema](v1-discover.md#GetDiscoveredSchema "v1-discover.md#GetDiscoveredSchema")

Get the discovered schema that was generated based on sampled events.

- [GetResourcePolicy](v1-policy.md#GetResourcePolicy "v1-policy.md#GetResourcePolicy")

Retrieves the resource-based policy attached to a given registry.

- [ListDiscoverers](v1-discoverers.md#ListDiscoverers "v1-discoverers.md#ListDiscoverers")

List the discoverers.

- [ListRegistries](v1-registries.md#ListRegistries "v1-registries.md#ListRegistries")

List the registries.

- [ListSchemas](v1-registries-name-registryname-schemas.md#ListSchemas "v1-registries-name-registryname-schemas.md#ListSchemas")

List the schemas.

- [ListSchemaVersions](v1-registries-name-registryname-schemas-name-schemaname-versions.md#ListSchemaVersions "v1-registries-name-registryname-schemas-name-schemaname-versions.md#ListSchemaVersions")

Provides a list of the schema versions and related information.

- [ListTagsForResource](tags-resource-arn.md#ListTagsForResource "tags-resource-arn.md#ListTagsForResource")

Get tags for resource.

- [PutCodeBinding](v1-registries-name-registryname-schemas-name-schemaname-language-language.md#PutCodeBinding "v1-registries-name-registryname-schemas-name-schemaname-language-language.md#PutCodeBinding")

Put code binding URI

- [PutResourcePolicy](v1-policy.md#PutResourcePolicy "v1-policy.md#PutResourcePolicy")

The name of the policy.

- [SearchSchemas](v1-registries-name-registryname-schemas-search.md#SearchSchemas "v1-registries-name-registryname-schemas-search.md#SearchSchemas")

Search the schemas

- [StartDiscoverer](v1-discoverers-id-discovererid-start.md#StartDiscoverer "v1-discoverers-id-discovererid-start.md#StartDiscoverer")

Starts the discoverer

- [StopDiscoverer](v1-discoverers-id-discovererid-stop.md#StopDiscoverer "v1-discoverers-id-discovererid-stop.md#StopDiscoverer")

Stops the discoverer

- [TagResource](tags-resource-arn.md#TagResource "tags-resource-arn.md#TagResource")

Add tags to a resource.

- [UntagResource](tags-resource-arn.md#UntagResource "tags-resource-arn.md#UntagResource")

Removes tags from a resource.

- [UpdateDiscoverer](v1-discoverers-id-discovererid.md#UpdateDiscoverer "v1-discoverers-id-discovererid.md#UpdateDiscoverer")

Updates the discoverer

- [UpdateRegistry](v1-registries-name-registryname.md#UpdateRegistry "v1-registries-name-registryname.md#UpdateRegistry")
- [UpdateSchema](v1-registries-name-registryname-schemas-name-schemaname.md#UpdateSchema "v1-registries-name-registryname-schemas-name-schemaname.md#UpdateSchema")

Updates the schema definition

###### Note

Inactive schemas will be deleted after two years.
