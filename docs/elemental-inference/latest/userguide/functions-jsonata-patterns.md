

# Common patterns

## Example – Fallback for a value that might be absent
<a name="functions-jsonata-patterns-fallback"></a>

A `media.contextual` field that has no value is left out. The summary, for example, is left out when the contextual metadata output has summary generation disabled, so don't build a prompt that assumes it. Test for the field with `$exists()`, and fall back to a field that is still there, such as the Interactive Advertising Bureau (IAB) categories.

```
$exists(media.contextual.scene.summary)
  ? media.contextual.scene.summary
  : $join(media.contextual.scene.iabTaxonomy.categories.path[-1], ", ")
```

## Example – Skipping an empty window
<a name="functions-jsonata-patterns-guard"></a>

A window with no speech produces an empty transcript. Send the model something meaningful instead of an empty prompt.

```
$exists(media.transcript) and $length($trim(media.transcript)) > 0
  ? "Summarize: " & media.transcript
  : "No speech in this window."
```

## Example – Flattening clips into one line of prompt
<a name="functions-jsonata-patterns-flatten"></a>

```
$join(media.clip.events.(keyword & ": " & description), "\n")
```

## Example – Extracting a structured answer
<a name="functions-jsonata-patterns-extract"></a>

Ask the model for JSON in the request expression, then parse it in the response expression so that the stored value is data.

```
/* in the request expression */
{ "text": "Answer as JSON with keys sentiment and reason. Transcript: " & media.transcript }
```

```
/* in the response expression */
$parse(content[type = "text"][0].text)
```

## Example – Guarding a response expression
<a name="functions-jsonata-patterns-defensive"></a>

A model can return a truncated or unexpected response. A response expression that finds nothing stores nothing useful, so provide a fallback.

```
(
  $text := content[type = "text"][0].text;
  $exists($text) ? { "result": $text } : { "note": "empty model response" }
)
```