End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# AllSubscriptionEvents and OwnershipChanges contain events from the last call

The return values of calls to `Api::AllSubscriptionEvents()` and
`Api::OwnershipChanges()` contain events from the last call,
**not the last tick**. In the following example,
`secondSubscriptionEvents` and `secondOwnershipChangeList`
are empty because their functions are called immediately after the first calls.

If you wait 10 ticks and then call `Api::AllSubscriptionEvents()` and
`Api::OwnershipChanges()`, their results will both contain events and changes
from the last 10 ticks (not the last tick).

###### Example

```
Result<void> ProcessOwnershipChanges(Transaction& transaction)
{
    WEAVERRUNTIME_TRY(
        Api::SubscriptionChangeList firstSubscriptionEvents,
        Api::AllSubscriptionEvents(transaction));
    WEAVERRUNTIME_TRY(
        Api::OwnershipChangeList firstOwnershipChangeList,
        Api::OwnershipChanges(transaction));

    WEAVERRUNTIME_TRY(
        Api::SubscriptionChangeList secondSubscriptionEvents,
        Api::AllSubscriptionEvents(transaction));
    WEAVERRUNTIME_TRY(
        Api::OwnershipChangeList secondOwnershipChangeList,
        Api::OwnershipChanges(transaction));

    /**
     * secondSubscriptionEvents and secondOwnershipChangeList are
     * both empty because there are no changes since the last call.
     */
}

```

###### Note

The function `AllSubscriptionEvents()` is implemented
but the function `SubscriptionEvents()` is
**not implemented**.
