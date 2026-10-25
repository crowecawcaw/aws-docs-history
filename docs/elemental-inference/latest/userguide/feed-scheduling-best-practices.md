

# Best practices for editing feeds that have schedule actions
<a name="feed-scheduling-best-practices"></a>

At the scheduled time, Elemental Inference applies the action's operations to the feed's configuration as it is at that time. Elemental Inference doesn't save a copy of the feed configuration when you create the action. If you edit the feed after you create an action, your edit might make the action invalid. For example, if you create an action that targets `event-clip-output`, and then you delete that output, the action fails with `INVALID_ACTION_TARGET` at the scheduled time.

When you edit a feed, Elemental Inference doesn't check whether your edit conflicts with pending schedule actions. To avoid failed actions, follow these practices:
+ Review the pending actions with the `list-schedule-actions` command after you edit a feed. If your edit makes an action invalid, delete the action and create a new one.
+ Check for actions that have a status of `FAILED`.
+ Avoid editing the feed close to the scheduled time of an action. If you update the feed at the same time that an action runs, your `UpdateFeed` request can fail with a `ConflictException`, or the action can fail with an `INTERNAL_ERROR`. Elemental Inference retries the action for a few seconds before it fails the action.