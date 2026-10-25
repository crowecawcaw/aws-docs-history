

# Creating a function using the CLI
<a name="functions-create-cli"></a>

Use `create-function`. The following example creates a function that sends sampled frames to an Anthropic Claude model and keeps one sentence of description.

```
aws elemental-inference create-function \
  --region {{us-west-2}} \
  --name play-description \
  --description "One-sentence description of the last few seconds of play" \
  --target '{
    "bedrock": {
      "api": "INVOKE_MODEL",
      "model": "{{model-id}}"
    }
  }' \
  --request-expression '{
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": $append(
          [{ "type": "text", "text": "Describe what is happening in these frames in one sentence." }],
          media.frames.{
            "type": "image",
            "source": { "type": "base64", "media_type": "image/jpeg", "data": $ }
          }
        )
      }
    ]
  }' \
  --response-expression '{ "result": content[type = "text"][0].text }' \
  --tags '{"Project":"highlights"}'
```

The response expression keeps the first text block of the reply, because some Claude models return a thinking block first.

The response contains the function, including the fields that Elemental Inference computed. A create response always reports `CREATING`; `get-function` reports `AVAILABLE` right away.

```
{
  "arn": "arn:aws:elemental-inference:us-west-2:111122223333:function/3k9x2m7p4q1w8n5t6vz",
  "id": "3k9x2m7p4q1w8n5t6vz",
  "name": "play-description",
  "target": {
    "bedrock": {
      "api": "INVOKE_MODEL",
      "model": "{{model-id}}"
    }
  },
  "requestExpression": "...",
  "responseExpression": "{ \"result\": content[type = \"text\"][0].text }",
  "description": "One-sentence description of the last few seconds of play",
  "status": "CREATING",
  "references": [],
  "contextTypes": ["FRAMES"],
  "tags": { "Project": "highlights" }
}
```

**Important**  
Check `contextTypes` in the response. It is how you confirm that Elemental Inference read your expression the way you intended. A function that you expect to analyze frames but that returns `"contextTypes": []` does not actually reference `media.frames`, so no frames will be decoded and the model will receive no images.

For a passthrough function, specify the `passthrough` target instead. The following example reshapes the contextual classification of each scene into a compact record of your own, with no model invocation.

```
aws elemental-inference create-function \
  --region {{us-west-2}} \
  --name scene-brand-safety-record \
  --target '{ "passthrough": {} }' \
  --request-expression '{
    "categories": media.contextual.categories,
    "risk": media.contextual.garm.risk,
    "flagged": media.contextual.garm.flagged
  }'
```

A passthrough function evaluates the request expression and then applies the response expression, if there is one, to that result. The example above has no response expression, so Elemental Inference stores the result of the request expression as it is. For more information, see [Passthrough functions](functions-expressions-passthrough.md).