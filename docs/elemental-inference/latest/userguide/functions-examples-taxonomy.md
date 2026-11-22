

# Example – Classify each scene against your own taxonomy

Reuses the classification that Elemental Inference has already produced, and asks the model only to map it onto categories of your own – a much cheaper prompt than sending frames. Requires an enabled contextual metadata output on the feed, and a per-scene trigger.

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
          "text": "Scene summary: " & ($exists(media.contextual.scene.summary) ? media.contextual.scene.summary : "none")
                & "\nInteractive Advertising Bureau (IAB) categories: " & $join(media.contextual.scene.iabTaxonomy.categories.path[-1], ", ")
                & "\nObjects: " & $join(media.contextual.scene.objects, ", ")
                & "\nFlagged brand safety categories: " & $join(media.contextual.scene.garm.suitability.categories[flagged].category, ", ")
                & "\n\nChoose the single best match from this list: sport-live, sport-studio, advertising, news, other."
                & " Reply with only a JSON object with keys segment and confidence, where confidence is a number from 0 to 1."
                & " Don't wrap it in a code block."
        }
      ]
    }
  ]
}
```

`summary` is left out when the contextual metadata output doesn't generate summaries, so the expression tests it with `$exists()`. A list that is left out, such as `objects` with no labels, adds nothing after its label in the prompt.

**Response expression**. Parsing the model's text stores structured data rather than a string that your application has to parse again.

```
(
  $answer := $parse(content[type = "text"][0].text);
  {
    "segment": $answer.segment,
    "confidence": $answer.confidence
  }
)
```

**Function output**

```
{
  "name": "segment-class",
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
{"segment":"sport-live","confidence":0.92}
```

**Note**  
A model can return text that isn't valid JSON, most often JSON wrapped in a Markdown code block. `$parse()` then fails and the window produces no metadata. Ask for a bare JSON object, as this prompt does, and keep the schema small. Don't set `temperature`: newer Claude models reject a request that includes it.