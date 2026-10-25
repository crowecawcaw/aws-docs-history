

# Reshape contextual metadata without a model
<a name="functions-examples-passthrough-flatten"></a>

A passthrough function that publishes each scene's classification in a flat shape of your own, with no model invocation and no model cost. Use it when your application wants a different schema, not a new analysis. Requires an enabled contextual metadata output on the feed, and a per-scene trigger.

**Target**

```
{ "passthrough": {} }
```

**Request expression**

```
{
  "topic": media.contextual.categories[0],
  "allTopics": media.contextual.categories,
  "risk": media.contextual.garm.risk,
  "flagged": media.contextual.garm.flagged,
  "objects": media.contextual.objects,
  "adSafe": $not(media.contextual.garm.risk = "HIGH" or media.contextual.garm.risk = "FLOOR")
}
```

**Response expression**. None. The request expression already produces the record to store, so there is nothing for a second stage to do.

**Function output**

```
{
  "name": "scene-flat",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "perScene": {} },
      "contextualMetadataSettings": { "outputName": "ctx-md" }
    }
  }
}
```

**Result**

```
{"topic":"Basketball","allTopics":["Basketball","Television"],"risk":"LOW","flagged":[],"objects":["basketball","hoop"],"adSafe":true}
```