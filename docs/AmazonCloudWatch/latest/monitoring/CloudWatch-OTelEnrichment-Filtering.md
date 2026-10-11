

# Filtering enrichment by namespace and metric
<a name="CloudWatch-OTelEnrichment-Filtering"></a>

CloudWatch OTel enrichment decorates your account's vended metrics with resource ARN and resource tag labels. You can then group and filter by resource attributes in PromQL and Query Studio. By default, enrichment applies to every namespace that CloudWatch supports for enrichment. You can narrow enrichment to a chosen subset of namespaces and metric names by using two optional parameters, `IncludeFilters` and `ExcludeFilters`. You can also change those filters on a running account with the `UpdateOTelEnrichment` operation. Use filtering to optimize enrichment cost when you need only some of your metrics in OTel.

Before you filter enrichment, you must start enrichment for your account. For more information, see [Enabling OpenTelemetry enrichment for vended metrics](CloudWatch-OTelEnrichment.md#CloudWatch-OTelEnrichment-Enable).

**Related**
+ [Enabling OpenTelemetry enrichment for vended metrics](CloudWatch-OTelEnrichment.md#CloudWatch-OTelEnrichment-Enable)
+ [Querying vended AWS metrics with PromQL](CloudWatch-PromQL-Querying.md#CloudWatch-PromQL-Querying-Vended)
+ [Enabling resource tags on telemetry](EnableResourceTagsOnTelemetry.md)

## Operations that set enrichment filters
<a name="CloudWatch-OTelEnrichment-Filtering-Operations"></a>

You set enrichment filters with two operations. Each operation applies to your account and is scoped to a single AWS Region.
+ `StartOTelEnrichment` — Starts enrichment, and optionally sets the initial filters.
+ `UpdateOTelEnrichment` — Replaces the filters of an account that is already running enrichment.

## The metric selector
<a name="CloudWatch-OTelEnrichment-Filtering-Selector"></a>

A metric selector is an `OTelEnrichmentMetricSelector` data type that picks the metrics in exactly one namespace. Both `IncludeFilters` and `ExcludeFilters` are lists of these selectors. A selector has the following members.

`Namespace`  
Type: String. Length: 1–255 characters. This member is required, and it must not start with a colon. CloudWatch matches the namespace exactly and case-sensitively.

`MetricNames`  
Type: list of String. Each name is 1–255 characters, and the list holds 0–100 items. This member is optional. Omit it to match every metric in the namespace.

## How filters are evaluated
<a name="CloudWatch-OTelEnrichment-Filtering-Evaluation"></a>

CloudWatch evaluates `IncludeFilters` and `ExcludeFilters` according to the following rules.
+ **Include first, then exclude** – CloudWatch applies `IncludeFilters` first, then subtracts the `ExcludeFilters` match set from the result. Exclude always takes precedence, so a metric matched by both filters is not enriched.
+ **Empty and absent are equivalent** – An omitted list, a null list, and an empty list (`[]`) mean the same thing everywhere, including `MetricNames` within a selector.
+ **Exact, case-sensitive matching** – CloudWatch matches names exactly and case-sensitively, with no wildcards, prefixes, or normalization. `AWS/EC2` matches only `AWS/EC2`, and `aws/ec2` matches nothing.
+ **An inactive direction is permissive** – When you set no `IncludeFilters`, every supported namespace is in scope. When you set no `ExcludeFilters`, nothing is removed.

The following table shows what gets enriched for each combination of filters.


| `IncludeFilters` | `ExcludeFilters` | What gets enriched | 
| --- | --- | --- | 
| Absent or empty | Absent or empty | Every namespace that CloudWatch supports for enrichment. | 
| Present | Absent or empty | Only what `IncludeFilters` matches. | 
| Absent or empty | Present | Everything supported, minus what `ExcludeFilters` matches. | 
| Present | Present | The `IncludeFilters` match set, minus the `ExcludeFilters` match set. | 

## Example: Enrich a subset of metrics
<a name="CloudWatch-OTelEnrichment-Filtering-Example"></a>

Suppose that you want to enrich all of `AWS/EC2` except two network metrics, plus exactly two `AWS/RDS` metrics, and nothing else. The following filter configuration produces that result.

```
{
  "IncludeFilters": [
    { "Namespace": "AWS/EC2" },
    { "Namespace": "AWS/RDS", "MetricNames": ["CPUUtilization", "DatabaseConnections"] }
  ],
  "ExcludeFilters": [
    { "Namespace": "AWS/EC2", "MetricNames": ["NetworkPacketsIn", "NetworkPacketsOut"] }
  ]
}
```

This configuration produces the following result.
+ Every `AWS/EC2` metric except `NetworkPacketsIn` and `NetworkPacketsOut` is enriched.
+ `AWS/RDS` `CPUUtilization` and `DatabaseConnections` are enriched.
+ Every other `AWS/RDS` metric is not enriched, because `IncludeFilters` did not name it.
+ Every other namespace is not enriched, because `IncludeFilters` is active and does not list it.

This configuration consumes 3 of the 100 available selectors: two include selectors and one exclude selector.

## Starting enrichment on an account that is already running
<a name="CloudWatch-OTelEnrichment-Filtering-StartNoop"></a>

Calling `StartOTelEnrichment` on an account that is already running enrichment is a no-op. It does not return an error, and it does not apply the filters in the request. The stored configuration is unchanged.

The response makes this behavior observable. `StartOTelEnrichment` returns the filters that were already stored, not the filters that the request carried. If you send filters and get different filters back, enrichment was already running, and the filters you sent were discarded.

To change filters on a running account, use `UpdateOTelEnrichment`. Do not stop and restart enrichment to change filters, because a restart resets `CreatedAt` and creates an enrichment gap.

## Updating filters
<a name="CloudWatch-OTelEnrichment-Filtering-Update"></a>

`UpdateOTelEnrichment` replaces filters. It does not merge them. `IncludeFilters` and `ExcludeFilters` move as a pair, so whatever the request omits is cleared. The following table shows the effect of each request shape on the stored configuration.


| Request | Effect on stored configuration | 
| --- | --- | 
| Both specified | Both are replaced. | 
| Only `IncludeFilters` | `IncludeFilters` is replaced, and `ExcludeFilters` is cleared. | 
| Only `ExcludeFilters` | `ExcludeFilters` is replaced, and `IncludeFilters` is cleared. | 
| Neither specified | Both are cleared, and enrichment reverts to every supported namespace. | 

The last write wins. There is no read-modify-write helper, so to add one selector you send the full intended list. If you do not already track the current state, read it with `GetOTelEnrichment` first.

`UpdateOTelEnrichment` requires enrichment to already be running. Against a stopped account, it returns `ResourceNotFoundException` (HTTP 404), so start enrichment first.

## Timestamps
<a name="CloudWatch-OTelEnrichment-Filtering-Timestamps"></a>

`GetOTelEnrichment` returns `CreatedAt` and `UpdatedAt`.
+ After `StartOTelEnrichment` starts enrichment on an account that isn't already running it, `CreatedAt` is set to the current time, and `UpdatedAt` equals `CreatedAt`. On an account that is already running enrichment, `StartOTelEnrichment` is a no-op and leaves both timestamps unchanged.
+ After `UpdateOTelEnrichment`, `CreatedAt` is unchanged, and `UpdatedAt` is set to the current time.

An `UpdatedAt` value that is greater than `CreatedAt` indicates that the filters have changed at least once since enrichment started.

## Reading enrichment state
<a name="CloudWatch-OTelEnrichment-Filtering-Reading"></a>

`GetOTelEnrichment` returns `Status` (`Running` or `Stopped`) plus the filters and timestamps. Every member below `Status` is omitted when enrichment is stopped.

When enrichment is running, an omitted `IncludeFilters` is not unknown. It means that no include direction is stored, so every supported namespace is in scope. Likewise, an omitted `ExcludeFilters` means that nothing is excluded. Treat an absent filter as the permissive case, never as an error.

## Limits
<a name="CloudWatch-OTelEnrichment-Filtering-Limits"></a>

The following table lists the limits for enrichment filters.


| Limit | Value | Enforced by | 
| --- | --- | --- | 
| Selectors across `IncludeFilters` and `ExcludeFilters` combined | 100 | Service (the binding limit) | 
| Selectors per individual list | 100 | Model length backstop | 
| Metric names per selector | 100 | Model length | 
| Namespace length | 1–255 characters, must not begin with a colon | Model | 
| `MetricName` length | 1–255 characters | Model | 

The combined cap is the limit that rejects requests. Two lists of 60 selectors each satisfy the per-list limit of 100, but they sum to 120 and fail with `ValidationException`.

## Errors
<a name="CloudWatch-OTelEnrichment-Filtering-Errors"></a>

The following table lists the errors that each operation can return.


| Operation | Errors | 
| --- | --- | 
| `StartOTelEnrichment` | `ValidationException` | 
| `UpdateOTelEnrichment` | `ValidationException`, `ResourceNotFoundException` | 
| `GetOTelEnrichment` | None | 
| `StopOTelEnrichment` | None | 

`ValidationException` covers malformed namespaces, over-long names, and exceeding the combined-selector cap. `ResourceNotFoundException` on `UpdateOTelEnrichment` means exactly one thing: enrichment is not running for this account. The framework raises throttling, internal, and access-denied errors. They are not modeled on these operations, and you handle them as you do for any other CloudWatch call.

## Managing filters with the AWS CLI
<a name="CloudWatch-OTelEnrichment-Filtering-CLI"></a>

To start enrichment with initial filters, run the following command.

```
aws cloudwatch start-otel-enrichment \
    --include-filters '[{"Namespace":"AWS/EC2"},{"Namespace":"AWS/RDS","MetricNames":["CPUUtilization"]}]' \
    --exclude-filters '[{"Namespace":"AWS/EC2","MetricNames":["NetworkPacketsIn"]}]'
```

To read the current state, run the following command.

```
aws cloudwatch get-otel-enrichment
```

To replace the filters, run the following command. This command clears anything that you omit.

```
aws cloudwatch update-otel-enrichment \
    --include-filters '[{"Namespace":"AWS/EC2"},{"Namespace":"AWS/Lambda"}]' \
    --exclude-filters '[]'
```

To revert to enriching every supported namespace, run the following command.

```
aws cloudwatch update-otel-enrichment
```

To stop enrichment, run the following command.

```
aws cloudwatch stop-otel-enrichment
```

To verify that a change took effect, read it back and compare `UpdatedAt`.

```
aws cloudwatch get-otel-enrichment --query '{S:Status,U:UpdatedAt,I:IncludeFilters,E:ExcludeFilters}'
```

## Best practices
<a name="CloudWatch-OTelEnrichment-Filtering-BestPractices"></a>

We recommend the following practices when you filter enrichment.
+ Start enrichment once, then use `UpdateOTelEnrichment` to change filters. Never restart to change filters.
+ Send the complete intended filter set on every update, because omission clears.
+ Copy namespace names exactly from `ListMetrics` output. Matching is case-sensitive with no wildcards.
+ Budget selectors against the combined limit of 100, not 100 per list.
+ Read absent filters as permissive, not as missing data.
+ Confirm writes from the response rather than the request that you sent. On the `StartOTelEnrichment` no-op path they differ, and that difference is the signal.