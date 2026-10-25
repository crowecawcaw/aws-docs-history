

# Passthrough functions
<a name="functions-expressions-passthrough"></a>

A passthrough function invokes no model. Elemental Inference evaluates the request expression against `media`, and then evaluates the response expression against *that result*. Use a passthrough function to publish the metadata that Elemental Inference already produced in a shape of your own choosing — a flattened record, your own field names, a filtered subset — at no model cost.

A passthrough request expression can't reference `media.frames` or `media.video`, because there is no model to send media to. A function that does is rejected when you save it.

The response expression stays optional. For a straightforward reshape, put the whole transform in the request expression and omit the response expression — Elemental Inference stores the result of the request expression as it is. Add a response expression when you want a second stage, such as keeping the full record only for some windows. Either way, the final result must have a value for the sample context, or the function is rejected when you save it.

The following pair flattens a scene's classification into one record and keeps the full record only for the scenes that were flagged.

```
/* request expression */
{
  "categories": media.contextual.categories,
  "risk": media.contextual.garm.risk,
  "flagged": media.contextual.garm.flagged,
  "summary": media.contextual.summary != null ? media.contextual.summary
}
```

```
/* response expression */
$count(flagged) > 0 ? $ : { "risk": risk }
```