

# Common patterns
<a name="functions-jsonata-patterns"></a>

## Fallback for a value that might be absent
<a name="functions-jsonata-patterns-fallback"></a>

The summary is `null` unless the contextual metadata output has summary generation enabled, so don't build a prompt that assumes it. Test for `null` with `!= null`: `$exists()` returns true for a field whose value is `null`.

```
media.contextual.summary != null
  ? media.contextual.summary
  : $join(media.contextual.objects, ", ")
```

## Skipping an empty window
<a name="functions-jsonata-patterns-guard"></a>

A window with no speech produces an empty transcript. Send the model something meaningful instead of an empty prompt.

```
$exists(media.transcript) and $length($trim(media.transcript)) > 0
  ? "Summarize: " & media.transcript
  : "No speech in this window."
```

## Flattening clips into one line of prompt
<a name="functions-jsonata-patterns-flatten"></a>

```
$join(media.clip.events.(keyword & ": " & description), "\n")
```

## Extracting a structured answer
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

## Guarding a response expression
<a name="functions-jsonata-patterns-defensive"></a>

A model can return a truncated or unexpected response. A response expression that finds nothing stores nothing useful, so provide a fallback.

```
(
  $text := content[type = "text"][0].text;
  $exists($text) ? { "result": $text } : { "note": "empty model response" }
)
```