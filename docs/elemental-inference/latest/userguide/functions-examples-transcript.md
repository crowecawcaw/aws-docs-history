

# Summarize the last 30 seconds of speech
<a name="functions-examples-transcript"></a>

Sends the transcript of each 30-second window to a text model and keeps a two-sentence summary. Requires an enabled smart subtitles output on the feed, named in `subtitlingSettings`.

**Request expression** (Anthropic Claude models)

```
{
  "anthropic_version": "bedrock-2023-05-31",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": $exists(media.transcript) and $length($trim(media.transcript)) > 0
            ? "Summarize this broadcast transcript in at most two sentences:\n\n" & media.transcript
            : "Reply with exactly: no speech in this window."
        }
      ]
    }
  ]
}
```

**Response expression**

```
{ "summary": content[type = "text"][0].text }
```

**Function output**

```
{
  "name": "commentary-summary",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "fixedInterval": { "intervalSeconds": 30 } },
      "subtitlingSettings": { "outputName": "subs-eng" }
    }
  }
}
```

**Result**

```
{"summary":"The commentators recap the opening 20 minutes and note that the home side has kept possession in midfield. They preview the substitution expected at the half."}
```