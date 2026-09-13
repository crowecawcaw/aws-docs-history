

# Example 3: Contextual metadata
<a name="monetization-functions-examples-contextual-metadata"></a>

This section provides JSONata expressions for common patterns when working with Elemental Inference `GetMetadata` responses. Use these in the `Output` block of your `AWS_SERVICE_REQUEST` function.

**Note**  
`GetMetadata` returns an `items` array where each item represents an analyzed shot with IAB taxonomy categories and GARM brand safety assessments. When your query time window spans multiple shots, the response includes multiple items. The expressions in the following sections handle this by aggregating across all shots.  
For the complete Elemental Inference `GetMetadata` response schema, see the Elemental Inference API reference.

## Build the query time window
<a name="monetization-functions-examples-contextual-metadata-timewindow"></a>

Use the following expression for the `Body` field of your `AWS_SERVICE_REQUEST` function:

```
{%'{"outputName": "my-contextual-output", "timeSpecification": {"ptsBased": {"startPts": ' & $string(($exists(inference.previousBreakEndPts) and inference.previousBreakEndPts > inference.pts - 30 * inference.timescale ? inference.previousBreakEndPts : inference.pts - 30 * inference.timescale)) & ', "endPts": ' & $string(inference.pts + 1) & ', "timescale": ' & $string(inference.timescale) & '}}, "parameters": {"contextualMetadata": {}}}' %}
```

This expression selects the more recent of `inference.previousBreakEndPts` and a 30-second lookback, ensuring the query window never exceeds 30 seconds. If `inference.previousBreakEndPts` is unavailable (for example, the first ad break), the expression defaults to the 30-second lookback.

**Note**  
Replace `my-contextual-output` with the name of your Elemental Inference feed's contextual metadata output.

## Extract IAB category IDs
<a name="monetization-functions-examples-contextual-metadata-iab-ids"></a>

```
{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.uniqueId), ',') : ''%}
```

Result: `"641,645,324"` — IAB Content Taxonomy unique IDs, suitable for passing as a query parameter (for example, `iab_cats=641,645,324`).

## Extract IAB category paths
<a name="monetization-functions-examples-contextual-metadata-iab-paths"></a>

```
{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.($join(path, ' > '))), '|') : ''%}
```

Result: `"Genres > Animation & Anime|Genres > Family/Children|Entertainment > Movies"` — human-readable taxonomy paths.

## Extract flagged GARM categories
<a name="monetization-functions-examples-contextual-metadata-garm-flagged"></a>

```
{%response.statusCode = 200 ? $join($distinct(response.body.items.metadata.contextualMetadata.garm.suitability.categories[flagged = true].category), ',') : ''%}
```

Result: `"ILLEGAL_DRUGS_TOBACCO_ALCOHOL"` — categories to exclude from ad targeting or to signal brand safety concerns to your ad decision server.

## Determine highest GARM risk level
<a name="monetization-functions-examples-contextual-metadata-garm-risk"></a>

```
{%response.statusCode = 200 and $exists(response.body.items) ? ($names := ['NONE','LOW','MEDIUM','HIGH']; $flagged := response.body.items.metadata.contextualMetadata.garm.suitability.categories[flagged = true].risk; $scores := $map($flagged, function($r){ $r = 'HIGH' ? 3 : $r = 'MEDIUM' ? 2 : $r = 'LOW' ? 1 : 0 }); $count($scores) > 0 ? $names[$max($scores)] : 'NONE') : ''%}
```

Result: `"MEDIUM"` — the worst-case risk level across all analyzed shots and GARM categories. Returns an empty string if the request fails or the response body is missing, so that missing data is not reported as `NONE`.

## Check brand safety
<a name="monetization-functions-examples-contextual-metadata-brand-safe"></a>

```
{%response.statusCode = 200 and $exists(response.body.items) ? $string($not($exists(response.body.items.metadata.contextualMetadata.garm.suitability.categories[flagged = true]))) : ''%}
```

Result: `"false"` if any GARM category is flagged, `"true"` if content is brand-safe. Returns an empty string if the request fails or the response body is missing.

**Important**  
The `$exists(response.body.items)` guard is required. A response can return status code 200 while `response.body` is `null` — for example, when the body exceeds 20,000 characters or is not valid JSON. Without the guard, the expression returns `"true"` and reports the content as brand-safe even though the GARM classifications were never received.

## Combined contextual signal
<a name="monetization-functions-examples-contextual-metadata-combined"></a>

```
{%response.statusCode = 200 ? $string({'categories': $distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.($join(path, ' > '))), 'category_ids': $distinct(response.body.items.metadata.contextualMetadata.iabTaxonomy.categories.uniqueId), 'garm_flagged': $distinct(response.body.items.metadata.contextualMetadata.garm.suitability.categories[flagged = true].category)}) : ''%}
```

Result: A JSON string combining all contextual signals into a single structured payload.

## Per-shot detail
<a name="monetization-functions-examples-contextual-metadata-per-shot"></a>

```
{%response.statusCode = 200 ? $string(response.body.items.{'pts': pts, 'categories': metadata.contextualMetadata.iabTaxonomy.categories.($join(path, ' > ')), 'garm_flagged': metadata.contextualMetadata.garm.suitability.categories[flagged = true].category}) : ''%}
```

Result: Array of per-shot objects preserving which content at which PTS triggered which classifications. Use when your ad decisioning logic needs temporal granularity.

## Tips and best practices
<a name="monetization-functions-examples-contextual-metadata-tips"></a>

Use the following tips when building output expressions for Elemental Inference responses.
+ Always check `response.statusCode` before processing the body. If the call fails, `response.body` is `null`.
+ Use `$distinct()` to deduplicate categories across multiple shots.
+ Elemental Inference returns multiple IAB categories per shot and a set of GARM brand safety categories. For current limits, see the Elemental Inference documentation.
+ When the time window spans multiple shots, the response contains multiple items in the `items` array.
+ The maximum response size is 20,000 characters. If you receive truncated responses, reduce the time window.
+ Use `temp.*` output keys when chaining with other functions in a `SEQUENTIAL_EXECUTOR`, and `player_params.*` when passing values directly to the ad decision server URL.
+ For the complete list of supported JSONata functions and operators, see [JSONata expression reference for Functions](monetization-functions-jsonata.md).

For the complete setup guide including prerequisites and resource policies, see [Elemental Inference integration](monetization-functions-elemental-inference-integration.md). For the function type reference, see [AWS service request](monetization-functions-types-aws-service-request.md).