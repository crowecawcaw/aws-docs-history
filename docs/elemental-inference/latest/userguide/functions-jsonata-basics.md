

# Language basics

## Path navigation
<a name="functions-jsonata-dot-notation"></a>

Use dot notation to walk into the input. Each dot descends one level.

```
media.transcript                    the transcript for this window
media.contextual.scene.summary      the summary of the scene
usage.output_tokens                 a field of a model response
```

A path that doesn't exist evaluates to nothing, without raising an error. This applies at any depth, so a missing intermediate object doesn't break the expression.

```
media.contextual.nonExistent                       nothing
media.contextual.scene.nonExistent.deeply.nested   nothing
```

Use `[n]` to index an array, starting at zero, and `[-1]` to take the last element.

```
media.frames[0]              the first sampled frame
media.clip.events[0].keyword the keyword of the first clip in the window
```

## Mapping over an array
<a name="functions-jsonata-map"></a>

Applying a path or an object constructor to an array maps it over every element. Inside the map, `$` is the current element.

```
media.clip.events.keyword
  ["touchdown", "interception"]

media.clip.events.{ "label": keyword, "at": startPts }
  [{ "label": "touchdown", "at": 900000 }, ...]

media.frames.{ "type": "image", "source": { "type": "base64", "media_type": "image/jpeg", "data": $ } }
  one object per frame
```

## String concatenation
<a name="functions-jsonata-concat"></a>

The `&` operator joins two values into a string. Non-string values are converted automatically.

```
"Summary: " & media.contextual.scene.summary
"objects=" & $join(media.contextual.shot.objects, ", ") & " flagged=" & $count(media.contextual.shot.garm.suitability.categories[flagged])
```

## Conditional expressions
<a name="functions-jsonata-ternary"></a>

Use the ternary operator to choose between two values.

```
condition ? value_if_true : value_if_false
```

You can nest ternary expressions for multi-way branching.

```
$exists(media.contextual.scene.summary) ? media.contextual.scene.summary : "No summary available."

"FLOOR" in media.contextual.shot.garm.suitability.categories.risk ? "block"
  : "HIGH" in media.contextual.shot.garm.suitability.categories.risk ? "review"
  : "allow"
```

## Variable binding
<a name="functions-jsonata-binding"></a>

Inside parentheses, use `:=` to name an intermediate value, and semicolons to separate statements. The last statement is the value of the expression. Bound variables exist only within their parentheses.

```
(
  $flagged := media.contextual.shot.garm.suitability.categories[flagged];
  {
    "text": "Flagged: " & $join($flagged.category, ", ") & ". Write a one-line advertiser note."
  }
)
```