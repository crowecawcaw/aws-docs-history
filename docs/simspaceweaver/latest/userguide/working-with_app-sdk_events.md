End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Entity events

You can use the following functions in the SimSpace Weaver app SDK to get all ownership and subscription events:

- `Result<OwnershipChangeList> OwnershipChanges(Transaction& txn)`
- `Result<SubscriptionChangeList> AllSubscriptionEvents(Transaction& txn)`
  You can use the SimSpace Weaver demo framework if you need callback-driven entity event processing.
  For more information, see the following header file:

- ``sdk-folder`/packaging-tools/samples/ext/DemoFramework/include/DemoFramework/EntityEventProcessor.h`
  You can also create your own entity event processing.

###### Topics

- [Iterate through events for owned entities](working-with_app-sdk_events_own.md "working-with_app-sdk_events_own.md")
- [Iterate through events for subscribed entities](working-with_app-sdk_events_sub.md "working-with_app-sdk_events_sub.md")
- [Iterate through ownership change events for entities](working-with_app-sdk_events_change.md "working-with_app-sdk_events_change.md")
