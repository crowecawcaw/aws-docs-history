

# Example – Reshape contextual metadata without a model

A passthrough function that publishes each scene's classification in a flat shape of your own, with no model invocation and no model cost. Use it when you want a different schema, not a new analysis. Requires an enabled contextual metadata output on the feed, and a per-scene trigger.

**Target**

```
{ "passthrough": {} }
```

**Request expression**

```
{
  "topic": media.contextual.scene.iabTaxonomy.categories[0].path[-1],
  "allTopics": [media.contextual.scene.iabTaxonomy.categories.path[-1]],
  "flagged": [media.contextual.scene.garm.suitability.categories[flagged].category],
  "objects": media.contextual.scene.objects,
  "adSafe": $not("HIGH" in media.contextual.scene.garm.suitability.categories.risk
    or "FLOOR" in media.contextual.scene.garm.suitability.categories.risk)
}
```

The `[ ]` around the `allTopics` and `flagged` paths keeps each one an array when it matches one value or none. For more information, see [Fields in `media.contextual`](functions-context.md#functions-context-contextual).

**Response expression**. None. The request expression already produces the record to store, so there is nothing for a second stage to do.

**Function output**

```
{
  "name": "scene-flat",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:function/{{function-id}}",
      "trigger": { "perScene": {} },
      "contextualMetadataSettings": { "outputName": "ctx-md" }
    }
  }
}
```

**Result**

```
{"topic":"Basketball","allTopics":["Basketball","Television"],"flagged":[],"objects":["basketball","hoop"],"adSafe":true}
```