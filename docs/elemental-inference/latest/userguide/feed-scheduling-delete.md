

# Deleting a schedule action
<a name="feed-scheduling-delete"></a>

To delete a pending schedule action, use the `delete-schedule-action` command. Specify the feed ID and the name of the action.

```
aws elemental-inference delete-schedule-action \
  --id <{{feed-id}}> \
  --action-name "enable-smartcrop-game-1"
```

If the request succeeds, Elemental Inference returns the name of the deleted action. A deleted action never runs.

```
{ "actionName": "enable-smartcrop-game-1" }
```

You can delete only actions that have a status of `PENDING`. If the action has already run, the request returns a `ValidationException`. If the action starts to run while your delete request is in progress, the request returns a `ConflictException`. In that case, use the `list-schedule-actions` command to check whether the action ran.

Deleting an action never reverses changes that the action already made.

When you delete or archive a feed, Elemental Inference deletes all schedule actions on the feed.