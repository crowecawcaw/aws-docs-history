

# Request expression examples by model family
<a name="functions-expressions-request"></a>

Each model family has its own request body, so the reference for the body shape is always the Amazon Bedrock documentation for the model that you chose. The examples in this section use the Anthropic Claude Messages API to show the technique; the placement of `media.frames` and `media.video` is the same whichever family you use, and only the field names around them change.

**Frames**

```
{
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
}
```

`media.video` is placed the same way, in whichever field the model uses for inline video bytes. Only a model that accepts video can take that input, so check the documentation for the model you chose.

**Text-only context**. The transcript and the contextual classification are plain data, so build the prompt with string concatenation (`&`).

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text", "text": "Summarize the following transcript in two sentences:\n\n" & media.transcript }
      ]
    }
  ]
}
```

Guard against an empty window with a conditional. A window with no speech in it produces an empty transcript, and a prompt with nothing in it wastes an invocation.

```
{ "type": "text", "text": media.transcript ? "Summarize: " & media.transcript : "No speech in this window." }
```

You can read specific fields of the contextual classification rather than sending the whole object, which keeps the prompt short and the answer focused.

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": [
        { "type": "text",
          "text": "Scene summary: " & (media.contextual.summary != null ? media.contextual.summary : "none")
                & "\nObjects: " & $join(media.contextual.objects, ", ")
                & "\nBrand-safety risk: " & media.contextual.garm.risk
                & "\n\nIs this scene suitable for a family audience? Answer yes or no, with one reason." }
      ]
    }
  ]
}
```

Use `$string()` when you do want to hand the model the whole object.

```
{ "type": "text", "text": "Classify this scene against my taxonomy:\n\n" & $string(media.contextual) }
```