End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Entities

You call the `Store` and `Load` APIs using the
`Api:Entity` of the `Result<Api::Entity>`
returned from `CreateEntity()`, or from an ownership change
event when an entity enters
the app's subscription area (for more information, see
[Entity events](working-with_app-sdk_events.md "working-with_app-sdk_events.md")).
We recommend that you track your `Api::Entity` objects
so that you can use them with these APIs.

###### Topics

- [Create entities](working-with_app-sdk_ent_create.md "working-with_app-sdk_ent_create.md")
- [Transfer an entity to a spatial domain](working-with_app-sdk_ent_transfer.md "working-with_app-sdk_ent_transfer.md")
- [Write and read entity field data](working-with_app-sdk_ent_readwrite.md "working-with_app-sdk_ent_readwrite.md")
- [Store the position of an entity](working-with_app-sdk_ent_store-position.md "working-with_app-sdk_ent_store-position.md")
- [Load the position of an entity](working-with_app-sdk_ent_load-position.md "working-with_app-sdk_ent_load-position.md")
