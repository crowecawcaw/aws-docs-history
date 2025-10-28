# Asset and model states

When you create, update, or delete an asset, an asset model, or a component model, the
changes take time to propagate. AWS IoT SiteWise resolves these operations asynchronously and updates
the status of each resource. Each asset, asset model, and component model has a status field
that contains the state of the resource and any error message, if applicable. The state can be
one of the following values:

- `ACTIVE` – The resource is active. This is the only state in which
  you can query and interact with assets, asset models, and component models.
- `CREATING` – The resource is being created.
- `UPDATING` – The resource is being updated.
- `DELETING` – The resource is being deleted.
- `PROPAGATING` – (Asset models and component models only) The changes
  are propagating to all dependent resources (from asset model to assets, or from component
  model to asset models).
- `FAILED` – The resource failed to validate during a create or update
  operation, possibly due to a circular reference in an expression. You can delete resources
  that are in the `FAILED` state.
  Some of the create, update, and delete operations in AWS IoT SiteWise place an asset, asset model,
  or component model in a state other than `ACTIVE` while the operation resolves. To
  query or interact with a resource after you perform one of these operations, you must wait
  until the state changes to `ACTIVE`. Otherwise, your requests fail.

###### Topics

- [Check the status of an asset](check-asset-status.md "check-asset-status.md")
- [Check the status of an asset or component
  model](check-model-status.md "check-model-status.md")
