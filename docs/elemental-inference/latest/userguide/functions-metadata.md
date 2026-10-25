

# Reading function results
<a name="functions-metadata"></a>

A function writes its result to the feed's metadata timeline under the name of the function output. You read it with the same `GetMetadata` operation that you use for the native features, on the feed's data endpoint. You can find the data endpoint in the `dataEndpoints` field of `GetFeed`.

The following are specific to functions:
+ `parameters` must contain the `function` object. It has no fields, so send `{}`. A request that names a function output with a different `parameters` type is rejected.
+ The result is returned as `metadata.function.value`, a JSON string. Elemental Inference does not impose a schema on it – the content is whatever your response expression produced. Parse it in your application.
+ For a function with a model target, `metadata.function.bedrockRequestId` is the request ID that Amazon Bedrock assigned to the model invocation. Use it to match the result to an entry in your model invocation logs, or include it in a support case about the model's response. A passthrough function invokes no model, so its items have no `bedrockRequestId`.

The following `awscurl` command queries a nine-second window of a function output named `play-description`.

```
# Query one window of function metadata
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST 'https://<{{data-endpoint}}>/v1/feed/<{{feed-id}}>/input/0/metadata' \
  -H "Content-Type: application/json" \
  -d '{"outputName": "play-description", "timeSpecification": { "ptsBased": { "startPts": 168295430000000, "endPts": 168295430810000, "timescale": 90000 }}, "parameters": { "function": {}}}'
```

The response contains one item for each successful run whose window starts in the requested range. The item's `pts` is the start of the window that the function analyzed.

```
{
  "items": [
    {
      "pts": 168295430000000,
      "metadata": {
        "function": {
          "value": "{\"result\":\"A striker breaks past two defenders and shoots from the edge of the box.\"}",
          "bedrockRequestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
      }
    }
  ]
}
```

Note the following about the request and the response.
+ `input/0` is the pipeline index. Use `0` for a single-pipeline source. For a standard-class AWS Elemental MediaLive channel, the second pipeline is `input/1`.
+ `timescale` is conventionally `90000` for live content, where PTS is the epoch time in seconds multiplied by the timescale. A request can cover at most 30 seconds of content.
+ On a live feed, a function result is available at most about 20 seconds after the end of the window it covers. The model invocation times out after about 18 seconds, and a run that doesn't finish in time stores no result. `GetMetadata` waits up to 30 seconds for a result whose window reaches the end of the requested range, then returns `MetadataUnavailableException`. To avoid the wait, query a range that ends at least one trigger window plus 20 seconds behind the live edge.
+ A run that fails stores nothing. If no stored result overlaps the requested range, `GetMetadata` returns `ResourceNotFoundException`. If a stored result overlaps the range but no run started in it, `items` is empty. A `perClip` window with no clips returns no item. See [Troubleshooting functions](functions-troubleshooting.md).
+ If the function has no response expression, `value` holds the entire result of the target – for a model target, the raw model response body.

Elemental Inference retains function metadata for 7 days, as it does for every other output. Disabling the function output stops new runs; results that were already stored remain readable until they age out. After you remove the output from the feed, `GetMetadata` no longer finds it by name. For more information, see [Lifecycle of metadata](monitor-inference-feed-lifecycle.md#monitor-inference-metadata-lifecycle).

**Tip**  
Ask the model for JSON, then use `$parse()` in your response expression, and `value` becomes a structured record instead of a sentence you have to interpret. See [Response expressions](functions-expressions-response.md).