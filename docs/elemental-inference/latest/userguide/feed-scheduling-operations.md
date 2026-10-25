

# Operations that you can schedule
<a name="feed-scheduling-operations"></a>

The following table lists the operations that you can schedule and the fields that each one takes. Each operation in the `operations` list must contain exactly one of these members.


| Operation | Fields | Description | 
| --- | --- | --- | 
| updateOutputStatus | outputName, status | Enables or disables an output. Set status to ENABLED or DISABLED. | 
| updateClippingDataSourceConfiguration | outputName, dataSourceConfiguration.fixtureId | Attaches a game to an event clipping output. Set fixtureId to the ID of a game that you got from the SearchFixtures operation. The ID can be 1–128 characters. The output must be an event clipping output. If an action has more than one of these operations, they must all use the same fixtureId. | 
| removeClippingDataSourceConfiguration | outputName | Removes the game from an event clipping output. The output must be an event clipping output. | 

Elemental Inference applies all operations in an action as a single update to the feed. If any operation fails, Elemental Inference doesn't apply any of the operations, and the action status changes to `FAILED`.

When you create the action, Elemental Inference validates the targets that the operations name. It checks that each `outputName` refers to an existing output in the feed. It also checks that clipping operations target an event clipping output. For each `fixtureId`, it checks that the game is one that Elemental Inference can find and that the game is in a supported sport.

If a check fails, the request returns a `ValidationException`. You therefore find out about the problem when you create the action instead of when it runs.