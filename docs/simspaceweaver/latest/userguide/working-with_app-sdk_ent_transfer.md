End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Transfer an entity to a spatial domain

After a custom app or service app creates an entity, the app must transfer the
entity to a spatial domain in order for the entity to exist spatially in the
simulation. Entities in a spatial domain can be read by other apps and updated by a
spatial app. Use the `ModifyEntityDomain()` API to transfer an entity to a spatial
domain.

```
AWS_WEAVERRUNTIME_API Result<void> ModifyEntityDomain(Transaction& txn, const Entity& entity, DomainId domainId) noexcept;

```

If the `DomainId` doesn't match the assigned `Partition` of the calling app, then the
`DomainId` must be for a `DomainType::Spatial` `Domain`. The ownership transfer to the new
`Domain` occurs during the `Commit(Transaction&&)`.

###### Parameters

`txn`
The current `Transaction`.

`entity`
The target `Entity` for the change of `Domain`.

`domainId`
The `DomainId` of the destination `Domain` for the `Entity`.

This API returns `Success` if the entity domain was successfully changed.
