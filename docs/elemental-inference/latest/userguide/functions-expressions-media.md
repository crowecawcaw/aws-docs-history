

# Placing media in the request
<a name="functions-expressions-media"></a>

You never encode media yourself. Reference `media.frames` or `media.video` where the model expects the encoded bytes, and Elemental Inference substitutes them after your expression has been evaluated. While the expression runs, those values are placeholders, so the media itself is never exposed to the expression.

The consequence is one rule: **place a media value whole**.
+ Assign `media.video`, or an item of `media.frames`, directly to a field. Don't concatenate it, take a substring of it, or otherwise transform it.
+ Don't place the same frame or clip in two places in the same request. It doubles the size of the request and what the model charges for it.

A request expression that breaks either rule is rejected when you save the function, or, in a branch that the sample context doesn't reach, fails at run time with a guardrail error. See [Expression limits and guardrails](functions-expressions-guardrails.md).

`media.transcript`, `media.contextual`, and `media.clip` are ordinary data, not media payloads. You can test them, concatenate them, iterate over them, and reshape them freely.

Use the `.` map operator to expand `media.frames` into the array shape that the model expects, and `$append()` to place that array after your prompt text. Inside the map, `$` refers to the current frame.

```
$append(
  [{ "type": "text", "text": "Describe these frames." }],
  media.frames.{
    "type": "image",
    "source": { "type": "base64", "media_type": "image/jpeg", "data": $ }
  }
)
```