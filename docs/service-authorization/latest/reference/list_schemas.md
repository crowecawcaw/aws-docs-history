

# Actions, resources, and condition keys for Amazon EventBridge Schemas
<a name="list_schemas"></a>

Amazon EventBridge Schemas (service prefix: `schemas`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/eventbridge/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-security.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/schemas/schemas.json) for this service.

**Topics**
+ [API operations defined by Amazon EventBridge Schemas](#list_schemas-operations)
+ [Actions defined by Amazon EventBridge Schemas](#list_schemas-actions-as-permissions)
+ [Resource types defined by Amazon EventBridge Schemas](#list_schemas-resources-for-iam-policies)
+ [Condition keys for Amazon EventBridge Schemas](#list_schemas-policy-keys)

## API operations defined by Amazon EventBridge Schemas
<a name="list_schemas-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_schemas-actions-as-permissions).




- **   CreateDiscoverer  **
  - **IAM action:**  [schemas:CreateDiscoverer](#list_schemas-action-CreateDiscoverer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [schemas:TagResource](#list_schemas-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRegistry  **
  - **IAM action:**  [schemas:CreateRegistry](#list_schemas-action-CreateRegistry)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [schemas:TagResource](#list_schemas-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSchema  **
  - **IAM action:**  [schemas:CreateSchema](#list_schemas-action-CreateSchema)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [schemas:TagResource](#list_schemas-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDiscoverer  **
  - **IAM action:**  [schemas:DeleteDiscoverer](#list_schemas-action-DeleteDiscoverer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRegistry  **
  - **IAM action:**  [schemas:DeleteRegistry](#list_schemas-action-DeleteRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [schemas:DeleteResourcePolicy](#list_schemas-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchema  **
  - **IAM action:**  [schemas:DeleteSchema](#list_schemas-action-DeleteSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSchemaVersion  **
  - **IAM action:**  [schemas:DeleteSchemaVersion](#list_schemas-action-DeleteSchemaVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCodeBinding  **
  - **IAM action:**  [schemas:DescribeCodeBinding](#list_schemas-action-DescribeCodeBinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDiscoverer  **
  - **IAM action:**  [schemas:DescribeDiscoverer](#list_schemas-action-DescribeDiscoverer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeRegistry  **
  - **IAM action:**  [schemas:DescribeRegistry](#list_schemas-action-DescribeRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSchema  **
  - **IAM action:**  [schemas:DescribeSchema](#list_schemas-action-DescribeSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ExportSchema  **
  - **IAM action:**  [schemas:ExportSchema](#list_schemas-action-ExportSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeBindingSource  **
  - **IAM action:**  [schemas:GetCodeBindingSource](#list_schemas-action-GetCodeBindingSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDiscoveredSchema  **
  - **IAM action:**  [schemas:GetDiscoveredSchema](#list_schemas-action-GetDiscoveredSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourcePolicy  **
  - **IAM action:**  [schemas:GetResourcePolicy](#list_schemas-action-GetResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDiscoverers  **
  - **IAM action:**  [schemas:ListDiscoverers](#list_schemas-action-ListDiscoverers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRegistries  **
  - **IAM action:**  [schemas:ListRegistries](#list_schemas-action-ListRegistries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemaVersions  **
  - **IAM action:**  [schemas:ListSchemaVersions](#list_schemas-action-ListSchemaVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSchemas  **
  - **IAM action:**  [schemas:ListSchemas](#list_schemas-action-ListSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [schemas:ListTagsForResource](#list_schemas-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutCodeBinding  **
  - **IAM action:**  [schemas:PutCodeBinding](#list_schemas-action-PutCodeBinding) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutResourcePolicy  **
  - **IAM action:**  [schemas:PutResourcePolicy](#list_schemas-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchSchemas  **
  - **IAM action:**  [schemas:SearchSchemas](#list_schemas-action-SearchSchemas) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartDiscoverer  **
  - **IAM action:**  [schemas:StartDiscoverer](#list_schemas-action-StartDiscoverer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDiscoverer  **
  - **IAM action:**  [schemas:StopDiscoverer](#list_schemas-action-StopDiscoverer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [schemas:TagResource](#list_schemas-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [schemas:UntagResource](#list_schemas-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDiscoverer  **
  - **IAM action:**  [schemas:UpdateDiscoverer](#list_schemas-action-UpdateDiscoverer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRegistry  **
  - **IAM action:**  [schemas:UpdateRegistry](#list_schemas-action-UpdateRegistry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSchema  **
  - **IAM action:**  [schemas:UpdateSchema](#list_schemas-action-UpdateSchema) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon EventBridge Schemas
<a name="list_schemas-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#CreateDiscoverer)  **
  - **Description:** Grants permission to create an event schema discoverer. Once created, your events will be automatically map into corresponding schema documents
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_schemas-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRegistry](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname.html#CreateRegistry)  **
  - **Description:** Grants permission to create a new schema registry in your account
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_schemas-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSchema](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.html#CreateSchema)  **
  - **Description:** Grants permission to create a new schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_schemas-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#DeleteDiscoverer)  **
  - **Description:** Grants permission to delete discoverer in your account
  - **Resource types (\*required):** [discoverer\*](#list_schemas-resource-discoverer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRegistry](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname.html#DeleteRegistry)  **
  - **Description:** Grants permission to delete an existing registry in your account
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-policy.html#DeleteResourcePolicy)  **
  - **Description:** Grants permission to delete the resource-based policy attached to a given registry
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchema](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.html#DeleteSchema)  **
  - **Description:** Grants permission to delete an existing schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSchemaVersion](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-version-schemaversion.html#DeleteSchemaVersion)  **
  - **Description:** Grants permission to delete a specific version of schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCodeBinding](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-language-language.html#DescribeCodeBinding)  **
  - **Description:** Grants permission to retrieve metadata for generated code for specific schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#DescribeDiscoverer)  **
  - **Description:** Grants permission to retrieve discoverer metadata in your account
  - **Resource types (\*required):** [discoverer\*](#list_schemas-resource-discoverer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeRegistry](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname.html#DescribeRegistry)  **
  - **Description:** Grants permission to describe an existing registry metadata in your account
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSchema](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.html#DescribeSchema)  **
  - **Description:** Grants permission to retrieve an existing schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ExportSchema](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-policy.html#ExportSchema)  **
  - **Description:** Grants permission to export the AWS registry or discovered schemas in OpenAPI 3 format to JSONSchema format
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCodeBindingSource](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-language-language-source.html#GetCodeBindingSource)  **
  - **Description:** Grants permission to retrieve metadata for generated code for specific schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDiscoveredSchema](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discover.html#GetDiscoveredSchema)  **
  - **Description:** Grants permission to retrieve a schema for the provided list of sample events
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetResourcePolicy](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-policy.html#GetResourcePolicy)  **
  - **Description:** Grants permission to retrieve the resource-based policy attached to a given registry
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDiscoverers](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers.html#ListDiscoverers)  **
  - **Description:** Grants permission to list all discoverers in your account
  - **Resource types (\*required):** [discoverer\*](#list_schemas-resource-discoverer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRegistries](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries.html#ListRegistries)  **
  - **Description:** Grants permission to list all registries in your account
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSchemaVersions](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-versions.html#ListSchemaVersions)  **
  - **Description:** Grants permission to list all versions of a schema
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSchemas](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas.html#ListSchemas)  **
  - **Description:** Grants permission to list all schemas
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/tags-resource-arn.html#ListTagsForResource)  **
  - **Description:** Grants permission to lists tags for a resource
  - **Resource types (\*required):** [discoverer](#list_schemas-resource-discoverer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [registry](#list_schemas-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [schema](#list_schemas-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutCodeBinding](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname-language-language.html#PutCodeBinding)  **
  - **Description:** Grants permission to generate code for specific schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutResourcePolicy](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-policy.html#PutResourcePolicy)  **
  - **Description:** Grants permission to attach a resource-based policy to a given registry
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchSchemas](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-search.html#SearchSchemas)  **
  - **Description:** Grants permission to search schemas based on specified keywords in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [StartDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#StartDiscoverer)  **
  - **Description:** Grants permission to start the specified discoverer. Once started the discoverer will automatically register schemas for published events to configured source in your account
  - **Resource types (\*required):** [discoverer\*](#list_schemas-resource-discoverer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#StopDiscoverer)  **
  - **Description:** Grants permission to stop the specified discoverer. Once stopped the discoverer will no longer register schemas for published events to configured source in your account
  - **Resource types (\*required):** [discoverer\*](#list_schemas-resource-discoverer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/tags-resource-arn.html#TagResource)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [discoverer](#list_schemas-resource-discoverer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_schemas-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Resource types (\*required):** [registry](#list_schemas-resource-registry) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_schemas-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Resource types (\*required):** [schema](#list_schemas-resource-schema) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_schemas-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/tags-resource-arn.html#UntagResource)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [discoverer](#list_schemas-resource-discoverer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Resource types (\*required):** [registry](#list_schemas-resource-registry) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Resource types (\*required):** [schema](#list_schemas-resource-schema) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_schemas-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#UpdateDiscoverer)  **
  - **Description:** Grants permission to update an existing discoverer in your account
  - **Resource types (\*required):** [discoverer\*](#list_schemas-resource-discoverer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRegistry](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname.html#UpdateRegistry)  **
  - **Description:** Grants permission to update an existing registry metadata in your account
  - **Resource types (\*required):** [registry\*](#list_schemas-resource-registry)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSchema](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-registries-name-registryname-schemas-name-schemaname.html#UpdateSchema)  **
  - **Description:** Grants permission to update an existing schema in your account
  - **Resource types (\*required):** [schema\*](#list_schemas-resource-schema)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon EventBridge Schemas
<a name="list_schemas-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [discoverer](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html)  | arn:${Partition}:schemas:${Region}:${Account}:discoverer/${DiscovererId} | [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_) | 
|  [registry](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html)  | arn:${Partition}:schemas:${Region}:${Account}:registry/${RegistryName} | [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_) | 
|  [schema](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-schema.html)  | arn:${Partition}:schemas:${Region}:${Account}:schema/${RegistryName}/${SchemaName} | [aws:ResourceTag/${TagKey}](#list_schemas-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon EventBridge Schemas
<a name="list_schemas-policy-keys"></a>

Amazon EventBridge Schemas defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by allowed set of values for each of the tags | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag-value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of mandatory tags in the request | ArrayOfString | 