# HubContentDocument schema

A `HubContentDocument` is a JSON-formatted document that describes information
about a piece of hub content, such as its type, associated containers, scripts, and more. The
[DescribeHubContent](../APIReference/API_DescribeHubContent.md "../APIReference/API_DescribeHubContent.md")
operation returns this document in the `HubContentDocument` response field as a
string. To list the hub content items that are available before describing one, use
[ListHubContents](../APIReference/API_ListHubContents.md "../APIReference/API_ListHubContents.md").

The properties in a `HubContentDocument` capture the metadata that describes a
piece of hub content. Use this metadata to evaluate and compare content and to make informed
decisions about which item best fits your use case. Because applications and AI agents
increasingly read this metadata programmatically to reason about hub content on your behalf,
this section documents what each property means.

The set of properties depends on the content type. The `HubContentType` of a
piece of hub content is one of the following values:

- `Model`
- `Notebook`
- `ModelReference`
- `DataSet`
- `JsonDoc`
  This reference currently documents the schema for the `Model` HubContentType.

###### Note

This reference describes the latest version of the `HubContentDocument`
schema. Earlier schema versions might define a different set of properties. The schema
version is returned in the `DocumentSchemaVersion` field of the
`DescribeHubContent` response.

###### Topics

- [Model properties](hub-content-document-model-properties.md "hub-content-document-model-properties.md")
