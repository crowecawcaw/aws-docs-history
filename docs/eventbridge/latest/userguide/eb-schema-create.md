# Creating an event schema in Amazon EventBridge

You create schemas by using JSON files with either the [OpenAPI Specification](https://swagger.io/specification/ "https://swagger.io/specification/") or the [JSONSchema Draft4
specification](https://json-schema.org/specification-links.html#draft-4 "https://json-schema.org/specification-links.html#draft-4"). You can create or upload your own schemas in EventBridge by using a
template or generating a schema based on the JSON of an [event](eb-events.md "eb-events.md"). You can also infer the schema from events on an [event bus](eb-event-bus.md "eb-event-bus.md"). To create a schema by using the EventBridge Schema
Registry API, use the [`CreateSchema`](../schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#v1-registries-nam "../schema-reference/v1-registries-name-registryname-schemas-name-schemaname.md#v1-registries-nam") API action.

When you choose between OpenAPI 3 and JSONSchema Draft4 formats,
consider the following differences:

- JSONSchema format supports additional keywords that aren't supported in OpenAPI,
  such as `$schema, additionalItems`.
- There are minor differences in how keywords are handled, such as `type`
  and `format`.
- OpenAPI doesn't support JSONSchema Hyper-Schema hyperlinks in JSON documents.
- Tools for OpenAPI tend to focus on build-time, whereas tools for JSONSchema tend to
  focus on run-time operations, such as client tools for schema validation.
  We recommend using JSONSchema format to implement client-side validation so that events
  sent to EventBridge conform to the schema. You can use JSONSchema to define a contract for valid
  JSON documents, and then use a [JSON schema validator](https://json-schema.org/implementations.html "https://json-schema.org/implementations.html") before sending the associated events.

After you have a new schema, you can download [code bindings](eb-schema-code-bindings.md "eb-schema-code-bindings.md") to help create applications
for events with that schema.
