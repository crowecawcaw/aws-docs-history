

# CloudWatch Metrics (OTel)
<a name="metrics-pipeline-selection-criteria"></a>

Selection criteria determine which OTel metrics enter a pipeline for processing. Each criterion is an expression of the form `<path> == "<value>"` that matches against a specific attribute of the incoming metric. At least one selection criterion is required.

Criteria are grouped inside a `match_all` block with AND semantics — a metric must match every expression in the group to enter the pipeline.

## Supported paths
<a name="selection-criteria-paths"></a>

The following OTTL paths are supported in selection criteria:


| Path | Description | 
| --- | --- | 
| `resource.attributes["key"]` | Resource-level attribute | 
| `instrumentation_scope.name` | Instrumentation scope name | 
| `instrumentation_scope.version` | Instrumentation scope version | 
| `instrumentation_scope.attributes["key"]` | Instrumentation scope attribute | 
| `metric.name` | Metric name | 
| `datapoint.attributes["key"]` | Datapoint-level attribute | 
| `attributes["key"]` | Short form for `datapoint.attributes["key"]` | 

## Configuration
<a name="selection-criteria-configuration"></a>

Selection criteria are defined in the `source` section of the pipeline configuration:

```
pipeline:
  source:
    cloudwatch_metrics:
      format: otlp
      selection_criteria:
        - match_all:
            - 'resource.attributes["service.name"] == "my-service"'
            - 'metric.name == "http.server.request.duration"'
  processor:
    - add_attributes:
        attributes:
          - key: resource.attributes["team"]
            value: "platform-engineering"
  sink:
    - cloudwatch_metrics: {}
```

The following example uses all supported path types:

```
pipeline:
  source:
    cloudwatch_metrics:
      format: otlp
      selection_criteria:
        - match_all:
            - 'resource.attributes["service.name"] == "my-service"'
            - 'instrumentation_scope.name == "my-scope"'
            - 'instrumentation_scope.version == "1.0.0"'
            - 'instrumentation_scope.attributes["library"] == "otel-java"'
            - 'metric.name == "http.server.request.duration"'
            - 'datapoint.attributes["status_code"] == "200"'
            - 'attributes["environment"] == "production"'
  processor:
    - add_attributes:
        attributes:
          - key: resource.attributes["team"]
            value: "observability"
  sink:
    - cloudwatch_metrics: {}
```

## Verifying with PromQL
<a name="selection-criteria-promql"></a>

CloudWatch maps OTLP attribute scopes to PromQL labels using the `@` prefix convention. Use this mapping to verify that your pipeline is processing metrics as expected in Query Studio:


| Pipeline OTTL path | PromQL label prefix | Example | 
| --- | --- | --- | 
| `resource.attributes["key"]` | `@resource.` | `@resource.service.name` | 
| `instrumentation_scope.name` | `@instrumentation.@name` | `@instrumentation.@name` | 
| `instrumentation_scope.attributes["key"]` | `@instrumentation.` | `@instrumentation.library` | 
| `datapoint.attributes["key"]` / `attributes["key"]` | `@datapoint.` or bare | `status_code` | 

For example, if your pipeline adds `resource.attributes["team"]` with value `"platform-engineering"`, you can confirm it was applied:

```
{"CPUUtilization", "@resource.team"="platform-engineering"}
```

## Requirements and limitations
<a name="selection-criteria-requirements"></a>

Single `match_all` group  
Each pipeline supports exactly one `match_all` group in `selection_criteria`. You cannot define multiple `match_all` groups in a single pipeline.

Minimum criteria  
At least one expression is required in the `match_all` group.

Maximum criteria  
A `match_all` group can contain at most 20 expressions.

AND semantics  
All expressions in the `match_all` group must match for a metric to enter the pipeline.

Exact string matching  
Values must be static strings. Wildcards, regular expressions, and partial matches are not supported. Each expression must use the `==` operator.

No overlapping criteria across pipelines  
Each metric datapoint must match at most one pipeline. If a datapoint matches both new and existing pipeline criteria, pipeline creation fails. To prevent overlap, include at least one attribute path with distinct values in each pipeline's selection criteria.  
For example, the following two selection criteria overlap because Pipeline A selects all metrics from `payment-service`, which includes the specific metric that Pipeline B targets:  

```
# Pipeline A — selects ALL metrics from payment-service
selection_criteria:
  - match_all:
      - 'resource.attributes["service.name"] == "payment-service"'

# Pipeline B — FAILS: a datapoint with service.name="payment-service"
# and metric.name="http.server.request.duration" matches both pipelines
selection_criteria:
  - match_all:
      - 'metric.name == "http.server.request.duration"'
```