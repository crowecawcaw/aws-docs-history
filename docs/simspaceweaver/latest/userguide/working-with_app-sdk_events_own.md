End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Iterate through events for owned entities

Use `OwnershipChanges()` to get a list of events for owned entities
(entities in the app's ownership area). The function has the following signature:

```
Result<OwnershipChangeList> OwnershipChanges(Transaction& txn)

```

Then iterate through the entities with a loop, as demonstrated in the following example.

###### Example

```
WEAVERRUNTIME_TRY(Result<Api::OwnershipChangeList> ownershipChangesResult, Api::OwnershipChanges(transaction));

for (const Api::OwnershipChange& event : ownershipChangeList.changes)
{
    Api::Entity entity = event.entity;
    Api::ChangeListAction action = event.action;

    switch (action)
    {
    case Api::ChangeListAction::None:
        // insert code to handle the event
        break;
    case Api::ChangeListAction::Remove:
        // insert code to handle the event
        break;
    case Api::ChangeListAction::Add:
        // insert code to handle the event
        break;
    case Api::ChangeListAction::Update:
        // insert code to handle the event
        break;
    case Api::ChangeListAction::Reject:
        // insert code to handle the event
        break;
    }
}

```

###### Event types

- `None` – The entity is in the area and its position
  and field data weren't modified.
- `Remove` – The entity was removed from the area.
- `Add` – The entity was added to the area.
- `Update` – The entity is in the area and was modified.
- `Reject` – The app failed to remove the entity from the area.

###### Note

In the case of a `Reject` event, the app will attempt the transfer again on the next tick.
