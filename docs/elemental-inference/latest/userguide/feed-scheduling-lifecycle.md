

# Lifecycle of a schedule action
<a name="feed-scheduling-lifecycle"></a>

A schedule action has one of the following statuses:

`PENDING`  
The action is waiting for its scheduled time. You can delete the action while it has this status.

`COMPLETED`  
Elemental Inference applied all the action's operations to the feed.

`FAILED`  
Elemental Inference couldn't apply the action. The action includes an `error` with one of the following error codes:  
+ `INVALID_ACTION_TARGET` – The action refers to something that doesn't exist or isn't valid at the scheduled time. For example, the output was deleted, the output is no longer an event clipping output, or Elemental Inference can no longer find the game.
+ `INTERNAL_ERROR` – An unexpected error prevented the action from completing.

Elemental Inference keeps `COMPLETED` and `FAILED` actions for about 48 hours after the scheduled time, and then deletes them automatically. To check the result of an action, use the `list-schedule-actions` command during this period.

If you delete or archive the feed before an action runs, Elemental Inference deletes the action and the action never runs.