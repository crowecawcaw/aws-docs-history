End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Iterate through events for subscribed entities

Use `AllSubscriptionEvents()` to get a list of events for subscribed entities
(entities in the app's subscription area). The function has the following signature:

```
Result<SubscriptionChangeList> AllSubscriptionEvents(Transaction& txn)

```

Then iterate through the entities with a loop, as demonstrated in the following example.

###### Example

```
WEAVERRUNTIME_TRY(Api::SubscriptionChangeList subscriptionChangeList, Api::AllSubscriptionEvents(transaction));

for (const Api::SubscriptionEvent& event : subscriptionChangeList.changes)
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
