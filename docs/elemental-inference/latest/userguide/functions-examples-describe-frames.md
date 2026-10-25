

# Describe the action every 10 seconds
<a name="functions-examples-describe-frames"></a>

Sends four frames from each 10-second window to a model that accepts images, and keeps one sentence of description. The function reads no context from another output, but the feed still needs a video input and at least one enabled smart crop, event clipping, smart subtitles, or contextual metadata output.

**Request expression** (Anthropic Claude models)

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": $append(
        [{ "type": "text", "text": "These frames are consecutive moments from a live broadcast. Describe what is happening in one sentence. Do not speculate." }],
        media.frames.{
          "type": "image",
          "source": { "type": "base64", "media_type": "image/jpeg", "data": $ }
        }
      )
    }
  ]
}
```

**Response expression**

```
{ "description": content[type = "text"][0].text }
```

Newer Claude models can think before they answer, and the thinking counts toward `max_tokens`. The response can start with a `thinking` block, so the response expression selects the first block of type `text` instead of `content[0]`, and `max_tokens` leaves room for the thinking as well as the answer. The other Claude examples in this section follow the same rules.

**Function output**

```
{
  "name": "action-description",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "fixedInterval": { "intervalSeconds": 10 } },
      "frameSettings": { "frameSampling": { "mode": "UNIFORM", "count": 4 } }
    }
  }
}
```

**Result**

```
{"description":"A striker breaks past two defenders and shoots from the edge of the box."}
```