

# How schedule actions work
<a name="feed-scheduling-how-it-works"></a>

A schedule action has the following parts:

Action name  
This is the name that identifies the action. The name must be unique within the feed.

Start configuration  
This specifies when the action runs. Currently, only fixed mode is supported. In fixed mode, the action runs once, at the UTC time that you specify in `scheduledAt`.

Operations  
This is a list of the configuration changes to make. Elemental Inference applies all operations in an action together, in the order that you list them. For more information, see [Operations that you can schedule](feed-scheduling-operations.md).

Status  
This indicates the state of the action, which can be `PENDING`, `COMPLETED`, or `FAILED`. For more information, see [Lifecycle of a schedule action](feed-scheduling-lifecycle.md).

When you create a schedule action, the following rules apply to the scheduled time:
+ The time must be at least 1 hour in the future.
+ The time must be in whole seconds. Don't include milliseconds.
+ The time can't be more than 3 years in the future.

**Important**  
The scheduled time is approximate. After Elemental Inference applies the change to the feed, it can take up to about 4 minutes for the change to take effect on the media that the feed is processing. For example, if you schedule an action for `18:00:00Z`, the change might not be in effect until about `18:04:00Z`. Plan your schedule so that this delay doesn't affect your workflow.

A feed can have up to 100 schedule actions. For more information about quotas, see [Quotas for AWS Elemental Inference](quotas.md).

You can't update a schedule action. To change an action, delete it and then create a new action. You can reuse the same action name as soon as the delete succeeds.

You can add schedule actions only to a live feed that you can update. The request fails if the feed is archived. It also fails if the feed is a video-on-demand (VOD) feed that an AWS Elemental MediaConvert (MediaConvert) job created. In both cases, Elemental Inference returns a `ValidationException`.