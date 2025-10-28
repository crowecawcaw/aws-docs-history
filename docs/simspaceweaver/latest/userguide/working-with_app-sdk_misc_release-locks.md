End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Release read locks after processing SubscriptionChangeList

When you begin an update, there are shared memory segments for the
committed data in other partitions for the previous tick. These shared
memory segments might be locked by readers. An app can’t fully commit
until all the readers have released the locks. As an optimization, an
app should call `Api::ReleaseReadLeases()` to release the
locks after processing `Api::SubscriptionChangelist` items.
This reduces contention at commit time. `Api::Commit()`
releases the read leases by default, but it's a best practice to manually
release them after processing subscription updates.

###### Example

```
Result<void> ProcessSubscriptionChanges(Transaction& transaction)
{
    WEAVERRUNTIME_TRY(ProcessSubscriptionChanges(transaction));

    /**
     * Done processing Api::SubscriptionChangeList items.
     * Release read locks.
     */

    WEAVERRUNTIME_EXPECT(Api::ReleaseReadLeases(transaction));

    ...
}

```
